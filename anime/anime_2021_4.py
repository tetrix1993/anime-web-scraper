import os
import anime.constants as constants
from anime.main_download import MainDownload
from datetime import datetime
from scan import AniverseMagazineScanner, MocaNewsScanner, WebNewtypeScanner


# Muv-Luv Alternative https://muv-luv-alternative-anime.com/ #マブラヴ #マブラヴアニメ #muvluv @Muv_Luv_A_anime
# Saihate no Paladin https://farawaypaladin.com/ #最果てのパラディン #faraway_paladin @faraway_paladin
# Senpai ga Uzai Kouhai no Hanashi https://senpaiga-uzai-anime.com/ #先輩がうざい後輩の話 @uzai_anime
# Taishou Otome Otogibanashi http://taisho-otome.com/ #大正オトメ #昭和オトメ @otome_otogi
# Tate no Yuusha S2 http://shieldhero-anime.jp/ #shieldhero #盾の勇者の成り上がり @shieldheroanime
# Yuuki Yuuna wa Yuusha de Aru: Dai Mankai no Shou https://yuyuyu.tv/season2/ #yuyuyu @anime_yukiyuna


# Fall 2021 Anime
class Fall2021AnimeDownload(MainDownload):
    season = "2021-4"
    season_name = "Fall 2021"
    folder_name = '2021-4'

    def __init__(self):
        super().__init__()


# Muv-Luv Alternative
class MuvLuvAlternativeDownload(Fall2021AnimeDownload):
    title = 'Muv-Luv Alternative'
    keywords = [title]
    folder_name = 'muv-luv-alt'

    PAGE_PREFIX = 'https://muv-luv-alternative-anime.com/'

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
            for page in range(1, 2, 1):
                page_url = news_url
                if page > 1:
                    page_url = news_url + 'page/' + str(page) + '/'
                soup = self.get_soup(page_url, decode=True)
                articles = soup.select('section.u-mg_b_l5 a')
                for article in articles:
                    tag_date = article.find('span', class_='c-thumb-list__date')
                    tag_title = article.find('span', class_='c-thumb-list__title')
                    if tag_date and tag_title and article.has_attr('href'):
                        article_id = news_url + article['href'].replace('./', '')
                        date = self.format_news_date(tag_date.text.strip())
                        if len(date) == 0:
                            continue
                        title = tag_title.text.strip()
                        if news_obj and (news_obj['id'] == article_id or date < news_obj['date']):
                            stop = True
                            break
                        results.append(self.create_news_log_object(date, title, article_id))
                if stop:
                    break
                # pagination = soup.select('ul.c-pagenation li.c-pagenation__item')
                # if len(pagination) == 0:
                #     break
                # if pagination[-1].has_attr('class') and 'is__current' in pagination[-1]['class']:
                #     break
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
        self.add_to_image_list('visual_1b', self.PAGE_PREFIX + 'img/teaser/visual_1b.jpg')
        self.download_image_list(folder)
        self.download_by_template(folder, self.PAGE_PREFIX + 'img/teaser/visual_%s.jpg', 1, 2)


