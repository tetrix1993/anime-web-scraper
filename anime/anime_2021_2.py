import json
import os
from datetime import datetime
from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate3
from scan import AniverseMagazineScanner, MocaNewsScanner, WebNewtypeScanner, NatalieScanner


# 86 https://anime-86.com/ #エイティシックス @anime_eightysix
# Dragon, Ie wo Kau https://doraie.com/ #ドラ家 @anime_doraie [TUE]
# Fumetsu no Anata e https://anime-fumetsunoanatae.com/ #不滅のあなたへ @nep_fumetsu
# Hige wo Soru. Soshite Joshikousei wo Hirou. http://higehiro-anime.com/ #higehiro #ひげひろ @higehiro_anime [TUE]
# Ijiranaide, Nagatoro-san https://www.nagatorosan.jp/ #長瀞さん @nagatoro_tv [FRI]
# Isekai Maou to Shoukan Shoujo no Dorei Majutsu Ω https://isekaimaou-anime.com/ #異世界魔王 @isekaimaou [TUE]
# Kyuukyoku Shinka Shita Full Dive RPG ga Genjitsu Yori mo Kusogee Dattara https://fulldive-rpg.com/ #フルダイブ @fulldive_anime [SAT]
# Mairimashita! Iruma-kun S2 https://www.nhk.jp/p/iruma2 #魔入りました入間くん @wc_mairuma
# Odd Taxi https://oddtaxi.jp/ #オッドタクシー @oddtaxi_
# Osananajimi ga Zettai ni Makenai Love Comedy https://osamake.com/ #おさまけ #osamake [FRI]
# Sayonara Watashi no Cramer https://sayonara-cramer.com/tv/ #さよなら私のクラマー @cramer_pr [FRI]
# Seijo no Maryoku wa Bannou Desu https://seijyonomaryoku.jp/ #seijyonoanime @seijyonoanime [FRI]
# Sentouin, Hakenshimasu! https://kisaragi-co.jp/ #sentoin @sentoin_anime [THU]
# Shadows House https://shadowshouse-anime.com/1st/ #シャドーハウス @shadowshouse_yj [SAT]
# Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita https://1st.slime300-anime.com/ #スライム倒して300年 @slime300_PR [THU]
# SSSS.Dynazenon https://dynazenon.net/ #SSSS_DYNAZENON @SSSS_PROJECT [SUN]
# Super Cub https://supercub-anime.com/ #スーパーカブ @supercub_anime [FRI]
# Vivy: Fluroite Eye's Song https://vivy-portal.com/ #ヴィヴィ @vivy_portal [FRI]
# Yakunara Mug Cup mo https://yakumo-project.com/ #やくもtv @yakumo_project


# Spring 2021 Anime
class Spring2021AnimeDownload(MainDownload):
    season = "2021-2"
    season_name = "Spring 2021"
    folder_name = '2021-2'

    def __init__(self):
        super().__init__()


# 86
class EightySixDownload(Spring2021AnimeDownload, NewsTemplate):
    title = '86 -Eighty Six-'
    keywords = [title, 'Eighty Six']
    website = 'https://anime-86.com/'
    twitter = 'anime_eightysix'
    hashtags = 'エイティシックス'
    folder_name = '86'

    PAGE_PREFIX = 'https://anime-86.com/'
    FINAL_EPISODE = 26
    IMAGES_PER_EPISODE = 5

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
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            lis = soup.select('li.p-story__nav-item')
            for li in lis:
                a_tag = li.find('a')
                span = li.find('span')
                if a_tag and span:
                    try:
                        episode = str(int(span.text.strip().replace('#', ''))).zfill(2)
                    except:
                        continue
                    if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                        continue
                    ep_soup = soup
                    if 'is-current' not in li['class']:
                        if not a_tag.has_attr('href'):
                            continue
                        if a_tag['href'].startswith('/'):
                            ep_url = self.PAGE_PREFIX + a_tag['href'][1:]
                        else:
                            ep_url = self.PAGE_PREFIX + a_tag['href']
                        ep_soup = self.get_soup(ep_url)
                    images = ep_soup.select('li.p-story__img-item img')
                    self.image_list = []
                    for i in range(len(images)):
                        if images[i].has_attr('src'):
                            image_url = self.PAGE_PREFIX + images[i]['src'].replace('../', '')
                            image_name = episode + '_' + str(i + 1)
                            self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        is_success = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            start_num = None
            for j in range(self.IMAGES_PER_EPISODE):
                if self.is_image_exists(episode + '_' + str(j + 1)):
                    start_num = j + 2
                else:
                    break
            if not start_num or start_num > self.IMAGES_PER_EPISODE:
                continue
            template = self.PAGE_PREFIX + 'assets/img/story/img_ep%s-%s.jpg' % (episode, '%s')
            if not self.download_by_template(folder, template, 1, start=start_num, end=5):
                break
            print(self.__class__.__name__ + ' - Episode %s guessed correctly!' % episode)
            is_success = True
        return is_success

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, paging_type=1, article_select='li.c-list__item',
                                    date_select='div.c-list__item-date', title_select='div.c-list__item-title',
                                    id_select='a', a_tag_prefix=news_url, a_tag_replace_from='./',
                                    next_page_select='div.c-pagination__arrow.-next',
                                    next_page_eval_index_class='is-disable')

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

        # 2nd Cour
        self.add_to_image_list('c2_kv1_tw', 'https://pbs.twimg.com/media/EvxfN86U8AAoYZx?format=jpg&name=4096x4096')
        self.add_to_image_list('c2_kv1', self.PAGE_PREFIX + 'assets/img/top/img_kv-second.jpg')

        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        self.download_character2(folder)
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

    def download_character2(self, base_folder):
        folder = base_folder + '/c2'
        if not os.path.exists(folder):
            os.makedirs(folder)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/second-half/')
            figures = soup.select('div.m-chara__body figure, div.m-chara__face figure')
            self.image_list = []
            for figure in figures:
                if figure.has_attr('style'):
                    style = figure['style']
                    if style.startswith('background-image: url(../../') and style.endswith(');'):
                        image_url = self.PAGE_PREFIX + style[28:len(style) - 2]
                        image_name = self.extract_image_name_from_url(image_url)
                        self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character 2nd Cour')

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

        self.image_list = []
        self.add_to_image_list('spearhead', 'https://pbs.twimg.com/media/EzLrAlAVkAMLVso?format=jpg&name=large')
        self.add_to_image_list('bd_bonus_1', 'https://pbs.twimg.com/media/Ezlb2fZXIAASwMM?format=jpg&name=4096x4096')
        self.add_to_image_list('bd_bonus_2', 'https://pbs.twimg.com/media/EzvwlyUWQAQIa0X?format=jpg&name=4096x4096')
        self.add_to_image_list('bd_bonus_all_1', 'https://pbs.twimg.com/media/E-brhvJUYAIdmkm?format=jpg&name=4096x4096')
        self.add_to_image_list('bd_bonus_all_2', 'https://pbs.twimg.com/media/E-brhvGVkAA6Jo3?format=jpg&name=4096x4096')
        self.download_image_list(folder)

        # Blu-ray
        cache_filepath = folder + '/cache'
        if os.path.exists(cache_filepath):
            try:
                with open(cache_filepath, 'r', encoding='utf-8') as f:
                    bd_list = json.load(f)
                if not isinstance(bd_list, list):
                    bd_list = []
            except Exception:
                bd_list = []
        else:
            bd_list = []

        stop = False
        bd_urls = ['special', 'vol01', 'vol02', 'vol03', 'vol04']
        for bd_url in bd_urls:
            if bd_url.startswith('vol') and bd_url in bd_list:
                continue
            url = self.PAGE_PREFIX + 'bddvd/' + bd_url + '/'
            try:
                soup = self.get_soup(url)
                images = soup.select('div.p-bddvd img')
                self.image_list = []
                for image in images:
                    if image.has_attr('src') and '_np.jpg' not in image['src']:
                        image_url = self.PAGE_PREFIX + image['src'].replace('../../', '')
                        image_name = self.extract_image_name_from_url(image_url)
                        self.add_to_image_list(image_name, image_url)
                if bd_url.startswith('vol'):
                    if len(self.image_list) > 0:
                        bd_list.append(bd_url)
                    else:
                        stop = True
                        break
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray {bd_url}')
            if stop:
                break

        try:
            with open(cache_filepath, 'w+', encoding='utf-8') as f:
                json.dump(bd_list, f)
        except Exception as e:
            print("Error in writing to %s" % cache_filepath)
            print(e)

        # Blu-ray Guess
        templates = [self.PAGE_PREFIX + 'assets/img/bddvd/img_vol%s-1.jpg',
                     self.PAGE_PREFIX + 'assets/img/bddvd/img_vol%s-2.jpg']
        self.download_by_template(folder, templates, 2)


