import os
import anime.constants as constants
from anime.main_download import MainDownload
from datetime import datetime
from scan import AniverseMagazineScanner, MocaNewsScanner, WebNewtypeScanner


# Genjitsu Shugi Yuusha no Oukoku Saikenki https://genkoku-anime.com/ #現国アニメ @genkoku_info


# Summer 2021 Anime
class Summer2021AnimeDownload(MainDownload):
    season = "2021-3"
    season_name = "Summer 2021"
    folder_name = '2021-3'

    def __init__(self):
        super().__init__()


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
