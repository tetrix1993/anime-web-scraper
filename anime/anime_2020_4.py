import os
import anime.constants as constants
from anime.main_download import MainDownload
from datetime import datetime
from scan import AniverseMagazineScanner, MocaNewsScanner, WebNewtypeScanner

# 100-man no Inochi no Ue ni Ore wa Tatteiru http://1000000-lives.com/ #俺100 @1000000_lives
# Adachi to Shimamura https://www.tbs.co.jp/anime/adashima/ #安達としまむら @adashima_staff
# Assault Lily: Bouquet https://anime.assaultlily-pj.com/ #アサルトリリィ @assaultlily_pj
# Danmachi III http://danmachi.com/danmachi3/ #danmachi @danmachi_anime
# Dogeza de Tanondemita https://dogeza-anime.com/ #土下座で @dgz_anime
# Gochuumon wa Usagi desu ka? Bloom https://gochiusa.com/bloom/ #gochiusa @usagi_anime
# Golden Kamuy 3rd Season https://www.kamuy-anime.com/ #ゴールデンカムイ @kamuy_official
# Higurashi no Naku Koro ni (2020) https://higurashianime.com/ #ひぐらし @higu_anime
# Iwa Kakeru!: Sport Climbing Girls http://iwakakeru-anime.com/ #いわかける #iwakakeru @iwakakeru_anime
# Jujutsu Kaisen https://jujutsukaisen.jp/ #呪術廻戦 @animejujutsu
# Kamisama ni Natta Hi https://kamisama-day.jp/ #神様になった日 @kamisama_Ch_AB
# Kami-tachi ni Hirowareta Otoko https://kamihiro-anime.com/ #神達に拾われた男 @kamihiro_anime
# Kimi to Boku no Saigo no Senjou, Aruiwa Sekai ga Hajimaru Seisen https://kimisentv.com/ #キミ戦 #kimisen @kimisen_project
# Kuma Kuma Kuma Bear https://kumakumakumabear.com/ #くまクマ熊ベアー #kumabear @kumabear_anime
# Maesetsu https://maesetsu.jp/ #まえせつ @maesetsu_anime
# Mahouka Koukou no Rettousei: Raihousha-hen https://mahouka.jp/ #mahouka @mahouka_anime
# Majo no Tabitabi https://majotabi.jp/ #魔女の旅々 #魔女の旅々はいいぞ #majotabi @majotabi_PR
# Maou-jou de Oyasumi https://maoujo-anime.com/ #魔王城でおやすみ @maoujo_anime
# Munou na Nana https://munounanana.com/ #無能なナナ @munounanana
# Ochikobore Fruit Tart http://ochifuru-anime.com/ #ochifuru @ochifuru_anime
# One Room S3 https://oneroom-anime.com/ #OneRoom @anime_one_room
# Rail Romanesque https://railromanesque.jp/ @rail_romanesque #まいてつ #レヱルロマネスク
# Senyoku no Sigrdrifa https://sigururi.com/ #シグルリ @sigururi
# Strike Witches: Road to Berlin http://w-witch.jp/strike_witches-rtb/ #w_witch #s_witch_rtb @RtbWitch
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
    STORY_PAGE = 'http://1000000-lives.com/story/'

    def __init__(self):
        super().__init__()
        self.init_base_folder('100-man-no-inochi')

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.STORY_PAGE)

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


# Adachi to Shimamura
class AdashimaDownload(Fall2020AnimeDownload):
    title = 'Adachi to Shimamura'
    keywords = [title, 'Adashima']

    PAGE_PREFIX = 'https://www.tbs.co.jp/anime/adashima/'
    STORY_PAGE = 'https://www.tbs.co.jp/anime/adashima/story/'

    def __init__(self):
        super().__init__()
        self.init_base_folder('adashima')

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()
        self.download_bluray()

    def download_episode_preview(self):
        self.has_website_updated(self.STORY_PAGE)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'teaser', 'url': 'https://pbs.twimg.com/media/EMwxnAfVUAAkw_i?format=jpg&name=medium'},
            {'name': 'kv1', 'url': 'https://pbs.twimg.com/media/Egzs0tCUMAA9ycs?format=jpg&name=medium'}]
        self.download_image_objects(image_objs, folder)

    def download_character(self):
        folder = self.create_character_directory()
        img_url_template = 'https://www.tbs.co.jp/anime/adashima/character/img/chara_stand_%s@2x.png'
        for i in range(1, 11, 1):
            img_url = img_url_template % str(i).zfill(2)
            img_name = 'chara_stand_%s@2x' % str(i).zfill(2)
            result = self.download_image(img_url, folder + '/' + img_name)
            if result == -1:
                break

    def download_bluray(self):
        folder = self.create_bluray_directory()
        image_objs = [
            {'name': 'music_op', 'url': 'https://pbs.twimg.com/media/Ehjk3IFUMAEm8g6?format=jpg&name=large'},
        ]
        self.download_image_objects(image_objs, folder)


# Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka III
class Danmachi3Download(Fall2020AnimeDownload):
    title = 'Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka III'
    keywords = [title, 'Danmachi', 'Is It Wrong to Try to Pick Up Girls in a Dungeon? III', '3rd']

    PAGE_PREFIX = 'http://danmachi.com/danmachi3/'
    STORY_PAGE = 'http://danmachi.com/danmachi3/story/index.html'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/danmachi3"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.STORY_PAGE)

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


# Golden Kamuy 3rd Season
class GoldenKamuy3Download(Fall2020AnimeDownload):
    title = "Golden Kamuy 3rd Season"
    keywords = [title, "Kamui"]

    PAGE_URL = "https://kamuy-anime.com/story/%s.html"
    PAGE_PREFIX = "https://kamuy-anime.com/"
    FIRST_EPISODE = 25
    FINAL_EPISODE = 36

    def __init__(self):
        super().__init__()
        self.init_base_folder('golden-kamuy3')

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        try:
            for i in range(self.FIRST_EPISODE, self.FINAL_EPISODE + 1, 1):
                episode = str(i).zfill(2)
                if self.is_file_exists(self.base_folder + "/" + episode + "_1.jpg"):
                    continue
                response = self.get_response(self.PAGE_URL % episode)
                split1 = response.split('<div class="ph"><a href="../')
                for j in range(1, len(split1), 1):
                    imageUrl = self.PAGE_PREFIX + split1[j].split('"')[0]
                    filepathWithoutExtension = self.base_folder + "/" + episode + '_' + str(j)
                    self.download_image(imageUrl, filepathWithoutExtension)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'kv1', 'url': 'https://pbs.twimg.com/media/Ea1xVSTUEAA1G7y?format=jpg&name=large'},
            {'name': 'kv2', 'url': 'https://pbs.twimg.com/media/Eh2IA2VUMAAdhyT?format=jpg&name=large'},
            {'name': 'kv3', 'url': 'https://pbs.twimg.com/media/Eh2IDQdVgAM9bfy?format=jpg&name=large'},
        ]
        self.download_image_objects(image_objs, folder)


