import os
import anime.constants as constants
from anime.main_download import MainDownload

# Goblin Slayer S2 http://www.goblinslayer.jp/ #ゴブスレ @GoblinSlayer_GA
# Hataraku Maou-sama! https://maousama.jp/ #maousama @anime_maousama
# Itai no wa https://bofuri.jp/story/ #防振り #bofuri @bofuri_anime
# Kanojo mo Kanojo https://kanokano-anime.com/ #kanokano #カノジョも彼女 @kanokano_anime
# Mahouka Koukou no Yuutousei https://mahouka-yuutousei.jp/ #mahouka
# Maou Gakuin no Futekigousha 2nd Season https://maohgakuin.com/ #魔王学院 @maohgakuin
# Megami-ryou no Ryoubo-kun. https://megamiryou.com/ #女神寮 @megamiryou
# Princess Connect! Re:Dive S2 https://anime.priconne-redive.jp/ #アニメプリコネ #プリコネR #プリコネ @priconne_anime
# Seirei Gensouki https://seireigensouki.com/ #精霊幻想記 @seireigensouki
# Shikkakumon no Saikyou Kenja https://shikkakumon.com/ #失格紋 @shikkakumon_PR
# Shokei Shoujo no Virgin Road http://virgin-road.com/ #処刑少女 #shokei_anime @virginroad_GA
# Shuumatsu no Harem https://end-harem-anime.com/ #終末のハーレム @harem_official_
# Slow Loop https://slowlooptv.com/ #slowloop @slowloop_tv
# Tensai Ouji no Akaji Kokka Saisei Jutsu: Souda, Baikoku shiyou https://tensaiouji-anime.com/ #天才王子の赤字国家再生術 @tensaiouji_PR
# Tsuki to Laika to Nosferatu https://tsuki-laika-nosferatu.com/ #月とライカ @LAIKA_anime
# Vlad Love https://www.vladlove.com/index.html #ぶらどらぶ #vladlove @VLADLOVE_ANIME
# Yama no Susume: Next Summit https://yamanosusume-ns.com/ #ヤマノススメ @yamanosusume


# Unconfirmed Season Anime
class UnconfirmedDownload(MainDownload):
    season = "9999-9"
    season_name = "Unconfirmed"
    folder_name = 'unconfirmed'

    def __init__(self):
        super().__init__()


# Goblin Slayer 2nd Season
class GoblinSlayer2Download(UnconfirmedDownload):
    title = "Goblin Slayer 2nd Season"
    keywords = [title]
    folder_name = 'goblin-slayer2'

    PAGE_PREFIX = 'http://www.goblinslayer.jp/'

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
        try:
            soup = self.get_soup(news_url, decode=True)
            articles = soup.select('div.newsbox dl.news')
            news_obj = self.get_last_news_log_object()
            results = []
            for article in articles:
                tag_date = article.find('dt')
                a_tag = article.find('a')
                if tag_date and a_tag and a_tag.has_attr('href'):
                    article_id = a_tag['href']
                    date = self.format_news_date(tag_date.text.strip().replace('/', '.'))
                    if len(date) == 0:
                        continue
                    title = a_tag.text.strip()
                    if date.startswith('2020') or (news_obj and news_obj['id'] == article_id):
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
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/EtDYBThUYAEBIWI?format=jpg&name=4096x4096')
        self.download_image_list(folder)


# Hataraku Maou-sama!
class HatarakuMaousama2Download(UnconfirmedDownload):
    title = 'Hataraku Maou-sama! 2nd Season'
    keywords = [title, 'Maousama', 'The Devil is a Part-Timer!']
    folder_name = 'hataraku-maousama2'

    PAGE_PREFIX = 'https://maousama.jp/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser_tw', 'https://pbs.twimg.com/media/EvyqsA_UcAcPT9B?format=jpg&name=large')
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'assets/img/top/visual.jpg')
        self.download_image_list(folder)


