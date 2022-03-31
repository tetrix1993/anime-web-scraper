import os
import requests
import anime.constants as constants
from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate3

# Anohana S2 https://10th.anohana.jp/ #あの花 #anohana @anohana_project
# Ayakashi Triangle https://ayakashitriangle-anime.com/ #あやかしトライアングル #あやトラ @ayakashi_anime
# Do It Yourself!! https://diy-anime.com/ #diyアニメ @diy_anime
# Futoku no Guild https://futoku-no-anime.com/ #futoku_anime #不徳のギルド @futoku_anime
# Goblin Slayer S2 http://www.goblinslayer.jp/ #ゴブスレ @GoblinSlayer_GA
# Inu ni Nattara Suki na Hito ni Hirowareta. https://inuhiro-anime.com/ #犬ひろ @inuninattara
# Isekai Yakkyoku https://isekai-yakkyoku.jp/ #異世界薬局 @isekai_yakkyoku
# Itai no wa https://bofuri.jp/story/ #防振り #bofuri @bofuri_anime
# Kunoichi Tsubaki no Mune no Uchi https://kunoichi-tsubaki.com/ #くノ一ツバキ @tsubaki_anime
# Mamahaha no Tsurego ga Motokano datta https://tsurekano-anime.com/ #連れカノ #tsurekano @tsurekano
# Maou Gakuin no Futekigousha 2nd Season https://maohgakuin.com/ #魔王学院 @maohgakuin
# Mato Seihei no Slave https://mabotai.jp/ #魔都精兵のスレイブ #まとスレ @mabotai_kohobu
# Otonari no Tenshi-sama ni Itsunomanika Dame Ningen ni Sareteita Ken https://otonarino-tenshisama.jp/ #お隣の天使様 @tenshisama_PR
# Renai Flops https://loveflops.com/ #恋愛フロップス @loveflops_pr
# Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita 2nd Season https://slime300-anime.com/ #スライム倒して300年 @slime300_PR
# Spy Kyoushitsu https://spyroom-anime.com/ #スパイ教室 #spyroom #SpyClassroom @spyroom_anime
# Tonikaku Kawaii S2 http://tonikawa.com/ #トニカクカワイイ #tonikawa @tonikawa_anime
# Vlad Love https://www.vladlove.com/index.html #ぶらどらぶ #vladlove @VLADLOVE_ANIME
# Yama no Susume: Next Summit https://yamanosusume-ns.com/ #ヤマノススメ @yamanosusume


# Unconfirmed Season Anime
class UnconfirmedDownload(MainDownload):
    season = "9999-9"
    season_name = "Unconfirmed"
    folder_name = 'unconfirmed'

    def __init__(self):
        super().__init__()


# Ano Hi Mita Hana no Namae wo Bokutachi wa Mada Shiranai. 10th Anniversary Project
class Anohana2Download(UnconfirmedDownload):
    title = 'Ano Hi Mita Hana no Namae wo Bokutachi wa Mada Shiranai. 10th Anniversary Project'
    keywords = [title, 'Anohana', 'The Flower We Saw That Day']
    website = 'https://10th.anohana.jp/'
    twitter = 'anohana_project'
    hashtags = ['anohana', 'あの花']
    folder_name = 'anohana2'
    enabled = False

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
        news_url = self.PAGE_PREFIX + 'news/'
        stop = False
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            page_url = news_url
            for page in range(1, 100, 1):
                soup = self.get_soup(page_url, decode=True)
                lis = soup.select('div.news_list ul li.news_list__item')
                for li in lis:
                    tag_date = li.find('p', class_='news_date')
                    tag_title = li.find('p', class_='news_title')
                    a_tag = li.find('a')
                    if tag_date and tag_title:
                        article_id = ''
                        if a_tag and a_tag.has_attr('href'):
                            article_id = news_url + a_tag['href'].replace('./', '').split('&p=')[0]
                        date = self.format_news_date(tag_date.text.strip())
                        if len(date) == 0:
                            continue
                        title = tag_title.text.strip()
                        if date.startswith('2020') or (news_obj and
                                                       ((news_obj['id'] == article_id and news_obj['title'] == title)
                                                        or date < news_obj['date'])):
                            stop = True
                            break
                        results.append(self.create_news_log_object(date, title, article_id))
                if stop:
                    break
                btn_next = soup.find('p', class_='btn_next')
                if btn_next is None:
                    break
                btn_next_a_tag = btn_next.find('a')
                if btn_next_a_tag is None or not btn_next_a_tag.has_attr('href'):
                    break
                page_url = news_url + btn_next_a_tag['href'].replace('./', '')
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
        self.image_list = []
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/ExRRykWU4AEZ6Cy?format=jpg&name=large')
        self.add_to_image_list('teaser_tw', self.PAGE_PREFIX + 'assets/images/pc/teaser/img_kv.png')
        self.download_image_list(folder)