# Dragon, Ie wo Kau
class DoraieDownload(Spring2021AnimeDownload, NewsTemplate):
    title = 'Dragon, Ie wo Kau'
    keywords = [title, 'Dragon Goes House-Hunting', 'Doraie']
    website = 'https://doraie.com/'
    twitter = 'anime_doraie'
    hashtags = 'ドラ家'
    folder_name = 'doraie'

    PAGE_PREFIX = website
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
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE,
                                min_width=1200, end_date='20210330', download_id=self.download_id).run()

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.news-item',
                                    date_select='span.news-item__date', title_select='span.news-item__title',
                                    id_select='a.news-item__link', a_tag_prefix=self.PAGE_PREFIX,
                                    a_tag_start_text_to_remove='/', next_page_select='i.i-dot-arrow-r-12')

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
    website = 'https://anime-fumetsunoanatae.com'
    twitter = 'nep_fumetsu'
    hashtags = '不滅のあなたへ'
    folder_name = 'fumetsunoanatae'

    PAGE_PREFIX = website
    FINAL_EPISODE = 20

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_guess()
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

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        is_success = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            template = self.PAGE_PREFIX + '/story/images/1_%s/%s.png' % (str(i + 1), '%s')
            if not self.download_by_template(folder, template, 1, 1):
                break
            print(self.__class__.__name__ + ' - Episode %s guessed correctly!' % episode)
            is_success = True
        return is_success

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
                    if len(date) == 0 or date > '2022.08.30':
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
    website = 'http://higehiro-anime.com/'
    twitter = 'higehiro_anime'
    hashtags = ['higehiro', 'ひげひろ']
    folder_name = 'higehiro'

    PAGE_PREFIX = website
    FINAL_EPISODE = 13

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
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            lis = soup.select('li.slide-item')
            for li in lis:
                p_tag = li.find('p')
                if p_tag and '第' in p_tag.text and '話' in p_tag.text:
                    try:
                        episode = str(int(p_tag.text.strip().replace('第', '').replace('話', ''))).zfill(2)
                    except:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    images = li.select('ul.img')
                    if len(images) == 0:
                        images = li.select('div.images img')
                    self.image_list = []
                    for i in range(len(images)):
                        if images[i].has_attr('src'):
                            image_url = images[i]['src'].split('?')[0]
                            image_name = episode + '_' + str(i + 1)
                            self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        is_success = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            template1 = self.PAGE_PREFIX + 'wp-content/themes/higehiro/images/story/s%s-%s.jpg' % (str(i + 1), '%s')
            template2 = self.PAGE_PREFIX + 'wp-content/themes/higehiro/images/story/s%s-%s.jpg' % (episode, '%s')
            if not self.download_by_template(folder, [template1, template2], 1, start=1, end=6):
                break
            print(self.__class__.__name__ + ' - Episode %s guessed correctly!' % episode)
            is_success = True
        return is_success

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
        self.add_to_image_list('bd_bonus_toranoana', 'https://pbs.twimg.com/media/E1pQfvrUcAA4P8z?format=jpg&name=large')
        self.add_to_image_list('bd_bonus_animate', 'https://pbs.twimg.com/media/E4dq_w9UUAIErz5?format=jpg&name=large')
        self.add_to_image_list('bd_bonus_amazon_1', 'https://pbs.twimg.com/media/E4jpUOwVoAMNgim?format=jpg&name=medium')
        self.add_to_image_list('bd_bonus_amazon_2', 'https://pbs.twimg.com/media/E4jpUOzVEAIcvZK?format=jpg&name=medium')
        self.add_to_image_list('bd_bonus_sofmap', 'https://pbs.twimg.com/media/E4jpbqjUYAMU9zZ?format=jpg&name=medium')
        self.download_image_list(folder)

        # Blu-ray
        try:
            soup = self.get_soup('https://www.toei-video.co.jp/special/higehiro-anime/')
            self.image_list = []
            packages = soup.select('div.package')
            for i in range(len(packages)):
                bd_image_name = 'bd' + str(i + 1)
                if self.is_image_exists(bd_image_name, folder):
                    continue
                bd_image = packages[i].find('img')
                if bd_image and bd_image.has_attr('src'):
                    if self.is_matching_content_length(bd_image['src'], 8907):
                        continue
                    bd_image_url = bd_image['src'].split('?')[0]
                    self.add_to_image_list(bd_image_name, bd_image_url)

            images = soup.select('div.shoplist img')
            for image in images:
                if image.has_attr('src'):
                    image_url = 'https://www.toei-video.co.jp' + image['src'].split('?')[0]
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Blu-ray")
            print(e)


