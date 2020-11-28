import os
import requests
import anime.constants as constants
from anime.main_download import MainDownload
from datetime import datetime
from scan import AniverseMagazineScanner, MocaNewsScanner, WebNewtypeScanner
from PIL import Image

# 100-man no Inochi no Ue ni Ore wa Tatteiru http://1000000-lives.com/ #俺100 @1000000_lives [TUE]
# Adachi to Shimamura https://www.tbs.co.jp/anime/adashima/ #安達としまむら @adashima_staff [TUE]
# Assault Lily: Bouquet https://anime.assaultlily-pj.com/ #アサルトリリィ @assaultlily_pj [FRI]
# Danmachi III http://danmachi.com/danmachi3/ #danmachi @danmachi_anime [SAT]
# Dogeza de Tanondemita https://dogeza-anime.com/ #土下座で @dgz_anime [WED]
# Gochuumon wa Usagi desu ka? Bloom https://gochiusa.com/bloom/ #gochiusa @usagi_anime [FRI]
# Golden Kamuy 3rd Season https://www.kamuy-anime.com/ #ゴールデンカムイ @kamuy_official [MON]
# Higurashi no Naku Koro ni Gou https://higurashianime.com/ #ひぐらし @higu_anime [MON]
# Iwa Kakeru!: Sport Climbing Girls http://iwakakeru-anime.com/ #いわかける #iwakakeru @iwakakeru_anime [THU]
# Jujutsu Kaisen https://jujutsukaisen.jp/ #呪術廻戦 @animejujutsu [MON]
# Kamisama ni Natta Hi https://kamisama-day.jp/ #神様になった日 @kamisama_Ch_AB [SAT/SUN]
# Kami-tachi ni Hirowareta Otoko https://kamihiro-anime.com/ #神達に拾われた男 @kamihiro_anime [FRI]
# Kimi to Boku no Saigo no Senjou, Aruiwa Sekai ga Hajimaru Seisen https://kimisentv.com/ #キミ戦 #kimisen @kimisen_project [THU]
# Kuma Kuma Kuma Bear https://kumakumakumabear.com/ #くまクマ熊ベアー #kumabear @kumabear_anime [TUE]
# Maesetsu https://maesetsu.jp/ #まえせつ @maesetsu_anime [WED]
# Mahouka Koukou no Rettousei: Raihousha-hen https://mahouka.jp/ #mahouka @mahouka_anime [FRI]
# Majo no Tabitabi https://majotabi.jp/ #魔女の旅々 #魔女の旅々はいいぞ #majotabi @majotabi_PR [MON]
# Maoujou de Oyasumi https://maoujo-anime.com/ #魔王城でおやすみ @maoujo_anime [FRI]
# Munou na Nana https://munounanana.com/ #無能なナナ @munounanana [WED]
# Ochikobore Fruit Tart http://ochifuru-anime.com/ #ochifuru @ochifuru_anime
# One Room S3 https://oneroom-anime.com/ #OneRoom @anime_one_room
# Rail Romanesque https://railromanesque.jp/ @rail_romanesque #まいてつ #レヱルロマネスク
# Senyoku no Sigrdrifa https://sigururi.com/ #シグルリ @sigururi [WED]
# Strike Witches: Road to Berlin http://w-witch.jp/strike_witches-rtb/ #w_witch #s_witch_rtb @RtbWitch [THU]
# Tonikaku Kawaii http://tonikawa.com/ #トニカクカワイイ #tonikawa @tonikawa_anime [FRI]


# Fall 2020 Anime
class Fall2020AnimeDownload(MainDownload):
    season = "2020-4"
    season_name = "Fall 2020"
    folder_name = '2020-4'

    def __init__(self):
        super().__init__()


# 100-man no Inochi no Ue ni Ore wa Tatteiru
class HyakumanNoInochiDownload(Fall2020AnimeDownload):
    title = "100-man no Inochi no Ue ni Ore wa Tatteiru"
    keywords = [title, "I'm standing on 1,000,000 lives.", "Hyakuman", "1000000"]
    folder_name = '100-man-no-inochi'

    PAGE_PREFIX = 'http://1000000-lives.com'
    STORY_PAGE = 'http://1000000-lives.com/story/'
    LAST_EPISODE = 12

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_guess()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.STORY_PAGE)
            story_list = soup.find('ul', class_='l_storylist')
            if story_list:
                stories = story_list.find_all('li')
                for story in stories:
                    a_tag = story.find('a')
                    if a_tag and a_tag.has_attr('href'):
                        try:
                            episode = str(int(a_tag['href'].replace('story', '').replace('/', ''))).zfill(2)
                        except:
                            continue
                        if self.is_image_exists(episode + '_1'):
                            continue
                        story_url = self.PAGE_PREFIX + a_tag['href']
                        story_soup = self.get_soup(story_url)
                        thumblist = story_soup.find('ul', class_='l_thumblist')
                        if thumblist:
                            lis = thumblist.find_all('li')
                            image_objs = []
                            for i in range(len(lis)):
                                a_tag = lis[i].find('a')
                                if a_tag and a_tag.has_attr('data-imgload'):
                                    image_url = self.PAGE_PREFIX + a_tag['data-imgload']
                                    image_name = episode + '_' + str(i + 1)
                                    image_objs.append({'name': image_name, 'url': image_url})
                            self.download_image_objects(image_objs, self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_episode_preview_guess(self):
        if self.is_image_exists(str(self.LAST_EPISODE) + '_1'):
            return

        image_url_template = 'http://1000000-lives.com/img/story/img_story%s.jpg'
        for i in range(self.LAST_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            for j in range(1, 7, 1):
                num = i * 6 + j
                image_name = episode + '_' + str(j)
                image_url = image_url_template % str(num).zfill(2)
                result = self.download_image(image_url, self.base_folder + '/' + image_name)
                if result == -1:
                    return

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'kv', 'url': 'https://pbs.twimg.com/media/ESLrKCWUcAExG_i?format=jpg&name=4096x4096'},
            {'name': 'kv2', 'url': 'https://pbs.twimg.com/media/Ee03f7CU8AUtfE5?format=png&name=large'}]
        self.download_image_objects(image_objs, folder)

    def download_character(self):
        folder = self.create_character_directory()
        image_objs = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX + '/character/')
            images = soup.find_all('div', class_='charadata_body_img')
            for image in images:
                if image.has_attr('data-imgload'):
                    image_url = self.PAGE_PREFIX + image['data-imgload']
                    image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                    image_objs.append({'name': image_name, 'url': image_url})
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)
        self.download_image_objects(image_objs, folder)


# Adachi to Shimamura
class AdashimaDownload(Fall2020AnimeDownload):
    title = 'Adachi to Shimamura'
    keywords = [title, 'Adashima']
    folder_name = 'adashima'

    PAGE_PREFIX = 'https://www.tbs.co.jp/anime/adashima/'
    STORY_PAGE = 'https://www.tbs.co.jp/anime/adashima/story/'
    LAST_EPISODE = 12

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()
        self.download_bluray()

    def download_episode_preview(self):
        if self.is_image_exists(str(self.LAST_EPISODE) + '_1'):
            return

        image_url_template = 'https://www.tbs.co.jp/anime/adashima/story/img/story%s/%s.jpg'
        for i in range(1, self.LAST_EPISODE + 1, 1):
            for j in range(1, 4, 1):
                image_name = str(i).zfill(2) + '_' + str(j)
                if self.is_image_exists(image_name):
                    continue
                image_url = image_url_template % (str(i).zfill(2), str(j).zfill(2))
                result = self.download_image(image_url, self.base_folder + '/' + image_name)
                if result == -1:
                    return

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
            {'name': 'music_ed', 'url': 'https://pbs.twimg.com/media/Elao8sOU0AA1nzm?format=jpg&name=medium'},
            {'name': 'bd_vol_1', 'url': 'https://pbs.twimg.com/media/ElfsmoIUYAECjjH?format=jpg&name=4096x4096'},
            {'name': 'bd_bonus_1', 'url': 'https://pbs.twimg.com/media/ElftV_5UcAAVxFC?format=jpg&name=medium'},
            {'name': 'bd_bonus_2', 'url': 'https://pbs.twimg.com/media/ElftthlVgAA3ejg?format=jpg&name=medium'},
            {'name': 'bd_bonus_3', 'url': 'https://pbs.twimg.com/media/Elft8pYVkAAYRIo?format=jpg&name=medium'},
        ]
        self.download_image_objects(image_objs, folder)

        bd_prefix = 'https://www.tbs.co.jp/anime/adashima/disc/'

        # Blu-Ray Bonus
        try:
            soup = self.get_soup('https://www.tbs.co.jp/anime/adashima/disc/store.html')
            table = soup.find('table', class_='oritoku-table')
            tds = table.find_all('td', class_='td-img')
            for td in tds:
                a_tag = td.find('a')
                if a_tag and a_tag.has_attr('data-image'):
                    image_url = bd_prefix + a_tag['data-image']
                    image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Blu-Ray Bonus')
            print(e)

        # Blu-Ray
        try:
            for i in range(4):
                volume = str(i + 1)
                if self.is_image_exists('bd_' + volume, folder):
                    continue
                bd_url = 'https://www.tbs.co.jp/anime/adashima/disc/disc0%s.html' % volume
                soup = self.get_soup(bd_url)
                div = soup.find('div', class_='disc-img')
                if div:
                    image = div.find('img')
                    if image and image.has_attr('src'):
                        image_url = bd_prefix + image['src']
                        if self.is_matching_content_length(image_url, 25371):
                            break
                        image_name = 'bd_' + volume
                        self.add_to_image_list(image_name, image_url)
                        self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Blu-Ray')
            print(e)


