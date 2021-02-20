import os
import anime.constants as constants
from anime.main_download import MainDownload
from anime.external_download import MocaNewsDownload
from datetime import datetime
from scan import MocaNewsScanner, NatalieScanner, AniverseMagazineScanner, WebNewtypeScanner


# Dr. Stone: Stone Wars https://dr-stone.jp/ #DrSTONE @DrSTONE_off [MON]
# Gotoubun no Hanayome S2 https://www.tbs.co.jp/anime/5hanayome/ #五等分の花嫁 @5Hanayome_anime [TUE]
# Hataraku Saibou S2 https://hataraku-saibou.com/2nd.html #はたらく細胞 @hataraku_saibou [WED]
# Hataraku Saibou Black https://saibou-black.com/ #細胞BLACK @cellsatworkbla1 [FRI]
# Horimiya https://horimiya-anime.com/ #ホリミヤ #horimiya @horimiya_anime [SAT]
# Jaku-Chara Tomozaki-kun http://tomozaki-koushiki.com/ #友崎くん @tomozakikoshiki [MON]
# Kaifuku Jutsushi no Yarinaoshi http://kaiyari.com/ #回復術士 @kaiyari_anime [WED]
# Kemono Jihen https://kemonojihen-anime.com/ #怪物事変 #kemonojihen @Kemonojihen_tv [WED]
# Kumo Desu ga, Nani ka? https://kumo-anime.com/ #蜘蛛ですが @kumoko_anime [MON]
# Log Horizon: Entaku Houkai https://www6.nhk.or.jp/anime/program/detail.html?i=loghorizon3 #loghorizon @loghorizon_DORT [WED]
# Mushoku Tensei https://mushokutensei.jp/ #無職転生 @mushokutensei_A [WED]
# Non Non Biyori Nonstop https://nonnontv.com/ #なのん #のんのんびより @nonnontv [THU]
# Ore dake Haireru Kakushi Dungeon https://kakushidungeon-anime.jp/ #隠しダンジョン @kakushidungeon [WED]
# Tatoeba Last Dungeon https://lasdan.com/ #ラスダン @lasdan_PR [FRI]
# Tensei shitara Slime Datta Ken S2 https://www.ten-sura.com/anime/tensura #転スラ #tensura @ten_sura_anime [FRI]
# Urasekai Picnic https://www.othersidepicnic.com/ #裏ピク @OthersidePicnic [FRI AM]
# Wonder Egg Priority https://wonder-egg-priority.com/ #ワンエグ @WEP_anime [MON]
# World Trigger S2 http://www.toei-anim.co.jp/tv/wt/ #ワールドトリガー #トリガーオン @Anime_W_Trigger [SAT]
# Yuru Camp S2 https://yurucamp.jp/second/ #ゆるキャン @yurucamp_anime [FRI]


# Winter 2021 Anime
class Winter2021AnimeDownload(MainDownload):
    season = "2021-1"
    season_name = "Winter 2021"
    folder_name = '2021-1'

    def __init__(self):
        super().__init__()


# Dr. Stone: Stone Wars
class DrStone2Download(Winter2021AnimeDownload):
    title = "Dr. Stone: Stone Wars"
    keywords = [title, "2nd Season"]
    folder_name = 'dr-stone2'

    PAGE_LINK = 'https://dr-stone.jp/'
    FIRST_EPISODE = 1
    FINAL_EPISODE = 13

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_key_visual()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_LINK + 'story/2nd/')
            lis = soup.find_all('li', class_='storyarea_body_main_story_list_item')
            for li in lis:
                a_tag = li.find('a', class_='story_body')
                if a_tag and a_tag.has_attr('href'):
                    episode_div = a_tag.find('div', class_='story_body_main_ttl')
                    if episode_div:
                        ep_text = episode_div.text.strip()
                        if len(ep_text) > 2 and ep_text[0] == '第' and ep_text[-1] == '話':
                            try:
                                episode_number = int(ep_text.split('話')[0].split('第')[1])
                                episode = str(episode_number).zfill(2)
                            except:
                                continue
                            if episode_number > self.FINAL_EPISODE:
                                break
                            if episode_number < self.FIRST_EPISODE or self.is_image_exists(episode + '_1'):
                                continue
                            ep_soup = self.get_soup(a_tag['href'])
                            divs = ep_soup.find_all('div', class_='storydetail_body_main_subimg_img')
                            self.image_list = []
                            for i in range(len(divs)):
                                if divs[i].has_attr('data-imgload'):
                                    image_url = divs[i]['data-imgload']
                                    image_name = episode + '_' + str(i + 1)
                                    self.add_to_image_list(image_name, image_url)
                            self.download_image_list(self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_episode_preview_external(self):
        jp_title = 'Ｄｒ．ＳＴＯＮＥ'
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE, min_width=800, end_date='20210111').run()

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        template = self.PAGE_LINK + 'wp-content/themes/dr-stone_web/img/index/img_hero%s.jpg'
        i = 5
        while i < 10:
            image_url = template % str(i).zfill(2)
            image_name = 'img_hero' + str(i).zfill(2)
            result = self.download_image(image_url, folder + '/' + image_name)
            if result == -1:
                break
            i += 1


