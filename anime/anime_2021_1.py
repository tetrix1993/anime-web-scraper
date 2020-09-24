import os
import anime.constants as constants
from anime.main_download import MainDownload
from datetime import datetime
from scan import AniverseMagazineScanner, MocaNewsScanner, WebNewtypeScanner


# Gotoubun no Hanayome S2 https://www.tbs.co.jp/anime/5hanayome/ #五等分の花嫁 @5Hanayome_anime
# Horimiya https://horimiya-anime.com/ #ホリミヤ @horimiya_anime
# Jaku-Chara Tomozaki-kun http://tomozaki-koushiki.com/ #友崎くん @tomozakikoshiki
# Ore dake Haireru Kakushi Dungeon https://kakushidungeon-anime.jp/ #隠しダンジョン @kakushidungeon
# Tatoeba Last Dungeon https://lasdan.com/ #ラスダン @lasdan_PR
# Urasekai Picnic https://www.othersidepicnic.com/ #裏ピク @OthersidePicnic
# Yuru Camp S2 https://yurucamp.jp/second/ #ゆるキャン @yurucamp_anime


# Winter 2021 Anime
class Winter2021AnimeDownload(MainDownload):
    season = "2021-1"
    season_name = "Winter 2021"

    def __init__(self):
        super().__init__()
        self.init_base_folder('2021-1')


# Gotoubun no Hanayome ∬
class Gotoubun2Download(Winter2021AnimeDownload):
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


# Horimiya
class HorimiyaDownload(Winter2021AnimeDownload):
    title = "Horimiya"
    keywords = [title]

    PAGE_PREFIX = 'https://horimiya-anime.com/'

    def __init__(self):
        super().__init__()
        self.init_base_folder('horimiya')

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)
        #image_objs = []
        #self.download_image_objects(image_objs, self.base_folder)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'kv1_1', 'url': 'https://pbs.twimg.com/media/EiH_LNCU8AM5msx?format=png&name=900x900'},
            {'name': 'kv1_2', 'url': 'https://horimiya-anime.com/teaser/img/top/main/img_main.jpg'},
        ]
        self.download_image_objects(image_objs, folder)

    def download_character(self):
        folder = self.create_character_directory()
        image_objs = [
            {'name': 'img_hori', 'url': 'https://horimiya-anime.com/teaser/img/top/chara/img_hori.png'},
            {'name': 'img_miya', 'url': 'https://horimiya-anime.com/teaser/img/top/chara/img_miya.png'},
        ]
        self.download_image_objects(image_objs, folder)


# Jaku-Chara Tomozaki-kun
class TomozakiKunDownload(Winter2021AnimeDownload):
    title = "Jaku-Chara Tomozaki-kun"
    keywords = [title, 'The Low Tier Character "Tomozaki-kun"', 'Tomozaki-kun']

    PAGE_PREFIX = 'http://tomozaki-koushiki.com/'

    def __init__(self):
        super().__init__()
        self.init_base_folder('tomozakikun')

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        #self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)
        #image_objs = []
        #self.download_image_objects(image_objs, self.base_folder)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'announce', 'url': 'https://pbs.twimg.com/media/EToARdRU0AACyGk?format=jpg&name=large'},
            {'name': 'kv1', 'url': 'http://tomozaki-koushiki.com/news/wp-content/uploads/2020/09/キービジュアル.jpg'},
        ]
        self.download_image_objects(image_objs, folder)

    def download_character(self):
        folder = self.create_character_directory()
        image_objs = []
        self.download_image_objects(image_objs, folder)


