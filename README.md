# Analyzing images and videos with AI

*NICAR 2025, Minneapolis*

Jonathan Soma, Knight Chair in Data Journalism at Columbia Journalism School

[jonathan.soma@gmail.com](mailto:jonathan.soma@gmail.com) / [Twitter](https://x.com/dangerscarf) / [Bluesky](https://bsky.app/profile/dangerscarf.bsky.social) / [jonathansoma.com](https://jonathansoma.com)

## Using this on the cloud

[Visit Google Colab here](https://colab.research.google.com/github/jsoma/nicar25-ai-images-video)

## Setup and installation

### Normal human setup

Various Pythons may or may not work for this – I use 3.10 or 3.11, not exactly sure about more recent ones.

### NICAR setup
I'm providing this just for setup on the NICAR computers right now. SORRY!!

```
brew install ffmpeg
brew install pyenv
mkdir -p ~/Desktop/hands_on_classes/20250307-friday-analyzing-images-and-videos-with-ai
cd ~/Desktop/hands_on_classes/20250307-friday-analyzing-images-and-videos-with-ai
pyenv install "3.11"
pyenv local "3.11"
PYENV_VERSION=3.11 pyenv exec python -m venv env
source env/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name="images-video-ai" --display-name="AI for Images and Video"
python test/test-cache.py
```

Also, download [Msty](https://msty.app/) and then open it up and click 'setup local AI' (or 'continue' down at the bottom if there are any ollama models around).