# Ijiranaide, Nagatoro-san
class NagatorosanDownload(Spring2021AnimeDownload, NewsTemplate):
    title = 'Ijiranaide, Nagatoro-san'
    keywords = [title, 'Nagatorosan', "Don't Toy with Me, Miss Nagatoro"]
    website = 'https://www.nagatorosan.jp/1st/'
    twitter = 'nagatoro_tv'
    hashtags = '長瀞さん'
    folder_name = 'nagatoro-san'

    PAGE_PREFIX = website

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
                    if self.is_image_exists(episode + '_5'):
                        continue
                    episode_soup = soup
                    if link['href'] != './':
                        episode_soup = self.get_soup(story_prefix + link['href'])
                    if episode_soup:
                        images = episode_soup.select('div.swiper-container.slider img')
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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ul.list li', date_select='time',
                                    title_select='p', id_select='a', a_tag_prefix=news_url, date_separator='-')

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

        # Blu-ray Bonus
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'blu-ray/tokuten.html')
            images = soup.select('div.tokuten img')
            self.image_list = []
            for image in images:
                if image.has_attr('src') and not image['src'].endswith('nowprinting.png'):
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Blu-ray Bonus")
            print(e)

        # Blu-ray
        stop = False
        for i in range(4):
            if self.is_image_exists('bd' + str(i + 1), folder):
                continue
            bd_url = self.PAGE_PREFIX + 'blu-ray/' + str(i + 1).zfill(2) + '.html'
            try:
                soup = self.get_soup(bd_url)
                prefix = 'bd' + str(i + 1)
                images = soup.select('div.detail img')
                self.image_list = []
                for j in range(len(images)):
                    if images[j].has_attr('src'):
                        if images[j]['src'].endswith('nowprinting.png'):
                            if j == 0:
                                stop = True
                                break
                            else:
                                continue
                        image_url = self.PAGE_PREFIX + images[j]['src'].replace('../', '')
                        if j == 0:
                            image_name = prefix
                        else:
                            image_name = prefix + '_' + str(j)
                        self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
                if stop:
                    break
            except Exception as e:
                print("Error in running " + self.__class__.__name__ + " - Blu-ray Bonus")
                print(e)


# Isekai Maou to Shoukan Shoujo no Dorei Majutsu Ω
class IsekaiMaou2Download(Spring2021AnimeDownload, NewsTemplate):
    title = 'Isekai Maou to Shoukan Shoujo no Dorei Majutsu 2nd Season'
    keywords = [title, "How Not to Summon a Demon Lord", "Isekaimaou"]
    website = 'https://isekaimaou-anime.com/'
    twitter = 'isekaimaou'
    hashtags = '異世界魔王'
    folder_name = 'isekai-maou2'

    PAGE_PREFIX = website
    FINAL_EPISODE = 10

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
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            lis = soup.select('nav.story--topnav li')
            for li in lis:
                em = li.find('em')
                if em:
                    try:
                        episode = str(int(em.text.strip())).zfill(2)
                    except:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    a_tag = li.find('a')
                    if a_tag and a_tag.has_attr('href'):
                        ep_soup = self.get_soup(a_tag['href'])
                        if ep_soup:
                            images = ep_soup.select('div.ss img')
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
        dt_month = datetime.now().strftime("%m").zfill(2)
        is_success = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            template = f'{self.PAGE_PREFIX}wp/wp-content/uploads/2021/{dt_month}/異世界魔王Ω_{episode}-%s.jpg'
            if not self.download_by_template(folder, template, 2, start=1, end=6):
                break
            is_success = True
            print(self.__class__.__name__ + ' - Episode %s guessed correctly!' % episode)
        return is_success

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.md-newsblock',
                                    date_select='div.date', title_select='h3.ttl', id_select='a',
                                    next_page_select='ul.pagenation-list li', next_page_eval_index_class='is__current',
                                    next_page_eval_index=-1)

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

    def download_media(self):
        folder = self.create_media_directory()
        self.image_list = []
        self.add_to_image_list('bd1_1', 'https://pbs.twimg.com/media/E2OSa-MVkAQ2x2t?format=jpg&name=medium')
        self.add_to_image_list('bd1_2', 'https://pbs.twimg.com/media/E2OSbaxUUAA_5xy?format=jpg&name=medium')
        self.add_to_image_list('bd1_3', 'https://pbs.twimg.com/media/E2eUWbLVgAUVk66?format=jpg&name=large')
        self.download_image_list(folder)

        for url in ['bd/store/', 'bd/', 'bd/vol1/', 'bd/vol2/', 'bd/vol3/']:
            bd_url = self.PAGE_PREFIX + url
            self.image_list = []
            try:
                soup = self.get_soup(bd_url)
                images = soup.select('main.bd img')
                for image in images:
                    if 'nowprinting' in image['src']:
                        continue
                    image_url = self.clear_resize_in_url(image['src'])
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            except Exception as e:
                print("Error in running " + self.__class__.__name__ + " - Media %s" % url)
                print(e)
            self.download_image_list(folder)

        # End Cards
        self.image_list = []
        self.add_to_image_list('ec01', 'https://pbs.twimg.com/media/Eyd3DA5UYAIzlMh?format=jpg&name=large')
        self.add_to_image_list('ec02', 'https://pbs.twimg.com/media/EzB7zsDVIAEdVYr?format=jpg&name=large')
        self.add_to_image_list('ec03', 'https://pbs.twimg.com/media/Ezl_TbfVIAEm0tk?format=jpg&name=large')
        self.add_to_image_list('ec04', 'https://pbs.twimg.com/media/E0I6qaZVcAk4Ib-?format=jpg&name=large')
        self.add_to_image_list('ec05', 'https://pbs.twimg.com/media/E0txjzzVUAcln7Y?format=jpg&name=large')
        self.add_to_image_list('ec06', 'https://pbs.twimg.com/media/E1SHDB-VcAEE4Bw?format=jpg&name=large')
        self.add_to_image_list('ec07', 'https://pbs.twimg.com/media/E12LK07UcAAKz6c?format=jpg&name=large')
        self.add_to_image_list('ec08_1', 'https://pbs.twimg.com/media/E2aPBxWVcAUM7Fv?format=jpg&name=large')
        self.add_to_image_list('ec08_2', 'https://pbs.twimg.com/media/E2aPCEiVUAEXiHh?format=jpg&name=large')
        self.add_to_image_list('ec09', 'https://pbs.twimg.com/media/E29wfKCVcAgAR64?format=jpg&name=large')
        self.add_to_image_list('ec10', 'https://pbs.twimg.com/media/E3h7EFkVUAIG91-?format=jpg&name=large')
        self.download_image_list(folder)


