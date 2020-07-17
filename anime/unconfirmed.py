import os
import anime.constants as constants
from anime.main_download import MainDownload

# 100-man no Inochi no Ue ni Ore wa Tatteiru http://1000000-lives.com/ #俺100 @1000000_lives
# Bokutachi no Remake http://bokurema.com/ #ぼくリメ #bokurema @bokurema
# Cheat Kusushi no Slow Life: Isekai ni Tsukurou Drugstore https://www.cheat-kusushi.jp/ #チート薬師 #スローライフ @cheat_kusushi
# Danmachi III http://danmachi.com/danmachi3/ #danmachi @danmachi_anime
# Higurashi no Naku Koro ni (2020) https://higurashianime.com/ #ひぐらし @higu_anime
# Ijiranaide, Nagatoro-san https://www.nagatorosan.jp/ #長瀞さん @nagatoro_tv
# Iwa Kakeru!: Sport Climbing Girls http://iwakakeru-anime.com/ #いわかける #iwakakeru @iwakakeru_anime
# Kaifuku Jutsushi no Yarinaoshi http://kaiyari.com/ #回復術士 @kaiyari_anime
# Kamisama ni Natta Hi https://kamisama-day.jp/ #神様になった日 @kamisama_Ch_AB
# Kami-tachi ni Hirowareta Otoko https://kamihiro-anime.com/ #神達に拾われた男 @kamihiro_anime
# Kuma Kuma Kuma Bear https://kumakumakumabear.com/ #くまクマ熊ベアー #kumabear @kumabear_anime
# Kimi to Boku no Saigo no Senjou, Aruiwa Sekai ga Hajimaru Seisen https://kimisentv.com/ #キミ戦 #kimisen @kimisen_project
# Majo no Tabitabi https://majotabi.jp/ #魔女の旅々 #魔女の旅々はいいぞ #majotabi @majotabi_PR
# Maou-jou de Oyasumi https://maoujo-anime.com/ #魔王城でおやすみ @maoujo_anime
# Mushoku Tensei https://mushokutensei.jp/ #無職転生 @mushokutensei_A
# Ochikobore Fruit Tart http://ochifuru-anime.com/ #ochifuru @ochifuru_anime
# Ore dake Haireru Kakushi Dungeon https://kakushidungeon-anime.jp/ #隠しダンジョン @kakushidungeon
# Rail Romanesque https://railromanesque.jp/ @rail_romanesque #まいてつ #レヱルロマネスク
# Tatoeba Last Dungeon https://lasdan.com/ #ラスダン @lasdan_PR
# Tonikaku Kawaii http://tonikawa.com/ #トニカクカワイイ #tonikawa @tonikawa_anime


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


# 100-man no Inochi no Ue ni Ore wa Tatteiru
class HyakumanNoInochiDownload(UnconfirmedDownload):
    title = "100-man no Inochi no Ue ni Ore wa Tatteiru"
    keywords = [title, "I'm standing on 1,000,000 lives.", "Hyakuman"]

    PAGE_PREFIX = 'http://1000000-lives.com/'

    def __init__(self):
        super().__init__()
        self.init_base_folder('100-man-no-inochi')

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'kv', 'url': 'https://pbs.twimg.com/media/ESLrKCWUcAExG_i?format=jpg&name=4096x4096'}]
        self.download_image_objects(image_objs, folder)

    def download_character(self):
        folder = self.create_character_directory()
        chara_url_template = 'http://1000000-lives.com/img/index/img_character%s.png'
        i = 0
        while True:
            i += 1
            image_name = 'img_character' + str(i).zfill(2)
            if self.is_image_exists(image_name, folder):
                continue
            image_url = chara_url_template % str(i).zfill(2)
            image_filepath = folder + '/' + image_name
            result = self.download_image(image_url, image_filepath)
            if result == -1:
                break


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


# Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka III
class Danmachi3Download(UnconfirmedDownload):
    title = 'Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka III'
    keywords = [title, 'Danmachi', 'Is It Wrong to Try to Pick Up Girls in a Dungeon? III', '3rd']

    PAGE_PREFIX = 'http://danmachi.com/danmachi3/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/danmachi3"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'teaser', 'url': 'https://pbs.twimg.com/media/ETtwMdUUMAAdqd1?format=jpg&name=4096x4096'},
            {'name': 'kv1', 'url': 'https://pbs.twimg.com/media/EcCRpVLUcAAdpGv?format=jpg&name=900x900'}
        ]
        self.download_image_objects(image_objs, folder)


# Higurashi no Naku Koro ni (2020)
class Higurashi2020Download(UnconfirmedDownload):
    title = "Higurashi no Naku Koro ni"
    keywords = [title, "When They Cry"]

    PAGE_PREFIX = 'https://higurashianime.com/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/higurashi2020"
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
            {'name': 'kv', 'url': 'https://higurashianime.com/images/images/v_001.jpg'}]
        self.download_image_objects(image_objs, filepath)

    def download_character(self):
        filepath = self.create_character_directory()
        image_objs = []
        image_url_template = 'https://higurashianime.com/images/chara/p_%s_%s.png'
        try:
            soup = self.get_soup('https://higurashianime.com/chara.html')
            chara_url_tags = soup.find('div', class_='chara_list_wrap').find_all('a')
            for chara_url_tag in chara_url_tags:
                chara_short_url = chara_url_tag['href']
                chara_num = str(int(chara_short_url.split('chara')[1].split('.html')[0]))
                for j in range(1, 3, 1):
                    image_name = 'chara' + chara_num.zfill(2) + '_' + str(j)
                    image_url = image_url_template % (str(j).zfill(2), chara_num.zfill(2))
                    image_objs.append({'name': image_name, 'url': image_url})
            self.download_image_objects(image_objs, filepath)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)


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


# Iwa Kakeru!: Sport Climbing Girls
class IwakakeruDownload(UnconfirmedDownload):
    title = "Iwa Kakeru!: Sport Climbing Girls"
    keywords = [title, "Iwakakeru"]

    PAGE_PREFIX = 'http://iwakakeru-anime.com/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/iwakakeru"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

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


# Kamisama ni Natta Hi
class KamisamaNiNattaHiDownload(UnconfirmedDownload):
    title = "Kamisama ni Natta Hi"
    keywords = [title, "The Day I Became a God"]

    PAGE_PREFIX = 'https://kamisama-day.jp/'

    def __init__(self):
        super().__init__()
        self.init_base_folder('kamisama-ni-natta-hi')

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'opening_1', 'url': 'https://kamisama-day.jp/assets/img/opening_1.jpg'},
            {'name': 'opening_2', 'url': 'https://kamisama-day.jp/assets/img/opening_2.jpg'},
            {'name': 'opening_3', 'url': 'https://kamisama-day.jp/assets/img/opening_3.jpg'},
            {'name': 'kv', 'url': 'https://kamisama-day.jp/assets/img/kv.jpg'}
        ]
        self.download_image_objects(image_objs, folder)


# Kami-tachi ni Hirowareta Otoko
class KamihiroDownload(UnconfirmedDownload):
    title = 'Kami-tachi ni Hirowareta Otoko'
    keywords = [title, 'Kamihiro', 'Kamitachi']

    PAGE_PREFIX = 'https://kamihiro-anime.com'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/kamihiro"
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
            {'name': 'teaser', 'url': 'https://pbs.twimg.com/media/EVy1wvNVcAAWcJH?format=jpg&name=large'},
            {'name': 'kv1', 'url': 'https://pbs.twimg.com/media/Eb_jqRLUYAAZ01A?format=jpg&name=4096x4096'}
        ]
        self.download_image_objects(image_objs, folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.find_all('div', class_='char')
            image_objs = []
            for image in images:
                image_tag = image.find('img')
                if image_tag is None:
                    continue
                image_url = self.PAGE_PREFIX + image_tag['src']
                image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                image_objs.append({'name': image_name, 'url': image_url})
            self.download_image_objects(image_objs, folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)



# Kimi to Boku no Saigo no Senjou, Aruiwa Sekai ga Hajimaru Seisen
class KimisenDownload(UnconfirmedDownload):
    title = "Kimi to Boku no Saigo no Senjou, Aruiwa Sekai ga Hajimaru Seisen"
    keywords = [title, "Kimisen"]

    PAGE_PREFIX = 'https://kimisentv.com/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/kimisen"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_key_visual(self):
        keyvisual_folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'teaser', 'url': 'https://kimisentv.com/teaser/images/top-main-vis.jpg'}]
        self.download_image_objects(image_objs, keyvisual_folder)

    def download_character(self):
        folder = self.create_character_directory()
        character_url = 'https://kimisentv.com/assets/character/c%s.png'
        i = 0
        while True:
            i += 1
            image_name = 'c' + str(i)
            if self.is_image_exists(image_name, folder):
                continue
            image_url = character_url % str(i)
            result = self.download_image(image_url, folder + '/' + image_name)
            if result == -1:
                break