# Assault Lily: Bouquet
class AssaultLilyDownload(Fall2020AnimeDownload):
    title = 'Assault Lily: Bouquet'
    keywords = [title]
    folder_name = 'assault-lily'

    PAGE_PREFIX = 'https://anime.assaultlily-pj.com/'
    STORY_PAGE = 'https://anime.assaultlily-pj.com/story/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_key_visual()
        self.download_character()
        self.download_bluray()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'introduction/')
            story_list = soup.find('ul', id='story-List')
            if story_list:
                a_tags = story_list.find_all('a')
                for a_tag in a_tags:
                    if a_tag.has_attr('href') and self.STORY_PAGE in a_tag['href']:
                        try:
                            episode = str(int(a_tag.text.split('第')[1].split('話')[0])).zfill(2)
                        except:
                            continue
                        if self.is_image_exists(episode + '_1'):
                            continue
                        story_soup = self.get_soup(a_tag['href'])
                        uls = story_soup.find('ul', class_='story-Detail_List')
                        if uls:
                            images = uls.find_all('img')
                            image_objs = []
                            for i in range(len(images)):
                                if images[i].has_attr('src'):
                                    image_url = images[i]['src']
                                    image_name = episode + '_' + str(i + 1)
                                    image_objs.append({'name': image_name, 'url': image_url})
                            self.download_image_objects(image_objs, self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_episode_preview_external(self):
        jp_title = 'アサルトリリィ'
        AniverseMagazineScanner(jp_title, self.base_folder, 12).run()

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'teaser', 'url': 'https://anime.assaultlily-pj.com/wordpress/wp-content/themes/anime_al_v1/assets/images/common/story/img_intro.jpg'},
            {'name': 'kv1', 'url': 'https://anime.assaultlily-pj.com/wordpress/wp-content/themes/anime_al_v1/assets/images/pc/index/kv_1.jpg'}]
        self.download_image_objects(image_objs, folder)

    def download_character(self):
        folder = self.create_character_directory()
        image_objs = []
        try:
            soup = self.get_soup('https://anime.assaultlily-pj.com/character/')
            cat_items = soup.find_all('li', class_='chara_Cat_Item')
            if len(cat_items) > 1:
                for i in range(len(cat_items)):
                    list_items = cat_items[i].find_all('li', class_='chara_List_Item')
                    for list_item in list_items:
                        img_tag = list_item.find('img')
                        if img_tag and img_tag.has_attr('src'):
                            image_url = img_tag['src']
                            if i == 0:
                                image_url = image_url.replace('chara_', 'body_')
                            image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                            image_objs.append({'name': image_name, 'url': image_url})
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)
        self.download_image_objects(image_objs, folder)

    def download_bluray(self):
        folder = self.create_bluray_directory()
        image_objs = []
        try:
            soup = self.get_soup('https://anime.assaultlily-pj.com/cd_blu-ray/')
            list_items = soup.find_all('li', class_='cdbd_List_Item')
            for list_item in list_items:
                img_tags = list_item.find_all('img')
                for img_tag in img_tags:
                    if img_tag.has_attr('src'):
                        image_url = img_tag['src']
                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                        image_objs.append({'name': image_name, 'url': image_url})
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Blu-Ray')
            print(e)
        self.download_image_objects(image_objs, folder)


# Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka III
class Danmachi3Download(Fall2020AnimeDownload):
    title = 'Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka III'
    keywords = [title, 'Danmachi', 'Is It Wrong to Try to Pick Up Girls in a Dungeon? III', '3rd']
    folder_name = 'danmachi3'

    PAGE_PREFIX = 'http://danmachi.com/danmachi3/'
    STORY_PAGE = 'http://danmachi.com/danmachi3/story/index.html'
    LAST_EPISODE = 12
    NUM_OF_IMAGE_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.generate_combined_episode_preview_image()
        self.download_key_visual()

    def download_episode_preview(self):
        if self.is_image_exists(str(self.LAST_EPISODE) + '_1'):
            return

        image_url_template = 'http://danmachi.com/danmachi3/story/images/story%s-%s.jpg'
        for i in range(1, self.LAST_EPISODE + 1, 1):
            for j in range(1, self.NUM_OF_IMAGE_PER_EPISODE + 1, 1):
                image_name = str(i).zfill(2) + '_' + str(j)
                if self.is_image_exists(image_name):
                    continue
                image_url = image_url_template % (str(i), str(j))
                result = self.download_image(image_url, self.base_folder + '/' + image_name)
                if result == -1:
                    return

    def generate_combined_episode_preview_image(self):
        for i in range(1, self.LAST_EPISODE + 1, 1):
            combined_image_name = str(i).zfill(2) + '_0'
            if self.is_image_exists(combined_image_name):
                continue
            image_filepaths = []
            for j in range(1, self.NUM_OF_IMAGE_PER_EPISODE + 1, 1):
                image_name = str(i).zfill(2) + '_' + str(j)
                if self.is_image_exists(image_name):
                    image_filepaths.append(self.base_folder + '/' + image_name + '.jpg')
            if len(image_filepaths) == 6:
                images = [Image.open(x) for x in image_filepaths]
                width, height = images[0].size
                new_image = Image.new('RGB', (width * 3, height * 2))
                for row in range(2):
                    for col in range(3):
                        index = row * 3 + col
                        new_image.paste(images[index], (width * col, height * row))
                new_image.save(self.base_folder + '/' + combined_image_name + '.jpg', subsampling=0, quality=100)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'teaser', 'url': 'https://pbs.twimg.com/media/ETtwMdUUMAAdqd1?format=jpg&name=4096x4096'},
            {'name': 'kv1', 'url': 'https://pbs.twimg.com/media/EcCRpVLUcAAdpGv?format=jpg&name=900x900'}
        ]
        self.download_image_objects(image_objs, folder)


# Dogeza de Tanondemita
class DogezaDeTanondemitaDownload(Fall2020AnimeDownload):
    title = 'Dogeza de Tanondemita'
    keywords = [title]
    folder_name = 'dogeza'

    PAGE_PREFIX = 'https://dogeza-anime.com/'
    LAST_EPISODE = 13

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()
        self.download_bluray()

    def download_episode_preview(self):
        story_template = 'https://dogeza-anime.com/assets/story/%s_%s.jpg'
        for i in range(self.LAST_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            for j in range(3):
                img_num = str(j + 1)
                image_url = story_template % (str(i + 1), str(j + 1))
                image_name = episode + '_' + img_num
                result = self.download_image(image_url, self.base_folder + '/' + image_name)
                if result == -1:
                    return

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'vist1', 'url': 'https://dogeza-anime.com/assets/news/vist1.jpg'},
            {'name': 'visk1', 'url': 'https://dogeza-anime.com/assets/news/visk1.jpg'},
            {'name': 'vis', 'url': 'https://dogeza-anime.com/assets/top/main-k1/vis.jpg'},
            {'name': 'visk2', 'url': 'https://dogeza-anime.com/assets/news/visk2.jpg'},
            {'name': 'vis2', 'url': 'https://dogeza-anime.com/assets/top/main-k2/vis.jpg'},
            #{'name': 'vis2', 'url': 'https://pbs.twimg.com/media/Emik0XfU4AEcfIz?format=jpg&name=4096x4096'}
        ]
        self.download_image_objects(image_objs, folder)

    def download_character(self):
        folder = self.create_character_directory()
        for i in range(1, 31, 1):
            image_url = 'https://dogeza-anime.com/assets/character/c%s.png' % str(i)
            image_name = 'c' + str(i)
            if self.is_image_exists(image_name, folder):
                continue
            result = self.download_image(image_url, folder + '/' + image_name)
            if result == -1:
                break

    def download_bluray(self):
        folder = self.create_bluray_directory()
        image_objs = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            content = soup.find('div', id='PackageCont')
            if content:
                images = content.find_all('img')
                for image in images:
                    if image.has_attr('src'):
                        image_url = self.PAGE_PREFIX + image['src'].replace('./', '')
                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                        image_objs.append({'name': image_name, 'url': image_url})
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)
        self.download_image_objects(image_objs, folder)