# Gotoubun no Hanayome ∬
class Gotoubun2Download(Winter2021AnimeDownload):
    title = "Gotoubun no Hanayome 2nd Season"
    keywords = [title, "The Quintessential Quintuplets", "Go-toubun", "5-toubun", "5hanayome", "2nd"]
    folder_name = 'gotoubun2'

    PAGE_PREFIX = 'https://www.tbs.co.jp/anime/5hanayome/'
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()
        self.download_bluray()
        self.download_bluray_bonus()

    def download_episode_preview(self):
        image_template = 'https://www.tbs.co.jp/anime/5hanayome/story/img/story%s/%s.jpg'
        try:
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_1'):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = image_template % (episode, str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1)
                    result = self.download_image(image_url, self.base_folder + '/' + image_name)
                    if result == -1:
                        return
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

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

    def download_bluray(self):
        folder = self.create_bluray_directory()
        self.image_list = []
        self.add_to_image_list('bd1_big', 'https://aniverse-mag.com/wp-content/uploads/2021/01/f52988a7c17bf03cfc9369cb7777b84d.jpg', to_jpg=True)
        #self.add_to_image_list('bd2_big', 'https://aniverse-mag.com/wp-content/uploads/2021/02/704f1147ac034226999fbead9d593edc.jpgg', to_jpg=True)
        self.add_to_image_list('bd2_big', 'https://pbs.twimg.com/media/Euj7GNJVgAMuDU2?format=jpg&name=large')
        self.add_to_image_list('game_music', 'https://pbs.twimg.com/media/Eujsxh9VgAQD_PZ?format=jpg&name=large')
        self.download_image_list(folder)
        try:
            urls = ['music']
            for i in range(5):
                urls.append('disc/disc' + str(i + 1).zfill(2) + '.html')
            for i in range(len(urls)):
                if i > 0 and self.is_image_exists('bd' + str(i), folder):
                    continue
                bd_url = self.PAGE_PREFIX + urls[i]
                soup = self.get_soup(bd_url, decode=True)
                divs = soup.find_all(lambda tag: tag.name == 'div' and tag.has_attr('class') and 'music-image' in tag['class'])
                self.image_list = []
                for div in divs:
                    image = div.find(lambda tag: tag.name == 'img' and (tag.has_attr('srcset') or tag.has_attr('src')))
                    if image:
                        if i == 0:
                            bd_prefix = self.PAGE_PREFIX + 'music/'
                        else:
                            bd_prefix = self.PAGE_PREFIX + 'disc/'
                        if image.has_attr('srcset'):
                            image_url = bd_prefix + image['srcset']
                        else:
                            image_url = bd_prefix + image['src']
                        if 'noimage' in image_url:
                            if i == 0:
                                continue
                            else:
                                return
                        if i == 0:
                            image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                        else:
                            image_name = 'bd' + str(i)
                        self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Blu-Ray')
            print(e)

    def download_bluray_bonus(self):
        folder = self.create_bluray_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'disc/oritoku.html', decode=True)
            images = soup.find_all(lambda tag: tag.name == 'img' and tag.has_attr('class') and 'oritoku-img' in tag['class']
                          and (tag.has_attr('src') or tag.has_attr('srcset')))
            self.image_list = []
            for image in images:
                if image.has_attr('srcset'):
                    image_url = self.PAGE_PREFIX + image['srcset']
                else:
                    image_url = self.PAGE_PREFIX + image['src']
                if 'noimage' in image_url:
                    continue
                image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Blu-Ray Bonus')
            print(e)