# Kuma Kuma Kuma Bear
class KumaBearDownload(UnconfirmedDownload):
    title = "Kuma Kuma Kuma Bear"
    keywords = [title]

    PAGE_PREFIX = 'https://kumakumakumabear.com/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/kumabear"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

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

    def download_character(self):
        folder = self.create_character_directory()
        try:
            img_objs = [{'name': 'list_img',
                'url': 'https://kumakumakumabear.com/core_sys/images/main/character/list_img.png'}]
            self.download_image_objects(img_objs, folder)

            soup = self.get_soup('https://kumakumakumabear.com/chara/')
            chara_tags = soup.find_all('div', class_='nwu_box')
            for chara_tag in chara_tags:
                chara_url_tag = chara_tag.find('a')
                chara_url = self.PAGE_PREFIX + chara_url_tag['href'].replace('../', '')
                chara_num = chara_url.split('/')[-1].split('.html')[0].zfill(2)
                if os.path.exists(folder + '/' + 'thumb_' + chara_num + '.png')\
                        and not (chara_num == '01' or chara_num == '02'):
                    continue
                image_objs_list = [{'name': 'thumb_' + chara_num, 'url': self.PAGE_PREFIX
                    + chara_url_tag.find('img')['src'].replace('../', '')}]
                if chara_num == '01' or chara_num == '02':
                    if os.path.exists(folder + '/' + 'main_' + chara_num + 'a' + '.png') \
                            and os.path.exists(folder + '/' + 'main_' + chara_num + '.png'):
                        continue
                    if not os.path.exists(folder + '/' + 'main_' + chara_num + '.png'):
                        if chara_num == '01':
                            image_objs_list.append({'name': 'main_01', 'url': 'https://66.media.tumblr.com/9c9652165c3656fefc86789815a5585d/c8a5ee31f02427b4-47/s1280x1920/782016087a2ee0740a8f54341e58bffad80addcb.png'})
                        elif chara_num == '02':
                            image_objs_list.append({'name': 'main_02', 'url': 'https://66.media.tumblr.com/a469c9d9b8c8016ef2b957be6f1f05cd/c8a5ee31f02427b4-dc/s1280x1920/4694b1072c94a3c7a3a90ffc71fb74d1c5170aae.png'})
                chara_soup = self.get_soup(chara_url)
                chara_frame = chara_soup.find('div', class_='chraFrame')

                chara_sub_images = chara_frame.find_all('div', class_='charaSubImg')
                for i in range(len(chara_sub_images)):
                    chara_sub_name = 'sub_' + chara_num
                    if len(chara_sub_images) > 1:
                        chara_sub_name += '_' + str(i + 1)
                    chara_sub_image_url = self.PAGE_PREFIX + chara_sub_images[i].find('img')['src'].replace('../', '')
                    image_objs_list.append({'name': chara_sub_name, 'url': chara_sub_image_url})

                chara_main_images = chara_frame.find_all('div', class_='charaMainImg')
                for i in range(len(chara_main_images)):
                    chara_main_name = 'main_' + chara_num
                    if chara_num == '01' or chara_num == '02':
                        chara_main_name += 'a'
                    if len(chara_sub_images) > 1:
                        chara_main_name += '_' + str(i + 1)
                    chara_main_image_url = self.PAGE_PREFIX + chara_main_images[i].find('img')['src'].replace('../', '')
                    image_objs_list.append({'name': chara_main_name, 'url': chara_main_image_url})

                scene_images = chara_frame.find('ul', class_='sceneImg').find_all('img')
                for i in range(len(scene_images)):
                    image_objs_list.append({'name': 'scene_' + chara_num + '_' + str(i + 1), 'url': self.PAGE_PREFIX
                        + scene_images[i]['src'].replace('../', '')})
                self.download_image_objects(image_objs_list, folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)