# Kyuukyoku Shinka Shita Full Dive RPG ga Genjitsu Yori mo Kusogee Dattara
class FullDiveRPGDownload(Spring2021AnimeDownload, NewsTemplate):
    title = "Kyuukyoku Shinka Shita Full Dive RPG ga Genjitsu Yori mo Kusogee Dattara"
    keywords = [title, "Fulldive", "Kiwame Quest"]
    website = 'https://fulldive-rpg.com/'
    twitter = 'fulldive_anime'
    hashtags = 'フルダイブ'
    folder_name = 'fulldive'

    PAGE_PREFIX = website
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
        is_success = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            ep_num = str(i + 1)
            url_template = template % (ep_num, '%s')
            result = self.download_by_template(folder, url_template, 2, start=1, end=self.IMAGES_PER_EPISODE)
            if not result:
                break
            print(self.__class__.__name__ + ' - Episode %s guessed correctly!' % episode)
            is_success = True
        return is_success

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='div.page_contents_wrapper.cf ul li',
                                    date_select='p.page_news_date', title_select='p.page_news_title', id_select='a',
                                    news_prefix='news.html', a_tag_prefix=self.PAGE_PREFIX)

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
    website = 'https://www.nhk.jp/p/iruma2'
    twitter = 'wc_mairuma'
    hashtags = '魔入りました入間くん'
    folder_name = 'iruma-kun2'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            divs = soup.select('div.title-desc-wrapper')
            for div in divs:
                a_tags = div.select('a')
                if len(a_tags) > 0 and a_tags[0].has_attr('href'):
                    try:
                        h3_tag = a_tags[0].select('h3')[0]
                        episode = str(int(h3_tag.text.split('(')[1].split(')')[0])).zfill(2)
                    except:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    ep_soup = self.get_soup(a_tags[0]['href'])
                    if ep_soup:
                        images = ep_soup.select('div.series-page amp-lightbox div.base-image')
                        self.image_list = []
                        for i in range(len(images)):
                            if images[i].has_attr('style') and 'background-image:url(' in images[i]['style']:
                                image_url = images[i]['style'].split('background-image:url(')[1].split(')')[0]
                                image_name = episode + '_' + str(i + 1)
                                self.add_to_image_list(image_name, image_url)
                        self.download_image_list(self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)


# Odd Taxi
class OddTaxiDownload(Spring2021AnimeDownload):
    title = 'Odd Taxi'
    keywords = [title]
    website = 'https://oddtaxi.jp/'
    twitter = 'oddtaxi_'
    hashtags = ['oddtaxi', 'オッドタクシー']
    folder_name = 'oddtaxi'

    PAGE_PREFIX = website
    JSON_URL = PAGE_PREFIX + 'wp-json/oddtaxi/init'

    def __init__(self):
        super().__init__()

    def run(self):
        json_obj = self.get_json(self.JSON_URL)
        if not json_obj:
            return
        self.download_episode_preview(json_obj)
        self.download_news(json_obj)

    def download_episode_preview(self, json_obj=None):
        if not json_obj:
            json_obj = self.get_json(self.JSON_URL)
        try:
            if json_obj:
                if 'stories' in json_obj and isinstance(json_obj['stories'], list):
                    for story in reversed(json_obj['stories']):
                        if 'images' in story and 'num' in story and isinstance(story['images'], list):
                            episode = str(story['num']).zfill(2)
                            if self.is_image_exists(episode + '_8'):
                                continue
                            images = story['images']
                            self.image_list = []
                            for i in range(len(images)):
                                if isinstance(images[i], str) and len(images[i]) > 0:
                                    image_url = self.clear_resize_in_url(images[i])
                                    image_name = episode + '_' + str(i + 1)
                                    self.add_to_image_list(image_name, image_url)
                            self.download_image_list(self.base_folder)
            else:
                raise Exception('Json Object is invalid')
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_news(self, json_obj=None):
        if not json_obj:
            json_obj = self.get_json(self.JSON_URL)
        try:
            if json_obj and 'news' in json_obj and isinstance(json_obj['news'], list):
                news_obj = self.get_last_news_log_object()
                results = []
                for article in json_obj['news']:
                    if not ('title' in article and 'date' in article and 'id' in article):
                        continue
                    date = article['date'][0:10].replace('-', '.')
                    title = ''.join(article['title'].strip())
                    article_id = self.PAGE_PREFIX + 'news/' + article['id']
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
            else:
                raise Exception('Json Object is invalid')
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - News')
            print(e)


