# Analyzing images and videos with AI

*NICAR 2025, Minneapolis*

Jonathan Soma, Knight Chair in Data Journalism at Columbia Journalism School

[jonathan.soma@gmail.com](mailto:jonathan.soma@gmail.com) / [Twitter](https://x.com/dangerscarf) / [Bluesky](https://bsky.app/profile/dangerscarf.bsky.social) / [jonathansoma.com](https://jonathansoma.com)

## Setup and installation

I'm providing this just for setup on the NICAR computers right now. SORRY!!

```
brew install ffmpeg
brew install pyenv
mkdir -p ~/Desktop/hands_on_classes/20250307-friday-analyzing-images-and-videos-with-ai
cd ~/Desktop/hands_on_classes/20250307-friday-analyzing-images-and-videos-with-ai
pyenv install "3.12"
pyenv local "3.12"
PYENV_VERSION=3.12 pyenv exec python -m venv env
source env/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name="ai-newsroom" --display-name="AI Newsroom"
python test/test-cache.py
```
