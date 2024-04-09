from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2
from datetime import datetime, timedelta
from scan import AniverseMagazineScanner
from requests.exceptions import HTTPError
import json
import os
import time
import math

# Dekisokonai to Yobareta Motoeiyuu wa Jikka kara Tsuihou sareta node Sukikatte ni Ikiru Koto ni Shita https://dekisoko-anime.com/ #できそこ @dekisoko_pr
# Hananoi-kun to Koi no Yamai https://hananoikun-pr.com/ #花野井くんと恋の病 @hananoikun_pr
# Henjin no Salad Bowl https://www.tbs.co.jp/anime/hensara/ #変サラ @hensara_anime
# Hibike! Euphonium 3 https://anime-eupho.com/ #anime_eupho @anime_eupho
# Jii-san Baa-san Wakagaeru https://jisanbasan.com/ #じいさんばあさん若返る @jisanbasan_prj
# Kaijuu 8-gou https://kaiju-no8.net/ #怪獣８号 #KaijuNo8 @KaijuNo8_O
# Kami wa Game ni Ueteiru. https://godsgame-anime.com/ #神飢え #神飢えアニメ #kamiue @kami_to_game
# Kono Sekai wa Fukanzen Sugiru https://konofuka.com/ #このふか @konofuka_QA
# Kono Subarashii Sekai ni Shukufuku wo! 3 http://konosuba.com/3rd/ #konosuba #このすば @konosubaanime
# Lv2 kara Cheat datta Motoyuusha Kouho no Mattari Isekai Life https://lv2-cheat.com/ #Lv2チート @Lv2cheat_anime
# Mahouka Koukou no Rettousei S3 https://mahouka.jp/3rd/ #mahouka @mahouka_anime
# Maou no Ore ga Dorei Elf wo Yome ni Shitanda ga, Dou Medereba Ii? https://madome-anime.com/ #まどめ #madome @madome_PR
# One Room, Hiatari Futsuu, Tenshi-tsuki. https://tenshitsuki.com/ #天使つき @tenshitsuki_off
# Ookami to Koushinryou https://spice-and-wolf.com/ #狼と香辛料 #spice_and_wolf @Spicy_Wolf_Prj
# Re:Monster https://re-monster.com/ #remonster_anime @ReMonster_anime
# Sasayaku You ni Koi wo Utau https://sasakoi-anime.com/ #ささこい @sasakoi_anime
# Seiyuu Radio no Uraomote https://seiyuradio-anime.com/ #声優ラジオのウラオモテ @sayyouradio_prj
# Shinigami Bocchan to Kuro Maid S3 https://bocchan-anime.com/ #死神坊ちゃん @bocchan_anime
# Tensei Kizoku, Kantei Skill de Nariagaru https://kanteiskill.com/ #鑑定スキル @kanteiskill
# Tensei shitara Dainana Ouji Datta node, Kimama ni Majutsu wo Kiwamemasu https://dainanaoji.com/ #第七王子 @dainanaoji_pro
# The New Gate https://the-new-gate-pr.com/ #THENEWGATE @thenewgateanime
# Unnamed Memory https://unnamedmemory.com/ #UnnamedMemory #アンメモ @Project_UM
# Yoru no Kurage wa Oyogenai https://yorukura-anime.com/ #ヨルクラ #yorukura_anime @yorukura_anime
# Yozakura-san Chi no Daisakusen https://mission-yozakura-family.com/ #夜桜さんちの大作戦 #MissionYozakuraFamily @OfficialHitsuji
# Yuru Camp S3 https://yurucamp.jp/third/ #ゆるキャン @yurucamp_anime


# Spring 2024 Anime
class Spring2024AnimeDownload(MainDownload):
    season = "2024-2"
    season_name = "Spring 2024"
    folder_name = '2024-2'

    def __init__(self):
        super().__init__()