# Ayakashi Triangle
class AyakashiTriangleDownload(UnconfirmedDownload):
    title = 'Ayakashi Triangle'
    keywords = [title]
    website = 'https://ayakashitriangle-anime.com/'
    twitter = 'ayakashi_anime'
    hashtags = ['あやトラ', 'あやかしトライアングル']
    folder_name = 'ayakashi-triangle'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        # self.add_to_image_list('announce_tw', 'https://pbs.twimg.com/media/FG33dXJagAY1HcQ?format=jpg&name=medium')
        self.add_to_image_list('announce_aniverse', 'https://aniverse-mag.com/wp-content/uploads/2021/12/img_kokuchi.jpg')
        self.add_to_image_list('announce', self.PAGE_PREFIX + 'assets/img/img_kv.png')
        self.download_image_list(folder)


# Do It Yourself!!
class DoItYourselfDownload(UnconfirmedDownload):
    title = 'Do It Yourself!!'
    keywords = [title, 'DIY']
    website = 'https://diy-anime.com/'
    twitter = 'diy_anime'
    hashtags = 'diyアニメ'
    folder_name = 'diy'
    enabled = False

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index', diff=2)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        try:
            page = 0
            stop = False
            news_obj = self.get_last_news_log_object()
            results = []
            curr_news_url = news_url
            while len(curr_news_url) > 0:
                page += 1
                soup = self.get_soup(curr_news_url, decode=True)
                articles = soup.select('li.news_List_Item')
                for article in articles:
                    tag_date = article.find('time', class_='roboto')
                    tag_title = article.find('div', class_='ttl')
                    a_tag = article.find('a')
                    if tag_date and a_tag and a_tag.has_attr('href'):
                        article_id = news_url + a_tag['href']
                        date = self.format_news_date(tag_date.text.strip().replace('/', '.'))
                        if len(date) == 0:
                            continue
                        title = ' '.join(tag_title.text.strip().split())
                        if news_obj and ((news_obj['id'] == article_id and news_obj['title'] == title)
                                         or date < news_obj['date']):
                            stop = True
                            break
                        results.append(self.create_news_log_object(date, title, article_id))

                if stop:
                    break
                next_page = soup.select('div.paging a.next')
                if len(next_page) > 0:
                    try:
                        next_page_num = int(next_page[0]['href'].split('=')[1])
                        if next_page_num == page:
                            break
                        else:
                            curr_news_url = next_page[0]['href']
                    except Exception:
                        break
                else:
                    break
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
        self.image_list = []
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/ExRRykWU4AEZ6Cy?format=jpg&name=large')
        self.add_to_image_list('teaser_tw', self.PAGE_PREFIX + 'assets/images/pc/teaser/img_kv.png')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'assets/images/pc/index/img_kv-%s.png'
        self.download_by_template(folder, template, 1)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/images/pc/teaser/img_chara-%s.png'
        self.download_by_template(folder, template, 1, 0)


