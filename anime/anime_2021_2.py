import os
import anime.constants as constants
from anime.main_download import MainDownload
from datetime import datetime
from scan import AniverseMagazineScanner, MocaNewsScanner, WebNewtypeScanner


# Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita https://slime300-anime.com/


# Spring 2021 Anime
class Spring2021AnimeDownload(MainDownload):
    season = "2021-2"
    season_name = "Spring 2021"

    def __init__(self):
        super().__init__()
        self.init_base_folder('2021-2')


# Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita
class Slime300Download(Spring2021AnimeDownload):
    title = "Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita"
    keywords = [title, "I've Been Killing Slimes for 300 Years and Maxed Out My Level", "Slime 300"]

    PAGE_PREFIX = 'https://slime300-anime.com'

    def __init__(self):
        super().__init__()
        self.init_base_folder('slime300')

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