# Gochuumon wa Usagi Desu ka? Bloom
class GochiUsa3Download(Fall2020AnimeDownload):
    title = "Gochuumon wa Usagi Desu ka? Bloom"
    keywords = [title, 'Gochiusa', '3rd']
    folder_name = 'gochiusa3'

    PAGE_PREFIX = 'https://gochiusa.com/bloom/'
    STORY_PAGE = 'https://gochiusa.com/bloom/story/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_guess()
        self.download_key_visual()
        self.download_bluray()
        self.download_bluray_bonus()
        self.download_music()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.STORY_PAGE, decode=True)
            div_contents = soup.find('div', id='ContentsListUnit01')
            if div_contents:
                a_tags = div_contents.find_all('a')
                for a_tag in a_tags:
                    if a_tag.has_attr('href'):
                        a_tag_text = a_tag.text.strip()
                        if len(a_tag_text) > 2 and '第' in a_tag_text[0] and '羽' in a_tag_text[-1]:
                            try:
                                episode = str(int(a_tag_text.split('第')[1].split('羽')[0])).zfill(2)
                            except:
                                continue
                            if self.is_image_exists(episode + '_1'):
                                continue
                            ep_url = self.PAGE_PREFIX + a_tag['href'].replace('../', '')
                            ep_soup = self.get_soup(ep_url)
                            ph_divs = ep_soup.find_all('div', class_='ph')
                            image_objs = []
                            for i in range(len(ph_divs)):
                                image = ph_divs[i].find('a')
                                if image and image.has_attr('href'):
                                    image_url = self.PAGE_PREFIX + image['href'].replace('../', '').split('?')[0]
                                    image_name = episode + '_' + str(i + 1)
                                    image_objs.append({'name': image_name, 'url': image_url})
                            self.download_image_objects(image_objs, self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_episode_preview_guess(self):
        # Episode 5-1 https://gochiusa.com/bloom/core_sys/images/contents/00000019/block/00000096/00000080.jpg
        # Episode 5-6 https://gochiusa.com/bloom/core_sys/images/contents/00000019/block/00000096/00000085.jpg
        folder = self.create_custom_directory('guess')
        url_base = 'https://gochiusa.com/bloom/core_sys/images/contents/%s/block/%s/%s.jpg'
        contents_base = 19
        block_base = 96
        num_base = 80
        for i in range(8):
            episode = str(i + 5).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            contents = contents_base + i
            block = block_base + i * 4
            for j in range(6):
                num = num_base + j + i * 6
                image_url = url_base % (str(contents).zfill(8), str(block).zfill(8), str(num).zfill(8))
                image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                if self.is_image_exists(image_name, folder):
                    continue
                result = self.download_image(image_url, folder + '/' + image_name)
                if result == -1:
                    return
                else:
                    print(self.__class__.__name__ + ' - Guessed successfully!')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'original_kv', 'url': 'https://gochiusa.com/bloom/core_sys/images/main/home/main_img.jpg'},
            {'name': 'kv', 'url': 'https://pbs.twimg.com/media/EdIvRRNUEAI7tTZ?format=jpg&name=medium'}
        ]
        self.download_image_objects(image_objs, folder)

    def download_bluray(self):
        folder = self.create_bluray_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bddvd/', decode=True)
            boxes = soup.find_all('div', class_='nwu_box')
            for box in boxes:
                img_tag = box.find('img')
                if img_tag and img_tag.has_attr('src'):
                    img_url = self.PAGE_PREFIX + img_tag['src'].replace('../', '')
                    content_length = requests.head(img_url).headers['Content-Length']
                    if content_length == '269101':  # Skip Now Printing
                        continue
                    title = box.find('div', class_='title')
                    if title:
                        a_tag = title.find('a')
                        if a_tag and a_tag.has_attr('href'):
                            a_tag_text = a_tag.text.strip()
                            if len(a_tag_text) > 2 and a_tag_text[-3] == '第' and a_tag_text[-1] == '巻':
                                try:
                                    bd_num = str(int(a_tag_text[-2]))
                                except:
                                    continue
                                if self.is_image_exists('bd' + bd_num, folder):
                                    continue
                                bd_soup = self.get_soup(self.PAGE_PREFIX + a_tag['href'].replace('../', ''))
                                phs = bd_soup.find_all('div', class_='ph')
                                image_objs = []
                                for i in range(len(phs)):
                                    image = phs[i].find('img')
                                    if image and image.has_attr('src'):
                                        image_url = self.PAGE_PREFIX + \
                                                    image['src'].replace('../', '').replace('/sn_', '/').split('?')[0]
                                        cont_length = requests.head(image_url).headers['Content-Length']
                                        if cont_length == '127825':  # Skip Now Printing
                                            continue
                                        if i == 0:
                                            image_name = 'bd' + bd_num
                                        else:
                                            image_name = 'bd' + bd_num + '_' + str(i)
                                        image_objs.append({'name': image_name, 'url': image_url})
                                self.download_image_objects(image_objs, folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Blu-Ray')
            print(e)

    def download_bluray_bonus(self):
        folder = self.create_bluray_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bddvd/tokuten.html')
            phs = soup.find_all('div', class_='ph')
            image_objs = []
            for ph in phs:
                image = ph.find('img')
                if image and image.has_attr('src'):
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '').replace('/sn_', '/').split('?')[0]
                    cont_length = requests.head(image_url).headers['Content-Length']
                    if cont_length == '127825':  # Skip Now Printing
                        continue
                    image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                    image_objs.append({'name': image_name, 'url': image_url})
            self.download_image_objects(image_objs, folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Blu-Ray Bonus')
            print(e)

    def download_music(self):
        folder = self.create_custom_directory('music')
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'cd/list00000000.html')
            boxes = soup.find_all('div', class_='nwu_box')
            visited_url = []
            for box in boxes:
                img_tag = box.find('img')
                if img_tag and img_tag.has_attr('src'):
                    img_url = self.PAGE_PREFIX + img_tag['src'].replace('../', '')
                    content_length = requests.head(img_url).headers['Content-Length']
                    if content_length == '59689':  # Skip Now Printing
                        continue
                    title = box.find('div', class_='title')
                    if title:
                        a_tag = title.find('a')
                        if a_tag and a_tag.has_attr('href'):
                            music_url = self.PAGE_PREFIX + a_tag['href'].replace('../', '').split('#')[0]
                            if music_url in visited_url:
                                continue
                            visited_url.append(music_url)
                            music_soup = self.get_soup(music_url)
                            phs = music_soup.find_all('div', class_='ph')
                            image_objs = []
                            for ph in phs:
                                image = ph.find('img')
                                if image and image.has_attr('src'):
                                    image_url = self.PAGE_PREFIX + \
                                                image['src'].replace('../', '').replace('/sn_', '/').split('?')[0]
                                    cont_length = requests.head(image_url).headers['Content-Length']
                                    if cont_length == '111405':  # Skip Now Printing
                                        continue
                                    image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                                    image_objs.append({'name': image_name, 'url': image_url})
                            self.download_image_objects(image_objs, folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Blu-Ray')
            print(e)


# Golden Kamuy 3rd Season
class GoldenKamuy3Download(Fall2020AnimeDownload):
    title = "Golden Kamuy 3rd Season"
    keywords = [title, "Kamui"]
    folder_name = 'golden-kamuy3'

    PAGE_URL = "https://kamuy-anime.com/story/%s.html"
    PAGE_PREFIX = "https://kamuy-anime.com/"
    FIRST_EPISODE = 25
    FINAL_EPISODE = 36

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_guess()
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

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        url_base = 'https://kamuy-anime.com/core_sys/images/contents/%s/block/%s/%s.jpg'
        first_episode = 26
        contents_base = 233
        block_base = 788
        num_base = 706
        invalid_length = [54936, 45206, 42226, 46380, 48763, 51224, 32391, 44256]
        for i in range(13):
            episode = str(i + first_episode).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            contents = contents_base + i
            block = block_base + i * 5
            for j in range(8):
                num = num_base + j + i * 8
                image_url = url_base % (str(contents).zfill(8), str(block).zfill(8), str(num).zfill(8))
                image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                if self.is_matching_content_length(image_url, invalid_length[j]):
                    continue
                if self.is_image_exists(image_name, folder):
                    continue
                result = self.download_image(image_url, folder + '/' + image_name)
                if result == -1:
                    return
                else:
                    print(self.__class__.__name__ + ' - Guessed successfully!')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'kv1', 'url': 'https://pbs.twimg.com/media/Ea1xVSTUEAA1G7y?format=jpg&name=large'},
            {'name': 'kv2', 'url': 'https://pbs.twimg.com/media/Eh2IA2VUMAAdhyT?format=jpg&name=large'},
            {'name': 'kv3', 'url': 'https://pbs.twimg.com/media/Eh2IDQdVgAM9bfy?format=jpg&name=large'},
        ]
        self.download_image_objects(image_objs, folder)


