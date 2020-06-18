import os
import requests
import anime.constants as constants
from anime.main_download import MainDownload
from scan import WebNewtypeScanner

# Darwin's Game https://darwins-game.com/story/ #Dゲーム @d_game_official [WED]
# Eizouken http://eizouken-anime.com/story/ #映像研 @Eizouken_anime [FRI]
# Hatena Illusion http://hatenaillusion-anime.com/story.html #はてなイリュージョン #hatenaillusion @hatena_anime [SAT]
# Heya Camp https://yurucamp.jp/heyacamp/ #ゆるキャン #へやキャン @yurucamp_anime [MON]
# Infinite Dendrogram http://dendro-anime.jp/story/ #デンドロ @dendro_anime [FRI]
# Isekai Quartet 2 http://isekai-quartet.com/story/ #いせかる @isekai_quartet [WED]
# Ishuzoku Reviewers https://isyuzoku.com/story/ #isyuzoku @isyuzoku [TUE]
# Itai no wa https://bofuri.jp/story/ #防振り #bofuri @bofuri_anime [FRI]
# Jibaku Shounen Hanako-kun https://www.tbs.co.jp/anime/hanakokun/story/ #花子くん #花子くんアニメ @hanakokun_info [WED]
# Koisuru Asteroid http://koiastv.com/story.html #koias #koiastv #恋アス #恋する小惑星 @koiastv [TUE]
# Kyokou Suiri https://kyokousuiri.jp/ #虚構推理 @kyokou_suiri [THU]
# Murenase! Seton Gakuen https://anime-seton.jp/story/ #シートン #群れなせシートン学園 @anime_seton [FRI]
# Nekopara https://nekopara-anime.com/ja/story/ #ネコぱら @nekopara_anime [FRI]
# Oshibudo https://oshibudo.com/story #推し武道 #oshibudo @anime_oshibudo
# Plunderer http://plunderer-info.com/ #プランダラ #pldr @plundereranime [FRI]
# Rikekoi https://rikekoi.com/story #リケ恋 #りけこい #rikekoi @rikeigakoini [MON]
# Runway de Waratte https://runway-anime.com/introduction/ #ランウェイで笑って @runway_anime
# Somali https://somali-anime.com/story.html #ソマリと森の神様 @somali_anime [THU]
# Toaru Kagaku no Railgun T https://toaru-project.com/railgun_t/story/ #超電磁砲T @toaru_project [SUN]


# Winter 2020 Anime
class Winter2020AnimeDownload(MainDownload):
    season = "2020-1"
    season_name = "Winter 2020"

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/2020-1"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)


