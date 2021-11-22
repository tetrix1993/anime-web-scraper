import os
import anime.constants as constants
from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate3
from datetime import datetime
from scan import AniverseMagazineScanner, MocaNewsScanner, WebNewtypeScanner


# Akebi-chan no Sailor-fuku https://akebi-chan.jp/ #明日ちゃんのセーラー服 #明日ちゃん @AKEBI_chan
# Arifureta Shokugyou de Sekai Saikyou 2nd Season https://arifureta.com/ #ありふれた #ARIFURETA @ARIFURETA_info
# Fantasy Bishoujo Juniku Ojisan to https://fabiniku.com/ #ファ美肉おじさん @fabiniku
# Hakozume: Kouban Joshi no Gyakushuu https://hakozume-anime.com/ #ハコヅメ @hakozume_anime
# Kaijin Kaihatsubu no Kuroitsu-san https://kuroitsusan-anime.com/ #黒井津さん @kuroitsusan
# Karakai Jouzu no Takagi-san 3 https://takagi3.me/ #高木さんめ @takagi3_anime
# Kenja no Deshi wo Nanoru Kenja https://kendeshi-anime.com/ #賢でし @kendeshi_anime
# Leadale no Daichi nite https://leadale.net/ #leadale #リアデイル @leadale_anime
# Mahouka Koukou no Rettousei: Tsuioku-hen https://mahouka.jp/ #mahouka @mahouka_anime
# Princess Connect! Re:Dive S2 https://anime.priconne-redive.jp/ #アニメプリコネ #プリコネR #プリコネ #アニメプリコネR @priconne_anime
# Shikkakumon no Saikyou Kenja https://shikkakumon.com/ #失格紋 @shikkakumon_PR
# Slow Loop https://slowlooptv.com/ #slowloop @slowloop_tv
# Sono Bisque Doll wa Koi wo Suru https://bisquedoll-anime.com/ #着せ恋 @kisekoi_anime
# Tensai Ouji no Akaji Kokka Saisei Jutsu: Souda, Baikoku shiyou https://tensaiouji-anime.com/ #天才王子 #天才王子の赤字国家再生術 @tensaiouji_PR


# Winter 2022 Anime
class Winter2022AnimeDownload(MainDownload):
    season = "2022-1"
    season_name = "Winter 2022"
    folder_name = '2022-1'

    def __init__(self):
        super().__init__()


# Akebi-chan no Sailor-fuku
class AkebichanDownload(Winter2022AnimeDownload, NewsTemplate):
    title = 'Akebi-chan no Sailor-fuku'
    keywords = [title, "Akebi's Sailor Uniform"]
    website = 'https://akebi-chan.jp/'
    twitter = 'AKEBI_chan'
    hashtags = ['明日ちゃんのセーラー服', '明日ちゃん']
    folder_name = 'akebichan'

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
        prefix = self.PAGE_PREFIX + '?scroll='
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.p-news-in__item',
                                    date_select='p.date', title_select='h3.title', id_select=None,
                                    id_has_id=True, a_tag_prefix=prefix)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.add_to_image_list('tz_img_kv', f'{self.PAGE_PREFIX}assets_teaser/img/img_kv.jpg')
        self.add_to_image_list('tz_main', f'{self.PAGE_PREFIX}assets_teaser/img/main.jpg')
        self.add_to_image_list('tz_main_tw', 'https://pbs.twimg.com/media/FAmRYw-UcAkGiCO?format=jpg&name=large')
        self.download_image_list(folder)


# Arifureta Shokugyou de Sekai Saikyou 2nd Season
class Arifureta2Download(Winter2022AnimeDownload):
    title = "Arifureta Shokugyou de Sekai Saikyou 2nd Season"
    keywords = [title, "Arifureta: From Commonplace to World's Strongest 2nd Season"]
    website = 'https://arifureta.com/'
    twitter = 'ARIFURETA_info'
    hashtags = ['ARIFURETA', 'ありふれた']
    folder_name = 'arifureta2'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, diff=67)

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
                articles = soup.select('ul.news_list li')
                for article in articles:
                    tag_date = article.find('h5', class_='date')
                    tag_title = article.find('h1')
                    a_tag = article.find('a')
                    if tag_date and tag_title and a_tag and a_tag.has_attr('href'):
                        article_id = a_tag['href']
                        date = self.format_news_date(tag_date.text.strip())
                        if len(date) == 0:
                            continue
                        title = tag_title.text.strip()
                        if date.startswith('2021.03') or \
                                news_obj and (news_obj['id'] == article_id or date < news_obj['date']):
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
        self.add_to_image_list('mainvisual08', self.PAGE_PREFIX + 'wp-content/themes/arifureta-v3.2/library/img/main_visual/mainvisual08.png')
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'wp-content/uploads/2021/04/02.jpg')
        self.add_to_image_list('kv1_art', self.PAGE_PREFIX + 'wp-content/uploads/2021/04/03.jpg')
        self.download_image_list(folder)


