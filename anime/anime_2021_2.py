import os
import anime.constants as constants
from anime.main_download import MainDownload
from datetime import datetime
from scan import AniverseMagazineScanner, MocaNewsScanner, WebNewtypeScanner


# 86 https://anime-86.com/ #エイティシックス @anime_eightysix
# Dragon, Ie wo Kau #ドラ家 @anime_doraie
# Hige wo Soru. Soshite Joshikousei wo Hirou. http://higehiro-anime.com/ #higehiro #ひげひろ @higehiro_anime
# Ijiranaide, Nagatoro-san https://www.nagatorosan.jp/ #長瀞さん @nagatoro_tv
# Isekai Maou to Shoukan Shoujo no Dorei Majutsu Ω https://isekaimaou-anime.com/ #異世界魔王 @isekaimaou
# Kyuukyoku Shinka Shita Full Dive RPG ga Genjitsu Yori mo Kusogee Dattara https://fulldive-rpg.com/ #フルダイブ @fulldive_anime
# Osananajimi ga Zettai ni Makenai Love Comedy https://osamake.com/ #おさまけ #osamake
# Sayonara Watashi no Cramer https://sayonara-cramer.com/tv/ #さよなら私のクラマー @cramer_pr
# Seijo no Maryoku wa Bannou desu https://seijyonomaryoku.jp/ #seijyonoanime @seijyonoanime
# Sentouin, Hakenshimasu! https://kisaragi-co.jp/ #sentoin @sentoin_anime
# Shadows House https://shadowshouse-anime.com/ #シャドーハウス @shadowshouse_yj
# Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita https://slime300-anime.com/ #スライム倒して300年 @slime300_PR
# Super Cub https://supercub-anime.com/ #スーパーカブ @supercub_anime
# Vivy: Fluroite Eye's Song https://vivy-portal.com/ #ヴィヴィ @vivy_portal
# Yakunara Mug Cup mo https://yakumo-project.com/ #やくもtv @yakumo_project


# Spring 2021 Anime
class Spring2021AnimeDownload(MainDownload):
    season = "2021-2"
    season_name = "Spring 2021"
    folder_name = '2021-2'

    def __init__(self):
        super().__init__()


