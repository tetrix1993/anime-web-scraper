import os
import anime.constants as constants
from anime.main_download import MainDownload
from datetime import datetime
from scan import AniverseMagazineScanner, MocaNewsScanner, WebNewtypeScanner, NatalieScanner


# 86 https://anime-86.com/ #エイティシックス @anime_eightysix
# Dragon, Ie wo Kau https://doraie.com/ #ドラ家 @anime_doraie
# Fumetsu no Anata e https://anime-fumetsunoanatae.com/ #不滅のあなたへ @nep_fumetsu
# Hige wo Soru. Soshite Joshikousei wo Hirou. http://higehiro-anime.com/ #higehiro #ひげひろ @higehiro_anime
# Ijiranaide, Nagatoro-san https://www.nagatorosan.jp/ #長瀞さん @nagatoro_tv
# Isekai Maou to Shoukan Shoujo no Dorei Majutsu Ω https://isekaimaou-anime.com/ #異世界魔王 @isekaimaou
# Kyuukyoku Shinka Shita Full Dive RPG ga Genjitsu Yori mo Kusogee Dattara https://fulldive-rpg.com/ #フルダイブ @fulldive_anime
# Mairimashita! Iruma-kun S2 https://www6.nhk.or.jp/anime/program/detail.html?i=iruma #魔入りました入間くん @wc_mairuma
# Osananajimi ga Zettai ni Makenai Love Comedy https://osamake.com/ #おさまけ #osamake
# Sayonara Watashi no Cramer https://sayonara-cramer.com/tv/ #さよなら私のクラマー @cramer_pr
# Seijo no Maryoku wa Bannou Desu https://seijyonomaryoku.jp/ #seijyonoanime @seijyonoanime
# Sentouin, Hakenshimasu! https://kisaragi-co.jp/ #sentoin @sentoin_anime
# Shadows House https://shadowshouse-anime.com/ #シャドーハウス @shadowshouse_yj
# Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita https://slime300-anime.com/ #スライム倒して300年 @slime300_PR
# SSSS.Dynazenon https://dynazenon.net/ #SSSS_DYNAZENON @SSSS_PROJECT
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
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index', diff=2)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        stop = False
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            for page in range(1, 100, 1):
                page_url = news_url
                if page > 1:
                    page_url = news_url + '?p=' + str(page)
                soup = self.get_soup(page_url, decode=True)
                lis = soup.find_all('li', class_='c-list__item')
                for li in lis:
                    tag_date = li.find('div', class_='c-list__item-date')
                    tag_title = li.find('div', class_='c-list__item-title')
                    a_tag = li.find('a')
                    if tag_date and tag_title and a_tag and a_tag.has_attr('href'):
                        article_id = news_url + a_tag['href'].replace('./', '')
                        date = tag_date.text.strip()
                        title = tag_title.text.strip()
                        if news_obj and (news_obj['id'] == article_id or date < news_obj['date']):
                            stop = True
                            break
                        results.append(self.create_news_log_object(date, title, article_id))
                if stop:
                    break
                next_page_tag = soup.select('div.c-pagination__arrow.-next')
                if len(next_page_tag) == 0:
                    break
                if next_page_tag[0].has_attr('class') and 'is-disable' in next_page_tag[0]['class']:
                    break
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - News')
            print(e)

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
        folder = self.create_media_directory()
        valentine_01_url = 'http://brightcove04.brightcove.com/34/4929511769001/202102/551/4929511769001_6230722968001_6230722910001.mp4?pubId=4929511769001&videoId=6230722910001'
        valentine_ex_url = 'http://brightcove04.brightcove.com/34/4929511769001/202102/1719/4929511769001_6230723857001_6230722072001.mp4?pubId=4929511769001&videoId=6230722072001'
        self.download_content(valentine_01_url, folder + '/valentine_01.mp4')
        self.download_content(valentine_ex_url, folder + '/valentine_ex.mp4')