# Fantasy Bishoujo Juniku Ojisan to
class FabinikuDownload(Winter2022AnimeDownload, NewsTemplate):
    title = 'Fantasy Bishoujo Juniku Ojisan to'
    keywords = [title, 'fabiniku']
    website = 'https://fabiniku.com/'
    twitter = 'fabiniku'
    hashtags = 'ファ美肉おじさん'
    folder_name = 'fabiniku'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ul.news_lists li',
                                    date_select='p.news_info_date', title_select='h3.news_title', id_select='a',
                                    date_func=lambda x: x.replace('年', '.').replace('月', '.').replace('日', ''),
                                    next_page_select='li.pager_lists_item',
                                    next_page_eval_index_class='current', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'wordpress/wp-content/uploads/2021/10/18201715/【PR】1018_fabiniku_ファ美肉おじさん完成ティザー-scaled-1.jpeg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wordpress/wp-content/themes/fabiniku/assets/img/character/img%s.png'
        self.download_by_template(folder, template, 1, 1)


# Hakozume: Kouban Joshi no Gyakushuu
class HakozumeDownload(Winter2022AnimeDownload, NewsTemplate3):
    title = 'Hakozume: Kouban Joshi no Gyakushuu'
    keywords = [title, 'Police in a Pod']
    website = 'https://hakozume-anime.com/'
    twitter = 'hakozume_anime'
    hashtags = 'ハコヅメ'
    folder_name = 'hakozume'

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
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/E7tsWw7VUAIhRav?format=jpg&name=medium')
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'assets/top/t1/vis.jpg')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/FEi5uNYaUAIOmIY?format=jpg&name=medium')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'assets/top/k%s/vis.jpg'
        for i in range(1, 11, 1):
            image_name = f'kv{i}'
            if self.is_image_exists(image_name, folder):
                continue
            image_url = template % str(i)
            result = self.download_image(image_url, f'{folder}/{image_name}')
            if result == -1:
                break

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'assets/character/'
        templates = [prefix + 'c/%s.png', prefix + 'f/%s.png']
        self.download_by_template(folder, templates, 1, 1, prefix=['c_', 'f_'])


# Kaijin Kaihatsubu no Kuroitsu-san
class KuroitsusanDownload(Winter2022AnimeDownload, NewsTemplate):
    title = 'Kaijin Kaihatsubu no Kuroitsu-san'
    keywords = [title]
    website = 'https://kuroitsusan-anime.com/'
    twitter = 'kuroitsusan'
    hashtags = '黒井津さん'
    folder_name = 'kuroitsusan'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.list-item',
                                    date_select='.item-date', title_select='.text-row', id_select='a',
                                    date_separator='_')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FA_AHLfVEAMNrqD?format=jpg&name=4096x4096')
        self.add_to_image_list('top_pc_img_01', self.PAGE_PREFIX + 'img/top/top_pc_img_01.png')
        self.add_to_image_list('top_pc_img_02', self.PAGE_PREFIX + 'img/top/top_pc_img_02.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'img/character/detail/pc/pc_img_%s.png'
        self.download_by_template(folder, template, 2, 1)


# Karakai Jouzu no Takagi-san 3
class Takagisan3Download(Winter2022AnimeDownload, NewsTemplate):
    title = 'Karakai Jouzu no Takagi-san 3'
    keywords = [title, 'Takagisan', 'Teasing Master Takagi-san']
    website = 'https://takagi3.me/'
    twitter = 'takagi3_anime'
    hashtags = '高木さんめ'
    folder_name = 'takagisan3'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.newsList', date_select='time',
                                    title_select='span.newsList__name', id_select='a', a_tag_prefix=news_url,
                                    a_tag_start_text_to_remove='./')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/E-MCnEaUYAc-D9X?format=jpg&name=900x900')
        self.add_to_image_list('top_story__pcvs', self.PAGE_PREFIX + 'assets/img/top/top_story__pcvs.jpg')
        self.download_image_list(folder)

        prefix = self.PAGE_PREFIX + 'assets/img/top/'
        templates = [prefix + 'fv_mv%s.jpg', prefix + 'footer_mv%s.jpg']
        self.download_by_template(folder, templates, 1, 1)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            a_tags = soup.select('li.charaList a')
            self.image_list = []
            template = self.PAGE_PREFIX + 'assets/img/top/character/character-main%s.jpg'
            for a_tag in a_tags:
                if a_tag.has_attr('href') and a_tag['href'].startswith("javascript:chara('") and \
                        a_tag['href'].endswith("');"):
                    href = a_tag['href']
                    image_url = template % href[18:len(href) - 3]
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)