# Hataraku Saibou S2
class HatarakuSaibou2Download(Winter2021AnimeDownload):
    title = "Hataraku Saibou!!"
    keywords = [title, "Cells at Work!", "2nd Season"]
    folder_name = "hataraku-saibou2"

    PAGE_PREFIX = 'https://hataraku-saibou.com/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        try:
            story_url = self.PAGE_PREFIX + 'story/'
            soup = self.get_soup(story_url)
            tab = soup.find('div', class_='page_tab')
            if not tab:
                return
            ul = tab.find('ul')
            if ul:
                a_tags = ul.find_all('a')
                for a_tag in a_tags:
                    if a_tag.has_attr('href') and 'id=' in a_tag['href']:
                        try:
                            episode = str(int(a_tag.text)).zfill(2)
                        except:
                            continue
                        if self.is_image_exists(episode + '_1'):
                            continue
                        episode_url = story_url + a_tag['href'].replace('./', '')
                        episode_soup = self.get_soup(episode_url)
                        div_image = episode_soup.find('div', class_='s_image')
                        if div_image:
                            images = div_image.find_all('img')
                            self.image_list = []
                            for i in range(len(images)):
                                if images[i].has_attr('src'):
                                    image_url = story_url + images[i]['src']
                                    image_name = episode + '_' + str(i + 1)
                                    self.add_to_image_list(image_name, image_url)
                            self.download_image_list(self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

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
        try:
            story_url = self.PAGE_PREFIX + 'story/'
            soup = self.get_soup(story_url, decode=True)
            tab = soup.find('div', class_='page_tab')
            if not tab:
                return
            ul = tab.find('ul')
            if ul:
                a_tags = ul.find_all('a')
                for a_tag in a_tags:
                    if a_tag.has_attr('href') and 'id=' in a_tag['href']:
                        try:
                            a_text = a_tag.text.strip().replace('第', '').replace('話', '')
                            episode = str(int(a_text)).zfill(2)
                        except:
                            continue
                        if self.is_image_exists(episode + '_1'):
                            continue
                        episode_url = story_url + a_tag['href'].replace('./', '')
                        episode_soup = self.get_soup(episode_url)
                        div_image = episode_soup.find('div', class_='p-story__img-swiper')
                        if div_image:
                            images = div_image.find_all('img')
                            self.image_list = []
                            for i in range(len(images)):
                                if images[i].has_attr('src'):
                                    image_url = story_url + images[i]['src']
                                    image_name = episode + '_' + str(i + 1)
                                    self.add_to_image_list(image_name, image_url)
                            self.download_image_list(self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

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
        self.download_bluray()

    def download_episode_preview(self):
        try:
            story_url = self.PAGE_PREFIX + 'story/'
            soup = self.get_soup(story_url, decode=True)
            ul = soup.find('ul', class_='nav-story_list')
            if ul:
                lis = ul.find_all('li')
                for li in lis:
                    span = li.find('span')
                    a_tag = li.find('a')
                    if not span and not a_tag:
                        continue
                    if a_tag.has_attr('href') and 'id=' in a_tag['href']:
                        try:
                            episode = str(int(span.text.strip())).zfill(2)
                        except:
                            continue
                        if self.is_image_exists(episode + '_1'):
                            continue
                        if len(a_tag['href'][0]) > 1 and a_tag['href'][0] == '/':
                            episode_url = self.PAGE_PREFIX + a_tag['href'][1:]
                        else:
                            episode_url = self.PAGE_PREFIX + a_tag['href']
                        episode_soup = self.get_soup(episode_url)
                        items = episode_soup.find_all('li', class_='p-story__scene-item')
                        self.image_list = []
                        for i in range(len(items)):
                            image = items[i].find('img')
                            if image and image.has_attr('src'):
                                image_url = story_url + image['src']
                                image_name = episode + '_' + str(i + 1)
                                self.add_to_image_list(image_name, image_url)
                        self.download_image_list(self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'kv1_1', 'url': 'https://pbs.twimg.com/media/EiH_LNCU8AM5msx?format=png&name=900x900'},
            {'name': 'kv1_2', 'url': self.PAGE_PREFIX + 'teaser/img/top/main/img_main.jpg'},
            {'name': 'kv2', 'url': self.PAGE_PREFIX + 'assets/img/top/main/img_main.jpg'},
            {'name': 'kv3', 'url': self.PAGE_PREFIX + 'assets/img/top/main/img_main02.jpg'},
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

    def download_bluray(self):
        folder = self.create_bluray_directory()
        self.image_list = []
        self.add_to_image_list('music_ed', 'https://pbs.twimg.com/media/ErR1scoVEAM0pVu?format=jpg&name=large')
        self.add_to_image_list('bd7_bonus', 'https://pbs.twimg.com/media/EuHiHw5UcA4qJwt?format=jpg&name=medium')
        b1_ids = [1] + [i for i in range(931, 935, 1)]
        j = 0
        for i in b1_ids:
            image_url = MocaNewsDownload.generate_image_url('2021011001000a_', i)
            if i == 1:
                self.add_to_image_list('bd1', image_url, is_mocanews=True)
            else:
                j += 1
                self.add_to_image_list('bd_bonus' + str(j), image_url, is_mocanews=True)
        self.add_to_image_list('bd2', 'https://pbs.twimg.com/media/EulEYB8VgAMh7Eb?format=jpg&name=medium')
        self.download_image_list(folder)


# Jaku-Chara Tomozaki-kun
class TomozakiKunDownload(Winter2021AnimeDownload):
    title = "Jaku-Chara Tomozaki-kun"
    keywords = [title, 'The Low Tier Character "Tomozaki-kun"', 'Tomozaki-kun']
    folder_name = 'tomozakikun'

    PAGE_PREFIX = 'http://tomozaki-koushiki.com/'
    FINAL_EPISODE = 12

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
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            story_boxes = soup.find_all('div', class_='storyBox')
            for story_box in story_boxes:
                if story_box.has_attr('id') and 'story' in story_box['id'] and '_box' in story_box['id']:
                    try:
                        episode = str(int(story_box['id'].split('_box')[0].split('story')[1])).zfill(2)
                    except:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    img_list = story_box.find('ul', 'imgList')
                    if img_list:
                        images = img_list.find_all('img')
                        self.image_list = []
                        for i in range(len(images)):
                            if images[i].has_attr('src'):
                                image_url = self.PAGE_PREFIX + images[i]['src'].replace('../', '')
                                image_name = episode + '_' + str(i + 1)
                                self.add_to_image_list(image_name, image_url)
                        self.download_image_list(self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_episode_preview_external(self):
        jp_title = '弱キャラ友崎くん'
        last_date = datetime.strptime('20210330', '%Y%m%d')
        today = datetime.today()
        if today < last_date:
            end_date = today
        else:
            end_date = last_date
        MocaNewsScanner(jp_title, self.base_folder, '20201225', end_date.strftime('%Y%m%d')).run()
        NatalieScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE).run()

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'announce', 'url': 'https://pbs.twimg.com/media/EToARdRU0AACyGk?format=jpg&name=large'},
            {'name': 'kv1', 'url': 'http://tomozaki-koushiki.com/news/wp-content/uploads/2020/09/キービジュアル.jpg'},
            {'name': 'kv2', 'url': 'https://pbs.twimg.com/media/EmCdhd0VoAE8-n5?format=jpg&name=4096x4096'},
        ]
        self.download_image_objects(image_objs, folder)

    def download_character(self):
        folder = self.create_character_directory()
        image_url_1 = self.PAGE_PREFIX + 'img/character/chara%s_img.png'
        image_url_2 = self.PAGE_PREFIX + 'img/character/chara%s_name.png'
        for i in range(20):
            url_1 = image_url_1 % str(i + 1)
            if not self.is_valid_url(url_1, is_image=True):
                break
            url_2 = image_url_2 % str(i + 1)
            name_1 = self.extract_image_name_from_url(url_1, with_extension=False)
            name_2 = self.extract_image_name_from_url(url_2, with_extension=False)
            self.add_to_image_list(name_1, url_1)
            self.add_to_image_list(name_2, url_2)
        self.download_image_list(folder)

    def download_bluray(self):
        folder = self.create_bluray_directory()
        self.image_list = []
        self.add_to_image_list('bd_tw_1_1', 'https://pbs.twimg.com/media/EqDDs1iVgAANXji?format=jpg&name=large')
        self.add_to_image_list('bd_tw_1_2', 'https://pbs.twimg.com/media/EqDDtt9UwAA4Rld?format=jpg&name=large')
        self.add_to_image_list('bd_vol_1_bonus', 'https://pbs.twimg.com/media/ErMwxwrVEAAQ9vU?format=jpg&name=4096x4096')
        #self.add_to_image_list('bd_vol_1_bonus', 'http://tomozaki-koushiki.com/news/wp-content/uploads/2021/01/ブルーレイ特典画像_.jpg')
        self.add_to_image_list('music_op', 'https://pbs.twimg.com/media/Eprwl4IVEAIIb14?format=jpg&name=medium')
        self.add_to_image_list('music_ed', 'https://pbs.twimg.com/media/Eprwl4HVQAEWDX6?format=jpg&name=medium')
        self.download_image_list(folder)
        self.download_bluray_volume(folder)
        self.download_bluray_bonus(folder)

    def download_bluray_volume(self, folder):
        try:
            bddvd_url = self.PAGE_PREFIX + 'bddvd/'
            soup = self.get_soup(bddvd_url)
            item_list = soup.find('ul', class_='itemList')
            if item_list:
                a_tags = item_list.find_all('a')
                for a_tag in a_tags:
                    if a_tag.has_attr('href'):
                        if a_tag['href'] == 'shop.php':
                            continue
                        volume = a_tag['href'].replace('vol', '').split('.php')[0]
                        if self.is_image_exists('bd' + volume, folder):
                            continue
                        img = a_tag.find('img')
                        if img and img.has_attr('src'):
                            if 'nowprinting' in img['src']:
                                continue
                            if len(volume) != 1:
                                continue
                            bd_url = bddvd_url + a_tag['href']
                            bd_soup = self.get_soup(bd_url)
                            imglist = bd_soup.find('div', class_='box_imgList')
                            if imglist:
                                img_list = imglist.find_all('img')
                                self.image_list = []
                                for i in range(len(img_list)):
                                    if img_list[i].has_attr('src'):
                                        if 'nowprinting' in img_list[i]['src']:
                                            continue
                                        image_url = self.PAGE_PREFIX + img_list[i]['src'].replace('../', '')
                                        if self.is_matching_content_length(image_url, 9318):
                                            continue
                                        if i == 0:
                                            image_name = 'bd' + volume
                                        else:
                                            image_name = 'bd' + volume + '_' + str(i)
                                        self.add_to_image_list(image_name, image_url)
                                self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Blu-ray")
            print(e)

    def download_bluray_bonus(self, folder):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bddvd/shop.php')
            img_divs = soup.find_all('div', class_='shop_img')
            self.image_list = []
            for img_div in img_divs:
                image = img_div.find('img')
                if image and image.has_attr('src'):
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                    image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Blu-ray Bonus")
            print(e)


