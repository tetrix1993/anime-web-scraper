import os
import anime.constants as constants
from anime.main_download import MainDownload

# Bokutachi no Remake http://bokurema.com/ #ぼくリメ #bokurema @bokurema
# Cheat Kusushi no Slow Life: Isekai ni Tsukurou Drugstore https://www.cheat-kusushi.jp/ #チート薬師 #スローライフ @cheat_kusushi
# Gotoubun no Hanayome S2 https://www.tbs.co.jp/anime/5hanayome/ #五等分の花嫁 @5Hanayome_anime
# Ijiranaide, Nagatoro-san https://www.nagatorosan.jp/ #長瀞さん @nagatoro_tv
# Kaifuku Jutsushi no Yarinaoshi http://kaiyari.com/ #回復術士 @kaiyari_anime
# Kobayashi-san Chi no Maid Dragon S https://maidragon.jp/2nd/ #maidragon @maidragon_anime
# Mushoku Tensei https://mushokutensei.jp/ #無職転生 @mushokutensei_A
# Ore dake Haireru Kakushi Dungeon https://kakushidungeon-anime.jp/ #隠しダンジョン @kakushidungeon
# Princess Connect! Re:Dive S2 https://anime.priconne-redive.jp/ #アニメプリコネ #プリコネR #プリコネ @priconne_anime
# Tatoeba Last Dungeon https://lasdan.com/ #ラスダン @lasdan_PR


# Unconfirmed Season Anime
class UnconfirmedDownload(MainDownload):
    season = "9999-9"
    season_name = "Unconfirmed"

    PAGE_PREFIX = 'https://www.cheat-kusushi.jp/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/unconfirmed"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)


# Cheat Kusushi no Slow Life: Isekai ni Tsukurou Drugstore
class CheatKusushiDownload(UnconfirmedDownload):
    title = 'Cheat Kusushi no Slow Life: Isekai ni Tsukurou Drugstore'
    keywords = [title, 'Cheat Pharmacist\'s Slow Life: Making a Drugstore in Another World']

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


# Gotoubun no Hanayome ∬
class Gotoubun2Download(UnconfirmedDownload):
    title = "Gotoubun no Hanayome 2nd Season"
    keywords = [title, "The Quintessential Quintuplets", "Go-toubun", "5-toubun"]

    PAGE_PREFIX = 'https://www.tbs.co.jp/anime/5hanayome/'

    def __init__(self):
        super().__init__()
        self.init_base_folder('gotoubun2')

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated('https://www.tbs.co.jp/anime/5hanayome/story/')
        image_objs = []
        image_template = self.PAGE_PREFIX + 'story/img/intro_slide%s@2x.jpg'
        for i in range(6):
            image_url = image_template % str(i + 1).zfill(2)
            image_name = self.extract_image_name_from_url(image_url, with_extension=False)
            image_objs.append({'name': image_name, 'url': image_url})
        self.download_image_objects(image_objs, self.base_folder)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'teaser_visual', 'url': self.PAGE_PREFIX + 'img/teaser_visual.jpg'}
        ]
        self.download_image_objects(image_objs, folder)

    def download_character(self):
        folder = self.create_character_directory()
        image_objs = []
        image_template = self.PAGE_PREFIX + 'character/img/character_%s@2x.png'
        for i in range(6):
            image_url = image_template % str(i).zfill(2)
            image_name = self.extract_image_name_from_url(image_url, with_extension=False)
            image_objs.append({'name': image_name, 'url': image_url})
        self.download_image_objects(image_objs, folder)


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


# Ore dake Haireru Kakushi Dungeon
class KakushiDungeonDownload(UnconfirmedDownload):
    title = "Ore dake Haireru Kakushi Dungeon"
    keywords = [title, "The Hidden Dungeon Only I Can Enter"]

    PAGE_PREFIX = 'https://kakushidungeon-anime.jp/'

    def __init__(self):
        super().__init__()
        self.init_base_folder('kakushi-dungeon')

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [{'name': 'teaser', 'url': 'https://kakushidungeon-anime.jp/teaser/images/top-main-vis.jpg'},
                      {'name': 'teaser_2', 'url': 'https://pbs.twimg.com/media/EXZB_ZiU0AA4srN?format=jpg&name=large'}]
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


# Tatoeba Last Dungeon Mae no Mura no Shounen ga Joban no Machi de Kurasu Youna Monogatari
class LasdanDownload(UnconfirmedDownload):
    title = "Tatoeba Last Dungeon Mae no Mura no Shounen ga Joban no Machi de Kurasu Youna Monogatari"
    keywords = [title, "Lasdan"]

    PAGE_PREFIX = 'https://lasdan.com/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/lasdan"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_key_visual(self):
        filepath = self.create_key_visual_directory()
        image_objs = [
            {'name': 'kv1', 'url': 'https://pbs.twimg.com/media/ETrMsHWUMAIIE59?format=jpg&name=large'},
            {'name': 'kv2', 'url': 'https://pbs.twimg.com/media/ETsAx85UcAEJSAn?format=jpg&name=900x900'}]
        self.download_image_objects(image_objs, filepath)

    def download_character(self):
        chara_folder = self.create_character_directory()
        chara_main_url = 'https://lasdan.com/character/lloyd.html'
        image_objs = []
        try:
            soup = self.get_soup(chara_main_url)
            chara_list = soup.find('div', id='c_list_block_0001').find_all('a')
            cache_filepath = chara_folder + '/chara.log'
            chara_link_visited = []
            if os.path.exists(cache_filepath):
                with open(cache_filepath, 'r', encoding='utf-8') as f:
                    try:
                        line = f.readline()
                        while line:
                            chara_link_visited.append(line.strip())
                            line = f.readline()
                    except:
                        pass
            for chara_tag in chara_list:
                chara_temp_url = chara_tag['href'].replace('../', '')
                chara_url = self.PAGE_PREFIX + chara_temp_url
                chara_page_name = chara_temp_url.split('/')[-1]
                if chara_page_name in chara_link_visited:
                    continue
                chara_soup = self.get_soup(chara_url)
                body_image_url = self.PAGE_PREFIX + \
                    chara_soup.find('div', class_='charaBody').find('img')['src'].replace('../', '')
                body_image_name = self.extract_image_name_from_url(body_image_url, with_extension=False)
                image_objs.append({'name': body_image_name, 'url': body_image_url})
                face_image_url = self.PAGE_PREFIX + \
                    chara_soup.find('div', class_='charaFace').find('img')['src'].replace('../', '')
                face_image_name = self.extract_image_name_from_url(face_image_url, with_extension=False)
                image_objs.append({'name': face_image_name, 'url': face_image_url})
                with open(cache_filepath, 'a+', encoding='utf-8') as f:
                    f.write(chara_page_name + '\n')
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)
        self.download_image_objects(image_objs, chara_folder)
