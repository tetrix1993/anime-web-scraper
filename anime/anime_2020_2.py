import os
import re
from anime.main_download import MainDownload
from datetime import datetime
from scan import WebNewtypeScanner
from scan import MocaNewsScanner

# Arte http://arte-anime.com/ #アルテ @arte_animation [SUN]
# BNA https://bna-anime.com/story/ #ビーエヌエー @bna_anime [THU]
# Gleipnir http://gleipnir-anime.com/ #グレイプニル @gleipnir_anime [MON]
# Hachi-nan tte http://hachinan-anime.com/story/ #八男 #hachinan @Hachinan_PR [WED]
# Honzuki S2 http://booklove-anime.jp/story/ #本好きの下剋上 @anime_booklove [MON]
# Houkago Teibou Nisshi https://teibotv.com/ #teibo @teibo_bu [MON]
# Kaguya-sama S2 https://kaguya.love/ #かぐや様 @anime_kaguya [SAT]
# Kakushigoto https://kakushigoto-anime.com/ #かくしごと @kakushigoto_pr [TUE]
# Kingdom S3 https://kingdom-anime.com/story/ #キングダム @kingdom_animePR [THU]
# Otome Game https://hamehura-anime.com/story/ #はめふら #hamehura @hamehura [WED]
# Namiyo https://namiyo-anime.com/story/ #波よ聞いてくれ #namiyo [WED]
# Princess Connect https://anime.priconne-redive.jp/story/ #アニメプリコネ #プリコネR #プリコネ @priconne_anime [FRI]
# Shachibato https://shachibato-anime.com/story.html #シャチバト #shachibato @schbt_anime [TUE]
# Tamayomi https://tamayomi.com/story/ #tamayomi @tamayomi_PR [WED]
# Tsugumomo S2 http://tsugumomo.com/story/ #つぐもも @tsugumomo_anime [FRI]
# Yesterday wo Utatte https://singyesterday.com/ #イエスタデイをうたって @anime_yesterday [FRI]


# Spring 2020 Anime
class Spring2020AnimeDownload(MainDownload):
    season = "2020-2"
    season_name = "Spring 2020"

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/2020-2"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)


# Arte
class ArteDownload(Spring2020AnimeDownload):
    title = "Arte"
    keywords = ["Arte"]

    PAGE_PREFIX = "http://arte-anime.com/"
    IMAGE_TEMPLATE = 'http://arte-anime.com/U1y9gMfZ/wp-content/themes/arte/images/story/img%s_%s.jpg'
    FINAL_EPISODE = 13
    IMAGES_PER_EPISODE = 5

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/arte"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                    self.base_folder + "/" + episode + "_1.png"):
                continue
            for j in range(self.IMAGES_PER_EPISODE):
                image_url = self.IMAGE_TEMPLATE % (episode, str(j + 1).zfill(2))
                file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1)
                result = self.download_image(image_url, file_path_without_extension)
                if result == -1:
                    break
            if result == -1:
                break

        '''
        soup = self.get_soup(self.PAGE_PREFIX)
        story_mob = soup.find_all('div', class_='story_mob')
        regex = '#[０|１|２|３|４|５|６|７|８|９|0-9]+'
        prog = re.compile(regex)
        for story in story_mob:
            h4_tag_text = story.find('h4', class_='st_ntit').text.strip()
            result = prog.match(h4_tag_text)
            if result is None:
                continue
            episode = str(int(result.group(0).split('#')[1])).zfill(2)
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                    self.base_folder + "/" + episode + "_1.png"):
                continue
            st_smlist = story.find_all('div', class_='st_smlist')
            for j in range(len(st_smlist)):
                image_url = st_smlist[j].find('img')['src']
                file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1)
                self.download_image(image_url, file_path_without_extension)
        '''