# 86
class EightySixDownload(Spring2021AnimeDownload):
    title = '86'
    keywords = [title, 'Eighty Six']
    folder_name = '86'

    PAGE_PREFIX = 'https://anime-86.com/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index', diff=2)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        #self.add_to_image_list('kv', self.PAGE_PREFIX + 'assets/img/top/img_kv.jpg')
        self.add_to_image_list('kv1', 'https://pbs.twimg.com/media/EvxfN8wU8AI_Dps?format=jpg&name=4096x4096')
        self.add_to_image_list('kv2', 'https://pbs.twimg.com/media/EvxfN86U8AAoYZx?format=jpg&name=4096x4096')

        valentine_prefix = self.PAGE_PREFIX + 'special/valentine/assets/img/86_valentine_'
        self.add_to_image_list('86_valentine_icon_01', valentine_prefix + 'icon_01.jpg')
        self.add_to_image_list('86_valentine_icon_ex', valentine_prefix + 'icon_ex.jpg')
        self.add_to_image_list('86_valentine_wp_01', valentine_prefix + 'wp_01.jpg')
        self.add_to_image_list('86_valentine_wp_ex', valentine_prefix + 'wp_ex.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        #try:
        #    soup = self.get_soup(self.PAGE_PREFIX + 'character/')
        #    contents = soup.find_all('div', class_='m-chara__content')
        #    for content in contents:
        #        figures = content.find_all('figure')
        #        for figure in figures:
        #            if figure.has_attr('style') and 'url(' in figure['style']:
        #                image_url = self.PAGE_PREFIX + figure['style'].split('url(')[1].split(');')[0].replace('../', '')
        #                image_name = self.extract_image_name_from_url(image_url, with_extension=False)
        #                self.add_to_image_list(image_name, image_url)
        #except Exception as e:
        #    print("Error in running " + self.__class__.__name__ + " - Character")
        #    print(e)
        template = self.PAGE_PREFIX + 'assets/img/character/%s.png'
        for i in range(30):
            num = str(i + 1).zfill(2)
            filenames = []
            exist = False
            for j in ['chara_%s', 'chara_face_%s']:
                filename = j % num
                filenames.append(filename)
                if self.is_image_exists(filename, folder):
                    exist = True
                    break
            if exist:
                continue
            image_downloaded = 0
            for name in filenames:
                image_url = template % name
                result = self.download_image(image_url, folder + '/' + name)
                if result == -1:
                    continue
                image_downloaded += 1
            if image_downloaded == 0:
                break
        self.download_image_list(folder)

    def download_media(self):
        # API Link:
        # https://edge.api.brightcove.com/playback/v1/accounts/4929511769001/videos/6230722910001
        # https://edge.api.brightcove.com/playback/v1/accounts/4929511769001/videos/6230722072001
        # Headers: Accept: application/json;pk=BCpkADawqM1XGilraBDORB63T7mXX_DO0PvAeb0nPGOcNdREe4o42wzOOr9_chEsztXD6gxOSBCVpmrsc3Iczz0I3xEMohICjq69krvIZ8s1P0F1uVZiKjttPKy5vXHsTNB20y3uGjMBFeGj
        folder = self.create_custom_directory('media')
        valentine_01_url = 'http://brightcove04.brightcove.com/34/4929511769001/202102/551/4929511769001_6230722968001_6230722910001.mp4?pubId=4929511769001&videoId=6230722910001'
        valentine_ex_url = 'http://brightcove04.brightcove.com/34/4929511769001/202102/1719/4929511769001_6230723857001_6230722072001.mp4?pubId=4929511769001&videoId=6230722072001'
        self.download_content(valentine_01_url, folder + '/valentine_01.mp4')
        self.download_content(valentine_ex_url, folder + '/valentine_ex.mp4')


class DoraieDownload(Spring2021AnimeDownload):
    title = 'Dragon, Ie wo Kau'
    keywords = [title, 'Dragon Goes House-Hunting']
    folder_name = 'doraie'

    PAGE_PREFIX = 'https://doraie.com/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index', diff=2)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv2', self.PAGE_PREFIX + 'news/wp/wp-content/uploads/2020/11/7e7632e1c37c768e225d8f78d1a5a6f3.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        try:
            json_obj = self.get_json(self.PAGE_PREFIX + 'character/chara_data.php')
            if isinstance(json_obj, dict):
                if 'charas' in json_obj and isinstance(json_obj['charas'], list):
                    for chara in json_obj['charas']:
                        if 'images' in chara and 'visual' in chara['images']:
                            image_url = self.PAGE_PREFIX + 'character/' + chara['images']['visual'].split('?')[0]
                            image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                            self.add_to_image_list(image_name, image_url)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)
        self.download_image_list(folder)


# Hige wo Soru. Soshite Joshikousei wo Hirou.
class HigehiroDownload(Spring2021AnimeDownload):
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
        self.has_website_updated(self.PAGE_PREFIX, 'index', diff=2)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/EjO4FTcU0AIPm2X?format=jpg&name=medium')

        theme_url = self.PAGE_PREFIX + 'wp-content/themes/higehiro/images/'
        self.add_to_image_list('kv_sayu', theme_url + 'kv_sayu.png')
        self.add_to_image_list('kv_yoshida', theme_url + 'kv_yoshida.png')
        self.add_to_image_list('hige_keyvisual', theme_url + 'hige_keyvisual.jpg')

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


# Ijiranaide, Nagatoro-san
class NagatorosanDownload(Spring2021AnimeDownload):
    title = 'Ijiranaide, Nagatoro-san'
    keywords = [title, 'Nagatorosan']
    folder_name = 'nagatoro-san'

    PAGE_PREFIX = 'https://www.nagatorosan.jp/'

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
            {'name': 'teaser', 'url': 'https://pbs.twimg.com/media/Eb6NC6rU0AAoaUm?format=jpg&name=medium'},
            {'name': 'mainimg', 'url': 'https://www.nagatorosan.jp/images/mainimg.jpg'},
            {'name': 'kv1', 'url': 'https://pbs.twimg.com/media/EmIPL3dU0AABjQI?format=jpg&name=medium'},
            {'name': 'kv1_2', 'url': 'https://www.nagatorosan.jp/img/top/mainimg.jpg'},
        ]
        self.download_image_objects(image_objs, folder)

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        self.add_to_image_list('img_nagatoro', 'https://www.nagatorosan.jp/images/img_nagatoro.png')
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            sliders =soup.find_all('div', class_='swiper-slide')
            for slider in sliders:
                images = slider.find_all('img')
                for image in images:
                    if image.has_attr('src'):
                        image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                        self.add_to_image_list(image_name, image_url)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)
        self.download_image_list(folder)


