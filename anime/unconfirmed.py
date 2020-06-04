import os
import anime.constants as constants
from anime.main_download import MainDownload


# Bokutachi no Remake http://bokurema.com/ #ぼくリメ #bokurema @bokurema
# Cheat Kusushi no Slow Life: Isekai ni Tsukurou Drugstore https://www.cheat-kusushi.jp/ #チート薬師 #スローライフ @cheat_kusushi
# Dokyuu Hentai HxEros https://hxeros.com/ #エグゼロス @hxeros_anime
# Iwa Kakeru!: Sport Climbing Girls http://iwakakeru-anime.com/ #いわかける #iwakakeru @iwakakeru_anime
# Kanojo, Okarishimasu https://kanokari-official.com/ #かのかり #kanokari @kanokari_anime
# Kuma Kuma Kuma Bear https://kumakumakumabear.com/ #くまクマ熊ベアー #kumabear @kumabear_anime
# Kimi to Boku no Saigo no Senjou, Aruiwa Sekai ga Hajimaru Seisen #キミ戦 #kimisen @kimisen_project
# Majo no Tabitabi https://majotabi.jp/ #魔女の旅々 #魔女の旅々はいいぞ #majotabi @majotabi_PR
# Maou Gakuin no Futekigousha https://maohgakuin.com/ #魔王学院 @maohgakuin
# Monster Musume no Oishasan https://mon-isha-anime.com/character/ #モン医者 #m_doctor @mon_isha_anime
# Ochikobore Fruit Tart http://ochifuru-anime.com/ #ochifuru @ochifuru_anime
# Peter Grill to Kenja no Jikan http://petergrill-anime.jp/ #賢者タイムアニメ #petergrill @petergrillanime
# Re:Zero S2 http://re-zero-anime.jp/tv/story/ #rezero #リゼロ @Rezero_official
# Tonikaku Kawaii http://tonikawa.com/ #トニカクカワイイ #tonikawa @tonikawa_anime
# Uzaki-chan wa Asobitai! https://uzakichan.com/ #宇崎ちゃん @uzakichan_asobi
# Yahari Ore no Seishun http://www.tbs.co.jp/anime/oregairu/story/ #俺ガイル #oregairu @anime_oregairu


# Unconfirmed Season Anime
class UnconfirmedDownload(MainDownload):
    season = "9999-9"
    season_name = "Unconfirmed"

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/unconfirmed"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)


class CheatKusushiDownload(UnconfirmedDownload):
    title = 'Cheat Kusushi no Slow Life: Isekai ni Tsukurou Drugstore'
    keywords = [title, 'Cheat Pharmacist\'s Slow Life: Making a Drugstore in Another World']

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/cheat-kusushi"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_key_visual()

    def download_key_visual(self):
        keyvisual_folder = self.base_folder + '/' + constants.FOLDER_KEY_VISUAL
        if not os.path.exists(keyvisual_folder):
            os.makedirs(keyvisual_folder)

        image_objs = [
            {'name': 'teaser', 'url': 'https://www.cheat-kusushi.jp/img/top-main.png'}]
        for image_obj in image_objs:
            if os.path.exists(keyvisual_folder + '/' + image_obj['name'] + '.png'):
                continue
            filepath_without_extension = keyvisual_folder + '/' + image_obj['name']
            self.download_image(image_obj['url'], filepath_without_extension)


