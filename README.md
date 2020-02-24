# Anime Web Scraper
Download images of anime's episode previews from official and news websites

## Introduction
The Anime Web Scraper downloads images of previews of episodes from official websites. The program is written in Python 3.

## Setting Up
1. Download and install the latest version of [Python](https://www.python.org/downloads/)
2. When installing Python, make sure to check 'Add Python 3.X to PATH':
![win_installer.png](/images/win_installer.png)
3. Open the Command Prompt (for Windows) or Terminal (for MacOS).
4. Run the following commands:
```
pip install requests
pip install bs4
```

## Running the Program
1. Using the Command Prompt (Terminal for MacOS), change to the directory to where the file `run.py` is located.
2. Open `run.py` with a plain text editor (e.g. Notepad) and uncomment (remove the first '#') all the anime you want to download (see picture):
![example1.png](/images/example1.png)
3. Once you uncomment all the anime you wanted to download, save it.
4. Going back to the Command Prompt (or Terminal), run the following command: `python run.py`
![example2.png](/images/example2.png)
5. The images will be saved at the folder `download`.
![example3.jpg](/images/example3.jpg)