# Kaifuku Jutsushi no Yarinaoshi
class KaiyariDownload(Winter2021AnimeDownload):
    title = "Kaifuku Jutsushi no Yarinaoshi"
    keywords = [title, "Kaiyari", "Redo of Healer"]
    folder_name = 'kaiyari'

    PAGE_PREFIX = "http://kaiyari.com/"
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()
        self.download_bluray()

    def download_episode_preview(self):
        image_template = self.PAGE_PREFIX + 'assets/story/%s_%s.jpg'
        try:
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_1'):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = image_template % (str(i + 1), str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    result = self.download_image(image_url, self.base_folder + '/' + image_name)
                    if result == -1:
                        return
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

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

    def download_bluray(self):
        folder = self.create_bluray_directory()
        self.image_list = []
        self.add_to_image_list('music_op', 'http://kaiyari.com/assets/music/op.jpg')
        self.add_to_image_list('music_ed', 'http://kaiyari.com/assets/music/ed.jpg')
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bddvd.html')
            articles = soup.find_all('article')
            for article in articles:
                if article.has_attr('id'):
                    id = article['id']
                    if len(id) == 0:
                        id = 'Bnf'
                else:
                    continue
                images = article.find_all('img')
                for image in images:
                    if image.has_attr('src'):
                        image_url = self.PAGE_PREFIX + image['src'].replace('./', '').split('?')[0]
                        if len(image_url) > 6 and image_url[-6:] == 'np.png':
                            continue
                        image_name = id + '_' + self.extract_image_name_from_url(image_url, with_extension=False)
                        self.add_to_image_list(image_name, image_url)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Blu-Ray")
            print(e)
        self.download_image_list(folder)


# Kemono Jihen
class KemonoJihenDownload(Winter2021AnimeDownload):
    title = "Kemono Jihen"
    keywords = [title, 'Kemonojihen']
    folder_name = 'kemonojihen'

    PAGE_PREFIX = 'https://kemonojihen-anime.com/'
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        template = 'https://kemonojihen-anime.com/story/img/%s/%s_%s.jpg'
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            first_image_url = template % (episode, episode, '01')
            if not self.is_valid_url(first_image_url, is_image=True):
                break
            self.image_list = []
            for j in range(self.IMAGES_PER_EPISODE):
                image_url = template % (episode, episode, str(j + 1).zfill(2))
                image_name = episode + '_' + str(j + 1)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(self.base_folder)

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
    FINAL_EPISODE = 24
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        image_template = self.PAGE_PREFIX + 'assets/story/%s_%s.jpg'
        try:
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_1'):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = image_template % (str(i + 1), str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    result = self.download_image(image_url, self.base_folder + '/' + image_name)
                    if result == -1:
                        return
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('top-main', 'https://kumo-anime.com/teaser/images/top-main.jpg')
        self.add_to_image_list('top-main2', 'https://kumo-anime.com/teaser/images/top-main2.jpg')
        self.add_to_image_list('kv0', 'https://kumo-anime.com/assets/news/kv0.jpg')
        self.add_to_image_list('kv1', 'https://kumo-anime.com/assets/news/kv1.jpg')
        self.add_to_image_list('kv2', 'https://kumo-anime.com/assets/news/kv2.jpg')
        self.add_to_image_list('kv2_visr', 'https://kumo-anime.com/assets/top/kv2/visr.jpg')
        self.add_to_image_list('kv2_visr2', 'https://kumo-anime.com/assets/top/kv2/visr2.jpg')
        self.download_image_list(folder)


# Log Horizon: Entaku Houkai
class LogHorizon3Download(Winter2021AnimeDownload):
    title = "Log Horizon: Entaku Houkai"
    keywords = [title, '3rd Season']
    folder_name = 'loghorizon3'

    MAIN_PAGE = 'https://www6.nhk.or.jp/anime/program/detail.html?i=loghorizon3'
    IMAGE_PREFIX = 'https://www6.nhk.or.jp/anime/program/common/images/loghorizon3/'
    FINAL_EPISODE = 12

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            image_url = self.IMAGE_PREFIX + 'story_' + episode + '.jpg'
            if self.is_valid_url(image_url):
                self.download_image(image_url, self.base_folder + '/' + episode + '_1')
            else:
                break

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('main', self.IMAGE_PREFIX + 'main.jpg')
        self.add_to_image_list('main2', self.IMAGE_PREFIX + 'main2.jpg')
        self.download_image_list(folder)


