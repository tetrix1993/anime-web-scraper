import os
import anime.constants as constants
from anime.main_download import MainDownload

# Dokyuu Hentai HxEros https://hxeros.com/ #エグゼロス #hxeros @hxeros_anime [SUN]
# Kanojo, Okarishimasu https://kanokari-official.com/ #かのかり #kanokari @kanokari_anime
# Maou Gakuin no Futekigousha https://maohgakuin.com/ #魔王学院 @maohgakuin
# Monster Musume no Oishasan https://mon-isha-anime.com/character/ #モン医者 #m_doctor @mon_isha_anime
# Re:Zero S2 http://re-zero-anime.jp/tv/story/ #rezero #リゼロ @Rezero_official
# Peter Grill to Kenja no Jikan http://petergrill-anime.jp/ #賢者タイムアニメ #petergrill @petergrillanime
# Re:Zero S2 http://re-zero-anime.jp/tv/story/ #rezero #リゼロ @Rezero_official
# Uzaki-chan wa Asobitai! https://uzakichan.com/ #宇崎ちゃん @uzakichan_asobi
# Yahari Ore no Seishun http://www.tbs.co.jp/anime/oregairu/story/ #俺ガイル #oregairu @anime_oregairu


# Summer 2020 Anime
class Summer2020AnimeDownload(MainDownload):
    season = "2020-3"
    season_name = "Summer 2020"

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/2020-3"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)


