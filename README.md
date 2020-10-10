# Anime Web Scraper
Download images of anime's episode previews from official and news websites.

## Introduction
The Anime Web Scraper downloads images of previews of episodes from official websites. The program is written in Python 3.

Click [here](https://youtu.be/K-83J5aZ5P0) to see the demo on YouTube.

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

## Websites
<details>
<summary>Here are the some of the websites that are scraped (click to expand):</summary>

### News Website
* [Aniverse Magazine](https://aniverse-mag.com/)
* [Moca News](https://moca-news.net/)
* [WebNewtype](https://webnewtype.com/)

### New Anime
* [Cheat Kusushi no Slow Life: Isekai ni Tsukurou Drugstore](https://www.cheat-kusushi.jp/)
* [Ijiranaide, Nagatoro-san](https://www.nagatorosan.jp/)
* [Kaifuku Jutsushi no Yarinaoshi](http://kaiyari.com/)
* [Mushoku Tensei: Isekai Ittara Honki Dasu](https://mushokutensei.jp/)
* [Ore dake Haireru Kakushi Dungeon](https://kakushidungeon-anime.jp/)

### Fall 2020 Anime
* [100-man no Inochi no Ue ni Ore wa Tatteiru](http://1000000-lives.com/)
* [Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka III](http://danmachi.com/danmachi3/)
* [Gochuumon wa Usagi Desu ka? Bloom](https://gochiusa.com/bloom/)
* [Higurashi no Naku Koro ni (2020)](https://higurashianime.com/)
* [Iwa Kakeru!: Sport Climbing Girls](http://iwakakeru-anime.com/)
* [Kamisama ni Natta Hi](https://kamisama-day.jp/)
* [Kami-tachi ni Hirowareta Otoko](https://kamihiro-anime.com/)
* [Kimi to Boku no Saigo no Senjou, Aruiwa Sekai ga Hajimaru Seisen](https://kimisentv.com/)
* [Kuma Kuma Kuma Bear](https://kumakumakumabear.com/)
* [Maesetsu!](https://maesetsu.jp/)
* [Mahouka Koukou no Rettousei: Raihousha-hen](https://mahouka.jp/)
* [Majo no Tabitabi](https://majotabi.jp/)
* [Maou-jou de Oyasumi](https://maoujo-anime.com/)
* [Ochikobore Fruit Tart](http://ochifuru-anime.com/)
* [Rail Romanesque](https://railromanesque.jp/)
* [Senyoku no Sigrdrifa](https://sigururi.com/)
* [Tatoeba Last Dungeon Mae no Mura no Shounen ga Joban no Machi de Kurasu Youna Monogatari](https://lasdan.com/)
* [Tonikaku Kawaii](http://tonikawa.com/)

### Summer 2020 Anime
* [Dokyuu Hentai HxEros](https://hxeros.com/)
* [Kanojo, Okarishimasu](https://kanokari-official.com/)
* [Maou Gakuin no Futekigousha: Shijou Saikyou no Maou no Shiso, Tensei shite Shison-tachi no Gakkou e](https://maohgakuin.com/)
* [Monster Musume no Oishasan](https://mon-isha-anime.com/)
* [Peter Grill to Kenja no Jikan](http://petergrill-anime.jp/)
* [Re:Zero kara Hajimeru Isekai Seikatsu 2nd Season](http://re-zero-anime.jp/tv/)
* [Uzaki-chan wa Asobitai!](https://uzakichan.com/)
* [Yahari Ore no Seishun Love Comedy wa Machigatteiru. Kan](http://www.tbs.co.jp/anime/oregairu/)

### Spring 2020 Anime
* [Arte](http://arte-anime.com/)
* [Brand New Animal](https://bna-anime.com/)
* [Gleipnir](http://gleipnir-anime.com)
* [Hachi-nan tte, Sore wa Nai deshou!](http://hachinan-anime.com/)
* [Honzuki no Gekokujou: Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen 2nd Season](http://booklove-anime.jp/)
* [Houkago Teibou Nisshi](https://teibotv.com/)
* [Kaguya-sama wa Kokurasetai? Tensai-tachi no Renai Zunousen](https://kaguya.love/)
* [Kakushigoto](https://kakushigoto-anime.com/)
* [Kingdom 3rd Season](https://kingdom-anime.com/)
* [Otome Game no Hametsu Flag shika Nai Akuyaku Reijou ni Tensei shiteshimatta...](https://hamehura-anime.com/)
* [Nami yo Kiitekure](https://namiyo-anime.com/)
* [Princess Connect! Re:Dive](https://anime.priconne-redive.jp)
* [Shachou, Battle no Jikan Desu!](https://shachibato-anime.com/)
* [Tamayomi](https://tamayomi.com)
* [Tsugu Tsugumomo](http://tsugumomo.com/)
* [Yesterday wo Utatte](https://singyesterday.com/)

### Winter 2020 Anime
* [Darwin's Game](https://darwins-game.com/)
* [Eizouken ni wa Te wo Dasu na!](http://eizouken-anime.com)
* [Hatena Illusion](http://hatenaillusion-anime.com/)
* [Heya Camp](https://yurucamp.jp/heyacamp/)
* [Infinite Dendrogram](http://dendro-anime.jp/)
* [Isekai Quartet 2](http://isekai-quartet.com/)
* [Ishuzoku Reviewers](https://isyuzoku.com/)
* [Itai no wa Iya nano de Bougyoryoku ni Kyokufuri Shitai to Omoimasu.](https://bofuri.jp/)
* [Jibaku Shounen Hanako-kun](https://www.tbs.co.jp/anime/hanakokun/)
* [Koisuru Asteroid](http://koiastv.com/)
* [Kyokou Suiri](https://kyokousuiri.jp/)
* [Murenase! Seton Gakuen](https://anime-seton.jp/)
* [Nekopara](https://nekopara-anime.com/ja/)
* [Oshi ga Budoukan Ittekuretara Shinu](https://oshibudo.com/)
* [Plunderer](http://plunderer-info.com/)
* [Rikei ga Koi ni Ochita no de Shoumei shitemita.](https://rikekoi.com)
* [Runway de Waratte](https://runway-anime.com/)
* [Somali to Mori no Kamisama](https://somali-anime.com/)
* [Toaru Kagaku no Railgun T](https://toaru-project.com/railgun_t/)
</details>
