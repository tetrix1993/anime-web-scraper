import os
import requests
import anime.constants as constants
from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate3

# Akiba Meido Sensou https://akibamaidwar.com/ #アキバ冥途戦争 @akbmaidwar
# Anohana S2 https://10th.anohana.jp/ #あの花 #anohana @anohana_project
# Ayakashi Triangle https://ayakashitriangle-anime.com/ #あやかしトライアングル #あやトラ @ayakashi_anime
# Do It Yourself!! https://diy-anime.com/ #diyアニメ @diy_anime
# Eiyuu Kyoushitsu https://eiyukyoushitsu-anime.com/ #英雄教室 #eiyu_anime @eiyu_anime
# Fuufu Ijou, Koibito Miman. https://fuukoi-anime.com/ #ふうこいアニメ @fuukoi_anime
# Goblin Slayer S2 http://www.goblinslayer.jp/ #ゴブスレ @GoblinSlayer_GA
# Inu ni Nattara Suki na Hito ni Hirowareta. https://inuhiro-anime.com/ #犬ひろ @inuninattara
# Itai no wa https://bofuri.jp/story/ #防振り #bofuri @bofuri_anime
# Kubo-san wa Mob wo Yurusanai https://kubosan-anime.jp/ #久保さん @kubosan_anime
# Maou Gakuin no Futekigousha 2nd Season https://maohgakuin.com/ #魔王学院 @maohgakuin
# Masamune-kun no Revenge R https://masamune-tv.com/ #MASA_A @masamune_tv
# Mato Seihei no Slave https://mabotai.jp/ #魔都精兵のスレイブ #まとスレ @mabotai_kohobu
# Oshi no Ko https://ichigoproduction.com/ #推しの子 @anime_oshinoko
# Otonari ni Ginga https://otonari-anime.com/ #おとなりに銀河 @otonariniginga
# Otonari no Tenshi-sama ni Itsunomanika Dame Ningen ni Sareteita Ken https://otonarino-tenshisama.jp/ #お隣の天使様 @tenshisama_PR
# Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita 2nd Season https://slime300-anime.com/ #スライム倒して300年 @slime300_PR
# Spy Kyoushitsu https://spyroom-anime.com/ #スパイ教室 #spyroom #SpyClassroom @spyroom_anime
# Tonikaku Kawaii S2 http://tonikawa.com/ #トニカクカワイイ #tonikawa @tonikawa_anime
# Vlad Love https://www.vladlove.com/index.html #ぶらどらぶ #vladlove @VLADLOVE_ANIME
# Watashi no Yuri wa Oshigoto desu! https://watayuri-anime.com/ #わたゆり #私の百合はお仕事です @watayuri_anime
# Yuusha ga Shinda! https://heroisdead.com/ #勇者が死んだ @yuusyagasinda


# Unconfirmed Season Anime
class UnconfirmedDownload(MainDownload):
    season = "9999-9"
    season_name = "Unconfirmed"
    folder_name = 'unconfirmed'

    def __init__(self):
        super().__init__()