# Higurashi no Naku Koro ni (2020)
class Higurashi2020Download(Fall2020AnimeDownload):
    title = "Higurashi no Naku Koro ni"
    keywords = [title, "When They Cry"]

    PAGE_PREFIX = 'https://higurashianime.com/'
    STORY_PAGE = 'https://higurashianime.com/intro.html'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/higurashi2020"
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
        filepath = self.create_key_visual_directory()
        image_objs = [
            {'name': 'kv', 'url': 'https://higurashianime.com/images/images/v_001.jpg'},
            {'name': 'kv1', 'url': 'https://higurashianime.com/images/index/v_002.jpg'},
            {'name': 'kv2', 'url': 'https://higurashianime.com/images/index/v_001.jpg'}
        ]
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

    def download_bluray(self):
        folder = self.create_bluray_directory()
        try:
            soup = self.get_soup('https://higurashianime.com/package.html')
            kiji_wraps = soup.find_all('div', class_='kiji_wrap')
            for kiji_wrap in kiji_wraps:
                image_tags = kiji_wrap.find_all('img')
                image_objs = []
                for image_tag in image_tags:
                    if image_tag.has_attr('src'):
                        image_url = self.PAGE_PREFIX + image_tag['src']
                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                        image_objs.append({'name': image_name, 'url': image_url})
                self.download_image_objects(image_objs, folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Blu-ray')
            print(e)


# Iwa Kakeru!: Sport Climbing Girls
class IwakakeruDownload(Fall2020AnimeDownload):
    title = "Iwa Kakeru!: Sport Climbing Girls"
    keywords = [title, "Iwakakeru"]

    PAGE_PREFIX = 'http://iwakakeru-anime.com/'
    STORY_PAGE = 'http://iwakakeru-anime.com/story/'

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
        self.has_website_updated(self.STORY_PAGE)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'mainvisual', 'url': 'http://iwakakeru-anime.com/img/index/mainvisual.png'},
            {'name': 'mainvisual_2', 'url': 'http://iwakakeru-anime.com/img/index/mainvisual_2.png'},
            {'name': 'kv2', 'url': 'https://pbs.twimg.com/media/EfLNG6MVAAAYWZ2?format=jpg&name=large'},
        ]
        self.download_image_objects(image_objs, folder)

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
    STORY_PAGE = 'https://kamisama-day.jp/story/'

    def __init__(self):
        super().__init__()
        self.init_base_folder('kamisama-ni-natta-hi')

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()
        self.download_music()
        self.download_other()

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

    def download_music(self):
        folder = self.create_custom_directory('music')
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'music/')
            contents_inner = soup.find('div', class_='main_contents_wrap')
            if contents_inner:
                img_tags = contents_inner.find_all('img')
                image_objs = []
                for img_tag in img_tags:
                    if img_tag.has_attr('src'):
                        image_url = self.PAGE_PREFIX + img_tag['src'].replace('../', '')
                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                        image_objs.append({'name': image_name, 'url': image_url})
                self.download_image_objects(image_objs, folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Music")
            print(e)

    def download_other(self):
        folder = self.create_custom_directory('other')
        image_objs = [
            {'name': 'bs11_guide', 'url': 'https://pbs.twimg.com/media/EilpMUKU4AAv0TX?format=jpg&name=large'}
        ]
        self.download_image_objects(image_objs, folder)


# Kami-tachi ni Hirowareta Otoko
class KamihiroDownload(Fall2020AnimeDownload):
    title = 'Kami-tachi ni Hirowareta Otoko'
    keywords = [title, 'Kamihiro', 'Kamitachi']

    PAGE_PREFIX = 'https://kamihiro-anime.com'
    STORY_PAGE = 'https://kamihiro-anime.com/story/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/kamihiro"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()
        self.download_music()

    def download_episode_preview(self):
        self.has_website_updated(self.STORY_PAGE)

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

    def download_music(self):
        folder = self.create_custom_directory('music')
        try:
            for music_page in ['opening-theme', 'ending-theme']:
                soup = self.get_soup(self.PAGE_PREFIX + '/music/' + music_page + '/')
                contents_inner = soup.find('div', class_='music-info__detail__data')
                if contents_inner:
                    img_tags = contents_inner.find_all('img')
                    image_objs = []
                    for img_tag in img_tags:
                        if img_tag.has_attr('src'):
                            image_url = img_tag['src']
                            image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                            image_objs.append({'name': image_name, 'url': image_url})
                    self.download_image_objects(image_objs, folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Music")
            print(e)


# Kimi to Boku no Saigo no Senjou, Aruiwa Sekai ga Hajimaru Seisen
class KimisenDownload(Fall2020AnimeDownload):
    title = "Kimi to Boku no Saigo no Senjou, Aruiwa Sekai ga Hajimaru Seisen"
    keywords = [title, "Kimisen"]

    PAGE_PREFIX = 'https://kimisentv.com/'
    STORY_PAGE = 'https://kimisentv.com/story/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/kimisen"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()
        self.download_music()

    def download_episode_preview(self):
        self.has_website_updated(self.STORY_PAGE)

    def download_key_visual(self):
        keyvisual_folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'teaser', 'url': 'https://kimisentv.com/teaser/images/top-main-vis.jpg'},
            {'name': 'kv1', 'url': 'https://pbs.twimg.com/media/EgvNvZXUYAEUPfC?format=jpg&name=large'}]
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

    def download_music(self):
        folder = self.create_custom_directory('music')
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'music/')
            contents_inner = soup.find('div', class_='cont-body')
            if contents_inner:
                img_tags = contents_inner.find_all('img')
                image_objs = []
                for img_tag in img_tags:
                    if img_tag.has_attr('src'):
                        image_url = self.PAGE_PREFIX + img_tag['src'].replace('../', '').split('?')[0]
                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                        image_objs.append({'name': image_name, 'url': image_url})
                self.download_image_objects(image_objs, folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Music")
            print(e)


# Kuma Kuma Kuma Bear
class KumaBearDownload(Fall2020AnimeDownload):
    title = "Kuma Kuma Kuma Bear"
    keywords = [title, 'Kumabear']

    PAGE_PREFIX = 'https://kumakumakumabear.com/'
    STORY_PAGE = 'https://kumakumakumabear.com/story/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/kumabear"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_key_visual()
        self.download_character()
        self.download_music()

    def download_episode_preview(self):
        self.download_episode_preview_guess()
        try:
            soup = self.get_soup(self.STORY_PAGE)
            content_div = soup.find('div', id='ContentsListUnit02')
            if content_div:
                title_divs = content_div.find_all('div', class_='title')
                for i in range(1, len(title_divs), 1):
                    a_tag = title_divs[i].find('a')
                    if a_tag and a_tag.has_attr('href'):
                        try:
                            episode = str(int(a_tag.text.replace('＃', '').replace('#', ''))).zfill(2)
                        except:
                            continue
                        if self.is_image_exists(episode + '_1'):
                            continue
                        episode_url = self.PAGE_PREFIX + a_tag['href'].replace('../', '')
                        episode_soup = self.get_soup(episode_url)
                        wdxmax_div_tag = episode_soup.find('div', class_='wdxmax')
                        if wdxmax_div_tag:
                            images = wdxmax_div_tag.find_all('img')
                            image_objs = []
                            for j in range(len(images)):
                                if images[j].has_attr('src'):
                                    image_url = self.PAGE_PREFIX + images[j]['src'].replace('../', '').split('?')[0]
                                    image_name = episode + '_' + str(j + 1)
                                    image_objs.append({'name': image_name, 'url': image_url})
                            self.download_image_objects(image_objs, self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_episode_preview_guess(self):
        story_template = 'https://kumakumakumabear.com/core_sys/images/contents/%s/block/%s/%s.jpg'
        content_num_first = 18
        block_num_first = 25
        image_num_first = 30
        for i in range(13):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            for j in range(4):
                img_num = str(j + 1)
                content_num = str(content_num_first + i).zfill(8)
                block_num = str(block_num_first + i).zfill(8)
                image_num = str(image_num_first + i * 4 + j).zfill(8)
                image_url = story_template % (content_num, block_num, image_num)
                image_name = episode + '_' + img_num
                result = self.download_image(image_url, self.base_folder + '/' + image_name)
                if result == -1:
                    return

    def download_episode_preview_external(self):
        jp_title = 'くまクマ熊ベアー'
        AniverseMagazineScanner(jp_title, self.base_folder).run()

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

                scene_image_tag = chara_frame.find('ul', class_='sceneImg')
                if scene_image_tag:
                    scene_images = scene_image_tag.find_all('img')
                    for i in range(len(scene_images)):
                        image_objs_list.append({'name': 'scene_' + chara_num + '_' + str(i + 1), 'url': self.PAGE_PREFIX
                            + scene_images[i]['src'].replace('../', '')})
                self.download_image_objects(image_objs_list, folder)

                chara_dam_img_tag = chara_frame.find('div', class_='charaDamImg')
                if chara_dam_img_tag:
                    dam_images = chara_dam_img_tag.find_all('img')
                    for i in range(len(dam_images)):
                        image_objs_list.append({'name': 'scene_' + chara_num + '_' + str(i + 1), 'url': self.PAGE_PREFIX
                            + dam_images[i]['src'].replace('../', '')})
                self.download_image_objects(image_objs_list, folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)

    def download_music(self):
        folder = self.create_custom_directory('music')
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'music/')
            contents_inner = soup.find('div', id='contents_inner')
            if contents_inner:
                img_tags = contents_inner.find_all('img')
                image_objs = []
                for img_tag in img_tags:
                    if img_tag.has_attr('src'):
                        image_url = self.PAGE_PREFIX + img_tag['src'].replace('../', '').split('?')[0]
                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                        image_objs.append({'name': image_name, 'url': image_url})
                self.download_image_objects(image_objs, folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Music")
            print(e)


# Maesetsu!
class MaesetsuDownload(Fall2020AnimeDownload):
    title = "Maesetsu!"
    keywords = [title]

    PAGE_PREFIX = 'https://maesetsu.jp/'
    STORY_PAGE = 'https://maesetsu.jp/story/'

    def __init__(self):
        super().__init__()
        self.init_base_folder('maesetsu')

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()
        self.download_music()
        self.download_other()

    def download_episode_preview(self):
        self.has_website_updated(self.STORY_PAGE)

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

    def download_music(self):
        folder = self.create_custom_directory('music')
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'music/')
            contents_inner = soup.find('div', id='cms_block')
            if contents_inner:
                img_tags = contents_inner.find_all('img')
                image_objs = []
                for img_tag in img_tags:
                    if img_tag.has_attr('src'):
                        image_url = self.PAGE_PREFIX + img_tag['src'].replace('../', '').split('?')[0]
                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                        image_objs.append({'name': image_name, 'url': image_url})
                self.download_image_objects(image_objs, folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Music")
            print(e)


# Mahouka Koukou no Rettousei: Raihousha-hen
class Mahouka2Download(Fall2020AnimeDownload):
    title = "Mahouka Koukou no Rettousei: Raihousha-hen"
    keywords = [title, "The Irregular at Magic High School", "2nd"]

    PAGE_PREFIX = 'https://mahouka.jp/'
    STORY_PAGE = 'https://mahouka.jp/story/'

    def __init__(self):
        super().__init__()
        self.init_base_folder('mahouka2')

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.STORY_PAGE)

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
            {'name': 'kv7', 'url': 'https://pbs.twimg.com/media/Eezxq0UUEAAj6vn?format=jpg&name=large'},
            {'name': 'kv8', 'url': 'https://pbs.twimg.com/media/EhDzQhiU4AQRDcg?format=jpg&name=medium'},
            {'name': 'kv8_1', 'url': 'https://majotabi.jp/assets/news/kv8.jpg'}
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
    STORY_PAGE = 'https://maoujo-anime.com/story/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/maoujo"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()
        self.download_music()

    def download_episode_preview(self):
        self.has_website_updated(self.STORY_PAGE)

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

    def download_music(self):
        folder = self.create_custom_directory('music')
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'music/')
            contents_inner = soup.find('div', class_='l-content_l')
            if contents_inner:
                img_tags = contents_inner.find_all('img')
                tokuten_tags = contents_inner.find_all('div', class_='c-tokuten-item__img')
                image_objs = []
                for img_tag in img_tags:
                    if img_tag.has_attr('data-src'):
                        image_url = self.PAGE_PREFIX + img_tag['data-src']
                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                        image_objs.append({'name': image_name, 'url': image_url})
                for tokuten_tag in tokuten_tags:
                    if tokuten_tag.has_attr('style'):
                        style = tokuten_tag['style']
                        if len(style) > 25 and style[0:22] == "background-image:url('" and style[-3:] == "');":
                            image_url_before = style[22:len(style) - 3]
                            if '../' in image_url_before:
                                image_url = self.PAGE_PREFIX + image_url_before.replace('../', '')
                            else:
                                image_url = self.PAGE_PREFIX + 'music/' + image_url_before
                            image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                            image_objs.append({'name': image_name, 'url': image_url})
                self.download_image_objects(image_objs, folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Music")
            print(e)


# Munou na Nana
class MunounaNanaDownload(Fall2020AnimeDownload):
    title = 'Munou na Nana'
    keywords = [title, 'Talentless Nana']

    PAGE_PREFIX = 'https://munounanana.com/'
    STORY_PAGE = 'https://munounanana.com/story/'

    def __init__(self):
        super().__init__()
        self.init_base_folder('munou-na-nana')

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.STORY_PAGE)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'kv1', 'url': 'https://munounanana.com/assets/top/main1/vis.jpg'},
            {'name': 'kv2', 'url': 'https://munounanana.com/assets/top/main2/vis.png'},
            {'name': 'kv2_1', 'url': 'https://pbs.twimg.com/media/EhTHrVKVgAA0u-d?format=jpg&name=medium'}
        ]
        self.download_image_objects(image_objs, folder)

    def download_character(self):
        folder = self.create_character_directory()
        image_objs = []
        try:
            soup = self.get_soup('https://munounanana.com/character/')
            chara_data = soup.find_all('div', class_='character-data')
            for chara in chara_data:
                img = chara.find('img')
                if img and img.has_attr('src'):
                    image_url = self.PAGE_PREFIX + img['src'].replace('../', '').split('?')[0]
                    image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                    image_objs.append({'name': image_name, 'url': image_url})
        except:
            pass
        self.download_image_objects(image_objs, folder)