# Osananajimi ga Zettai ni Makenai Love Comedy
class OsamakeDownload(Spring2021AnimeDownload, NewsTemplate3):
    title = 'Osananajimi ga Zettai ni Makenai Love Comedy'
    keywords = [title, 'Osamake']
    website = 'https://osamake.com/'
    twitter = 'osamake'
    hashtags = ['osamake', 'おさまけ']
    folder_name = 'osamake'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_guess()
        self.download_episode_preview_external()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story.html')
            stories = soup.select('div.story-data')
            for story in stories:
                if story.has_attr('id') and story['id'].upper() != 'S0':
                    try:
                        episode = str(int(story['id'].strip()[1:])).zfill(2)
                    except Exception:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    images = story.select('div.sld img')
                    self.image_list = []
                    for i in range(len(images)):
                        if images[i].has_attr('src'):
                            image_url = self.PAGE_PREFIX + images[i]['src'].replace('./', '')
                            image_name = episode + '_' + str(i + 1)
                            self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        is_success = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            template = self.PAGE_PREFIX + 'assets/story/%s_%s.jpg' % (str(i + 1), '%s')
            if not self.download_by_template(folder, template, 1):
                break
            print(self.__class__.__name__ + ' - Episode %s guessed correctly!' % episode)
            is_success = True
        return is_success

    def download_episode_preview_external(self):
        jp_title = '幼なじみが絶対に負けないラブコメ'
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE, min_width=800,
                                end_date='20210408', download_id=self.download_id).run()

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX)

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
class SayonaraCramerDownload(Spring2021AnimeDownload, NewsTemplate):
    title = 'Sayonara Watashi no Cramer'
    keywords = [title, 'Good-bye, Cramer!']
    website = 'https://sayonara-cramer.com/'
    twitter = 'cramer_pr'
    hashtags = 'さよなら私のクラマー'
    folder_name = 'sayonara-cramer'

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
            soup = self.get_soup(self.PAGE_PREFIX + 'tv/story/')
            ep_tags = soup.select('nav.story--nav li a')
            for ep_tag in ep_tags:
                if ep_tag.has_attr('href'):
                    span = ep_tag.find('span')
                    if span:
                        try:
                            episode = str(int(span.text.strip())).zfill(2)
                        except:
                            continue
                        if self.is_image_exists(episode + '_1'):
                            continue
                        ep_soup = self.get_soup(ep_tag['href'])
                        if ep_soup is None:
                            continue
                        self.image_list = []
                        images = ep_soup.select('div.story--main__slider--slide img')
                        for i in range(len(images)):
                            if images[i].has_attr('src'):
                                image_url = images[i]['src']
                                image_name = episode + '_' + str(i + 1)
                                self.add_to_image_list(image_name, image_url)
                        self.download_image_list(self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.news-main__block',
                                    date_select='div.news-main__block--date span', title_select='div.ttl',
                                    id_select='a', next_page_select='ul.pagenation-list li',
                                    next_page_eval_index_class='is__current', next_page_eval_index=-1)

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
class SeijonoMaryokuDownload(Spring2021AnimeDownload, NewsTemplate):
    title = 'Seijo no Maryoku wa Bannou Desu'
    keywords = [title, 'seijonomaryoku', 'seijyonomaryoku', "The Saint's Magic Power is Omnipotent"]
    website = 'https://seijyonomaryoku.jp/'
    twitter = 'seijyonoanime'
    hashtags = ['seijyonoanime', '聖女の魔力は万能です']
    folder_name = 'seijyonomaryoku'

    PAGE_PREFIX = website + '1st/'

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
            soup = self.get_soup(self.PAGE_PREFIX + 'story01.php')
            links = soup.select('div.m-story-thumbs-container a')
            for link in links:
                try:
                    episode = str(int(link.text.replace('Episode', '').strip())).zfill(2)
                except Exception:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if episode == '01':
                    ep_soup = soup
                elif link.has_attr('href'):
                    ep_soup = self.get_soup(self.PAGE_PREFIX + '/' + link['href'])
                else:
                    continue
                if ep_soup:
                    images = ep_soup.find_all('img', class_='m-story-article-img')
                    for i in range(len(images)):
                        if images[i].has_attr('src'):
                            image_url = self.PAGE_PREFIX + images[i]['src']
                            image_name = episode + '_' + str(i + 1)
                            self.add_to_image_list(image_name, image_url)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)
        self.download_image_list(self.base_folder)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.m-newspage-article',
                                    date_select='time.m-newspage-article-time',
                                    title_select='h1.m-newspage-article-heading', id_select=None, id_has_id=True,
                                    news_prefix='news.php', date_separator='-', date_attr='datetime')

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

        # Blu-ray
        stop = False
        for i in ['soft-giveaway', 'soft-campaign', 'soft01', 'soft02', 'soft03']:
            try:
                bd_vol = None
                if i in ['soft01', 'soft02', 'soft03']:
                    bd_vol = i[-1]
                    if self.is_image_exists('bd' + bd_vol, folder):
                        continue
                bd_url = self.PAGE_PREFIX + i + '.php'
                soup = self.get_soup(bd_url)
                images = soup.select('#soft img')
                self.image_list = []
                for j in range(len(images)):
                    if images[j].has_attr('src'):
                        image_url = self.PAGE_PREFIX + images[j]['src']
                        if bd_vol:
                            if 'placeholder' in image_url:
                                stop = True
                                break
                            if j == 0:
                                image_name = 'bd' + bd_vol
                            else:
                                image_name = 'bd' + bd_vol + '_' + str(j)
                        else:
                            image_name = self.extract_image_name_from_url(image_url)
                        self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
                if stop:
                    break
            except Exception as e:
                print("Error in running " + self.__class__.__name__ + " - Blu-ray %s" % i)
                print(e)


# Sentouin, Hakenshimasu!
class SentoinDownload(Spring2021AnimeDownload, NewsTemplate3):
    title = "Sentouin, Hakenshimasu!"
    keywords = [title, "Sentoin", "Combatants Will Be Dispatched!"]
    website = 'https://kisaragi-co.jp/'
    twitter = 'sentoin_anime'
    hashtags = 'sentoin'
    folder_name = 'sentoin'

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
        self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/Eqbrtf7VEAADuiD?format=jpg&name=4096x4096')
        self.add_to_image_list('teaser_1', self.PAGE_PREFIX + 'assets/top/main-t1/vis.png')
        self.add_to_image_list('topic-1', self.PAGE_PREFIX + 'assets/top/topic-1.jpg')
        self.add_to_image_list('kv1', 'https://pbs.twimg.com/media/E18L8GgVkAMJFZa?format=jpg&name=4096x4096')
        #self.add_to_image_list('kv1', self.PAGE_PREFIX + 'assets/news/kv1.jpg')
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

    def download_media(self):
        folder = self.create_media_directory()
        self.image_list = []
        self.add_to_image_list('collab_komecircus', self.PAGE_PREFIX + 'assets/news/210522-2/main.png')
        self.download_image_list(folder)

        self.image_list = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            divs = soup.select('#BddvdData div.bddvd-data')
            for div in divs:
                if div.has_attr('id'):
                    id_ = div['id']
                    images = div.select('img')
                    for image in images:
                        if image.has_attr('src'):
                            if image['src'].endswith('np.jpg'):
                                continue
                            image_url = self.PAGE_PREFIX + image['src'].replace('./', '')
                            image_name = id_ + '_' + self.extract_image_name_from_url(image_url, with_extension=False)
                            self.add_to_image_list(image_name, image_url)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Media')
            print(e)
        self.download_image_list(folder)