# Kenja no Deshi wo Nanoru Kenja
class KendeshiDownload(Winter2022AnimeDownload, NewsTemplate):
    title = 'Kenja no Deshi wo Nanoru Kenja'
    keywords = [title, 'Kendeshi', 'She Professed Herself Pupil of the Wise Man']
    website = 'https://kendeshi-anime.com/'
    twitter = 'kendeshi_anime'
    hashtags = '賢でし'
    folder_name = 'kendeshi'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='#news li', date_select=None,
                                    title_select='span', id_select='a', a_tag_prefix=news_url,
                                    date_func=lambda x: x[0:10])

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv1', 'https://pbs.twimg.com/media/ExX8OtZVcAs2aEk?format=jpg&name=4096x4096')
        self.add_to_image_list('main_pc', self.PAGE_PREFIX + '_img/main_pc.jpg')
        self.add_to_image_list('kv2_tw', 'https://pbs.twimg.com/media/E5Cte8ZVIAY8TJg?format=jpg&name=4096x4096')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'news/_image/keyvisual%s.png'
        self.download_by_template(folder, template, 2, 2)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + '_img/cha%s.png'
        self.download_by_template(folder, template)


# Leadale no Daichi nite
class LeadaleDownload(Winter2022AnimeDownload, NewsTemplate3):
    title = 'Leadale no Daichi nite'
    keywords = [title, 'World of Leadale']
    website = 'https://leadale.net/'
    twitter = 'leadale_anime'
    hashtags = ['leadale', 'リアデイル']
    folder_name = 'leadale'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_character()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/character/c/%s.png'
        self.download_by_template(folder, template, 1, 1, prefix='c', save_zfill=2)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'assets/top/main-t1/vis.jpg')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/Ezi8NqIVkAMv0Yv?format=jpg&name=medium')
        self.add_to_image_list('kv2_tw', 'https://pbs.twimg.com/media/E8Ouua3UUAIFSvH?format=jpg&name=medium')
        self.add_to_image_list('kv3_tw', 'https://pbs.twimg.com/media/FEmTgkJUcAUk9kQ?format=jpg&name=4096x4096')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'assets/news/kv-t%s.jpg'
        template2 = self.PAGE_PREFIX + 'assets/special/vis/%s.jpg'
        self.download_by_template(folder, template, 1, 1)
        self.download_by_template(folder, template2, 1, 1, prefix='kv_s')


# Mahouka Koukou no Rettousei: Tsuioku-hen
class Mahouka3Download(Winter2022AnimeDownload, NewsTemplate):
    title = "Mahouka Koukou no Rettousei: Tsuioku-hen"
    keywords = [title, "The Irregular at Magic High School: Reminiscence Arc", "3rd"]
    website = 'https://mahouka.jp/'
    twitter = 'mahouka_anime'
    hashtags = 'mahouka'
    folder_name = 'mahouka3'

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
        # Next page logic may need updates
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, paging_type=1, article_select='li.c-list__item',
                                    date_select='div.c-list__item-date', title_select='div.c-list__item-title',
                                    id_select='a', a_tag_prefix=news_url, a_tag_replace_from='./',
                                    date_func=lambda x: x[0:4] + '.' + x[5:].replace('/', '.'),
                                    next_page_select='div.c-pagination__arrow.-next',
                                    next_page_eval_index_class='is-disable')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'assets/img/top/img_main.jpg')
        # self.add_to_image_list('kv1', self.PAGE_PREFIX + 'news/SYS/CONTENTS/5618109f-c116-4a2a-96d1-43644cce1fa3/w850')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            images = soup.select('div.p-in-main img')
            self.image_list = []
            for image in images:
                if image.has_attr('src'):
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)


# Princess Connect! Re:Dive Season 2
class Priconne2Download(Winter2022AnimeDownload, NewsTemplate):
    title = "Princess Connect! Re:Dive Season 2"
    keywords = [title, "Priconne"]
    website = "https://anime.priconne-redive.jp/"
    twitter = 'priconne_anime'
    hashtags = ['プリコネ', 'プリコネR', 'アニメプリコネ', 'アニメプリコネR']
    folder_name = 'priconne2'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ul.newsList li',
                                    date_select='time', title_select='div.desc', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'assets/images/top_kv.png')
        self.add_to_image_list('kv_bg_pc', self.PAGE_PREFIX + 'assets/images/top/kv_bg_pc.png')
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'app/wp-content/uploads/2021/08/b34c29383da0e37a1104e94492001b1a.png')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'assets/images/top/kv_chara%s_pc.png'
        self.download_by_template(folder, template, 2, 1, 4)


