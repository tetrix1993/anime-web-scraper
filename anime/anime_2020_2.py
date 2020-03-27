import os
import re
from anime.main_download import MainDownload

# Arte http://arte-anime.com/ #アルテ @arte_animation
# Gleipnir http://gleipnir-anime.com/ #グレイプニル @gleipnir_anime
# Hachi-nan tte http://hachinan-anime.com/story/ #八男 #hachinan @Hachinan_PR
# Honzuki S2 http://booklove-anime.jp/story/ #本好きの下剋上 @anime_booklove
# Houkago Teibou Nisshi https://teibotv.com/ #teibo @teibo_bu
# Kaguya-sama S2 https://kaguya.love/ #かぐや様 @anime_kaguya
# Kakushigoto https://kakushigoto-anime.com/ #かくしごと @kakushigoto_pr
# Kingdom S3 https://kingdom-anime.com/story/ #キングダム @kingdom_animePR
# Otome Game https://hamehura-anime.com/story/ #はめふら #hamehura @hamehura
# Princess Connect https://anime.priconne-redive.jp/ #アニメプリコネ #プリコネR #プリコネ @priconne_anime
# Shachibato https://shachibato-anime.com/story.html #シャチバト #shachibato @schbt_anime
# Tamayomi https://tamayomi.com/story/ #tamayomi @tamayomi_PR
# Tsugumomo S2 http://tsugumomo.com/story/ #つぐもも @tsugumomo_anime
# Yahari Ore no Seishun http://www.tbs.co.jp/anime/oregairu/story/ #俺ガイル #oregairu @anime_oregairu
# Yesterday wo Utatte https://singyesterday.com/ #イエスタデイをうたって @anime_yesterday


# Spring 2020 Anime
class Spring2020AnimeDownload(MainDownload):
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/2020-2"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)


# Arte
class ArteDownload(Spring2020AnimeDownload):

    PAGE_PREFIX = "http://arte-anime.com/"

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/arte"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        pass


# Gleipnir
class GleipnirDownload(Spring2020AnimeDownload):
    
    PAGE_PREFIX = "http://gleipnir-anime.com/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/gleipnir"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass


# Hachi-nan tte, Sore wa Nai deshou!
class HachinanDownload(Spring2020AnimeDownload):
    
    PAGE_PREFIX = "http://hachinan-anime.com"
    STORY_PAGE = "http://hachinan-anime.com/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/hachinan"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        story_area_sect = str(self.get_soup(self.STORY_PAGE).find('section', class_='storyArea'))
        split1 = story_area_sect.split('<p class="number-stories">')
        for i in range(1, len(split1), 1):
            episode = ''
            try:
                ep_num = int(split1[i].split('</p>')[0].split('</span>')[0].split('<span>')[1])
                episode = str(ep_num).zfill(2)
            except:
                continue
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                continue
            split2 = split1[i].split('<li><img src="')
            for j in range(1, len(split2), 1):
                image_url = self.PAGE_PREFIX + split2[j].split('"/></li>')[0]
                file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j)
                self.download_image(image_url, file_path_without_extension)


# Honzuki no Gekokujou: Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen 2nd Season
class Honzuki2Download(Spring2020AnimeDownload):
    
    PAGE_PREFIX = "http://booklove-anime.jp/story/"
    IMAGE_PREFIX = "http://booklove-anime.jp/"
    FIRST_EPISODE = 15
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/honzuki2"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        ep_num = self.FIRST_EPISODE - 1
        box_story_divs = self.get_soup(self.PAGE_PREFIX).find('section', id='second').find_all('div', class_='box_story')
        for box_story_div in box_story_divs:
            if 'intro02' in box_story_div['class']:
                continue
            ep_num += 1
            episode = str(ep_num)
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                continue
            lis = box_story_div.find_all('li')
            for j in range(len(lis)):
                img = lis[j].find('img')
                image_url = self.IMAGE_PREFIX + img['src'].replace('../', '')
                file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1)
                self.download_image(image_url, file_path_without_extension)


# Houkago Teibou Nisshi
class TeiboDownload(Spring2020AnimeDownload):

    PAGE_PREFIX = "https://teibotv.com/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/teibo"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass


# Kaguya-sama wa Kokurasetai? Tensai-tachi no Renai Zunousen
class Kaguyasama2Download(Spring2020AnimeDownload):

    PAGE_PREFIX = "https://teibotv.com/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/kaguya-sama2"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass


# Kakushigoto
class KakushigotoDownload(Spring2020AnimeDownload):

    PAGE_PREFIX = "https://kakushigoto-anime.com/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/kakushigoto"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass


# Kingdom 3rd Season
class Kingdom3Download(Spring2020AnimeDownload):

    PAGE_PREFIX = "https://kingdom-anime.com/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/kingdom3"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass


# Otome Game no Hametsu Flag shika Nai Akuyaku Reijou ni Tensei shiteshimatta...
class HamehuraDownload(Spring2020AnimeDownload):

    PAGE_PREFIX = "https://hamehura-anime.com/story"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/hamehura"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass


# Princess Connect! Re:Dive
class PriconneDownload(Spring2020AnimeDownload):
    
    PAGE_PREFIX = "https://anime.priconne-redive.jp"
    STORY_PREFIX = "https://anime.priconne-redive.jp/story/";
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/priconne"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        soup = self.get_soup(self.STORY_PREFIX)
        img_list = soup.find_all('ul', class_='img-list')
        for i in range(len(img_list)):
            episode = str(i + 1).zfill(2)
            if self.is_file_exists(self.base_folder + "/" + episode + "_01.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_01.png"):
                continue
            images = img_list[i].find_all('img')
            for j in range(len(images)):
                image_url = self.PAGE_PREFIX + images[j]['src'].replace('-840x472', '')
                file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1).zfill(2)
                self.download_image(image_url, file_path_without_extension)


# Shachou, Battle no Jikan Desu!
class ShachibatoDownload(Spring2020AnimeDownload):

    PAGE_PREFIX = "https://shachibato-anime.com/"
    STORY_PAGE = "https://shachibato-anime.com/story.html"

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/shachibato"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        soup = self.get_soup(self.STORY_PAGE)
        prog = re.compile('第[0-9]+話')
        story_list = soup.find('ul', class_='story_navi').find_all('a')
        for story in story_list:
            result = prog.match(story.text)
            if result is None:
                continue
            episode = result.group(0).split('話')[0].split('第')[1].zfill(2)
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                    self.base_folder + "/" + episode + "_1.png"):
                continue
            story_url = self.PAGE_PREFIX + story['href']
            story_soup = self.get_soup(story_url)
            images = story_soup.find('div', class_='slider-for').find_all('img')
            for j in range(len(images)):
                image_url = self.PAGE_PREFIX + images[j]['src'].replace('../', '')
                file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1)
                self.download_image(image_url, file_path_without_extension)



# Tamayomi
class TamayomiDownload(Spring2020AnimeDownload):

    PAGE_PREFIX = "https://tamayomi.com/"
    STORY_PREFIX = "https://tamayomi.com/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/tamayomi"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        soup = self.get_soup(self.STORY_PREFIX)
        stories = soup.find('ul', class_='story-storybox_thumbs').find_all('li', class_='story-storybox_thumbs_item')
        for i in range(len(stories)):
            episode = str(i + 1).zfill(2)
            if self.is_file_exists(self.base_folder + "/" + episode + "_0.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_0.png"):
                continue
            story_url = self.STORY_PREFIX + stories[i].find('a')['href']
            story_soup = self.get_soup(story_url)
            images = story_soup.find('div', class_='story-detbox_main').find_all('img')
            for j in range(len(images)):
                image_url = images[j]['src']
                file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1).zfill(2)
                self.download_image(image_url, file_path_without_extension)


# Tsugu Tsugumomo
class Tsugumomo2Download(Spring2020AnimeDownload):

    PAGE_PREFIX = "http://tsugumomo.com/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/tsugumomo2"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass


# Yahari Ore no Seishun Love Comedy wa Machigatteiru. Kan
class Oregairu3Download(Spring2020AnimeDownload):

    PAGE_PREFIX = "http://www.tbs.co.jp/anime/oregairu/"
    STORY_PAGE = "http://www.tbs.co.jp/anime/oregairu/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/oregairu3"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        soup = self.get_soup(self.STORY_PAGE, decode=True)
        story_nav = soup.find('ul', class_='story-nav')
        chapters = story_nav.find_all('li')
        for chapter in chapters:
            try:
                link_tag = chapter.find('a')
                link_text = link_tag.text
                if '第' in link_text and '話' in link_text:
                    episode = link_text.split('話')[0].split('第')[1].zfill(2)
                    if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                        continue
                    episode_link = self.STORY_PAGE + link_tag['href']
                    episode_soup = self.get_soup(episode_link)
                    image_tags = episode_soup.find('ul', class_='slides').find_all('img')
                    j = 0
                    for image_tag in image_tags:
                        j += 1
                        image_url = self.STORY_PAGE + image_tag['src']
                        file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j)
                        self.download_image(image_url, file_path_without_extension)
            except:
                continue


# Yesterday wo Utatte
class YesterdayDownload(Spring2020AnimeDownload):

    PAGE_PREFIX = "https://singyesterday.com/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/yesterday"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        pass