# Itai no wa Iya nano de Bougyoryoku ni Kyokufuri Shitai to Omoimasu. 2nd Season
class Bofuri2Download(UnconfirmedDownload):
    title = "Itai no wa Iya nano de Bougyoryoku ni Kyokufuri Shitai to Omoimasu. 2nd Season"
    keywords = [title, 'bofuri', "BOFURI: I Don't Want to Get Hurt, so I'll Max Out My Defense.", '2nd']
    folder_name = 'bofuri2'

    PAGE_PREFIX = "https://bofuri.jp/"

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
        try:
            soup = self.get_soup(news_url, decode=True)
            articles = soup.select('section.news-data')
            news_obj = self.get_last_news_log_object()
            results = []
            for article in articles:
                tag_date = article.find('div', class_='date')
                tag_title = article.find('div', class_='title')
                a_tag = article.find('a')
                if tag_date and tag_title and a_tag and a_tag.has_attr('href'):
                    article_id = news_url + a_tag['href'].replace('./', '')
                    date = self.format_news_date(tag_date.text.strip().replace('/', '.'))
                    if len(date) == 0:
                        continue
                    title = tag_title.text.strip()
                    if date.startswith('2021.01.04') or (news_obj and news_obj['id'] == article_id):
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
        self.add_to_image_list('animation_works', 'https://pbs.twimg.com/media/ErSRQUmVoAAkgt7?format=jpg&name=large')
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/ErSKnRwW8AAjOyU?format=jpg&name=4096x4096')
        self.download_image_list(folder)


# Kanojo mo Kanojo
class KanokanoDownload(UnconfirmedDownload):
    title = 'Kanojo mo Kanojo'
    keywords = [title, 'Kanokano']
    folder_name = 'kanokano'

    PAGE_PREFIX = 'https://kanokano-anime.com/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        news_url = self.PAGE_PREFIX
        try:
            soup = self.get_soup(news_url, decode=True)
            articles = soup.select('ul.news-list li.news-list-node')
            news_obj = self.get_last_news_log_object()
            results = []
            for article in articles:
                tag_date = article.find('div', class_='news-date')
                tag_title = article.find('div', class_='news-title')
                if tag_date and tag_title:
                    article_id = ''
                    date = self.format_news_date(tag_date.text.strip().replace('/', '.'))
                    if len(date) == 0:
                        continue
                    title = tag_title.text.strip()
                    if news_obj and news_obj['date'] == date and news_obj['title'] == title:
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
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'assets/img/mv-img.png')
        self.download_image_list(folder)


# Mahouka Koukou no Yuutousei
class MahoukaYuutouseiDownload(UnconfirmedDownload):
    title = 'Mahouka Koukou no Yuutousei'
    keywords = [title, 'The Honor Student at Magic High School']
    folder_name = 'mahouka-yuutousei'

    PAGE_PREFIX = "https://mahouka-yuutousei.jp/"

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        news_url = self.PAGE_PREFIX
        try:
            soup = self.get_soup(news_url, decode=True)
            articles = soup.select('ul.p-news__list li.p-news__item')
            news_obj = self.get_last_news_log_object()
            results = []
            for article in articles:
                tag_date = article.find('div', class_='p-news__date')
                tag_title = article.find('div', class_='p-news__title')
                if tag_date and tag_title:
                    article_id = ''
                    date = self.format_news_date(tag_date.text.strip().replace('/', '.'))
                    if len(date) == 0:
                        continue
                    title = tag_title.text.strip()
                    if news_obj and news_obj['date'] == date and news_obj['title'] == title:
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
        self.add_to_image_list('teaser', self.PAGE_PREFIX + '/teaser/img/top/kv_character.png')
        self.add_to_image_list('kv1', self.PAGE_PREFIX + '/teaser/img/top/kv.jpg')
        self.download_image_list(folder)


