import os
import anime.constants as constants
from anime.main_download import MainDownload
from datetime import datetime
from scan import AniverseMagazineScanner, MocaNewsScanner, WebNewtypeScanner


# Cheat Kusushi no Slow Life: Isekai ni Tsukurou Drugstore https://www.cheat-kusushi.jp/ #チート薬師 #スローライフ @cheat_kusushi
# Genjitsu Shugi Yuusha no Oukoku Saikenki https://genkoku-anime.com/ #現国アニメ @genkoku_info
# Kobayashi-san Chi no Maid Dragon S https://maidragon.jp/2nd/ #maidragon @maidragon_anime
# Meikyuu Black Company https://meikyubc-anime.com/ #迷宮ブラックカンパニー @meikyubc_anime
# Otome Game https://hamehura-anime.com/story/ #はめふら #hamehura @hamehura
# Peach Boy Riverside https://peachboyriverside.com/ #ピーチボーイリバーサイド @peachboy_anime
# Sekai Saikou no Ansatsusha, Isekai Kizoku ni Tensei suru https://ansatsu-kizoku.jp/ #暗殺貴族 @ansatsu_kizoku
# Shiroi Suna no Aquatope https://aquatope-anime.com/ #白い砂のアクアトープ @aquatope_anime


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


# Kobayashi-san Chi no Maid Dragon S
class KobayashiMaidDragon2Download(Summer2021AnimeDownload):
    title = 'Kobayashi-san Chi no Maid Dragon S'
    keywords = [title, "Miss Kobayashi's Maid Dragon"]
    folder_name = 'maidragon2'

    PAGE_PREFIX = 'https://maidragon.jp/2nd/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index', diff=2)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/EfEVvJEUwAI6LmD?format=jpg&name=large')
        self.add_to_image_list('teaser_covid', 'https://pbs.twimg.com/media/EfEVvJEUwAI6LmD?format=jpg&name=large')
        self.add_to_image_list('newyear_2021', 'https://pbs.twimg.com/media/EqkvG-lUcAInMkK?format=jpg&name=4096x4096')
        self.add_to_image_list('kv1_1', 'https://pbs.twimg.com/media/Ervaz89VEAkqjT-?format=jpg&name=900x900')
        self.add_to_image_list('kv1_2', 'https://maidragon.jp/2nd/img/pre/visual_02.png')
        self.download_image_list(folder)


# Meikyuu Black Company
class MeikyuBCDownload(Summer2021AnimeDownload):
    title = 'Meikyuu Black Company'
    keywords = [title, "The Dungeon of Black Company"]
    folder_name = 'meikyubc'

    PAGE_PREFIX = 'https://meikyubc-anime.com/'

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/Es40z-1UYAAg7_x?format=jpg&name=medium')
        self.download_image_list(folder)


# Otome Game no Hametsu Flag shika Nai Akuyaku Reijou ni Tensei shiteshimatta... X
class Hamehura2Download(Summer2021AnimeDownload):
    title = "Otome Game no Hametsu Flag shika Nai Akuyaku Reijou ni Tensei shiteshimatta... X"
    keywords = [title, "Hamehura", "Hamefura", "My Next Life as a Villainess: All Routes Lead to Doom!", "2nd"]
    folder_name = 'hamehura2'

    PAGE_PREFIX = 'https://hamehura-anime.com/'
    IMAGE_PREFIX = 'https://hamehura-anime.com/2nd/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', self.IMAGE_PREFIX + 'wp-content/uploads/2021/01/はめふらX_ティザービジュアル-1.jpg')
        #self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/EsJL9ZQVkAEDktJ?format=jpg&name=large')
        self.download_image_list(folder)


# Peach Boy Riverside
class PeachBoyRiverside(Summer2021AnimeDownload):
    title = 'Peach Boy Riverside'
    keywords = [title]
    folder_name = 'peachboyriverside'

    PAGE_PREFIX = 'https://peachboyriverside.com/'

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
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'wp/wp-content/themes/peachboyriverside_main/_assets/images/top/fv/fv_pc.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        image_name_template = 'char_main_%s@2x'
        url_template = self.PAGE_PREFIX + 'wp/wp-content/themes/peachboyriverside_main/_assets/images/pages/char/main/'\
            + image_name_template + '.png'
        try:
            for i in range(1, 100, 1):
                image_name = image_name_template % str(i).zfill(3)
                if self.is_image_exists(image_name, folder):
                    continue
                url = url_template % str(i).zfill(3)
                result = self.download_image(url, folder + '/' + image_name)
                if result == -1:
                    break
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)


# Sekai Saikou no Ansatsusha, Isekai Kizoku ni Tensei suru
class AnsatsuKizokuDownload(Summer2021AnimeDownload):
    title = 'Sekai Saikou no Ansatsusha, Isekai Kizoku ni Tensei suru'
    keywords = [title, "The world's best assassin, To reincarnate in a different world aristocrat"]
    folder_name = 'ansatsu-kizoku'

    PAGE_PREFIX = 'https://ansatsu-kizoku.jp/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')


# Shiroi Suna no Aquatobe
class AquatopeDownload(Summer2021AnimeDownload):
    title = 'Shiroi Suna no Aquatope'
    keywords = [title, 'Aquatope of White Sand']
    folder_name = 'aquatope'

    PAGE_PREFIX = 'https://aquatope-anime.com/'

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
        self.add_to_image_list('teaser_tw', 'https://pbs.twimg.com/media/ErwuT7rVQAISak1?format=jpg&name=large')
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'wp/wp-content/themes/aquatope-teaser/_assets/images/kv/kv_pc@2x.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            articles = soup.find_all('article', class_='char--slider--block')
            for article in articles:
                pictures = article.find_all('picture')
                for picture in pictures:
                    source = picture.find('source')
                    if source and source.has_attr('srcset'):
                        try:
                            image_url = source['srcset'].split(',')[-1].split(' ')[0]
                            image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                            self.add_to_image_list(image_name, image_url)
                        except:
                            continue
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)
        self.download_image_list(folder)
