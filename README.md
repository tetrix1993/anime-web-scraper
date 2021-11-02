# Anime Web Scraper
Download images of anime's episode previews from official and news websites.

## Introduction
The Anime Web Scraper is a script that downloads images of previews of episodes from official websites. The scraper also detects and downloads character visuals, Blu-ray cover and bonus illustrations for newer anime (mostly from 2020). The program is written in Python 3.

Click [here](https://youtu.be/K-83J5aZ5P0) to see the demo on YouTube.

## Motivations

The motivations for building the scraper is to download contents quickly for blogging purpose (e.g. posting on Twitter).

## Setting Up
1. Download and install the latest version of [Python](https://www.python.org/downloads/)
2. When installing Python, make sure to check 'Add Python 3.X to PATH':\
![win_installer.png](/images/win_installer.png)
3. Open the Command Prompt (for Windows) or Terminal (for MacOS).
4. Run the following command to install all the packages needed to run the program:
```
pip install -r requirements.txt
```

## Running the Program
1. Using the Command Prompt (Terminal for MacOS), change to the directory to where the file `program.py` is located.
2. Run the following command: `python program.py`
3. Select the filtering method (1, 2, or 3) to search for anime to be selected by entering the number. Enter '0' to exit.\
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

### Other Commands in the Program
1. Option 4 - Identify the season the anime belongs to
    * Similar to Option `1`, filter by keyword, then select the anime to see which season it belongs to.
2. Option 5 - Download from news website
    * Select the news website (Aniverse, MocaNews, Natalie, WebNewtype) to download from.
    * Upon selecting, enter the Article ID to download the images in the article.
    * Examples:
        * Anime Recorder: Article ID is `12345` from `https://anime-recorder.com/tvanime/12345`
        * Aniverse: Article ID is `12345` from `https://aniverse-mag.com/archives/12345`
        * MocaNews: Article ID is `2021010101000a_` from `https://moca-news.net/article/20210101/2021010101000a_/01/`
        * Natalie: Article ID is `12345` from `https://natalie.mu/comic/news/414049`
        * WebNewtype: Article ID is `12345` from `https://webnewtype.com/news/article/12345/`
    * The images will be saved at the folder `download\news\{website}\{article_id}`, where
        * `{website}` is
            * `animerecorder` for Anime Recorder;
            * `aniverse` for Aniverse;
            * `moca` for MocaNews;
            * `natalie` for Natalie; and
            * `wnt` for WebNewtype
        * `{article_id}` is the Article ID.

## Websites
<details>
<summary>Here are the some of the websites that are scraped (click to expand):</summary>

### News Website
* [Anime Recorder](https://anime-recorder.com/)
* [Aniverse Magazine](https://aniverse-mag.com/)
* [Moca News](https://moca-news.net/)
* [Natalie](https://natalie.mu/)
* [WebNewtype](https://webnewtype.com/)

### New Anime
The premiere date for the anime listed here has not been announced.
* [Deaimon](https://deaimon.jp/)
* [Do It Yourself!!](https://diy-anime.com/)
* [Gaikotsu Kishi-sama, Tadaima Isekai e Odekakechuu](https://skeleton-knight.com/)
* [Goblin Slayer 2nd Season](http://www.goblinslayer.jp/)
* [Hataraku Maou-sama! 2nd Season](https://maousama.jp/)
* [Isekai Ojisan](https://isekaiojisan.com/)
* [Isekai Yakkyoku](https://isekai-yakkyoku.jp/)
* [Itai no wa Iya nano de Bougyoryoku ni Kyokufuri Shitai to Omoimasu. 2nd Season](https://bofuri.jp/)
* [Kage no Jitsuryokusha ni Naritakute!](https://shadow-garden.jp/)
* [Kakkou no Iinazuke](https://cuckoos-anime.com/)
* [Koi wa Sekai Seifuku no Ato de](https://koiseka-anime.com/)
* [Kono Healer, Mendokusai](https://kono-healer-anime.com/)
* [Maou Gakuin no Futekigousha: Shijou Saikyou no Maou no Shiso, Tensei shite Shison-tachi no Gakkou e 2nd Season](https://maohgakuin.com/)
* [RPG Fudousan](https://rpg-rs.jp/)
* [Shokei Shoujo no Virgin Road](http://virgin-road.com/)
* [Spy x Family](https://spy-family.net/)
* [Summertime Render](https://summertime-anime.com/)
* [Yama no Susume: Next Summit](https://yamanosusume-ns.com/)

### Summer 2022 Anime
* [Soredemo Ayumu wa Yosetekuru](https://soreayu.com/)

### Spring 2022 Anime
* [Aharen-san wa Hakarenai](https://aharen-pr.com/)
* [Honzuki no Gekokujou: Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen 3rd Season](http://booklove-anime.jp/)
* [Kaguya-sama wa Kokurasetai: Ultra Romantic](https://kaguya.love/)
* [Kawaii dake ja Nai Shikimori-san](https://shikimori-anime.com/)
* [Mahoutsukai Reimeiki](https://www.tbs.co.jp/anime/reimeiki/)
* [Tate no Yuusha no Nariagari 2nd Season](http://shieldhero-anime.jp)
* [Yuusha, Yamemasu](https://yuuyame.com/)

### Winter 2022 Anime
* [Akebi-chan no Sailor-fuku](https://akebi-chan.jp/)
* [Arifureta Shokugyou de Sekai Saikyou 2nd Season](https://arifureta.com/)
* [Fantasy Bishoujo Juniku Ojisan to](https://fabiniku.com/)
* [Hakozume: Kouban Joshi no Gyakushuu](https://hakozume-anime.com/)
* [Kaijin Kaihatsubu no Kuroitsu-san](https://kuroitsusan-anime.com/)
* [Karakai Jouzu no Takagi-san 3](https://takagi3.me/)
* [Kenja no Deshi wo Nanoru Kenja](https://kendeshi-anime.com/)
* [Leadale no Daichi nite](https://leadale.net/)
* [Mahouka Koukou no Rettousei: Tsuioku-hen](https://mahouka.jp/)
* [Princess Connect! Re:Dive Season 2](https://anime.priconne-redive.jp)
* [Shikkakumon no Saikyou Kenja](https://shikkakumon.com/)
* [Slow Loop](https://slowlooptv.com/)
* [Sono Bisque Doll wa Koi wo Suru](https://bisquedoll-anime.com/)
* [Tensai Ouji no Akaji Kokka Saisei Jutsu: Souda, Baikoku shiyou](https://tensaiouji-anime.com/)

### Fall 2021 Anime
* [Blue Period](https://blue-period.jp/)
* [Deep Insanity: The Lost Child](https://www.jp.square-enix.com/deepinsanity/anime/)
* [Gyakuten Sekai no Denchi Shoujo](https://denchi-project.com/)
* [Isekai Shokudou 2](https://isekai-shokudo2.com/)
* [Kaizoku Oujo](http://fena-pirate-princess.com/)
* [Komi-san wa, Comyushou desu.](https://komisan-official.com/)
* [Mieruko-chan](https://mierukochan.jp/)
* [Muv-Luv Alternative](https://muv-luv-alternative-anime.com/)
* [Ousama Ranking](https://osama-ranking.com/)
* [Platinum End](https://anime-platinumend.com/)
* [Saihate no Paladin](https://farawaypaladin.com/)
* [Sakugan](http://sakugan-anime.com/)
* [Sekai Saikou no Ansatsusha, Isekai Kizoku ni Tensei suru](https://ansatsu-kizoku.jp/)
* [Senpai ga Uzai Kouhai no Hanashi](https://senpaiga-uzai-anime.com/)
* [Shin no Nakama ja Nai to Yuusha no Party wo Oidasareta node, Henkyou de Slow Life suru Koto ni Shimashita](https://shinnonakama.com/)
* [Shinka no Mi: Shiranai Uchi ni Kachigumi Jinsei](https://www.shinkanomi-anime.com/)
* [Shuumatsu no Harem](https://end-harem-anime.com/)
* [Taishou Otome Otogibanashi](http://taisho-otome.com/)
* [takt op.Destiny](https://anime.takt-op.jp/)
* [Tsuki to Laika to Nosferatu](https://tsuki-laika-nosferatu.com/)
* [Yuuki Yuuna wa Yuusha de Aru: Dai Mankai no Shou](https://yuyuyu.tv/season2/)

### Summer 2021 Anime
* [100-man no Inochi no Ue ni Ore wa Tatteiru 2nd Season](https://1000000-lives.com/)
* [Bokutachi no Remake](http://bokurema.com/)
* [Cheat Kusushi no Slow Life: Isekai ni Tsukurou Drugstore](https://www.cheat-kusushi.jp/)
* [Deatte 5-byou de Battle](https://dea5-anime.com/)
* [Genjitsu Shugi Yuusha no Oukoku Saikenki](https://genkoku-anime.com/)
* [Higurashi no Naku Koro ni Sotsu](https://higurashianime.com/)
* [Jahy-sama wa Kujikenai!](https://jahysama-anime.com/)
* [Kanojo mo Kanojo](https://kanokano-anime.com/)
* [Kobayashi-san Chi no Maid Dragon S](https://maidragon.jp/2nd/)
* [Mahouka Koukou no Yuutousei](https://mahouka-yuutousei.jp/)
* [Megami-ryou no Ryoubo-kun.](https://megamiryou.com/)
* [Meikyuu Black Company](https://meikyubc-anime.com/)
* [Otome Game no Hametsu Flag shika Nai Akuyaku Reijou ni Tensei shiteshimatta... X](https://hamehura-anime.com/)
* [Peach Boy Riverside](https://peachboyriverside.com/)
* [Seirei Gensouki](https://seireigensouki.com/)
* [Shinigami Bocchan to Kuro Maid](https://bocchan-anime.com/)
* [Shiroi Suna no Aquatope](https://aquatope-anime.com/)
* [Tantei wa Mou, Shindeiru.](https://tanmoshi-anime.jp/)
* [Tsuki ga Michibiku Isekai Douchuu](https://tsukimichi.com/)

### Spring 2021 Anime
* [86](https://anime-86.com/)
* [Dragon, Ie wo Kau](https://doraie.com/)
* [Fumetsu no Anata e](https://anime-fumetsunoanatae.com/)
* [Hige wo Soru. Soshite Joshikousei wo Hirou.](http://higehiro-anime.com/)
* [Ijiranaide, Nagatoro-san](https://www.nagatorosan.jp/)
* [Isekai Maou to Shoukan Shoujo no Dorei Majutsu Ω](https://isekaimaou-anime.com/)
* [Kyuukyoku Shinka Shita Full Dive RPG ga Genjitsu Yori mo Kusogee Dattara](https://fulldive-rpg.com/)
* [Mairimashita! Iruma-kun 2nd Season](https://www.nhk.jp/p/iruma2/ts/Q8ZL6MQQ4Y/)
* [Odd Taxi](https://oddtaxi.jp/)
* [Osananajimi ga Zettai ni Makenai Love Comedy](https://osamake.com/)
* [Sayonara Watashi no Cramer](https://sayonara-cramer.com/tv/)
* [Seijo no Maryoku wa Bannou Desu](https://seijyonomaryoku.jp/)
* [Sentouin, Hakenshimasu!](https://kisaragi-co.jp/)
* [Shadows House](https://shadowshouse-anime.com/)
* [Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita](https://slime300-anime.com/)
* [SSSS.Dynazenon](https://dynazenon.net/)
* [Super Cub](https://supercub-anime.com/)
* [Vivy: Fluorite Eye's Song](https://vivy-portal.com/)
* [Yakunara Mug Cup mo](https://yakumo-project.com/)

### Winter 2021 Anime
* [Dr. Stone: Stone Wars](https://dr-stone.jp/)
* [Gotoubun no Hanayome ∬](https://www.tbs.co.jp/anime/5hanayome/)
* [Hataraku Saibou Black](https://saibou-black.com/)
* [Hataraku Saibou!!](https://hataraku-saibou.com/2nd.html)
* [Horimiya](https://horimiya-anime.com/)
* [Jaku-Chara Tomozaki-kun](http://tomozaki-koushiki.com/)
* [Kaifuku Jutsushi no Yarinaoshi](http://kaiyari.com/)
* [Kemono Jihen](https://kemonojihen-anime.com/)
* [Kumo Desu ga, Nani ka?](https://kumo-anime.com/)
* [Mushoku Tensei: Isekai Ittara Honki Dasu](https://mushokutensei.jp/)
* [Non Non Biyori Nonstop](https://nonnontv.com)
* [Ore dake Haireru Kakushi Dungeon](https://kakushidungeon-anime.jp/)
* [Tatoeba Last Dungeon Mae no Mura no Shounen ga Joban no Machi de Kurasu Youna Monogatari](https://lasdan.com/)
* [Tensei shitara Slime Datta Ken 2nd Season](https://www.ten-sura.com/anime/tensura)
* [Urasekai Picnic](https://www.othersidepicnic.com)
* [Wonder Egg Priority](https://wonder-egg-priority.com/)
* [World Trigger 2nd Season](http://www.toei-anim.co.jp/tv/wt/)
* [Yuru Camp△ 2nd Season](https://yurucamp.jp/second/)

### Fall 2020 Anime
* [100-man no Inochi no Ue ni Ore wa Tatteiru](http://1000000-lives.com/)
* [Adachi to Shimamura](https://www.tbs.co.jp/anime/adashima/)
* [Assault Lily: Bouquet](https://anime.assaultlily-pj.com/)
* [Dogeza de Tanondemita](https://dogeza-anime.com/)
* [Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka III](http://danmachi.com/danmachi3/)
* [Golden Kamuy 3rd Season](https://www.kamuy-anime.com/)
* [Gochuumon wa Usagi Desu ka? Bloom](https://gochiusa.com/bloom/)
* [Higurashi no Naku Koro ni Gou](https://higurashianime.com/)
* [Iwa Kakeru!: Sport Climbing Girls](http://iwakakeru-anime.com/)
* [Jujutsu Kaisen](https://jujutsukaisen.jp/)
* [Kamisama ni Natta Hi](https://kamisama-day.jp/)
* [Kami-tachi ni Hirowareta Otoko](https://kamihiro-anime.com/)
* [Kimi to Boku no Saigo no Senjou, Aruiwa Sekai ga Hajimaru Seisen](https://kimisentv.com/)
* [Kuma Kuma Kuma Bear](https://kumakumakumabear.com/)
* [Maesetsu!](https://maesetsu.jp/)
* [Mahouka Koukou no Rettousei: Raihousha-hen](https://mahouka.jp/2nd/)
* [Majo no Tabitabi](https://majotabi.jp/)
* [Maoujou de Oyasumi](https://maoujo-anime.com/)
* [Munou na Nana](https://munounanana.com/)
* [Ochikobore Fruit Tart](http://ochifuru-anime.com/)
* [Rail Romanesque](https://railromanesque.jp/)
* [Senyoku no Sigrdrifa](https://sigururi.com/)
* [Strike Witches: Road to Berlin](http://w-witch.jp/strike_witches-rtb/)
* [Tonikaku Kawaii](http://tonikawa.com/)

### Summer 2020 Anime
* [Deca-Dence](http://decadence-anime.com/)
* [Dokyuu Hentai HxEros](https://hxeros.com/)
* [Kanojo, Okarishimasu](https://kanokari-official.com/)
* [Maou Gakuin no Futekigousha: Shijou Saikyou no Maou no Shiso, Tensei shite Shison-tachi no Gakkou e](https://maohgakuin.com/1st/)
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
* [Kaguya-sama wa Kokurasetai? Tensai-tachi no Renai Zunousen](https://kaguya.love/2nd/)
* [Kakushigoto](https://kakushigoto-anime.com/)
* [Kingdom 3rd Season](https://kingdom-anime.com/)
* [Otome Game no Hametsu Flag shika Nai Akuyaku Reijou ni Tensei shiteshimatta...](https://hamehura-anime.com/1st/)
* [Nami yo Kiitekure](https://namiyo-anime.com/)
* [Princess Connect! Re:Dive](https://anime.priconne-redive.jp/archive/1st/)
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

### Fall 2019 Anime
* [Assassins Pride](https://assassinspride-anime.com/)
* [Bokutachi wa Benkyou ga Dekinai!](https://boku-ben.com/story/2nd/)
* [Choujin Koukousei-tachi wa Isekai demo Yoyuu de Ikinuku you desu!](http://choyoyu.com)
* [Hataage! Kemonomichi](http://hataage-kemonomichi.com)
* [High Score Girl II](http://hi-score-girl.com)
* [Honzuki no Gekokujou: Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen](http://booklove-anime.jp)
* [Houkago Saikoro Club](http://saikoro-club.com)
* [Kandagawa Jet Girls](http://kjganime.com/)
* [Mairimashita! Iruma-kun](https://www6.nhk.or.jp/anime/program/detail.html?i=iruma)
* [Null Peta](https://nullpeta.com/)
* [Ore wo Suki nano wa Omae dake ka yo](https://ore.ski/)
* [Rifle is Beautiful](https://chidori-high-school.com/)
* [Shinchou Yuusha: Kono Yuusha ga Ore Tueee Kuse ni Shinchou Sugiru](http://shincho-yusha.jp)
* [Val x Love](https://val-love.com/)
* [Watashi, Nouryoku wa Heikinchi de tte Itta yo ne!](https://noukin-anime.com/)

### Summer 2019 Anime
* [Arifureta Shokugyou de Sekai Saikyou](https://arifureta.com/)
* [Dr. Stone](https://dr-stone.jp/)
* [Dumbbell Nan Kilo Moteru?](https://dumbbell-anime.jp/)
* [Granbelm](http://granbelm.com/)
* [Kawaikereba Hentai demo Suki ni Natte Kuremasu ka?](https://hensuki.com/)
* [Isekai Cheat Magician](http://isekai-cheat-magician.com/)
* [Joshikousei no Mudazukai](http://jyoshimuda.com)
* [Kanata no Astra](http://astra-anime.com/)
* [Machikado Mazoku](http://www.tbs.co.jp/anime/machikado/)
* [Tsuujou Kougeki ga Zentai Kougeki de Ni-kai Kougeki no Okaasan wa Suki Desu ka?](https://okaasan-online.com/)
* [Sounan Desu ka?](http://sounandesuka.jp/)
* [Tejina-senpai](http://www.tejina-senpai.jp/)
* [Uchi no Ko no Tame naraba, Ore wa Moshikashitara Maou mo Taoseru kamo Shirenai.](http://uchinoko-anime.com/)

### Spring 2019 Anime
* [Bokutachi wa Benkyou ga Dekinai](https://boku-ben.com/)
* [Choukadou Girl 1/6](http://choukadou-anime.com/)
* [Hachigatsu no Cinderella Nine](https://anime-hachinai.com/)
* [Hangyakusei Million Arthur 2nd Season](http://hangyakusei-anime.com/)
* [Hitoribocchi no Marumaru Seikatsu](http://hitoribocchi.jp)
* [Isekai Quartet](http://isekai-quartet.com/)
* [Kenja no Mago](http://kenja-no-mago.jp/)
* [Kono Yo no Hate de Koi wo Utau Shoujo YU-NO](http://yuno-anime.com/)
* [Midara na Ao-chan wa Benkyou ga Dekinai](http://aochan-anime.com/)
* [Nande Koko ni Sensei ga!?](http://nankoko-anime.com/)
* [Nobunaga-sensei no Osanazuma](http://nobutsuma-anime.com/)
* [Senryuu Shoujo](http://senryu-girl-official.com/)
* [Sewayaki Kitsune no Senko-san](http://senkosan.com/)
* [Yatogame-chan Kansatsu Nikki](https://yatogame.nagoya/)

### Winter 2019 Anime
* [Circlet Princess](https://cirpri-anime.jp/)
* [Date A Live III](http://date-a-live-anime.com/)
* [Domestic na Kanojo](http://domekano-anime.com/)
* [Egao no Daika](http://egaonodaika.com/)
* [Endro~!](http://www.endro.jp/)
* [Girly Air Force](http://www.gaf-anime.jp/)
* [Gotoubun no Hanayome](http://www.tbs.co.jp/anime/5hanayome/1st/)
* [Grimms Notes The Animation](http://www.tbs.co.jp/anime/grimmsnotes/)
* [Kaguya-sama wa Kokurasetai: Tensai-tachi no Renai Zunousen](https://kaguya.love/1st/)
* [Mahou Shoujo Tokushusen Asuka](http://magical-five.jp/)
* [Mini Toji](http://minitoji.jp/)
* [Pastel Memories](https://pasumemotv.com/)
* [Tate no Yuusha no Nariagari](http://shieldhero-anime.jp/1st/)
* [Watashi ni Tenshi ga Maiorita!](http://watatentv.com/)

### Fall 2018 Anime
* [Akanesasu Shoujo](http://akanesasushojo.com/)
* [Anima Yell!](http://www.animayell.com/)
* [Beelzebub-jou no Okinimesu mama.](https://beelmama.com/)
* [Conception](http://conception-anime.com/)
* [Goblin Slayer](http://goblinslayer.jp/)
* [Golden Kamuy 2nd Season](https://kamuy-anime.com/)
* [Hangyakusei Million Arthur](http://hangyakusei-anime.com/)
* [Irozuku Sekai no Ashita kara](http://www.iroduku.jp/)
* [Kishuku Gakkou no Juliet](https://www.juliet-anime.com/)
* [Merc Storia: Mukiryoku no Shounen to Bin no Naka no Shoujo](http://www.mercstoria.jp/)
* [Ore ga Suki nano wa Imouto dakedo Imouto ja Nai](http://imo-imo.jp/assets/story/)
* [Release the Spyce](https://releasethespyce.jp/)
* [Sora to Umi no Aida](http://soraumi-anime.com/)
* [SSSS.Gridman](https://gridman.net/)
* [Seishun Buta Yarou wa Bunny Girl Senpai no Yume wo Minai](https://ao-buta.com/)
* [Tensei shitara Slime Datta Ken](http://www.ten-sura.com/)
* [Tonari no Kyuuketsuki-san](http://kyuketsukisan-anime.com/)
* [Uchi no Maid ga Uzasugiru!](http://uzamaid.com/)
* [Ulysses: Jehanne Darc to Renkin no Kishi](https://ulysses-anime.jp/)

### Summer 2018 Anime
* [Angolmois: Genkou Kassenki](https://angolmois-anime.jp/)
* [Asobi Asobase](http://asobiasobase.com/assets/)
* [Chio-chan no Tsuugakuro](http://chiochan.jp/)
* [Grand Blue](https://www.grandblue-anime.com/)
* [Hanebado!](http://hanebad.com/)
* [Happy Sugar Life](http://happysugarlife.tv/)
* [Harukana Receive](http://www.harukana-receive.jp/)
* [Hataraku Saibou](https://hataraku-saibou.com/)
* [High Score Girl](http://hi-score-girl.com/)
* [Hyakuren no Haou to Seiyaku no Valkyria](http://hyakuren-anime.com/)
* [Isekai Maou to Shoukan Shoujo no Dorei Majutsu](https://season1.isekaimaou-anime.com/)
* [Island](http://never-island.com/)
* [Overlord III](http://overlord-anime.com/)
* [Satsuriku no Tenshi](http://satsuriku.com/)
* [Shichisei no Subaru](http://7subaru.jp/)
* [Tsukumogami Kashimasu](http://tsukumogami.jp/)
* [Yuragi-sou no Yuuna-san](https://yuragisou.com/)

### Spring 2018 Anime
* [Alice or Alice](http://alice-or-alice.com/)
* [Amanchu! Advance](http://amanchu-anime.com/)
* [Comic Girls](http://comic-girls.com/)
* [Golden Kamuy](https://kamuy-anime.com/)
* [Hinamatsuri](http://hina-matsuri.net/)
* [Hisone to Maso-tan](http://hisomaso.com/)
* [Last Period: Owarinaki Rasen no Monogatari](https://www.lastperiod.jp/)
* [Lostorage Conflated WIXOSS](http://lostorage-wixoss.com/)
* [Sword Art Online Alternative: Gun Gale Online](https://gungale-online.net/)
* [Tada-kun wa Koi wo Shinai](http://tadakoi.tv/)
* [Wotaku ni Koi wa Muzukashii](https://wotakoi-anime.com/)

### Winter 2018 Anime
* [Beatless](http://beatless-anime.jp/)
* [Darling in the FranXX](https://darli-fra.jp/)
* [Death March kara Hajimaru Isekai Kyousoukyoku](https://deathma-anime.com/)
* [Grancrest Senki](https://grancrest-anime.jp/)
* [Hakumei to Mikochi](http://hakumiko.com/)
* [Karakai Jouzu no Takagi-san](https://takagi3.me/1st/)
* [Marchen Madchen](https://maerchen-anime.com/)
* [Mitsuboshi Colors](http://mitsuboshi-anime.com/)
* [Overlord II](http://overlord-anime.com/)
* [Pop Team Epic](http://hoshiiro.jp/)
* [Ramen Daisuki Koizumi-san](http://ramen-koizumi.com/)
* [Ryuuou no Oshigoto!](http://www.ryuoh-anime.com/)
* [Slow Start](https://slow-start.com/)
* [Sora yori mo Tooi Basho](http://yorimoi.com/)
* [Toji no Miko](http://tojinomiko.jp/)
* [Yuru Camp](https://yurucamp.jp/first/)

### Fall 2017 Anime
* [Animegataris](http://animegataris.com/)
* [Blend S](https://blend-s.jp/)
* [Imouto sae Ireba Ii.](http://imotosae.com/)
* [Konohana Kitan](http://konohanatei.jp/)
* [Shoujo Shuumatsu Ryokou](http://girls-last-tour.com/)

### Summer 2017 Anime
* [Gamers!](https://www.gamers-anime.com/)
* [Isekai wa Smartphone to Tomo ni](http://isesuma-anime.jp/)
* [New Game!!](http://newgame-anime.com/)
* [Tenshi no 3P!](http://www.tenshi-no-3p.com/)
* [Tsurezure Children](http://tsuredure-project.jp/)
* [Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e](http://you-zitsu.com/)

### Spring 2017 Anime
* [Alice to Zouroku](https://www.alicetozouroku.com)
* [Busou Shoujo Machiavellianism](http://machiavellism-anime.jp/)
* [Clockwork Planet](http://www.tbs.co.jp/anime/cp/)
* [Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka Gaiden: Sword Oratoria](http://danmachi.com/sword_oratoria/)
* [Eromanga Sensei](https://eromanga-sensei.com/)
* [Hinako Note](http://hinakonote.jp/)
* [Re:Creators](https://recreators.tv/)
* [Renai Boukun](https://renaiboukun.com/story/)
* [Rokudenashi Majutsu Koushi to Akashic Records](http://rokuaka.jp)
* [Saenai Heroine no Sodatekata Flat](https://www.saenai.tv/)
* [Sakura Quest](http://sakura-quest.com/)
* [Sakurada Reset](http://wwwsp.sagrada-anime.com/)
* [Shuumatsu Nani Shitemasu ka? Isogashii Desu ka? Sukutte Moratte Ii Desu ka?](http://sukasuka-anime.com/)
* [Zero kara Hajimeru Mahou no Sho](http://zeronosyo.com/)

### Spring 2016 Anime
* [Gakusen Toshi Asterisk 2nd Season](https://asterisk-war.com/)

### Fall 2015 Anime
* [Gakusen Toshi Asterisk](https://asterisk-war.com/)
* [Rakudai Kishi no Cavalry](http://ittoshura.com/)

### Notes on Season
The anime are grouped according to the season it first premiered. There are four seasons:
* Winter (January to March)
* Spring (April to June)
* Summer (July to September)
* Fall (October to December)

</details>

## Content Viewer
You may browse the media downloaded by the scraper on a web browser.

### Setting Up for PHP
1. Download the latest PHP. Click [here](https://www.php.net/) to download.
2. Set the system environment path to where the PHP is downloaded.
3. Open Command Prompt/Terminal and input `php -v`. If the PHP version appeared, this means it is installed successfully.

### Instructions
1. Change directory to where `index.html` is located.
2. Run `php -S localhost:4000` to run a PHP server at port `4000`. You can specify other port numbers.
3. Open a web browser and type `localhost:4000` to access the Content Viewer.