# Dragon, Ie wo Kau
class DoraieDownload(Spring2021AnimeDownload):
    title = 'Dragon, Ie wo Kau'
    keywords = [title, 'Dragon Goes House-Hunting', 'Doraie']
    folder_name = 'doraie'

    PAGE_PREFIX = 'https://doraie.com/'
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'story/img/%s/%s_%s.jpg'
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

    def download_episode_preview_external(self):
        jp_title = 'ドラゴン、家を買う。'
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE, min_width=1200, end_date='20210330').run()

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        try:
            soup = self.get_soup(news_url)
            articles = soup.find_all('article', class_='news-item')
            news_obj = self.get_last_news_log_object()
            results = []
            for article in articles:
                tag_date = article.find('span', class_='news-item__date')
                tag_title = article.find('span', class_='news-item__title')
                a_tag = article.find('a', class_='news-item__link')
                if tag_date and tag_title and a_tag and a_tag.has_attr('href'):
                    article_id = a_tag['href']
                    if article_id.startswith('/'):
                        article_id = article_id[1:]
                    article_id = self.PAGE_PREFIX + article_id
                    date = self.format_news_date(tag_date.text.strip())
                    if len(date) == 0:
                        continue
                    title = tag_title.text.strip()
                    if news_obj and (news_obj['id'] == article_id or date < news_obj['date']):
                        break
                    results.append(self.create_news_log_object(date, title, article_id))
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - News')
            print(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv2', self.PAGE_PREFIX + 'news/wp/wp-content/uploads/2020/11/7e7632e1c37c768e225d8f78d1a5a6f3.jpg')
        self.add_to_image_list('kv3', self.PAGE_PREFIX + 'news/wp/wp-content/uploads/2021/03/22c816279916034a8e5490b4d831d432.jpg')
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


# Fumetsu no Anata e
class FumetsuNoAnataeDownload(Spring2021AnimeDownload):
    title = 'Fumetsu no Anata e'
    keywords = [title, 'To Your Eternity']
    folder_name = 'fumetsunoanatae'

    PAGE_PREFIX = 'https://anime-fumetsunoanatae.com'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        json_url = self.PAGE_PREFIX + '/assets/data/story-ja.json'
        image_url_template = self.PAGE_PREFIX + '/story/images/%s_%s/%s.png'
        self.image_list = []
        try:
            json_obj = self.get_json(json_url)
            if 'list' in json_obj and isinstance(json_obj['list'], list):
                for obj in json_obj['list']:
                    if 'series' in obj and 'episodes' in obj and isinstance(obj['series'], int)\
                            and isinstance(obj['episodes'], int):
                        episode = str(obj['episodes']).zfill(2)
                        if self.is_image_exists(episode + '_1'):
                            continue
                        for i in range(3):
                            image_url = image_url_template % (str(obj['series']), str(obj['episodes']), str(i + 1))
                            image_name = episode + '_' + str(i + 1)
                            self.add_to_image_list(image_name, image_url)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)
        self.download_image_list(self.base_folder)

    def download_news(self):
        json_url = self.PAGE_PREFIX + '/assets/data/topics-ja.json'
        news_obj = self.get_last_news_log_object()
        try:
            json_obj = self.get_json(json_url)
            results = []
            topics = json_obj['topics']
            for topic in topics:
                try:
                    date = self.format_news_date(topic['date'])
                    if len(date) == 0:
                        continue
                    title = topic['text'].strip()
                    article_id = ''
                    if len(topic['url'].strip()) > 0:
                        article_id = self.PAGE_PREFIX + topic['url'].strip()
                    if news_obj and ((news_obj['id'] == article_id and news_obj['title'] == title)
                                     or date < news_obj['date'] ):
                        break
                    results.append(self.create_news_log_object(date, title, article_id))
                except:
                    continue
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - News")
            print(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv', self.PAGE_PREFIX + '/assets/images/top/top-kv_ja.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        json_url = self.PAGE_PREFIX + '/assets/data/character-ja.json'
        image_url_template = self.PAGE_PREFIX + '/assets/images/characters/%s.png'
        self.image_list = []
        try:
            json_obj = self.get_json(json_url)
            if 'list' in json_obj and isinstance(json_obj['list'], list):
                for obj in json_obj['list']:
                    if 'img_body' in obj:
                        image_name = obj['img_body']
                        if self.is_image_exists(image_name, folder):
                            continue
                        image_url = image_url_template % image_name
                        self.add_to_image_list(image_name, image_url)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
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
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index', diff=2)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        try:
            soup = self.get_soup(news_url, decode=True)
            ul = soup.find('ul', class_='news')
            if not ul:
                return
            lis = ul.find_all('li')
            news_obj = self.get_last_news_log_object()
            results = []
            for li in lis:
                if not li.has_attr('id'):
                    continue
                tag_date = li.find('span')
                tag_title = li.find('h3')
                if tag_date and tag_title:
                    article_id = li['id']
                    date = self.format_news_date(tag_date.text)
                    if len(date) == 0:
                        continue
                    title = tag_title.text.split(tag_date.text)[1].strip()
                    if news_obj and (news_obj['id'] == article_id or date < news_obj['date']):
                        break
                    results.append(self.create_news_log_object(date, title, article_id))
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - News')
            print(e)

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

    def download_media(self):
        folder = self.create_media_directory()
        self.image_list = []
        self.add_to_image_list('music_ed', 'https://pbs.twimg.com/media/ExEnxiIVoAkofD0?format=jpg&name=large')
        self.download_image_list(folder)


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
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        story_prefix = self.PAGE_PREFIX + 'story/'
        self.image_list = []
        try:
            soup = self.get_soup(story_prefix)
            links = soup.select('div.navi ul li a')
            for link in links:
                if link.has_attr('href'):
                    if link['href'].startswith('introduction'):
                        continue
                    try:
                        episode = str(int(link.text)).zfill(2)
                    except:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    episode_soup = soup
                    if link['href'] != './':
                        episode_soup = self.get_soup(story_prefix + link['href'])
                    if episode_soup:
                        images = episode_soup.select('div.story ul.image li img')
                        for i in range(len(images)):
                            if images[i].has_attr('src'):
                                image_name = episode + '_' + str(i + 1)
                                image_url = self.PAGE_PREFIX + images[i]['src'].replace('../', '')
                                self.add_to_image_list(image_name, image_url)
                        self.download_image_list(self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        try:
            soup = self.get_soup(news_url, decode=True)
            ul = soup.find('ul', class_='list')
            if not ul:
                return
            lis = ul.find_all('li')
            news_obj = self.get_last_news_log_object()
            results = []
            for li in lis:
                tag_date = li.find('time')
                tag_title = li.find('p')
                a_tag = li.find('a')
                if tag_date and tag_title and a_tag and a_tag.has_attr('href'):
                    article_id = news_url + a_tag['href']
                    date = tag_date.text.strip().replace('-', '.')
                    title = tag_title.text.strip()
                    if news_obj and (news_obj['id'] == article_id or date < news_obj['date']):
                        break
                    results.append(self.create_news_log_object(date, title, article_id))
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - News')
            print(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/Eb6NC6rU0AAoaUm?format=jpg&name=medium')
        self.add_to_image_list('mainimg', self.PAGE_PREFIX + 'images/mainimg.jpg')
        self.add_to_image_list('kv1', 'https://pbs.twimg.com/media/EmIPL3dU0AABjQI?format=jpg&name=medium')
        self.add_to_image_list('kv1_2', self.PAGE_PREFIX + 'img/top/mainimg.jpg')
        self.add_to_image_list('kv2', 'https://pbs.twimg.com/media/ExXb2leUYAQuyZA?format=jpg&name=medium')
        #self.add_to_image_list('kv2', self.PAGE_PREFIX + 'img/news/img_visual2.jpg')
        self.download_image_list(folder)

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

    def download_media(self):
        folder = self.create_media_directory()
        self.image_list = []
        self.add_to_image_list('music_op', 'https://pbs.twimg.com/media/Es0lBfcUcAMusgu?format=jpg&name=medium')
        self.add_to_image_list('music_ed', self.PAGE_PREFIX + 'img/music/KICM-3365.jpg')
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
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        stop = False
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            for page in range(1, 100, 1):
                page_url = news_url
                if page > 1:
                    page_url = news_url + 'page/' + str(page) + '/'
                soup = self.get_soup(page_url, decode=True)
                articles = soup.find_all('article', class_='md-newsblock')
                for article in articles:
                    tag_date = article.find('div', class_='date')
                    tag_title = article.find('h3', class_='ttl')
                    a_tag = article.find('a')
                    if tag_date and tag_title and a_tag and a_tag.has_attr('href'):
                        article_id = a_tag['href']
                        date = tag_date.text.strip()
                        title = tag_title.text.strip()
                        if news_obj and (news_obj['id'] == article_id or date < news_obj['date']):
                            stop = True
                            break
                        results.append(self.create_news_log_object(date, title, article_id))
                if stop:
                    break
                pagination = soup.select('ul.pagenation-list li')
                if len(pagination) == 0:
                    break
                if pagination[-1].has_attr('class') and 'is__current' in pagination[-1]['class']:
                    break
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - News')
            print(e)

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
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_guess()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story.html', decode=True)
            ep_list = soup.select('div.story_navi ul.cf li a')
            for ep in ep_list:
                if not ep.has_attr('href'):
                    continue
                try:
                    episode = str(int(ep.text.strip().split('#')[1])).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                ep_soup = self.get_soup(self.PAGE_PREFIX + ep['href'])
                if ep_soup:
                    images = ep_soup.select('ul.story_large_img li img')
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

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'img/story/ep%s_img%s.jpg'
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            ep_num = str(i + 1)
            url_template = template % (ep_num, '%s')
            result = self.download_by_template(folder, url_template, 2, start=1, end=self.IMAGES_PER_EPISODE)
            if not result:
                break

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news.html'
        try:
            soup = self.get_soup(news_url, decode=True)
            lis = soup.select('div.page_contents_wrapper.cf ul li')
            news_obj = self.get_last_news_log_object()
            results = []
            for li in lis:
                tag_date = li.find('p', class_='page_news_date')
                tag_title = li.find('p', class_='page_news_title')
                a_tag = li.find('a')
                if tag_date and tag_title and a_tag and a_tag.has_attr('href'):
                    article_id = self.PAGE_PREFIX + a_tag['href']
                    date = tag_date.text.strip().replace(' ', '')
                    title = tag_title.text.strip()
                    if news_obj and (news_obj['id'] == article_id or date < news_obj['date']):
                        break
                    results.append(self.create_news_log_object(date, title, article_id))
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - News')
            print(e)

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

    def download_media(self):
        folder = self.create_media_directory()
        for page in ['bluray', 'music']:
            page_url = self.PAGE_PREFIX + '/%s.html' % page
            try:
                self.image_list = []
                soup = self.get_soup(page_url)
                images = soup.select('#page_contents img')
                for image in images:
                    if image.has_attr('src'):
                        if image['src'].endswith('music_jake_cs.jpg'):
                            continue
                        image_url = self.PAGE_PREFIX + image['src'].replace('./', '')
                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                        self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
            except Exception as e:
                display = 'Blu-Ray'
                if display == 'music':
                    display = 'Music'
                print("Error in running " + self.__class__.__name__ + ' - ' + display)
                print(e)


# Mairimashita! Iruma-kun 2nd Season
class IrumaKun2Download(Spring2021AnimeDownload):
    title = "Mairimashita! Iruma-kun 2nd Season"
    keywords = ["Mairimashita! Iruma-kun", "Welcome to Demon School! Iruma-kun", "Irumakun"]
    folder_name = 'iruma-kun2'

    IMAGE_PREFIX = 'https://www6.nhk.or.jp/anime/program/common/images/iruma/'
    FINAL_EPISODE = 23

    def __init__(self):
        super().__init__()

    def run(self):
        pass
        #self.download_episode_preview()

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
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news.html'
        try:
            soup = self.get_soup(news_url, decode=True)
            articles = soup.find_all('article', class_='content-entry')
            news_obj = self.get_last_news_log_object()
            results = []
            for article in articles:
                if not article.has_attr('id'):
                    continue
                tag_date = article.find('div', class_='entry-date')
                tag_title = article.find('h2', class_='entry-title')
                if tag_date and tag_title:
                    article_id = article['id']
                    date = self.format_news_date(tag_date.text.strip())
                    if len(date) == 0:
                        continue
                    title = tag_title.text.strip()
                    if news_obj and (news_obj['id'] == article_id or date < news_obj['date']):
                        break
                    results.append(self.create_news_log_object(date, title, article_id))
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - News')
            print(e)

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

    def download_media(self):
        folder = self.create_media_directory()
        for page in ['bddvd', 'music']:
            page_url = self.PAGE_PREFIX + '/%s.html' % page
            try:
                self.image_list = []
                soup = self.get_soup(page_url)
                articles = soup.select('#Entries article')
                for article in articles:
                    if article.has_attr('id'):
                        id_ = article['id']
                        if id_.upper() == 'BNF':
                            if page == 'bddvd':
                                id_ = 'bd_' + id_
                            else:
                                id_ = 'music_' + id_
                        images = article.select('img')
                        for image in images:
                            if image.has_attr('src'):
                                if image['src'].endswith('np.png'):
                                    continue
                                image_url = self.PAGE_PREFIX + image['src'].replace('./', '')
                                image_name = id_ + '_' + self.extract_image_name_from_url(image_url,
                                                                                          with_extension=False)
                                self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
            except Exception as e:
                display = 'Blu-Ray'
                if display == 'music':
                    display = 'Music'
                print("Error in running " + self.__class__.__name__ + ' - ' + display)
                print(e)


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
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX + 'tv/', 'index')

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        stop = False
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            for page in range(1, 100, 1):
                page_url = news_url
                if page > 1:
                    page_url = news_url + 'page/' + str(page) + '/'
                soup = self.get_soup(page_url, decode=True)
                articles = soup.find_all('article', class_='news-main__block')
                for article in articles:
                    tag_date = article.select('div.news-main__block--date span')
                    tag_title = article.find('div', class_='ttl')
                    a_tag = article.find('a')
                    if len(tag_date) > 0 and tag_title and a_tag and a_tag.has_attr('href'):
                        article_id = a_tag['href']
                        date = tag_date[0].text.strip()
                        title = tag_title.text.strip()
                        if news_obj and (news_obj['id'] == article_id or date < news_obj['date']):
                            stop = True
                            break
                        results.append(self.create_news_log_object(date, title, article_id))
                if stop:
                    break
                pagination = soup.select('ul.pagenation-list li')
                if len(pagination) == 0:
                    break
                if pagination[-1].has_attr('class') and 'is__current' in pagination[-1]['class']:
                    break
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - News')
            print(e)

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


# Seijo no Maryoku wa Bannou Desu
class SeijonoMaryokuDownload(Spring2021AnimeDownload):
    title = 'Seijo no Maryoku wa Bannou Desu'
    keywords = [title, 'seijonomaryoku', 'seijyonomaryoku', "The Saint's Magic Power is Omnipotent"]
    folder_name = 'seijyonomaryoku'

    PAGE_PREFIX = 'https://seijyonomaryoku.jp/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        self.image_list = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story.php')
            images = soup.find_all('img', class_='m-story-article-img')
            current_episode = None
            count = 1
            for image in images:
                if image and image.has_attr('src'):
                    split1 = image['src'].split('/')
                    if len(split1) == 4:
                        try:
                            episode = str(int(split1[2])).zfill(2)
                        except:
                            continue
                        if self.is_image_exists(episode + '_1'):
                            continue
                        if current_episode is None or current_episode != episode:
                            current_episode = episode
                            count = 1
                        else:
                            count += 1
                        image_url = self.PAGE_PREFIX + image['src']
                        image_name = episode + '_' + str(count)
                        self.add_to_image_list(image_name, image_url)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)
        self.download_image_list(self.base_folder)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news.php'
        try:
            soup = self.get_soup(news_url, decode=True)
            articles = soup.find_all('article', class_='m-newspage-article')
            news_obj = self.get_last_news_log_object()
            results = []
            for article in articles:
                if not article.has_attr('id'):
                    continue
                tag_date = article.find('time', class_='m-newspage-article-time')
                tag_title = article.find('h1', class_='m-newspage-article-heading')
                if tag_date and tag_title and tag_date.has_attr('datetime'):
                    article_id = article['id']
                    date = tag_date['datetime'].strip().replace('-', '.')
                    title = tag_title.text.strip()
                    if news_obj and (news_obj['id'] == article_id or date < news_obj['date']):
                        break
                    results.append(self.create_news_log_object(date, title, article_id))
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - News')
            print(e)

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

    def download_media(self):
        folder = self.create_media_directory()
        self.image_list = []
        self.add_to_image_list('music_op', self.PAGE_PREFIX + 'images/music/blessing/blessing_back.jpg')
        self.add_to_image_list('music_ed', self.PAGE_PREFIX + 'images/music/page-for-tomorrow/pagefortomorrow.jpg')
        self.download_image_list(folder)


