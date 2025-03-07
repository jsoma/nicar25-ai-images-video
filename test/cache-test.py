## yt-dlp test

print("Testing yt-dlp")
import subprocess
from yt_dlp import YoutubeDL

result = subprocess.call("""
yt-dlp -f 'bestvideo[height<=720]+bestaudio' "https://www.youtube.com/watch?v=rDXubdQdJYs"
""", shell=True)
if result != 0:
    raise RuntimeError(f"Command failed with return code {result}")

print("Done")

## Audio test

print("Testing audio transcribing")

import whisperx
import torch
from pathlib import Path

# audio_path = Path(__file__).parent.joinpath("audio.m4a")

# device = "cuda" if torch.cuda.is_available() else "cpu"
# batch_size = 16 if device == "cuda" else 8
# compute_type = "float16" if device == "cuda" else "float32" 

model = whisperx.load_model("tiny.en", "cpu"/)

# audio = whisperx.load_audio(audio_path.absolute())
# result = model.transcribe(audio, batch_size=batch_size)
# model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=device)
# result = whisperx.align(result["segments"], model_a, metadata, audio, device, return_char_alignments=False)

print("Done")

## Scene detection test

print("Testing scene detection")

import subprocess

video_path = Path(__file__).parent.joinpath("rDXubdQdJYs.webm")

result = subprocess.call(f"""
scenedetect -i "{video_path}" \
    detect-content \
    save-images --output debate --width 300 --num-images 5 \
    export-html --image-width 300 \
    list-scenes --skip-cuts
""", shell=True)
if result != 0:
    raise RuntimeError(f"Command failed with return code {result}")

print("Done")

## Transformers test

print("Testing transformers zero-shot image pipeline")

from transformers import pipeline
from PIL import Image

photo_path = Path(__file__).parent.joinpath("photo.jpg")

image = Image.open(photo_path)

detector = pipeline("zero-shot-image-classification", model="openai/clip-vit-large-patch14") 
results = detector(image, candidate_labels=["donald trump", "joe biden"])
print("Done")

## YOLO test

print("Testing roboflow inference")

import os
import cv2
import supervision as sv
from inference import get_model

model = get_model("yolov10n-640")

video_path = Path(__file__).parent.joinpath("istockphoto-534232220-640_adpp_is.mp4")
frame_generator = sv.get_video_frames_generator(video_path)

box_annotator = sv.BoxAnnotator()
label_annotator = sv.LabelAnnotator()
line_zone_annotator = sv.LineZoneAnnotator(text_thickness=1)

byte_track = sv.ByteTrack()
byte_track.reset()

start = sv.Point(200, 175)
end = sv.Point(700, 175)
line_zone = sv.LineZone(start, end)
trace_annotator = sv.TraceAnnotator()
smoother = sv.DetectionsSmoother()

for frame in frame_generator:
    result = model.infer(frame, confidence=0.3)[0]
    detections = sv.Detections.from_inference(result)
    detections = byte_track.update_with_detections(detections)
    detections = smoother.update_with_detections(detections)

    line_zone.trigger(detections)

    annotated_frame = frame.copy()

    labels = [
        f"#{tracker_id} {model.class_names[class_id]} {confidence:0.2f}"
        for _, _, confidence, class_id, tracker_id, _
        in detections
    ]

    annotated_frame = box_annotator.annotate(annotated_frame, detections)
    annotated_frame = trace_annotator.annotate(annotated_frame, detections)

    annotated_frame = label_annotator.annotate(
        scene=annotated_frame,
        detections=detections,
        labels=labels)

    annotated_frame = line_zone_annotator.annotate(
        annotated_frame,
        line_counter=line_zone)
    break

print("Done")

print("SUCCESS!!!")