# Maou Gakuin no Futekigousha: Shijou Saikyou no Maou no Shiso, Tensei shite Shison-tachi no Gakkou e
class Maohgakuin2Download(UnconfirmedDownload):
    title = "Maou Gakuin no Futekigousha: Shijou Saikyou no Maou no Shiso, Tensei shite Shison-tachi no Gakkou e 2nd Season"
    keywords = [title, 'Maohgakuin', 'The Misfit of Demon King Academy']
    folder_name = 'maohgakuin2'

    PAGE_PREFIX = "https://maohgakuin.com/"

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'assets/img/img_main.jpg')
        # self.add_to_image_list('teaser_tw', 'https://pbs.twimg.com/media/EvylQFOVkAID_0B?format=jpg&name=medium')
        self.download_image_list(folder)


# Megami-ryou no Ryoubo-kun.
class MegamiryouDownload(UnconfirmedDownload):
    title = 'Megami-ryou no Ryoubo-kun'
    keywords = [title, 'Megamiryou', "Mother of the Goddess' Dormitory"]
    folder_name = 'megamiryou'

    PAGE_PREFIX = 'https://megamiryou.com/'

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        news_url = self.PAGE_PREFIX
        try:
            soup = self.get_soup(news_url, decode=True)
            articles = soup.select('#nwu_001_t tr')
            news_obj = self.get_last_news_log_object()
            results = []
            for article in articles:
                tag_date = article.find('td', class_='day')
                tag_title = article.find('div', class_='title')
                a_tag = article.find('a')
                if tag_date and tag_title:
                    article_id = ''
                    if a_tag and a_tag.has_attr('href'):
                        article_id = self.PAGE_PREFIX + a_tag['href']
                    date = self.format_news_date(tag_date.text.strip().replace('/', '.'))
                    if len(date) == 0:
                        continue
                    title = tag_title.text.strip()
                    if news_obj and news_obj['id'] == article_id and news_obj['title'] == title:
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
        self.add_to_image_list('teaser_tw', 'https://pbs.twimg.com/media/EsTnmn-U0Acx83l?format=jpg&name=large')
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv_pc.png')
        self.add_to_image_list('tzOriginImg', self.PAGE_PREFIX + 'core_sys/images/main/tz/tzOriginImg.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            char_wraps = soup.find_all('div', class_='charWrap')
            for char_wrap in char_wraps:
                for char in ['charImg', 'charStand']:
                    char_class = char_wrap.find('div', class_=char)
                    if char_class:
                        images = char_class.find_all('img')
                        for image in images:
                            if image and image.has_attr('src'):
                                image_url = self.PAGE_PREFIX + image['src']
                                image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                                self.add_to_image_list(image_name, image_url)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)
        self.download_image_list(folder)


# Princess Connect! Re:Dive 2nd Season
class Priconne2Download(UnconfirmedDownload):
    title = "Princess Connect! Re:Dive 2nd Season"
    keywords = [title, "Priconne"]
    folder_name = 'priconne2'

    PAGE_PREFIX = "https://anime.priconne-redive.jp"

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        news_url = self.PAGE_PREFIX + '/news/'
        stop = False
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            for page in range(1, 100, 1):
                page_url = news_url
                if page > 1:
                    page_url = news_url + '?page=' + str(page)
                soup = self.get_soup(page_url, decode=True)
                articles = soup.select('ul.news-list li.article')
                for article in articles:
                    tag_date = article.find('p', class_='date')
                    tag_title = article.find('div', class_='desc')
                    a_tag = article.find('a')
                    if tag_date and tag_title and a_tag and a_tag.has_attr('href'):
                        article_id = self.PAGE_PREFIX + a_tag['href'].replace('../', '')
                        date = tag_date.text.strip()
                        title = tag_title.text.strip()
                        if date.startswith('2020.08.07') or (news_obj and news_obj['id'] == article_id):
                            stop = True
                            break
                        results.append(self.create_news_log_object(date, title, article_id))
                if stop or len(soup.select('div.more')) == 0:
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
        image_objs = [{'name': 'teaser', 'url': self.PAGE_PREFIX + '/assets/images/top_kv.png'}]
        self.download_image_objects(image_objs, folder)