# Dokyuu Hentai HxEros
class HxErosDownload(Summer2020AnimeDownload):
    title = "Dokyuu Hentai HxEros"
    keywords = [title]

    PAGE_PREFIX = 'https://hxeros.com'
    STORY_PAGE = 'https://hxeros.com/story/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/hxeros"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        #self.has_website_updated(self.STORY_PAGE)
        try:
            soup = self.get_soup(self.STORY_PAGE)
            episode_tags = soup.find('ul', class_='storynav').find_all('a')
            for episode_tag in episode_tags:
                try:
                    episode = str(int(episode_tag.text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                episode_url = self.PAGE_PREFIX + episode_tag['href']
                episode_soup = self.get_soup(episode_url)
                story_slider = episode_soup.find('div', class_='story__slider')
                if story_slider is not None:
                    images = story_slider.find_all('img')
                    image_objs = []
                    for i in range(len(images)):
                        image_name = episode + '_' + str(i + 1)
                        image_url = self.STORY_PAGE + images[i]['src']
                        image_objs.append({'name': image_name, 'url': image_url})
                    self.download_image_objects(image_objs, self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_key_visual(self):
        filepath = self.create_key_visual_directory()
        image_objs = [
            {'name': 'teaser', 'url': 'https://pbs.twimg.com/media/EIRucj0XkAUJTsE?format=jpg&name=medium'},
            {'name': 'kv', 'url': 'https://pbs.twimg.com/media/ESLTIUOVAAAWQ5L?format=jpg&name=4096x4096'},
            {'name': 'kv_web', 'url': 'https://hxeros.com/assets/img/top/ph_main.jpg'},
            {'name': 'kv2', 'url': 'https://pbs.twimg.com/media/EZo3lpqUEAEH3Xp?format=jpg&name=4096x4096'},
            {'name': 'kv2_web', 'url': 'https://hxeros.com/assets/img/top/ph_main_2.jpg'}]
        self.download_image_objects(image_objs, filepath)

    def download_character(self):
        try:
            character_folder = self.base_folder + '/' + constants.FOLDER_CHARACTER
            if not os.path.exists(character_folder):
                os.makedirs(character_folder)

            # Main Characters
            image_objs = [
                {'name': 'retto', 'url': 'https://hxeros.com/assets/img/character/single/retto/ph_character.png'},
                {'name': 'kirara', 'url': 'https://hxeros.com/assets/img/character/single/kirara/ph_character.png'},
                {'name': 'momoka', 'url': 'https://hxeros.com/assets/img/character/single/momoka/ph_character.png'},
                {'name': 'sora', 'url': 'https://hxeros.com/assets/img/character/single/sora/ph_character.png'},
                {'name': 'maihime', 'url': 'https://hxeros.com/assets/img/character/single/maihime/ph_character.png'}]
            for image_obj in image_objs:
                if os.path.exists(character_folder + '/' + image_obj['name'] + '.png'):
                    continue
                filepath_without_extension = character_folder + '/' + image_obj['name']
                self.download_image(image_obj['url'], filepath_without_extension)

            # Other Characters
            image_urls = []
            try:
                soup = self.get_soup('https://hxeros.com/character/other/')
                image_divs = soup.find_all('div', class_='other_sec__ph')
                for image_div in image_divs:
                    image_url = self.PAGE_PREFIX + image_div.find('img')['src']
                    image_urls.append(image_url)
            except:
                pass

            for image_url in image_urls:
                image_with_extension = self.extract_image_name_from_url(image_url, with_extension=True)
                if os.path.exists(character_folder + '/' + image_with_extension):
                    continue
                image_without_extension = self.extract_image_name_from_url(image_url, with_extension=False)
                filepath_without_extension = character_folder + '/' + image_without_extension
                self.download_image(image_url, filepath_without_extension)
        except Exception as e:
                print("Error in running " + self.__class__.__name__ + ' - Character')
                print(e)


# Kanojo, Okarishimasu
class KanokariDownload(Summer2020AnimeDownload):
    title = "Kanojo, Okarishimasu"
    keywords = [title, "Kanokari", "Rent-a-Girlfriend"]

    STORY_PAGE = 'https://kanokari-official.com/story/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/kanokari"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()
        self.download_bluray()

    def download_episode_preview(self):
        self.has_website_updated(self.STORY_PAGE)

    def download_key_visual(self):
        keyvisual_folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'chara_new_kv1', 'url': 'https://kanokari-official.com/wp/wp-content/themes/kanokari_main/_assets/images/slider/kv_chizuru.jpg'},
            {'name': 'chara_new_kv2', 'url': 'https://kanokari-official.com/wp/wp-content/themes/kanokari_main/_assets/images/slider/kv_mami.jpg'},
            {'name': 'chara_new_kv3', 'url': 'https://kanokari-official.com/wp/wp-content/themes/kanokari_main/_assets/images/slider/kv_ruka.jpg'},
            {'name': 'chara_new_kv4', 'url': 'https://kanokari-official.com/wp/wp-content/themes/kanokari_main/_assets/images/slider/kv_sumi.jpg'},
            {'name': 'chara_kv1', 'url': 'https://kanokari-official.com/wp/wp-content/uploads/2020/03/mv01.jpg'},
            {'name': 'chara_kv2', 'url': 'https://kanokari-official.com/wp/wp-content/uploads/2020/03/mv02.jpg'},
            {'name': 'chara_kv3', 'url': 'https://kanokari-official.com/wp/wp-content/uploads/2020/03/ruka_KV.jpg'},
            {'name': 'chara_kv4', 'url': 'https://kanokari-official.com/wp/wp-content/uploads/2020/03/sumi_KV0322.jpg'},
            {'name': 'kv_web', 'url': 'https://kanokari-official.com/wp/wp-content/themes/kanokari_main/_assets/images/slider/kv_main.jpg'},
            {'name': 'kv', 'url': 'https://pbs.twimg.com/media/EYwr-OVU8AANFm4?format=jpg&name=large'}]
        self.download_image_objects(image_objs, keyvisual_folder)

    def download_character(self):
        character_folder = self.create_character_directory()
        image_objs = [
            {'name': 'chara_body01', 'url': 'https://kanokari-official.com/wp/wp-content/themes/kanokari_teaser/assets/img/top/chara/chara_body01.png'},
            {'name': 'chara_body02', 'url': 'https://kanokari-official.com/wp/wp-content/themes/kanokari_teaser/assets/img/top/chara/chara_body02.png'},
            {'name': 'chara_body03', 'url': 'https://kanokari-official.com/wp/wp-content/themes/kanokari_teaser/assets/img/top/chara/chara_body03.png'},
            {'name': 'chara_body04', 'url': 'https://kanokari-official.com/wp/wp-content/themes/kanokari_teaser/assets/img/top/chara/chara_body04.png'},
            {'name': 'chara_body05', 'url': 'https://kanokari-official.com/wp/wp-content/themes/kanokari_teaser/assets/img/top/chara/chara_body05.png'},
            {'name': 'chara_yt01', 'url': 'https://kanokari-official.com/wp/wp-content/uploads/2020/03/かのかり_千鶴PV-06.jpg'},
            {'name': 'chara_yt02', 'url': 'https://kanokari-official.com/wp/wp-content/uploads/2020/03/かのかり_麻美PV-01.jpg'},
            {'name': 'chara_yt03', 'url': 'https://kanokari-official.com/wp/wp-content/uploads/2020/03/かのかり_瑠夏PV-06.jpg'},
            {'name': 'chara_yt04', 'url': 'https://kanokari-official.com/wp/wp-content/uploads/2020/03/かのかり_墨PV-06.jpg'}]
        try:
            soup = self.get_soup("https://kanokari-official.com/character/")
            chara_details = soup.find_all('div', class_='visual-chara')
            for chara_detail in chara_details:
                image = chara_detail.find('img')
                image_url = image['src']
                image_with_extension = self.extract_image_name_from_url(image_url, with_extension=True)
                if os.path.exists(character_folder + '/' + image_with_extension):
                    continue
                image_without_extension = self.extract_image_name_from_url(image_url, with_extension=False)
                image_objs.append({'name': image_without_extension, 'url': image_url})
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)
        self.download_image_objects(image_objs, character_folder)

    def download_bluray(self):
        bluray_folder = self.create_bluray_directory()
        url_template = 'https://kanokari-official.com/bluray/vol%s/'
        try:
            for i in range(1, 5, 1):
                image_objs = []
                bluray_url = url_template % str(i)
                soup = self.get_soup(bluray_url)
                bluray_div = soup.find('div', class_='bluray-main')
                if bluray_div is None:
                    continue
                images = bluray_div.find_all('img')
                if images is None or len(images) == 0:
                    continue
                for image in images:
                    image_url = image['src']
                    image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                    image_objs.append({'name': image_name, 'url': image_url})
                self.download_image_objects(image_objs, bluray_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Blu-Ray')
            print(e)

        image_objs = []
        bd_bonus_page_url = 'https://kanokari-official.com/bluray/store/'
        self.has_website_updated(url=bd_bonus_page_url, cache_name='bd_bonus')
        try:
            soup = self.get_soup(bd_bonus_page_url)
            bonus_blocks = soup.find_all('li')
            if bonus_blocks is not None and len(bonus_blocks) > 0:
                for bonus_block in bonus_blocks:
                    images = bonus_block.find_all('div', class_='slider__img')
                    if images is not None and len(images) > 0:
                        for image in images:
                            try:
                                image_url = image['style'].split('url(')[1].split(');')[0]
                                image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                                image_objs.append({'name': image_name, 'url': image_url})
                            except:
                                pass
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Blu-Ray Bonus')
            print(e)
        self.download_image_objects(image_objs, bluray_folder)


# Maou Gakuin no Futekigousha: Shijou Saikyou no Maou no Shiso, Tensei shite Shison-tachi no Gakkou e
class MaohgakuinDownload(Summer2020AnimeDownload):
    title = "Maou Gakuin no Futekigousha: Shijou Saikyou no Maou no Shiso, Tensei shite Shison-tachi no Gakkou e"
    keywords = [title, 'Maohgakuin']

    PAGE_PREFIX = "https://maohgakuin.com/"
    CHARACTER_PREFIX = 'https://maohgakuin.com/character/'
    STORY_PAGE = 'https://maohgakuin.com/story/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/maohgakuin"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()
        self.download_bluray()

    def download_episode_preview(self):
        #self.has_website_updated(self.STORY_PAGE)
        try:
            soup = self.get_soup(self.STORY_PAGE)
            episodes = soup.find('nav', class_='page_nav').find_all('a')
            for episode_tag in episodes:
                episode_num = ''
                try:
                    episode_num = str(int(episode_tag.text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode_num + '_1'):
                    continue
                episode_url = self.STORY_PAGE + episode_tag['href'].replace('./', '')
                episode_soup = self.get_soup(episode_url)
                image_container = episode_soup.find('div', class_='main_image')
                if image_container is not None:
                    images = image_container.find_all('img')
                    if images is not None and len(images) > 0:
                        image_objs = []
                        for i in range(len(images)):
                            image_url = self.STORY_PAGE + images[i]['src']
                            image_name = episode_num + '_' + str(i + 1)
                            image_objs.append({'name': image_name, 'url': image_url})
                        self.download_image_objects(image_objs, self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


    def download_key_visual(self):
        keyvisual_folder = self.create_key_visual_directory()
        image_objs = [
            #{'name': 'kv', 'url': 'https://maohgakuin.com/assets/img/top/kv.jpg'}
            {'name': 'kv', 'url': 'https://pbs.twimg.com/media/EZbC3ljUMAEAkei?format=jpg&name=4096x4096'},
            {'name': 'kv2', 'url': 'https://pbs.twimg.com/media/EZaMb5WUEAAxxIg?format=jpg&name=4096x4096'}]
        self.download_image_objects(image_objs, keyvisual_folder)

    def download_character(self):
        character_folder = self.create_character_directory()
        try:
            soup = self.get_soup("https://maohgakuin.com/character/")
            chara_details = soup.find('div', class_='chara_list').find_all('li')
            for chara_detail in chara_details:
                thumb_image_url = self.PAGE_PREFIX + chara_detail.find('img')['src'].replace('../', '')
                image_with_extension = self.extract_image_name_from_url(thumb_image_url, with_extension=True)
                if os.path.exists(character_folder + '/' + image_with_extension):
                    continue
                image_urls = [thumb_image_url]
                chara_url = self.CHARACTER_PREFIX + chara_detail.find('a')['href'].replace('./', '')
                chara_soup = self.get_soup(chara_url)
                chara_detail = chara_soup.find('div', class_='chara_detail')
                image_urls.append(self.PAGE_PREFIX + chara_detail.find('p', class_='stand_image')
                                  .find('img')['src'].replace('../', ''))
                image_urls.append(self.PAGE_PREFIX + chara_detail.find('div', class_='face_image')
                                  .find('img')['src'].replace('../', ''))

                for image_url in image_urls:
                    image_with_extension = self.extract_image_name_from_url(image_url, with_extension=True)
                    if os.path.exists(character_folder + '/' + image_with_extension):
                        continue
                    image_without_extension = self.extract_image_name_from_url(image_url, with_extension=False)
                    filepath_without_extension = character_folder + '/' + image_without_extension
                    self.download_image(image_url, filepath_without_extension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)

    def download_bluray(self):
        folder = self.create_bluray_directory()
        image_objs = [
            {'name': 'music_ed', 'url': 'https://pbs.twimg.com/media/Eb6ctYuU8AEVilj?format=jpg&name=large'}
        ]
        self.download_image_objects(image_objs, folder)


# Monster Musume no Oishasan
class MonIshaDownload(Summer2020AnimeDownload):
    title = "Monster Musume no Oishasan"
    keywords = [title, "Monisha", "Mon-Isha"]

    PAGE_PREFIX = 'https://mon-isha-anime.com/'
    STORY_PAGE = 'https://mon-isha-anime.com/story/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/mon-isha"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_episode_preview()
        self.download_intro()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.STORY_PAGE)

    def download_intro(self):
        intro_folder = self.create_custom_directory(constants.FOLDER_INTRO)
        image_objs = []
        intro_image_url_template = 'https://mon-isha-anime.com/images/story/st_ph_a%s.jpg'
        for i in range(26):
            image_url = intro_image_url_template % str(i + 1).zfill(2)
            image_name = self.extract_image_name_from_url(image_url, with_extension=False)
            image_objs.append({'name': image_name, 'url': image_url})
        self.download_image_objects(image_objs, intro_folder)

    def download_key_visual(self):
        keyvisual_folder = self.base_folder + '/' + constants.FOLDER_KEY_VISUAL
        if not os.path.exists(keyvisual_folder):
            os.makedirs(keyvisual_folder)

        image_objs = [
            {'name': 'teaser', 'url': 'https://pbs.twimg.com/media/EJTToJMU0AEgpMK?format=jpg&name=medium'},
            {'name': 'kv', 'url': 'https://pbs.twimg.com/media/ETrymlxU0AA0Oep?format=jpg&name=medium'}]
        for image_obj in image_objs:
            if os.path.exists(keyvisual_folder + '/' + image_obj['name'] + '.png') or \
                    os.path.exists(keyvisual_folder + '/' + image_obj['name'] + '.jpg'):
                continue
            filepath_without_extension = keyvisual_folder + '/' + image_obj['name']
            self.download_image(image_obj['url'], filepath_without_extension)

    def download_character(self):
        character_folder = self.create_character_directory()
        try:
            soup = self.get_soup("https://mon-isha-anime.com/character/")
            chara_details = soup.find_all('div', class_='swinmob')
            for chara_detail in chara_details:
                images = chara_detail.find_all('img')
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                    image_with_extension = self.extract_image_name_from_url(image_url, with_extension=True)
                    if os.path.exists(character_folder + '/' + image_with_extension):
                        continue
                    image_without_extension = self.extract_image_name_from_url(image_url, with_extension=False)
                    filepath_without_extension = character_folder + '/' + image_without_extension
                    self.download_image(image_url, filepath_without_extension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)


# Peter Grill to Kenja no Jikan
class PeterGrillDownload(Summer2020AnimeDownload):
    title = "Peter Grill to Kenja no Jikan"
    keywords = [title, "Peter Grill and the Philosopher's Time"]

    PAGE_PREFIX = 'http://petergrill-anime.jp/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/petergrill"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()
        self.download_bluray()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_key_visual(self):
        keyvisual_folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'kv', 'url': 'http://petergrill-anime.jp/images/key_v_202003.png'}]
        self.download_image_objects(image_objs, keyvisual_folder)

    def download_character(self):
        character_folder = self.create_character_directory()
        try:
            soup = self.get_soup("http://petergrill-anime.jp/character.php")
            chara_details = soup.find_all('li', class_='character_item')
            for chara_detail in chara_details:
                images = chara_detail.find_all('img')
                for image in images:
                    if 'upload' not in image['src']:
                        continue
                    image_url = self.PAGE_PREFIX + image['src']
                    image_with_extension = self.extract_image_name_from_url(image_url, with_extension=True)
                    if os.path.exists(character_folder + '/' + image_with_extension):
                        continue
                    image_without_extension = self.extract_image_name_from_url(image_url, with_extension=False)
                    filepath_without_extension = character_folder + '/' + image_without_extension
                    self.download_image(image_url, filepath_without_extension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)

    def download_bluray(self):
        folder = self.create_bluray_directory()
        image_objs = [
            {'name': 'bd_1_1', 'url': 'https://aniverse-mag.com/wp-content/uploads/2020/07/200702_01.jpg'},
            {'name': 'bd_1_2', 'url': 'https://aniverse-mag.com/wp-content/uploads/2020/07/200702_02.jpg'}
        ]
        self.download_image_objects(image_objs, folder)