# Akiba Meido Sensou
class AkibaMaidWarDownload(UnconfirmedDownload, NewsTemplate):
    title = 'Akiba Meido Sensou'
    keywords = [title, 'Akiba Maid War']
    website = 'https://akibamaidwar.com/'
    twitter = 'akbmaidwar'
    hashtags = 'アキバ冥途戦争'
    folder_name = 'akibamaidwar'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, news_prefix='', article_select='#news-area li',
                                    title_select='dt span', date_select='dd.new', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FWAaCg-UEAAJ5sw?format=jpg&name=4096x4096')
        self.add_to_image_list('tz_kv', self.PAGE_PREFIX + 'assets/images/pc/kv.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        self.add_to_image_list('tz_chara_image', self.PAGE_PREFIX + 'assets/images/pc/chara_image.png')
        self.download_image_list(folder)


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


# Eiyuu Kyoushitsu
class EiyuKyoushitsuDownload(UnconfirmedDownload):
    title = 'Eiyuu Kyoushitsu'
    keywords = [title, 'Classroom for Heroes']
    website = 'https://eiyukyoushitsu-anime.com/'
    twitter = 'eiyu_anime'
    hashtags = ['英雄教室', 'eiyu_anime']
    folder_name = 'eiyukyoushitsu'

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
        self.add_to_image_list('eiyukyoushitsu_KV', self.PAGE_PREFIX + 'images/eiyukyoushitsu_KV.jpg')
        self.download_image_list(folder)


# Fuufu Ijou, Koibito Miman.
class FuukoiDownload(UnconfirmedDownload, NewsTemplate2):
    title = 'Fuufu Ijou, Koibito Miman.'
    keywords = [title, 'More Than a Married Couple, But Not Lovers', 'fuukoi']
    website = 'https://fuukoi-anime.com/'
    twitter = 'fuukoi_anime'
    hashtags = 'ふうこいアニメ'
    folder_name = 'fuukoi'

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
        image_prefix = self.PAGE_PREFIX + 'core_sys/images/'
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FRbNkGEakAEHfD5?format=jpg&name=4096x4096')
        self.add_to_image_list('tz_kv_webp', image_prefix + 'main/tz/kv.webp')
        self.add_to_image_list('tz_kv', image_prefix + 'main/tz/kv.jpg')
        self.add_to_image_list('tz_news', image_prefix + 'news/00000003/block/00000006/00000001.jpg')
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
        self.add_to_image_list('aprilfools_tw', 'https://pbs.twimg.com/media/FPOV5F5agAE3czc?format=jpg&name=4096x4096')
        self.add_to_image_list('aprilfools_news', self.PAGE_PREFIX + 'assets/news/65a.jpg')
        self.add_to_image_list('aprilfools_top', self.PAGE_PREFIX + 'images/top-visual/2022apr/all.jpg')
        self.download_image_list(folder)


# Kubo-san wa Mob wo Yurusanai
class KubosanDownload(UnconfirmedDownload, NewsTemplate2):
    title = 'Kubo-san wa Mob wo Yurusanai'
    keywords = [title, "Kubo Won't Let Me Be Invisible"]
    website = 'https://kubosan-anime.jp/'
    twitter = 'kubosan_anime'
    hashtags = '久保さん'
    folder_name = 'kubosan'

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
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'core_sys/images/news/00000002/block/00000008/00000002.jpg')
        self.add_to_image_list('img_kv1', 'https://pbs.twimg.com/media/FXsiHJWaQAU3UsM?format=jpg&name=large')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        self.add_to_image_list('tz_chara_kubo', self.PAGE_PREFIX + 'core_sys/images/main/tz/chara_kubo.png')
        self.add_to_image_list('tz_chara_shiraishi', self.PAGE_PREFIX + 'core_sys/images/main/tz/chara_shiraishi.png')
        self.download_image_list(folder)


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


# Masamune-kun no Revenge R
class Masamunekun2Download(UnconfirmedDownload, NewsTemplate):
    title = 'Masamune-kun no Revenge'
    keywords = [title, "Masamune's Revenge"]
    website = 'https://masamune-tv.com/'
    twitter = 'masamune_tv'
    hashtags = ['MASA_A']
    folder_name = 'masamune2'

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
        # Paging logic may need update
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news--lineup article',
                                    date_select='.txt--date', title_select='.txt--ttl', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_kv', self.PAGE_PREFIX + '_assets/images/fv/fv@2x.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.chardata img[src]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'][1:]
                image_name = 'tz_' + self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


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