# Shikkakumon no Saikyou Kenja
class ShikkakumonDownload(Winter2022AnimeDownload, NewsTemplate2):
    title = 'Shikkakumon no Saikyou Kenja'
    keywords = [title, 'The Strongest Sage of Disqualified Crest']
    website = 'https://shikkakumon.com/'
    twitter = 'shikkakumon_PR'
    hashtags = '失格紋'
    folder_name = 'shikkakumon'

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
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.png')
        self.add_to_image_list('teaser_tw', 'https://pbs.twimg.com/media/EtDguMkU0AQjk4b?format=jpg&name=4096x4096')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'core_sys/images/main/tz/char'
        templates = [prefix + '%s_stand.png', prefix + '%s_face.png']
        self.download_by_template(folder, templates, 2, 1, prefix='tz_')


# Slow Loop
class SlowLoopDownload(Winter2022AnimeDownload, NewsTemplate):
    title = 'Slow Loop'
    keywords = [title]
    website = 'https://slowlooptv.com/'
    twitter = 'slowloop_tv'
    hashtags = 'slowloop'
    folder_name = 'slow-loop'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, news_prefix='news.html', article_select='article',
                                    date_select='div.news_list_day', title_select='div.news_list_title',
                                    id_select='a', a_tag_prefix=self.PAGE_PREFIX, date_separator='/')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('announce', 'https://pbs.twimg.com/media/Ep5-SoLUUAAHq36?format=jpg&name=4096x4096')
        self.add_to_image_list('announce_2', self.PAGE_PREFIX + 'images/top/v_001.jpg')
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'images/top/v_002_02.jpg')
        self.add_to_image_list('teaser_tw', 'https://pbs.twimg.com/media/E15YSghVgAIdgJf?format=jpg&name=medium')
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'images/top/v_003.jpg')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/E9eeba0VIAYQ3-l?format=jpg&name=medium')
        self.add_to_image_list('kv2_tw', 'https://pbs.twimg.com/media/FEyFu9eaIAE9mfc?format=jpg&name=large')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'images/top/v_%s.jpg'
        self.download_by_template(folder, template, 3, 4)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'images/chara/p_%s.png'
        self.download_by_template(folder, template, 3, 1)

        template2 = self.PAGE_PREFIX + 'images/news/p_%s.jpg'
        self.download_by_template(folder, template2, 3, 8, 10, prefix='news_')


# Sono Bisque Doll wa Koi wo Suru
class KisekoiDownload(Winter2022AnimeDownload, NewsTemplate):
    title = 'Sono Bisque Doll wa Koi wo Suru'
    keywords = [title, 'kisekoi', 'My Dress-Up Darling']
    website = 'https://bisquedoll-anime.com/'
    twitter = 'kisekoi'
    hashtags = '着せ恋'
    folder_name = 'kisekoi'

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
        # Paging logic not known
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.p-news__list-item',
                                    date_select='div.p-in-data', title_select='div.p-in-title',
                                    id_select=None, id_has_id=True, id_attr='data-news-id', news_prefix='',
                                    a_tag_prefix=self.PAGE_PREFIX + '?news=')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/FBs3mm8VUAAoYEo?format=jpg&name=4096x4096')
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'assets/teaser/img/kv_image.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/teaser/img/chara_%s.png'
        self.download_by_template(folder, template, 1, 1, prefix='tz_')


# Tensai Ouji no Akaji Kokka Saisei Jutsu: Souda, Baikoku shiyou
class TensaiOujiDownload(Winter2022AnimeDownload, NewsTemplate2):
    title = 'Tensai Ouji no Akaji Kokka Saisei Jutsu: Souda, Baikoku shiyou'
    keywords = [title, 'tensaiouji']
    website = 'https://tensaiouji-anime.com/'
    twitter = 'tensaiouji_PR'
    hashtags = ['天才王子', '天才王子の赤字国家再生術']
    folder_name = 'tensaiouji'

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
        self.download_template_news(self.PAGE_PREFIX, 'news/list00010000.html')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv', self.PAGE_PREFIX + 'core_sys/images/main/home/kv.jpg')
        self.add_to_image_list('kv1_5', self.PAGE_PREFIX + 'core_sys/images/main/home/kv_1_5.jpg')
        self.add_to_image_list('kv1_5_tw', 'https://pbs.twimg.com/media/E_PAfkYVgAc6n2Q?format=jpg&name=large')
        self.add_to_image_list('kv2_tw', 'https://pbs.twimg.com/media/FEfLUMjVIAg-mP5?format=jpg&name=4096x4096')
        self.download_image_list(folder)

        template = f'{self.PAGE_PREFIX}core_sys/images/main/home/kv%s.jpg'
        self.download_by_template(folder, template, 1, 2)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'core_sys/images/main/cont/char/c%s_%s.png'
        templates = [template % ('%s', '01'), template % ('%s', '02')]
        self.download_by_template(folder, templates, 2, 1)