# Re:Zero kara Hajimeru Isekai Seikatsu 2nd Season
class ReZero2Download(Summer2020AnimeDownload):
    title = "Re:Zero kara Hajimeru Isekai Seikatsu 2nd Season"
    keywords = [title, "rezero", "Re:Zero - Starting Life in Another World"]

    STORY_PAGE = "http://re-zero-anime.jp/tv/story/"

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/rezero2"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.STORY_PAGE)

    def download_key_visual(self):
        keyvisual_folder = self.create_key_visual_directory()
        image_objs = [
            #{'name': 'kv_old', 'url': 'http://re-zero-anime.jp/tv/assets/top/main-tv1r.jpg'},
            {'name': 'kv', 'url': 'http://re-zero-anime.jp/tv/assets/top/main-tv2.jpg'},
            {'name': 'kv2', 'url': 'http://re-zero-anime.jp/tv/assets/top/main-tv2b.jpg'}]
        self.download_image_objects(image_objs, keyvisual_folder)


# Uzaki-chan wa Asobitai!
class UzakiChanDownload(Summer2020AnimeDownload):
    title = "Uzaki-chan wa Asobitai!"
    keywords = [title, "Uzakichan"]

    PAGE_PREFIX = 'https://uzakichan.com/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/uzakichan"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_bluray()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_key_visual(self):
        keyvisual_folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'kv', 'url': 'https://pbs.twimg.com/media/EP1u35XUEAAvg4f?format=jpg&name=large'},
            {'name': 'kv2', 'url': 'https://pbs.twimg.com/media/EXi1RaHUYAAVJPM?format=jpg&name=medium'}]
        self.download_image_objects(image_objs, keyvisual_folder)

    def download_bluray(self):
        bd_url = 'https://uzakichan.com/package.html'
        self.has_website_updated(bd_url, 'bd')
        folder = self.create_bluray_directory()
        image_objs = []
        try:
            soup = self.get_soup(bd_url)
            specialboxes = soup.find_all('div', class_='specialbox')
            for specialbox in specialboxes:
                images = specialbox.find_all('img')
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src']
                    image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                    image_objs.append({'name': image_name, 'url': image_url})
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Blu-Ray')
            print(e)
        self.download_image_objects(image_objs, folder)