# Futoku no Guild
class FutokunoGuildDownload(UnconfirmedDownload, NewsTemplate):
    title = 'Futoku no Guild'
    keywords = [title]
    website = 'https://futoku-no-anime.com/'
    twitter = 'futoku_anime'
    hashtags = ['futoku_anime', '不徳のギルド']
    folder_name = 'futoku-no-guild'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='#nwu_001_t tr',
                                    date_select='.day', title_select='.title', id_select='#nothing',
                                    date_separator='/', news_prefix='')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FNfyKsbVcAMufgT?format=jpg&name=medium')
        self.add_to_image_list('tz_kv', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.png')
        self.download_image_list(folder)


# Goblin Slayer 2nd Season
class GoblinSlayer2Download(UnconfirmedDownload):
    title = "Goblin Slayer 2nd Season"
    keywords = [title]
    website = 'http://www.goblinslayer.jp/'
    twitter = 'GoblinSlayer_GA'
    hashtags = 'ゴブスレ'
    folder_name = 'goblin-slayer2'

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
                    if date.startswith('2020') or (news_obj and
                                                   (news_obj['id'] == article_id or date < news_obj['date'])):
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
            self.print_exception(e, 'News')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/EtDYBThUYAEBIWI?format=jpg&name=4096x4096')
        self.download_image_list(folder)


# Inu ni Nattara Suki na Hito ni Hirowareta.
class InuhiroDownload(UnconfirmedDownload, NewsTemplate):
    title = "Inu ni Nattara Suki na Hito ni Hirowareta."
    keywords = [title, 'Inuhiro']
    website = 'https://inuhiro-anime.com/'
    twitter = 'inuninattara'
    hashtags = '犬ひろ'
    folder_name = 'inuhiro'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='#news article',
                                    date_select='time', title_select='h3', id_select=None,
                                    id_has_id=True, news_prefix='')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FNybC1EaAAEoRmq?format=jpg&name=large')
        self.add_to_image_list('tz_mainimg_pc', self.PAGE_PREFIX + 'teaser/images/mainimg_pc.png')
        self.download_image_list(folder)


# Isekai Yakkyoku
class IsekaiYakkyokuDownload(UnconfirmedDownload, NewsTemplate2):
    title = 'Isekai Yakkyoku'
    keywords = [title]
    website = 'https://isekai-yakkyoku.jp/'
    twitter = 'isekai_yakkyoku'
    hashtags = '異世界薬局'
    folder_name = 'isekai-yakkyoku'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/E6Rh8S_VcAQWTLG?format=jpg&name=4096x4096')
        self.add_to_image_list('tz_kv', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.jpg')
        self.download_image_list(folder)

        kv_template = self.PAGE_PREFIX + 'core_sys/images/main/tz/kv%s'
        kv_template1 = kv_template + '.jpg'
        kv_template2 = kv_template + '.png'
        self.download_by_template(folder, [kv_template1, kv_template2], 1, 2, prefix='tz_')

    def download_character(self):
        folder = self.create_character_directory()
        tz_prefix = self.PAGE_PREFIX +'core_sys/images/main/tz/chara/'
        templates = [tz_prefix + '%s_stand.png', tz_prefix + '%s_face.png']
        self.download_by_template(folder, templates, 2, 1, prefix='tz_')


# Itai no wa Iya nano de Bougyoryoku ni Kyokufuri Shitai to Omoimasu. 2nd Season
class Bofuri2Download(UnconfirmedDownload):
    title = "Itai no wa Iya nano de Bougyoryoku ni Kyokufuri Shitai to Omoimasu. 2nd Season"
    keywords = [title, 'bofuri', "BOFURI: I Don't Want to Get Hurt, so I'll Max Out My Defense.", '2nd']
    website = "https://bofuri.jp/"
    twitter = 'bofuri_anime'
    hashtags = ['bofuri', '#防振り']
    folder_name = 'bofuri2'

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
                    if date.startswith('2021.01.04') or (news_obj and
                                                         (news_obj['id'] == article_id or date < news_obj['date'])):
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
            self.print_exception(e, 'News')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('animation_works', 'https://pbs.twimg.com/media/ErSRQUmVoAAkgt7?format=jpg&name=large')
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/ErSKnRwW8AAjOyU?format=jpg&name=4096x4096')
        self.download_image_list(folder)


# Mamahaha no Tsurego ga Motokano datta
class TsurekanoDownload(UnconfirmedDownload):
    title = 'Mamahaha no Tsurego ga Motokano datta'
    keywords = [title, "My Stepmom's Daughter Is My Ex", 'tsurekano']
    website = 'https://tsurekano-anime.com/'
    twitter = 'tsurekano'
    hashtags = ['連れカノ', 'tsurekano']
    folder_name = 'tsurekano'

    PAGE_PREFIX = website

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
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FKA8xQ1aAAEmNl3?format=jpg&name=4096x4096')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'img/top/kv_%s.png'
        self.download_by_template(folder, template, 1, 1, prefix='top_')

        self.download_youtube_thumbnails(self.PAGE_PREFIX, folder)


# Maou Gakuin no Futekigousha: Shijou Saikyou no Maou no Shiso, Tensei shite Shison-tachi no Gakkou e
class Maohgakuin2Download(UnconfirmedDownload, NewsTemplate):
    title = "Maou Gakuin no Futekigousha: Shijou Saikyou no Maou no Shiso, Tensei shite Shison-tachi no Gakkou e 2nd Season"
    keywords = [title, 'Maohgakuin', 'The Misfit of Demon King Academy']
    website = "https://maohgakuin.com/"
    twitter = 'maohgakuin'
    hashtags = '魔王学院'
    folder_name = 'maohgakuin2'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news_list li',
                                    date_select='.news_date', title_select='.news_title', id_select='a',
                                    a_tag_prefix=news_url, a_tag_start_text_to_remove='./')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'assets/img/img_main.jpg')
        # self.add_to_image_list('teaser_tw', 'https://pbs.twimg.com/media/EvylQFOVkAID_0B?format=jpg&name=medium')
        self.download_image_list(folder)


