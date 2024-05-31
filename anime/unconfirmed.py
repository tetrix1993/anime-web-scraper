import os
import requests
import datetime
import anime.constants as constants
from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate3

# Anohana S2 https://10th.anohana.jp/ #あの花 #anohana @anohana_project
# ATRI -My Dear Moments- https://atri-anime.com/ #ATRI @ATRI_anime
# Giji Harem https://gijiharem.com/ #疑似ハーレム @GijiHarem
# Isekai de Mofumofu Nadenade suru Tame ni Ganbattemasu. https://mohunadeanime.com/ #もふなで @mohunade_anime
# Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita 2nd Season https://slime300-anime.com/ #スライム倒して300年 @slime300_PR
# Tsuyokute New Saga https://tsuyosaga-pr.com/ #つよサガ @tsuyosaga_pr
# Vlad Love https://www.vladlove.com/index.html #ぶらどらぶ #vladlove @VLADLOVE_ANIME


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


# ATRI -My Dear Moments-
class AtriDownload(UnconfirmedDownload):
    title = 'ATRI -My Dear Moments-'
    keywords = [title]
    website = 'https://atri-anime.com/'
    twitter = 'ATRI_anime'
    hashtags = 'ATRI'
    folder_name = 'atri'

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
        self.add_to_image_list('ATRI_visual', 'https://ogre.natalie.mu/media/news/comic/2022/0924/ATRI_visual.jpg')
        self.add_to_image_list('kv_kv_wide', self.PAGE_PREFIX + 'assets/img/kv/kv_wide.png')
        self.download_image_list(folder)


# Giji Harem
class GijiHaremDownload(UnconfirmedDownload, NewsTemplate2):
    title = "Giji Harem"
    keywords = [title]
    website = 'https://gijiharem.com/'
    twitter = 'GijiHarem'
    hashtags = '疑似ハーレム'
    folder_name = 'gijiharem'

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
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.kvSlide__img source[srcset]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset']
                if '/main/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'main')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')


# Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita 2nd Season
class Slime3002Download(UnconfirmedDownload, NewsTemplate):
    title = "Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita 2nd Season"
    keywords = [title, "I've Been Killing Slimes for 300 Years and Maxed Out My Level", "Slime 300", "slime300", '2nd']
    website = 'https://slime300-anime.com/'
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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-list li',
                                    date_select='.date', title_select='p:nth-child(2)', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        # self.image_list = []
        # self.add_to_image_list('announce', self.PAGE_PREFIX + '/static/944a17585cc6d3dccaf125c0201aab71/99383/promo.png')
        # self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.slider img[src*="/images/"]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('./', '')
                image_name = self.generate_image_name_from_url(image_url, 'images')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')


# Tsuyokute New Saga
class TsuyosagaDownload(UnconfirmedDownload, NewsTemplate):
    title = 'Tsuyokute New Saga'
    keywords = [title, 'New Saga', 'Tsuyosaga']
    website = 'https://tsuyosaga-pr.com/'
    twitter = 'tsuyosaga_pr'
    hashtags = 'つよサガ'
    folder_name = 'tsuyosaga'

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
        pass

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_aniverse', 'https://aniverse-mag.com/wp-content/uploads/2022/10/1628619ceb9f5f0127d70926036c5ffd.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/newsaga/static/character/%s/main.png'
        for i in range(10):
            number = str(i + 1).zfill(2)
            image_name = 'tz_char' + number
            if self.is_image_exists(image_name, folder):
                continue
            image_url = template % number
            result = self.download_image(image_url, folder + '/' + image_name)
            if result == -1:
                break


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
