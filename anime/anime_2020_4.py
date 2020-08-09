import os
import anime.constants as constants
from anime.main_download import MainDownload
from datetime import datetime
from scan import AniverseMagazineScanner, MocaNewsScanner, WebNewtypeScanner

# 100-man no Inochi no Ue ni Ore wa Tatteiru http://1000000-lives.com/ #俺100 @1000000_lives
# Danmachi III http://danmachi.com/danmachi3/ #danmachi @danmachi_anime
# Gochuumon wa Usagi desu ka? Bloom https://gochiusa.com/bloom/ #gochiusa @usagi_anime
# Higurashi no Naku Koro ni (2020) https://higurashianime.com/ #ひぐらし @higu_anime
# Iwa Kakeru!: Sport Climbing Girls http://iwakakeru-anime.com/ #いわかける #iwakakeru @iwakakeru_anime
# Kamisama ni Natta Hi https://kamisama-day.jp/ #神様になった日 @kamisama_Ch_AB
# Kami-tachi ni Hirowareta Otoko https://kamihiro-anime.com/ #神達に拾われた男 @kamihiro_anime
# Kimi to Boku no Saigo no Senjou, Aruiwa Sekai ga Hajimaru Seisen https://kimisentv.com/ #キミ戦 #kimisen @kimisen_project
# Kuma Kuma Kuma Bear https://kumakumakumabear.com/ #くまクマ熊ベアー #kumabear @kumabear_anime
# Maesetsu https://maesetsu.jp/ #まえせつ @maesetsu_anime
# Mahouka Koukou no Rettousei: Raihousha-hen https://mahouka.jp/ #mahouka @mahouka_anime
# Majo no Tabitabi https://majotabi.jp/ #魔女の旅々 #魔女の旅々はいいぞ #majotabi @majotabi_PR
# Maou-jou de Oyasumi https://maoujo-anime.com/ #魔王城でおやすみ @maoujo_anime
# Ochikobore Fruit Tart http://ochifuru-anime.com/ #ochifuru @ochifuru_anime
# Rail Romanesque https://railromanesque.jp/ @rail_romanesque #まいてつ #レヱルロマネスク
# Senyoku no Sigrdrifa https://sigururi.com/ #シグルリ @sigururi
# Tatoeba Last Dungeon https://lasdan.com/ #ラスダン @lasdan_PR
# Tonikaku Kawaii http://tonikawa.com/ #トニカクカワイイ #tonikawa @tonikawa_anime


# Fall 2020 Anime
class Fall2020AnimeDownload(MainDownload):
    season = "2020-4"
    season_name = "Fall 2020"

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/2020-4"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)


# 100-man no Inochi no Ue ni Ore wa Tatteiru
class HyakumanNoInochiDownload(Fall2020AnimeDownload):
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
            {'name': 'kv', 'url': 'https://pbs.twimg.com/media/ESLrKCWUcAExG_i?format=jpg&name=4096x4096'},
            {'name': 'kv2', 'url': 'https://pbs.twimg.com/media/Ee03f7CU8AUtfE5?format=png&name=large'}]
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


# Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka III
class Danmachi3Download(Fall2020AnimeDownload):
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


# Gochuumon wa Usagi Desu ka? Bloom
class GochiUsa3Download(Fall2020AnimeDownload):
    title = "Gochuumon wa Usagi Desu ka? Bloom"
    keywords = [title, 'Gochiusa', '3rd']

    PAGE_PREFIX = 'https://gochiusa.com/bloom/'

    def __init__(self):
        super().__init__()
        self.init_base_folder('gochiusa3')

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'original_kv', 'url': 'https://gochiusa.com/bloom/core_sys/images/main/home/main_img.jpg'},
            {'name': 'kv', 'url': 'https://pbs.twimg.com/media/EdIvRRNUEAI7tTZ?format=jpg&name=medium'}
        ]
        self.download_image_objects(image_objs, folder)


# Higurashi no Naku Koro ni (2020)
class Higurashi2020Download(Fall2020AnimeDownload):
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


