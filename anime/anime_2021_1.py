import os
# import anime.constants as constants
from anime.main_download import MainDownload
# from datetime import datetime
# from scan import AniverseMagazineScanner, MocaNewsScanner, WebNewtypeScanner


# Gotoubun no Hanayome S2 https://www.tbs.co.jp/anime/5hanayome/ #五等分の花嫁 @5Hanayome_anime
# Hataraku Saibou S2 https://hataraku-saibou.com/2nd.html #はたらく細胞 @hataraku_saibou
# Hataraku Saibou Black https://saibou-black.com/ #細胞BLACK @cellsatworkbla1
# Horimiya https://horimiya-anime.com/ #ホリミヤ @horimiya_anime
# Jaku-Chara Tomozaki-kun http://tomozaki-koushiki.com/ #友崎くん @tomozakikoshiki
# Kaifuku Jutsushi no Yarinaoshi http://kaiyari.com/ #回復術士 @kaiyari_anime
# Kemono Jihen https://kemonojihen-anime.com/ #怪物事変 #kemonojihen @Kemonojihen_tv
# Kumo Desu ga, Nani ka? https://kumo-anime.com/ #蜘蛛ですが @kumoko_anime
# Mushoku Tensei https://mushokutensei.jp/ #無職転生 @mushokutensei_A
# Non Non Biyori Nonstop https://nonnontv.com/ #なのん #のんのんびより @nonnontv
# Ore dake Haireru Kakushi Dungeon https://kakushidungeon-anime.jp/ #隠しダンジョン @kakushidungeon
# Tatoeba Last Dungeon https://lasdan.com/ #ラスダン @lasdan_PR
# Tensei shitara Slime Datta Ken S2 https://www.ten-sura.com/anime/tensura #転スラ #tensura @ten_sura_anime
# Urasekai Picnic https://www.othersidepicnic.com/ #裏ピク @OthersidePicnic
# World Trigger S2 http://www.toei-anim.co.jp/tv/wt/ #ワールドトリガー #トリガーオン @Anime_W_Trigger
# Yuru Camp S2 https://yurucamp.jp/second/ #ゆるキャン @yurucamp_anime


# Winter 2021 Anime
class Winter2021AnimeDownload(MainDownload):
    season = "2021-1"
    season_name = "Winter 2021"
    folder_name = '2021-1'

    def __init__(self):
        super().__init__()


# Gotoubun no Hanayome ∬
class Gotoubun2Download(Winter2021AnimeDownload):
    title = "Gotoubun no Hanayome 2nd Season"
    keywords = [title, "The Quintessential Quintuplets", "Go-toubun", "5-toubun"]
    folder_name = 'gotoubun2'

    PAGE_PREFIX = 'https://www.tbs.co.jp/anime/5hanayome/'

    def __init__(self):
        super().__init__()

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


# Hataraku Saibou S2
class HatarakuSaibou2Download(Winter2021AnimeDownload):
    title = "Hataraku Saibou!!"
    keywords = [title, "Cells at Work!", "2nd Season"]
    folder_name = "hataraku-saibou2"

    PAGE_PREFIX = 'https://hataraku-saibou.com/'
    MAIN_PAGE = 'https://hataraku-saibou.com/2nd.html'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.MAIN_PAGE, 'index')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv1', 'https://hataraku-saibou.com/assets/img/kv_pc.jpg')
        self.download_image_list(folder)


# Hataraku Saibou Black
class HatarakuSaibouBlackDownload(Winter2021AnimeDownload):
    title = "Hataraku Saibou Black"
    keywords = [title, "Cells at Work! Code Black"]
    folder_name = "hataraku-saibou-black"

    PAGE_PREFIX = 'https://saibou-black.com/'

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
        self.add_to_image_list('kv1', 'https://pbs.twimg.com/media/EngvcwDVoAAgALQ?format=jpg&name=large')
        self.add_to_image_list('kv2', 'https://saibou-black.com/assets/img/kv.jpg')
        self.download_image_list(folder)


