## Installation

First, you'll need to install **ffmpeg** for video processing.

```
brew install ffmpeg
```

Then you'll need to create and activate a virtual environment, then install the requirements.

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