# Iwa Kakeru!: Sport Climbing Girls
class IwakakeruDownload(Fall2020AnimeDownload):
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
        self.download_character()

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

    def download_character(self):
        folder = self.create_character_directory()
        chara_url_template = 'http://iwakakeru-anime.com/img/character/chara%s.png'
        thumb_url_template = 'http://iwakakeru-anime.com/img/character/chara%s_thum.png'
        face_url_template = 'http://iwakakeru-anime.com/img/character/chara%s_face%s.png'
        maximum = 0
        try:
            soup = self.get_soup('http://iwakakeru-anime.com/character/')
            main_inner_div = soup.find('div', id='main_inner')
            if main_inner_div is not None:
                sections = main_inner_div.find_all('section')
                for section in sections:
                    links = section.find_all('a')
                    for link in links:
                        if link.has_attr('href') and 'chara' in link['href'] and '.php' in link['href']:
                            try:
                                number = int(link['href'].split('.php')[0].split('chara')[1])
                                if number > maximum:
                                    maximum = number
                            except:
                                pass
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)
            return

        for i in range(1, maximum + 1, 1):
            chara_name = 'chara' + str(i)
            if self.is_image_exists(chara_name, folder):
                continue
            chara_url = chara_url_template % str(i)
            result = self.download_image(chara_url, folder + '/' + chara_name)
            if result == -1:
                continue
            image_objs = [
                {'name': 'chara' + str(i) + '_thum', 'url': thumb_url_template % str(i)},
                {'name': 'chara' + str(i) + '_face1', 'url': face_url_template % (str(i), '1')},
                {'name': 'chara' + str(i) + '_face2', 'url': face_url_template % (str(i), '2')}
            ]
            self.download_image_objects(image_objs, folder)


# Kamisama ni Natta Hi
class KamisamaNiNattaHiDownload(Fall2020AnimeDownload):
    title = "Kamisama ni Natta Hi"
    keywords = [title, "The Day I Became a God"]

    PAGE_PREFIX = 'https://kamisama-day.jp/'

    def __init__(self):
        super().__init__()
        self.init_base_folder('kamisama-ni-natta-hi')

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'opening_1', 'url': 'https://kamisama-day.jp/assets/img/opening_1.jpg'},
            {'name': 'opening_2', 'url': 'https://kamisama-day.jp/assets/img/opening_2.jpg'},
            {'name': 'opening_3', 'url': 'https://kamisama-day.jp/assets/img/opening_3.jpg'},
            {'name': 'kv', 'url': 'https://kamisama-day.jp/assets/img/kv.jpg'},
            {'name': 'kv2', 'url': 'https://kamisama-day.jp/assets/img/top/kv.jpg'}
        ]
        self.download_image_objects(image_objs, folder)

    def download_character(self):
        folder = self.create_character_directory()
        image_objs = []
        face_url = 'https://kamisama-day.jp/assets/img/chara/face_%s.png'
        img_url = 'https://kamisama-day.jp/assets/img/chara/img_%s.png'
        try:
            soup = self.get_soup('https://kamisama-day.jp/character/')
            nav = soup.find('nav', class_='chara_nav')
            if nav is not None:
                chara_links = nav.find_all('a')
                for chara_link in chara_links:
                    if chara_link.has_attr('href') and '?chara=' in chara_link['href']:
                        chara_name = chara_link['href'].split('?chara=')[1]
                        image_objs.append({'name': 'face_' + chara_name, 'url': face_url % chara_name})
                        image_objs.append({'name': 'img_' + chara_name, 'url': img_url % chara_name})
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)
        self.download_image_objects(image_objs, folder)