# Ore dake Haireru Kakushi Dungeon
class KakushiDungeonDownload(Winter2021AnimeDownload):
    title = "Ore dake Haireru Kakushi Dungeon"
    keywords = [title, "The Hidden Dungeon Only I Can Enter"]

    PAGE_PREFIX = 'https://kakushidungeon-anime.jp/'

    def __init__(self):
        super().__init__()
        self.init_base_folder('kakushi-dungeon')

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [{'name': 'teaser', 'url': 'https://kakushidungeon-anime.jp/teaser/images/top-main-vis.jpg'},
                      {'name': 'teaser_2', 'url': 'https://pbs.twimg.com/media/EXZB_ZiU0AA4srN?format=jpg&name=large'},
                      {'name': 'kv1', 'url': 'https://kakushidungeon-anime.jp/assets/top/kv1/vis.jpg'},
                      {'name': 'kv1_2', 'url': 'https://pbs.twimg.com/media/EhKKkt2U0AMw5k8?format=jpg&name=4096x4096'}]
        self.download_image_objects(image_objs, folder)

    def download_character(self):
        folder = self.create_character_directory()
        image_objs = []
        try:
            soup = self.get_soup('https://kakushidungeon-anime.jp/character/index.html')
            chr_imgs = soup.find_all('div', class_='chr-img')
            for chr_img in chr_imgs:
                picture = chr_img.find('picture')
                if picture:
                    img_tag = picture.find('img')
                    if img_tag and img_tag.has_attr('src'):
                        img_url = img_tag['src'].replace('../', self.PAGE_PREFIX)
                        img_name = self.extract_image_name_from_url(img_url, with_extension=False)
                        image_objs.append({'name': img_name, 'url': img_url})
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)
        self.download_image_objects(image_objs, folder)


# Tatoeba Last Dungeon Mae no Mura no Shounen ga Joban no Machi de Kurasu Youna Monogatari
class LasdanDownload(Winter2021AnimeDownload):
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


# Urasekai Picnic
class UrasekaiPicnicDownload(Winter2021AnimeDownload):
    title = 'Urasekai Picnic'
    keywords = [title, 'Otherside Picnic']

    PAGE_PREFIX = 'https://www.othersidepicnic.com'

    def __init__(self):
        super().__init__()
        self.init_base_folder('urasekai-picnic')

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'main')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'kv1', 'url': 'https://www.othersidepicnic.com/cms/wp-content/themes/othersidepicnic/images/home/kv.jpg'},
        ]
        self.download_image_objects(image_objs, folder)

    def download_character(self):
        folder = self.create_character_directory()
        image_objs = []
        try:
            soup = self.get_soup('https://www.othersidepicnic.com/character/')
            chr_imgs = soup.find_all('div', class_='stand-chara')
            for chr_img in chr_imgs:
                img_tag = chr_img.find('img')
                if img_tag and img_tag.has_attr('src'):
                    img_url = self.PAGE_PREFIX + img_tag['src']
                    img_name = self.extract_image_name_from_url(img_url, with_extension=False)
                    image_objs.append({'name': img_name, 'url': img_url})
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)
        self.download_image_objects(image_objs, folder)


# Yuru Camp S2
class YuruCamp2Download(Winter2021AnimeDownload):
    title = "Yuru Camp 2nd Season"
    keywords = [title]

    PAGE_PREFIX = 'https://yurucamp.jp/second/'

    def __init__(self):
        super().__init__()
        self.init_base_folder('yurucamp2')

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        #self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)
        #image_objs = []
        #self.download_image_objects(image_objs, self.base_folder)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'teaser1', 'url': 'https://pbs.twimg.com/media/ETy4ZCFUYAEXlLl?format=jpg&name=4096x4096'},
            {'name': 'teaser2', 'url': 'https://pbs.twimg.com/media/ETy4ZC0U4AAbSS_?format=jpg&name=4096x4096'},
            {'name': 'mv_l', 'url': 'https://yurucamp.jp/second/images/mv_l.jpg'},
            {'name': 'mv_r', 'url': 'https://yurucamp.jp/second/images/mv_r.jpg'},
            {'name': 'g_visual_01', 'url': 'https://yurucamp.jp/second/images/g_visual_01.jpg'},
        ]
        self.download_image_objects(image_objs, folder)

    def download_character(self):
        folder = self.create_character_directory()
        image_objs = []
        self.download_image_objects(image_objs, folder)
