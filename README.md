# Anime Web Scraper
Download images of anime's episode previews from official and news websites

## Introduction
The Anime Web Scraper downloads images of previews of episodes from official websites. The program is written in Python 3.

## Setting Up
1. Download and install the latest version of [Python](https://www.python.org/downloads/)
2. When installing Python, make sure to check 'Add Python 3.X to PATH':\
![win_installer.png](/images/win_installer.png)
3. Open the Command Prompt (for Windows) or Terminal (for MacOS).
4. Run the following commands:
```
pip install requests
pip install bs4
pip install pillow
```

## Running the Program
1. Using the Command Prompt (Terminal for MacOS), change to the directory to where the file `program.py` is located.
2. Run the following command: `python program.py`
3. Select the filtering method to search for anime to be selected by entering the number. Enter '0' to exit.\
![example4.png](/images/example4.png)
    1. Filter by Keyword
        1. Enter the keyword to find matching anime. To list all anime available, just press 'Enter' without specifying any keyword.
        2. If a match is found, select the anime by choosing the number(s) beside the anime title.\
        ![example5.png](/images/example5.png)
        3. You can specify which anime to select using the following number format:
            1. Input `3` to select the 3rd anime.
            2. Input `2-5` to select the 2nd to the 5th anime (2nd, 3rd, 4th and 5th)
            3. Input `5,8` to select the 5th and 8th anime.
            4. Input `2-5,7,9-11` to select the 2nd, 3rd, 4th, 5th, 7th, 9th, 10th and 11th anime
            5. Input `0` or any number higher than the number of anime listed to exit without selecting any anime.
    2. Filter by Season
        1. A list of season available will be shown.\
        ![example5.png](/images/example6.png)
        2. Select the season(s) you want to display the list of anime that airs in the season(s) specified. You can select multiple season(s) using the same number format as mentioned in the Filter by Keyword section.
        3. Once selected, the list of anime will be shown. Select the anime in the same way as described in the Filter by Keyword section.\
        ![example5.png](/images/example8.png)
    3. Filter by Keyword and Season
        1. Refer to the above instructions in Filter by Keyword and Filter by Season sections.
4. The selected anime will be downloaded.\
![example5.png](/images/example7.png)
5. The images will be saved at the folder `download`.\
![example3.jpg](/images/example3.jpg)