# Higurashi no Naku Koro ni Gou
class Higurashi2020Download(Fall2020AnimeDownload):
    title = "Higurashi no Naku Koro ni Gou"
    keywords = [title, "When They Cry", "2020"]
    folder_name = 'higurashi2020'

    PAGE_PREFIX = 'https://higurashianime.com/'
    STORY_PAGE = 'https://higurashianime.com/intro.html'
    LAST_EPISODE = 25

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()
        self.download_bluray()

    def download_episode_preview(self):
        if self.is_image_exists(str(self.LAST_EPISODE) + '_1'):
            return

        image_url_template = 'https://higurashianime.com/images/story/%s/p_%s.jpg'
        for i in range(1, self.LAST_EPISODE + 1, 1):
            for j in range(1, 7, 1):
                image_name = str(i).zfill(2) + '_' + str(j)
                if self.is_image_exists(image_name):
                    continue
                image_url = image_url_template % (str(i).zfill(3), str(j).zfill(3))
                result = self.download_image(image_url, self.base_folder + '/' + image_name)
                if result == -1:
                    return

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
    folder_name = 'iwakakeru'

    PAGE_PREFIX = 'http://iwakakeru-anime.com/'
    STORY_PAGE = 'http://iwakakeru-anime.com/story/'
    LAST_EPISODE = 12

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()
        self.download_bluray()

    def download_episode_preview(self):
        story_template = self.PAGE_PREFIX + 'img/story/ep%s/img%s.jpg'
        for i in range(self.LAST_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            for j in range(4):
                img_num = str(j + 1)
                image_url = story_template % (episode, str(j + 1).zfill(2))
                image_name = episode + '_' + img_num
                result = self.download_image(image_url, self.base_folder + '/' + image_name)
                if result == -1:
                    return

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

    def download_bluray(self):
        folder = self.create_bluray_directory()
        music_url = self.PAGE_PREFIX + 'news/wp/wp-content/uploads/2020/10/%s.jpg'
        image_objs = [
            {'name': 'music_op', 'url': music_url % 'アニメ盤_LACM-24064'},
            {'name': 'music_ed', 'url': music_url % 'h1_lacm24067'},
        ]
        self.download_image_objects(image_objs, folder)

        cache_filepath = folder + '/' + 'cache'
        processed = []
        num_processed = 0
        if os.path.exists(cache_filepath):
            with open(cache_filepath, 'r') as f:
                inputs = f.read()
            processed = inputs.split(';')
            num_processed = len(processed)
        try:
            product_url = 'http://iwakakeru-anime.com/products/'
            soup = self.get_soup('http://iwakakeru-anime.com/products/')
            box_div = soup.find('div', class_='box')
            if box_div:
                lis = box_div.find_all('li')
                for li in lis:
                    image = li.find('img')
                    if image and image.has_attr('src'):
                        f_image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                        content_length = requests.head(f_image_url).headers['Content-Length']
                        if content_length == '15283' or content_length == '3379':  # Skip Now Printing
                            continue
                        a_tag = li.find('a')
                        if a_tag and a_tag.has_attr('href') and 'id=' in a_tag['href']:
                            a_tag_id = a_tag['href'].split('id=')[1]
                            if a_tag_id in processed:
                                continue
                            bd_url = product_url + a_tag['href']
                            bd_soup = self.get_soup(bd_url)
                            if bd_soup:
                                bd_box_div = bd_soup.find('div', class_='box')
                                if bd_box_div:
                                    images = bd_box_div.find_all('img')
                                    image_objs = []
                                    for image in images:
                                        if image.has_attr('src'):
                                            image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                                            image_name = self.extract_image_name_from_url(image_url,
                                                                                          with_extension=False)
                                            # if self.is_image_exists(image_name, folder):
                                            #     continue
                                            bd_content_length = requests.head(image_url).headers['Content-Length']
                                            if bd_content_length == '15283' or bd_content_length == '3379':
                                                continue
                                            image_objs.append({'name': image_name, 'url': image_url})
                                    success = self.download_image_objects(image_objs, folder)
                                    if success and len(images) == len(image_objs):
                                        processed.append(a_tag_id)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Blu-Ray")
            print(e)

        if len(processed) > num_processed:
            with open(cache_filepath, 'w+') as f:
                for i in range(len(processed)):
                    if i > 0:
                        f.write(';')
                    f.write(processed[i])


# Jujutsu Kaisen
class JujutsuKaisenDownload(Fall2020AnimeDownload):
    title = 'Jujutsu Kaisen'
    keywords = [title]
    folder_name = 'jujutsu-kaisen'

    PAGE_PREFIX = 'https://jujutsukaisen.jp/'
    STORY_PAGE = 'https://jujutsukaisen.jp/episodes/'
    LAST_EPISODE = 12

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_guess()
        self.download_key_visual()

    def download_episode_preview(self):
        if self.is_image_exists(str(self.LAST_EPISODE) + '_01'):
            return

        try:
            soup = self.get_soup(self.STORY_PAGE)
            ul = soup.find('ul', class_='normalList')
            if ul:
                a_tags = ul.find_all('a')
                for a_tag in a_tags:
                    if a_tag.has_attr('href'):
                        try:
                            episode = str(int(a_tag['href'].split('.php')[0])).zfill(2)
                        except:
                            continue
                        if self.is_image_exists(episode + '_01'):
                            continue
                        story_url = self.STORY_PAGE + a_tag['href']
                        story_soup = self.get_soup(story_url)
                        image_ul = story_soup.find('ul', class_='imgClick')
                        images = image_ul.find_all('img')
                        image_objs = []
                        for i in range(len(images)):
                            if images[i].has_attr('src'):
                                image_url = self.PAGE_PREFIX + images[i]['src'].replace('../', '')
                                image_name = episode + '_' + str(i + 1).zfill(2)
                                image_objs.append({'name': image_name, 'url': image_url})
                        self.download_image_objects(image_objs, self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_episode_preview_guess(self):
        if self.is_image_exists(str(self.LAST_EPISODE) + '_01'):
            return

        image_url_template = 'https://jujutsukaisen.jp/images/episodes/%s-%s.jpg'
        for i in range(1, self.LAST_EPISODE + 1, 1):
            for j in range(1, 11, 1):
                image_name = str(i).zfill(2) + '_' + str(j).zfill(2)
                if self.is_image_exists(image_name):
                    continue
                image_url = image_url_template % (str(i), str(j))
                result = self.download_image(image_url, self.base_folder + '/' + image_name)
                if result == -1:
                    return

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'kv1', 'url': 'https://jujutsukaisen.jp/news/images/20200914_01_01.jpg'},
            {'name': 'kv2', 'url': 'https://jujutsukaisen.jp/news/images/20200525_01_01.jpg'},
        ]
        self.download_image_objects(image_objs, folder)