# Brand New Animal
class BrandNewAnimalDownload(Spring2020AnimeDownload):
    title = "Brand New Animal"
    keywords = ["BNA", "Brand New Animal"]

    STORY_PAGE = "https://bna-anime.com/story/"
    IMAGE_TEMPLATE = 'https://bna-anime.com/story/images/%s_%s.jpg'
    TOTAL_EPISODES = 24
    TOTAL_IMAGES_PER_EPISODE = 8

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/bna"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        soup = self.get_soup(self.STORY_PAGE)
        ep_list = soup.find('ul', id='storyList').find_all('li')
        for ep in ep_list:
            try:
                episode = self.get_episode_number(ep.find('span', class_='cn').text)
                if episode is None:
                    continue
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                        self.base_folder + "/" + episode + "_1.png"):
                    continue
                ep_url = self.STORY_PAGE + ep.find('a')['href']
                ep_soup = self.get_soup(ep_url)
                images = ep_soup.find('ul', {'class': ['imgClick', 'cf']}).find_all('img')
                for j in range(len(images)):
                    image_url = self.STORY_PAGE + images[j]['src']
                    file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1)
                    self.download_image(image_url, file_path_without_extension)
            except:
                continue

        for i in range(self.TOTAL_EPISODES):
            episode = str(i + 1).zfill(2)
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                    self.base_folder + "/" + episode + "_1.png"):
                continue
            for j in range(self.TOTAL_IMAGES_PER_EPISODE):
                image_url = self.IMAGE_TEMPLATE % (str(i + 1), str(j + 1))
                file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1)
                result = self.download_image(image_url, file_path_without_extension)
                if result == -1:
                    return


# Gleipnir
class GleipnirDownload(Spring2020AnimeDownload):
    title = "Gleipnir"
    keywords = ["Gleipnir"]
    
    PAGE_PREFIX = "http://gleipnir-anime.com"
    STORY_PAGE = 'http://gleipnir-anime.com/story/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/gleipnir"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        soup = self.get_soup(self.STORY_PAGE)
        stories = soup.find('section', class_='storyNavi').find_all('li')
        for story in stories:
            story_url_tag = story.find('a')
            episode = self.get_episode_number(story_url_tag.text)
            if episode is None:
                continue
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                    self.base_folder + "/" + episode + "_1.png"):
                continue
            story_url = self.PAGE_PREFIX + story_url_tag['href']
            story_soup = self.get_soup(story_url)
            images = story_soup.find('section', class_='story_slider').find_all('img')
            for j in range(len(images)):
                image_url = images[j]['src'].replace('-1024x576', '')
                file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1)
                self.download_image(image_url, file_path_without_extension)
        WebNewtypeScanner('グレイプニル', self.base_folder).run()


# Hachi-nan tte, Sore wa Nai deshou!
class HachinanDownload(Spring2020AnimeDownload):
    title = "Hachi-nan tte, Sore wa Nai deshou!"
    keywords = ["Hachi-nan tte, Sore wa Nai deshou!", "Hachinan", "The 8th Son? Are You Kidding Me?"]
    
    PAGE_PREFIX = "http://hachinan-anime.com"
    STORY_PAGE = "http://hachinan-anime.com/story/"
    TOTAL_EPISODES = 13
    IMAGES_PER_EPISODE = 6
    IMAGE_TEMPLATE = 'http://hachinan-anime.com/wp-content/themes/hachinan-anime/images/story/%s-%s.jpg'
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/hachinan"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        soup = self.get_soup(self.STORY_PAGE)
        a_tags = soup.find('nav', class_='l-nav').find_all('a')
        for a_tag in a_tags:
            episode = self.get_episode_number(a_tag.text)
            if episode is None:
                continue
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                continue
            story_soup = self.get_soup(self.PAGE_PREFIX + a_tag['href'])
            images = story_soup.find('ul', class_='capture').find_all('img')
            for j in range(len(images)):
                image_url = self.PAGE_PREFIX + images[j]['src']
                file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1)
                self.download_image(image_url, file_path_without_extension)

        # Download Blu-ray pictures
        image_urls = []
        other_filepath = self.base_folder + '/' + 'other'
        if not os.path.exists(other_filepath):
            os.makedirs(other_filepath)
        url_list = ["http://hachinan-anime.com/bd/",
                    "http://hachinan-anime.com/bd/bd-special/",
                    "http://hachinan-anime.com/bd/campaign/"]
        for url in url_list:
            bd_soup = self.get_soup(url)
            try:
                images = bd_soup.find('section', class_='bdvdArea').find_all('img')
                for image in images:
                    image_urls.append(self.PAGE_PREFIX + image['src'])
            except:
                pass

        music_soup = self.get_soup("http://hachinan-anime.com/music/")
        try:
            music_sections = music_soup.find_all('section', class_='musicArea')
            for music_section in music_sections:
                images = music_section.find_all('img')
                for image in images:
                    image_url = image['src']
                    if 'http://' not in image_url and 'https://' not in image_url:
                        image_url = self.PAGE_PREFIX + image_url
                    image_urls.append(image_url)
        except:
            pass

        for image_url in image_urls:
            try:
                image_filename = image_url.split('/')[-1]
                file_path_without_extension = other_filepath + '/' + image_filename.split('.jpg')[0].split('.jpeg')[0].split('.png')[0]
                if os.path.exists(other_filepath + '/' + image_filename):
                    self.download_image_if_exists(image_url, file_path_without_extension, other_filepath + '/' + image_filename)
                    continue
                self.download_image(image_url, file_path_without_extension)
            except Exception as e:
                print(e)
                pass