# Dokyuu Hentai HxEros
class HxErosDownload(UnconfirmedDownload):
    title = "Dokyuu Hentai HxEros"
    keywords = ["Dokyuu Hentai HxEros"]

    PAGE_PREFIX = 'https://hxeros.com'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/hxeros"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_key_visual()
        self.download_character()

    def download_key_visual(self):
        keyvisual_folder = self.base_folder + '/' + constants.FOLDER_KEY_VISUAL
        if not os.path.exists(keyvisual_folder):
            os.makedirs(keyvisual_folder)

        image_objs = [
            {'name': 'teaser', 'url': 'https://pbs.twimg.com/media/EIRucj0XkAUJTsE?format=jpg&name=medium'},
            {'name': 'kv', 'url': 'https://pbs.twimg.com/media/ESLTIUOVAAAWQ5L?format=jpg&name=4096x4096'},
            {'name': 'kv_web', 'url': 'https://hxeros.com/assets/img/top/ph_main.jpg'},
            {'name': 'kv2', 'url': 'https://pbs.twimg.com/media/EZo3lpqUEAEH3Xp?format=jpg&name=4096x4096'},
            {'name': 'kv2_web', 'url': 'https://hxeros.com/assets/img/top/ph_main_2.jpg'}]
        for image_obj in image_objs:
            if os.path.exists(keyvisual_folder + '/' + image_obj['name'] + '.jpg') or \
                    os.path.exists(keyvisual_folder + '/' + image_obj['name'] + '.png'):
                continue
            filepath_without_extension = keyvisual_folder + '/' + image_obj['name']
            self.download_image(image_obj['url'], filepath_without_extension)

    def download_character(self):
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


# Iwa Kakeru!: Sport Climbing Girls
class IwakakeruDownload(UnconfirmedDownload):
    title = "Iwa Kakeru!: Sport Climbing Girls"
    keywords = ["Iwa Kakeru!: Sport Climbing Girls", "Iwakakeru"]

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/iwakakeru"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_key_visual()

    def download_key_visual(self):
        keyvisual_folder = self.base_folder + '/' + constants.FOLDER_KEY_VISUAL
        if not os.path.exists(keyvisual_folder):
            os.makedirs(keyvisual_folder)

        image_urls = ["http://iwakakeru-anime.com/img/index/mainvisual.png"]
        for image_url in image_urls:
            image_with_extension = self.extract_image_name_from_url(image_url, with_extension=True)
            if os.path.exists(keyvisual_folder + '/' + image_with_extension):
                continue
            image_without_extension = self.extract_image_name_from_url(image_url, with_extension=False)
            filepath_without_extension = keyvisual_folder + '/' + image_without_extension
            self.download_image(image_url, filepath_without_extension)


# Kanojo, Okarishimasu
class KanokariDownload(UnconfirmedDownload):
    title = "Kanojo, Okarishimasu"
    keywords = ["Kanojo, Okarishimasu", "Kanokari", "Rent-a-Girlfriend"]

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/kanokari"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_key_visual()
        self.download_character()

    def download_key_visual(self):
        keyvisual_folder = self.base_folder + '/' + constants.FOLDER_KEY_VISUAL
        if not os.path.exists(keyvisual_folder):
            os.makedirs(keyvisual_folder)

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
        for image_obj in image_objs:
            if os.path.exists(keyvisual_folder + '/' + image_obj['name'] + '.jpg') or \
                    os.path.exists(keyvisual_folder + '/' + image_obj['name'] + '.png'):
                continue
            filepath_without_extension = keyvisual_folder + '/' + image_obj['name']
            self.download_image(image_obj['url'], filepath_without_extension)

    def download_character(self):
        character_folder = self.base_folder + '/' + constants.FOLDER_CHARACTER
        if not os.path.exists(character_folder):
            os.makedirs(character_folder)

        try:
            soup = self.get_soup("https://kanokari-official.com/")
            chara_details = soup.find('section', class_='chara_area').find_all('div', class_='chara_detail')
            for chara_detail in chara_details:
                images = chara_detail.find_all('img')
                for image in images:
                    image_url = image['src']
                    image_with_extension = self.extract_image_name_from_url(image_url, with_extension=True)
                    if os.path.exists(character_folder + '/' + image_with_extension):
                        continue
                    image_without_extension = self.extract_image_name_from_url(image_url, with_extension=False)
                    filepath_without_extension = character_folder + '/' + image_without_extension
                    self.download_image(image_url, filepath_without_extension)
        except Exception as e:
            pass