class MajotabiDownload(UnconfirmedDownload):
    title = "Majo no Tabitabi"
    keywords = [title, "Wandering Witch: The Journey of Elaina", "Majotabi"]

    PAGE_PREFIX = 'https://majotabi.jp/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/majotabi"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_key_visual(self):
        keyvisual_folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'kv1', 'url': 'https://pbs.twimg.com/media/EHPjPtFU8AAHo9S?format=jpg&name=large'},
            {'name': 'kv2', 'url': 'https://pbs.twimg.com/media/ESahsP9UEAAhzgn?format=jpg&name=large'},
            {'name': 'kv3', 'url': 'https://pbs.twimg.com/media/EUqV9B7UcAAOCeE?format=jpg&name=medium'},
            {'name': 'kv4', 'url': 'https://pbs.twimg.com/media/EW64PYgUMAAGDIk?format=jpg&name=4096x4096'},
            {'name': 'kv5', 'url': 'https://pbs.twimg.com/media/EZvKDzlUcAEVTt-?format=jpg&name=large'},
            {'name': 'kv6', 'url': 'https://pbs.twimg.com/media/Eb_X0idVAAAjpNx?format=jpg&name=medium'}
        ]
        self.download_image_objects(image_objs, keyvisual_folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            characters = soup.find_all('div', class_='chr-img')
            image_objs = []
            for character in characters:
                image_tag = character.find('img')
                if image_tag is None:
                    continue
                image_url = self.PAGE_PREFIX + image_tag['src'].replace('./', '')
                image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                image_objs.append({'name': image_name, 'url': image_url})
            self.download_image_objects(image_objs, folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)


# Maou-jou de Oyasumi
class MaoujoDownload(UnconfirmedDownload):
    title = "Maou-jou de Oyasumi"
    keywords = [title, "Maoujo", "Sleepy Princess in the Demon Castle"]

    PAGE_PREFIX = 'https://maoujo-anime.com/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/maoujo"
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
        image_objs = [{'name': 'teaser', 'url': 'https://pbs.twimg.com/media/EOUT0DDU0AEEKKN?format=jpg&name=900x900'},
                      #{'name': 'teaser_2', 'url': 'https://maoujo-anime.com/img/visual/visual_01.png'},
                      {'name': 'teaser_2', 'url': 'https://64.media.tumblr.com/48ca6877e25711c2f1122fe1ea52167e/e6093826ece4bf20-9a/s2048x3072/88f0c7494e7d2c8c95f5b9495b79cdb6b799f401.png'},
                      {'name': 'kv', 'url': 'https://maoujo-anime.com/img/home/visual_02.jpg'},
                      {'name': 'gensaku_20200527', 'url': 'https://maoujo-anime.com/special/illust/gensaku_20200527.jpg'},
                      {'name': 'gensaku_twitter', 'url': 'https://pbs.twimg.com/media/EY_hB6lVcAAduDe?format=jpg&name=medium'}]
        self.download_image_objects(image_objs, folder)

    def download_character(self):
        folder = self.create_character_directory()
        image_objs = []
        try:
            json_obj = self.get_json('https://maoujo-anime.com/character/chara_data.php')
            charas = json_obj['charas']
            for chara in charas:
                image_url = self.PAGE_PREFIX + chara['images']['visual'].split('?')[0]
                image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                image_objs.append({'name': image_name, 'url': image_url})
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)
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