# Seirei Gensouki
class SeireiGensoukiDownload(UnconfirmedDownload):
    title = "Seirei Gensouki"
    keywords = [title, "Spirit Chronicles"]
    folder_name = 'seirei-gensouki'

    PAGE_PREFIX = "https://seireigensouki.com/"

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
        news_url = self.PAGE_PREFIX + 'news-list/'
        try:
            soup = self.get_soup(news_url, decode=True)
            articles = soup.select('ul.news-list li.news-item')
            news_obj = self.get_last_news_log_object()
            results = []
            for article in articles:
                tag_date = article.find('p', class_='news-date')
                tag_title = article.find('p', class_='news-title')
                a_tag = article.find('a')
                if tag_date and tag_title and a_tag and a_tag.has_attr('href'):
                    article_id = a_tag['href']
                    date = self.format_news_date(tag_date.text.strip())
                    if len(date) == 0:
                        continue
                    title = tag_title.text.strip()
                    if news_obj and news_obj['id'] == article_id:
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
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/EnytdwVVQAESUct?format=jpg&name=large')
        #self.add_to_image_list('teaser', self.PAGE_PREFIX + 'wp/wp-content/uploads/2020/11/SG_teaser_logoc.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            chara_pics = soup.find_all('div', class_='chara-pic')
            for chara_pic in chara_pics:
                image = chara_pic.find('img')
                if image and image.has_attr('src'):
                    image_url = image['src']
                    image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)


# Shikkakumon no Saikyou Kenja
class ShikkakumonDownload(UnconfirmedDownload):
    title = 'Shikkakumon no Saikyou Kenja'
    keywords = [title]
    folder_name = 'shikkakumon'

    PAGE_PREFIX = 'https://shikkakumon.com/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        news_url = self.PAGE_PREFIX
        try:
            soup = self.get_soup(news_url, decode=True)
            articles = soup.select('#nwu_001_t tr')
            news_obj = self.get_last_news_log_object()
            results = []
            for article in articles:
                tag_date = article.find('td', class_='day')
                tag_title = article.find('div', class_='title')
                a_tag = article.find('a')
                if tag_date and tag_title:
                    article_id = ''
                    if a_tag and a_tag.has_attr('href'):
                        article_id = self.PAGE_PREFIX + a_tag['href']
                    date = self.format_news_date(tag_date.text.strip().replace('/', '.'))
                    if len(date) == 0:
                        continue
                    title = tag_title.text.strip()
                    if news_obj and news_obj['id'] == article_id and news_obj['title'] == title:
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
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.png')
        self.add_to_image_list('teaser_tw', 'https://pbs.twimg.com/media/EtDguMkU0AQjk4b?format=jpg&name=4096x4096')
        self.download_image_list(folder)


# Shokei Shoujo no Virgin Road
class ShokeiShoujoDownload(UnconfirmedDownload):
    title = 'Shokei Shoujo no Virgin Road'
    keywords = [title]
    folder_name = 'shokeishoujo'

    PAGE_PREFIX = 'http://virgin-road.com/'

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.png')
        self.add_to_image_list('teaser_tw', 'https://pbs.twimg.com/media/EtDn9lYU0AAKje-?format=jpg&name=4096x4096')
        self.download_image_list(folder)