# Mato Seihei no Slave
class MatoSlaveDownload(UnconfirmedDownload, NewsTemplate):
    title = 'Mato Seihei no Slave'
    keywords = [title]
    website = 'https://mabotai.jp/'
    twitter = 'mabotai_kohobu'
    hashtags = ['魔都精兵のスレイブ', 'まとスレ']
    folder_name = 'matoslave'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        # self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    # def download_news(self):
    #    self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        # self.image_list = []
        # self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FEiqZdFaUAQyOy4?format=jpg&name=900x900')
        # self.download_image_list(folder)

        teaser_template = self.PAGE_PREFIX + 'img/teaser/visual_%s.jpg'
        for i in range(1, 11, 1):
            image_name = f'tz{i}'
            if self.is_image_exists(image_name, folder):
                continue
            image_url = teaser_template % str(i).zfill(2)
            result = self.download_image(image_url, f'{folder}/{image_name}')
            if result == -1:
                break


# Otonari no Tenshi-sama ni Itsunomanika Dame Ningen ni Sareteita Ken
class OtonarinoTenshisamaDownload(UnconfirmedDownload, NewsTemplate):
    title = 'Otonari no Tenshi-sama ni Itsunomanika Dame Ningen ni Sareteita Ken'
    keywords = [title, 'The Angel Next Door Spoils Me Rotten']
    website = 'https://otonarino-tenshisama.jp/'
    twitter = 'tenshisama_PR'
    hashtags = 'お隣の天使様'
    folder_name = 'otonarino-tenshisama'

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
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.allNews__item',
                                    title_select='.allNews__title', date_select='.allNews__date',
                                    id_select='a', next_page_select='a.next.page-numbers')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FIQhzRlagAAxK-X?format=jpg&name=large')
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'wordpress/wp-content/themes/otonari/images/mainvisual.jpg')
        self.add_to_image_list('tz2_tw', 'https://pbs.twimg.com/media/FOtPcAMVkAcoYzY?format=jpg&name=4096x4096')
        self.add_to_image_list('aprilfool_0331_A', self.PAGE_PREFIX + 'wordpress/wp-content/uploads/2022/03/aprilfool_0331_A.jpg')
        self.add_to_image_list('aprilfool_all', self.PAGE_PREFIX + 'wordpress/wp-content/uploads/2022/03/aprilfool_all.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wordpress/wp-content/themes/otonari/images/character-%s.png'
        self.download_by_template(folder, template, 1, prefix='tz_')

    def download_media(self):
        folder = self.create_media_directory()
        # self.add_to_image_list('valentine_tw', 'https://pbs.twimg.com/media/FLfDFR8aQAIWt1u?format=jpg&name=large')
        self.add_to_image_list('valentine_chara', 'https://aniverse-mag.com/wp-content/uploads/2022/02/8e5cda5d29024d4bf78d1e9452225fb6-e1644755501739.png')
        self.add_to_image_list('valentine_pos', self.PAGE_PREFIX + 'wordpress/wp-content/uploads/2022/02/valentine_pos.jpg')
        self.add_to_image_list('valentine', self.PAGE_PREFIX + 'wordpress/wp-content/uploads/2022/02/valentine_sp-kabegami.jpg')
        self.download_image_list(folder)


# Renai Flops
class RenaiFlopsDownload(UnconfirmedDownload, NewsTemplate):
    title = 'Renai Flops'
    keywords = [title, 'Love Flops']
    website = 'https://loveflops.com/'
    twitter = 'loveflops_pr'
    hashtags = '恋愛フロップス'
    folder_name = 'renai-flops'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news_list article',
                                    date_select='.news_list_day', title_select='.ne', id_select='a',
                                    date_separator='/', news_prefix='news.html', a_tag_prefix=self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FOrTLwXagAE6Q-C?format=jpg&name=large')
        self.add_to_image_list('tz_aniverse', 'https://aniverse-mag.com/wp-content/uploads/2022/03/6a1f645dc99cda5844a8d86a77f24193-e1648196815379.jpg')
        self.download_image_list(folder)

        self.download_by_template(folder, self.PAGE_PREFIX + 'images/top/visual/v%s.jpg', 3, prefix='top_visual_')
        self.download_by_template(folder, self.PAGE_PREFIX + 'images/news/p_%s.jpg', 3, prefix='news_')

    def download_character(self):
        folder = self.create_character_directory()
        template_prefix = self.PAGE_PREFIX + 'images/chara/'
        templates = [template_prefix + 'b_%s.png', template_prefix + 'a_%s.png']
        self.download_by_template(folder, templates, 3, 1)


# Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita 2nd Season
class Slime3002Download(UnconfirmedDownload, NewsTemplate):
    title = "Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita 2nd Season"
    keywords = [title, "I've Been Killing Slimes for 300 Years and Maxed Out My Level", "Slime 300", "slime300", '2nd']
    website = 'https://slime300-anime.com'
    twitter = 'slime300_PR'
    hashtags = 'スライム倒して300年'
    folder_name = 'slime300-2'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        pass

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
                    if date < '2022.01.04':
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
        self.image_list = []
        self.add_to_image_list('announce', self.PAGE_PREFIX + '/static/944a17585cc6d3dccaf125c0201aab71/99383/promo.png')
        self.download_image_list(folder)


# Spy Kyoushitsu
class SpyroomDownload(UnconfirmedDownload, NewsTemplate2):
    title = "Spy Kyoushitsu"
    keywords = [title, "Spy Classroom", "Spyroom"]
    website = 'https://spyroom-anime.com/'
    twitter = 'spyroom_anime'
    hashtags = ['スパイ教室', 'spyroom', 'SpyClassroom']
    folder_name = 'spyroom'

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
        self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_kv_chara', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv_chara.png')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FNuvFFSaAAkbDy3?format=jpg&name=4096x4096')
        self.download_image_list(folder)