# Honzuki no Gekokujou: Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen 2nd Season
class Honzuki2Download(Spring2020AnimeDownload):
    title = "Honzuki no Gekokujou: Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen 2nd Season"
    keywords = ["Honzuki no Gekokujou: Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen 2nd Season",
                "Ascendance of a Bookworm"]
    
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

        template = 'http://booklove-anime.jp/img/story/ep%s/img%s.jpg'
        episode = 14
        result = 0
        while True:
            episode += 1
            if self.is_file_exists(self.base_folder + "/" + str(episode) + "_1.jpg") or self.is_file_exists(
                    self.base_folder + "/" + str(episode) + "_1.png"):
                continue
            for j in range(6):
                image_url = template % (str(episode), str(j + 1).zfill(2))
                file_path_without_extension = self.base_folder + '/' + str(episode) + '_' + str(j + 1)
                result = self.download_image(image_url, file_path_without_extension)
                if result == -1 or result is None:
                    break
            if result == -1 or result is None:
                break

        last_date = datetime.strptime('20200630', '%Y%m%d')
        today = datetime.today()
        if today < last_date:
            end_date = today
        else:
            end_date = last_date
        MocaNewsScanner('本好きの下剋上', self.base_folder, '20200401', end_date.strftime('%Y%m%d')).run()


# Nami yo Kiitekure
class NamiyoDownload(Spring2020AnimeDownload):
    title = "Nami yo Kiitekure"
    keywords = ["Namiyo", "Nami yo Kiitekure", "Wave, Listen to Me!"]

    STORY_PAGE = 'https://namiyo-anime.com/story/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/namiyo"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        soup = self.get_soup(self.STORY_PAGE)
        stories = soup.find('ul', class_='l-episode-list').find_all('li', class_='l-episode-item')
        ep_num = 0
        for story in stories:
            ep_num += 1
            episode = str(ep_num).zfill(2)
            if self.is_file_exists(self.base_folder + "/" + str(episode) + "_1.jpg") or self.is_file_exists(
                    self.base_folder + "/" + str(episode) + "_1.png"):
                continue
            images = story.find_all('div', class_='swiper-slide')
            for j in range(len(images)):
                image_url = images[j].find('img')['src']
                file_path_without_extension = self.base_folder + '/' + str(episode) + '_' + str(j + 1)
                self.download_image(image_url, file_path_without_extension)