# Shadows House
class ShadowsHouseDownload(Spring2021AnimeDownload, NewsTemplate):
    title = "Shadows House"
    keywords = [title]
    website = 'https://shadowshouse-anime.com/1st/'
    twitter = 'shadowshouse_yj'
    hashtags = 'シャドーハウス'
    folder_name = 'shadows-house'

    PAGE_PREFIX = website

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
            story_url = self.PAGE_PREFIX + 'story/'
            soup = self.get_soup(story_url)
            lis = soup.select('div.page_tab li')
            for li in lis:
                a_tag = li.find('a')
                if a_tag and a_tag.has_attr('href'):
                    try:
                        episode = str(int(a_tag.text.strip())).zfill(2)
                    except Exception:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    if li.has_attr('class') and 'current' in li['class']:
                        ep_soup = soup
                    else:
                        ep_soup = self.get_soup(story_url + a_tag['href'].replace('./', ''))
                    if ep_soup:
                        images = ep_soup.select('div.s_image img')
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

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.p-news__item',
                                    date_select='div.p-news__date', title_select='div.p-news__title',
                                    id_select='a', paging_type=1, a_tag_prefix=news_url, a_tag_replace_from='./',
                                    next_page_select='ul.c-pager__list li.c-pager__item',
                                    next_page_eval_index_class='is-current', next_page_eval_index=-1)

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

        special_template = self.PAGE_PREFIX + 'special/shindan/assets/img/character_%s.png'
        self.download_by_template(folder, special_template, 2)

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

    def download_media(self):
        folder = self.create_media_directory()
        self.image_list = []
        self.add_to_image_list('music_ed', 'https://pbs.twimg.com/media/Ex9GZKuU4AEaMU6?format=jpg&name=large')
        self.download_image_list(folder)

        # Blu-ray
        cache_filepath = folder + '/cache'
        if os.path.exists(cache_filepath):
            try:
                with open(cache_filepath, 'r', encoding='utf-8') as f:
                    bd_list = json.load(f)
                if not isinstance(bd_list, list):
                    bd_list = []
            except Exception:
                bd_list = []
        else:
            bd_list = []

        stop = False
        bd_urls = ['special', 'music', 'vol01', 'vol02', 'vol03', 'vol04', 'vol05', 'vol06']
        for bd_url in bd_urls:
            if bd_url.startswith('vol') and bd_url in bd_list:
                continue
            if bd_url == 'music':
                url = self.PAGE_PREFIX + 'music/'
            else:
                url = self.PAGE_PREFIX + 'bddvd/' + bd_url + '/'
            try:
                soup = self.get_soup(url)
                if bd_url == 'music':
                    images = soup.select('div.p-music img')
                else:
                    images = soup.select('div.p-bddvd img')
                self.image_list = []
                for image in images:
                    if image.has_attr('src') and '_np.jpg' not in image['src']:
                        image_url = self.PAGE_PREFIX + image['src'].replace('../../', '')
                        image_name = self.extract_image_name_from_url(image_url)
                        self.add_to_image_list(image_name, image_url)
                if bd_url.startswith('vol'):
                    if len(self.image_list) > 0:
                        bd_list.append(bd_url)
                    else:
                        stop = True
                        break
                self.download_image_list(folder)
            except Exception as e:
                print("Error in running " + self.__class__.__name__ + ' - Blu-ray %s' % bd_url)
                print(e)
            if stop:
                break

        try:
            with open(cache_filepath, 'w+', encoding='utf-8') as f:
                json.dump(bd_list, f)
        except Exception as e:
            print("Error in writing to %s" % cache_filepath)
            print(e)

        # Blu-ray Guess
        template = self.PAGE_PREFIX + 'assets/img/bddvd/img_jk_vol%s.jpg'
        self.download_by_template(folder, template, 2)


# Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita
class Slime300Download(Spring2021AnimeDownload):
    title = "Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita"
    keywords = [title, "I've Been Killing Slimes for 300 Years and Maxed Out My Level", "Slime 300", "slime300"]
    website = 'https://1st.slime300-anime.com'
    twitter = 'slime300_PR'
    hashtags = 'スライム倒して300年'
    folder_name = 'slime300'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        json_url = self.PAGE_PREFIX + '/page-data/story/page-data.json'
        try:
            json_obj = self.get_json(json_url)
            edges = json_obj['result']['data']['allContentfulStory']['edges']
            for edge in edges:
                try:
                    node = edge['node']
                    episode = str(int(node['no'])).zfill(2)
                    if self.is_image_exists(episode + '_01'):
                        continue
                    images = node['images']
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = 'https:' + images[i]['fluid']['src'].split('?')[0]
                        image_name = episode + '_' + str(i + 1).zfill(2)
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
                except Exception:
                    continue
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

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
                    if date >= '2022.01.04':
                        continue
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

        self.image_list = []
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/Ej2u1tDU4AAsi_J?format=jpg&name=large')
        self.add_to_image_list('kv2_tw', 'https://pbs.twimg.com/media/Ej2u3l7U8AIfJ4w?format=jpg&name=large')
        self.add_to_image_list('kv3_tw', 'https://pbs.twimg.com/media/EtDYnPRVoAAwPdr?format=jpg&name=4096x4096')
        self.add_to_image_list('kv4_tw', 'https://pbs.twimg.com/media/EtDYnPWU0AUQCXF?format=jpg&name=4096x4096')
        self.add_to_image_list('kv5_tw', 'https://pbs.twimg.com/media/ExcpTlJUUAEm876?format=jpg&name=4096x4096')
        self.add_to_image_list('kv6_tw', 'https://pbs.twimg.com/media/EyDcmrkUcAAGNmg?format=jpg&name=4096x4096')
        self.download_image_list(folder)

        page_data_url = self.PAGE_PREFIX + '/page-data/index/page-data.json'
        self.image_list = []
        try:
            data_main_obj = self.get_json(page_data_url)
            data_obj = None
            for hash_ in data_main_obj['staticQueryHashes']:
                chara_json = self.PAGE_PREFIX + ('/page-data/sq/d/%s.json' % hash_.strip())
                data_obj = self.get_json(chara_json)['data']
                if 'logo' not in data_obj:
                    continue
                else:
                    break
            if data_obj is None:
                return
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
            data_main_obj = self.get_json(page_data_url)
            data_obj = None
            for hash_ in data_main_obj['staticQueryHashes']:
                chara_json = self.PAGE_PREFIX + ('/page-data/sq/d/%s.json' % hash_.strip())
                data_obj = self.get_json(chara_json)['data']
                if 'azusa' not in data_obj:
                    continue
                else:
                    break
            if data_obj is None:
                return
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

    def download_media(self):
        folder = self.create_media_directory()
        image_objs = []
        page_data_url = self.PAGE_PREFIX + '/page-data/bluray-cd/page-data.json'
        try:
            data_main_obj = self.get_json(page_data_url)
            data_obj = None
            for hash_ in data_main_obj['staticQueryHashes']:
                chara_json = self.PAGE_PREFIX + ('/page-data/sq/d/%s.json' % hash_.strip())
                data_obj = self.get_json(chara_json)['data']
                if 'op01' not in data_obj:
                    continue
                else:
                    break
            if data_obj is None:
                return
            for data in data_obj.keys():
                try:
                    if data in ['logo', 'nowprinting']:
                        continue
                    image_url = self.PAGE_PREFIX + data_obj[data]['childImageSharp']['fluid']['src']
                    image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                    image_objs.append({'name': image_name, 'url': image_url})
                except:
                    pass
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Media")
            print(e)
        self.download_image_objects(image_objs, folder)