# Isekai Maou to Shoukan Shoujo no Dorei Majutsu Ω
class IsekaiMaou2Download(Spring2021AnimeDownload):
    title = 'Isekai Maou to Shoukan Shoujo no Dorei Majutsu 2nd Season'
    keywords = [title, "How Not to Summon a Demon Lord", "Isekaimaou"]
    folder_name = 'isekai-maou2'

    PAGE_PREFIX = 'https://isekaimaou-anime.com/'

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
        upload_url = self.PAGE_PREFIX + 'wp/wp-content/uploads/2021/'
        self.image_list = []
        self.add_to_image_list('teaser', 'https://64.media.tumblr.com/5b236a6eb6f70ee69097815a8b9bc9ce/eb7b1b50731487c4-05/s1280x1920/04c8ff15baf833620d39f90e910d23aff8fa0019.png')
        self.add_to_image_list('chara_visual_shera', upload_url + '01/異世界魔王Ω_添い寝ビジュアルシェラ_mini.jpg')
        self.add_to_image_list('chara_visual_rem', upload_url + '01/異世界魔王Ω_添い寝ビジュアルレム_mini.jpg')
        self.add_to_image_list('chara_visual_lumachina', upload_url + '02/異世界魔王Ω_添い寝ビジュアルルマキーナ_mini.jpg')
        self.add_to_image_list('chara_visual_rose', upload_url + '02/異世界魔王Ω_添い寝ビジュアルロゼ_mini.jpg')
        self.add_to_image_list('kv1', 'https://pbs.twimg.com/media/EuwlST0VcAAY_hC?format=jpg&name=medium')
        #self.add_to_image_list('kv1', upload_url + '02/異世界魔王Ω_本ビジュアル_mini_c.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            visuals = soup.find_all('div', class_='visual--main')
            for visual in visuals:
                images = visual.find_all('img')
                for image in images:
                    if image.has_attr('src'):
                        image_url = image['src']
                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                        self.add_to_image_list(image_name, image_url)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)
        self.download_image_list(folder)


# Kyuukyoku Shinka Shita Full Dive RPG ga Genjitsu Yori mo Kusogee Dattara
class FullDiveRPGDownload(Spring2021AnimeDownload):
    title = "Kyuukyoku Shinka Shita Full Dive RPG ga Genjitsu Yori mo Kusogee Dattara"
    keywords = [title, "Fulldive", "Kiwame Quest"]
    folder_name = 'fulldive'

    PAGE_PREFIX = 'https://fulldive-rpg.com/'

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
        self.add_to_image_list('visual01', 'https://pbs.twimg.com/media/EoYbnevVoAAnE3-?format=jpg&name=large')
        self.add_to_image_list('visual01_1', self.PAGE_PREFIX + 'img/main_visual.png')
        self.add_to_image_list('visual01_2', self.PAGE_PREFIX + 'img/special/contents_gallery_01.jpg')
        self.add_to_image_list('visual02', 'https://pbs.twimg.com/media/EvtFCncUYAMRtb1?format=jpg&name=large')
        self.add_to_image_list('visual02_1', self.PAGE_PREFIX + 'img/special/contents_gallery_02.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'img/chara/%s.png'
        self.image_list = []
        for i in range(30):
            num = str(i + 1).zfill(2)
            filenames = []
            exist = False
            for j in ['body_%s_real', 'body_%s_vr', 'face_%s']:
                filename = j % num
                filenames.append(filename)
                if self.is_image_exists(filename, folder):
                    exist = True
                    break
            if exist:
                continue
            image_downloaded = 0
            for name in filenames:
                image_url = template % name
                result = self.download_image(image_url, folder + '/' + name)
                if result == -1:
                    continue
                image_downloaded += 1
            if image_downloaded == 0:
                break
        self.download_image_list(folder)


# Osananajimi ga Zettai ni Makenai Love Comedy
class OsamakeDownload(Spring2021AnimeDownload):
    title = 'Osananajimi ga Zettai ni Makenai Love Comedy'
    keywords = [title, 'Osamake']
    folder_name = 'osamake'

    PAGE_PREFIX = 'https://osamake.com/'

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
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'assets/top/main-t1b/vis.jpg')
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'assets/top/main-h1/vis.jpg')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/Ev2vZFhUUAACs3Y?format=jpg&name=large')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        for i in range(20):
            image_url = (self.PAGE_PREFIX + 'assets/character/c/%s.png') % str(i + 1)
            image_name = 'chara_' + str(i + 1).zfill(2)
            result = self.download_image(image_url, folder + '/' + image_name)
            if result == -1:
                break