# Dekisokonai to Yobareta Motoeiyuu wa Jikka kara Tsuihou sareta node Sukikatte ni Ikiru Koto ni Shita
class DekisokoDownload(Spring2024AnimeDownload, NewsTemplate):
    title = 'Dekisokonai to Yobareta Motoeiyuu wa Jikka kara Tsuihou sareta node Sukikatte ni Ikiru Koto ni Shita'
    keywords = [title, 'The Banished Former Hero Lives as He Pleases']
    website = 'https://dekisoko-anime.com/'
    twitter = 'dekisoko_pr'
    hashtags = 'できそこ'
    folder_name = 'dekisoko'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 5

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'dist/img/story/ep%s/img%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1).zfill(2)
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news_item',
                                    title_select='.ttl', date_select='.year,.day', date_tag_count=2,
                                    id_select='a', a_tag_start_text_to_remove='../', a_tag_prefix=self.PAGE_PREFIX,
                                    date_func=lambda x: x[0:4] + '.' + x[4:6] + '.' + x[7:])

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        prefix = self.PAGE_PREFIX + 'dist/img/news/detail/'
        self.image_list = []
        self.add_to_image_list('tz', prefix + 'news0620-1.jpg')
        self.add_to_image_list('kv1', prefix + 'news0124-1.jpg')
        self.add_to_image_list('kv2', prefix + 'news0301-1.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'dist/img/character/chara%s/stand.webp'
        try:
            for i in range(1, 20, 1):
                image_url = template % i
                image_name = 'chara' + str(i)
                result = self.download_image(image_url, folder + '/' + image_name)
                if result == -1:
                    break
        except Exception as e:
            self.print_exception(e, 'Character')


# Hananoi-kun to Koi no Yamai #花野井くんと恋の病
class HananoikunDownload(Spring2024AnimeDownload, NewsTemplate):
    title = 'Hananoi-kun to Koi no Yamai'
    keywords = [title, 'A Condition Called Love']
    website = 'https://hananoikun-pr.com/'
    twitter = 'hananoikun_pr'
    hashtags = '花野井くんと恋の病'
    folder_name = 'hananoikun'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_guess(print_invalid=False, download_valid=True)
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            stories = soup.select('.story-box')
            for story in stories:
                try:
                    episode = str(int(story.select('.num')[0].text.replace('#', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                images = story.select('.story-ss img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = images[i]['src']
                    if '-sample' in image_url:
                        break
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_guess(self, print_invalid=False, download_valid=False):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_' + str(self.IMAGES_PER_EPISODE)):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wp/wp-content/uploads/%s/%s/%shananoi_%s_c%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        valid_urls = []
        image_folder = folder + '/' + year + '/' + month
        for i in range(self.FINAL_EPISODE):
            ep_num = str(i + 1)
            episode = ep_num.zfill(2)
            if self.is_image_exists(episode + '_1') or self.is_image_exists(episode + '_1', image_folder):
                continue
            image_count = 0
            for j in range(1, self.IMAGES_PER_EPISODE + 1, 1):
                image_url = template % (year, month, '' if j > 1 else '【MAIN】', ep_num, str(j))
                image_name = episode + '_' + str(image_count + 2)
                if self.is_valid_url(image_url, is_image=True):
                    print('VALID - ' + image_url)
                    is_successful = True
                    valid_urls.append({'name': image_name, 'url': image_url, 'folder': image_folder})
                    image_count += 1
                elif print_invalid:
                    print('INVALID - ' + image_url)
            if image_count == 0:
                break

        if download_valid and len(valid_urls) > 0:
            for valid_url in valid_urls:
                image_name = valid_url['name']
                image_folder = valid_url['folder']
                if not os.path.exists(image_folder):
                    os.makedirs(image_folder)
                self.download_image(valid_url['url'], image_folder + '/' + image_name)
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-item',
                                    title_select='.title', date_select='.date', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'wp/wp-content/themes/hananoi-honban/images/kv1.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/hananoi-honban/images/chara-pic%s.png'
        self.download_by_template(folder, template, 1, 1)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'package/')
            images = soup.select('.section-contents img[src*="/images/"]')
            self.image_list = []
            for image in images:
                image_url = image['src']
                image_name = self.generate_image_name_from_url(image_url, 'images')
                if image_name in ['privilege-pic-sample', 'package-pic-sample', 'package-pic-event']:
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Henjin no Salad Bowl
class HensaraDownload(Spring2024AnimeDownload, NewsTemplate):
    title = 'Henjin no Salad Bowl'
    keywords = [title, 'Salad Bowl of Eccentrics']
    website = 'https://www.tbs.co.jp/anime/hensara/'
    twitter = 'hensara_anime'
    hashtags = '変サラ'
    folder_name = 'hensara'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'story/img/v%s_%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='#nw-ind-list li',
                                    date_select='.date', title_select='.txt', id_select='a', a_tag_prefix=news_url)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        # self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/F7lu7ArboAAFbIl?format=jpg&name=large')
        # self.add_to_image_list('teaser_hero', self.PAGE_PREFIX + 'img/teaser/hero.jpg')
        self.add_to_image_list('top_hero', self.PAGE_PREFIX + 'img/top/hero.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'img/character/chara%s_st.png'
        self.download_by_template(folder, template, 1, 1)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            bd_url = self.PAGE_PREFIX + 'disc/'
            soup = self.get_soup(bd_url)
            images = soup.select('section img[src]')
            self.image_list = []
            for image in images:
                if image['src'].startswith('/'):
                    continue
                image_url = bd_url + image['src'].split('?')[0]
                image_name = self.generate_image_name_from_url(image_url, 'disc')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Hibike! Euphonium 3
class HibikiEuphonium3Download(Spring2024AnimeDownload, NewsTemplate):
    title = 'Hibike! Euphonium 3'
    keywords = [title, 'Sound! Euphonium 3']
    website = 'https://anime-eupho.com/'
    twitter = 'anime_eupho'
    hashtags = ['anime_eupho']
    folder_name = 'eupho3'

    PAGE_PREFIX = website
    FINAL_EPISODE = 13
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'img/story/story%s-%s-tv3.webp'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsEntryList li',
                                    title_select='.entryTitle', date_select='.entryDate', id_select='a',
                                    a_tag_start_text_to_remove='/', a_tag_prefix=self.PAGE_PREFIX,
                                    paging_type=3, paging_suffix='index.php?pageID=%s',
                                    next_page_select='#pager a[title^="next"]', stop_date='2023.08.03')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('top_keyvisual02', self.PAGE_PREFIX + 'img/top/keyvisual02.webp')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            self.image_list = []
            images = soup.select('.character-item-img img[src*="/character/"]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'][1:]
                image_name = self.generate_image_name_from_url(image_url, 'character')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Jii-san Baa-san Wakagaeru
class JisanBasanDownload(Spring2024AnimeDownload, NewsTemplate):
    title = 'Jii-san Baa-san Wakagaeru'
    keywords = [title, 'jiisanbaasan', 'Grandpa and Grandma Turn Young Again']
    website = 'https://jisanbasan.com/'
    twitter = 'jisanbasan_prj'
    hashtags = ['じいさんばあさん若返る']
    folder_name = 'jisanbasan'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        soup = self.download_key_visual()
        self.download_character(soup)
        self.download_media()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'assets/story/%s/%s.webp'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.content-entry',
                                    title_select='.entry-title span', date_select='.entry-date',
                                    id_select=None, id_has_id=True, news_prefix='news.html',
                                    date_func=lambda x: x.replace('年', '.').replace('月', '.').replace('日', ''))

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        soup = None
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.vis img[src*="/top/"]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('./', '')
                image_name = self.generate_image_name_from_url(image_url, 'top')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')
        return soup

    def download_character(self, soup=None):
        folder = self.create_character_directory()
        try:
            if soup is None:
                soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.chr-img img[data-src*="/character/"]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['data-src'].replace('./', '')
                image_name = self.generate_image_name_from_url(image_url, 'character')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bluray.html')
            images = soup.select('section img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('./', '')
                image_name = self.extract_image_name_from_url(image_url)
                if image_name == 'np':
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Kaijuu 8-gou
class Kaiju8Download(Spring2024AnimeDownload, NewsTemplate):
    title = 'Kaijuu 8-gou'
    keywords = [title, "Kaiju No. 8"]
    website = 'https://kaiju-no8.net/'
    twitter = 'KaijuNo8_O'
    hashtags = ['KaijuNo8', '怪獣８号']
    folder_name = 'kaiju8'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        try:
            a = self.get_response(news_url + 'news.js', decode=True)
            b = a.split('Array(')[1].replace('\r\n', '').replace('\t', '')
            c = '[' + b[:b.rfind('}') + 1] + ']'
            json_obj = json.loads(c)

            results = []
            news_obj = self.get_last_news_log_object()
            for item in json_obj:
                if 'date' in item and 'name' in item and 'title' in item:
                    date = item['date']
                    title = item['title']
                    url = news_url + item['name'] + '.html'
                    if news_obj is not None and (news_obj['id'] == url or news_obj['title'] == title
                                                 or date < news_obj['date']):
                        break
                    results.append(self.create_news_log_object(date, title, url))
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            self.print_exception(e, 'News')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        template = self.PAGE_PREFIX + 'assets/img/top/kv%s.jpg'
        i = 0
        try:
            while i < 20:
                i += 1
                number = ''
                if i > 1:
                    number = str(i)
                image_url = template % number
                image_name = 'top_kv' + number
                if self.is_image_exists(image_name, folder):
                    continue
                result = self.download_image(image_url, folder + '/' + image_name)
                if result == -1:
                    break
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/img/character/c%s_main.png'
        self.download_by_template(folder, template, 1, 0)


# Kami wa Game ni Ueteiru.
class KamiueDownload(Spring2024AnimeDownload, NewsTemplate):
    title = 'Kami wa Game ni Ueteiru.'
    keywords = [title, "Gods' Game We Play"]
    website = 'https://godsgame-anime.com/'
    twitter = 'kami_to_game'
    hashtags = ['神飢え', '神飢えアニメ', 'kamiue']
    folder_name = 'kamiue'

    PAGE_PREFIX = website
    FINAL_EPISODE = 13
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'images/story/%s/p_%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1).zfill(3), str(j + 1).zfill(3))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            json_obj = self.get_json(self.PAGE_PREFIX + 'news.json')
            for item in json_obj:
                if 'day' in item and 'url' in item and 'title' in item:
                    try:
                        date = datetime.strptime(item['day'], "%Y/%m/%d").strftime("%Y.%m.%d")
                    except:
                        continue
                    title = item['title']
                    url = self.PAGE_PREFIX + item['url']
                    if news_obj is not None and (news_obj['id'] == url or news_obj['title'] == title
                                                 or date < news_obj['date']):
                        break
                    results.append(self.create_news_log_object(date, title, url))
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            self.print_exception(e, 'News')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.visual_wrap .img_100 img[src*="/visual/"]')
            self.image_list = []
            for image in images:
                image_name = self.extract_image_name_from_url(image['src'])
                image_url = self.PAGE_PREFIX + image['src']
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'images/chara/'
        template = prefix + 'c_%s.png'
        self.download_by_template(folder, template, 3, 1)
        templates = [prefix + 'a%s_left.png', prefix + 'a%s_center.png', prefix + 'a%s_right.png']
        self.download_by_template(folder, templates, 2, 1)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'package.html')
            images = soup.select('img[src*="/package/"]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].split('?')[0]
                image_name = self.generate_image_name_from_url(image_url, 'package')
                if 'nowpri' in image_name:
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')

        special_folder = self.create_custom_directory(folder.split('/')[-1] + '/special')
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'special.html?cat=visual')
            images = soup.select('article.visual a[href^="images/"]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['href']
                image_name = self.generate_image_name_from_url(image_url, 'images')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(special_folder)
        except Exception as e:
            self.print_exception(e, 'Special')


# Kono Sekai wa Fukanzen Sugiru
class KonofukaDownload(Spring2024AnimeDownload, NewsTemplate):
    title = 'Kono Sekai wa Fukanzen Sugiru'
    keywords = [title, "Quality Assurance in Another World"]
    website = 'https://konofuka.com/'
    twitter = 'konofuka_QA'
    hashtags = ['このふか', 'konofuka']
    folder_name = 'konofuka'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.top-news a',
                                    title_select='.news-ttl', date_select='.news-date', id_select=None,
                                    next_page_select='ul.page-numbers li span', next_page_eval_index=-1,
                                    next_page_eval_index_class='current',
                                    date_func=lambda x: x.replace('(', '').replace(')', ''))

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'pDK2yjkH/wp-content/themes/konofuka_v0.1/assets/img/top/mv.png')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fr85Cb4aAAAgWlS?format=jpg&name=4096x4096')
        self.download_image_list(folder)


# Kono Subarashii Sekai ni Shukufuku wo! 3
class Konosuba3Download(Spring2024AnimeDownload, NewsTemplate):
    title = 'Kono Subarashii Sekai ni Shukufuku wo! 3'
    keywords = [title, 'konosuba', 'KonoSuba: God’s Blessing on This Wonderful World! 3', '3rd']
    website = 'http://konosuba.com/3rd/'
    twitter = 'konosubaanime'
    hashtags = ['konosuba', 'このすば']
    folder_name = 'konosuba3'

    PAGE_PREFIX = website
    FINAL_EPISODE = 11
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_media()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'story/img/%s/%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-list__item',
                                    date_select='.news-list__date', title_select='.news-list__title',
                                    id_select='a', a_tag_prefix=news_url)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.top-main__mv img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        bd_url = self.PAGE_PREFIX + 'bd/'
        for page in ['cmp', 'shop', 'bd_box', 'bd1', 'bd2', 'bd3', 'bd4']:
            try:
                if page in processed:
                    continue
                soup = self.get_soup(bd_url + '?mode=' + page)
                images = soup.select('.cts_area img[src^="img/"]')
                self.image_list = []
                for image in images:
                    image_url = bd_url + image['src'].split('?')[0]
                    image_name = self.generate_image_name_from_url(image_url, 'img')
                    if self.is_image_exists(image_name, folder):
                        continue
                    self.add_to_image_list(image_name, image_url)
                if len(self.image_list) == 0:
                    break
                else:
                    processed.append(page)
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Lv2 kara Cheat datta Motoyuusha Kouho no Mattari Isekai Life
class Lv2CheatDownload(Spring2024AnimeDownload, NewsTemplate):
    title = 'Lv2 kara Cheat datta Motoyuusha Kouho no Mattari Isekai Life'
    keywords = [title, "Chillin' in Another World with Level 2 Super Cheat Powers"]
    website = 'https://lv2-cheat.com/'
    twitter = 'Lv2cheat_anime'
    hashtags = 'Lv2チート'
    folder_name = 'lv2cheat'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_guess(print_invalid=False, download_valid=True)
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            title = soup.select('.title')
            curr_episode = None
            try:
                curr_episode = str(int(title[0].text.split('話')[0].replace('第', ''))).zfill(2)
            except:
                pass
            stories = soup.select('.switch a[href]')
            for story in stories:
                try:
                    episode = str(int(story.text)).zfill(2)
                except:
                    continue
                if episode == curr_episode:
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(story['href'])
                    if ep_soup is None:
                        continue
                self.image_list = []
                images = ep_soup.select('#story_cont img[src]')
                for i in range(len(images)):
                    image_url = self.clear_resize_in_url(images[i]['src'].split('?')[0])
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_guess(self, print_invalid=False, download_valid=False, min_limit=20, max_limit=200):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_' + str(self.IMAGES_PER_EPISODE)):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wp/wp-content/uploads/%s/%s/lv2_%s-%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        valid_urls = []
        image_folder = folder + '/' + year + '/' + month
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1') or self.is_image_exists(episode + '_1', image_folder):
                continue
            j = 0
            image_count = 0
            valid_nums = []
            while j < max_limit:
                image_url = template % (year, month, episode, str(j))
                image_name = episode + '_' + str(image_count + 1)
                if self.is_valid_url(image_url, is_image=True):
                    print('VALID - ' + image_url)
                    is_successful = True
                    valid_urls.append({'name': image_name, 'url': image_url, 'folder': image_folder})
                    image_count += 1
                    valid_nums.append(j)
                elif print_invalid:
                    print('INVALID - ' + image_url)
                j += 1
                if image_count >= self.IMAGES_PER_EPISODE:
                    break
                if j > min_limit and image_count == 0:
                    break
            if image_count == 0:
                break
        if download_valid and len(valid_urls) > 0:
            for valid_url in valid_urls:
                image_name = valid_url['name']
                image_folder = valid_url['folder']
                if not os.path.exists(image_folder):
                    os.makedirs(image_folder)
                self.download_image(valid_url['url'], image_folder + '/' + image_name)
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newslist',
                                    date_select='.date', title_select='.title', id_select='a',
                                    date_func=lambda x: x[0:4] + '.' + x[4:6] + '.' + x[7:9])

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.mainvisual .slide img[src*="/img/"]')
            for image in images:
                image_url = image['src']
                image_name = self.generate_image_name_from_url(image_url, 'img')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/lv2cheat-v2/img/%s.png'
        self.download_by_template(folder, template, 2, 1)