# Darwin's Game
class DarwinsGameDownload(Winter2020AnimeDownload):
    title = "Darwin's Game"
    keywords = ["Darwin's Game"]

    STORY_PAGE = "https://darwins-game.com/story/"
    PAGE_PREFIX = "https://darwins-game.com/story/?id=ep"
    BD_PAGE = "https://darwins-game.com/bddvd/"
    BD_PAGE_PREFIX = "https://darwins-game.com/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/darwins-game"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        self.download_episode_preview()
        self.download_bluray()

    def download_bluray(self):
        bluray_filepath = self.create_bluray_directory()
        '''
        try:
            bd_soup = self.get_soup(self.BD_PAGE)
            bd_tags = bd_soup.find('ul', class_='nav_package').find_all('img')
            k = 0
            for bd_tag in bd_tags:
                k += 1
                bd_link = self.BD_PAGE_PREFIX + bd_tag['src'].replace('../', '')
                if "img_jk_1.jpg" not in bd_link:  # Skip Coming Soon picture
                    filepath_without_extension = bluray_filepath + "/bd_" + str(k)
                    self.download_image(bd_link, filepath_without_extension)
        except:
            pass
        '''
        image_objs = [
            {'name': 'bd_1_1', 'url': 'https://pbs.twimg.com/media/EPNlw-1UYAEFHTR?format=jpg&name=4096x4096'},
            {'name': 'bd_1_2', 'url': 'https://pbs.twimg.com/media/EPNlw-1UEAA-pLI?format=jpg&name=4096x4096'},
            {'name': 'bd_2_1', 'url': 'https://pbs.twimg.com/media/ETPHRi2UMAYlNoj?format=png&name=900x900'},
            {'name': 'bd_2_2', 'url': 'https://pbs.twimg.com/media/ETPHSqoU8AASZkk?format=png&name=900x900'},
            {'name': 'bd_3_1', 'url': 'https://darwins-game.com/assets/img/bddvd/img_jk_03.jpg'},
            {'name': 'bd_3_2', 'url': 'https://pbs.twimg.com/media/EVO8qahUMAApK2A?format=jpg&name=4096x4096'},
            {'name': 'bd_4_1', 'url': 'https://pbs.twimg.com/media/Eai1XvsVAAAcHGN?format=jpg&name=4096x4096'},
            {'name': 'bd_4_2', 'url': 'https://pbs.twimg.com/media/Eai1a3PUMAAtii5?format=jpg&name=4096x4096'},
            {'name': 'bd_bonus_1', 'url': 'https://darwins-game.com/assets/img/bddvd/img_animate.jpg'},
            {'name': 'bd_bonus_2', 'url': 'https://darwins-game.com/assets/img/bddvd/img_aniplex03.jpg'},
            {'name': 'bd_bonus_3', 'url': 'https://darwins-game.com/assets/img/bddvd/img_amazon.jpg'},
            {'name': 'bd_bonus_4', 'url': 'https://darwins-game.com/assets/img/bddvd/img_sofmap.jpg'}]
        self.download_image_objects(image_objs, bluray_filepath)

    def download_episode_preview(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<ul class="story_list">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('</ul>')[0].split('<a href="./?id=ep')
            for i in range(1, len(split2), 1):
                episode_num = ''
                try:
                    episode_num = split2[i].split('"')[0]
                    temp = int(episode_num)
                except:
                    continue
                episode = episode_num.zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                page_url = self.PAGE_PREFIX + episode_num
                page_response = self.get_response(page_url)
                split3 = page_response.split('<div class="slider clearfix">')
                if len(split3) < 2:
                    continue
                split4 = split3[1].split('</div>')[0].split('<img src="')
                for j in range(1, len(split4), 1):
                    imageUrl = self.STORY_PAGE + split4[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Eizouken ni wa Te wo Dasu na!
class EizoukenDownload(Winter2020AnimeDownload):
    title = "Eizouken ni wa Te wo Dasu na!"
    keywords = ["Eizouken ni wa Te wo Dasu na!", "Keep Your Hands Off Eizouken!"]

    PAGE_PREFIX = "http://eizouken-anime.com"
    STORY_DATA_JSON = "http://eizouken-anime.com/story/story_data.json"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/eizouken"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            story_json = self.get_json(self.STORY_DATA_JSON)
            story_data = story_json['data']
            for data in story_data:
                name = data['name']
                episode_num = name.split('.html')[0]
                try:
                    temp = int(episode_num)
                except:
                    continue
                episode = episode_num.zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_01.jpg"):
                    continue
                html = data['html']
                split1 = html.split('<img src="')
                for i in range(1, len(split1), 1):
                    imageUrl = self.PAGE_PREFIX + split1[i].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(i).zfill(2)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Hatena Illusion
class HatenaIllusionDownload(Winter2020AnimeDownload):
    title = "Hatena Illusion"
    keywords = ["Hatena Illusion"]

    PAGE_PREFIX = "http://hatenaillusion-anime.com/"
    STORY_PAGE = "http://hatenaillusion-anime.com/story.html"
    
    CHAR_DAI = "\\xe7\\xac\\xac" #第
    CHAR_WA = "\\xe8\\xa9\\xb1" #話
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/hatena-illusion"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<img class="story_r RightToLeft"')
            for i in range(1, len(split1), 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                split2 = split1[i].split('src="./')
                if len(split2) < 2:
                    continue
                imageUrl = self.PAGE_PREFIX + split2[1].split('"')[0]
                filepathWithoutExtension = self.base_folder + "/" + episode + "_1"
                self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Heya Camp
class HeyaCampDownload(Winter2020AnimeDownload):
    title = "Heya Camp"
    keywords = ["Heya Camp", "Room Camp", "Yuru Camp", "Yurucamp", "Laid-Back Camp"]

    PAGE_PREFIX = "https://yurucamp.jp/heyacamp/"
    EPISODE_PREFIX = "https://yurucamp.jp/heyacamp/episode/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/heya-camp"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
            
    def run(self):
        try:
            response = self.get_response(self.EPISODE_PREFIX)
            split1 = response.split('<ul id="episodeList">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('</ul>')[0].split('<a href="')
            for i in range(1, len(split2), 1):
                split3 = split2[i].split('"')[0]
                try:
                    episode = str(int(split3.split('.php')[0])).zfill(2)
                except:
                    continue
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                page_url = self.EPISODE_PREFIX + split3
                page_response = self.get_response(page_url)
                split4 = page_response.split('<ul id="episodeImgs">')
                if len(split4) < 2:
                    continue
                split5 = split4[1].split('</ul>')[0].split('<img src="../')
                for j in range(1, len(split5), 1):
                    imageUrl = self.PAGE_PREFIX + split5[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

'''
# Heya Camp
class HeyaCampDownload(Winter2020AnimeDownload):
    
    PAGE_PREFIX = "https://yurucamp.jp/news/page/"
    FINAL_EPISODE = 13
    FIRST_EPISODE_ARTICLE_ID = 5138
    FINAL_EPISODE_ARTICLE_ID = 10000 # to be updated
    
    CHAR_DAI = "\\xe7\\xac\\xac" #第
    CHAR_WA = "\\xe8\\xa9\\xb1" #話
    
    MAX_PAGES = 20 # To avoid infinite loop
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/heya-camp"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            page = 0
            loop = True
            while page < self.MAX_PAGES and loop:
                page += 1
                page_url = self.PAGE_PREFIX + str(page)
                response = self.get_response(page_url)
                split1 = response.split('<ul id="articleList">')
                if len(split1) < 2:
                    continue
                split2 = split1[1].split("wp-pagenavi")[0].split('<li><a href="')
                for i in range(1, len(split2), 1):
                    article_url = split2[i].split('"')[0]
                    article_url_split = article_url.split('/')
                    article_id = article_url_split[len(article_url_split) - 1]
                    if int(article_id) < self.FIRST_EPISODE_ARTICLE_ID:
                        loop = False
                        break
                    split3 = split2[i].split('<p class="articleTitle">')
                    if len(split3) < 2:
                        continue
                    article_title = split3[1].split('</p>')[0]
                    if self.CHAR_DAI in article_title and self.CHAR_WA in article_title:
                        split4 = article_title.split(self.CHAR_WA)[0].split(self.CHAR_DAI)
                        if len(split4) < 2:
                            continue
                        episode_num = split4[1]
                        try:
                            temp = int(episode_num) # check if it is an integer
                            episode = episode_num.zfill(2)
                            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                                continue
                            article_response = self.get_response(article_url)
                            split5 = article_response.split('<article>')
                            if len(split5) < 2:
                                continue
                            split6 = split5[1].split('</article>')[0].split('<p><a href="')
                            for j in range(1, len(split6), 1):
                                imageUrl = split6[j].split('"')[0]
                                filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                                self.download_image(imageUrl, filepathWithoutExtension)
                        except Exception as e:
                            print("Error in running " + self.__class__.__name__)
                            print(e)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)
'''


# Infinite Dendrogram
class InfiniteDendrogramDownload(Winter2020AnimeDownload):
    title = "Infinite Dendrogram"
    keywords = ["Infinite Dendrogram"]

    PAGE_PREFIX = "http://dendro-anime.jp/story/"
    EPISODE_PAGE_PREFIX = "http://dendro-anime.jp/story/ep"
    EPISODE_PAGE_SUFFIX = "/"
    STORY_PAGE = "http://dendro-anime.jp/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/infinite-dendrogram"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<section class="categiry_list is-pc">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('</section>')[0].split('<li><a href="http://dendro-anime.jp/story/ep')
            for i in range(1, len(split2), 1):
                split3 = split2[i].split('"')[0].split('/')[0]
                try:
                    episode_temp = int(split3)
                    episode = str(episode_temp).zfill(2)
                except Exception as e:
                    continue
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                page_url = self.EPISODE_PAGE_PREFIX + split3 + self.EPISODE_PAGE_SUFFIX
                page_response = self.get_response(page_url)
                split4 = page_response.split('<div class="slide">')
                for j in range(1, len(split4), 1):
                    split5 = split4[j].split('<img src="')
                    if len(split5) < 2:
                        continue
                    imageUrl = split5[1].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Isekai Quartet 2
class IsekaiQuartet2Download(Winter2020AnimeDownload):
    title = "Isekai Quartet 2"
    keywords = ["Isekai Quartet 2"]

    PAGE_PREFIX = "http://isekai-quartet.com/"
    STORY_PAGE = "http://isekai-quartet.com/story/index.html"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/isekai-quartet2"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<div id="S_')
            for i in range(len(split1)-1, 0, -1):
                num = split1[i].split('"')[0]
                try:
                    number = int(num)
                except Exception as e:
                    continue
                episode = str(number).zfill(2)
                split2 = split1[i].split('<div class="slider-sceneImage">')
                #print('daaaaa')
                if len(split2) < 2:
                    continue
                #print('goooo')
                split3 = split2[1].split('<div class="ep-text">')[0].split('<img src="')
                for j in range(1, len(split3), 1):
                    split4 = split3[j].split('../')
                    if len(split4) < 2:
                        continue
                    imageUrl = self.PAGE_PREFIX + split4[1].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Ishuzoku Reviewers
class IshuzokuReviewersDownload(Winter2020AnimeDownload):
    title = "Ishuzoku Reviewers"
    keywords = ["Isyuzoku", "Ishuzoku Reviewers", "Interspecies Reviewers"]

    PAGE_PREFIX = "https://isyuzoku.com/"
    STORY_PAGE = "https://isyuzoku.com/story/"
    CHAR_DAI = "\\xe7\\xac\\xac" #第
    CHAR_WA = "\\xe8\\xa9\\xb1" #話
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/ishuzoku-reviewers"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<div id="StoryData">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('<div id="S_itl1">')[0].split('<div id="S_')
            for i in range(1, len(split2), 1):
                split3 = split2[i].split('<h2 class="ep-title">')
                if len(split3) < 2:
                    continue
                split4 = split3[1].split('</span>')[0]
                if self.CHAR_DAI in split4 and self.CHAR_WA in split4:
                    split5 = split4.split(self.CHAR_WA)[0].split(self.CHAR_DAI)
                    if len(split5) < 2:
                        continue
                else:
                    continue
                episode = ''
                try:
                    episode_temp = int(split5[1])
                    episode = str(episode_temp).zfill(2)
                except:
                    continue
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                split6 = split2[i].split('<div class="ep-slider-sceneImage">')
                if len(split6) < 2:
                    continue
                split7 = split6[1].split('<div class="ep-slider-thumb">')[0].split('<img src="../')
                for j in range(1, len(split7), 1):
                    imageUrl = self.PAGE_PREFIX + split7[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Itai no wa Iya nano de Bougyoryoku ni Kyokufuri Shitai to Omoimasu.
class BofuriDownload(Winter2020AnimeDownload):
    title = "Itai no wa Iya nano de Bougyoryoku ni Kyokufuri Shitai to Omoimasu."
    keywords = ["Itai no wa Iya nano de Bougyoryoku ni Kyokufuri Shitai to Omoimasu.",
                "BOFURI: I Don't Want to Get Hurt, so I'll Max Out My Defense."]

    PAGE_PREFIX = "https://bofuri.jp/"
    STORY_PAGE = "https://bofuri.jp/story/"
    EPISODE_PAGE = "https://bofuri.jp/story/episode.html"
    FINAL_EPISODE = 12
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/bofuri"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        self.download_bluray()
        self.download_episode_preview()

    def download_episode_preview(self):
        try:
            response = self.get_response(self.EPISODE_PAGE)
            for i in range(1, self.FINAL_EPISODE + 1, 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                split1 = response.split('<div class="episode-data" id="EP' + str(i) + '"')
                if len(split1) < 2:
                    continue
                split2 = split1[1].split('<div class="ep-staff">')[0].split('<img src="../')
                for j in range(1, len(split2), 1):
                    imageUrl = self.PAGE_PREFIX + split2[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_bluray(self):
        bluray_filepath = self.base_folder + '/' + constants.FOLDER_BLURAY
        if not os.path.exists(bluray_filepath):
            os.makedirs(bluray_filepath)

        image_objs = [
            {'name': 'bd_bonus_1', 'url': 'https://bofuri.jp/assets/bluray/cp/1.png'},
            {'name': 'bd_bonus_2', 'url': 'https://bofuri.jp/assets/bluray/bnf/th/1.jpg'},
            {'name': 'bd_bonus_3', 'url': 'https://bofuri.jp/assets/bluray/bnf/th/2.jpg'},
            {'name': 'bd_bonus_4', 'url': 'https://bofuri.jp/assets/bluray/bnf/th/3.jpg'},
            {'name': 'bd_bonus_5', 'url': 'https://bofuri.jp/assets/bluray/bnf/th/4.jpg'},
            {'name': 'bd_bonus_6', 'url': 'https://bofuri.jp/assets/bluray/bnf/th/5.jpg'},
            {'name': 'bd_bonus_7', 'url': 'https://bofuri.jp/assets/bluray/bnf/th/6.jpg'},
            {'name': 'bd_1_1', 'url': 'https://pbs.twimg.com/media/ES0VfovUMAAY11q?format=jpg&name=4096x4096'},
            {'name': 'bd_1_2', 'url': 'https://tc-animate.techorus-cdn.com/resize_image/resize_image.php?image=03111454_5e687d099c28c.jpg'},
            {'name': 'bd_2_1', 'url': 'https://pbs.twimg.com/media/EUlhuICUMAAvPf6?format=jpg&name=4096x4096'},
            {'name': 'bd_2_2', 'url': 'https://tc-animate.techorus-cdn.com/resize_image/resize_image.php?image=05111439_5eb8e52a46095.jpg'},
            {'name': 'bd_3_1', 'url': 'https://bofuri.jp/assets/bluray/3/main.jpg'},
            {'name': 'bd_3_2', 'url': 'https://tc-animate.techorus-cdn.com/resize_image/resize_image.php?image=04171104_5e990ebc07a88.jpg'}]
        for image_obj in image_objs:
            if os.path.exists(bluray_filepath + '/' + image_obj['name'] + '.png') or \
                    os.path.exists(bluray_filepath + '/' + image_obj['name'] + '.jpg'):
                continue
            filepath_without_extension = bluray_filepath + '/' + image_obj['name']
            self.download_image(image_obj['url'], filepath_without_extension)


# Jibaku Shounen Hanako-kun
class HanakoKunDownload(Winter2020AnimeDownload):
    title = "Jibaku Shounen Hanako-kun"
    keywords = ["Jibaku Shounen Hanako-kun", "Toilet Bound Hanako-kun", "Hanakokun"]

    PAGE_PREFIX = "https://www.tbs.co.jp/anime/hanakokun/"
    STORY_PAGE = "https://www.tbs.co.jp/anime/hanakokun/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/hanako-kun"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<ul class="story-nav">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('</ul>')[0].split('<!--')[0].split('<a href="')
            for i in range(1, len(split2), 1):
                split3 = split2[i].split('.png"></a>')[0].split('src="img/storynav_')
                if len(split3) < 2:
                    continue
                try:
                    episode_temp = int(split3[1])
                    episode = str(episode_temp).zfill(2)
                except Exception as e:
                    continue
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                page_url = self.STORY_PAGE + split2[i].split('"')[0]
                page_response = self.get_response(page_url)
                split4 = page_response.split('<div class="swiper-slide"><img src="')
                for j in range(1, len(split4), 1):
                    imageUrl = self.STORY_PAGE + split4[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Koisuru Asteroid
class KoisuruAsteroidDownload(Winter2020AnimeDownload):
    title = "Koisuru Asteroid"
    keywords = ["Koisuru Asteroid", "Asteroid in Love"]

    STORY_PAGE = "http://koiastv.com/story.html"
    PAGE_PREFIX = "http://koiastv.com/story"
    IMAGE_PREFIX = "http://koiastv.com/"
    PAGE_SUFFIX = ".html"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/koisuru-asteroid"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        self.download_episode_preview()
        self.download_keyvisual()
        self.download_bluray()
        self.download_endcard()
        self.download_event()

    def download_episode_preview(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<a href="story')
            for i in range(1, len(split1), 1):
                episode_split = split1[i].split('.html"')[0]
                try:
                    temp = int(episode_split)
                except Exception as e:
                    continue
                episode = episode_split.zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                page_url = self.PAGE_PREFIX + episode_split + self.PAGE_SUFFIX
                page_response = self.get_response(page_url)
                split2 = page_response.split('<ol class="main">')
                if len(split2) < 2:
                    continue
                split3 = split2[1].split('</ol>')[0].split('<img src="')
                for j in range(1, len(split3), 1):
                    imageUrl = self.IMAGE_PREFIX + split3[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_endcard(self):
        filepath = self.create_custom_directory(constants.FOLDER_ENDCARD)
        image_objs = [
            {'name': 'ec01', 'url': 'https://pbs.twimg.com/media/ENGSq1FUUAAWIAk?format=png&name=900x900'},
            {'name': 'ec02', 'url': 'https://pbs.twimg.com/media/EN1wCCGUcAAGxZO?format=jpg&name=medium'},
            {'name': 'ec03', 'url': 'https://pbs.twimg.com/media/EOao-mwU8AAIFfF?format=jpg&name=medium'},
            {'name': 'ec04', 'url': 'https://pbs.twimg.com/media/EO9r0v_UYAEgYPu?format=jpg&name=medium'},
            {'name': 'ec05', 'url': 'https://pbs.twimg.com/media/EPmPDAoU0AUX3jo?format=jpg&name=medium'},
            {'name': 'ec06', 'url': 'https://pbs.twimg.com/media/EQKCfFIUEAMvJG2?format=jpg&name=900x900'},
            {'name': 'ec07', 'url': 'https://pbs.twimg.com/media/ERNrIGsVAAI3zj2?format=jpg&name=medium'},
            {'name': 'ec08', 'url': 'https://pbs.twimg.com/media/ER3HzkDUUAIbiBW?format=jpg&name=medium'},
            {'name': 'ec09', 'url': 'https://pbs.twimg.com/media/ESbMX2_U0AAIA7v?format=png&name=900x900'},
            {'name': 'ec10', 'url': 'https://pbs.twimg.com/media/ES-LTOmU4AYlBor?format=png&name=900x900'},
            {'name': 'ec11', 'url': 'https://pbs.twimg.com/media/ETePfWDU0AE9qzl?format=png&name=900x900'},
            {'name': 'ec12', 'url': 'https://pbs.twimg.com/media/EUGBTQ-U4AELyLs?format=jpg&name=medium'}]
        self.download_image_objects(image_objs, filepath)

    def download_bluray(self):
        filepath = self.create_bluray_directory()
        image_objs = [
            {'name': 'music_ost', 'url': 'https://pbs.twimg.com/media/ER3JRDCVUAMnQjM?format=jpg&name=small'},
            {'name': 'music_op', 'url': 'https://pbs.twimg.com/media/EQKEKLVVAAEtmJ0?format=jpg&name=900x900'},
            {'name': 'bd_1_1', 'url': 'https://pbs.twimg.com/media/ER3Nv8IVUAIgJqQ?format=png&name=medium'},
            {'name': 'bd_1_2', 'url': 'http://koiastv.com/images/package/001/j_002.jpg'},
            {'name': 'bd_2_1', 'url': 'https://pbs.twimg.com/media/EUFWg1bVAAAmMsD?format=jpg&name=medium'},
            {'name': 'bd_2_2', 'url': 'http://koiastv.com/images/package/002/j_002.jpg'},
            {'name': 'bd_3_1', 'url': 'https://pbs.twimg.com/media/EWGL6AxUMAApbvB?format=jpg&name=900x900'},
            {'name': 'bd_3_2', 'url': 'http://koiastv.com/images/package/003/j_002.jpg'},
            {'name': 'bd_bonus_1', 'url': 'http://koiastv.com/images/package/tokuten/p_amazon2.jpg'},
            {'name': 'bd_bonus_2', 'url': 'http://koiastv.com/images/package/tokuten/p_animate2.jpg'},
            {'name': 'bd_bonus_3', 'url': 'http://koiastv.com/images/package/tokuten/p_gamers3.jpg'},
            {'name': 'bd_bonus_4', 'url': 'http://koiastv.com/images/package/tokuten/p_sofmap2.jpg'},
            {'name': 'bd_bonus_5', 'url': 'http://koiastv.com/images/package/tokuten/p_tora2.jpg'},
            {'name': 'bd_bonus_6', 'url': 'http://koiastv.com/images/package/tokuten/p_gstore2.jpg'}]
        self.download_image_objects(image_objs, filepath)

    def download_event(self):
        filepath = self.create_custom_directory(constants.FOLDER_EVENT)
        image_objs = [
            {'name': 'valentine', 'url': 'http://koiastv.com/images/news/p_038.jpg'},
            {'name': 'valentine_big', 'url': 'http://koiastv.com/images/top/v_002.jpg'},
            {'name': 'special_event_visual', 'url': 'http://koiastv.com/images/news/p_043.jpg'}]
        self.download_image_objects(image_objs, filepath)

    def download_keyvisual(self):
        filepath = self.create_key_visual_directory()
        image_objs = [
            {'name': 'kv', 'url': 'http://koiastv.com/images/top/v_001.jpg'}]
        self.download_image_objects(image_objs, filepath)


# Kyokou Suiri
class KyokouSuiriDownload(Winter2020AnimeDownload):
    title = "Kyokou Suiri"
    keywords = ["Kyokou Suiri", "In/Spectre"]

    PAGE_PREFIX = "https://kyokousuiri.jp/"
    STORY_PAGE = "https://kyokousuiri.jp/story/"
    
    CHAR_DAI = "\\xe7\\xac\\xac" #第
    CHAR_WA = "\\xe8\\xa9\\xb1" #話
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/kyokou-suiri"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<div class="p-story_ep__header">')
            for i in range(1, len(split1), 1):
                split2 = split1[i].split('<div class="p-story_ep__no">')
                if len(split2) < 2:
                    continue
                split3 = split2[1].split('</div>')[0]
                if self.CHAR_DAI in split3 and self.CHAR_WA in split3:
                    episode = ''
                    try:
                        split4 = split3.split(self.CHAR_WA)[0].split(self.CHAR_DAI)[1]
                        episode_temp = int(split4)
                        episode = str(episode_temp).zfill(2)
                    except Exception as e:
                        continue
                    if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                        continue
                    split5 = split1[i].split('</ul>')[0].split('<img src="')
                    for j in range(1, len(split5), 1):
                        imageUrl = split5[j].split('"')[0]
                        filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                        self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Murenase! Seton Gakuen
class MurenaseSetonGakuenDownload(Winter2020AnimeDownload):
    title = "Murenase! Seton Gakuen"
    keywords = ["Murenase! Seton Gakuen", "Seton Academy: Join the Pack!"]

    PAGE_PREFIX = "https://anime-seton.jp/"
    STORY_PAGE = "https://anime-seton.jp/story/"
    BD_PAGE = "https://anime-seton.jp/bddvd/"
    FINAL_EPISODE = 13
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/murenase-seton"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        self.download_episode_preview()
        self.download_bluray()

    def download_bluray(self):
        filepath = self.create_bluray_directory()
        image_objs = [
            {'name': 'bd_1_1', 'url': 'https://anime-seton.jp/app/wp-content/uploads/2020/01/36ba84898e9b91bc5b376373e600e8d5.jpg'},
            {'name': 'bd_1_1_2', 'url': 'https://anime-seton.jp/app/wp-content/uploads/2020/01/a6f93f0b7d4ac58b00ddf264fb353e9a.jpg'},
            {'name': 'bd_2_1', 'url': 'https://anime-seton.jp/app/wp-content/uploads/2020/01/a46f6ed8cdd7ee40c9818ebe95c931e2.jpg'},
            {'name': 'bd_2_2', 'url': 'https://pbs.twimg.com/media/ETtwvtwUYAAbP6V?format=png&name=900x900'},
            {'name': 'bd_3_1', 'url': 'https://anime-seton.jp/app/wp-content/uploads/2020/01/4f28f65f18cbe1aa57d5faf1a196bd04.jpg'},
            {'name': 'bd_3_2', 'url': 'https://pbs.twimg.com/media/EZqAhRjU8AI23qE?format=jpg&name=900x900'},
            {'name': 'bd_bonus_1', 'url': 'https://anime-seton.jp/app/wp-content/uploads/2020/02/9ec9b9d4b1255a0606353a5144f9c335.jpg'},
            {'name': 'bd_bonus_2', 'url': 'https://anime-seton.jp/app/wp-content/uploads/2020/01/0025f8f13f5e4f4eb913da12576b70ea.jpg'},
            {'name': 'bd_bonus_3', 'url': 'https://anime-seton.jp/app/wp-content/uploads/2020/01/e3eb7162e11acf8e2caaabd195f7302d.jpg'}]
        self.download_image_objects(image_objs, filepath)

    def download_episode_preview(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<section class="story__list">')[1].split('</section>')[0].split('<li')
            total_episodes = len(split1) - 1
            for i in range(total_episodes):
                episode = str(i+1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_01.jpg"):
                    continue
                page_url = self.STORY_PAGE + "?ep=" + str(i+1)
                page_response = self.get_response(page_url)
                split2 = page_response.split('<ul class="slider">')
                if len(split2) < 2:
                    continue
                split3 = split2[1].split('</ul>')[0].split('<li><img src="')
                for j in range(1, len(split3), 1):
                    imageUrl = split3[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j).zfill(2)
                    self.download_image(imageUrl, filepathWithoutExtension)
            bd_soup = self.get_soup(self.BD_PAGE)
            bd_tags = bd_soup.find_all('ul', class_='bddvd__list')
            k = 0
            for bd_tag in bd_tags:
                k += 1
                bd_link = bd_tag.find('img')['src']
                if '8cffe16fefc1bd3bf15f31330d324626' not in bd_link: # not Now Printing image
                    filepath_without_extension = self.base_folder + "/bluray_vol" + str(k)
                    self.download_image(bd_link, filepath_without_extension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Nekopara
class NekoparaDownload(Winter2020AnimeDownload):
    title = "Nekopara"
    keywords = ["Nekopara"]
    
    API_45_JSON = 'https://nekopara-anime.com/ja/php/avex/api.php?mode=45'
    API_46_JSON_PREFIX = 'https://nekopara-anime.com/ja/php/avex/api.php?mode=46&id='
    BD_PAGE = 'https://nekopara-anime.com/ja/product/detail.php?id=1017384'
    
    PAGE_PREFIX = "https://nekopara-anime.com/ja/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/nekopara"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        self.download_episode_preview()
        self.download_keyvisual()
        self.download_bluray()
        self.download_event()
        self.download_endcard()

    def download_episode_preview(self):
        try:
            api45_json = self.get_json(self.API_45_JSON)
            ids = api45_json['item']
            for i in range(len(ids)):
                id = ids[i]['id']
                url = self.API_46_JSON_PREFIX + id
                api46_json = self.get_json(url)
                #episode = api46_json['item']['title_mobile'].split('話')[0].replace('第','').zfill(2)
                episode = str(len(ids) - i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    break
                split1 = api46_json['item']['contents'].split('<br')[0].split('<img src=\"')
                for j in range(1, len(split1), 1):
                    imageUrl = split1[j].split('\"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)

            bd_soup = self.get_soup(self.BD_PAGE)
            bd_tags = bd_soup.find_all('div', class_='c-article-visual__item')
            k = 0
            for bd_tag in bd_tags:
                k += 1
                bd_link = bd_tag.find('img')['src']
                if 'nowprinting.jpg' not in bd_link:
                    filepath_without_extension = self.base_folder + "/bluray_vol" + str(k)
                    self.download_image(bd_link, filepath_without_extension)

        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)
        WebNewtypeScanner('ネコぱら',self.base_folder).run()

    def download_keyvisual(self):
        filepath = self.create_key_visual_directory()
        image_objs = [
            {'name': 'kv_1', 'url': 'https://nekopara-anime.com/ja/img/home/visual_01.jpg'},
            {'name': 'kv_2', 'url': 'https://nekopara-anime.com/ja/img/home/visual_02.jpg'},
            {'name': 'kv_2b', 'url': 'https://nekopara-anime.com/ja/img/home/visual_02.jpg'},
            {'name': 'kv_3', 'url': 'https://nekopara-anime.com/ja/img/home/visual_03.jpg'},
            {'name': 'kv_3_pc', 'url': 'https://nekopara-anime.com/ja/img/home/visual_03_pc.png'},
            {'name': 'kv_4', 'url': 'https://nekopara-anime.com/ja/img/home/visual_04_pc.png'},
            {'name': 'kv_5', 'url': 'https://nekopara-anime.com/ja/img/home/visual_05_pc.png'}]
        self.download_image_objects(image_objs, filepath)

    def download_bluray(self):
        filepath = self.create_bluray_directory()
        image_objs = [
            {'name': 'music_op', 'url': 'https://img.imageimg.net/artist/nekopara-anime/img/product_1031077.jpg'},
            {'name': 'music_ed', 'url': 'https://img.imageimg.net/artist/nekopara-anime/img/product_1031101.jpg'},
            {'name': 'music_ost', 'url': 'https://img.imageimg.net/artist/nekopara-anime/img/product_1031239.jpg'},
            {'name': 'bd_1', 'url': 'https://img.imageimg.net/artist/nekopara-anime/img/product_1031240.jpg'},
            {'name': 'bd_2', 'url': 'https://img.imageimg.net/artist/nekopara-anime/img/product_1031241.jpg'},
            {'name': 'bd_bonus_1_1', 'url': 'https://m.imageimg.net/upload/artist_img/NKPRA/0116a14b28b259b049b9c1d235cc100979a3c5e4_5e3ba84feaad8.jpg'},
            {'name': 'bd_bonus_1_2', 'url': 'https://m.imageimg.net/upload/artist_img/NKPRA/9d3b89466d93d37f9d72b557ca87bcd0ee5e5df9_5e7b0d79705b2.jpg'},
            {'name': 'bd_bonus_1_3', 'url': 'https://m.imageimg.net/upload/artist_img/NKPRA/d2f96e4c177cd49d17aa356c38e1820da1030008_5e7b0d9364282.jpg'},
            {'name': 'bd_bonus_1_4', 'url': 'https://m.imageimg.net/upload/artist_img/NKPRA/e49f6ab0cfb91fa3cefe49f81384ee849b6c68c6_5e7b0da5dddab.jpg'},
            {'name': 'bd_bonus_2', 'url': 'https://m.imageimg.net/upload/artist_img/NKPRA/4ee0a49df45d2dc987a6b707ebaed013b57023bb_5e7b0e19ce06d.jpg'},
            {'name': 'bd_bonus_3', 'url': 'https://m.imageimg.net/upload/artist_img/NKPRA/a071447604066d768245b9ffeff7204d065e398e_5e3ba84f78244.jpg'},
            {'name': 'bd_bonus_4', 'url': 'https://m.imageimg.net/upload/artist_img/NKPRA/0135f75e251f30014adb7ee63f925125b98b2585_5eddd001a7e4a.jpg'},
            {'name': 'bd_bonus_5', 'url': 'https://m.imageimg.net/upload/artist_img/NKPRA/d05814a8be31ddb04c2662a66c9da235aac3ced7_5eddd000f1102.jpg'}]
        self.download_image_objects(image_objs, filepath)

    def download_event(self):
        filepath = self.create_custom_directory(constants.FOLDER_EVENT)
        image_objs = [
            {'name': 'c97', 'url': 'https://pbs.twimg.com/media/EMyYJvUVAAAGYpK?format=jpg&name=900x900'}]
        self.download_image_objects(image_objs, filepath)

    def download_endcard(self):
        filepath = self.create_custom_directory(constants.FOLDER_ENDCARD)
        image_objs = [
            {'name': 'ec01', 'url': 'https://pbs.twimg.com/media/ENxmTedUwAEgfx1?format=jpg&name=900x900'},
            {'name': 'ec02', 'url': 'https://pbs.twimg.com/media/EN-o56OUEAASMdD?format=jpg&name=900x900'},
            {'name': 'ec03', 'url': 'https://pbs.twimg.com/media/EN-pP27U8AADHNC?format=jpg&name=900x900'},
            {'name': 'ec04', 'url': 'https://pbs.twimg.com/media/EN-pzv4VAAE78yp?format=jpg&name=900x900'},
            {'name': 'ec05', 'url': 'https://pbs.twimg.com/media/EN-qLLSVAAEwKy8?format=jpg&name=900x900'},
            {'name': 'ec06', 'url': 'https://pbs.twimg.com/media/EN-q7jJUcAAfDjG?format=jpg&name=900x900'},
            {'name': 'ec07', 'url': 'https://pbs.twimg.com/media/ERIxa0bVAAEdXoQ?format=jpg&name=900x900'},
            {'name': 'ec08', 'url': 'https://pbs.twimg.com/media/ERIx4CXUcAI_8PO?format=jpg&name=900x900'},
            {'name': 'ec09', 'url': 'https://pbs.twimg.com/media/ESFRo6TU8AAFvvt?format=jpg&name=900x900'},
            {'name': 'ec10', 'url': 'https://pbs.twimg.com/media/ERIyogOVAAED-eX?format=jpg&name=900x900'},
            {'name': 'ec11', 'url': 'https://pbs.twimg.com/media/ETJ8K-0UUAADTyx?format=jpg&name=medium'},
            {'name': 'ec12', 'url': 'https://pbs.twimg.com/media/ETxU3O8UcAU269_?format=jpg&name=900x900'}]
        self.download_image_objects(image_objs, filepath)


# Oshi ga Budoukan Ittekuretara Shinu
class OshibudoDownload(Winter2020AnimeDownload):
    title = "Oshi ga Budoukan Ittekuretara Shinu"
    keywords = ["Oshibudo", "Oshi ga Budoukan Ittekuretara Shinu",
                "If My Favorite Pop Idol Made It to the Budokan, I Would Die"]
    
    EPISODE_DATA_JSON = "https://oshibudo.com/story/episode_data.php"
    PAGE_PREFIX = "https://oshibudo.com/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/oshibudo"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
            
    def run(self):
        try:
            episodes = self.get_json(self.EPISODE_DATA_JSON)
            for episode_obj in episodes:
                episode = ''
                try:
                    episode = str(int(episode_obj['id'])).zfill(2)
                except:
                    continue
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                images = episode_obj['images']
                for j in range(len(images)):
                    imageUrl = self.PAGE_PREFIX + images[j]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j+1)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Plunderer
class PlundererDownload(Winter2020AnimeDownload):
    title = "Plunderer"
    keywords = ["Plunderer"]

    PAGE_PREFIX = "http://plunderer-info.com/"
    CHAR_DAI = "\\xe7\\xac\\xac" #第
    CHAR_WA = "\\xe8\\xa9\\xb1" #話
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/plunderer"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.PAGE_PREFIX)
            split1 = response.split('<h1 class="news_ttl">')
            for i in range(1, len(split1), 1):
                split2 = split1[i].split('</h1>')[0]
                if self.CHAR_DAI in split2 and self.CHAR_WA in split2:
                    split3 = split2.split(self.CHAR_WA)[0].split(self.CHAR_DAI)
                    if len(split3) < 2:
                        continue
                else:
                    continue
                episode = ''
                try:
                    episode_temp = int(split3[1])
                    episode = str(episode_temp).zfill(2)
                except:
                    continue
                if self.is_file_exists(self.base_folder + "/" + episode + "_01.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_01.png"):
                    continue
                split4 = split1[i].split('<ul class="bxslider')
                if len(split4) < 2:
                    continue
                split5 = split4[1].split('</ul>')[0].split('<img src="')
                for j in range(1, len(split5), 1):
                    imageUrl = self.PAGE_PREFIX + split5[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j).zfill(2)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Rikei ga Koi ni Ochita no de Shoumei shitemita.
class RikekoiDownload(Winter2020AnimeDownload):
    title = "Rikei ga Koi ni Ochita no de Shoumei shitemita."
    keywords = ["Rikekoi", "Rikei ga Koi ni Ochita no de Shoumei shitemita.",
                "Science Fell in Love, So I Tried to Prove It"]

    PAGE_PREFIX = "https://rikekoi.com"
    STORY_PAGE = "https://rikekoi.com/story/1"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/rikekoi"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE, decode=True)
            split1 = response.split('<div class="story-link-item this-page">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('<u class="red-marker">')[0].split('<a href="')
            for i in range(1, len(split2), 1):
                page_url = self.PAGE_PREFIX + split2[i].split('"')[0]
                episode = ''
                try:
                    split3 = page_url.split('/')
                    if len(split3) < 2:
                        continue
                    episode_temp = int(split3[len(split3) - 1])
                except:
                    continue
                episode = str(episode_temp).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                if episode_temp == 1:
                    page_response = response
                else:
                    page_response = self.get_response(page_url, decode=True)
                imageUrls = []
                
                # First image
                split4 = page_response.split('<figure class="wp-block-image"><a href="')
                if len(split4) < 2:
                    continue
                firstImageUrl = split4[1].split('</figure>')[0].split('"')[0]
                
                # Other images
                split5 = page_response.split('<ul class="wp-block-gallery columns-5 is-cropped">')
                if len(split5) < 2:
                    continue
                split6 = split5[1].split('</ul>')[0].split('<a href="')
                for j in range(1, len(split6), 1):
                    imageUrl = split6[j].split('"')[0]
                    imageUrls.append(imageUrl)
                
                firstImageUrlReplaced = firstImageUrl.replace('-1024x576','')
                filepathWithoutExtension = self.base_folder + "/" + episode + "_1"
                self.download_image(firstImageUrlReplaced, filepathWithoutExtension)
                
                for k in range(len(imageUrls)):
                    imageUrl = imageUrls[k].replace('-1024x576','')
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(k+2)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Runway de Waratte
class RunwayDeWaratteDownload(Winter2020AnimeDownload):
    title = "Runway de Waratte"
    keywords = ["Runway de Waratte", "Smile Down the Runway"]

    STORY_PAGE = "https://runway-anime.com/introduction/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/runway"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<p class="episode">')
            for i in range(1, len(split1), 1):
                episode = ''
                try:
                    episode = str(int(split1[i].split('</p>')[0].replace('EPISODE.',''))).zfill(2)
                except:
                    continue
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                split2 = split1[i].split('</ul>')[0].split('src="')
                for j in range(1, len(split2), 1):
                    imageUrl = split2[j].split('"')[0].replace('-1024x576','')
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Somali to Mori no Kamisama
class SomaliDownload(Winter2020AnimeDownload):
    title = "Somali to Mori no Kamisama"
    keywords = ["Somali to Mori no Kamisama", "Somali and the Forest Spirit"]

    PAGE_PREFIX = "https://somali-anime.com/"
    STORY_PAGE = "https://somali-anime.com/story.html"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/somali"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<div class="contents_container story">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('<a href="')
            for i in range(2, len(split2), 1):
                split3 = split2[i].split('"')[0]
                episode = ''
                try:
                    episode_temp = int(split3.split('.html')[0].split('story')[1])
                    episode = str(episode_temp).zfill(2)
                except Exception as e:
                    continue
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                page_url = self.PAGE_PREFIX + split3
                page_response = self.get_response(page_url)
                split4 = page_response.split('<div class="cp_slide_item"><img src="')
                for j in range(1, len(split4), 1):
                    imageUrl = self.PAGE_PREFIX + split4[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)
        WebNewtypeScanner('ソマリと森の神様',self.base_folder).run()


# Toaru Kagaku no Railgun T
class RailgunTDownload(Winter2020AnimeDownload):
    title = "Toaru Kagaku no Railgun T"
    keywords = ["Toaru Kagaku no Railgun T", "A Certain Scientific Railgun T"]
    
    PAGE_PREFIX = "https://toaru-project.com/railgun_t/"
    STORY_PAGE = "https://toaru-project.com/railgun_t/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/railgun-t"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        self.download_episode_preview()
        self.download_bluray()
        self.download_character()

    def download_episode_preview(self):
        try:
            response = self.get_response(self.STORY_PAGE)
            split1 = response.split('<table summary="List_Type01">')
            if len(split1) < 2:
                return
            split2 = split1[1].split('</table>')[0].split('<a href="../')
            for i in range(len(split2) - 2, 0, -1):
                page_url = self.PAGE_PREFIX + split2[i].split('"')[0]
                split3 = page_url.split('.html')[0]
                episode = ''
                if len(split3) < 2:
                    continue
                try:
                    episode_num = int(split3[-2:])
                    episode = str(episode_num).zfill(2)
                except:
                    continue
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                    continue
                page_response = self.get_response(page_url)
                split4 = page_response.split('<ul class="tp5">')
                if len(split4) < 2:
                    continue
                split5 = split4[1].split('</ul>')[0].split('<a href="../')
                for j in range(1, len(split5), 1):
                    imageUrl = self.PAGE_PREFIX + split5[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_bluray(self):
        bluray_filepath = self.base_folder + '/' + constants.FOLDER_BLURAY
        if not os.path.exists(bluray_filepath):
            os.makedirs(bluray_filepath)

        for i in range(8):
            volume = i + 1
            if volume == 1:
                url = 'https://toaru-project.com/railgun_t/bd/'
            else:
                url = 'https://toaru-project.com/railgun_t/bd/%s.html' % str(volume).zfill(2)
            try:
                filename_without_extension = bluray_filepath + '/bd_' + str(volume)
                if os.path.exists(filename_without_extension + '.jpg') or os.path.exists(
                        filename_without_extension + '.png'):
                    continue
                bd_soup = self.get_soup(url)
                image_url = self.PAGE_PREFIX + bd_soup.find('div', class_='ph').find('img')['src'].replace('../', '')
                content_length = requests.head(image_url).headers['Content-Length']
                if content_length == '163509': # preview image
                    continue
                self.download_image(image_url, filename_without_extension)
            except Exception as e:
                print("Error in running " + self.__class__.__name__ + ' - Blu-Ray')
                print(e)

        # Blu-ray Bonus / Music
        url_list = ['https://toaru-project.com/railgun_t/bd/privilege.html',
                    'https://toaru-project.com/railgun_t/music/']
        for url in url_list:
            soup = self.get_soup(url)
            image_objs = []
            try:
                images = soup.find('div', id='cms_block').find_all('img')
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].split('?')[0].replace('../', '')
                    content_length = requests.head(image_url).headers['Content-Length']
                    if content_length == '121984': # preview image
                        continue
                    image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                    image_objs.append({'name': image_name, 'url': image_url})
            except:
                pass
            self.download_image_objects(image_objs, bluray_filepath)

    def download_character(self):
        folder = self.create_character_directory()
        image_objs = []
        try:
            soup = self.get_soup('https://toaru-project.com/railgun_t/chara/')
            chara_list = soup.find('div', id='main_inner').find_all('div', class_='nwu_box')
            for chara in chara_list:
                chara_url = self.PAGE_PREFIX + chara.find('a')['href'].replace('../', '')
                chara_name = chara_url.split('/')[-1].split('.html')[0]
                picture_filepath = folder + '/' + chara_name + '_body'
                if os.path.exists(picture_filepath + '.jpg') or os.path.exists(picture_filepath + '.png'):
                    continue
                chara_soup = self.get_soup(chara_url)

                chara_body = chara_soup.find('div', class_='charaBody')
                if chara_body is not None:
                    chara_body_image_url = self.PAGE_PREFIX + chara_body.find('img')['src'].replace('../', '')
                    chara_body_name = chara_name + '_body'
                    image_objs.append({'name': chara_body_name, 'url': chara_body_image_url})

                chara_face = chara_soup.find('div', class_='charaFace')
                if chara_face is not None:
                    chara_face_image_url = self.PAGE_PREFIX + chara_face.find('img')['src'].replace('../', '')
                    chara_face_name = chara_name + '_face'
                    image_objs.append({'name': chara_face_name, 'url': chara_face_image_url})
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)
        self.download_image_objects(image_objs, folder)


# Toaru Kagaku no Railgun T
'''
class RailgunTDownload2(Winter2020AnimeDownload):

    #https://toaru-project.com/railgun_t/core_sys/images/contents/00000014/block/00000021/00000030.jpg
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/railgun-t-forced"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        template = "https://toaru-project.com/railgun_t/core_sys/images/contents/%s/block/%s/%s.jpg"
        try:
            first = 14
            second = 21
            k = 30
            for i in range(12):
                episode = str(i+1).zfill(2)
                for j in range(6):
                    imageUrl = template % (str(first+i).zfill(8),str(second+i).zfill(8),str(k).zfill(8))
                    filepathWithoutExtension = self.base_folder + "/" + episode + "_" + str(j+1)
                    k += 1
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)
'''