# Tonikaku Kawaii S2
class Tonikawa2Download(UnconfirmedDownload, NewsTemplate):
    title = "Tonikaku Kawaii 2nd Season"
    keywords = [title, "Tonikawa", "Cawaii", "Fly Me to the Moon", "Over the Moon for You", "2nd"]
    website = 'http://tonikawa.com/'
    twitter = 'tonikawa_anime'
    hashtags = ['トニカクカワイイ', 'tonikawa']
    folder_name = 'tonikawa2'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='div.archive li',
                                    date_select='.date', title_select='.title p', id_select='a',
                                    a_tag_prefix=self.PAGE_PREFIX, a_tag_start_text_to_remove='/',
                                    stop_date='2021.10.08')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FDf9oGkaIAE7jnd?format=jpg&name=large')
        self.download_image_list(folder)


# Vlad Love
class VladLoveDownload(UnconfirmedDownload):
    title = 'Vlad Love'
    keywords = [title, "Vladlove"]
    website = 'https://www.vladlove.com/'
    twitter = 'VLADLOVE_ANIME'
    hashtags = ['vladlove', 'ぶらどらぶ']
    folder_name = 'vladlove'
    enabled = False

    PAGE_PREFIX = website

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
            self.print_exception(e, 'Character')


# Yama no Susume: Next Summit
class YamaNoSusume4Download(UnconfirmedDownload):
    title = 'Yama no Susume: Next Summit'
    keywords = [title, "Encouragement of Climb"]
    website = 'https://yamanosusume-ns.com/'
    twitter = 'yamanosusume'
    hashtags = 'ヤマノススメ'
    folder_name = 'yamanosusume4'

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
                    if news_obj and ((news_obj['id'] == article_id and news_obj['title'] == title)
                                     or date < news_obj['date']):
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
            self.print_exception(e, 'News')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.png')
        self.download_image_list(folder)