# Houkago Teibou Nisshi
class TeiboDownload(Spring2020AnimeDownload):
    title = "Houkago Teibou Nisshi"
    keywords = ["Teibo", "Houkago Teibou Nisshi", "Diary of Our Days at the Breakwater"]

    PAGE_PREFIX = "https://teibotv.com/"
    STORY_PAGE = 'https://teibotv.com/story.html'
    IMAGE_TEMPLATE = 'https://teibotv.com/images/story/%s/p_%s.jpg'

    TOTAL_EPISODES = 13
    TOTAL_IMAGES_PER_EPISODE = 6

    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/teibo"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        soup = self.get_soup(self.STORY_PAGE)
        story_thumb_boxes = soup.find_all('div', class_='story_thumb_box')
        for story_thumb_box in story_thumb_boxes:
            try:
                content = str(story_thumb_box.find('div', class_='title'))
                split1 = content.split('<span')[0].split('"title">')[1].split('れぽーと')[1]
                episode = str(int(split1)).zfill(2)
            except:
                continue
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_1.png"):
                continue
            story_url = story_thumb_box.find('a')['href']
            story_soup = self.get_soup(self.PAGE_PREFIX + story_url)
            images = story_soup.find('ol', class_='main').find_all('img')
            for j in range(len(images)):
                image_url = self.PAGE_PREFIX + images[j]['src']
                file_path_without_extension = self.base_folder + '/' + str(episode) + '_' + str(j + 1)
                self.download_image(image_url, file_path_without_extension)

        for i in range(self.TOTAL_EPISODES):
            episode = str(i + 1).zfill(2)
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                    self.base_folder + "/" + episode + "_1.png"):
                continue
            for j in range(self.TOTAL_IMAGES_PER_EPISODE):
                image_url = self.IMAGE_TEMPLATE % (str(i + 1).zfill(3), str(j).zfill(3))
                file_path_without_extension = self.base_folder + '/' + str(episode) + '_' + str(j + 1)
                result = self.download_image(image_url, file_path_without_extension)
                if result == -1 or result is None:
                    return



# Kaguya-sama wa Kokurasetai? Tensai-tachi no Renai Zunousen
class Kaguyasama2Download(Spring2020AnimeDownload):
    title = "Kaguya-sama wa Kokurasetai?: Tensai-tachi no Renai Zunousen"
    keywords = ["Kaguya", "Kaguyasama", "Kaguya-sama wa Kokurasetai?: Tensai-tachi no Renai Zunousen",
                "Kaguya-sama: Love is War 2nd Season"]

    STORY_PAGE = "https://kaguya.love/story/"
    PAGE_PREFIX = 'https://kaguya.love'
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/kaguya-sama2"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        soup = self.get_soup(self.STORY_PAGE)
        story_nav = soup.find('div', class_='p-story_nav').find_all('a')
        for story_tag in story_nav:
            try:
                page_url = self.PAGE_PREFIX + story_tag['href']
                episode = str(int(story_tag.text)).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                        self.base_folder + "/" + episode + "_1.png"):
                    continue
                page_soup = self.get_soup(page_url)
                story_div = page_soup.find('div', class_='p-story__main')
                li_tags = story_div.find_all('li', class_='scene_item')
                for j in range(len(li_tags)):
                    image_url = self.STORY_PAGE + li_tags[j].find('img')['src']
                    file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1)
                    self.download_image(image_url, file_path_without_extension)
            except:
                continue

        # Download Blu-ray/Music
        image_urls = []
        other_filepath = self.base_folder + '/' + 'other'
        if not os.path.exists(other_filepath):
            os.makedirs(other_filepath)
        url_list = ["https://kaguya.love/bddvd/",
                    "https://kaguya.love/bddvd/02.html",
                    "https://kaguya.love/bddvd/03.html",
                    "https://kaguya.love/bddvd/04.html",
                    "https://kaguya.love/bddvd/05.html",
                    "https://kaguya.love/bddvd/06.html"]
        for url in url_list:
            bd_soup = self.get_soup(url)
            try:
                images = bd_soup.find('div', class_='p-bddvd').find_all('img')
                for image in images:
                    image_url = image['src'].replace('../..', '')
                    if 'http://' not in image_url and 'https://' not in image_url:
                        image_url = self.PAGE_PREFIX + image_url
                    image_urls.append(image_url)
            except:
                pass

        url_list = ["https://kaguya.love/music/opening/",
                    "https://kaguya.love/music/ending/",
                    "https://kaguya.love/music/charasong/"]
        for url in url_list:
            music_soup = self.get_soup(url)
            try:
                images = music_soup.find('div', class_='p-music').find_all('img')
                for image in images:
                    image_url = image['src'].replace('../..', '')
                    if 'http://' not in image_url and 'https://' not in image_url:
                        image_url = self.PAGE_PREFIX + image_url
                    image_urls.append(image_url)
            except:
                pass

        for image_url in image_urls:
            try:
                image_filename = image_url.split('/')[-1]
                if os.path.exists(other_filepath + '/' + image_filename):
                    continue
                file_path_without_extension = other_filepath + '/' + \
                    image_filename.split('.jpg')[0].split('.jpeg')[0].split('.png')[0]
                self.download_image(image_url, file_path_without_extension)
            except:
                pass

        # Download character image
        chara_filepath = self.base_folder + '/chara'
        if not os.path.exists(chara_filepath):
            os.makedirs(chara_filepath)
        chara_image_templates = [self.PAGE_PREFIX + '/assets/img/chara/img_chara%s.png',
                                 self.PAGE_PREFIX + '/assets/img/chara/img_face%s-1.png',
                                 self.PAGE_PREFIX + '/assets/img/chara/img_face%s-2.png']
        num_of_characters = 10
        for i in range(len(chara_image_templates)):
            for j in range(num_of_characters):
                image_url = chara_image_templates[i] % str(j + 1).zfill(2)
                filename = image_url.split('/')[-1].replace('.jpg', '').replace('.png', '')
                filepath = chara_filepath + '/' + filename
                if not os.path.exists(filepath + '.jpg') or os.path.exists(filepath + '.png'):
                    self.download_image(image_url, filepath)