# Oshi no Ko
class OshinokoDownload(UnconfirmedDownload, NewsTemplate2):
    title = 'Oshi no Ko'
    keywords = [title, 'oshinoko']
    website = 'https://ichigoproduction.com/'
    twitter = 'anime_oshinoko'
    hashtags = '推しの子'
    folder_name = 'oshinoko'

    PAGE_PREFIX = website

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
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FU0bJsjaAAAE7Bf?format=jpg&name=large')
        self.add_to_image_list('tz_kv', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.jpg')
        self.download_image_list(folder)


# Otonari ni Ginga
class OtonariniGingaDownload(UnconfirmedDownload, NewsTemplate):
    title = 'Otonari ni Ginga'
    keywords = [title, 'A Galaxy Next Door']
    website = 'https://otonari-anime.com/'
    twitter = 'otonariniginga'
    hashtags = 'おとなりに銀河'
    folder_name = 'otonariniginga'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, news_prefix='', article_select='#news article',
                                    title_select='h3', date_select='time', id_select=None, id_has_id=True,
                                    date_func=lambda x: x[0:4] + '.' + x[5:7] + '.' + x[8:10])

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FRV6mlUVIAAa9xK?format=jpg&name=medium')
        self.add_to_image_list('tz_mainimg', self.PAGE_PREFIX + 'teaser/images/mainimg.png')
        self.download_image_list(folder)


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
        self.add_to_image_list('tz3', self.PAGE_PREFIX + 'wordpress/wp-content/themes/otonari/images/mainvisual-v2.jpg')
        self.add_to_image_list('tz3_pc', self.PAGE_PREFIX + 'wordpress/wp-content/themes/otonari/images/mainvisual-v2_pc.jpg')
        self.add_to_image_list('tz3_news', self.PAGE_PREFIX + 'wordpress/wp-content/uploads/2022/05/tenshisama_teser3_title.jpg')
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
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_kv_chara', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv_chara.png')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FNuvFFSaAAkbDy3?format=jpg&name=4096x4096')
        self.add_to_image_list('home_kv', self.PAGE_PREFIX + 'core_sys/images/main/home/kv.png')
        self.add_to_image_list('tz_kv', self.PAGE_PREFIX + 'core_sys/images/news/00000015/block/00000031/00000005.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'chara/lily.html')
            a_tags = soup.select('#ContentsListUnit02 a[href]')
            for a_tag in a_tags:
                chara_url = self.PAGE_PREFIX + a_tag['href'].replace('../', '')
                chara_name = chara_url.split('/')[-1].replace('.html', '')
                if chara_name in processed:
                    continue
                if chara_name == 'lily':
                    chara_soup = soup
                else:
                    chara_soup = self.get_soup(chara_url)
                if chara_soup is not None:
                    images = chara_soup.select('.chara__img img[src]')
                    for image in images:
                        image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                        image_name = self.extract_image_name_from_url(image_url)
                        self.add_to_image_list(image_name, image_url)
                    if len(self.image_list) > 0:
                        processed.append(chara_name)
                    self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)


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


# Watashi no Yuri wa Oshigoto desu!
class WatayuriDownload(UnconfirmedDownload):
    title = 'Watashi no Yuri wa Oshigoto desu!'
    keywords = [title, 'watayuri', 'Yuri is My Job!']
    website = 'https://watayuri-anime.com/'
    twitter = 'watayuri_anime'
    hashtags = ['わたゆり', '私の百合はお仕事です']
    folder_name = 'watayuri'

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
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FStxiD1VIAEX1nk?format=jpg&name=4096x4096')
        self.add_to_image_list('tz_mv1', self.PAGE_PREFIX + 'assets/img/top/mv1.jpg')
        self.add_to_image_list('tz_mv2', self.PAGE_PREFIX + 'assets/img/top/mv2.jpg')
        self.download_image_list(folder)


# Yuusha ga Shinda!
class YuushagaShindaDownload(UnconfirmedDownload):
    title = 'Yuusha ga Shinda!: Murabito no Ore ga Hotta Otoshiana ni Yuusha ga Ochita Kekka.'
    keywords = [title, 'The Legendary Hero Is Dead!']
    website = 'https://heroisdead.com/'
    twitter = 'yuusyagasinda'
    hashtags = '勇者が死んだ'
    folder_name = 'yuushagashinda'

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
        self.add_to_image_list('tz_aniverse', 'https://aniverse-mag.com/wp-content/uploads/2022/04/4576fa0e88a0464f6a9b6e8844e05dbd-e1651058246996.jpg')
        self.add_to_image_list('tz_visual_01_chara', self.PAGE_PREFIX + 'img/teaser/visual_01_chara.png')
        self.download_image_list(folder)