# Mahouka Koukou no Rettousei S3
class Mahouka3Download(Spring2024AnimeDownload, NewsTemplate):
    title = 'Mahouka Koukou no Rettousei 3rd Season'
    keywords = [title, "The Irregular at Magic High School: Visitor Arc"]
    website = 'https://mahouka.jp/3rd/'
    twitter = 'mahouka_anime'
    hashtags = 'mahouka'
    folder_name = 'mahouka3'

    BASE_PREFIX = 'https://mahouka.jp/'
    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            story_url = self.PAGE_PREFIX + 'story/'
            soup = self.get_soup(story_url, decode=True)
            lis = soup.select('.p-story__nav-item')
            for li in lis:
                a_tag = li.find('a')
                if a_tag and a_tag.has_attr('href'):
                    try:
                        episode = str(int(a_tag.text)).zfill(2)
                    except Exception:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    if li.has_attr('class') and 'is-active' in li['class']:
                        ep_soup = soup
                    else:
                        ep_soup = self.get_soup(story_url + a_tag['href'].replace('./', ''))
                    if ep_soup:
                        images = ep_soup.select('.p-story__cut-imglist img[src]')
                        self.image_list = []
                        for i in range(len(images)):
                            image_url = story_url + images[i]['src']
                            image_name = episode + '_' + str(i + 1)
                            self.add_to_image_list(image_name, image_url)
                        self.download_image_list(self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.p-news__list-item',
                                    date_select='.p-news_article__date', title_select='.p-news_article__title',
                                    id_select='a', a_tag_start_text_to_remove='/', a_tag_prefix=self.BASE_PREFIX,
                                    next_page_select='.--next', paging_type=1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('main_kv', self.PAGE_PREFIX + 'assets/img/main_kv.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/img/character/c_%s.png'
        self.download_by_template(folder, template, 2, 1)


# Maou no Ore ga Dorei Elf wo Yome ni Shitanda ga, Dou Medereba Ii?
class MadomeDownload(Spring2024AnimeDownload, NewsTemplate):
    title = 'Maou no Ore ga Dorei Elf wo Yome ni Shitanda ga, Dou Medereba Ii?'
    keywords = [title, "An Archdemon's Dilemma: How to Love Your Elf Bride"]
    website = 'https://madome-anime.com/'
    twitter = 'madome_PR'
    hashtags = ['まどめ', 'madome']
    folder_name = 'madome'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 4

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_guess()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            story_url = self.PAGE_PREFIX + 'story/'
            soup = self.get_soup(story_url)
            stories = soup.select('section.list a[href]')
            for story in stories:
                try:
                    episode = str(int(story['href'].split('.html')[0])).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                ep_soup = self.get_soup(story_url + story['href'])
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.scene .thumb img[src]')
                for i in range(len(images)):
                    image_url = self.PAGE_PREFIX + images[i]['src'].replace('../', '')
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'assets/images/story/vol1/1-%s-%s.jpg'
        is_successful = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            is_success = False
            for j in range(self.IMAGES_PER_EPISODE):
                image_url = template % (episode, str(j + 1))
                image_name = episode + '_' + str(j + 1)
                result = self.download_image(image_url, folder + '/' + image_name)
                if result == 0:
                    is_success = True
                    is_successful = True
                elif result == -1:
                    break
            if is_success:
                print(self.__class__.__name__ + ' - Guessed successfully!')
            else:
                if len(os.listdir(folder)) == 0:
                    os.rmdir(folder)
                break
        if len(os.listdir(folder)) == 0:
            os.rmdir(folder)
        return is_successful

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.list article',
                                    date_select='time', title_select='h2', id_select='a', a_tag_prefix=news_url)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('top_kv', self.PAGE_PREFIX + 'assets/images/top/kv.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        chara_url = self.PAGE_PREFIX + 'character/'
        try:
            soup = self.get_soup(chara_url + 'zagan.html')
            pages = soup.select('.thumb a[href]')
            for page in pages:
                if not page['href'].endswith('.html'):
                    continue
                page_url = chara_url + page['href']
                page_name = page['href'].split('.html')[0]
                if page_name in processed:
                    continue
                if page_name == 'zagan':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(page_url)
                if ep_soup is None:
                    continue
                images = ep_soup.select('section picture img[src*="/character/"]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'][1:]
                    image_name = self.generate_image_name_from_url(image_url, 'character')
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
                processed.append(page_name)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)

    def download_media(self):
        folder = self.create_media_directory()
        bd_url = self.PAGE_PREFIX + 'blu-ray/'
        for i in range(1, 4, 1):
            page = str(i).zfill(3)
            try:
                soup = self.get_soup(bd_url + page + '.html')
                images = soup.select('.detail img[src*="/blu-ray/"]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].split('?')[0].replace('../', '')
                    if image_url.endswith('/item.png'):
                        continue
                    image_name = self.generate_image_name_from_url(image_url, 'blu-ray')
                    if self.is_image_exists(image_name, folder):
                        continue
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')


# One Room, Hiatari Futsuu, Tenshi-tsuki.
class TenshitsukiDownload(Spring2024AnimeDownload, NewsTemplate):
    title = 'One Room, Hiatari Futsuu, Tenshi-tsuki.'
    keywords = [title, 'SStudio Apartment, Good Lighting, Angel Included']
    website = 'https://tenshitsuki.com/'
    twitter = 'tenshitsuki_off'
    hashtags = ['天使つき']
    folder_name = 'tenshitsuki'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'assets/story/%s/%s.webp'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.content-entry',
                                    title_select='.entry-title span', date_select='.entry-date span',
                                    id_select=None, id_has_id=True, news_prefix='news.html')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.vis img[src*="/assets/"]')
            self.image_list = []
            for image in images:
                image_url = image['src']
                if image_url.startswith('./'):
                    image_url = self.PAGE_PREFIX + image_url[2:]
                image_name = self.generate_image_name_from_url(image_url, 'assets')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'assets/character/%s'
        templates = [prefix + 'c.webp', prefix + 'f.webp']
        self.download_by_template(folder, templates, 1, 1)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bluray.html')
            images = soup.select('article img[src*="/bluray/"]')
            self.image_list = []
            for image in images:
                image_url = image['src']
                if '/np.' in image_url:
                    continue
                if image_url.startswith('./'):
                    image_url = self.PAGE_PREFIX + image_url[2:]
                image_name = self.generate_image_name_from_url(image_url, 'bluray')
                self.add_to_image_list(image_name, image_url, to_jpg=True)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')


# Ookami to Koushinryou
class OokamitoKoushinryouDownload(Spring2024AnimeDownload, NewsTemplate):
    title = 'Ookami to Koushinryou'
    keywords = [title, 'Spice and Wolf']
    website = 'https://spice-and-wolf.com/'
    twitter = 'Spicy_Wolf_Prj'
    hashtags = ['狼と香辛料', 'spice_and_wolf']
    folder_name = 'spicewolf'

    PAGE_PREFIX = website
    FINAL_EPISODE = 25
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'story/img/ep%s/ep%s_img%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, episode, str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsList',
                                    title_select='.newsList__title', date_select='.newsList__date',
                                    id_select='a', a_tag_prefix=news_url)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        sub_folder = self.create_custom_directory(folder.split('/')[-1] + '/news')
        cache_filepath = sub_folder + '/cache'
        news_url = self.PAGE_PREFIX + 'news/'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(news_url, decode=True)
            items = soup.select('.newsList')
            for item in items:
                a_tag = item.select('a[href]')
                if len(a_tag) == 0:
                    continue
                page_name = a_tag[0]['href'].split('.html')[0]
                if page_name in processed:
                    break
                title_tag = item.select('.newsList__title')
                if len(title_tag) == 0:
                    continue
                title = title_tag[0].text.strip()
                if 'ビジュアル' in title or 'イラスト' in title:
                    page_soup = self.get_soup(news_url + a_tag[0]['href'])
                    if page_soup is not None:
                        images = page_soup.select('.newsArticle img[src]')
                        self.image_list = []
                        for image in images:
                            if not image['src'].startswith('img/'):
                                continue
                            image_url = news_url + image['src'].split('?')[0]
                            image_name = self.generate_image_name_from_url(image_url, 'img')
                            self.add_to_image_list(image_name, image_url)
                        self.download_image_list(sub_folder)
                processed.append(page_name)
        except Exception as e:
            self.print_exception(e, 'Key Visual News')
        self.create_cache_file(cache_filepath, processed, num_processed)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.characterDetailList img[src]')
            self.image_list = []
            for image in images:
                image_url = image['src']
                if image_url.startswith('./'):
                    image_url = self.PAGE_PREFIX + image_url[2:]
                if '/character/' in image_url:
                    image_name = self.generate_image_name_from_url(image_url, 'character')
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        bd_prefix = self.PAGE_PREFIX + 'bd/'
        for page in ['tokuten', '1', '2', '3', '4']:
            try:
                if page in processed:
                    continue
                page_url = bd_prefix
                if page.isnumeric():
                    page_url += 'vol'
                page_url += page + '.html'
                soup = self.get_soup(page_url)
                images = soup.select('.newsArticleIn img[src]')
                self.image_list = []
                for image in images:
                    image_url = bd_prefix + image['src'].replace('./', '').split('?')[0]
                    if 'nowprinting' in image_url:
                        continue
                    image_name = self.generate_image_name_from_url(image_url, 'bd')
                    self.add_to_image_list(image_name, image_url)
                if page.isnumeric() and len(self.image_list) > 0:
                    processed.append(page)
                elif page.isnumeric():
                    break
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Re:Monster
class ReMonsterDownload(Spring2024AnimeDownload, NewsTemplate):
    title = 'Re:Monster'
    keyword = [title]
    website = 'https://re-monster.com/'
    twitter = 'ReMonster_anime'
    hashtags = 'remonster_anime'
    folder_name = 'remonster'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 10

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_news()
        soup = self.download_key_visual()
        self.download_character(soup)
        self.download_media()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            stories = soup.select('.storyContent')
            for story in stories:
                try:
                    episode = str(int(story.select('.storyTitle__num')[0].text.replace('#', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_01'):
                    continue
                self.image_list = []
                images = story.select('.storyImageList img[src]')
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1).zfill(2)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        keywords = ['Re:Monster']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20240328', download_id=self.download_id).run()

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.newsList',
                                    date_select='.news__date', title_select='.newsTitle', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        soup = None
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.visualList source[srcset*="/top/"][type="image/webp"]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'].replace('./', '').split('?')[0]
                image_name = self.extract_image_name_from_url(image_url)
                if image_name.endswith('-s') or 'catch' in image_name:
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')
        return soup

    def download_character(self, soup=None):
        folder = self.create_character_directory()
        self.image_list = []
        try:
            if soup is None:
                soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.characterList img[src*="/character/"]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('./', '').split('?')[0]
                image_name = self.generate_image_name_from_url(image_url, 'character')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for num in range(4):
            page = str(num + 1)
            try:
                if num > 0 and page in processed:
                    continue
                soup = self.get_soup(self.PAGE_PREFIX + 'bd/vol' + page + '.php')
                if num > 0:
                    images = soup.select('.bdHeadContent img[src*="/bd/"]')
                else:
                    images = soup.select('img[src*="/bd/"]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                    image_name = self.generate_image_name_from_url(image_url, 'bd')
                    if image_name == 'bd_tokuten_visual':
                        continue
                    self.add_to_image_list(image_name, image_url)
                if num > 0:
                    if len(self.image_list) > 0:
                        processed.append(page)
                    else:
                        break
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Sasayaku You ni Koi wo Utau
class SasakoiDownload(Spring2024AnimeDownload, NewsTemplate):
    title = 'Sasayaku You ni Koi wo Utau'
    keywords = [title, "Whisper Me a Love Song"]
    website = 'https://sasakoi-anime.com/'
    twitter = 'sasakoi_anime'
    hashtags = ['ささこい', 'sasakoi']
    folder_name = 'sasakoi'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news__list tr', news_prefix='',
                                    date_select='.day', title_select='.title', id_select='a', date_separator='/',
                                    a_tag_prefix=self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_kv', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.webp')
        self.add_to_image_list('tz_teaser', self.PAGE_PREFIX + 'core_sys/images/main/tz/teaser.jpg')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.kv__img source[srcset]')
            self.image_list = []
            for image in images:
                if '/main/' not in image['srcset']:
                    continue
                image_name = self.extract_image_name_from_url(image['srcset'])
                if 'kv' not in image_name:
                    continue
                image_name = self.generate_image_name_from_url(image['srcset'], 'main')
                image_url = self.PAGE_PREFIX + image['srcset']
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'core_sys/images/main/tz/chara/c%s_face.jpg'
        self.download_by_template(folder, template, 2, 1, prefix='tz_')


# Seiyuu Radio no Uraomote  #
class SeiyuRadioDownload(Spring2024AnimeDownload, NewsTemplate):
    title = 'Seiyuu Radio no Uraomote'
    keywords = [title]
    website = 'https://seiyuradio-anime.com/'
    twitter = 'sayyouradio_prj'
    hashtags = '声優ラジオのウラオモテ'
    folder_name = 'seiyuradio'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 5

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'dist/img/story/ep%s/img%s.webp'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.c-article__item',
                                    date_select='time', title_select='h3', id_select='a', a_tag_prefix=news_url,
                                    a_tag_start_text_to_remove='./', date_func=lambda x: x[0:4] + '.' + x[4:])

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('top_kv', self.PAGE_PREFIX + 'dist/img/top/kv.webp')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'dist/img/character/character%s/chara%s.webp'
        try:
            for i in range(1, 21, 1):
                stop = False
                for j in range(1, 3, 1):
                    image_name = 'chara' + str(i) + '_' + str(j).zfill(2)
                    if self.is_image_exists(image_name, folder):
                        break
                    image_url = template % (str(i), str(j).zfill(2))
                    result = self.download_image(image_url, folder + '/' + image_name)
                    if result == -1 and j == 1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e, 'Character')


