import os
import anime.constants as constants
from anime.main_download import MainDownload
from datetime import datetime
from scan import AniverseMagazineScanner, MocaNewsScanner, WebNewtypeScanner


# Cheat Kusushi no Slow Life: Isekai ni Tsukurou Drugstore https://www.cheat-kusushi.jp/ #チート薬師 #スローライフ @cheat_kusushi
# Genjitsu Shugi Yuusha no Oukoku Saikenki https://genkoku-anime.com/ #現国アニメ @genkoku_info


# Summer 2021 Anime
class Summer2021AnimeDownload(MainDownload):
    season = "2021-3"
    season_name = "Summer 2021"
    folder_name = '2021-3'

    def __init__(self):
        super().__init__()


# Cheat Kusushi no Slow Life: Isekai ni Tsukurou Drugstore
class CheatKusushiDownload(Summer2021AnimeDownload):
    title = 'Cheat Kusushi no Slow Life: Isekai ni Tsukurou Drugstore'
    keywords = [title, 'Cheat Pharmacist\'s Slow Life: Making a Drugstore in Another World']
    folder_name = 'cheat-kusushi'

    PAGE_PREFIX = 'https://www.cheat-kusushi.jp/'

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
        self.add_to_image_list('teaser', 'https://www.cheat-kusushi.jp/img/top-main.png')
        self.add_to_image_list('kv1', 'https://cheat-kusushi.jp/assets/img/bg/top.png')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/EqTAkcgU8AAe39d?format=jpg&name=large')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            article = soup.find('article', id='js-scroll-to-CHARACTER')
            if article:
                containers = article.find_all('div', class_='container')
                for container in containers:
                    if len(container['class']) > 1:
                        continue
                    images = container.find_all('img')
                    for image in images:
                        if image.has_attr('src'):
                            image_url = self.PAGE_PREFIX + image['src']
                            image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                            self.add_to_image_list(image_name, image_url)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)
        self.download_image_list(folder)


# Genjitsu Shugi Yuusha no Oukoku Saikenki
class GenkokuDownload(Summer2021AnimeDownload):
    title = "Genjitsu Shugi Yuusha no Oukoku Saikenki"
    keywords = [title, "Genkoku"]
    folder_name = 'genkoku'

    PAGE_PREFIX = 'https://genkoku-anime.com/'

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
        self.add_to_image_list('teaser', 'https://genkoku-anime.com/teaser/images/mainimg.png')
        self.add_to_image_list(name='teaser_moca',
                               url='https://moca-news.net/article/20201104/2020110410000a_/image/001-i2casw.jpg',
                               is_mocanews=True)
        self.download_image_list(folder)

    def download_character(self):
        pass