# Kakushigoto
class KakushigotoDownload(Spring2020AnimeDownload):
    title = "Kakushigoto"
    keywords = ["Kakushigoto"]

    STORY_PAGE = "https://kakushigoto-anime.com/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/kakushigoto"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        soup = self.get_soup(self.STORY_PAGE)
        contents = soup.find_all('div', class_='story_tab_content')
        for content in contents:
            episode = ''
            try:
                episode = str(int(content['id'])).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                        self.base_folder + "/" + episode + "_1.png"):
                    continue
                image_divs = content.find_all('div', class_='swiper-slide')
                for j in range(len(image_divs)):
                    image_url = image_divs[j].find('img')['src']
                    file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1)
                    self.download_image(image_url, file_path_without_extension)
            except:
                continue


# Kingdom 3rd Season
class Kingdom3Download(Spring2020AnimeDownload):
    title = "Kingdom 3rd Season"
    keywords = ["Kingdom 3rd Season"]

    STORY_PAGE = "https://kingdom-anime.com/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/kingdom3"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        soup = self.get_soup(self.STORY_PAGE)
        ep_list = soup.find('ul', id='ep_list').find_all('li')
        for ep in ep_list:
            try:
                episode = self.get_episode_number(ep.find('span', class_='hd').text)
                if episode is None:
                    continue
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                        self.base_folder + "/" + episode + "_1.png"):
                    continue
                ep_url = self.STORY_PAGE + ep.find('a')['href']
                ep_soup = self.get_soup(ep_url)
                images = ep_soup.find('div', id='episodeCont').find_all('img')
                for j in range(len(images)):
                    image_url = images[j]['src']
                    file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1)
                    self.download_image(image_url, file_path_without_extension)
            except:
                continue


# Otome Game no Hametsu Flag shika Nai Akuyaku Reijou ni Tensei shiteshimatta...
class HamehuraDownload(Spring2020AnimeDownload):
    title = "Otome Game no Hametsu Flag shika Nai Akuyaku Reijou ni Tensei shiteshimatta..."
    keywords = ["Hamehura", "Otome Game no Hametsu Flag shika Nai Akuyaku Reijou ni Tensei shiteshimatta...",
                "My Next Life as a Villainess: All Routes Lead to Doom!"]

    STORY_PAGE = "https://hamehura-anime.com/story"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/hamehura"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        soup = self.get_soup(self.STORY_PAGE)
        story_content = soup.find_all('div', class_='story_content')
        for story in story_content:
            title = story.find('p', class_='orn_ttl').text
            episode = self.get_episode_number(title)
            if episode is None:
                continue
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                    self.base_folder + "/" + episode + "_1.png"):
                continue
            swiper_slide = story.find_all('div', class_='swiper-slide')
            for j in range(len(swiper_slide)):
                image_url = swiper_slide[j].find('img')['src']
                file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1)
                self.download_image(image_url, file_path_without_extension)

        '''
        self.base_folder += "_hidden"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
        image_template = "https://hamehura-anime.com/wp/wp-content/uploads/2020/%s/%s.jpg"
        for i in range(3, 7):
            month = str(i).zfill(2)
            for j in range(6):
                image_num = str(j + 1).zfill(2)
                for k in range(12):
                    if k == 0:
                        image_url = image_template % (month, image_num)
                    else:
                        image_url = image_template % (month, image_num + '-' + str(k))
                    file_path_without_extension = self.base_folder + '/' + month + '_' + image_num + '_' + str(k)
                    self.download_image(image_url, file_path_without_extension)
        '''