# Sentouin, Hakenshimasu!
class SentoinDownload(Spring2021AnimeDownload):
    title = "Sentouin, Hakenshimasu!"
    keywords = [title, "Sentoin", "Combatants Will Be Dispatched!"]
    folder_name = 'sentoin'

    PAGE_PREFIX = 'https://kisaragi-co.jp/'
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
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            for j in range(self.IMAGES_PER_EPISODE):
                image_name = episode + '_' + str(j + 1)
                image_url = self.PAGE_PREFIX + 'assets/story/%s_%s.jpg' % (str(i + 1), str(j + 1))
                result = self.download_image(image_url, self.base_folder + '/' + image_name)
                if result == -1:
                    return

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news.html'
        try:
            soup = self.get_soup(news_url, decode=True)
            articles = soup.find_all('article', class_='content-entry')
            news_obj = self.get_last_news_log_object()
            results = []
            for article in articles:
                if not article.has_attr('id'):
                    continue
                tag_date = article.find('div', class_='entry-date')
                tag_title = article.find('h2', class_='entry-title')
                if tag_date and tag_title:
                    article_id = article['id']
                    date = self.format_news_date(tag_date.text.strip())
                    if len(date) == 0:
                        continue
                    title = tag_title.text.strip()
                    if news_obj and (news_obj['id'] == article_id or date < news_obj['date']):
                        break
                    results.append(self.create_news_log_object(date, title, article_id))
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - News')
            print(e)

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
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        stop = False
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            for page in range(1, 100, 1):
                page_url = news_url
                if page > 1:
                    page_url = news_url + '?p=' + str(page)
                soup = self.get_soup(page_url, decode=True)
                lis = soup.find_all('li', class_='p-news__item')
                for li in lis:
                    tag_date = li.find('div', class_='p-news__date')
                    tag_title = li.find('div', class_='p-news__title')
                    a_tag = li.find('a')
                    if tag_date and tag_title and a_tag and a_tag.has_attr('href'):
                        article_id = news_url + a_tag['href'].replace('./', '')
                        date = tag_date.text.strip()
                        title = tag_title.text.strip()
                        if news_obj and (news_obj['id'] == article_id or date < news_obj['date']):
                            stop = True
                            break
                        results.append(self.create_news_log_object(date, title, article_id))
                if stop:
                    break
                pagination_lis = soup.select('ul.c-pager__list li.c-pager__item')
                if len(pagination_lis) == 0:
                    break
                if 'is-current' in pagination_lis[-1]['class']:
                    break
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - News')
            print(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'assets/img/img_kv_pc.jpg')
        self.add_to_image_list('kv', self.PAGE_PREFIX + 'assets/img/top/main/img_kv.jpg')
        self.add_to_image_list('kv_1', 'https://pbs.twimg.com/media/Ev84_PFVkAELn9Q?format=jpg&name=medium')
        #self.add_to_image_list('kv_1', self.PAGE_PREFIX + 'news/SYS/CONTENTS/2021030812263644689389')
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
    keywords = [title, "I've Been Killing Slimes for 300 Years and Maxed Out My Level", "Slime 300", "slime300"]
    folder_name = 'slime300'

    PAGE_PREFIX = 'https://slime300-anime.com'

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
        json_url = self.PAGE_PREFIX + '/page-data/news/page-data.json'
        news_obj = self.get_last_news_log_object()
        try:
            json_obj = self.get_json(json_url)
            results = []
            nodes = json_obj['result']['data']['allContentfulNews']['nodes']
            for node in nodes:
                try:
                    date = node['date']
                    title = node['title']
                    article_id = self.PAGE_PREFIX + '/news/' + node['slug']
                    if news_obj and (news_obj['id'] == article_id or date < news_obj['date']):
                        break
                    results.append(self.create_news_log_object(date, title, article_id))
                except:
                    continue
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - News")
            print(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        #self.image_list = []
        #self.add_to_image_list('keyvisual01', self.PAGE_PREFIX + '/static/8e3ba0a8b42628959e71b7f52c737a6a/eeb1b/keyvisual01.png')
        #self.add_to_image_list('keyvisual02', self.PAGE_PREFIX + '/static/a2a5d8a583acad23e9276580866d3aac/eeb1b/keyvisual02.png')
        #self.add_to_image_list('keyvisual03', self.PAGE_PREFIX + '/static/a03236e46bc620b60292da71514f9253/40ffe/keyvisual03.png')
        #self.add_to_image_list('keyvisual04', self.PAGE_PREFIX + '/static/98f5d8537a23ebf5b357bac8d63fcf39/eeb1b/keyvisual04.png')
        #self.download_image_list(folder)

        page_data_url = self.PAGE_PREFIX + '/page-data/index/page-data.json'
        self.image_list = []
        try:
            data_obj = self.get_json(page_data_url)
            hash_ = data_obj['staticQueryHashes'][-1]
            kv_json = self.PAGE_PREFIX + ('/page-data/sq/d/%s.json' % hash_.strip())
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
        page_data_url = self.PAGE_PREFIX + '/page-data/character/page-data.json'
        try:
            data_obj = self.get_json(page_data_url)
            hash_ = data_obj['staticQueryHashes'][-1]
            chara_json = self.PAGE_PREFIX + ('/page-data/sq/d/%s.json' % hash_.strip())
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


# SSSS.Dynazenon
class SsssDynazenonDownload(Spring2021AnimeDownload):
    title = 'SSSS.Dynazenon'
    keywords = [title]
    folder_name = 'ssss-dynazenon'

    PAGE_PREFIX = 'https://dynazenon.net/'
    FINAL_EPISODE = 13

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        story_prefix = self.PAGE_PREFIX + 'story/'
        json_url = story_prefix + 'episode_data.php'
        self.image_list = []
        try:
            json_obj = self.get_json(json_url)
            if isinstance(json_obj, list):
                for ep_obj in json_obj:
                    if 'number' in ep_obj and 'images' in ep_obj and isinstance(ep_obj['images'], list):
                        try:
                            episode = str(int(ep_obj['number'])).zfill(2)
                        except:
                            continue
                        if self.is_image_exists(episode + '_1'):
                            continue
                        for i in range(len(ep_obj['images'])):
                            image_url = story_prefix + ep_obj['images'][i].split('?')[0]
                            image_name = episode + '_' + str(i + 1)
                            self.add_to_image_list(image_name, image_url)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)
        self.download_image_list(self.base_folder)

    def download_episode_preview_external(self):
        jp_title = 'SSSS.DYNAZENON'
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE, suffix='回', min_width=1200, end_date='20210328').run()

    def download_news(self):
        prefix = 'https://gridman.net'
        news_url = prefix + '/news/'
        stop = False
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            for page in range(1, 100, 1):
                page_url = news_url
                if page > 1:
                    page_url = news_url + 'page/' + str(page)
                soup = self.get_soup(page_url, decode=True)
                articles = soup.find_all('article', class_='c-entry-item')
                for article in articles:
                    if article.find('span', class_='c-entry-tag__item--dynazenon') is None:
                        continue
                    tag_date = article.find('span', class_='c-entry-date')
                    tag_title = article.find('h1', class_='c-entry-item__title')
                    a_tag = article.find('a', class_='c-entry-item__link')
                    if tag_date and tag_title and a_tag and a_tag.has_attr('href'):
                        article_id = prefix + a_tag['href']
                        date = self.format_news_date(tag_date.text)
                        if len(date) == 0:
                            continue
                        title = tag_title.text.strip()
                        if news_obj and (news_obj['id'] == article_id or date < news_obj['date']):
                            stop = True
                            break
                        results.append(self.create_news_log_object(date, title, article_id))
                        if article_id == 'https://gridman.net/news/archives/1502':
                            stop = True
                            break
                if stop or soup.find('i', class_='i-arrows-angle-2-r') is None:
                    break
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - News')
            print(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'img/home/visual_01.jpg')
        self.add_to_image_list('kv2', self.PAGE_PREFIX + 'img/home/visual_02.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        char_url = self.PAGE_PREFIX + 'character/'
        json_url = char_url + 'chara_data.php'
        self.image_list = []
        try:
            json_obj = self.get_json(json_url)
            if 'charas' in json_obj and isinstance(json_obj['charas'], list):
                for chara in json_obj['charas']:
                    if 'images' in chara and 'visual' in chara['images']:
                        image_url = char_url + chara['images']['visual'].split('?')[0]
                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                        self.add_to_image_list(image_name, image_url)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)
        self.download_image_list(folder)