# Shuumatsu no Harem
class ShuumatsuNoHaremDownload(UnconfirmedDownload):
    title = 'Shuumatsu no Harem'
    keywords = [title, "World's End Harem"]
    folder_name = 'shuumatsu-no-harem'

    PAGE_PREFIX = 'https://end-harem-anime.com/'

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
        news_url = self.PAGE_PREFIX + 'news/list00010000.html'
        stop = False
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            page_url = news_url
            for page in range(1, 100, 1):
                soup = self.get_soup(page_url, decode=True)
                trs = soup.select('#list_01 tr')
                for tr in trs:
                    tag_date = tr.find('td', class_='day')
                    tag_title = tr.find('div', class_='title')
                    a_tag = tr.find('a')
                    if tag_date and tag_title:
                        article_id = ''
                        if a_tag and a_tag.has_attr('href'):
                            article_id = self.PAGE_PREFIX + a_tag['href'].replace('../', '')
                        date = tag_date.text.strip().replace('/', '.')
                        title = tag_title.text.strip()
                        if news_obj and news_obj['id'] == article_id and news_obj['title'] == title:
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
        self.add_to_image_list('announce', 'https://pbs.twimg.com/media/EXzkif6VAAAxqJI?format=png&name=900x900')
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'core_sys/images/news/00000002/block/00000005/00000001.jpg')
        #self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/EoYL6tMVgAADou1?format=jpg&name=large')
        self.add_to_image_list('teaser_char', self.PAGE_PREFIX + 'core_sys/images/main/top/kv_char.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed = []
        num_processed = 0
        if os.path.exists(cache_filepath):
            with open(cache_filepath, 'r', encoding='utf-8') as f:
                inputs = f.read()
            processed = inputs.split(';')
            num_processed = len(processed)

        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/reito.html')
            chara_list = soup.find('div', id='ContentsListUnit01')
            if chara_list:
                a_tags = chara_list.find_all('a')
                for a_tag in a_tags:
                    if a_tag.has_attr('href') and '/' in a_tag['href']:
                        chara_name = a_tag['href'].split('/')[-1].split('.html')[0]
                        if chara_name in processed:
                            continue
                        if chara_name == 'reito':  # First character
                            chara_soup = soup
                        else:
                            chara_soup = self.get_soup(self.PAGE_PREFIX + a_tag['href'].replace('../', ''))
                        self.image_list = []
                        divs = ['standWrap', 'faceWrap']
                        for div in divs:
                            wraps = chara_soup.find_all('div', class_=div)
                            for wrap in wraps:
                                if wrap:
                                    image = wrap.find('img')
                                    if image and image.has_attr('src'):
                                        image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                                        self.add_to_image_list(image_name, image_url)
                        self.download_image_list(folder)
                        processed.append(chara_name)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)

        if len(processed) > num_processed:
            with open(cache_filepath, 'w+', encoding='utf-8') as f:
                for i in range(len(processed)):
                    if i > 0:
                        f.write(';')
                    f.write(processed[i])


# Slow Loop
class SlowLoopDownload(UnconfirmedDownload):
    title = 'Slow Loop'
    keywords = [title]
    folder_name = 'slow-loop'

    PAGE_PREFIX = 'https://slowlooptv.com/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('announce', 'https://pbs.twimg.com/media/Ep5-SoLUUAAHq36?format=jpg&name=4096x4096')
        self.add_to_image_list('announce_2', self.PAGE_PREFIX + 'images/top/v_001.jpg')
        self.download_image_list(folder)


# Tensai Ouji no Akaji Kokka Saisei Jutsu: Souda, Baikoku shiyou
class TensaiOujiDownload(UnconfirmedDownload):
    title = 'Tensai Ouji no Akaji Kokka Saisei Jutsu: Souda, Baikoku shiyou'
    keywords = [title, 'tensaiouji']
    folder_name = 'tensaiouji'

    PAGE_PREFIX = 'https://tensaiouji-anime.com/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/list00010000.html'
        stop = False
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            page_url = news_url
            for page in range(1, 100, 1):
                soup = self.get_soup(page_url, decode=True)
                trs = soup.select('#list_01 tr')
                for tr in trs:
                    tag_date = tr.find('td', class_='day')
                    tag_title = tr.find('div', class_='title')
                    a_tag = tr.find('a')
                    if tag_date and tag_title:
                        article_id = ''
                        if a_tag and a_tag.has_attr('href'):
                            article_id = self.PAGE_PREFIX + a_tag['href'].replace('../', '')
                        date = tag_date.text.strip().replace('/', '.')
                        title = tag_title.text.strip()
                        if news_obj and news_obj['id'] == article_id and news_obj['title'] == title:
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
        self.download_image_list(folder)