# Horimiya
class HorimiyaDownload(Winter2021AnimeDownload):
    title = "Horimiya"
    keywords = [title]
    folder_name = 'horimiya'

    PAGE_PREFIX = 'https://horimiya-anime.com/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')
        #image_objs = []
        #self.download_image_objects(image_objs, self.base_folder)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'kv1_1', 'url': 'https://pbs.twimg.com/media/EiH_LNCU8AM5msx?format=png&name=900x900'},
            {'name': 'kv1_2', 'url': 'https://horimiya-anime.com/teaser/img/top/main/img_main.jpg'},
            {'name': 'kv2', 'url': 'https://horimiya-anime.com/assets/img/top/main/img_main.jpg'},
        ]
        self.download_image_objects(image_objs, folder)

    def download_character(self):
        folder = self.create_character_directory()
        image_objs = [
            {'name': 'img_hori', 'url': 'https://horimiya-anime.com/teaser/img/top/chara/img_hori.png'},
            {'name': 'img_miya', 'url': 'https://horimiya-anime.com/teaser/img/top/chara/img_miya.png'},
        ]
        self.download_image_objects(image_objs, folder)

        chara_url_template = 'https://horimiya-anime.com/assets/img/chara/img/img_chara%s-%s.jpg'
        try:
            i = 0
            stop = False
            while i <= 20:
                if stop:
                    break
                i += 1
                for j in range(10):
                    image_name = 'img_chara%s-%s' % (str(i).zfill(2), str(j + 1))
                    if self.is_image_exists(image_name, folder):
                        break
                    image_url = chara_url_template % (str(i).zfill(2), str(j + 1))
                    result = self.download_image(image_url, folder + '/' + image_name)
                    if result == -1:
                        if j == 0:
                            stop = True
                        break
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)


# Jaku-Chara Tomozaki-kun
class TomozakiKunDownload(Winter2021AnimeDownload):
    title = "Jaku-Chara Tomozaki-kun"
    keywords = [title, 'The Low Tier Character "Tomozaki-kun"', 'Tomozaki-kun']
    folder_name = 'tomozakikun'

    PAGE_PREFIX = 'http://tomozaki-koushiki.com/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')
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
    folder_name = 'kaiyari'

    PAGE_PREFIX = "http://kaiyari.com/"

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


# Kemono Jihen
class KemonoJihenDownload(Winter2021AnimeDownload):
    title = "Kemono Jihen"
    keywords = [title, 'Kemonojihen']
    folder_name = 'kemonojihen'

    PAGE_PREFIX = 'https://kemonojihen-anime.com/'

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
        self.add_to_image_list('kv1', 'https://kemonojihen-anime.com/img/home/visual_03.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        url_prefix = 'https://kemonojihen-anime.com/characters/'
        try:
            data = self.get_json('https://kemonojihen-anime.com/characters/chara_data.php')
            if 'charas' in data.keys():
                charas = data['charas']
                for chara in charas:
                    if 'images' in chara.keys():
                        images = chara['images']
                        for i in ['thumb', 'visual', 'face']:
                            if i in images.keys():
                                image_url = url_prefix + images[i].split('?')[0]
                                image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                                self.add_to_image_list(image_name, image_url)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)
        self.download_image_list(folder)


# Kumo Desu ga, Nani ka?
class KumoDesugaNanikaDownload(Winter2021AnimeDownload):
    title = "Kumo Desu ga, Nani ka?"
    keywords = [title, 'Kumoko', "So I'm a Spider, So What?"]
    folder_name = 'kumodesuga'

    PAGE_PREFIX = 'https://kumo-anime.com/'

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
        self.add_to_image_list('top-main', 'https://kumo-anime.com/teaser/images/top-main.jpg')
        self.add_to_image_list('top-main2', 'https://kumo-anime.com/teaser/images/top-main2.jpg')
        self.download_image_list(folder)