# Mushoku Tensei: Isekai Ittara Honki Dasu
class MushokuTenseiDownload(Winter2021AnimeDownload):
    title = "Mushoku Tensei: Isekai Ittara Honki Dasu"
    keywords = [title, 'Jobless Reincarnation']
    folder_name = 'mushoku-tensei'

    PAGE_PREFIX = 'https://mushokutensei.jp'
    FINAL_EPISODE = 23
    IMAGES_PER_EPISODE = 5

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_guess()
        self.download_key_visual()
        self.download_character()
        self.download_bluray()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + '/story/')
            ul = soup.find('ul', id='js_story')
            if not ul:
                return
            a_tags = ul.find_all('a', class_='storyarea')
            for a_tag in a_tags:
                if not a_tag.has_attr('href'):
                    continue
                try:
                    episode = str(int(a_tag.find('div', class_='storyarea_ttl')
                                      .find('span').text.replace('#', '').strip())).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                episode_url = a_tag['href']
                episode_soup = self.get_soup(episode_url)
                images = episode_soup.find_all('div', class_='storycontents_subimg_img')
                self.image_list = []
                for i in range(len(images)):
                    if images[i].has_attr('data-imgload'):
                        image_name = episode + '_' + str(i + 1)
                        image_url = images[i]['data-imgload']
                        self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        template_base = self.PAGE_PREFIX + '/wp-content/uploads/2021/%s/'
        template_first = template_base + 'img_story%s.jpg'
        template = template_base + 'MusyokuTensei_ep%s_%s.jpg'
        template_r = template_base + 'MusyokuTensei_ep%s_r_%s.jpg'
        dt_month = datetime.now().strftime("%m").zfill(2)

        template_first_2 = template_base + 'メイン%s.jpg'
        for i in range(20):
            if i == 0:
                image_url = template_first_2 % (dt_month, '')
            else:
                image_url = template_first_2 % (dt_month, '-' + str(i))
            image_name = 'main_' + dt_month + '_' + str(i)
            if self.is_image_exists(image_name, folder):
                continue
            if self.is_valid_url(image_url, is_image=True):
                self.download_image(image_url, folder + '/' + image_name)
            else:
                break

        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            j = 0
            is_success = False
            first_image_url = template_first % (dt_month, episode)
            if self.is_valid_url(first_image_url, is_image=True):
                j += 1
                image_name = self.extract_image_name_from_url(first_image_url, with_extension=False)
                result = self.download_image(first_image_url, folder + '/' + image_name)
                if result == 0:
                    is_success = True
                    print(self.__class__.__name__ + ' - Guessed successfully!')

            for k in range(201):
                if j > self.IMAGES_PER_EPISODE or (j == 0 and k > 50):
                    break
                for template_ in [template, template_r]:
                    image_url = template_ % (dt_month, episode, str(k).zfill(4))
                    if self.is_valid_url(image_url, is_image=True):
                        j += 1
                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                        result = self.download_image(image_url, folder + '/' + image_name)
                        if result == 0:
                            is_success = True
                            print(self.__class__.__name__ + ' - Guessed successfully!')
            if not is_success:
                if len(os.listdir(folder)) == 0:
                    os.rmdir(folder)
                return
        if len(os.listdir(folder)) == 0:
            os.rmdir(folder)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'teaser', 'url': 'https://pbs.twimg.com/media/EHKOHakU4AUq-A3?format=jpg&name=large'},
            {'name': 'kv1', 'url': 'https://pbs.twimg.com/media/Ea3MiJFU0AETcOY?format=jpg&name=4096x4096'},
            {'name': 'kv2', 'url': self.PAGE_PREFIX + '/wp-content/themes/mushoku_re/img/index/img_hero01.jpg'},
            {'name': 'bs11_poster', 'url': 'https://pbs.twimg.com/media/Ep9v3c4U8AISWC6?format=jpg&name=medium'},
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
            soup = self.get_soup(self.PAGE_PREFIX + '/character/')
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
            soup = self.get_soup(self.PAGE_PREFIX + '/bluray/')
            a_tags = soup.find_all('a', class_='bluraylist')
            for i in range(len(a_tags)):
                if not a_tags[i].has_attr('href'):
                    continue
                # Always evaluate the first volume's page to check for Blu-ray Bonus Illustrations
                if i > 0:
                    img = a_tags[i].find('div', class_='bluraylist_img')
                    if img is None or not img.has_attr('data-imgload'):
                        continue
                    if 'printing' in img['data-imgload']:
                        continue
                    if str(i + 1) in processed:
                        continue
                bd_soup = self.get_soup(a_tags[i]['href'])
                content = bd_soup.find('div', class_='content')
                if content:
                    images = content.find_all('img')
                    self.image_list = []
                    for image in images:
                        if image.has_attr('src'):
                            image_url = image['src']
                            if len(image_url) > 4 and ('printing' in image_url or '.svg' in image_url[-4:]):
                                continue
                            image_url = self.clear_resize_in_url(image_url.split('?')[0])
                            image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                            self.add_to_image_list(image_name, image_url)
                    self.download_image_list(folder)
                    if i > 0:
                        processed.append(str(i + 1))
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Blu-Ray")
            print(e)

        if len(processed) > num_processed:
            with open(cache_filepath, 'w+') as f:
                for i in range(len(processed)):
                    if i > 0:
                        f.write(';')
                    f.write(processed[i])


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
        self.download_bluray()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + '/tvanime/story/')
            a_tags = soup.find_all(lambda tag: tag.name == 'a' and tag.has_attr('href')
                and tag.has_attr('class') and 'story__nav__page__item' in tag['class'])
            for a_tag in a_tags:
                try:
                    episode = str(int(a_tag.find('span').text.split('#')[1].strip())).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                ep_url = self.PAGE_PREFIX + a_tag['href']
                ep_soup = self.get_soup(ep_url)
                ul = ep_soup.find('ul', class_='slider__pic')
                if ul:
                    images = ul.find_all(lambda tag: tag.name == 'img' and tag.has_attr('src'))
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = self.PAGE_PREFIX + images[i]['src']
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        key_visual_url = self.PAGE_PREFIX + '/tvanime/wp-content/themes/nonnon_tvanime/assets/img/page/top/v%s/mainvisual.%s'
        image_objs = []
        for i in range(1, 5, 1):
            j = 'jpg'
            if i == 4:
                j = 'png'
            image_objs.append({'name': 'kv' + str(i), 'url': key_visual_url % (str(i), j)})
        image_objs.append({'name': 'newyear_2021', 'url': 'https://pbs.twimg.com/media/EqkuXFXVkAEv1Oq?format=jpg&name=medium'})
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

    def download_bluray(self):
        folder = self.create_bluray_directory()
        self.image_list = []
        self.add_to_image_list('music_jkt', 'http://nanoripe.com/nanoripe/wp-content/uploads/2021/01/nonnon_days_H1_RGB_Shikaku.jpg')
        self.download_image_list(folder)


# Ore dake Haireru Kakushi Dungeon
class KakushiDungeonDownload(Winter2021AnimeDownload):
    title = "Ore dake Haireru Kakushi Dungeon"
    keywords = [title, "The Hidden Dungeon Only I Can Enter"]
    folder_name = 'kakushi-dungeon'

    PAGE_PREFIX = 'https://kakushidungeon-anime.jp/'
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()
        self.download_bluray()
        self.download_endcard()

    def download_episode_preview(self):
        image_template = 'https://kakushidungeon-anime.jp/assets/story/%s_%s.jpg'
        try:
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_1'):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = image_template % (str(i + 1), str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    result = self.download_image(image_url, self.base_folder + '/' + image_name)
                    if result == -1:
                        return
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

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

    def download_bluray(self):
        folder = self.create_bluray_directory()
        self.image_list = []
        self.add_to_image_list('music_ed', 'https://pbs.twimg.com/media/EsUxe--UwAAuYHv?format=jpg&name=medium')
        try:
            for i in ['index', 'music']:
                soup = self.get_soup(self.PAGE_PREFIX + 'bdcd/%s.html' % i)
                articles = soup.find_all('article', class_='content-single')
                for article in articles:
                    if article.has_attr('id'):
                        prefix = article['id'].strip() + '_'
                    else:
                        prefix = ''
                    images = article.find_all('img')
                    for image in images:
                        if image.has_attr('src'):
                            if 'bdcd-cmt-ic.png' in image['src']:
                                continue
                            image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                            image_name = prefix + self.extract_image_name_from_url(image_url, with_extension=False)
                            self.add_to_image_list(image_name, image_url)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Bluray")
            print(e)
        self.download_image_list(folder)

    def download_endcard(self):
        folder = self.create_custom_directory(constants.FOLDER_ENDCARD)
        self.image_list = []
        self.add_to_image_list('ec01', 'https://pbs.twimg.com/media/ErNZmC3U0AIfXT1?format=jpg&name=large')
        self.add_to_image_list('ec02', 'https://pbs.twimg.com/media/Ern5IxeVEAArIgY?format=jpg&name=large')
        self.add_to_image_list('ec03', 'https://pbs.twimg.com/media/Er1akPIVEAEFH2C?format=jpg&name=medium')
        self.add_to_image_list('ec04', 'https://pbs.twimg.com/media/EsQoJxuUYAIMZSi?format=jpg&name=large')
        self.add_to_image_list('ec05', 'https://pbs.twimg.com/media/EtSyGOqVEAQCbSq?format=jpg&name=large')
        self.add_to_image_list('ec06', 'https://pbs.twimg.com/media/EtxigFXVEAIpeHs?format=jpg&name=large')
        self.add_to_image_list('ec07', 'https://pbs.twimg.com/media/EuVJhvlU4AI4xmo?format=jpg&name=large')
        self.download_image_list(folder)