# Tsuki to Laika to Nosferatu
class TsukiLaikaNosferatuDownload(UnconfirmedDownload):
    title = 'Tsuki to Laika to Nosferatu'
    keywords = [title]
    folder_name = 'tsuki-laika-nosferatu'

    PAGE_PREFIX = 'https://tsuki-laika-nosferatu.com/'

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
                    page_url = news_url + 'page/' + str(page) + '/'
                soup = self.get_soup(page_url, decode=True)
                articles = soup.find_all('article', class_='news-box')
                for article in articles:
                    tag_date = article.find('p', 'news-box-date')
                    tag_title = article.find('h3', class_='news-box-ttl')
                    a_tag = article.find('a')
                    if tag_date and tag_title and a_tag and a_tag.has_attr('href'):
                        article_id = a_tag['href']
                        date = self.format_news_date(tag_date.text.strip())
                        if len(date) == 0:
                            continue
                        title = tag_title.text.strip()
                        if news_obj and news_obj['id'] == article_id:
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
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'Nr7R6svx/wp-content/themes/laika_tpl_v0/assets/img/top/visual.jpg')
        self.add_to_image_list('teaser_tw', 'https://pbs.twimg.com/media/EwpkNbsUUAAX00O?format=jpg&name=medium')
        self.download_image_list(folder)


# Vlad Love
class VladLoveDownload(UnconfirmedDownload):
    title = 'Vlad Love'
    keywords = [title, "Vladlove"]
    folder_name = 'vladlove'
    enabled = False

    PAGE_PREFIX = 'https://www.vladlove.com/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('visual01', self.PAGE_PREFIX + 'images/bg_cast.jpg')
        self.add_to_image_list('visual02', self.PAGE_PREFIX + 'images/bg_intro.jpg')
        self.add_to_image_list('visual03', self.PAGE_PREFIX + 'images/bg_character.jpg')
        self.add_to_image_list('visual04', self.PAGE_PREFIX + 'images/img_visual06.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character.html')
            detail_list = soup.find('ul', class_='characterDetailList')
            if detail_list:
                self.image_list = []
                images = detail_list.find_all('img')
                for image in images:
                    if image and image.has_attr('src'):
                        image_url = self.PAGE_PREFIX + image['src']
                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                        self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)


# Yama no Susume: Next Summit
class YamaNoSusume4Download(UnconfirmedDownload):
    title = 'Yama no Susume: Next Summit'
    keywords = [title, "Encouragement of Climb"]
    folder_name = 'yamanosusume4'

    PAGE_PREFIX = 'https://yamanosusume-ns.com/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        news_url = self.PAGE_PREFIX
        try:
            soup = self.get_soup(news_url, decode=True)
            articles = soup.select('#nwu_001_t tr')
            news_obj = self.get_last_news_log_object()
            results = []
            for article in articles:
                tag_date = article.find('td', class_='day')
                tag_title = article.find('div', class_='title')
                a_tag = article.find('a')
                if tag_date and tag_title:
                    article_id = ''
                    if a_tag and a_tag.has_attr('href'):
                        article_id = self.PAGE_PREFIX + a_tag['href']
                    date = self.format_news_date(tag_date.text.strip().replace('/', '.'))
                    if len(date) == 0:
                        continue
                    title = tag_title.text.strip()
                    if news_obj and news_obj['id'] == article_id and news_obj['title'] == title:
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
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.png')
        self.download_image_list(folder)