# Super Cub
class SuperCubDownload(Spring2021AnimeDownload):
    title = 'Super Cub'
    keywords = [title, 'Supercub']
    folder_name = 'supercub'

    PAGE_PREFIX = 'https://supercub-anime.com/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        stop = False
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            page_url = news_url
            for page in range(1, 100, 1):
                soup = self.get_soup(page_url, decode=True)
                list_div = soup.find('div', id='list_01')
                if not list_div:
                    continue
                trs = list_div.find_all('tr')
                for tr in trs:
                    tag_date = tr.find('td', class_='day')
                    tag_title = tr.find('div', class_='title')
                    a_tag = tr.find('a')
                    if tag_date and tag_title:
                        article_id = ''
                        if a_tag and a_tag.has_attr('href'):
                            article_id = self.PAGE_PREFIX + a_tag['href'].replace('../', '')
                        date = tag_date.text.replace('/', '.')
                        title = tag_title.text.strip()
                        if news_obj and ((news_obj['id'] == article_id and news_obj['title'] == title)
                                         or date < news_obj['date']):
                            stop = True
                            break
                        results.append(self.create_news_log_object(date, title, article_id))
                if stop:
                    break
                nb_nex = soup.find('li', class_='nb_nex')
                if nb_nex is None:
                    break
                nb_nex_a_tag = nb_nex.find('a')
                if nb_nex_a_tag is None or not nb_nex_a_tag.has_attr('href'):
                    break
                page_url = self.PAGE_PREFIX + nb_nex_a_tag['href'].replace('../', '')
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - News')
            print(e)

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
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        stop = False
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            for page in range(1, 100, 1):
                page_url = news_url
                if page > 1:
                    page_url = news_url + '?p=' + str(page)
                soup = self.get_soup(page_url, decode=True)
                lis = soup.find_all('li', class_='p-news__item')
                for li in lis:
                    tag_date = li.find('div', class_='p-news__date')
                    tag_title = li.find('div', class_='p-news__title')
                    a_tag = li.find('a')
                    if tag_date and tag_title and a_tag and a_tag.has_attr('href'):
                        article_id = news_url + a_tag['href'].replace('./', '')
                        date = tag_date.text.strip()
                        title = tag_title.text.strip()
                        if news_obj and (news_obj['id'] == article_id or date < news_obj['date']):
                            stop = True
                            break
                        results.append(self.create_news_log_object(date, title, article_id))
                if stop:
                    break
                pagination_lis = soup.select('ul.c-pager__list li.c-pager__item')
                if len(pagination_lis) == 0:
                    break
                if 'is-current' in pagination_lis[-1]['class']:
                    break
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - News')
            print(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'assets/img/kv_pc.jpg')
        self.add_to_image_list('teaser_tw', 'https://pbs.twimg.com/media/Erv_rEcUcAMlQ3e?format=jpg&name=medium')
        self.add_to_image_list('kv2', 'https://pbs.twimg.com/media/ExcWgj9UUAEYY53?format=jpg&name=large')
        self.download_image_list(folder)
        self.download_by_template(folder, self.PAGE_PREFIX + 'assets/img/top/main/kv%s_pc.jpg')