# Kami-tachi ni Hirowareta Otoko
class KamihiroDownload(Fall2020AnimeDownload):
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
            {'name': 'kv1', 'url': 'https://pbs.twimg.com/media/Eb_jqRLUYAAZ01A?format=jpg&name=4096x4096'},
            {'name': 'kv2', 'url': 'https://kamihiro-anime.com/wp/wp-content/uploads/2020/08/GF_KV2_logo.jpg'},
            #{'name': 'kv2', 'url': 'https://pbs.twimg.com/media/Ee095ywUwAAOSpk?format=jpg&name=4096x4096'}
        ]
        self.download_image_objects(image_objs, folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup('https://kamihiro-anime.com/character/')
            images = soup.find_all('div', class_='thumb')
            image_objs = []
            for image in images:
                image_tag = image.find('img')
                if image_tag is None:
                    continue
                image_url = image_tag['src']
                image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                image_objs.append({'name': image_name, 'url': image_url})
            self.download_image_objects(image_objs, folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)


# Kimi to Boku no Saigo no Senjou, Aruiwa Sekai ga Hajimaru Seisen
class KimisenDownload(Fall2020AnimeDownload):
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
class KumaBearDownload(Fall2020AnimeDownload):
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
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'main_img', 'url': 'https://kumakumakumabear.com/core_sys/images/main/tz/main_img.jpg'},
            {'name': 'main_img_2', 'url': 'https://kumakumakumabear.com/core_sys/images/main/tz/main_img_2.jpg'},
            {'name': 'main_img_3', 'url': 'https://kumakumakumabear.com/core_sys/images/main/tz/main_img_3.jpg'},
            {'name': 'main_img_4', 'url': 'https://kumakumakumabear.com/core_sys/images/main/tz/main_img_4.jpg'},
            {'name': 'pop_img', 'url': 'https://kumakumakumabear.com/core_sys/images/main/tz/pop_img.jpg'},
            {'name': 'pop_img', 'url': 'https://pbs.twimg.com/media/EeFRDpaU8AAiFuh?format=jpg&name=large'}
        ]
        self.download_image_objects(image_objs, folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            img_objs = [{'name': 'list_img',
                'url': 'https://kumakumakumabear.com/core_sys/images/main/character/list_img.png'}]

            special_chara_numbers = [str(num).zfill(2) for num in range(1, 6, 1)]
            special_chara_images = [
                'https://64.media.tumblr.com/9c9652165c3656fefc86789815a5585d/c8a5ee31f02427b4-47/s1280x1920/782016087a2ee0740a8f54341e58bffad80addcb.png',
                'https://64.media.tumblr.com/a469c9d9b8c8016ef2b957be6f1f05cd/c8a5ee31f02427b4-dc/s1280x1920/4694b1072c94a3c7a3a90ffc71fb74d1c5170aae.png',
                'https://64.media.tumblr.com/3025601ebb1822281a044f001d3bd3c3/c8a5ee31f02427b4-d0/s1280x1920/0f322395fd351ea30d7d9764cbaa7b715e2dd883.png',
                'https://64.media.tumblr.com/a27fee0b02d89dbee41c459b1b42e7fa/c8a5ee31f02427b4-3d/s1280x1920/c11c77d6e7bbd2fa7030be197f19522ba46703ec.png',
                'https://64.media.tumblr.com/5a26e287b34a1ccd1713d27a13c9293f/c8a5ee31f02427b4-62/s1280x1920/a67e3bf69f98bb7deb2c565ce0d07045d2baecf9.png'
            ]
            for i in range(len(special_chara_images)):
                img_objs.append({'name': 'main_' + str(i + 1).zfill(2), 'url': special_chara_images[i]})
            self.download_image_objects(img_objs, folder)

            soup = self.get_soup('https://kumakumakumabear.com/chara/')
            chara_tags = soup.find_all('div', class_='nwu_box')
            for chara_tag in chara_tags:
                chara_url_tag = chara_tag.find('a')
                chara_url = self.PAGE_PREFIX + chara_url_tag['href'].replace('../', '')
                chara_num = chara_url.split('/')[-1].split('.html')[0].zfill(2)
                if os.path.exists(folder + '/' + 'thumb_' + chara_num + '.png')\
                        and not (chara_num in special_chara_numbers):
                    continue
                if chara_num in special_chara_numbers and os.path.exists(folder + '/' + 'main_' + chara_num + 'a.png'):
                    continue
                image_objs_list = [{'name': 'thumb_' + chara_num, 'url': self.PAGE_PREFIX
                    + chara_url_tag.find('img')['src'].replace('../', '')}]
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
                    if chara_num in special_chara_numbers:
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


# Maesetsu!
class MaesetsuDownload(Fall2020AnimeDownload):
    title = "Maesetsu!"
    keywords = [title]

    PAGE_PREFIX = 'https://maesetsu.jp/'

    def __init__(self):
        super().__init__()
        self.init_base_folder('maesetsu')

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()
        self.download_other()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'kv', 'url': 'https://maesetsu.jp/core_sys/images/main/tz/kv.png'},
            {'name': 'kv2', 'url': 'https://maesetsu.jp/core_sys/images/main/tz/kv2.jpg'},
            {'name': 'kv3', 'url': 'https://maesetsu.jp/core_sys/images/main/tz/kv3.jpg'}
        ]
        self.download_image_objects(image_objs, folder)

    def download_character(self):
        folder = self.create_character_directory()
        image_objs = []
        face_url_template = 'https://maesetsu.jp/core_sys/images/main/tz/chara/msch%s_face.jpg'
        body_url_template = 'https://maesetsu.jp/core_sys/images/main/tz/chara/msch%s_body.jpg'
        for i in range(1, 12, 1):
            body_name = 'msch' + str(i) + '_body'
            if self.is_image_exists(body_name):
                continue
            face_name = 'msch' + str(i) + '_face'
            image_objs.append({'name': body_name, 'url': body_url_template % str(i)})
            image_objs.append({'name': face_name, 'url': face_url_template % str(i)})
        self.download_image_objects(image_objs, folder)

    def download_other(self):
        folder = self.create_custom_directory('other')
        image_objs = []
        image_url_template = 'https://maesetsu.jp/core_sys/images/main/tz/slider/scene_%s.jpg'
        for i in range(1, 23, 1):
            image_name = 'gallery_' + str(i).zfill(3)
            if self.is_image_exists(image_name):
                continue
            image_objs.append({'name': image_name, 'url': image_url_template % str(i).zfill(3)})
        self.download_image_objects(image_objs, folder)


