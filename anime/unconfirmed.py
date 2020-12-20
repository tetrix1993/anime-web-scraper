import os
import anime.constants as constants
from anime.main_download import MainDownload

# Bokutachi no Remake http://bokurema.com/ #ぼくリメ #bokurema @bokurema
# Cheat Kusushi no Slow Life: Isekai ni Tsukurou Drugstore https://www.cheat-kusushi.jp/ #チート薬師 #スローライフ @cheat_kusushi
# Kobayashi-san Chi no Maid Dragon S https://maidragon.jp/2nd/ #maidragon @maidragon_anime
# Osananajimi ga Zettai ni Makenai Love Comedy https://osamake.com/ #おさまけ
# Princess Connect! Re:Dive S2 https://anime.priconne-redive.jp/ #アニメプリコネ #プリコネR #プリコネ @priconne_anime
# Seirei Gensouki https://seireigensouki.com/ #精霊幻想記 @seireigensouki
# Shadows House https://shadowshouse-anime.com/ #シャドーハウス @shadowshouse_yj
# Shuumatsu no Harem https://end-harem-anime.com/ #終末のハーレム @harem_official_
# Tate no Yuusha S2 http://shieldhero-anime.jp/ #shieldhero #盾の勇者の成り上がり @shieldheroanime
# Vlad Love https://www.vladlove.com/index.html #ぶらどらぶ #vladlove @VLADLOVE_ANIME


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
        self.has_website_updated(self.PAGE_PREFIX, 'index', diff=2)

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


# Seirei Gensouki
class SeireiGensoukiDownload(UnconfirmedDownload):
    title = "Seirei Gensouki"
    keywords = [title, "Spirit Chronicles"]
    folder_name = 'seirei-gensouki'

    PAGE_PREFIX = "https://seireigensouki.com/"

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
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/EnytdwVVQAESUct?format=jpg&name=large')
        #self.add_to_image_list('teaser', 'https://seireigensouki.com/wp/wp-content/uploads/2020/11/SG_teaser_logoc.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            chara_pics = soup.find_all('div', class_='chara-pic')
            for chara_pic in chara_pics:
                image = chara_pic.find('img')
                if image and image.has_attr('src'):
                    image_url = image['src']
                    image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)


# Shadows House
class ShadowsHouseDownload(UnconfirmedDownload):
    title = "Shadows House"
    keywords = [title]
    folder_name = 'shadows-house'

    PAGE_PREFIX = 'https://shadowshouse-anime.com/'

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
        self.add_to_image_list('teaser', 'https://shadowshouse-anime.com/assets/img/img_kv_pc.jpg')
        self.download_image_list(folder)


# Shuumatsu no Harem
class ShuumatsuNoHaremDownload(UnconfirmedDownload):
    title = 'Shuumatsu no Harem'
    keywords = [title, "World's End Harem"]
    folder_name = 'shuumatsu-no-harem'

    PAGE_PREFIX = 'https://end-harem-anime.com/'

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
        self.add_to_image_list('announce', 'https://pbs.twimg.com/media/EXzkif6VAAAxqJI?format=png&name=900x900')
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'core_sys/images/news/00000002/block/00000005/00000001.jpg')
        #self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/EoYL6tMVgAADou1?format=jpg&name=large')
        self.add_to_image_list('teaser_char', self.PAGE_PREFIX + 'core_sys/images/main/top/kv_char.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed = []
        num_processed = 0
        if os.path.exists(cache_filepath):
            with open(cache_filepath, 'r', encoding='utf-8') as f:
                inputs = f.read()
            processed = inputs.split(';')
            num_processed = len(processed)

        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/reito.html')
            chara_list = soup.find('div', id='ContentsListUnit01')
            if chara_list:
                a_tags = chara_list.find_all('a')
                for a_tag in a_tags:
                    if a_tag.has_attr('href') and '/' in a_tag['href']:
                        chara_name = a_tag['href'].split('/')[-1].split('.html')[0]
                        if chara_name in processed:
                            continue
                        if chara_name == 'reito':  # First character
                            chara_soup = soup
                        else:
                            chara_soup = self.get_soup(self.PAGE_PREFIX + a_tag['href'].replace('../', ''))
                        self.image_list = []
                        divs = ['standWrap', 'faceWrap']
                        for div in divs:
                            wraps = chara_soup.find_all('div', class_=div)
                            for wrap in wraps:
                                if wrap:
                                    image = wrap.find('img')
                                    if image and image.has_attr('src'):
                                        image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                                        self.add_to_image_list(image_name, image_url)
                        self.download_image_list(folder)
                        processed.append(chara_name)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)

        if len(processed) > num_processed:
            with open(cache_filepath, 'w+', encoding='utf-8') as f:
                for i in range(len(processed)):
                    if i > 0:
                        f.write(';')
                    f.write(processed[i])


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


# Vlad Love
class VladLoveDownload(UnconfirmedDownload):
    title = 'Vlad Love'
    keywords = [title, "Vladlove"]
    folder_name = 'vladlove'

    PAGE_PREFIX = 'https://www.vladlove.com/'

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
        self.add_to_image_list('visual01', 'https://www.vladlove.com/images/bg_cast.jpg')
        self.add_to_image_list('visual02', 'https://www.vladlove.com/images/bg_intro.jpg')
        self.add_to_image_list('visual03', 'https://www.vladlove.com/images/bg_character.jpg')
        self.add_to_image_list('visual04', 'https://www.vladlove.com/images/img_visual06.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character.html')
            detail_list = soup.find('ul', class_='characterDetailList')
            if detail_list:
                self.image_list = []
                images = detail_list.find_all('img')
                for image in images:
                    if image and image.has_attr('src'):
                        image_url = self.PAGE_PREFIX + image['src']
                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                        self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)