# Yahari Ore no Seishun Love Comedy wa Machigatteiru. Kan
class Oregairu3Download(Summer2020AnimeDownload):
    title = "Yahari Ore no Seishun Love Comedy wa Machigatteiru. Kan"
    keywords = [title, "Oregairu", "My Teen Romantic Comedy SNAFU 3",
                "My youth romantic comedy is wrong as I expected 3"]

    PAGE_PREFIX = "http://www.tbs.co.jp/anime/oregairu/"
    STORY_PAGE = "http://www.tbs.co.jp/anime/oregairu/story/"
    IMAGE_TEMPLATE = 'http://www.tbs.co.jp/anime/oregairu/story/img/story%s/%s.jpg'
    TOTAL_EPISODES = 25
    TOTAL_IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/oregairu3"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        try:
            self.has_website_updated(self.STORY_PAGE)
            try:
                soup = self.get_soup(self.STORY_PAGE, decode=True)
                story_nav = soup.find('ul', class_='story-nav')
                chapters = story_nav.find_all('li')
                for chapter in chapters:
                    try:
                        link_tag = chapter.find('a')
                        link_text = link_tag.text
                        if '第' in link_text and '話' in link_text:
                            episode = link_text.split('話')[0].split('第')[1].zfill(2)
                            if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                                    self.base_folder + "/" + episode + "_1.png"):
                                continue
                            episode_link = self.STORY_PAGE + link_tag['href']
                            episode_soup = self.get_soup(episode_link)
                            image_tags = episode_soup.find('ul', class_='slides').find_all('img')
                            j = 0
                            for image_tag in image_tags:
                                j += 1
                                image_url = self.STORY_PAGE + image_tag['src']
                                file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j)
                                self.download_image(image_url, file_path_without_extension)
                    except:
                        continue
            except:
                pass

            for i in range(self.TOTAL_EPISODES):
                episode = str(i + 1).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg") or self.is_file_exists(
                        self.base_folder + "/" + episode + "_1.png"):
                    continue
                for j in range(self.TOTAL_IMAGES_PER_EPISODE):
                    image_url = self.IMAGE_TEMPLATE % (episode, str(j + 1).zfill(2))
                    file_path_without_extension = self.base_folder + '/' + episode + '_' + str(j + 1)
                    result = self.download_image(image_url, file_path_without_extension)
                    if result == -1:
                        return
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_key_visual(self):
        keyvisual_folder = self.create_key_visual_directory()
        image_objs = [{'name': 'kv', 'url': 'http://www.tbs.co.jp/anime/oregairu/img/keyvisual_pc_2.jpg'},
            {'name': 'kv2', 'url': 'http://www.tbs.co.jp/anime/oregairu/special/img/special02_01.png'}]
        self.download_image_objects(image_objs, keyvisual_folder)