# Ochikobore Fruit Tart
class OchifuruDownload(Fall2020AnimeDownload):
    title = "Ochikobore Fruit Tart"
    keywords = [title, "Dropout Idol", "Ochifuru"]

    PAGE_PREFIX = 'http://ochifuru-anime.com/'
    STORY_PAGE = 'http://ochifuru-anime.com/story.html'
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
        self.download_music()

    def download_episode_preview(self):
        self.download_episode_preview_guess()
        soup = self.get_soup(self.STORY_PAGE)
        try:
            ol_list = soup.find('ol', class_='story_menu2')
            if ol_list:
                lis = ol_list.find_all('li')
                for li in lis:
                    a_tag = li.find('a')
                    if a_tag and a_tag.has_attr('href'):
                        split1 = a_tag['href'].split('?cat=story')
                        if len(split1) == 2:
                            try:
                                episode = str(int(split1[1])).zfill(2)
                                if not self.is_image_exists(episode + '_1'):
                                    episode_url = self.PAGE_PREFIX + a_tag['href']
                                    episode_soup = self.get_soup(episode_url)
                                    image_ul = episode_soup.find('ul', class_='slider')
                                    if image_ul:
                                        image_lis = image_ul.find_all('li')
                                        image_objs = []
                                        for i in range(len(image_lis)):
                                            img_tag = image_lis[i].find('img')
                                            if img_tag and img_tag.has_attr('data-lazy'):
                                                image_name = episode + '_' + str(i + 1)
                                                image_url = self.PAGE_PREFIX + img_tag['data-lazy']
                                                image_objs.append({'name': image_name, 'url': image_url})
                                        self.download_image_objects(image_objs, self.base_folder)
                            except:
                                continue
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_episode_preview_guess(self):
        story_template = 'http://ochifuru-anime.com/images/story/%s/p_%s.jpg'
        for i in range(13):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            for j in range(5):
                img_num = str(j + 1)
                image_url = story_template % (str(i + 1).zfill(3), str(j + 1).zfill(3))
                image_name = episode + '_' + img_num
                result = self.download_image(image_url, self.base_folder + '/' + image_name)
                if result == -1:
                    return

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

    def download_music(self):
        folder = self.create_custom_directory('music')
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'music.html')
            contents_inner = soup.find('div', class_='music_wrap')
            if contents_inner:
                img_tags = contents_inner.find_all('img')
                image_objs = []
                for img_tag in img_tags:
                    if img_tag.has_attr('src'):
                        image_url = self.PAGE_PREFIX + img_tag['src'].replace('../', '')
                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                        image_objs.append({'name': image_name, 'url': image_url})
                self.download_image_objects(image_objs, folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Music")
            print(e)


# One Room 3rd Season
class OneRoom3Download(Fall2020AnimeDownload):
    title = "One Room 3rd Season"
    keywords = [title, "Third"]

    PAGE_PREFIX = "https://oneroom-anime.com/"

    def __init__(self):
        super().__init__()
        self.init_base_folder('one-room3')

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_bluray()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'kv', 'url': 'https://pbs.twimg.com/media/Eg9v7u7VgAAhwPr?format=jpg&name=4096x4096'}]
        self.download_image_objects(image_objs, folder)

    def download_bluray(self):
        folder = self.create_bluray_directory()
        image_objs = [
            {'name': 'bd_s1s2_1', 'url': 'https://oneroom-anime.com/wordpress/wp-content/uploads/2020/07/237a13f0134854b4d0b8162879eafef1.jpg'},
            {'name': 'bd_s1s2_2', 'url': 'https://oneroom-anime.com/wordpress/wp-content/uploads/2020/07/5cc4ed2d63953152405ca92e5549c420.jpg'}
        ]
        self.download_image_objects(image_objs, folder)


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
    STORY_PAGE = 'https://sigururi.com/intro/'

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
        self.has_website_updated(self.STORY_PAGE)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [{'name': 'kv_01_pc', 'url': 'https://sigururi.com/assets/img/top/kv_01_pc.jpg'},
                      {'name': 'kv_01_sp', 'url': 'https://sigururi.com/assets/img/top/kv_01_sp.jpg'},
                      {'name': 'kv_02_pc', 'url': 'https://sigururi.com/assets/img/top/kv_02_pc.jpg'},
                      {'name': 'kv_02_sp', 'url': 'https://sigururi.com/assets/img/top/kv_02_sp.jpg'},
                      {'name': 'kv_03_pc', 'url': 'https://sigururi.com/assets/img/top/kv_03_pc.jpg'},
                      {'name': 'kv_03_sp', 'url': 'https://sigururi.com/assets/img/top/kv_03_sp.jpg'},
                      {'name': 'kv_04_pc', 'url': 'https://sigururi.com/assets/img/top/kv_04_pc.jpg'},
                      {'name': 'kv_04_sp', 'url': 'https://sigururi.com/assets/img/top/kv_04_sp.jpg'}]
        self.download_image_objects(image_objs, folder)

    def download_character(self):
        folder = self.create_character_directory()
        image_url_templates = ['https://sigururi.com/assets/img/chara/chara_%s.png',
                               'https://sigururi.com/assets/img/character/chara_%s.png',
                               'https://sigururi.com/assets/img/character/chara_%s_new.png']
        soup = self.get_soup('https://sigururi.com/chara/')
        num_of_chara = len(soup.find_all('div', class_='chara_wrap'))
        chara_id_to_download = []
        for i in range(num_of_chara):
            if self.is_image_exists('chara_%s' % str(i + 1).zfill(2), folder)\
                    or self.is_image_exists('chara_%s_new' % str(i + 1).zfill(2), folder):
                continue
            chara_id_to_download.append(i + 1)

        for image_url_template in image_url_templates:
            for i in chara_id_to_download:
                image_url = image_url_template % str(i).zfill(2)
                image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                image_name_with_extension = self.extract_image_name_from_url(image_url, with_extension=True)
                filepath_without_extension = folder + '/' + image_name
                filepath = folder + '/' + image_name_with_extension
                if os.path.exists(filepath):
                    continue
                self.download_image(image_url, filepath_without_extension)

    def download_other(self):
        folder = self.create_custom_directory('other')
        image_objs = [
            {'name': 'news_vol_01', 'url': 'https://pbs.twimg.com/media/EdnNj1qVoAEY4MX?format=jpg&name=4096x4096'},
            {'name': 'news_vol_02', 'url': 'https://pbs.twimg.com/media/EeYvh7oUYAAdeWc?format=jpg&name=4096x4096'},
            {'name': 'news_vol_03', 'url': 'https://pbs.twimg.com/media/EhM2-ZbVoAA9hIY?format=jpg&name=4096x4096'},
            {'name': 'uminohi', 'url': 'https://sigururi.com/SYS/CONTENTS/2020072310293692693264/w708'},
            {'name': 'zanshomimai', 'url': 'https://sigururi.com/news/SYS/CONTENTS/2020083114133842932562/w712'},
            {'name': 'soranohi', 'url': 'https://pbs.twimg.com/media/EiSXMZrU8AA4ThC?format=jpg&name=medium'},
            {'name': 'img_miyako', 'url': 'https://sigururi.com/assets/img/special/interview/img_miyako.jpg'},
            {'name': 'img_azuzu', 'url': 'https://sigururi.com/assets/img/special/interview/img_azuzu.jpg'},
            {'name': 'img_sonoka', 'url': 'https://sigururi.com/assets/img/special/interview/img_sonoka.jpg'},
        ]
        self.download_image_objects(image_objs, folder)


# Tonikaku Kawaii
class TonikawaDownload(Fall2020AnimeDownload):
    title = "Tonikaku Kawaii"
    keywords = [title, "Tonikawa", "Cawaii", "Fly Me to the Moon"]

    PAGE_PREFIX = 'http://tonikawa.com/'
    STORY_PAGE = 'http://tonikawa.com/story/'

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/tonikawa"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.STORY_PAGE)

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