# Princess Connect! Re:Dive
class PriconneDownload(Spring2020AnimeDownload):
    title = "Princess Connect! Re:Dive"
    keywords = ["Princess Connect! Re:Dive", "Priconne"]
    
    PAGE_PREFIX = "https://anime.priconne-redive.jp"
    STORY_PREFIX = "https://anime.priconne-redive.jp/story/"
    STORY_TEMPLATE = "https://anime.priconne-redive.jp/story/?id=%s"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/priconne"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        soup = self.get_soup(self.STORY_PREFIX)
        latest_episode_text = soup.find('ul', class_='story-num').find('li', class_='active').text
        prog = re.compile('[0-9]+')
        result = prog.findall(latest_episode_text)
        max_episode = int(result[0])
        for i in range(max_episode):
            episode = str(i + 1).zfill(2)
            if self.is_file_exists(self.base_folder + "/" + episode + "_01.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_01.png"):
                continue
            try:
                story_soup = self.get_soup(self.STORY_TEMPLATE % episode)
                img_list = story_soup.find('ul', class_='img-list')
                images = img_list.find_all('img')
                for j in range(len(images)):
                    image_url = self.PAGE_PREFIX + images[j]['src'].replace('-840x472', '')
                    file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1).zfill(2)
                    self.download_image(image_url, file_path_without_extension)
            except:
                continue

        # Download characters
        chara_filepath = self.base_folder + '/chara'
        if not os.path.exists(chara_filepath):
            os.makedirs(chara_filepath)
        chara_soup = self.get_soup('https://anime.priconne-redive.jp/character/')
        full_image_urls = []
        thumb_image_urls = []
        chara_names = []
        try:
            main_lis = chara_soup.find('ul', class_='main-list').find_all('li')
            for li in main_lis:
                chara_names.append(li.find('p', class_='name').text)
                full_image_urls.append(self.PAGE_PREFIX + li.find('a')['href'])
                thumb_image_urls.append(self.PAGE_PREFIX + li.find('img')['src'])
            sub_lis = chara_soup.find('ul', class_='sub-list').find_all('li')
            for li in sub_lis:
                chara_names.append(li.find('p', class_='name').text)
                full_image_urls.append(self.PAGE_PREFIX + li.find('a')['href'])
                thumb_image_urls.append(self.PAGE_PREFIX + li.find('img')['src'])
        except:
            pass
        if len(full_image_urls) == len(thumb_image_urls) == len(chara_names):
            for i in range(len(full_image_urls)):
                full_image_filepath = chara_filepath + '/f_' + chara_names[i]
                thumb_image_filepath = chara_filepath + '/t_' + chara_names[i]
                self.download_image(full_image_urls[i], full_image_filepath)
                self.download_image(thumb_image_urls[i], thumb_image_filepath)