# Kimi to Boku no Saigo no Senjou, Aruiwa Sekai ga Hajimaru Seisen
class KimisenDownload(UnconfirmedDownload):
    title = "Kimi to Boku no Saigo no Senjou, Aruiwa Sekai ga Hajimaru Seisen"
    keywords = ["Kimi to Boku no Saigo no Senjou, Aruiwa Sekai ga Hajimaru Seisen", "Kimisen"]

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/kimisen"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_key_visual()

    def download_key_visual(self):
        keyvisual_folder = self.base_folder + '/' + constants.FOLDER_KEY_VISUAL
        if not os.path.exists(keyvisual_folder):
            os.makedirs(keyvisual_folder)

        image_objs = [
            {'name': 'teaser', 'url': 'https://kimisentv.com/teaser/images/top-main-vis.jpg'}]
        for image_obj in image_objs:
            if os.path.exists(keyvisual_folder + '/' + image_obj['name'] + '.png') or \
                    os.path.exists(keyvisual_folder + '/' + image_obj['name'] + '.jpg'):
                continue
            filepath_without_extension = keyvisual_folder + '/' + image_obj['name']
            self.download_image(image_obj['url'], filepath_without_extension)


# Kuma Kuma Kuma Bear
class KumaBearDownload(UnconfirmedDownload):
    title = "Kuma Kuma Kuma Bear"
    keywords = ["Kuma Kuma Kuma Bear"]

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/kumabear"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_key_visual()

    def download_key_visual(self):
        keyvisual_folder = self.base_folder + '/' + constants.FOLDER_KEY_VISUAL
        if not os.path.exists(keyvisual_folder):
            os.makedirs(keyvisual_folder)

        image_urls = ["https://kumakumakumabear.com/core_sys/images/main/tz/main_img.jpg",
                      "https://kumakumakumabear.com/core_sys/images/main/tz/main_img_2.jpg",
                      "https://kumakumakumabear.com/core_sys/images/main/tz/main_img_3.jpg"]
        for image_url in image_urls:
            image_with_extension = self.extract_image_name_from_url(image_url, with_extension=True)
            if os.path.exists(keyvisual_folder + '/' + image_with_extension):
                continue
            image_without_extension = self.extract_image_name_from_url(image_url, with_extension=False)
            filepath_without_extension = keyvisual_folder + '/' + image_without_extension
            self.download_image(image_url, filepath_without_extension)


class MajotabiDownload(UnconfirmedDownload):
    title = "Majo no Tabitabi"
    keywords = [title, "Wandering Witch: The Journey of Elaina", "Majotabi"]

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/majotabi"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_key_visual()

    def download_key_visual(self):
        keyvisual_folder = self.base_folder + '/' + constants.FOLDER_KEY_VISUAL
        if not os.path.exists(keyvisual_folder):
            os.makedirs(keyvisual_folder)

        image_objs = [
            {'name': 'kv1', 'url': 'https://pbs.twimg.com/media/EHPjPtFU8AAHo9S?format=jpg&name=large'},
            {'name': 'kv2', 'url': 'https://pbs.twimg.com/media/ESahsP9UEAAhzgn?format=jpg&name=large'},
            {'name': 'kv3', 'url': 'https://pbs.twimg.com/media/EUqV9B7UcAAOCeE?format=jpg&name=medium'},
            {'name': 'kv4', 'url': 'https://pbs.twimg.com/media/EW64PYgUMAAGDIk?format=jpg&name=4096x4096'}]
        for image_obj in image_objs:
            if os.path.exists(keyvisual_folder + '/' + image_obj['name'] + '.png'):
                continue
            filepath_without_extension = keyvisual_folder + '/' + image_obj['name']
            self.download_image(image_obj['url'], filepath_without_extension)