# Kamisama ni Natta Hi
class KamisamaNiNattaHiDownload(Fall2020AnimeDownload):
    title = "Kamisama ni Natta Hi"
    keywords = [title, "The Day I Became a God"]
    folder_name = 'kamisama-ni-natta-hi'

    PAGE_PREFIX = 'https://kamisama-day.jp/'
    STORY_PAGE = 'https://kamisama-day.jp/story/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()
        self.download_bluray()
        self.download_bluray_bonus()
        self.download_music()
        self.download_other()

    def download_episode_preview(self):
        #self.has_website_updated(self.STORY_PAGE)
        # Create episode log
        cache_filepath = self.base_folder + '/log/episode_cache'
        processed = []
        num_processed = 0
        if os.path.exists(cache_filepath):
            with open(cache_filepath, 'r') as f:
                inputs = f.read()
            processed = inputs.split(';')
            num_processed = len(processed)

        try:
            soup = self.get_soup(self.STORY_PAGE)
            nav = soup.find('nav', class_='page_tab')
            if nav:
                lis = nav.find_all('li')
                for li in lis:
                    if li.has_attr('class'):
                        if li['class'] == 'synopsis':
                            continue
                    a_tag = li.find('a')
                    if a_tag and a_tag.has_attr('href'):
                        try:
                            episode = str(int(a_tag.text)).zfill(2)
                        except:
                            continue
                        if self.is_image_exists(episode + '_5'):
                            continue
                        episode_url = self.STORY_PAGE + a_tag['href'].replace('./', '')
                        episode_soup = self.get_soup(episode_url)
                        div = episode_soup.find('div', class_='main_image')
                        if div:
                            images = div.find_all('img')
                            self.image_list = []
                            img_num = 1
                            for i in range(len(images)):
                                if images[i].has_attr('src'):
                                    image_url = self.STORY_PAGE + images[i]['src']
                                    if image_url in processed:
                                        continue
                                    while self.is_image_exists(episode + '_' + str(img_num)):
                                        img_num += 1
                                    image_name = episode + '_' + str(img_num)
                                    result = self.download_image(image_url, self.base_folder + '/' + image_name)
                                    if result != -1:
                                        processed.append(image_url)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

        if len(processed) > num_processed:
            with open(cache_filepath, 'w+') as f:
                for i in range(len(processed)):
                    if i > 0:
                        f.write(';')
                    f.write(processed[i])

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'opening_1', 'url': 'https://kamisama-day.jp/assets/img/opening_1.jpg'},
            {'name': 'opening_2', 'url': 'https://kamisama-day.jp/assets/img/opening_2.jpg'},
            {'name': 'opening_3', 'url': 'https://kamisama-day.jp/assets/img/opening_3.jpg'},
            {'name': 'kv', 'url': 'https://pbs.twimg.com/media/Ei13ho5UMAEhqwj?format=jpg&name=large'},
            {'name': 'kv2', 'url': 'https://kamisama-day.jp/assets/img/kv.jpg'},
            {'name': 'kv3', 'url': 'https://kamisama-day.jp/assets/img/top/kv.jpg'},
            {'name': 'kv4', 'url': 'https://kamisama-day.jp/assets/img/top/kv2/kv.jpg'},
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

    def download_bluray(self):
        folder = self.create_bluray_directory()
        try:
            for i in range(6):
                num = i + 1
                image_name = 'bd' + str(num)
                if self.is_image_exists(image_name):
                    continue
                soup = self.get_soup(self.PAGE_PREFIX + 'bddvd/?no=' + str(num).zfill(2))
                if soup is None:
                    continue
                div = soup.find('div', class_='jk_image')
                if div:
                    image = div.find('img')
                    if image and image.has_attr('src'):
                        image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                        if 'printing' in image_url:
                            break
                        content_length = requests.head(image_url).headers['Content-Length']
                        if content_length == '20243': # Now Printing
                            break
                        image_objs = [{'name': image_name, 'url': image_url}]
                        self.download_image_objects(image_objs, folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Blu-Ray")
            print(e)

        # Scrape the news for Blu-ray
        last_id = 55657 # News ID to stop scanning
        news_cache_file = folder + '/news_cache'
        if os.path.exists(news_cache_file):
            try:
                with open(news_cache_file, 'r', encoding='utf-8') as f:
                    latest_id = int(f.read())
                    last_id = latest_id
            except:
                latest_id = last_id
        else:
            latest_id = last_id
        try:
            page = 0
            stop = False
            while page < 50:
                if stop:
                    break
                page += 1
                soup = self.get_soup('https://kamisama-day.jp/news/?p=%s' % str(page), decode=True)
                news_list = soup.find('div', class_='news_list')
                if news_list:
                    news_items = news_list.find_all('li')
                    for news_item in news_items:
                        a_tag = news_item.find('a')
                        if a_tag and a_tag.has_attr('href'):
                            id = int(a_tag['href'].split('id=')[1])
                            if id < last_id:
                                stop = True
                                break
                            news_title = news_item.find('p', class_='news_title')
                            if news_title and 'Blu-ray' in news_title.text and '公開' in news_title.text\
                                and '第' in news_title.text and '巻' in news_title.text:
                                volume = news_title.text.split('第')[1].split('巻')[0]
                                news_url = 'https://kamisama-day.jp/news' + a_tag['href'].replace('.', '')
                                news_soup = self.get_soup(news_url, decode=True)
                                news_detail = news_soup.find('div', class_='news_detail')
                                if news_detail:
                                    images = news_detail.find_all('img')
                                    image_objs = []
                                    for i in range(len(images)):
                                        if images[i].has_attr('src'):
                                            image_url = 'https://kamisama-day.jp/news/'\
                                                        + images[i]['src'].split('/w')[0]
                                            if i > 0:
                                                image_name = 'bd_news_%s_%s' % (volume, str(i + 1))
                                            else:
                                                image_name = 'bd_news_%s' % volume
                                            image_objs.append({'name': image_name, 'url': image_url})
                                    if len(image_objs) > 0:
                                        self.download_image_objects(image_objs, folder)
                                        if id > latest_id:
                                            latest_id = id
                else:
                    break
            with open(news_cache_file, 'w+', encoding='utf-8') as f:
                f.write(str(latest_id))
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Blu-Ray News")
            print(e)

    def download_bluray_bonus(self):
        folder = self.create_bluray_directory()
        cache_filepath = folder + '/' + 'cache'
        processed = []
        num_processed = 0
        if os.path.exists(cache_filepath):
            with open(cache_filepath, 'r') as f:
                inputs = f.read()
            processed = inputs.split(';')
            num_processed = len(processed)

        queries = ['cmn', 'ltd']
        try:
            for query in queries:
                if query in processed:
                    continue
                page_url = self.PAGE_PREFIX + 'bddvd/?no=' + query
                if query == 'cmn':
                    search_tag = 'div'
                elif query == 'ltd':
                    search_tag = 'p'
                else:
                    continue
                soup = self.get_soup(page_url)
                if soup is None:
                    continue
                items = soup.find_all(search_tag, class_='item_image')
                image_objs = []
                image_count = 0
                for item in items:
                    image = item.find('img')
                    if image and image.has_attr('src'):
                        image_count += 1
                        image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                        content_length = requests.head(image_url).headers['Content-Length']
                        if content_length == '19597':  # Now Printing
                            continue
                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                        image_objs.append({'name': image_name, 'url': image_url})
                self.download_image_objects(image_objs, folder)
                if image_count == len(image_objs):
                    processed.append(query)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Blu-Ray Bonus")
            print(e)

        if len(processed) > num_processed:
            with open(cache_filepath, 'w+') as f:
                for i in range(len(processed)):
                    if i > 0:
                        f.write(';')
                    f.write(processed[i])

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
    folder_name = 'kamihiro'

    PAGE_PREFIX = 'https://kamihiro-anime.com'
    STORY_PAGE = 'https://kamihiro-anime.com/story/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_guess()
        self.download_key_visual()
        self.download_character()
        self.download_music()

    def download_episode_preview(self):
        self.has_website_updated(self.STORY_PAGE)
        try:
            soup = self.get_soup(self.STORY_PAGE)
            articles = soup.find_all('article', class_='story-block')
            for article in articles:
                episode_div = article.find('div', class_='episode')
                if not episode_div:
                    continue
                try:
                    episode = str(int(episode_div.find('em').text.strip())).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                slider_div = article.find('div', class_='story-block__main--slider')
                if slider_div:
                    images = slider_div.find_all('img')
                    image_objs = []
                    for i in range(len(images)):
                        if images[i].has_attr('src'):
                            image_url = images[i]['src']
                            image_name = episode + '_' + str(i + 1)
                            image_objs.append({'name': image_name, 'url': image_url})
                    self.download_image_objects(image_objs, self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        dt = datetime.now().strftime("%m").zfill(2)
        url_base = 'https://kamihiro-anime.com/wp/wp-content/uploads/2020/%s/%s.png'
        for i in range(1, 7, 1):
            j = 0
            while True:
                if j == 0:
                    image_url = url_base % (dt, str(i).zfill(2))
                    image_name = '%s-%s' % (dt, str(i).zfill(2))
                else:
                    image_url = url_base % (dt, str(i).zfill(2) + '-' + str(j))
                    image_name = '%s-%s' % (dt, str(i).zfill(2) + '-' + str(j))
                j += 1
                if self.is_image_exists(image_name, folder):
                    continue
                result = self.download_image(image_url, folder + '/' + image_name)
                if result == -1:
                    break
                else:
                    print(self.__class__.__name__ + ' - Guessed successfully!')

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
    folder_name = 'kimisen'

    PAGE_PREFIX = 'https://kimisentv.com/'
    STORY_PAGE = 'https://kimisentv.com/story/'
    LAST_EPISODE = 12

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()
        self.download_bluray()
        self.download_music()

    def download_episode_preview(self):
        story_template = self.PAGE_PREFIX + 'assets/story/%s_%s.jpg'
        for i in range(self.LAST_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            for j in range(6):
                img_num = str(j + 1)
                image_url = story_template % (str(i + 1), str(j + 1))
                image_name = episode + '_' + img_num
                result = self.download_image(image_url, self.base_folder + '/' + image_name)
                if result == -1:
                    return

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

    def download_bluray(self):
        folder = self.create_bluray_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bddvd/')
            sub_containers = soup.find_all('div', class_='sub-container')
            for sub_container in sub_containers:
                img_tags = sub_container.find_all('img')
                image_objs = []
                for img_tag in img_tags:
                    if img_tag.has_attr('src'):
                        image_url = self.PAGE_PREFIX + img_tag['src'].replace('../', '').split('?')[0]
                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                        image_objs.append({'name': image_name, 'url': image_url})
                self.download_image_objects(image_objs, folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Blu-Ray")
            print(e)

    def download_music(self):
        folder = self.create_custom_directory('music')
        image_objs = [
            {'name': 'music_ed', 'url': 'https://pbs.twimg.com/media/Ejum38pVcAMY8iO?format=jpg&name=large'},
        ]
        self.download_image_objects(image_objs, folder)
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
    folder_name = 'kumabear'

    PAGE_PREFIX = 'https://kumakumakumabear.com/'
    STORY_PAGE = 'https://kumakumakumabear.com/story/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_guess()
        self.download_episode_preview_external()
        self.download_key_visual()
        self.download_character()
        self.download_music()
        self.download_bluray()

    def download_episode_preview(self):
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
                        if self.is_image_exists(episode + '_6'):
                            continue
                        new_photo = False
                        episode_url = self.PAGE_PREFIX + a_tag['href'].replace('../', '')
                        episode_soup = self.get_soup(episode_url)
                        wdxmax_div_tag = episode_soup.find('div', class_='wdxmax')
                        if wdxmax_div_tag:
                            images = wdxmax_div_tag.find_all('img')
                            if self.is_image_exists(episode + '_4'):
                                if len(images) == 6:
                                    new_photo = True
                                else:
                                    continue
                            image_objs = []
                            k = 4
                            filesizes = []
                            if new_photo:
                                for m in range(4):
                                    filesizes.append(os.path.getsize(
                                        self.base_folder + ('/%s_%s.jpg' % (episode, str(m + 1)))))
                            for j in range(len(images)):
                                if images[j].has_attr('src'):
                                    image_url = self.PAGE_PREFIX + images[j]['src'].replace('../', '').split('?')[0]
                                    if new_photo:
                                        if self.is_matching_content_length(image_url, filesizes):
                                            continue
                                        k += 1
                                        image_name = episode + '_' + str(k)
                                    else:
                                        image_name = episode + '_' + str(j + 1)
                                    image_objs.append({'name': image_name, 'url': image_url})
                            self.download_image_objects(image_objs, self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        story_template = 'https://kumakumakumabear.com/core_sys/images/contents/%s/block/%s/%s.jpg'
        # Start from Episode 6
        content_num_first = 24
        block_num_first = 47
        image_num_first = 38
        num_of_pic_per_episode = 6
        for i in range(5, 13):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            is_success = False
            for j in range(num_of_pic_per_episode):
                content_num = str(content_num_first + i).zfill(8)
                block_num = str(block_num_first + i * 2).zfill(8)
                image_num = str(image_num_first + i * num_of_pic_per_episode + j).zfill(8)
                image_url = story_template % (content_num, block_num, image_num)
                image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                if self.is_image_exists(image_name, folder):
                    is_success = True
                    break
                result = self.download_image(image_url, folder + '/' + image_name)
                if result == 0:
                    print(self.__class__.__name__ + ' - Guessed successfully!')
                    is_success = True
            if not is_success:
                return

    def download_episode_preview_external(self):
        jp_title = 'くまクマ熊ベアー'
        AniverseMagazineScanner(jp_title, self.base_folder, 12).run()

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
                        content_length = requests.head(image_url).headers['Content-Length']
                        if content_length == '58281' or content_length == '106581':
                            continue
                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                        if image_name == '00000041':
                            image_name = 'music_ed'
                        if image_name == '00000148':
                            image_name = 'ost'
                        image_objs.append({'name': image_name, 'url': image_url})
                self.download_image_objects(image_objs, folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Music")
            print(e)

    def download_bluray(self):
        folder = self.create_bluray_directory()

        cache_filepath = folder + '/' + 'cache'
        processed = []
        num_processed = 0
        if os.path.exists(cache_filepath):
            with open(cache_filepath, 'r') as f:
                inputs = f.read()
            processed = inputs.split(';')
            num_processed = len(processed)

        try:
            bd_urls = ['privilege', '01', '02', '03']
            for i in range(len(bd_urls)):
                if bd_urls[i] in processed:
                    continue
                bd_url = self.PAGE_PREFIX + 'bddvd/' + bd_urls[i] + '.html'
                soup = self.get_soup(bd_url)
                ph_tags = soup.find_all('div', class_='ph')
                if ph_tags:
                    image_objs = []
                    image_count = 0
                    for ph_tag in ph_tags:
                        image = ph_tag.find('img')
                        if image and image.has_attr('src'):
                            image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                            image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                            # if self.is_image_exists(image_name, folder):
                            #     continue
                            image_count += 1
                            content_length = requests.head(image_url).headers['Content-Length']
                            if content_length == '58281' or content_length == '106581':
                                if i > 0:
                                    return
                                else:
                                    continue
                            image_objs.append({'name': image_name, 'url': image_url})
                    self.download_image_objects(image_objs, folder)
                    if image_count == len(image_objs):
                        processed.append(bd_url)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Music")
            print(e)

        if len(processed) > num_processed:
            with open(cache_filepath, 'w+') as f:
                for i in range(len(processed)):
                    if i > 0:
                        f.write(';')
                    f.write(processed[i])


# Maesetsu!
class MaesetsuDownload(Fall2020AnimeDownload):
    title = "Maesetsu!"
    keywords = [title]
    folder_name = 'maesetsu'

    PAGE_PREFIX = 'https://maesetsu.jp/'
    STORY_PAGE = 'https://maesetsu.jp/story/'
    LAST_EPISODE = 12

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_key_visual()
        self.download_character()
        self.download_bluray()
        self.download_music()
        self.download_other()

    def download_episode_preview(self):
        try:
            for i in range(self.LAST_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_1'):
                    continue
                soup = self.get_soup(self.STORY_PAGE + episode + '.html')
                if len(soup) == 0:
                    break
                ph_divs = soup.find_all('div', class_='ph')
                image_objs = []
                for i in range(len(ph_divs)):
                    image = ph_divs[i].find('img')
                    if image and image.has_attr('src'):
                        image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                        image_name = episode + '_' + str(i + 1)
                        image_objs.append({'name': image_name, 'url': image_url})
                self.download_image_objects(image_objs, self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_episode_preview_external(self):
        jp_title = 'まえせつ'
        AniverseMagazineScanner(jp_title, self.base_folder, 12, suffix='幕').run()

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

    def download_bluray(self):
        folder = self.create_bluray_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bd/privilege.html')
            # Blu-Ray Bonus
            cms_block = soup.find('div', id='cms_block')
            if cms_block:
                self.image_list = []
                bd_bonus_images = cms_block.find_all('img')
                for image in bd_bonus_images:
                    if image.has_attr('src'):
                        image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                        if len(image_url) > 12 and image_url[-12:] == 'newsPict.png':
                            continue
                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                        self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)

            # BLu-rays
            nav_bar = soup.find('div', id='ContentsListUnit03')
            if nav_bar:
                a_tags = nav_bar.find_all('a')
                for i in range(4):
                    bd_vol = i + 1
                    if self.is_image_exists('bd_vol' + str(bd_vol), folder):
                        continue
                    if a_tags[i].has_attr('href'):
                        header_image = a_tags[i].find('img')
                        if header_image and header_image.has_attr('src'):
                            header_image_url = self.PAGE_PREFIX + header_image['src'].replace('../', '').split('?')[0]
                            if self.is_matching_content_length(header_image_url, 54171):
                                continue
                            bd_url = self.PAGE_PREFIX + a_tags[i]['href'].replace('../', '')
                            bd_soup = self.get_soup(bd_url)
                            bd_cms_block = bd_soup.find('div', id='cms_block')
                            if bd_cms_block:
                                images = bd_cms_block.find_all('img')
                                self.image_list = []
                                for j in range(len(images)):
                                    if images[j].has_attr('src'):
                                        image_name = 'bd_vol' + str(bd_vol)
                                        if j > 0:
                                            image_name += '_' + str(j)
                                        image_url = self.PAGE_PREFIX + images[j]['src'].replace('../', '').split('?')[0]
                                        if self.is_matching_content_length(image_url, 53979):
                                            break
                                        self.add_to_image_list(image_name, image_url)
                                self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Blu-Ray")
            print(e)


# Mahouka Koukou no Rettousei: Raihousha-hen
class Mahouka2Download(Fall2020AnimeDownload):
    title = "Mahouka Koukou no Rettousei: Raihousha-hen"
    keywords = [title, "The Irregular at Magic High School", "2nd"]
    folder_name = 'mahouka2'

    PAGE_PREFIX = 'https://mahouka.jp/'
    STORY_PAGE = 'https://mahouka.jp/story/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()
        self.download_bluray()

    def download_episode_preview(self):
        #self.has_website_updated(self.STORY_PAGE)
        try:
            soup = self.get_soup(self.STORY_PAGE)
            nav = soup.find('nav', class_='story_nav')
            if nav:
                a_tags = nav.find_all('a')
                for a_tag in a_tags:
                    if a_tag.has_attr('href') and 'story' in a_tag['href']:
                        try:
                            episode = str(int(a_tag.text)).zfill(2)
                        except:
                            continue
                        if self.is_image_exists(episode + '_1'):
                            continue
                        episode_url = a_tag['href']
                        if len(episode_url) > 1 and episode_url[0] == '/':
                            episode_url = episode_url[1:]
                        episode_soup = self.get_soup(self.PAGE_PREFIX + episode_url)
                        div_image = episode_soup.find('div', class_='img_list')
                        if div_image:
                            images = div_image.find_all('img')
                            image_objs = []
                            for i in range(len(images)):
                                if images[i].has_attr('src'):
                                    image_url = self.STORY_PAGE + images[i]['src']
                                    image_name = episode + '_' + str(i + 1)
                                    image_objs.append({'name': image_name, 'url': image_url})
                            self.download_image_objects(image_objs, self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'teaser', 'url': 'https://mahouka.jp/news/SYS/CONTENTS/2019100420534812757301'},
            {'name': 'kv', 'url': 'https://mahouka.jp/assets/img/top/main/kv/kv.jpg'}
        ]
        self.download_image_objects(image_objs, folder)

    def download_character(self):
        folder = self.create_character_directory()
        image_objs = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            img_divs = soup.find_all('div', class_='charaBox')
            for img_div in img_divs:
                images = img_div.find_all('img')
                for image in images:
                    if image and image.has_attr('src'):
                        image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                        image_objs.append({'name': image_name, 'url': image_url})
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)
        self.download_image_objects(image_objs, folder)

    def download_bluray(self):
        folder = self.create_bluray_directory()
        image_objs = [
            {'name': 'music_op', 'url': 'https://pbs.twimg.com/media/Ej8Am0hVoAAGbKw?format=jpg&name=large'},
            {'name': 'music_ed', 'url': 'https://pbs.twimg.com/media/EjaDeI-U8AATDHD?format=jpg&name=900x900'},
            {'name': 'bd_1_1', 'url': 'https://pbs.twimg.com/media/EjZfp3DU4AEmx9C?format=jpg&name=4096x4096'},
            {'name': 'bd_1_2', 'url': 'https://pbs.twimg.com/media/EjZfrEUUwAAzXn2?format=jpg&name=large'},
            {'name': 'bd_2', 'url': 'https://pbs.twimg.com/media/ElEkb9KVMAE0XXw?format=jpg&name=large'},
            {'name': 'bd_3', 'url': 'https://pbs.twimg.com/media/EmxqPFoVcAA0zGu?format=jpg&name=large'},
            {'name': 'bd_bonus_1', 'url': 'https://pbs.twimg.com/media/EjZfyqAUwAAOBrL?format=jpg&name=4096x4096'},
            {'name': 'bd_bonus_2', 'url': 'https://pbs.twimg.com/media/EkhCx5mU8AAD3nA?format=jpg&name=4096x4096'},
            {'name': 'bd_bonus_3', 'url': 'https://pbs.twimg.com/media/EkhCy7jU0AYniNf?format=jpg&name=large'},
            {'name': 'bd_bonus_4', 'url': 'https://pbs.twimg.com/media/EkhDWRpVcAA-lgE?format=jpg&name=large'},
            {'name': 'bd_bonus_5', 'url': 'https://pbs.twimg.com/media/EkhDXcJVoAEGq9g?format=jpg&name=large'},
            {'name': 'bd_bonus_6', 'url': 'https://pbs.twimg.com/media/EkhDYR9U8AMFpw3?format=jpg&name=large'},
        ]
        self.download_image_objects(image_objs, folder)

        cache_filepath = folder + '/' + 'cache'
        processed = []
        num_processed = 0
        if os.path.exists(cache_filepath):
            with open(cache_filepath, 'r') as f:
                inputs = f.read()
            processed = inputs.split(';')
            num_processed = len(processed)

        try:
            package_template = 'https://mahouka.jp/package/%s.html'
            package_id = ['index'] + [str(i).zfill(2) for i in range(2, 6)] + ['ost']
            bd_urls = [package_template % id for id in package_id]
            to_process = True
            for i in range(len(bd_urls)):
                if package_id[i] in processed:
                    continue
                if 0 < i < 5 and not to_process:
                    continue
                soup = self.get_soup(bd_urls[i])
                if soup:
                    package_divs = soup.find_all('div', class_='pkg_info')
                    image_objs = []
                    image_count = 0
                    for package_div in package_divs:
                        images = package_div.find_all('img')
                        stop = False
                        for image in images:
                            if image.has_attr('src'):
                                image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                                image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                                # if self.is_image_exists(image_name, folder):
                                #     continue
                                image_count += 1
                                content_length = requests.head(image_url).headers['Content-Length']
                                if content_length == '12538' or content_length == '22084':  # Skip Now Printing
                                    if 0 < i < 5:
                                        to_process = False
                                        stop = True
                                        break
                                    else:
                                        continue
                                image_objs.append({'name': image_name, 'url': image_url})
                                if 0 < i < 5:  # Evaluate only the first image
                                    stop = True
                                    break
                        if stop:
                            break
                    self.download_image_objects(image_objs, folder)
                    if image_count == len(image_objs):
                        processed.append(package_id[i])
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Blu-ray')
            print(e)

        if len(processed) > num_processed:
            with open(cache_filepath, 'w+') as f:
                for i in range(len(processed)):
                    if i > 0:
                        f.write(';')
                    f.write(processed[i])


# Majo no Tabitabi
class MajotabiDownload(Fall2020AnimeDownload):
    title = "Majo no Tabitabi"
    keywords = [title, "Wandering Witch: The Journey of Elaina", "Majotabi"]
    folder_name = 'majotabi'

    PAGE_PREFIX = 'https://majotabi.jp/'
    LAST_EPISODE = 12

    def __init__(self):
        super().__init__()

    def run(self):
        soup = self.get_soup(self.PAGE_PREFIX)
        if soup is None:
            return

        self.download_episode_preview(soup)
        self.download_episode_preview_guess()
        self.download_key_visual()
        self.download_character(soup)
        self.download_bluray(soup)

    def download_episode_preview(self, soup=None):
        if not soup:
            soup = self.get_soup(self.PAGE_PREFIX)
        story_list = soup.find_all('div', class_='story-data')
        for story in story_list:
            slider_div = story.find('div', class_='ep-slider-sceneImage')
            if slider_div:
                episode_label = story.find('span', class_='ep-title-label')
                if episode_label and '第' in episode_label.text and '話' in episode_label.text:
                    try:
                        episode = str(int(episode_label.text.split('第')[1].split('話')[0])).zfill(2)
                    except:
                        continue
                else:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                images = slider_div.find_all('img')
                image_objs = []
                for i in range(len(images)):
                    if images[i].has_attr('src'):
                        image_url = self.PAGE_PREFIX + images[i]['src'].replace('./', '')
                        image_name = episode + '_' + str(i + 1)
                        image_objs.append({'name': image_name, 'url': image_url})
                self.download_image_objects(image_objs, self.base_folder)

    def download_episode_preview_guess(self):
        if self.is_image_exists(str(self.LAST_EPISODE) + '_1'):
            return

        image_url_template = 'https://majotabi.jp/assets/story/%s_%s.jpg'
        for i in range(1, self.LAST_EPISODE + 1, 1):
            for j in range(1, 9, 1):
                image_name = str(i).zfill(2) + '_' + str(j)
                if self.is_image_exists(image_name):
                    continue
                image_url = image_url_template % (str(i), str(j))
                result = self.download_image(image_url, self.base_folder + '/' + image_name)
                if result == -1:
                    return

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
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
        self.download_image_objects(image_objs, folder)

    def download_character(self, soup=None):
        folder = self.create_character_directory()
        try:
            if not soup:
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

    def download_bluray(self, soup=None):
        folder = self.create_bluray_directory()
        image_objs = [
            {'name': 'music_op', 'url': 'https://pbs.twimg.com/media/EjVEHVKVgAQ_uWB?format=jpg&name=large'},
            {'name': 'music_ed', 'url': 'https://pbs.twimg.com/media/Ej5FapIU0AAas9c?format=jpg&name=large'},
        ]
        self.download_image_objects(image_objs, folder)
        try:
            if not soup:
                soup = self.get_soup(self.PAGE_PREFIX)
            data_div = soup.find('div', id='BddvdData')
            if data_div:
                images = data_div.find_all('img')
                image_objs = []
                for image in images:
                    if image.has_attr('src'):
                        image_url = self.PAGE_PREFIX + image['src'].replace('./', '')
                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                        image_objs.append({'name': image_name, 'url': image_url})
                self.download_image_objects(image_objs, folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Bluray")
            print(e)


# Maoujou de Oyasumi
class MaoujoDownload(Fall2020AnimeDownload):
    title = "Maoujou de Oyasumi"
    keywords = [title, "Maoujo", "Sleepy Princess in the Demon Castle"]
    folder_name = 'maoujo'

    PAGE_PREFIX = 'https://maoujo-anime.com/'
    STORY_PAGE = 'https://maoujo-anime.com/story/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()
        self.download_music()

    def download_episode_preview(self):
        self.has_website_updated(self.STORY_PAGE)
        #json_url = 'https://maoujo-anime.com/news/wp-json/wp/v2/pages?orderby=date&order=asc&per_page=100&parent=246'
        try:
            soup = self.get_soup(self.STORY_PAGE)
            story_div = soup.find('div', id='app-story')
            if story_div and story_div.has_attr('data-url'):
                json_url = story_div['data-url']
                episode_objs = self.get_json(json_url)
                for ep_obj in episode_objs:
                    title = ep_obj['title']['rendered'].strip()
                    if len(title) > 2 and '第' == title[0] and '夜' in title[-1]:
                        try:
                            episode = str(int(title[1:len(title)-1])).zfill(2)
                        except:
                            continue
                    else:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    images = ep_obj['acf']['images']
                    image_objs = []
                    for i in range(len(images)):
                        image_url = images[i]['url']
                        image_name = episode + '_' + str(i + 1)
                        image_objs.append({'name': image_name, 'url': image_url})
                    self.download_image_objects(image_objs, self.base_folder)
        except Exception as e:
                print("Error in running " + self.__class__.__name__)
                print(e)

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
    folder_name = 'munou-na-nana'

    PAGE_PREFIX = 'https://munounanana.com/'
    STORY_PAGE = 'https://munounanana.com/story/'
    LAST_EPISODE = 13

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()
        self.download_bluray()

    def download_episode_preview(self):
        story_template = 'https://munounanana.com/assets/story/%s_%s.jpg'
        for i in range(self.LAST_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            for j in range(5):
                img_num = str(j + 1)
                image_url = story_template % (str(i + 1), str(j + 1))
                image_name = episode + '_' + img_num
                result = self.download_image(image_url, self.base_folder + '/' + image_name)
                if result == -1:
                    return

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
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)
        self.download_image_objects(image_objs, folder)

    def download_bluray(self):
        folder = self.create_bluray_directory()
        try:
            soup = self.get_soup('https://munounanana.com/bddvd/')
            containers = soup.find_all('div', class_='bddvd-container')
            for container in containers:
                images = container.find_all('img')
                self.image_list = []
                for image in images:
                    if image.has_attr('src'):
                        image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                        self.add_to_image_list(name=image_name, url=image_url)
                self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Blu-Ray")
            print(e)


# Ochikobore Fruit Tart
class OchifuruDownload(Fall2020AnimeDownload):
    title = "Ochikobore Fruit Tart"
    keywords = [title, "Dropout Idol", "Ochifuru"]
    folder_name = 'ochifuru'

    PAGE_PREFIX = 'http://ochifuru-anime.com/'
    STORY_PAGE = 'http://ochifuru-anime.com/story.html'
    CHARA_IMAGE_TEMPLATE = 'http://ochifuru-anime.com/images/chara/%s/p_002.png'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_key_visual()
        self.download_character()
        self.download_bluray()
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

    def download_episode_preview_external(self):
        jp_title = 'おちこぼれフルーツタルト'
        AniverseMagazineScanner(jp_title, self.base_folder, 12).run()

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

    def download_bluray(self):
        folder = self.create_bluray_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'package.html')
            div = soup.find('div', class_='newsPaging')
            if div:
                images = div.find_all('img')
                image_objs = []
                for image in images:
                    if image.has_attr('src'):
                        image_url = self.PAGE_PREFIX + image['src']
                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                        image_objs.append({'name': image_name, 'url': image_url})
                self.download_image_objects(image_objs, folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Blu-Ray")
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
    folder_name = 'one-room3'

    PAGE_PREFIX = "https://oneroom-anime.com/"
    STORY_PAGE = "https://oneroom-anime.com/story/"

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_bluray()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.STORY_PAGE)
            story_div = soup.find('div', class_='storyArea')
            if story_div:
                lis = story_div.find_all('li')
                for li in lis:
                    h4 = li.find('h4')
                    if h4 and '第' in h4.text and '話' in h4.text:
                        try:
                            episode = str(int(h4.text.split('第')[1].split('話')[0])).zfill(2)
                        except:
                            continue
                    else:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    image_objs = []
                    first_img = li.find('img')
                    if first_img and first_img.has_attr('src'):
                        image_objs.append({'name': episode + '_1', 'url': first_img['src']})
                    a_tag = li.find('a')
                    if a_tag and a_tag.has_attr('href'):
                        ep_soup = self.get_soup(a_tag['href'])
                        article_tag = ep_soup.find('article')
                        if not article_tag:
                            continue
                        main_img = article_tag.find('div', class_='mainImage')
                        if main_img:
                            main_img_tag = main_img.find('img')
                            if main_img_tag and main_img_tag.has_attr('src'):
                                image_objs.append({'name': episode + '_2', 'url': main_img_tag['src']})
                        img_lis = article_tag.find_all('li')
                        for i in range(len(img_lis)):
                            image = img_lis[i].find('img')
                            if image and image.has_attr('src'):
                                image_num = i + 3
                                image_objs.append({'name': episode + '_' + str(image_num), 'url': image['src']})
                    self.download_image_objects(image_objs, self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'kv', 'url': 'https://pbs.twimg.com/media/Eg9v7u7VgAAhwPr?format=jpg&name=4096x4096'}]
        self.download_image_objects(image_objs, folder)

    def download_bluray(self):
        folder = self.create_bluray_directory()
        image_objs = [
            {'name': 'bd_s1s2_1', 'url': 'https://oneroom-anime.com/wordpress/wp-content/uploads/2020/07/237a13f0134854b4d0b8162879eafef1.jpg'},
            {'name': 'bd_s1s2_2', 'url': 'https://oneroom-anime.com/wordpress/wp-content/uploads/2020/07/5cc4ed2d63953152405ca92e5549c420.jpg'},
            {'name': 'oneroom_bd3', 'url': 'https://oneroom-anime.com/wordpress/wp-content/uploads/2020/11/oneroom_bd3.jpg'},
        ]
        self.download_image_objects(image_objs, folder)


# Rail Romanesque
class RailRomanesqueDownload(Fall2020AnimeDownload):
    title = "Rail Romanesque"
    keywords = [title, "Maitetsu"]
    folder_name = 'rail-romanesque'

    PAGE_PREFIX = 'https://railromanesque.jp/'

    def __init__(self):
        super().__init__()

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
    folder_name = 'sigrdrifa'

    PAGE_PREFIX = "https://sigururi.com/"
    STORY_PAGE = 'https://sigururi.com/story/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()
        self.download_bluray()
        self.download_other()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.STORY_PAGE)
            nav = soup.find('nav', class_='page_tab')
            if nav:
                lis = nav.find_all('li')
                for li in lis:
                    a_tag = li.find('a')
                    if a_tag and a_tag.has_attr('href'):
                        try:
                            episode = str(int(a_tag.text.strip())).zfill(2)
                        except:
                            continue
                        if self.is_image_exists(episode + '_1'):
                            continue
                        story_url = self.STORY_PAGE + a_tag['href'].replace('./', '')
                        story_soup = self.get_soup(story_url)
                        img_div = story_soup.find('div', class_='s_image')
                        if img_div:
                            images = img_div.find_all('img')
                            image_objs = []
                            for i in range(len(images)):
                                if images[i].has_attr('src'):
                                    image_url = self.STORY_PAGE + images[i]['src']
                                    image_name = episode + '_' + str(i + 1)
                                    image_objs.append({'name': image_name, 'url': image_url})
                            self.download_image_objects(image_objs, self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

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

    def download_bluray(self):
        folder = self.create_bluray_directory()
        image_objs = [
            {'name': 'img_special_01_2', 'url': 'https://sigururi.com/news/SYS/CONTENTS/2020102619501742165262'}
        ]
        self.download_image_objects(image_objs, folder)
        try:
            bd_url_template = self.PAGE_PREFIX + 'bddvd/vol%s/'
            bd_urls = [self.PAGE_PREFIX + 'bddvd/special/'] + [bd_url_template % str(i + 1).zfill(2) for i in range(6)]
            j = -1
            for bd_url in bd_urls:
                j += 1
                is_volume = False
                if '/vol' in bd_url:
                    if self.is_image_exists('bd_vol%s' % str(j)):
                        continue
                    is_volume = True
                soup = self.get_soup(bd_url)
                if soup:
                    div = soup.find('div', class_='bddvd')
                    if div:
                        images = div.find_all('img')
                        image_objs = []
                        for k in range(len(images)):
                            if images[k].has_attr('src'):
                                if len(images[k]['src']) > 0 and images[k]['src'][0] == '/':
                                    image_url = self.PAGE_PREFIX + images[k]['src'][1:]
                                else:
                                    image_url = images[k]['src']
                                content_length = requests.head(image_url).headers['Content-Length']
                                if content_length == '29796' or content_length == '12133': # Skip Now Printing
                                    if is_volume:
                                        return
                                    continue
                                if is_volume:
                                    if k == 0:
                                        image_name = 'bd_vol%s' % str(j)
                                    else:
                                        image_name = 'bd_vol%s_%s' % (str(j), str(k))
                                else:
                                    image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                                image_objs.append({'name': image_name, 'url': image_url})
                        self.download_image_objects(image_objs, folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Blu-Ray")
            print(e)

    def download_other(self):
        folder = self.create_custom_directory('other')
        image_objs = [
            {'name': 'news_vol_01', 'url': 'https://pbs.twimg.com/media/EdnNj1qVoAEY4MX?format=jpg&name=4096x4096'},
            {'name': 'news_vol_02', 'url': 'https://pbs.twimg.com/media/EeYvh7oUYAAdeWc?format=jpg&name=4096x4096'},
            {'name': 'news_vol_03', 'url': 'https://pbs.twimg.com/media/EhM2-ZbVoAA9hIY?format=jpg&name=4096x4096'},
            {'name': 'uminohi', 'url': 'https://sigururi.com/SYS/CONTENTS/2020072310293692693264/w708'},
            {'name': 'zanshomimai', 'url': 'https://sigururi.com/news/SYS/CONTENTS/2020083114133842932562/w712'},
            {'name': 'soranohi', 'url': 'https://pbs.twimg.com/media/EiSXMZrU8AA4ThC?format=jpg&name=medium'},
            {'name': 'halloween', 'url': 'https://pbs.twimg.com/media/EllqxgTVcAEo3UO?format=jpg&name=large'},
            {'name': 'img_miyako', 'url': 'https://sigururi.com/assets/img/special/interview/img_miyako.jpg'},
            {'name': 'img_azuzu', 'url': 'https://sigururi.com/assets/img/special/interview/img_azuzu.jpg'},
            {'name': 'img_sonoka', 'url': 'https://sigururi.com/assets/img/special/interview/img_sonoka.jpg'},
            {'name': 'img_clau', 'url': 'https://sigururi.com/assets/img/special/interview/img_clau.jpg'},
            {'name': 'bs11_poster', 'url': 'https://pbs.twimg.com/media/EiuO9YwUYAAQ1U4?format=jpg&name=large'},
        ]
        self.download_image_objects(image_objs, folder)


# Strike Witches: Road to Berlin
class StrikeWitches3Download(Fall2020AnimeDownload):
    title = 'Strike Witches: Road to Berlin'
    keywords = [title]
    folder_name = 'strike-witches3'

    PAGE_PREFIX = 'http://w-witch.jp/strike_witches-rtb/'
    LAST_EPISODE = 12

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        image_url_template = 'http://w-witch.jp/strike_witches-rtb/story/img/%s/%s.jpg'
        stop = False
        for i in range(1, self.LAST_EPISODE + 1, 1):
            for j in range(1, 7, 1):
                image_url = image_url_template % (str(i).zfill(2), str(j).zfill(2))
                image_name = str(i).zfill(2) + '_' + str(j)
                result = self.download_image(image_url, self.base_folder + '/' + image_name)
                if result == -1:
                    stop = True
            if stop:
                break

        try:
            for m in range(1, self.LAST_EPISODE + 1, 1):
                episode = str(m).zfill(2)
                if self.is_image_exists(episode + '_1'):
                    continue
                page_url = 'http://w-witch.jp/strike_witches-rtb/story/?mode=detail&id=%s' % episode
                status_code = requests.head(page_url).status_code
                if status_code == 200:
                    soup = self.get_soup(page_url)
                    bxslider = soup.find('ul', class_='bxslider')
                    if bxslider:
                        images = bxslider.find_all('img')
                        self.image_list = []
                        for n in range(len(images)):
                            if images[n].has_attr('src'):
                                image_url = 'http://w-witch.jp/strike_witches-rtb/story/' + images[n]['src']
                                image_name = episode + '_' + str(n)
                                self.add_to_image_list(image_name, image_url)
                        self.download_image_list(self.base_folder)
                else:
                    break
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_episode_preview_external(self):
        try:
            jp_title = 'ストライクウィッチーズ ROAD to BERLIN'
            last_date = datetime.strptime('20201231', '%Y%m%d')
            today = datetime.today()
            if today < last_date:
                end_date = today
            else:
                end_date = last_date
            MocaNewsScanner(jp_title, self.base_folder, '20200925', end_date.strftime('%Y%m%d')).run()
            AniverseMagazineScanner(jp_title, self.base_folder, 12).run()
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - MocaNews')
            print(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'kv1', 'url': 'http://w-witch.jp/strike_witches-rtb/news/img/20200721_3/01.jpg'},
            {'name': 'mv-sp', 'url': 'http://w-witch.jp/strike_witches-rtb/img/top/mv-sp.jpg'},
            {'name': 'mv-pc', 'url': 'http://w-witch.jp/strike_witches-rtb/img/top/mv-pc.jpg'},
        ]
        self.download_image_objects(image_objs, folder)

    def download_character(self):
        folder = self.create_character_directory()
        stop = False
        for i in range(1, 31, 1):
            for j in range(1, 3, 1):
                image_url = self.PAGE_PREFIX + 'character/img/chara%s-%s.png' % (str(i), str(j))
                image_name = 'chara%s-%s' % (str(i), str(j))
                if self.is_image_exists(image_name, folder):
                    continue
                result = self.download_image(image_url, folder + '/' + image_name)
                if result == -1:
                    stop = True
            if stop:
                break

    def download_media(self):
        folder = self.create_bluray_directory()
        self.image_list = []
        self.add_to_image_list('bd1_1', 'https://pbs.twimg.com/media/EnqCinhUUAA8M6z?format=jpg&name=medium')
        self.add_to_image_list('bd1_2', 'https://pbs.twimg.com/media/EnqCinnVEAA24sK?format=jpg&name=medium')
        self.download_image_list(folder)

        for i in range(2):
            if i == 0:
                folder = self.create_bluray_directory()
                media_url = 'bd'
            else:
                folder = self.create_custom_directory('music')
                media_url = 'music'
            try:
                media_full_url = self.PAGE_PREFIX + media_url + '/'
                soup = self.get_soup(media_full_url)
                cts_boxes = soup.find_all('div', class_='cts_box')
                for cts_box in cts_boxes:
                    img_tags = cts_box.find_all('img')
                    image_objs = []
                    for img_tag in img_tags:
                        if img_tag.has_attr('src'):
                            if '../' in img_tag['src']:
                                image_url = self.PAGE_PREFIX + img_tag['src'].replace('../', '')
                            else:
                                image_url = media_full_url + img_tag['src']
                            image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                            image_objs.append({'name': image_name, 'url': image_url})
                    self.download_image_objects(image_objs, folder)
            except Exception as e:
                if i == 0:
                    output = 'Blu-ray'
                else:
                    output = 'Music'
                print("Error in running %s - %s" % (self.__class__.__name__, output))
                print(e)


# Tonikaku Kawaii
class TonikawaDownload(Fall2020AnimeDownload):
    title = "Tonikaku Kawaii"
    keywords = [title, "Tonikawa", "Cawaii", "Fly Me to the Moon"]
    folder_name = 'tonikawa'

    PAGE_PREFIX = 'http://tonikawa.com/'
    STORY_PAGE = 'http://tonikawa.com/story/'
    LAST_EPISODE = 12

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_guess()
        self.download_key_visual()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.STORY_PAGE)
            div_list = soup.find('div', class_='list')
            if div_list:
                item_list = div_list.find_all('div', class_='item')
                for item in item_list:
                    span_ep_num = item.find('span', class_='number')
                    if span_ep_num:
                        try:
                            episode = str(int(span_ep_num.text.replace('#', ''))).zfill(2)
                        except:
                            continue
                        if self.is_image_exists(episode + '_01'):
                            continue
                        ul = item.find('ul', class_='swiper-wrapper')
                        if ul:
                            images = ul.find_all('img')
                            image_objs = []
                            for i in range(len(images)):
                                if images[i].has_attr('src'):
                                    image_url = self.PAGE_PREFIX + images[i]['src'].replace('../', '')
                                    image_name = episode + '_' + str(i + 1).zfill(2)
                                    image_objs.append({'name': image_name, 'url': image_url})
                            self.download_image_objects(image_objs, self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_episode_preview_guess(self):
        image_url_template = 'http://tonikawa.com/assets/images/common/story/ep%s/img_%s.jpg'
        for i in range(1, self.LAST_EPISODE + 1, 1):
            for j in range(1, 11, 1):
                image_name = str(i).zfill(2) + '_' + str(j).zfill(2)
                if self.is_image_exists(image_name):
                    continue
                image_url = image_url_template % (str(i).zfill(2), str(j))
                result = self.download_image(image_url, self.base_folder + '/' + image_name)
                if result == -1:
                    return

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

