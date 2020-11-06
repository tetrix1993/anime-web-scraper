import os
import anime.constants as constants
from anime.main_download import MainDownload

# Bokutachi no Remake http://bokurema.com/ #ぼくリメ #bokurema @bokurema
# Cheat Kusushi no Slow Life: Isekai ni Tsukurou Drugstore https://www.cheat-kusushi.jp/ #チート薬師 #スローライフ @cheat_kusushi
# Hige wo Soru. Soshite Joshikousei wo Hirou. http://higehiro-anime.com/ #higehiro #ひげひろ @higehiro_anime
# Kobayashi-san Chi no Maid Dragon S https://maidragon.jp/2nd/ #maidragon @maidragon_anime
# Osananajimi ga Zettai ni Makenai Love Comedy https://osamake.com/ #おさまけ
# Princess Connect! Re:Dive S2 https://anime.priconne-redive.jp/ #アニメプリコネ #プリコネR #プリコネ @priconne_anime
# Tate no Yuusha S2 http://shieldhero-anime.jp/ #shieldhero #盾の勇者の成り上がり @shieldheroanime


# Unconfirmed Season Anime
class UnconfirmedDownload(MainDownload):
    season = "9999-9"
    season_name = "Unconfirmed"
    folder_name = 'unconfirmed'

    def __init__(self):
        super().__init__()


# Cheat Kusushi no Slow Life: Isekai ni Tsukurou Drugstore
class CheatKusushiDownload(UnconfirmedDownload):
    title = 'Cheat Kusushi no Slow Life: Isekai ni Tsukurou Drugstore'
    keywords = [title, 'Cheat Pharmacist\'s Slow Life: Making a Drugstore in Another World']
    folder_name = 'cheat-kusushi'

    PAGE_PREFIX = 'https://www.cheat-kusushi.jp/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_key_visual(self):
        keyvisual_folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'teaser', 'url': 'https://www.cheat-kusushi.jp/img/top-main.png'}]
        self.download_image_objects(image_objs, keyvisual_folder)


# Hige wo Soru. Soshite Joshikousei wo Hirou.
class HigehiroDownload(UnconfirmedDownload):
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
        self.has_website_updated(self.PAGE_PREFIX, 'index')

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


# Kobayashi-san Chi no Maid Dragon S
class KobayashiMaidDragon2Download(UnconfirmedDownload):
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
        pass
        #self.has_website_updated(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [{'name': 'teaser', 'url': 'https://pbs.twimg.com/media/EfEVvJEUwAI6LmD?format=jpg&name=large'},
                      {'name': 'teaser_covid', 'url': 'https://galleryamh2home.files.wordpress.com/2020/02/1597072728776.jpg'}]
        self.download_image_objects(image_objs, folder)


# Osananajimi ga Zettai ni Makenai Love Comedy
class OsamakeDownload(UnconfirmedDownload):
    title = 'Osananajimi ga Zettai ni Makenai Love Comedy'
    keywords = [title, 'Osamake']
    folder_name = 'osamake'

    PAGE_PREFIX = 'https://osamake.com/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'teaser', 'url': 'https://osamake.com/assets/top/main-t1b/vis.jpg'},
            #{'name': 'teaser', 'url': 'https://pbs.twimg.com/media/EjZnt4CUcAIJeqR?format=jpg&name=4096x4096'},
        ]
        self.download_image_objects(image_objs, folder)


# Princess Connect! Re:Dive 2nd Season
class Priconne2Download(UnconfirmedDownload):
    title = "Princess Connect! Re:Dive 2nd Season"
    keywords = [title, "Priconne"]
    folder_name = 'priconne2'

    PAGE_PREFIX = "https://anime.priconne-redive.jp"

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [{'name': 'teaser', 'url': 'https://anime.priconne-redive.jp/assets/images/top_kv.png'}]
        self.download_image_objects(image_objs, folder)


# Tate no Yuusha no Nariagari S2
class TateNoYuusha2Download(UnconfirmedDownload):
    title = "Tate no Yuusha no Nariagari 2nd Season"
    keywords = [title, "The Rising of the Shield Hero"]
    folder_name = 'tate-no-yuusha2'

    PAGE_PREFIX = "http://shieldhero-anime.jp"

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'announce', 'url': 'https://pbs.twimg.com/media/EDag4MkUwAAQnf0?format=jpg&name=medium'},
            {'name': 'kv1', 'url': 'https://pbs.twimg.com/media/EhHFvyVU4AA7cUw?format=jpg&name=large'}
        ]
        self.download_image_objects(image_objs, folder)