# Maou Gakuin no Futekigousha: Shijou Saikyou no Maou no Shiso, Tensei shite Shison-tachi no Gakkou e
class MaohgakuinDownload(UnconfirmedDownload):
    title = "Maou Gakuin no Futekigousha: Shijou Saikyou no Maou no Shiso, Tensei shite Shison-tachi no Gakkou e"
    keywords = [title, 'Maohgakuin']

    PAGE_PREFIX = "https://maohgakuin.com/"
    CHARACTER_PREFIX = 'https://maohgakuin.com/character/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/maohgakuin"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_key_visual()
        self.download_character()

    def download_key_visual(self):
        keyvisual_folder = self.base_folder + '/' + constants.FOLDER_KEY_VISUAL
        if not os.path.exists(keyvisual_folder):
            os.makedirs(keyvisual_folder)

        image_objs = [
            #{'name': 'kv', 'url': 'https://maohgakuin.com/assets/img/top/kv.jpg'}
            {'name': 'kv', 'url': 'https://pbs.twimg.com/media/EZbC3ljUMAEAkei?format=jpg&name=4096x4096'},
            {'name': 'kv2', 'url': 'https://pbs.twimg.com/media/EZaMb5WUEAAxxIg?format=jpg&name=4096x4096'}]
        for image_obj in image_objs:
            if os.path.exists(keyvisual_folder + '/' + image_obj['name'] + '.png'):
                continue
            filepath_without_extension = keyvisual_folder + '/' + image_obj['name']
            self.download_image(image_obj['url'], filepath_without_extension)

    def download_character(self):
        character_folder = self.base_folder + '/' + constants.FOLDER_CHARACTER
        if not os.path.exists(character_folder):
            os.makedirs(character_folder)

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
            pass


# Monster Musume no Oishasan
class MonIshaDownload(UnconfirmedDownload):
    title = "Monster Musume no Oishasan"
    keywords = ["Monster Musume no Oishasan", "Monisha", "Mon-Isha"]

    PAGE_PREFIX = 'https://mon-isha-anime.com/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/mon-isha"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_key_visual()
        self.download_character()

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
        character_folder = self.base_folder + '/' + constants.FOLDER_CHARACTER
        if not os.path.exists(character_folder):
            os.makedirs(character_folder)

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
            pass


# Ochikobore Fruit Tart
class OchifuruDownload(UnconfirmedDownload):
    title = "Ochikobore Fruit Tart"
    keywords = ["Ochikobore Fruit Tart", "Dropout Idol", "Ochifuru"]

    CHARA_IMAGE_TEMPLATE = 'http://ochifuru-anime.com/images/chara/%s/p_002.png'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/ochifuru"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_key_visual()
        self.download_character()

    def download_key_visual(self):
        keyvisual_folder = self.base_folder + '/' + constants.FOLDER_KEY_VISUAL
        if not os.path.exists(keyvisual_folder):
            os.makedirs(keyvisual_folder)

        image_objs = [
            {'name': 'kv', 'url': 'https://pbs.twimg.com/media/EKb4OniUwAELo-b?format=jpg&name=medium'}]
        for image_obj in image_objs:
            if os.path.exists(keyvisual_folder + '/' + image_obj['name'] + '.png') or \
                    os.path.exists(keyvisual_folder + '/' + image_obj['name'] + '.jpg'):
                continue
            filepath_without_extension = keyvisual_folder + '/' + image_obj['name']
            self.download_image(image_obj['url'], filepath_without_extension)

    def download_character(self):
        character_folder = self.base_folder + '/' + constants.FOLDER_CHARACTER
        if not os.path.exists(character_folder):
            os.makedirs(character_folder)

        try:
            i = 1
            while True:
                filepath_without_extension = character_folder + '/chara_' + str(i).zfill(2)
                if os.path.exists(filepath_without_extension + '.png') or \
                        os.path.exists(filepath_without_extension + '.jpg'):
                    continue
                image_url = self.CHARA_IMAGE_TEMPLATE % str(i).zfill(3)
                result = self.download_image(image_url, filepath_without_extension)
                if result == -1:
                    break
                i += 1
        except Exception as e:
            pass