# Shachou, Battle no Jikan Desu!
class ShachibatoDownload(Spring2020AnimeDownload):
    title = "Shachou, Battle no Jikan Desu!"
    keywords = ["Shachou, Battle no Jikan Desu!", "Shachibato! President, It's Time for Battle!"]

    PAGE_PREFIX = "https://shachibato-anime.com/"
    STORY_PAGE = "https://shachibato-anime.com/story.html"
    IMAGE_TEMPLATE = 'https://shachibato-anime.com/img/story/story-episode%s-img-%s.jpg'
    TOTAL_EPISODES = 25
    TOTAL_IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/shachibato"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        soup = self.get_soup(self.STORY_PAGE)
        story_list = soup.find('ul', class_='story_navi').find_all('a')
        for story in story_list:
            episode = self.get_episode_number(story.text)
            if episode is None:
                continue
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

        result = 0
        for i in range(self.TOTAL_EPISODES):
            episode = str(i + 1).zfill(2)
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                    self.base_folder + "/" + episode + "_1.png"):
                continue
            for j in range(self.TOTAL_IMAGES_PER_EPISODE):
                image_url = self.IMAGE_TEMPLATE % (episode, str(j + 1).zfill(2))
                file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1)
                result = self.download_image(image_url, file_path_without_extension)
                if result == -1:
                    break
            if result == -1:
                break

        image_urls = []
        other_filepath = self.base_folder + '/' + 'other'
        if not os.path.exists(other_filepath):
            os.makedirs(other_filepath)
        url_list = ["https://shachibato-anime.com/bluray.html",
                    "https://shachibato-anime.com/music.html"]
        for url in url_list:
            bd_soup = self.get_soup(url)
            try:
                images = bd_soup.find('div', class_='container1').find_all('img')
                for image in images:
                    image_url = image['src']
                    if 'http://' not in image_url and 'https://' not in image_url:
                        image_url = self.PAGE_PREFIX + image_url
                    image_urls.append(image_url)
            except:
                pass

        for image_url in image_urls:
            try:
                image_filename = image_url.split('/')[-1]
                if os.path.exists(other_filepath + '/' + image_filename):
                    continue
                file_path_without_extension = other_filepath + '/' + \
                    image_filename.split('.jpg')[0].split('.jpeg')[0].split('.png')[0]
                self.download_image(image_url, file_path_without_extension)
            except:
                pass

        # Download characters
        chara_filepath = self.base_folder + '/chara'
        if not os.path.exists(chara_filepath):
            os.makedirs(chara_filepath)
        chara_soup = self.get_soup('https://shachibato-anime.com/character.html')
        image_urls = []
        try:
            lis = chara_soup.find('ul', class_='panel').find_all()
            for li in lis:
                visual_div = li.find('div', class_='visual')
                if visual_div is not None:
                    image_urls.append(self.PAGE_PREFIX + visual_div.find('img')['src'])
                face_div = li.find('div', class_='face')
                if face_div is not None:
                    face_images = face_div.find_all('img')
                    for face_img in face_images:
                        image_urls.append(self.PAGE_PREFIX + face_img['src'])
                visual2_div = li.find('div', class_='visual2')
                if visual2_div is not None:
                    image_urls.append(self.PAGE_PREFIX + visual2_div.find('img')['src'])
        except:
            pass
        for image_url in image_urls:
            filename = image_url.split('/')[-1].replace('.jpg', '').replace('.png', '')
            file_path_without_extension = chara_filepath + '/' + filename
            self.download_image(image_url, file_path_without_extension)