# Mahouka Koukou no Rettousei: Raihousha-hen
class Mahouka2Download(Fall2020AnimeDownload):
    title = "Mahouka Koukou no Rettousei: Raihousha-hen"
    keywords = [title, "The Irregular at Magic High School", "2nd"]

    PAGE_PREFIX = 'https://mahouka.jp/'

    def __init__(self):
        super().__init__()
        self.init_base_folder('mahouka2')

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'teaser', 'url': 'https://mahouka.jp/news/SYS/CONTENTS/2019100420534812757301'},
            {'name': 'kv', 'url': 'https://mahouka.jp/assets/img/top/main/kv/kv.jpg'}
        ]
        self.download_image_objects(image_objs, folder)


# Majo no Tabitabi
class MajotabiDownload(Fall2020AnimeDownload):
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
            {'name': 'kv6', 'url': 'https://pbs.twimg.com/media/Eb_X0idVAAAjpNx?format=jpg&name=medium'},
            {'name': 'kv7', 'url': 'https://pbs.twimg.com/media/Eezxq0UUEAAj6vn?format=jpg&name=large'}
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
class MaoujoDownload(Fall2020AnimeDownload):
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


# Ochikobore Fruit Tart
class OchifuruDownload(Fall2020AnimeDownload):
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
            {'name': 'kv', 'url': 'https://pbs.twimg.com/media/EKb4OniUwAELo-b?format=jpg&name=medium'},
            {'name': 'kv_1', 'url': 'http://ochifuru-anime.com/images/top/v_001.png'},
            {'name': 'kv_2', 'url': 'http://ochifuru-anime.com/images/top/v_001m.png'},
            {'name': 'kv2', 'url': 'https://pbs.twimg.com/media/EeAHzyzU8AI2juU?format=jpg&name=medium'},
            {'name': 'kv2_1', 'url': 'http://ochifuru-anime.com/images/top/v_002.png'},
            {'name': 'kv2_2', 'url': 'http://ochifuru-anime.com/images/top/v_002m.png'}
        ]
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


# Rail Romanesque
class RailRomanesqueDownload(Fall2020AnimeDownload):
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
class SigrdrifaDownload(Fall2020AnimeDownload):
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
        self.download_other()

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

    def download_other(self):
        folder = self.create_custom_directory('other')
        image_objs = [
            {'name': 'news_vol_01', 'url': 'https://pbs.twimg.com/media/EdnNj1qVoAEY4MX?format=jpg&name=4096x4096'},
            {'name': 'news_vol_02', 'url': 'https://pbs.twimg.com/media/EeYvh7oUYAAdeWc?format=jpg&name=4096x4096'},
            {'name': 'uminohi', 'url': 'https://sigururi.com/SYS/CONTENTS/2020072310293692693264/w708'}
        ]
        self.download_image_objects(image_objs, folder)


# Tatoeba Last Dungeon Mae no Mura no Shounen ga Joban no Machi de Kurasu Youna Monogatari
class LasdanDownload(Fall2020AnimeDownload):
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
class TonikawaDownload(Fall2020AnimeDownload):
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
            {'name': 'w_teaser_3', 'url': 'http://tonikawa.com/assets/images/common/news/news-1/img.jpg'},
            {'name': 'kv', 'url': 'https://pbs.twimg.com/media/EeUsvfaVAAI-B7N?format=jpg&name=large'},
            {'name': 'img_keyvisual_character', 'url': 'http://tonikawa.com/assets/images/pc/index/img_keyvisual_character.png'}
        ]
        for image_obj in image_objs:
            if os.path.exists(keyvisual_folder + '/' + image_obj['name'] + '.png') or \
                    os.path.exists(keyvisual_folder + '/' + image_obj['name'] + '.jpg'):
                continue
            filepath_without_extension = keyvisual_folder + '/' + image_obj['name']
            self.download_image(image_obj['url'], filepath_without_extension)