# Saihate no Paladin
class SaihatenoPaladinDownload(Fall2021AnimeDownload):
    title = 'Saihate no Paladin'
    keywords = [title, 'The Faraway Paladin']
    folder_name = 'saihate-no-paladin'

    PAGE_PREFIX = 'https://farawaypaladin.com/'

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
        self.add_to_image_list('kv1', 'https://pbs.twimg.com/media/EzKrTkqVkAMxXZW?format=jpg&name=large')
        self.add_to_image_list('main_visual-min', self.PAGE_PREFIX + 'img/main_visual-min.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'img/cara%s.png'
        self.download_by_template(folder, template, 1)


# Senpai ga Uzai Kouhai no Hanashi
class SenpaigaUzaiDownload(Fall2021AnimeDownload):
    title = 'Senpai ga Uzai Kouhai no Hanashi'
    keywords = [title]
    folder_name = 'senpaiga-uzai'

    PAGE_PREFIX = 'https://senpaiga-uzai-anime.com/'

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
            articles = soup.select('article.article_contents article')
            news_obj = self.get_last_news_log_object()
            results = []
            for article in articles:
                if not article.has_attr('id'):
                    continue
                tag_date = article.find('time')
                tag_title = article.find('h3')
                if tag_date and tag_title:
                    article_id = article['id']
                    date = self.format_news_date(tag_date.text)
                    if len(date) == 0:
                        continue
                    title = tag_title.text
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
        self.add_to_image_list('main-visual', self.PAGE_PREFIX + 'img/top/main-visual.png')
        self.add_to_image_list('visual', 'https://pbs.twimg.com/media/Ez4yUbfVkAMPgny?format=jpg&name=4096x4096')
        self.download_image_list(folder)


# Taishou Otome Otogibanashi
class TaishoOtomeDownload(Fall2021AnimeDownload):
    title = 'Taishou Otome Otogibanashi'
    keywords = [title, 'Taisho Otome']
    folder_name = 'taisho-otome'

    PAGE_PREFIX = 'http://taisho-otome.com/'

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
            soup = self.get_soup(news_url, decode=True)
            lis = soup.select('ul.newslist li')
            news_obj = self.get_last_news_log_object()
            results = []
            for li in lis:
                tag_date = li.find('div', class_='newslist_date')
                tag_title = li.find('h2', class_='newslist_ttl')
                a_tag = li.find('a')
                if tag_date and tag_title and a_tag and a_tag.has_attr('href'):
                    article_id = news_url + a_tag['href'].replace('./', '')
                    date = self.format_news_date(tag_date.text.strip().replace('年', '.').replace('月', '.').replace('日', ''))
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
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/taisho-otome/img/index/%s.jpg'
        template_name = 'img_kv%s'
        self.image_list = []
        self.add_to_image_list(template_name % '01', template % (template_name % '01'))
        self.add_to_image_list(template_name % '02', template % (template_name % '02'))
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/taisho-otome/img/character/img_chara%s.png'
        self.download_by_template(folder, template, 2)


# Tate no Yuusha no Nariagari S2
class TateNoYuusha2Download(Fall2021AnimeDownload):
    title = "Tate no Yuusha no Nariagari 2nd Season"
    keywords = [title, "The Rising of the Shield Hero"]
    folder_name = 'tate-no-yuusha2'

    PAGE_PREFIX = "http://shieldhero-anime.jp"

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
        try:
            soup = self.get_soup(news_url, decode=True)
            articles = soup.select('article.p-newspage_item')
            news_obj = self.get_last_news_log_object()
            results = []
            for article in articles:
                tag_date = article.find('span', class_='a')
                tag_title = article.find('h2', class_='txt')
                if tag_date and tag_title and tag_title.has_attr('id'):
                    article_id = tag_title['id'].strip()
                    date = self.format_news_date(tag_date.text.strip())
                    if len(date) == 0:
                        continue
                    title = tag_title.text.strip()
                    if date.startswith('2019.08') or (news_obj
                                                      and (news_obj['id'] == article_id or date < news_obj['date'])):
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
        self.add_to_image_list('announce', 'https://pbs.twimg.com/media/EDag4MkUwAAQnf0?format=jpg&name=medium')
        self.add_to_image_list('kv1', 'https://pbs.twimg.com/media/EhHFvyVU4AA7cUw?format=jpg&name=large')
        self.add_to_image_list('mv_lg', self.PAGE_PREFIX + '/assets/img/2nd/mv_lg.jpg')
        self.download_image_list(folder)


# Yuuki Yuuna wa Yuusha de Aru: Dai Mankai no Shou
class Yuyuyu3Download(Fall2021AnimeDownload):
    title = "Yuuki Yuuna wa Yuusha de Aru: Dai Mankai no Shou"
    keywords = [title, "Yuyuyu", "Yuki Yuna is a Hero"]
    folder_name = 'yuyuyu3'

    PAGE_PREFIX = 'https://yuyuyu.tv/season2/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        prefix = 'https://yuyuyu.tv'
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
                        if article_id == (news_url + 'archives/1770'):
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
        self.add_to_image_list('tw_visual1', 'https://pbs.twimg.com/media/EeUu6NHVAAAqYgu?format=jpg&name=large')
        self.add_to_image_list('tw_visual2', 'https://pbs.twimg.com/media/E0L1PAhVEAICS7o?format=jpg&name=4096x4096')
        self.download_image_list(folder)
        self.download_by_template(folder, self.PAGE_PREFIX + 'img/home/visual_%s.jpg', 2, 10)