# Tamayomi
class TamayomiDownload(Spring2020AnimeDownload):
    title = "Tamayomi"
    keywords = ["Tamayomi"]

    PAGE_PREFIX = "https://tamayomi.com"
    STORY_PREFIX = "https://tamayomi.com/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/tamayomi"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        soup = self.get_soup(self.STORY_PREFIX)
        stories = soup.find('ul', class_='story-storybox_thumbs').find_all('li', class_='story-storybox_thumbs_item')
        for story in stories:
            story_title = story.find('p', class_='story-storybox_thumbs_title').text
            episode = self.get_episode_number(story_title, prefix='第', suffix='球')
            if episode is None:
                continue
            if self.is_file_exists(self.base_folder + "/" + episode + "_0.jpg") or self.is_file_exists(self.base_folder + "/" + episode + "_0.png"):
                continue
            story_url = self.STORY_PREFIX + story.find('a')['href']
            story_soup = self.get_soup(story_url)
            images = story_soup.find('div', class_='story-detbox_main').find_all('img')
            for j in range(len(images)):
                image_url = images[j]['src']
                file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1).zfill(2)
                self.download_image(image_url, file_path_without_extension)

        image_urls = []
        other_filepath = self.base_folder + '/' + 'other'
        if not os.path.exists(other_filepath):
            os.makedirs(other_filepath)
        url_list = ["https://tamayomi.com/discography/detail.php?id=1017453",
                    "https://tamayomi.com/discography/detail.php?id=1017468",
                    "https://tamayomi.com/discography/detail.php?id=1017553",
                    "https://tamayomi.com/discography/detail.php?id=1017554",
                    "https://tamayomi.com/discography/detail.php?id=1017555",
                    "https://tamayomi.com/discography/detail.php?id=1017556"]
        for url in url_list:
            bd_soup = self.get_soup(url)
            try:
                images = bd_soup.find('div', class_='disc-single').find_all('img')
                for image in images:
                    image_url = image['src']
                    if 'http://' not in image_url and 'https://' not in image_url:
                        image_url = self.PAGE_PREFIX + image_url
                    image_urls.append(image_url)
            except:
                pass

        for image_url in image_urls:
            try:
                image_filename = image_url.split('/')[-1]
                if os.path.exists(other_filepath + '/' + image_filename):
                    continue
                file_path_without_extension = other_filepath + '/' + \
                    image_filename.split('.jpg')[0].split('.jpeg')[0].split('.png')[0]
                self.download_image(image_url, file_path_without_extension)
            except:
                pass

        # Download characters
        chara_filepath = self.base_folder + '/chara'
        if not os.path.exists(chara_filepath):
            os.makedirs(chara_filepath)

        image_urls = []
        chara_soup = self.get_soup("https://tamayomi.com/character/")
        class_names = ['character-thumbs_imageArea', 'character-modal_item_headerFace', 'character-modal_item_imagebox']
        for class_name in class_names:
            try:
                div_tags = chara_soup.find_all('div', class_=class_name)
                for div_tag in div_tags:
                    image_url = div_tag.find('img')['src']
                    if image_url[0:3] == "../":
                        image_url = self.PAGE_PREFIX + image_url[2:]
                    image_urls.append(image_url)
            except:
                pass

        for image_url in image_urls:
            filename = image_url.split('/')[-1].replace('.jpg', '').replace('.png', '')
            file_path_without_extension = chara_filepath + '/' + filename
            self.download_image(image_url, file_path_without_extension)


# Tsugu Tsugumomo
class Tsugumomo2Download(Spring2020AnimeDownload):
    title = "Tsugu Tsugumomo"
    keywords = ["Tsugumomo"]

    STORY_PAGE = "http://tsugumomo.com/story/"
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/tsugumomo2"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        soup = self.get_soup(self.STORY_PAGE)
        ep_li = soup.find_all('div', class_='l-sub-title')
        ep_num = 0
        for ep in ep_li:
            ep_num += 1
            episode = str(ep_num).zfill(2)
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                    self.base_folder + "/" + episode + "_1.png"):
                continue
            images = ep.find('div', class_='inner').find_all('img')
            for j in range(len(images)):
                image_url = images[j]['src']
                file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1).zfill(2)
                self.download_image(image_url, file_path_without_extension)


# Yesterday wo Utatte
class YesterdayDownload(Spring2020AnimeDownload):
    title = "Yesterday wo Utatte"
    keywords = ["Yesterday wo Utatte", "Sing Yesterday For Me"]

    STORY_PAGE = "https://singyesterday.com/story/"
    PAGE_PREFIX = 'https://singyesterday.com/'
    IMAGE_TEMPLATE = 'https://singyesterday.com/cmn/images/story/%s/yd_%s_%s.jpg'
    TOTAL_EPISODES = 18
    TOTAL_IMAGES_PER_EPISODE = 10
    
    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/yesterday"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
    
    def run(self):
        for i in range(self.TOTAL_EPISODES):
            episode = str(i + 1).zfill(2)
            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                continue
            is_first_image = True
            for j in range(self.TOTAL_IMAGES_PER_EPISODE):
                if j == 1:
                    is_first_image = False
                image_url = self.IMAGE_TEMPLATE % (episode, episode, str(j + 1).zfill(2))
                file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1)
                result = self.download_image(image_url, file_path_without_extension)
                if result == -1:
                    break
            if result == -1 and is_first_image:
                break
        WebNewtypeScanner('イエスタデイをうたって', self.base_folder).run()