# SSSS.Dynazenon
class SsssDynazenonDownload(Spring2021AnimeDownload):
    title = 'SSSS.Dynazenon'
    keywords = [title]
    website = 'https://dynazenon.net/'
    twitter = 'SSSS_PROJECT'
    hashtags = 'SSSS_DYNAZENON'
    folder_name = 'ssss-dynazenon'

    PAGE_PREFIX = website
    FINAL_EPISODE = 13

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        # self.download_episode_preview_external()
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
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE, suffix='回',
                                min_width=1200, end_date='20210328', download_id=self.download_id).run()

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
class SuperCubDownload(Spring2021AnimeDownload, NewsTemplate2):
    title = 'Super Cub'
    keywords = [title, 'Supercub']
    website = 'https://supercub-anime.com/'
    twitter = 'supercub_anime'
    hashtags = ['SuperCub', 'スーパーカブ']
    folder_name = 'supercub'

    PAGE_PREFIX = website
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
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            links = soup.select('#ContentsListUnit01 a')
            for link in links:
                if link.has_attr('href') and '第' in link.text and '話' in link.text:
                    try:
                        episode = str(int(link.text.strip().replace('第', '').replace('話', ''))).zfill(2)
                    except:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    ep_soup = self.get_soup(self.PAGE_PREFIX + link['href'].replace('../', ''))
                    if ep_soup:
                        images = ep_soup.select('ul.tp5 a')
                        self.image_list = []
                        for i in range(len(images)):
                            if images[i].has_attr('href'):
                                image_url = self.PAGE_PREFIX + images[i]['href'].replace('../', '').split('?')[0]
                                image_name = episode + '_' + str(i + 1)
                                self.add_to_image_list(image_name, image_url)
                        self.download_image_list(self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'core_sys/images/contents/%s/block/%s/%s.jpg'
        is_successful = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            is_success = False
            if self.is_image_exists(episode + '_1'):
                continue
            first = 10 + (i - 1)
            second = 38 + self.IMAGES_PER_EPISODE * (i - 1)
            third = 52 + self.IMAGES_PER_EPISODE * (i - 1)
            for j in range(self.IMAGES_PER_EPISODE):
                image_url = template % (str(first).zfill(8), str(second).zfill(8), str(third + j).zfill(8))
                image_name = episode + '_' + str(j + 1)
                result = self.download_image(image_url, folder + '/' + image_name)
                if result == 0:
                    print(self.__class__.__name__ + ' - Guessed successfully!')
                    is_success = True
                    is_successful = True
                elif result == -1:
                    break
            if not is_success:
                if len(os.listdir(folder)) == 0:
                    os.rmdir(folder)
                return
        if len(os.listdir(folder)) == 0:
            os.rmdir(folder)
        return is_successful

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv', self.PAGE_PREFIX + 'core_sys/images/main/home/kv.jpg')
        self.add_to_image_list('kv_tw', 'https://pbs.twimg.com/media/ErvAcsEUcAMljAq?format=jpg&name=4096x4096')
        self.add_to_image_list('visual01', self.PAGE_PREFIX + 'core_sys/images/news/00000011/block/00000038/00000008.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        if os.path.exists(cache_filepath):
            try:
                with open(cache_filepath, 'r', encoding='utf-8') as f:
                    chara_list = json.load(f)
                if not isinstance(chara_list, list):
                    chara_list = []
            except Exception:
                chara_list = []
        else:
            chara_list = []

        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'chara/')
            a_tags = soup.select('td.l_wdp01 a')
            for a_tag in a_tags:
                if a_tag.has_attr('href'):
                    chara = a_tag['href'].split('/')[-1].replace('.html', '')
                    if chara not in chara_list:
                        if chara == 'index':
                            chara_soup = soup
                        else:
                            chara_soup = self.get_soup(self.PAGE_PREFIX + 'chara/' + chara + '.html')
                        if chara_soup:
                            images = chara_soup.select('div.charWrap img')
                            self.image_list = []
                            for image in images:
                                if image.has_attr('src'):
                                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                                    image_name = self.extract_image_name_from_url(image_url)
                                    self.add_to_image_list(image_name, image_url)
                            self.download_image_list(folder)
                            chara_list.append(chara)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)

        try:
            with open(cache_filepath, 'w+', encoding='utf-8') as f:
                json.dump(chara_list, f)
        except Exception as e:
            print("Error in writing to %s" % cache_filepath)
            print(e)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'dbbox/')
            self.image_list = []
            images = soup.select('#cms_block img')
            for image in images:
                if image.has_attr('src') and not image['src'].endswith('.svg'):
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                    if self.is_matching_content_length(image_url, 34077):
                        continue
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Blu-Ray')
            print(e)


