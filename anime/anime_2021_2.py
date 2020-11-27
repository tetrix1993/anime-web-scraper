import os
import anime.constants as constants
from anime.main_download import MainDownload
from datetime import datetime
from scan import AniverseMagazineScanner, MocaNewsScanner, WebNewtypeScanner


# Hige wo Soru. Soshite Joshikousei wo Hirou. http://higehiro-anime.com/ #higehiro #ひげひろ @higehiro_anime
# Ijiranaide, Nagatoro-san https://www.nagatorosan.jp/ #長瀞さん @nagatoro_tv
# Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita https://slime300-anime.com/ #スライム倒して300年 @slime300_PR
# Yakunara Mug Cup mo https://yakumo-project.com/ #やくもtv @yakumo_project


# Spring 2021 Anime
class Spring2021AnimeDownload(MainDownload):
    season = "2021-2"
    season_name = "Spring 2021"
    folder_name = '2021-2'

    def __init__(self):
        super().__init__()


# Hige wo Soru. Soshite Joshikousei wo Hirou.
class HigehiroDownload(Spring2021AnimeDownload):
    title = 'Hige wo Soru. Soshite Joshikousei wo Hirou.'
    keywords = [title, 'Higehiro']
    folder_name = 'higehiro'

    PAGE_PREFIX = 'http://higehiro-anime.com/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index', diff=2)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/EjO4FTcU0AIPm2X?format=jpg&name=medium')
        self.add_to_image_list('kv_sayu', 'http://higehiro-anime.com/wp-content/themes/higehiro/images/kv_sayu.png')
        self.add_to_image_list('kv_yoshida', 'http://higehiro-anime.com/wp-content/themes/higehiro/images/kv_yoshida.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        soup = self.get_soup(self.PAGE_PREFIX)
        try:
            self.image_list = []
            lis = soup.find_all('li', class_='thumbnail-item')
            for li in lis:
                image = li.find('img')
                if image and image.has_attr('src'):
                    image_url = image['src'].split('?')[0]
                    image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)

            slide_lis = soup.find_all('li', class_='slide-item')
            for li in slide_lis:
                images = li.find_all('img')
                for image in images:
                    if image.has_attr('src'):
                        image_url = image['src'].split('?')[0]
                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                        self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)


# Ijiranaide, Nagatoro-san
class NagatorosanDownload(Spring2021AnimeDownload):
    title = 'Ijiranaide, Nagatoro-san'
    keywords = [title, 'Nagatorosan']
    folder_name = 'nagatoro-san'

    PAGE_PREFIX = 'https://www.nagatorosan.jp/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'teaser', 'url': 'https://pbs.twimg.com/media/Eb6NC6rU0AAoaUm?format=jpg&name=medium'},
            {'name': 'mainimg', 'url': 'https://www.nagatorosan.jp/images/mainimg.jpg'},
            {'name': 'kv1', 'url': 'https://pbs.twimg.com/media/EmIPL3dU0AABjQI?format=jpg&name=medium'},
            {'name': 'kv1_2', 'url': 'https://www.nagatorosan.jp/img/top/mainimg.jpg'},
        ]
        self.download_image_objects(image_objs, folder)

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        self.add_to_image_list('img_nagatoro', 'https://www.nagatorosan.jp/images/img_nagatoro.png')
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            sliders =soup.find_all('div', class_='swiper-slide')
            for slider in sliders:
                images = slider.find_all('img')
                for image in images:
                    if image.has_attr('src'):
                        image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                        self.add_to_image_list(image_name, image_url)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)
        self.download_image_list(folder)


# Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita
class Slime300Download(Spring2021AnimeDownload):
    title = "Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita"
    keywords = [title, "I've Been Killing Slimes for 300 Years and Maxed Out My Level", "Slime 300"]
    folder_name = 'slime300'

    PAGE_PREFIX = 'https://slime300-anime.com'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'keyvisual01', 'url': self.PAGE_PREFIX + '/static/8e3ba0a8b42628959e71b7f52c737a6a/eeb1b/keyvisual01.png'},
            {'name': 'keyvisual02', 'url': self.PAGE_PREFIX + '/static/b915596c773e96cb35385563193752e8/eeb1b/keyvisual02.png'},
        ]
        self.download_image_objects(image_objs, folder)

    def download_character(self):
        folder = self.create_character_directory()
        image_objs = []
        chara_json = 'https://slime300-anime.com/page-data/sq/d/2919095229.json'
        try:
            json_obj = self.get_json(chara_json)
            data_obj = json_obj['data']
            for data in data_obj.keys():
                try:
                    image_url = self.PAGE_PREFIX + data_obj[data]['childImageSharp']['fluid']['src']
                    image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                    image_objs.append({'name': image_name, 'url': image_url})
                except:
                    pass
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)
        self.download_image_objects(image_objs, folder)

# Yakunara Mug Cup mo
class YakunaraMugCupMo(Spring2021AnimeDownload):
    title = "Yakunara Mug Cup mo"
    keywords = [title, 'Yakumo', "Let's Make a Mug Too"]
    folder_name = 'yakumo'

    PAGE_PREFIX = 'https://yakumo-project.com/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'news/images/200729_01.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        for i in range(20):
            image_url = 'https://yakumo-project.com/images/character_%sfull.png' % str(i + 1)
            image_name = self.extract_image_name_from_url(image_url, with_extension=False)
            if self.is_image_exists(image_name, folder):
                continue
            result = self.download_image(image_url, folder + '/' + image_name)
            if result == -1:
                break