# Peter Grill to Kenja no Jikan
class PeterGrillDownload(UnconfirmedDownload):
    title = "Peter Grill to Kenja no Jikan"
    keywords = ["Peter Grill to Kenja no Jikan", "Peter Grill and the Philosopher's Time"]

    PAGE_PREFIX = 'http://petergrill-anime.jp/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/petergrill"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_key_visual()
        self.download_character()

    def download_key_visual(self):
        keyvisual_folder = self.base_folder + '/' + constants.FOLDER_KEY_VISUAL
        if not os.path.exists(keyvisual_folder):
            os.makedirs(keyvisual_folder)

        image_objs = [
            {'name': 'kv', 'url': 'http://petergrill-anime.jp/images/key_v_202003.png'}]
        for image_obj in image_objs:
            if os.path.exists(keyvisual_folder + '/' + image_obj['name'] + '.png') or \
                    os.path.exists(keyvisual_folder + '/' + image_obj['name'] + '.jpg'):
                continue
            filepath_without_extension = keyvisual_folder + '/' + image_obj['name']
            self.download_image(image_obj['url'], filepath_without_extension)

    def download_character(self):
        character_folder = self.base_folder + '/' + constants.FOLDER_CHARACTER
        if not os.path.exists(character_folder):
            os.makedirs(character_folder)

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
            pass


# Re:Zero kara Hajimeru Isekai Seikatsu 2nd Season
class ReZero2Download(UnconfirmedDownload):
    title = "Re:Zero kara Hajimeru Isekai Seikatsu 2nd Season"
    keywords = ["Re:Zero kara Hajimeru Isekai Seikatsu 2nd Season",
                "Re:Zero - Starting Life in Another World"]

    PAGE_PREFIX = "http://re-zero-anime.jp/tv/story/"

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/rezero2"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        pass


# Tonikaku Kawaii
class TonikawaDownload(UnconfirmedDownload):
    title = "Tonikaku Kawaii"
    keywords = ["Tonikaku Kawaii", "Cawaii", "Fly Me to the Moon"]

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/tonikawa"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_key_visual()

    def download_key_visual(self):
        keyvisual_folder = self.base_folder + '/' + constants.FOLDER_KEY_VISUAL
        if not os.path.exists(keyvisual_folder):
            os.makedirs(keyvisual_folder)

        image_objs = [
            {'name': 'w_teaser_1', 'url': 'https://pbs.twimg.com/media/EXzj-iYVcAElclE?format=jpg&name=large'},
            {'name': 'w_teaser_2', 'url': 'https://pbs.twimg.com/media/EXzj-iaU0AATNM7?format=jpg&name=large'},
            {'name': 'w_teaser_3', 'url': 'http://tonikawa.com/assets/images/common/news/news-1/img.jpg'}]
        for image_obj in image_objs:
            if os.path.exists(keyvisual_folder + '/' + image_obj['name'] + '.png') or \
                    os.path.exists(keyvisual_folder + '/' + image_obj['name'] + '.jpg'):
                continue
            filepath_without_extension = keyvisual_folder + '/' + image_obj['name']
            self.download_image(image_obj['url'], filepath_without_extension)


# Uzaki-chan wa Asobitai!
class UzakiChanDownload(UnconfirmedDownload):
    title = "Uzaki-chan wa Asobitai!"
    keywords = ["Uzaki-chan wa Asobitai!", "Uzakichan"]

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/uzakichan"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_key_visual()

    def download_key_visual(self):
        keyvisual_folder = self.base_folder + '/' + constants.FOLDER_KEY_VISUAL
        if not os.path.exists(keyvisual_folder):
            os.makedirs(keyvisual_folder)

        image_objs = [
            {'name': 'kv', 'url': 'https://pbs.twimg.com/media/EP1u35XUEAAvg4f?format=jpg&name=large'},
            {'name': 'kv2', 'url': 'https://pbs.twimg.com/media/EXi1RaHUYAAVJPM?format=jpg&name=medium'}]
        for image_obj in image_objs:
            if os.path.exists(keyvisual_folder + '/' + image_obj['name'] + '.png'):
                continue
            filepath_without_extension = keyvisual_folder + '/' + image_obj['name']
            self.download_image(image_obj['url'], filepath_without_extension)


# Yahari Ore no Seishun Love Comedy wa Machigatteiru. Kan
class Oregairu3Download(UnconfirmedDownload):
    title = "Yahari Ore no Seishun Love Comedy wa Machigatteiru. Kan"
    keywords = ["Oregairu", "Yahari Ore no Seishun Love Comedy wa Machigatteiru. Kan",
                "My Teen Romantic Comedy SNAFU 3", "My youth romantic comedy is wrong as I expected 3"]

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