# Sayonara Watashi no Cramer
class SayonaraCramerDownload(Spring2021AnimeDownload):
    title = 'Sayonara Watashi no Cramer'
    keywords = [title, 'Good-bye, Cramer!']
    folder_name = 'sayonara-cramer'

    PAGE_PREFIX = 'https://sayonara-cramer.com/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX + 'tv/', 'index')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv1', self.PAGE_PREFIX + '_assets/images/tv/kv/kv.jpg')
        self.add_to_image_list('kv2', self.PAGE_PREFIX + 'wp/wp-content/themes/sayonaracramer-project/_assets/images/tv/kv/kv_tv_202101_004@2x.jpg')
        self.add_to_image_list('movie_kv1', self.PAGE_PREFIX + '_assets/images/project/kv/kv_movie.jpg')
        self.add_to_image_list('movie_kv2', 'https://ogre.natalie.mu/media/news/comic/2020/1205/sayonarawatashinocramar_KV2.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'tv/character/')
            divs = soup.find_all('div', class_='charmain--img')
            for div in divs:
                image = div.find('img')
                if image and image.has_attr('src'):
                    image_url = image['src']
                    image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                    self.add_to_image_list(image_name, image_url)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)
        self.download_image_list(folder)


# Seijo no Maryoku wa Bannou desu
class SeijonoMaryokuDownload(Spring2021AnimeDownload):
    title = 'Seijo no Maryoku wa Bannou desu'
    keywords = [title, 'seijonomaryoku', 'seijyonomaryoku', "The Saint's Magic Power is Omnipotent"]
    folder_name = 'seijyonomaryoku'

    PAGE_PREFIX = 'https://seijyonomaryoku.jp/'

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
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'images/main-visual.jpg')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/EqDkgusU0AAdO1C?format=jpg&name=large')
        self.add_to_image_list('valentine', self.PAGE_PREFIX + 'images/valentine_big.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX)

            images = soup.find_all('img', class_='m-character-list-heading-img')
            for image in images:
                if image and image.has_attr('src'):
                    image_url = self.PAGE_PREFIX + image['src']
                    image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                    self.add_to_image_list(image_name, image_url)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)
        self.download_image_list(folder)


# Sentouin, Hakenshimasu!
class SentoinDownload(Spring2021AnimeDownload):
    title = "Sentouin, Hakenshimasu!"
    keywords = [title, "Sentoin", "Combatants Will Be Dispatched!"]
    folder_name = 'sentoin'

    PAGE_PREFIX = 'https://kisaragi-co.jp/'

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
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/Eqbrtf7VEAADuiD?format=jpg&name=4096x4096')
        self.add_to_image_list('teaser_1', 'https://kisaragi-co.jp/assets/top/main-t1/vis.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = 'https://kisaragi-co.jp/assets/top/character/%s.png'
        for i in range(20):
            stop = 0
            for j in ['c', 'f']:
                image_name = '%s%s' % (j, str(i + 1))
                if self.is_image_exists(image_name, folder):
                    continue
                result = self.download_image(template % image_name, folder + '/' + image_name)
                if result == -1:
                    stop += 1
            if stop == 2:
                break


# Shadows House
class ShadowsHouseDownload(Spring2021AnimeDownload):
    title = "Shadows House"
    keywords = [title]
    folder_name = 'shadows-house'

    PAGE_PREFIX = 'https://shadowshouse-anime.com/'

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
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'assets/img/img_kv_pc.jpg')
        self.add_to_image_list('kv', self.PAGE_PREFIX + 'assets/img/top/main/img_kv.jpg')
        #self.add_to_image_list('chara_visual_louise', 'https://pbs.twimg.com/media/EsPEImfUYAEkuL1?format=jpg&name=large')
        self.download_image_list(folder)
        for i in range(10):
            image_name = 'img_kv_%s' % str(i + 1).zfill(2)
            if self.is_image_exists(image_name, folder):
                continue
            image_url = self.PAGE_PREFIX + 'assets/img/%s.jpg' % image_name
            if self.is_valid_url(image_url, is_image=True):
                self.download_image(image_url, folder + '/' + image_name)
            else:
                break

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/img/character/visual/%s.png'
        for i in range(20):
            num = str(i + 1).zfill(2)
            filenames = []
            exist = False
            for j in ['chara_%s_s', 'chara_%s_d']:
                filename = j % num
                filenames.append(filename)
                if self.is_image_exists(filename, folder):
                    exist = True
                    break
            if exist:
                continue
            image_downloaded = 0
            for name in filenames:
                image_url = template % name
                result = self.download_image(image_url, folder + '/' + name)
                if result == -1:
                    continue
                image_downloaded += 1
            if image_downloaded == 0:
                break

        # Other Characters
        other_template = self.PAGE_PREFIX + 'assets/img/character/sub/%s.png'
        for i in range(20):
            num = str(i + 1).zfill(2)
            image_name = 'img_chara-other_%s' % num
            if self.is_image_exists(image_name, folder):
                continue
            image_url = other_template % image_name
            result = self.download_image(image_url, folder + '/' + image_name)
            if result == -1:
                break


# Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita
class Slime300Download(Spring2021AnimeDownload):
    title = "Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita"
    keywords = [title, "I've Been Killing Slimes for 300 Years and Maxed Out My Level", "Slime 300"]
    folder_name = 'slime300'

    PAGE_PREFIX = 'https://slime300-anime.com'

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
        #self.image_list = []
        #self.add_to_image_list('keyvisual01', self.PAGE_PREFIX + '/static/8e3ba0a8b42628959e71b7f52c737a6a/eeb1b/keyvisual01.png')
        #self.add_to_image_list('keyvisual02', self.PAGE_PREFIX + '/static/a2a5d8a583acad23e9276580866d3aac/eeb1b/keyvisual02.png')
        #self.add_to_image_list('keyvisual03', self.PAGE_PREFIX + '/static/a03236e46bc620b60292da71514f9253/40ffe/keyvisual03.png')
        #self.add_to_image_list('keyvisual04', self.PAGE_PREFIX + '/static/98f5d8537a23ebf5b357bac8d63fcf39/eeb1b/keyvisual04.png')
        #self.download_image_list(folder)

        kv_json = self.PAGE_PREFIX + '/page-data/sq/d/621460424.json'
        self.image_list = []
        try:
            json_obj = self.get_json(kv_json)
            data_obj = json_obj['data']
            for data in data_obj.keys():
                try:
                    image_url = self.PAGE_PREFIX + data_obj[data]['childImageSharp']['fluid']['src']
                    image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                    self.add_to_image_list(image_name, image_url)
                except:
                    pass
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Key Visual")
            print(e)
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        image_objs = []
        chara_json = self.PAGE_PREFIX + '/page-data/sq/d/2919095229.json'
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


class SuperCubDownload(Spring2021AnimeDownload):
    title = 'Super Cub'
    keywords = [title, 'Supercub']
    folder_name = 'supercub'

    PAGE_PREFIX = 'https://supercub-anime.com/'

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
        self.add_to_image_list('kv', self.PAGE_PREFIX + 'core_sys/images/main/home/kv.jpg')
        self.add_to_image_list('kv_tw', 'https://pbs.twimg.com/media/ErvAcsEUcAMljAq?format=jpg&name=4096x4096')
        self.download_image_list(folder)


# Vivy: Fluorite Eye's Song
class VivyDownload(Spring2021AnimeDownload):
    title = "Vivy: Fluorite Eye's Song"
    keywords = [title, "Vivy -Fluorite Eye's Song"]
    folder_name = 'vivy'

    PAGE_PREFIX = 'https://vivy-portal.com/'

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
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'assets/img/kv_pc.jpg')
        self.add_to_image_list('teaser_tw', 'https://pbs.twimg.com/media/Erv_rEcUcAMlQ3e?format=jpg&name=medium')
        self.download_image_list(folder)


# Yakunara Mug Cup mo
class YakunaraMugCupMo(Spring2021AnimeDownload):
    title = "Yakunara Mug Cup mo"
    keywords = [title, 'Yakumo', "Let's Make a Mug Too"]
    folder_name = 'yakumo'

    PAGE_PREFIX = 'https://yakumo-project.com/'

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
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'news/images/200729_01.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        for i in range(20):
            image_url = 'https://yakumo-project.com/images/character_%sfull.png' % str(i + 1)
            image_name = self.extract_image_name_from_url(image_url, with_extension=False)
            if self.is_image_exists(image_name, folder):
                continue
            result = self.download_image(image_url, folder + '/' + image_name)
            if result == -1:
                break