# Ochikobore Fruit Tart
class OchifuruDownload(UnconfirmedDownload):
    title = "Ochikobore Fruit Tart"
    keywords = [title, "Dropout Idol", "Ochifuru"]

    PAGE_PREFIX = 'http://ochifuru-anime.com/'
    CHARA_IMAGE_TEMPLATE = 'http://ochifuru-anime.com/images/chara/%s/p_002.png'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/ochifuru"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_key_visual(self):
        keyvisual_folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'kv', 'url': 'https://pbs.twimg.com/media/EKb4OniUwAELo-b?format=jpg&name=medium'}]
        self.download_image_objects(image_objs, keyvisual_folder)

    def download_character(self):
        character_folder = self.base_folder + '/' + constants.FOLDER_CHARACTER
        if not os.path.exists(character_folder):
            os.makedirs(character_folder)

        try:
            i = 0
            while True:
                i += 1
                filepath_without_extension = character_folder + '/chara_' + str(i).zfill(2)
                if os.path.exists(filepath_without_extension + '.png') or \
                        os.path.exists(filepath_without_extension + '.jpg'):

                    continue
                image_url = self.CHARA_IMAGE_TEMPLATE % str(i).zfill(3)
                result = self.download_image(image_url, filepath_without_extension)
                if result == -1:
                    break
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)


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


# Rail Romanesque
class RailRomanesqueDownload(UnconfirmedDownload):
    title = "Rail Romanesque"
    keywords = [title, "Maitetsu"]

    PAGE_PREFIX = 'https://railromanesque.jp/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/rail-romanesque"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        #self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [{'name': 'kv', 'url': 'https://ogre.natalie.mu/media/news/comic/2020/0624/railromanesque_main.jpg'}]
        self.download_image_objects(image_objs, folder)

    def download_character(self):
        folder = self.create_character_directory()
        i = 0
        chara_url = 'https://railromanesque.jp/wp-content/themes/railromanesque/image/contents/top/chara-detail/%s-stand.png'
        while True:
            i += 1
            image_url = chara_url % str(i).zfill(2)
            image_name = self.extract_image_name_from_url(image_url, with_extension=True)
            if os.path.exists(folder + '/' + image_name):
                continue
            result = self.download_image(image_url, folder + '/' + image_name)
            if result == -1:
                break


# Senyoku no Sigrdrifa
class SigrdrifaDownload(UnconfirmedDownload):
    title = "Senyoku no Sigrdrifa"
    keywords = [title, "Warlords of Sigrdrifa", "Sigururi"]

    PAGE_PREFIX = "https://sigururi.com/"

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/sigrdrifa"
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
        image_objs = [{'name': 'kv_01_pc', 'url': 'https://sigururi.com/assets/img/top/kv_01_pc.jpg'},
                      {'name': 'kv_01_sp', 'url': 'https://sigururi.com/assets/img/top/kv_01_sp.jpg'},
                      {'name': 'kv_02_pc', 'url': 'https://sigururi.com/assets/img/top/kv_02_pc.jpg'},
                      {'name': 'kv_02_sp', 'url': 'https://sigururi.com/assets/img/top/kv_02_sp.jpg'},
                      {'name': 'kv_03_pc', 'url': 'https://sigururi.com/assets/img/top/kv_03_pc.jpg'},
                      {'name': 'kv_03_sp', 'url': 'https://sigururi.com/assets/img/top/kv_03_sp.jpg'}]
        self.download_image_objects(image_objs, folder)

    def download_character(self):
        folder = self.create_character_directory()
        image_url_templates = ['https://sigururi.com/assets/img/chara/chara_%s.png',
                               'https://sigururi.com/assets/img/character/chara_%s_new.png']
        for image_url_template in image_url_templates:
            i = 0
            while True:
                i += 1
                image_url = image_url_template % str(i).zfill(2)
                image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                image_name_with_extension = self.extract_image_name_from_url(image_url, with_extension=True)
                filepath_without_extension = folder + '/' + image_name
                filepath = folder + '/' + image_name_with_extension
                if os.path.exists(filepath):
                    continue
                result = self.download_image(image_url, filepath_without_extension)
                if result == -1:
                    break


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


# Tonikaku Kawaii
class TonikawaDownload(UnconfirmedDownload):
    title = "Tonikaku Kawaii"
    keywords = [title, "Tonikawa", "Cawaii", "Fly Me to the Moon"]

    PAGE_PREFIX = 'http://tonikawa.com/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/tonikawa"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

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