# Shinigami Bocchan to Kuro Maid S3
class ShinigamiBocchan3Download(Spring2024AnimeDownload, NewsTemplate2):
    title = 'Shinigami Bocchan to Kuro Maid 3rd Season'
    keywords = [title, 'The Duke of Death and His Maid']
    website = 'https://bocchan-anime.com/'
    twitter = 'bocchan_anime'
    hashtags = '死神坊ちゃん'
    folder_name = 'shinigami-bocchan3'

    PAGE_PREFIX = website
    FIRST_EPISODE = 25
    FINAL_EPISODE = 36
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            stories = soup.select('#ContentsListUnit01 a[href]')
            for story in stories:
                try:
                    ep_num = int(story.text.replace('#', ''))
                    if ep_num < self.FIRST_EPISODE:
                        continue
                    episode = str(ep_num).zfill(2)
                except:
                    continue
                ep_soup = self.get_soup(self.PAGE_PREFIX + story['href'].replace('../', ''))
                if ep_soup is None:
                    continue
                images = ep_soup.select('ul.tp5 img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = self.PAGE_PREFIX + images[i]['src'].split('?')[0].replace('../', '').replace('sn_', '')
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX, stop_date='2023.09.20')


# Tensei Kizoku, Kantei Skill de Nariagaru
class KanteiSkillDownload(Spring2024AnimeDownload, NewsTemplate):
    title = 'Tensei Kizoku, Kantei Skill de Nariagaru'
    keywords = [title, 'kanteiskill', "As a Reincarnated Aristocrat, I’ll Use My Appraisal Skill to Rise in the World"]
    website = 'https://kanteiskill.com/'
    twitter = 'kanteiskill'
    hashtags = '鑑定スキル'
    folder_name = 'kanteiskill'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self, print_http_error=False):
        try:
            objs = self.get_json(self.PAGE_PREFIX + 'story_data?_=' + str(math.floor(time.time() * 1000)))
            for obj in objs:
                if 'acf' in obj:
                    acf = obj['acf']
                    if 'number' in acf and 'images' in acf and isinstance(acf['images'], list):
                        try:
                            episode = str(int(acf['number'])).zfill(2)
                        except:
                            continue
                        for i in range(len(acf['images'])):
                            image_url = acf['images'][i]
                            image_name = episode + '_' + str(i + 1)
                            self.add_to_image_list(image_name, image_url)
                        self.download_image_list(self.base_folder)
        except HTTPError:
            if print_http_error:
                print(self.__class__.__name__ + ' - 403 Error when retrieving story API.')
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.c-news-item',
                                    title_select='.c-news-item__title', date_select='.c-news-item__date',
                                    id_select=None, a_tag_start_text_to_remove='/', a_tag_prefix=self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FvmXW8HakAAhiY6?format=jpg&name=large')
        self.add_to_image_list('home_visual_1_pc', self.PAGE_PREFIX + 'wordpress/wp-content/themes/kanteiskill_20231110/img/home/visual_1_pc.webp')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        json_url = self.PAGE_PREFIX + 'chara_data'
        self.image_list = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            if soup is None:
                return
            prefix = soup.select('body[data-theme-url]')[0]['data-theme-url']

            json_obj = self.get_json(json_url)
            if 'charas' in json_obj and isinstance(json_obj['charas'], list):
                for chara in json_obj['charas']:
                    if 'images' in chara:
                        if 'visuals' in chara['images'] and isinstance(chara['images']['visuals'], list):
                            for visual in chara['images']['visuals']:
                                if 'image' in visual:
                                    image_url = prefix + visual['image'].split('?')[0]
                                    image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                                    self.add_to_image_list(image_name, image_url)
                        if 'faces' in chara['images'] and isinstance(chara['images']['faces'], list):
                            for face in chara['images']['faces']:
                                image_url = prefix + face.split('?')[0]
                                image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                                self.add_to_image_list(image_name, image_url)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.download_image_list(folder)

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        bd_url = self.PAGE_PREFIX + 'product/'
        for page in ['shop-tokuten', 'bd']:
            try:
                if page in processed:
                    continue
                soup = self.get_soup(bd_url + page)
                images = soup.select('article img[data-src]')
                self.image_list = []
                for image in images:
                    image_url = image['data-src'].split('?')[0]
                    image_name = self.extract_image_name_from_url(image_url)
                    if self.is_image_exists(image_name, folder):
                        continue
                    self.add_to_image_list(image_name, image_url)
                if page != 'bd':
                    processed.append(page)
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Tensei shitara Dainana Ouji Datta node, Kimama ni Majutsu wo Kiwamemasu
class DainanaojiDownload(Spring2024AnimeDownload, NewsTemplate):
    title = 'Tensei shitara Dainana Ouji Datta node, Kimama ni Majutsu wo Kiwamemasu'
    keywords = [title, 'I Was Reincarnated as the 7th Prince so I Can Take My Time Perfecting My Magical Ability']
    website = 'https://dainanaoji.com/'
    twitter = 'dainanaoji_pro'
    hashtags = '第七王子'
    folder_name = 'dainanaoji'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 7

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_guess(print_invalid=False, download_valid=True)
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            stories = soup.select('.story-episode-item a[href]')
            for story in stories:
                try:
                    episode = str(int(story['href'].split('/')[-1])).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                ep_soup = self.get_soup(story['href'])
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.story-thumb-item img[src]')
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_guess(self, print_invalid=False, download_valid=False, min_limit=20, max_limit=200):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_' + str(self.IMAGES_PER_EPISODE)):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'd81Ft6ye/wp-content/uploads/%s/%s/%sDai7_ep%s_cap-%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        valid_urls = []
        image_folder = folder + '/' + year + '/' + month
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1') or self.is_image_exists(episode + '_1', image_folder):
                continue
            j = 0
            image_count = 0
            valid_nums = []
            while j < max_limit:
                image_url = template % (year, month, '', episode, str(j).zfill(3))
                image_name = episode + '_' + str(image_count + 1)
                if self.is_valid_url(image_url, is_image=True):
                    print('VALID - ' + image_url)
                    is_successful = True
                    valid_urls.append({'name': image_name, 'url': image_url, 'folder': image_folder})
                    image_count += 1
                    valid_nums.append(j)
                elif print_invalid:
                    print('INVALID - ' + image_url)
                j += 1
                if image_count >= self.IMAGES_PER_EPISODE:
                    break
                if j > min_limit and image_count == 0:
                    break
            if image_count == 0:
                break
            # elif image_count == self.IMAGES_PER_EPISODE - 1:
            #     j = 0
            #     while j < max_limit:
            #         if j in valid_nums:
            #             j += 1
            #             continue
            #         image_url = template % (year, month, '★main_', episode, str(j).zfill(3))
            #         image_name = episode + '_1'
            #         if self.is_valid_url(image_url, is_image=True):
            #             print('VALID - ' + image_url)
            #             valid_urls.append({'name': image_name, 'url': image_url, 'folder': image_folder})
            #             break
            #         elif print_invalid:
            #             print('INVALID - ' + image_url)
            #         j += 1

        if download_valid and len(valid_urls) > 0:
            for valid_url in valid_urls:
                image_name = valid_url['name']
                image_folder = valid_url['folder']
                if not os.path.exists(image_folder):
                    os.makedirs(image_folder)
                self.download_image(valid_url['url'], image_folder + '/' + image_name)
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='#news-container article',
                                    date_select='.news-box-date', title_select='.news-txt-box', id_select='a',
                                    date_func=lambda x: x.replace('-Date', '').strip())

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fgo-UydUAAAq3qH?format=jpg&name=medium')
        self.add_to_image_list('tz_visual_img', self.PAGE_PREFIX + 'd81Ft6ye/wp-content/themes/v0/assets/img/top/visual/img.webp')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        # template = self.PAGE_PREFIX + 'd81Ft6ye/wp-content/themes/v0/assets/img/character/%s.webp'
        # self.download_by_template(folder, template, 1, 0, prefix='tz_')
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.character-img-box>img[src]')
            for image in images:
                if '/img/' not in image['src']:
                    continue
                image_url = image['src']
                image_name = self.generate_image_name_from_url(image_url, 'img')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# The New Gate