# Mushoku Tensei: Isekai Ittara Honki Dasu
class MushokuTenseiDownload(Winter2021AnimeDownload):
    title = "Mushoku Tensei: Isekai Ittara Honki Dasu"
    keywords = [title, 'Jobless Reincarnation']
    folder_name = 'mushoku-tensei'

    PAGE_PREFIX = 'https://mushokutensei.jp/'

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
        image_objs = [
            {'name': 'teaser', 'url': 'https://pbs.twimg.com/media/EHKOHakU4AUq-A3?format=jpg&name=large'},
            {'name': 'kv1', 'url': 'https://pbs.twimg.com/media/Ea3MiJFU0AETcOY?format=jpg&name=4096x4096'},
            {'name': 'kv2', 'url': 'https://mushokutensei.jp/wp-content/themes/mushoku_re/img/index/img_hero01.jpg'},
        ]
        self.download_image_objects(image_objs, folder)

    def download_character(self):
        folder = self.create_character_directory()
        image_objs = [
            {'name': 'char_rudeus', 'url': 'https://pbs.twimg.com/media/EnA_xagUYAYBiol?format=jpg&name=4096x4096'},
            {'name': 'char_roxy', 'url': 'https://pbs.twimg.com/media/EnE0mAHVQAINnGd?format=jpg&name=4096x4096'},
            {'name': 'char_sylphiette', 'url': 'https://pbs.twimg.com/media/EnE1DPqVoAAVOIN?format=jpg&name=4096x4096'},
            {'name': 'char_eris', 'url': 'https://pbs.twimg.com/media/EnE1TUQUcAINJCX?format=jpg&name=4096x4096'},
        ]
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
    folder_name = 'non-non-biyori3'

    PAGE_PREFIX = 'https://nonnontv.com'
    # PAGE_PREFIX = 'https://nonnontv2.wp-adm.kadokawa-isys.jp'
    STORY_PAGE = 'https://nonnontv.com/tvanime/story/season3/s00-3'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.STORY_PAGE, 'index')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        key_visual_url = self.PAGE_PREFIX + '/tvanime/wp-content/themes/nonnon_tvanime/assets/img/page/top/v%s/mainvisual.jpg'
        image_objs = []
        for i in range(1, 4, 1):
            image_objs.append({'name': 'kv' + str(i), 'url': key_visual_url % str(i)})
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
    folder_name = 'kakushi-dungeon'

    PAGE_PREFIX = 'https://kakushidungeon-anime.jp/'

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
                    img_tag = picture.find('source')
                    if img_tag and img_tag.has_attr('srcset'):
                        img_url = img_tag['srcset'].replace('../', self.PAGE_PREFIX)
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
    folder_name = 'lasdan'

    PAGE_PREFIX = 'https://lasdan.com/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

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


# Tensei shitara Slime Datta Ken S2
class Tensura2Download(Winter2021AnimeDownload):
    title = 'Tensei shitara Slime Datta Ken 2nd Season'
    keywords = [title, "Tensura", "That Time I Got Reincarnated as a Slime"]
    folder_name = 'tensura2'

    PAGE_PREFIX = 'https://www.ten-sura.com/anime/tensura'

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
        self.add_to_image_list('kv1', 'https://www.ten-sura.com/4GfGdAp7/wp-content/themes/tensura_portal/anime/tensura-portal-anime-tensura/assets/images/kv.jpg')
        self.add_to_image_list('kv2', 'https://www.ten-sura.com/4GfGdAp7/wp-content/themes/tensura_portal/anime/tensura-portal-anime-tensura/assets/images/kv_2.jpg')
        self.download_image_list(folder)


# Urasekai Picnic
class UrasekaiPicnicDownload(Winter2021AnimeDownload):
    title = 'Urasekai Picnic'
    keywords = [title, 'Otherside Picnic']
    folder_name = 'urasekai-picnic'

    PAGE_PREFIX = 'https://www.othersidepicnic.com'

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
        image_objs = [
            {'name': 'kv1', 'url': 'https://www.othersidepicnic.com/cms/wp-content/themes/othersidepicnic/images/home/kv.jpg'},
            {'name': 'kv2', 'url': 'https://www.othersidepicnic.com/cms/wp-content/themes/othersidepicnic/images/home/key-visual.jpg'}
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


# World Trigger S2
class WorldTrigger2Download(Winter2021AnimeDownload):
    title = "World Trigger 2nd Season"
    keywords = [title]
    folder_name = 'world-trigger2'

    PAGE_PREFIX = 'http://www.toei-anim.co.jp/tv/wt/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')


# Yuru Camp S2
class YuruCamp2Download(Winter2021AnimeDownload):
    title = "Yuru Camp 2nd Season"
    keywords = [title, 'Yurucamp']
    folder_name = 'yurucamp2'

    PAGE_PREFIX = 'https://yurucamp.jp/second/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        #self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')
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
