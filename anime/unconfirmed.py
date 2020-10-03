import os
import anime.constants as constants
from anime.main_download import MainDownload

# Bokutachi no Remake http://bokurema.com/ #ぼくリメ #bokurema @bokurema
# Cheat Kusushi no Slow Life: Isekai ni Tsukurou Drugstore https://www.cheat-kusushi.jp/ #チート薬師 #スローライフ @cheat_kusushi
# Ijiranaide, Nagatoro-san https://www.nagatorosan.jp/ #長瀞さん @nagatoro_tv
# Kaifuku Jutsushi no Yarinaoshi http://kaiyari.com/ #回復術士 @kaiyari_anime
# Kobayashi-san Chi no Maid Dragon S https://maidragon.jp/2nd/ #maidragon @maidragon_anime
# Mushoku Tensei https://mushokutensei.jp/ #無職転生 @mushokutensei_A
# Osananajimi ga Zettai ni Makenai Love Comedy https://osamake.com/ #おさまけ
# Princess Connect! Re:Dive S2 https://anime.priconne-redive.jp/ #アニメプリコネ #プリコネR #プリコネ @priconne_anime
# Tate no Yuusha S2 http://shieldhero-anime.jp/ #shieldhero #盾の勇者の成り上がり @shieldheroanime


# Unconfirmed Season Anime
class UnconfirmedDownload(MainDownload):
    season = "9999-9"
    season_name = "Unconfirmed"

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/unconfirmed"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)


# Cheat Kusushi no Slow Life: Isekai ni Tsukurou Drugstore
class CheatKusushiDownload(UnconfirmedDownload):
    title = 'Cheat Kusushi no Slow Life: Isekai ni Tsukurou Drugstore'
    keywords = [title, 'Cheat Pharmacist\'s Slow Life: Making a Drugstore in Another World']

    PAGE_PREFIX = 'https://www.cheat-kusushi.jp/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/cheat-kusushi"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_key_visual(self):
        keyvisual_folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'teaser', 'url': 'https://www.cheat-kusushi.jp/img/top-main.png'}]
        self.download_image_objects(image_objs, keyvisual_folder)


# Ijiranaide, Nagatoro-san
class NagatorosanDownload(UnconfirmedDownload):
    title = 'Ijiranaide, Nagatoro-san'
    keywords = [title, 'Nagatorosan']

    PAGE_PREFIX = 'https://www.nagatorosan.jp/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/nagatoro-san"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'teaser', 'url': 'https://pbs.twimg.com/media/Eb6NC6rU0AAoaUm?format=jpg&name=medium'},
            {'name': 'mainimg', 'url': 'https://www.nagatorosan.jp/images/mainimg.jpg'}
        ]
        self.download_image_objects(image_objs, folder)

    def download_character(self):
        folder = self.create_character_directory()
        image_objs = [
            {'name': 'img_nagatoro', 'url': 'https://www.nagatorosan.jp/images/img_nagatoro.png'}
        ]
        self.download_image_objects(image_objs, folder)


# Kaifuku Jutsushi no Yarinaoshi
class KaiyariDownload(UnconfirmedDownload):
    title = "Kaifuku Jutsushi no Yarinaoshi"
    keywords = [title, "Kaiyari", "Redo of Healer"]

    PAGE_PREFIX = "http://kaiyari.com/"

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/kaiyari"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [{'name': 'announce', 'url': 'http://kaiyari.com/teaser/images/top-main-vis.jpg'},
            {'name': 'announce_2', 'url': 'https://pbs.twimg.com/media/EJ0V4iwVUAE-Ep7?format=jpg&name=medium'},
            {'name': 'teaser', 'url': 'http://kaiyari.com/teaser/images/top-main-vis2.jpg'},
            {'name': 'teaser_2', 'url': 'https://pbs.twimg.com/media/EaizJUOU8AATcDK?format=jpg&name=medium'}]
        self.download_image_objects(image_objs, folder)


# Kobayashi-san Chi no Maid Dragon S
class KobayashiMaidDragon2Download(UnconfirmedDownload):
    title = 'Kobayashi-san Chi no Maid Dragon S'
    keywords = [title, "Miss Kobayashi's Maid Dragon"]

    PAGE_PREFIX = 'https://maidragon.jp/2nd/'

    def __init__(self):
        super().__init__()
        self.init_base_folder('maidragon2')

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


# Mushoku Tensei: Isekai Ittara Honki Dasu
class MushokuTenseiDownload(UnconfirmedDownload):
    title = "Mushoku Tensei: Isekai Ittara Honki Dasu"
    keywords = [title, 'Jobless Reincarnation']

    PAGE_PREFIX = 'https://mushokutensei.jp/'

    def __init__(self):
        super().__init__()
        self.init_base_folder('mushoku-tensei')

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'teaser', 'url': 'https://pbs.twimg.com/media/EHKOHakU4AUq-A3?format=jpg&name=large'},
            {'name': 'kv1', 'url': 'https://pbs.twimg.com/media/Ea3MiJFU0AETcOY?format=jpg&name=4096x4096'}
        ]
        self.download_image_objects(image_objs, folder)

    def download_character(self):
        folder = self.create_character_directory()
        image_objs = []
        try:
            soup = self.get_soup('https://mushokutensei.jp/character/')
            charaslides = soup.find_all('div', class_='charaslide')
            for charaslide in charaslides:
                slideclasses = ['charaslide_img', 'charaslide_data_img']
                for slideclass in slideclasses:
                    slide_img = charaslide.find('div', class_=slideclass)
                    if slide_img is not None and slide_img.has_attr('data-imgload'):
                        image_url = slide_img['data-imgload']
                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                        image_objs.append({'name': image_name, 'url': image_url})
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)
        self.download_image_objects(image_objs, folder)


# Osananajimi ga Zettai ni Makenai Love Comedy
class OsamakeDownload(UnconfirmedDownload):
    title = 'Osananajimi ga Zettai ni Makenai Love Comedy'
    keywords = [title, 'Osamake']

    PAGE_PREFIX = 'https://osamake.com/'

    def __init__(self):
        super().__init__()
        self.init_base_folder('osamake')

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

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

    PAGE_PREFIX = "https://anime.priconne-redive.jp"

    def __init__(self):
        super().__init__()
        self.init_base_folder('priconne2')

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [{'name': 'teaser', 'url': 'https://anime.priconne-redive.jp/assets/images/top_kv.png'}]
        self.download_image_objects(image_objs, folder)


# Tate no Yuusha no Nariagari S2
class TateNoYuusha2Download(UnconfirmedDownload):
    title = "Tate no Yuusha no Nariagari 2nd Season"
    keywords = [title, "The Rising of the Shield Hero"]

    PAGE_PREFIX = "http://shieldhero-anime.jp"

    def __init__(self):
        super().__init__()
        self.init_base_folder('tate-no-yuusha2')

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'announce', 'url': 'https://pbs.twimg.com/media/EDag4MkUwAAQnf0?format=jpg&name=medium'},
            {'name': 'kv1', 'url': 'https://pbs.twimg.com/media/EhHFvyVU4AA7cUw?format=jpg&name=large'}
        ]
        self.download_image_objects(image_objs, folder)