class TheNewGateDownload(Spring2024AnimeDownload, NewsTemplate):
    title = 'The New Gate'
    keywords = [title]
    website = 'https://the-new-gate-pr.com/'
    twitter = 'thenewgateanime'
    hashtags = ['THENEWGATE']
    folder_name = 'thenewgate'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-item',
                                    title_select='.title', date_select='.date', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'wp/wp-content/themes/tng-honban/images/kv-pc.jpg')
        self.add_to_image_list('kv2-pc', self.PAGE_PREFIX + 'wp/wp-content/themes/tng-honban/images/kv2-pc.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/tng-honban/images/chara-pic%s.png'
        self.download_by_template(folder, template, 1, 1)


# Unnamed Memory
class UnnamedMemoryDownload(Spring2024AnimeDownload, NewsTemplate):
    title = 'Unnamed Memory'
    keywords = [title]
    website = 'https://unnamedmemory.com/'
    twitter = 'Project_UM'
    hashtags = ['UnnamedMemory', 'アンメモ']
    folder_name = 'unnamedmemory'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'assets/story/%s/%s.webp'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.content-entry',
                                    title_select='.entry-title span', date_select='.entry-date span',
                                    id_select=None, id_has_id=True, news_prefix='news.html')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fj2aPSZVIAEC9LY?format=jpg&name=4096x4096')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.vis source[srcset], .vis img[src]')
            self.image_list = []
            for image in images:
                if image.has_attr('srcset'):
                    image_url = image['srcset']
                else:
                    image_url = image['src']
                if image_url.startswith('./'):
                    image_url = self.PAGE_PREFIX + image_url[2:]
                if '/assets/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'assets')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

        sub_folder = self.create_custom_directory(folder.split('/')[-1] + '/news')
        cache_filepath = sub_folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        temp_processed = set()  # Some of the id is not unique
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'news.html')
            items = soup.select('article article')
            for item in items:
                page_name = item['id']
                if page_name in processed:
                    break
                title = item.select('.entry-title span')[0].text.strip()
                if 'ビジュアル' in title or 'イラスト' in title:
                    images = item.select('img[data-src]')
                    self.image_list = []
                    for image in images:
                        image_url = self.PAGE_PREFIX + image['data-src'].replace('./', '').split('?')[0]
                        if '/news/' not in image_url:
                            continue
                        image_name = self.generate_image_name_from_url(image_url, 'news')
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(sub_folder)
                temp_processed.add(page_name)
        except Exception as e:
            self.print_exception(e, 'Key Visual News')
        for page_name in temp_processed:
            processed.append(page_name)
        self.create_cache_file(cache_filepath, processed, num_processed)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/character/%s.webp'
        self.download_by_template(folder, template, 1, 1)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bddvd.html')
            images = soup.select('img[src*="/bddvd/"]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].split('?')[0].replace('./', '').split('?')[0]
                image_name = self.generate_image_name_from_url(image_url, 'bddvd')
                self.add_to_image_list(image_name, image_url, to_jpg=True)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Yoru no Kurage wa Oyogenai
class YorukuraDownload(Spring2024AnimeDownload, NewsTemplate):
    title = 'Yoru no Kurage wa Oyogenai'
    keywords = [title, 'Jellyfish Can’t Swim in the Night']
    website = 'https://yorukura-anime.com/'
    twitter = 'yorukura_anime'
    hashtags = ['ヨルクラ', 'yorukura_anime']
    folder_name = 'yorukura'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'assets/images/story/%s_%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, news_prefix='', article_select='#news article',
                                    date_select='time', title_select='h3', id_select=None, id_has_id=True)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        # self.image_list = []
        # self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fr6oNgXaIAIDcgR?format=jpg&name=large')
        # self.add_to_image_list('tz', self.PAGE_PREFIX + 'images/mainimg.jpg')
        # self.download_image_list(folder)

        css_url = self.PAGE_PREFIX + 'css/style.min.css'
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            mainslides = soup.select('.mainimg .mainslide[class]')
            _classes = []
            for slide in mainslides:
                for _class in slide['class']:
                    if _class not in ['mainslide', 'swiper-slide']:
                        _classes.append(_class)
                        break
            if len(_classes) > 0:
                self.image_list = []
                css_page = self.get_response(css_url)
                for _class in _classes:
                    search_text = '.mainslide.' + _class + '{background:url('
                    idx = css_page.find(search_text)
                    if idx > 0:
                        right_idx = css_page[idx + len(search_text):].find(')')
                        if right_idx > 0:
                            start_idx = idx + len(search_text)
                            image_url = css_page[start_idx:start_idx + right_idx]
                            if image_url.startswith('../'):
                                image_url = self.PAGE_PREFIX + image_url[3:]
                            image_name = self.extract_image_name_from_url(image_url)
                            self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'images/character/'
        templates = [prefix + 'img_%s.png', prefix + 'face_%s.png']
        self.download_by_template(folder, templates, 2, 1)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'blu-ray/')
            images = soup.select('.inner img[src]:not([src*="nowprinting"])')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Yozakura-san Chi no Daisakusen
