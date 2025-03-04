# Analyzing images and videos with AI

*NICAR 2025, Minneapolis*

Jonathan Soma, Knight Chair in Data Journalism at Columbia Journalism School

[jonathan.soma@gmail.com](mailto:jonathan.soma@gmail.com) / [Twitter](https://x.com/dangerscarf) / [Bluesky](https://bsky.app/profile/dangerscarf.bsky.social) / [jonathansoma.com](https://jonathansoma.com)

## Setup and installation

We're doing this on macOS, so I'm telling you setup instructions for macOS! First, you'll need to install [Homebrew](https://brew.sh/), then **ffmpeg** for video processing.

```
brew install ffmpeg
```

Then you'll need to create and activate a **virtual environment** and install the requirements.

```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

You should also run the following command to make this environment available in Jupyter notebook (you'll need to have installed Jupyter separately).

```
python -m ipykernel install --user --name="images-video-ai" --display-name="AI with images and video"
```

### Testing setup and caching materials

The following command will confirm that the install worked, while also caching some of the (rather large) AI models we'll be using.

```
source env/bin/activate
python test/cache-test.py
```