# Yakunara Mug Cup mo
class YakunaraMugCupMoDownload(Spring2021AnimeDownload):
    title = "Yakunara Mug Cup mo"
    keywords = [title, 'Yakumo', "Let's Make a Mug Too"]
    folder_name = 'yakumo'

    PAGE_PREFIX = 'https://yakumo-project.com/'
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 5

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        # self.download_episode_preview_external()
        self.download_episode_preview_guess()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        self.image_list = []
        story_url = self.PAGE_PREFIX + 'story/'
        try:
            soup = self.get_soup(story_url)
            nav_list = soup.select('ul.story__nav li a')
            for item in nav_list:
                if item.has_attr('href') and item['href'].endswith('.php'):
                    try:
                        episode = str(int(item.text.replace('#', ''))).zfill(2)
                    except:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    episode_url = story_url + item['href'].replace('./', '')
                    episode_soup = self.get_soup(episode_url)
                    images = episode_soup.select('ul.story__anime--imgs li img')
                    for i in range(len(images)):
                        if images[i].has_attr('src'):
                            image_name = episode + '_' + str(i + 1)
                            image_url = story_url + images[i]['src'].replace('./', '')
                            self.add_to_image_list(image_name, image_url)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)
        self.download_image_list(self.base_folder)

    def download_episode_preview_external(self):
        jp_title = 'やくならマグカップも'
        NatalieScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE).run()

    def download_episode_preview_guess(self):
        self.image_list = []
        image_template = 'https://yakumo-project.com/story/images/%s_%s.jpg'
        for i in range(self.FINAL_EPISODE):
            for j in range(self.IMAGES_PER_EPISODE):
                image_name = '%s_%s' % (str(i + 1).zfill(2), str(j + 1))
                if self.is_image_exists(image_name):
                    break
                image_url = image_template % (str(i + 1).zfill(2), str(j + 1).zfill(2))
                result = self.download_image(image_url, self.base_folder + '/' + image_name)
                if result == -1:
                    return

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        stop = False
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            for page in range(1, 100, 1):
                page_url = news_url
                if page > 1:
                    page_url = news_url + '?p=' + str(page)
                soup = self.get_soup(page_url, decode=True)
                lis = soup.select('div.news__wrap li')
                for li in lis:
                    tag_date = li.find('time')
                    tag_title = li.find('p')
                    a_tag = li.find('a')
                    if tag_date and tag_title and a_tag and a_tag.has_attr('href'):
                        article_id = news_url + a_tag['href']
                        date = tag_date.text.strip()
                        title = tag_title.text.strip()
                        if news_obj and (news_obj['id'] == article_id or date < news_obj['date']):
                            stop = True
                            break
                        results.append(self.create_news_log_object(date, title, article_id))
                if stop:
                    break
                pagination_tags = soup.select('div.pagingBox span')
                if len(pagination_tags) == 0:
                    break
                if pagination_tags[-1].text.strip() == str(page):
                    break
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - News')
            print(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'news/images/200729_01.jpg')
        self.add_to_image_list('mv', self.PAGE_PREFIX + 'assets/img/mv.jpg')
        self.add_to_image_list('mv_tw', 'https://pbs.twimg.com/media/EwgkOi4UcAIxr8m?format=jpg&name=medium')
        self.add_to_image_list('mv2', self.PAGE_PREFIX + 'assets/img/mv2.jpg')
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

    def download_media(self):
        folder = self.create_media_directory()
        self.image_list = []
        self.add_to_image_list('music_op', 'https://pbs.twimg.com/media/EwgnHeUVEAcY0XX?format=jpg&name=medium')
        self.download_image_list(folder)