class YozakurasanDownload(Spring2024AnimeDownload, NewsTemplate2):
    title = 'Yozakura-san Chi no Daisakusen'
    keywords = [title, 'Mission: Yozakura Family']
    website = 'https://mission-yozakura-family.com/'
    twitter = 'OfficialHitsuji'
    hashtags = ['夜桜さんちの大作戦', 'MissionYozakuraFamily']
    folder_name = 'yozakurasan'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/01.html')
            stories = soup.select('table[summary="List_Type01"] a[href]')
            for story in stories:
                story_url = self.PAGE_PREFIX + story['href'].replace('../', '')
                try:
                    episode = str(int(story_url.split('/')[-1].split('.html')[0])).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if episode == '01':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(story_url)
                if ep_soup is not None:
                    images = ep_soup.select('ul.tp5 img[src]')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = self.PAGE_PREFIX + images[i]['src'].split('?')[0]
                        image_url = self.remove_string(image_url, ['../', 'sn_'])
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FkJB8aSVEAA5Xd1?format=jpg&name=medium')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.kv__img img[src]')
            self.image_list = []
            for image in images:
                if '/images/' in image['src']:
                    image_url = self.PAGE_PREFIX + image['src']
                    image_name = self.generate_image_name_from_url(image_url, 'images')
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/taiyo.html')
            pages = soup.select('#ContentsListUnit01 a[href]')
            for page in pages:
                if not page['href'].endswith('.html') or not page['href'].startswith('../'):
                    continue
                page_url = self.PAGE_PREFIX + page['href'].replace('../', '')
                page_name = page_url.split('/')[-1].split('.html')[0]
                if page_name in processed:
                    continue
                if page_name == 'taiyo':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(page_url)
                if ep_soup is None:
                    continue
                images = ep_soup.select('.charaVisual__img source[srcset]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['srcset'].replace('../', '')
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
                processed.append(page_name)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Yuru Camp S3
class YuruCamp3Download(Spring2024AnimeDownload, NewsTemplate):
    title = "Yuru Camp 3rd Season"
    keywords = [title, 'Yurucamp']
    website = 'https://yurucamp.jp/third/'
    twitter = 'yurucamp_anime'
    hashtags = ['ゆるキャン', 'yurucamp']
    folder_name = 'yurucamp3'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_media()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'assets/img/episodes/%s/%s_%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, episode, str(j + 1))
                    image_name = episode + '_' + str(j + 1).zfill(2)
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        keywords = ['ゆるキャン']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20240329', download_id=self.download_id).run()

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bddvd/')
            images = soup.select('img[src*="/bddvd/"]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                image_name = self.generate_image_name_from_url(image_url, 'bddvd')
                if self.is_image_exists(image_name, folder):
                    continue
                if image_name == 'tokuten_nowprinting':
                    continue
                elif image_name in ['nowprinting_2', 'nowprinting_3']:
                    if not self.is_content_length_in_range(image_url, more_than_amount=39000):
                        continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception('Blu-ray')

        # Gallery
        gallery_folder = self.create_custom_directory(folder.split('/')[-1] + '/gallery')
        gallery_url = self.PAGE_PREFIX + 'gallery/'
        template = self.PAGE_PREFIX + 'assets/img/gallery/%s.jpg'
        try:
            soup = self.get_soup(gallery_url)
            images = soup.select('.gallery__lists a[data-imgname]')
            for image in images:
                image_name = image['data-imgname']
                image_url = template % image_name
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(gallery_folder)
        except Exception as e:
            self.print_exception(e, 'Gallery')