# Vivy: Fluorite Eye's Song
class VivyDownload(Spring2021AnimeDownload, NewsTemplate):
    title = "Vivy: Fluorite Eye's Song"
    keywords = [title, "Vivy -Fluorite Eye's Song"]
    website = 'https://vivy-portal.com/'
    twitter = 'vivy_portal'
    hashtags = 'ヴィヴィ'
    folder_name = 'vivy'

    PAGE_PREFIX = website
    FINAL_EPISODE = 13

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
            story_url = self.PAGE_PREFIX + 'story/'
            soup = self.get_soup(story_url)
            ep_items = soup.select('li.p-story__ep-item a')
            for ep_item in ep_items:
                if ep_item.has_attr('href'):
                    try:
                        str_ = ep_item['href'].split('?id=ep')[1]
                        final_str = ''
                        for s in str_:
                            if s.isdigit():
                                final_str += s
                        episode = str(int(final_str)).zfill(2)
                    except:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    self.image_list = []
                    first_image = ep_item.find('img')
                    if first_image and first_image.has_attr('src'):
                        if first_image['src'][0] == '/':
                            first_image_url = self.PAGE_PREFIX + first_image['src'][1:]
                        else:
                            first_image_url = self.PAGE_PREFIX + first_image['src']
                        self.add_to_image_list(episode + '_0', first_image_url)
                    ep_soup = self.get_soup(story_url + ep_item['href'].replace('./', ''))
                    if ep_soup:
                        images = ep_soup.select('li.p-story__detail-img-item img')
                        for i in range(len(images)):
                            if images[i].has_attr('src'):
                                image_url = story_url + 'detail/' + images[i]['src']
                                image_name = episode + '_' + str(i + 1)
                                self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'assets/img/story/cut/%s.jpg'
        is_success = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_01', folder):
                continue
            image_template = template % (episode + '_%s')
            if not self.download_by_template(folder, image_template, 2):
                break
            print(self.__class__.__name__ + ' - Episode %s guessed correctly!' % episode)
            is_success = True
        return is_success

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.p-news__item',
                                    date_select='div.p-news__date', title_select='div.p-news__title',
                                    id_select='a', paging_type=1, a_tag_prefix=news_url, a_tag_replace_from='./',
                                    next_page_select='a.c-pager__btn--prev')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'assets/img/kv_pc.jpg')
        self.add_to_image_list('teaser_tw', 'https://pbs.twimg.com/media/Erv_rEcUcAMlQ3e?format=jpg&name=medium')
        self.add_to_image_list('kv2', 'https://pbs.twimg.com/media/ExcWgj9UUAEYY53?format=jpg&name=large')
        self.download_image_list(folder)
        self.download_by_template(folder, self.PAGE_PREFIX + 'assets/img/top/main/kv%s_pc.jpg')

    def download_character(self):
        folder = self.create_character_directory()
        id_list = []
        try:
            chara_url = self.PAGE_PREFIX + 'character/'
            soup = self.get_soup(chara_url)
            char_items = soup.select('li.p-character__item a')
            for item in char_items:
                if item.has_attr('href'):
                    page_url = chara_url + item['href'].replace('./', '')
                    try:
                        id_ = page_url.split('?id=')[1]
                        id_list.append(id_)
                        if self.is_image_exists('img_' + id_, folder):
                            continue
                    except:
                        pass
                    chara_soup = self.get_soup(page_url)
                    if chara_soup:
                        images = chara_soup.select('div.p-character__detail img')
                        self.image_list = []
                        for image in images:
                            if image.has_attr('src') and len(image['src']) > 0:
                                image_url = self.PAGE_PREFIX + image['src'].replace('../../', '')
                                image_name = self.extract_image_name_from_url(image_url)
                                self.add_to_image_list(image_name, image_url)
                        self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)

        for id__ in id_list:
            if self.is_image_exists(id__ + '_01', folder):
                image_name = id__.lower() + '_%s'
                template = self.PAGE_PREFIX + 'assets/img/character/img/%s.jpg' % image_name
                self.download_by_template(folder, template, 2, 2)

    def download_media(self):
        folder = self.create_media_directory()
        self.image_list = []
        for suffix in ['music', 'bddvd']:
            try:
                soup = self.get_soup(self.PAGE_PREFIX + suffix + '/')
                if suffix == 'music':
                    images = soup.select('li.p-music__slide.js-slide img')
                else:
                    images = soup.select('li.p-bddvd__slide.js-slide img')
                for image in images:
                    if image.has_attr('src'):
                        if image['src'].startswith('/'):
                            image_url = self.PAGE_PREFIX + image['src'][1:]
                        elif image['src'].startswith('../'):
                            image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                        else:
                            image_url = self.PAGE_PREFIX + image['src']
                        image_name = suffix + '_' + self.extract_image_name_from_url(image_url)
                        self.add_to_image_list(image_name, image_url)
            except Exception as e:
                print("Error in running " + self.__class__.__name__ + ' - Media %s' % suffix)
                print(e)
        self.download_image_list(folder)


# Yakunara Mug Cup mo
class YakunaraMugCupMoDownload(Spring2021AnimeDownload, NewsTemplate):
    title = "Yakunara Mug Cup mo"
    keywords = [title, 'Yakumo', "Let's Make a Mug Too"]
    website = 'https://yakumo-project.com/'
    twitter = 'yakumo_project'
    hashtags = 'やくもtv'
    folder_name = 'yakumo'

    PAGE_PREFIX = website
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
        NatalieScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE, download_id=self.download_id).run()

    def download_episode_preview_guess(self):
        self.image_list = []
        image_template = 'https://yakumo-project.com/story/images/%s_%s.jpg'
        is_success = False
        for i in range(self.FINAL_EPISODE):
            for j in range(self.IMAGES_PER_EPISODE):
                image_name = '%s_%s' % (str(i + 1).zfill(2), str(j + 1))
                if self.is_image_exists(image_name):
                    break
                image_url = image_template % (str(i + 1).zfill(2), str(j + 1).zfill(2))
                result = self.download_image(image_url, self.base_folder + '/' + image_name)
                if result == -1:
                    return
                print(self.__class__.__name__ + ' - Episode %s guessed correctly!' % str(i + 1))
                is_success = True
        return is_success

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='div.news__wrap li',
                                    date_select='time', title_select='p', id_select='a', paging_type=1,
                                    a_tag_prefix=news_url, next_page_select='div.pagingBox span',
                                    next_page_eval_index=-1, next_page_eval_index_compare_page=True)

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
