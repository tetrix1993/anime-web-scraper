import os
# import anime.constants as constants
from anime.main_download import MainDownload
# from datetime import datetime
# from scan import AniverseMagazineScanner, MocaNewsScanner, WebNewtypeScanner


# Gotoubun no Hanayome S2 https://www.tbs.co.jp/anime/5hanayome/ #五等分の花嫁 @5Hanayome_anime
# Horimiya https://horimiya-anime.com/ #ホリミヤ @horimiya_anime
# Jaku-Chara Tomozaki-kun http://tomozaki-koushiki.com/ #友崎くん @tomozakikoshiki
# Kaifuku Jutsushi no Yarinaoshi http://kaiyari.com/ #回復術士 @kaiyari_anime
# Mushoku Tensei https://mushokutensei.jp/ #無職転生 @mushokutensei_A
# Non Non Biyori Nonstop https://nonnontv.com/ #なのん #のんのんびより @nonnontv
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
            {'name': 'teaser_visual', 'url': self.PAGE_PREFIX + 'img/teaser_visual.jpg'},
            {'name': 'key_visual', 'url': self.PAGE_PREFIX + 'img/key_visual.jpg'},
            {'name': 'kv1', 'url': 'https://pbs.twimg.com/media/EjF1rDMWAAMXOVa?format=jpg&name=medium'},
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
        self.download_character()

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
        image_url_1 = self.PAGE_PREFIX + 'img/character/chara%s_img.png'
        image_url_2 = self.PAGE_PREFIX + 'img/character/chara%s_name.png'
        for i in range(20):
            url_1 = image_url_1 % str(i + 1)
            if not self.is_valid_url(url_1):
                break
            url_2 = image_url_2 % str(i + 1)
            name_1 = self.extract_image_name_from_url(url_1, with_extension=False)
            name_2 = self.extract_image_name_from_url(url_2, with_extension=False)
            self.add_to_image_list(name_1, url_1)
            self.add_to_image_list(name_2, url_2)
        self.download_image_list(folder)


# Kaifuku Jutsushi no Yarinaoshi
class KaiyariDownload(Winter2021AnimeDownload):
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
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            #{'name': 'announce', 'url': 'http://kaiyari.com/teaser/images/top-main-vis.jpg'},
            {'name': 'announce', 'url': 'https://pbs.twimg.com/media/Elkq5pRUYAAXjxO?format=jpg&name=4096x4096'},
            {'name': 'announce_2', 'url': 'https://pbs.twimg.com/media/EJ0V4iwVUAE-Ep7?format=jpg&name=medium'},
            #{'name': 'teaser', 'url': 'http://kaiyari.com/teaser/images/top-main-vis2.jpg'},
            {'name': 'teaser', 'url': 'https://pbs.twimg.com/media/Elkq6M2VoAQ_Yky?format=jpg&name=4096x4096'},
            {'name': 'teaser_2', 'url': 'https://pbs.twimg.com/media/EaizJUOU8AATcDK?format=jpg&name=medium'},
            {'name': 'kv1', 'url': 'http://kaiyari.com/assets/top/kv1/vis.jpg'},
            #{'name': 'kv1', 'url': 'https://pbs.twimg.com/media/Elko8BRUcAENWA1?format=jpg&name=4096x4096'}
        ]
        self.download_image_objects(image_objs, folder)

    def download_character(self):
        folder = self.create_character_directory()
        image_objs = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character.html')
            chr_imgs = soup.find_all('div', class_='chr-img')
            for chr_img in chr_imgs:
                image = chr_img.find('img')
                if image and image.has_attr('src'):
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                    image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                    image_objs.append({'name': image_name, 'url': image_url})
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)
        self.download_image_objects(image_objs, folder)


# Mushoku Tensei: Isekai Ittara Honki Dasu
class MushokuTenseiDownload(Winter2021AnimeDownload):
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


# Non Non Biyori Nonstop
class NonNonBiyori3Download(Winter2021AnimeDownload):
    title = 'Non Non Biyori Nonstop'
    keywords = [title]

    PAGE_PREFIX = 'https://nonnontv.com'
    # PAGE_PREFIX = 'https://nonnontv2.wp-adm.kadokawa-isys.jp'
    STORY_PAGE = 'https://nonnontv.com/tvanime/story/season3/s00-3'

    def __init__(self):
        super().__init__()
        self.init_base_folder('non-non-biyori3')

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.STORY_PAGE)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'kv1', 'url': 'https://pbs.twimg.com/media/EYq7r4EUcAAQgCa?format=jpg&name=large'},
            {'name': 'kv2', 'url': self.PAGE_PREFIX + '/tvanime/wp-content/uploads/2020/09/マルシー入り小キービジュアル2-RE_特効済.jpg'},
        ]
        self.download_image_objects(image_objs, folder)

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/' + 'cache'
        processed = []
        num_processed = 0
        if os.path.exists(cache_filepath):
            with open(cache_filepath, 'r') as f:
                inputs = f.read()
            processed = inputs.split(';')
            num_processed = len(processed)
        try:
            character_url = self.PAGE_PREFIX + '/tvanime/character/'
            soup = self.get_soup(character_url)
            nav_tag = soup.find('nav', class_='character__nav__list')
            if nav_tag:
                a_tags = nav_tag.find_all('a', class_='character__nav__item')
                if len(a_tags) > num_processed:
                    for a_tag in a_tags:
                        if a_tag.has_attr('href'):
                            split1 = a_tag['href'].split('=')
                            if len(split1) != 2:
                                continue
                            chara_name = split1[1]
                            if chara_name in processed:
                                continue
                            chara_url = character_url + a_tag['href'].replace('./', '')
                            chara_soup = self.get_soup(chara_url)
                            chara_ph = chara_soup.find('div', class_='character__ph')
                            if chara_ph:
                                images = chara_ph.find_all('img')
                                image_objs = []
                                for image in images:
                                    if image.has_attr('src'):
                                        image_url = self.PAGE_PREFIX + image['src']
                                        image_name = chara_name + '_'\
                                            + self.extract_image_name_from_url(image_url, with_extension=False)
                                        image_objs.append({'name': image_name, 'url': image_url})
                                self.download_image_objects(image_objs, folder)
                                processed.append(chara_name)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)

        if len(processed) > num_processed:
            with open(cache_filepath, 'w+') as f:
                for i in range(len(processed)):
                    if i > 0:
                        f.write(';')
                    f.write(processed[i])


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
    keywords = [title, 'Yurucamp']

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