# Tatoeba Last Dungeon Mae no Mura no Shounen ga Joban no Machi de Kurasu Youna Monogatari
class LasdanDownload(Winter2021AnimeDownload):
    title = "Tatoeba Last Dungeon Mae no Mura no Shounen ga Joban no Machi de Kurasu Youna Monogatari"
    keywords = [title, "Lasdan"]
    folder_name = 'lasdan'

    PAGE_PREFIX = 'https://lasdan.com/'
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_guess()
        self.download_key_visual()
        self.download_character()
        self.download_bluray()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/', decode=True)
            episode_list = soup.find('div', id='ContentsListUnit02')
            if episode_list:
                a_tags = episode_list.find_all('a')
                for a_tag in a_tags:
                    if a_tag.has_attr('href'):
                        a_tag_text = a_tag.text.strip().replace(' ', '')
                        if len(a_tag_text) > 2 and '第' in a_tag_text[0] and '話' in a_tag_text[-1]:
                            try:
                                episode = str(int(a_tag_text.split('第')[1].split('話')[0])).zfill(2)
                            except:
                                continue
                            url = self.PAGE_PREFIX + a_tag['href'].replace('../', '')
                            ep_soup = self.get_soup(url)
                            ph_divs = ep_soup.find_all('div', class_='ph')
                            self.image_list = []
                            for i in range(len(ph_divs)):
                                image = ph_divs[i].find('a')
                                if image and image.has_attr('href'):
                                    image_url = self.PAGE_PREFIX + image['href'].replace('../', '').split('?')[0]
                                    image_name = episode + '_' + str(i + 1)
                                    self.add_to_image_list(image_name, image_url)
                            self.download_image_list(self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'core_sys/images/contents/%s/block/%s/%s.jpg'
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            is_success = False
            if self.is_image_exists(episode + '_1'):
                continue
            first = 22 + i
            second = 35 + 3 * i
            third = 49 + self.IMAGES_PER_EPISODE * i
            for j in range(self.IMAGES_PER_EPISODE):
                image_url = template % (str(first).zfill(8), str(second).zfill(8), str(third + j).zfill(8))
                image_name = episode + '_' + str(j + 1)
                result = self.download_image(image_url, folder + '/' + image_name)
                if result == 0:
                    print(self.__class__.__name__ + ' - Guessed successfully!')
                    is_success = True
            if not is_success:
                if len(os.listdir(folder)) == 0:
                    os.rmdir(folder)
                return
        if len(os.listdir(folder)) == 0:
            os.rmdir(folder)

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

    def download_bluray(self):
        folder = self.create_bluray_directory()
        self.image_list = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bd')
            list_div = soup.find('div', id='list_05')
            if list_div:
                sm_divs = list_div.find_all('div', class_='sm')
                for sm_div in sm_divs:
                    a_tag = sm_div.find('a')
                    if a_tag and a_tag.has_attr('href'):
                        image = a_tag.find('img')
                        if image and image.has_attr('src'):
                            image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                            if self.is_matching_content_length(image_url, 568871):
                                continue
                            a_url = self.PAGE_PREFIX + a_tag['href'].replace('../', '')
                            try:
                                volume = str(int(a_url.split('/')[-1].split('.html')[0]))
                            except:
                                continue
                            bd_filename = 'bd' + volume
                            if self.is_image_exists(bd_filename, folder):
                                continue
                            a_soup = self.get_soup(a_url)
                            cms_div = a_soup.find('div', id='cms_block')
                            if cms_div:
                                bd_images = cms_div.find_all('img')
                                for i in range(len(bd_images)):
                                    if bd_images[i].has_attr('src'):
                                        bd_image_url = self.PAGE_PREFIX + bd_images[i]['src'].replace('../', '').replace('/sn_', '/').split('?')[0]
                                        bd_image_name = bd_filename
                                        if i > 0:
                                            bd_image_name = bd_image_name + '_' + str(i)
                                        self.add_to_image_list(bd_image_name, bd_image_url)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Blu-Ray')
            print(e)
        self.download_image_list(folder)

        self.image_list = []
        self.add_to_image_list('bd_bonus1', 'https://pbs.twimg.com/media/Eq5OKyVVkAApAsg?format=jpg&name=large')
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bd/tokuten.html')
            cms_div = soup.find('div', id='cms_block')
            if cms_div:
                images = cms_div.find_all('img')
                for image in images:
                    if image.has_attr('src'):
                        image_url = self.PAGE_PREFIX + image['src'].replace('../', '').replace('/sn_', '/').split('?')[0]
                        if self.is_matching_content_length(image_url, 568871):
                            continue
                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                        self.add_to_image_list(image_name, image_url)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Blu-Ray Bonus')
            print(e)
        self.download_image_list(folder)

        music_url_template = 'https://lasdan.com/core_sys/images/contents/000000%s/block/000000%s/000000%s.jpg'
        self.image_list = []
        for i in range(43, 48, 1):
            j = 1 if i > 45 else 0
            music_url = music_url_template % (str(15 - j), str(29 + j), str(i))
            if not self.is_matching_content_length(music_url, 126468):
                self.add_to_image_list(self.extract_image_name_from_url(music_url, with_extension=False), music_url)
        self.download_image_list(folder)


# Tensei shitara Slime Datta Ken S2
class Tensura2Download(Winter2021AnimeDownload):
    title = 'Tensei shitara Slime Datta Ken 2nd Season'
    keywords = [title, "Tensura", "That Time I Got Reincarnated as a Slime"]
    folder_name = 'tensura2'

    PAGE_PREFIX = 'https://www.ten-sura.com/anime/tensura'
    FIRST_EPISODE = 25
    FINAL_EPISODE = 48
    IMAGES_PER_EPISODE = 5

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_episode_preview_guess()
        self.download_key_visual()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + '/intro/2nd')
            nav_list = soup.find_all('ul', class_='nav-list')
            if len(nav_list) < 2:
                return
            lis = nav_list[1].find_all('li', class_='nav-list-item')
            for li in lis:
                if li.has_attr('data-season') and li['data-season'] == '2':
                    a_tag = li.find('a')
                    if a_tag.has_attr('href'):
                        try:
                            episode = str(int(a_tag.text.replace('#', '').strip()))
                        except:
                            continue
                        ep_soup = self.get_soup(a_tag['href'])
                        slider_wrapper = ep_soup.find('div', class_='swiper-wrapper')
                        if slider_wrapper:
                            images = slider_wrapper.find_all('img')
                            self.image_list = []
                            for i in range(len(images)):
                                if images[i].has_attr('src'):
                                    image_url = images[i]['src']
                                    image_name = episode + '_' + str(i + 1)
                                    self.add_to_image_list(image_name, image_url)
                            self.download_image_list(self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        template = 'https://www.ten-sura.com/4GfGdAp7/wp-content/themes/tensura_portal/anime/tensura-portal-anime-tensura/assets/images/story/no%s/img%s.jpg'
        for i in range(self.FIRST_EPISODE, self.FINAL_EPISODE + 1, 1):
            episode = str(i).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            is_success = False
            image_url = template % (str(i + 2).zfill(2), '1')
            if self.is_valid_url(image_url, is_image=True):
                for k in range(self.IMAGES_PER_EPISODE):
                    valid_image_url = template % (str(i + 2).zfill(2), str(k + 1))
                    image_name = episode + '_' + str(k + 1)
                    result = self.download_image(valid_image_url, folder + '/' + image_name)
                    if result == 0:
                        is_success = True
                        print(self.__class__.__name__ + ' - Guessed successfully!')
            if not is_success:
                if len(os.listdir(folder)) == 0:
                    os.rmdir(folder)
                return
        if len(os.listdir(folder)) == 0:
            os.rmdir(folder)

    def download_episode_preview_external(self):
        jp_title = '転生したらスライムだった件'
        WebNewtypeScanner('転生したらスライムだった件', self.base_folder, last_episode=48, first_episode=25).run()
        #AniverseMagazineScanner(jp_title, self.base_folder, last_episode=48, min_width=1000, end_date='20210108').run()

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv1', 'https://www.ten-sura.com/4GfGdAp7/wp-content/themes/tensura_portal/anime/tensura-portal-anime-tensura/assets/images/kv.jpg')
        self.add_to_image_list('kv2', 'https://www.ten-sura.com/4GfGdAp7/wp-content/themes/tensura_portal/anime/tensura-portal-anime-tensura/assets/images/kv_2.jpg')
        self.add_to_image_list('newyear_2021', 'https://www.ten-sura.com/4GfGdAp7/wp-content/themes/tensura_portal/assets/images/2021_new.jpg')
        self.download_image_list(folder)


# Urasekai Picnic
class UrasekaiPicnicDownload(Winter2021AnimeDownload):
    title = 'Urasekai Picnic'
    keywords = [title, 'Otherside Picnic']
    folder_name = 'urasekai-picnic'

    PAGE_PREFIX = 'https://www.othersidepicnic.com'
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_episode_preview_guess()
        self.download_key_visual()
        self.download_character()
        self.download_bluray()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + '/story/')
            nav = soup.find('nav', id='l-nav')
            if nav:
                a_tags = nav.find_all('a')
                for a_tag in a_tags:
                    if a_tag.has_attr('href'):
                        try:
                            episode = str(int(a_tag.text.strip())).zfill(2)
                        except:
                            continue
                        if self.is_image_exists(episode + '_1'):
                            continue
                        url = self.PAGE_PREFIX + '/' + a_tag['href']
                        story_soup = self.get_soup(url)
                        slider = story_soup.find('ul', class_='slider')
                        if slider:
                            images = slider.find_all('img')
                            self.image_list = []
                            for i in range(len(images)):
                                if images[i].has_attr('src'):
                                    image_url = images[i]['src'].replace('-1024x576', '')
                                    image_name = episode + '_' + str(i + 1)
                                    self.add_to_image_list(image_name, image_url)
                            self.download_image_list(self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_episode_preview_external(self):
        NatalieScanner('裏世界ピクニック', self.base_folder, last_episode=self.FINAL_EPISODE).run()

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + '/cms/wp-content/uploads/2021/%s/%s_%s.jpg'
        template2 = self.PAGE_PREFIX + '/cms/wp-content/uploads/2021/%s/ep%s_%s.jpg'
        dt_month = datetime.now().strftime("%m").zfill(2)
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            is_success = False
            for j in [template, template2]:
                image_url = j % (dt_month, episode, '01')
                if self.is_valid_url(image_url, is_image=True):
                    for k in range(self.IMAGES_PER_EPISODE):
                        valid_image_url = j % (dt_month, episode, str(k + 1).zfill(2))
                        image_name = episode + '_' + str(k + 1)
                        result = self.download_image(valid_image_url, folder + '/' + image_name)
                        if result == 0:
                            is_success = True
                            print(self.__class__.__name__ + ' - Guessed successfully!')
            if not is_success:
                if len(os.listdir(folder)) == 0:
                    os.rmdir(folder)
                return
        if len(os.listdir(folder)) == 0:
            os.rmdir(folder)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        template = self.PAGE_PREFIX + '/cms/wp-content/themes/othersidepicnic/images/home/%s'
        self.image_list = []
        self.add_to_image_list('kv1', template % 'kv.jpg')
        self.add_to_image_list('kv2', template % 'key-visual.jpg')
        self.add_to_image_list('kv3', template % 'key-visual_20200104_.jpg')
        self.download_image_list(folder)

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

    def download_bluray(self):
        folder = self.create_bluray_directory()
        self.image_list = []
        self.add_to_image_list('music_op', 'https://pbs.twimg.com/media/Eq4iEpWVgAI_0oq?format=jpg&name=large')
        self.download_image_list(folder)


# Wonder Egg Priority
class WonderEggPriorityDownload(Winter2021AnimeDownload):
    title = 'Wonder Egg Priority'
    keywords = [title]
    folder_name = 'wonder-egg-priority'

    PAGE_PREFIX = 'https://wonder-egg-priority.com'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()
        self.download_bluray()

    def download_episode_preview(self):
        try:
            story_url = self.PAGE_PREFIX + '/story/'
            soup = self.get_soup(story_url)
            ul = soup.find('ul', class_='story-navs')
            if ul:
                a_tags = ul.find_all('a')
                for a_tag in a_tags:
                    if a_tag.has_attr('href') and 'id=' in a_tag['href']:
                        try:
                            episode = str(int(a_tag.text)).zfill(2)
                        except:
                            continue
                        if self.is_image_exists(episode + '_1'):
                            continue
                        episode_url = self.PAGE_PREFIX + a_tag['href']
                        episode_soup = self.get_soup(episode_url)
                        div_image = episode_soup.find('div', class_='story-images')
                        if div_image:
                            images = div_image.find_all('img')
                            self.image_list = []
                            for i in range(len(images)):
                                if images[i].has_attr('src'):
                                    image_url = story_url + images[i]['src']
                                    image_name = episode + '_' + str(i + 1)
                                    self.add_to_image_list(image_name, image_url)
                            self.download_image_list(self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/Ej1EFuKUwAACTDb?format=jpg&name=4096x4096')
        self.add_to_image_list('kv1', 'https://wonder-egg-priority.com/assets/img/top/main/visual.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + '/character/')
            chara_items = soup.find_all('li', class_='character__list__item')
            chara_names = []
            for chara_item in chara_items:
                a_tag = chara_item.find('a')
                if a_tag and a_tag.has_attr('href'):
                    split1 = a_tag['href'].split('/')
                    if len(split1) == 4:
                        chara_names.append(split1[2])
            self.image_list = []
            chara_url_template = self.PAGE_PREFIX + '/assets/img/character/%s/ph_main.png'
            for name in chara_names:
                self.add_to_image_list(name, chara_url_template % name)
            self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)

    def download_bluray(self):
        folder = self.create_bluray_directory()
        try:
            self.download_content(self.PAGE_PREFIX + '/assets/img/introduction/bgvideo_l.mp4',
                                  folder + '/bgvideo_l.mp4')
            soup = self.get_soup(self.PAGE_PREFIX + '/bddvd/')
            div = soup.find('div', class_='bddvd__main')
            if div:
                images = div.find_all('img')
                self.image_list = []
                for image in images:
                    if image.has_attr('src'):
                        image_url = self.PAGE_PREFIX + image['src']
                        if 'coming' in image_url:
                            continue
                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                        self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Blu-ray")
            print(e)


# World Trigger S2
class WorldTrigger2Download(Winter2021AnimeDownload):
    title = "World Trigger 2nd Season"
    keywords = [title]
    folder_name = 'world-trigger2'

    PAGE_PREFIX = 'http://www.toei-anim.co.jp/tv/wt/'
    FINAL_EPISODE = 24

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_episode_preview_external(self):
        jp_title = 'ワールドトリガー'
        NatalieScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE).run()


# Yuru Camp S2
class YuruCamp2Download(Winter2021AnimeDownload):
    title = "Yuru Camp 2nd Season"
    keywords = [title, 'Yurucamp']
    folder_name = 'yurucamp2'

    BASE_PREFIX = 'https://yurucamp.jp/'
    PAGE_PREFIX = BASE_PREFIX + 'second/'
    FINAL_EPISODE = 13
    IMAGES_PER_EPISODE = 8

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()
        self.download_bluray()

    def download_episode_preview(self):
        image_template = self.PAGE_PREFIX + 'images/episode/%s_%s.jpg'
        try:
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_1'):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = image_template % (episode, str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    result = self.download_image(image_url, self.base_folder + '/' + image_name)
                    if result == -1:
                        return
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        image_objs = [
            {'name': 'teaser1', 'url': 'https://pbs.twimg.com/media/ETy4ZCFUYAEXlLl?format=jpg&name=4096x4096'},
            {'name': 'teaser2', 'url': 'https://pbs.twimg.com/media/ETy4ZC0U4AAbSS_?format=jpg&name=4096x4096'},
            {'name': 'mv_l', 'url': self.PAGE_PREFIX + 'images/mv_l.jpg'},
            {'name': 'mv_r', 'url': self.PAGE_PREFIX + 'images/mv_r.jpg'},
            {'name': 'g_visual_01', 'url': self.PAGE_PREFIX + 'images/g_visual_01.jpg'},
            {'name': 'img_visual2', 'url': 'https://pbs.twimg.com/media/EjNUQLTU8AE0WWQ?format=jpg&name=4096x4096'},
            {'name': 'img_visual3', 'url': self.BASE_PREFIX + 'camping/content/uploads/2020/10/14e33f48d154e171f203f89674fa0b30.jpg'},
            {'name': 'img_visual4', 'url': self.BASE_PREFIX + 'camping/content/uploads/2020/10/159c0e04163a9fd00a97dd24c8843c00.jpg'},
            {'name': 'img_visual5', 'url': 'https://pbs.twimg.com/media/EsPghnxVQAMJ6nP?format=jpg&name=large'},
            {'name': 'g_visual_01', 'url': self.PAGE_PREFIX + 'images/g_visual_01.jpg'},
            {'name': 'nmv', 'url': 'https://pbs.twimg.com/media/Eo2Arj3U0AAEras?format=jpg&name=4096x4096'},
            #{'name': 'nmv', 'url': 'https://yurucamp.jp/second/images/nmv.jpg'},
            {'name': 'nmv1', 'url': self.PAGE_PREFIX + 'images/nmv1.jpg'},
            {'name': 'nmv2', 'url': self.PAGE_PREFIX + 'images/nmv2.jpg'},
        ]
        self.download_image_objects(image_objs, folder)
        try:
            image_name_template = 'wall%s'
            memorial_url_template = 'https://yurucamp.jp/second/images/download/' + image_name_template + '.jpg'
            i = 0
            while i < 100:
                i += 1
                image_name = image_name_template % str(i).zfill(2)
                if self.is_image_exists(image_name, folder):
                    continue
                image_url = memorial_url_template % str(i).zfill(2)
                if self.download_image(image_url, folder + '/' + image_name) == -1:
                    break
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Key Visual')
            print(e)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'images/chara%s_full.png'
        template2 = self.PAGE_PREFIX + 'images/chara%s_face%s.png'
        self.image_list = []
        for i in range(9):
            image_url = template % str(i + 1)
            image_name = self.extract_image_name_from_url(image_url, with_extension=False)
            self.add_to_image_list(image_name, image_url)
            if i < 5:
                for j in range(3):
                    image_url = template2 % (str(i + 1), str(j + 1))
                    image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                    self.add_to_image_list(image_name, image_url)
        self.download_image_list(folder)

    def download_bluray(self):
        folder = self.create_bluray_directory()
        self.image_list = []
        #self.add_to_image_list('music_op', 'https://pbs.twimg.com/media/Ep-m71UUUAEkLG5?format=jpg&name=small')
        #self.add_to_image_list('music_ed', 'https://pbs.twimg.com/media/Ep-PwosVoAIhGIn?format=jpg&name=medium')
        #self.add_to_image_list('music_ost', 'https://pbs.twimg.com/media/EuhD12dVoAM2qSe?format=jpg&name=large')
        self.add_to_image_list('music_op', 'https://images-na.ssl-images-amazon.com/images/I/91QzwEIKguL._AC_SL1500_.jpg')
        self.add_to_image_list('music_ed', 'https://images-na.ssl-images-amazon.com/images/I/81Ws%2Bmf25tL._AC_SL1500_.jpg')
        self.add_to_image_list('music_ost', self.BASE_PREFIX + 'camping/content/uploads/2021/02/yuru2ost_jak.jpg')
        self.download_image_list(folder)
        try:
            soup = self.get_soup('https://yurucamp.jp/news/information/6142')
            div = soup.find('div', class_='articlein')
            if div:
                images = div.find_all(lambda tag: tag.name == 'img' and tag.has_attr('src'))
                self.image_list = []
                for image in images:
                    image_url = self.clear_resize_in_url(image['src'])
                    image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Blu-Ray')
            print(e)
