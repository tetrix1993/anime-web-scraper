import os
import re
import requests
from anime.external_download import AniverseMagazineDownload, WebNewtypeDownload, MocaNewsDownload, NatalieDownload
from bs4 import BeautifulSoup as bs
from datetime import datetime
from datetime import timedelta


class MainScanner():

    MAXIMUM_PAGES = 10
    
    def __init__(self):
        pass
        
    def run(self):
        pass
    
    @staticmethod
    def get_response(url, headers=None, decode=False):
        response = ""
        if headers == None:
            headers = {}
            headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        try:
            result = requests.get(url, headers=headers)
            if (decode):
                response = str(result.content.decode())
            else:
                response = str(result.content)
        except Exception as e:
            print(e)
        return response

    @staticmethod
    def get_soup(url, headers=None, decode=False, charset=None):
        if headers == None:
            headers = {}
            headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        try:
            result = requests.get(url, headers=headers)
            if decode:
                if charset is None:
                    return bs(result.content.decode(), 'html.parser')
                else:
                    return bs(result.content.decode(charset), 'html.parser')
            else:
                return bs(result.text, 'html.parser')
        except Exception as e:
            print(e)
        return ""

    @staticmethod
    def is_image_exists(name, filepath):
        filename = 'download/' + filepath + '/' + name
        return os.path.exists(filename + '.jpg') \
            or os.path.exists(filename + '.png') \
            or os.path.exists(filename + '.gif') \
            or os.path.exists(filename + '.webp')


class AniverseMagazineScanner(MainScanner):
    
    # Example prefix: https://aniverse-mag.com/page/2?s=プランダラ
    SEARCH_URL = "https://aniverse-mag.com/page/%s?s=%s"
    
    def __init__(self, keyword, base_folder, last_episode=None, suffix=None, min_width=None):
        super().__init__()
        self.keyword = keyword
        self.base_folder = base_folder.replace("download/","") + "/aniverse"
        self.last_episode = last_episode
        self.suffix = suffix
        self.min_width = min_width

    @staticmethod
    def has_results(text):
        return "<h2>Sorry, nothing found.</h2>" not in text

    @staticmethod
    def has_next_page(text):
        return '<i class="fa fa-long-arrow-right">' in text

    @staticmethod
    def get_episode_num(result, suffix):
        split1 = result[0].split(suffix)[0].split('第')
        if len(split1) < 2:
            return -1
        try:
            return int(split1[1])
        except:
            return -1

    @staticmethod
    def get_article_id(url):
        split1 = url.split('/')
        if len(split1) < 1:
            return ""
        return split1[len(split1)-1]
        
    def process_page(self, text):
        split1 = text.split('<h2 class="cb-post-title">')
        for i in range(1, len(split1), 1):
            split2 = split1[i].split('</a>')[0].split('">')
            if len(split2) < 2:
                continue
            news_title = split2[1].split('</a>')[0]

            suffix = self.suffix
            if suffix is None:
                suffix = '話'

            regex = '第' + '[０|１|２|３|４|５|６|７|８|９|0-9]+' + suffix
            prog = re.compile(regex)
            result = prog.findall(news_title)
            if self.keyword in news_title and ('最終' + suffix) in news_title and len(result) == 0:
                episode = 'last'
            elif self.keyword in news_title and len(result) > 0:
                episode_num = self.get_episode_num(result, suffix)
                if episode_num < 1:
                    continue
                episode = str(episode_num).zfill(2)
            else:
                continue

            #if self.keyword not in news_title or '先行' not in news_title or '第' not in news_title or '話' not in news_title:
            #    continue
            #episode_num = self.get_episode_num(news_title)
            #if episode_num < 1:
            #    continue
            #episode = str(episode_num).zfill(2)
            if os.path.isfile(self.base_folder + "/" + episode + "_01.jpg"):
                return 1
            split3 = split2[0].split('<a href="')
            if len(split3) < 2:
                continue
            url = split3[1]
            article_id = self.get_article_id(url)
            if len(article_id) == 0:
                continue
            AniverseMagazineDownload(article_id, self.base_folder, episode, min_width=self.min_width).run()
        
    def run(self):
        if self.last_episode:
            # Stop processing if the last episode has already been downloaded
            if self.is_image_exists(str(self.last_episode).zfill(2) + '_01', self.base_folder) or\
                    self.is_image_exists('last_01', self.base_folder):
                return

        first_page_url = self.SEARCH_URL % ("1", self.keyword)
        first_page_response = self.get_response(url=first_page_url,decode=True)
        if self.has_results(first_page_response):
            response = first_page_response
            result = self.process_page(response)
            if result == 1:
                return
            page = 2
            while page <= self.MAXIMUM_PAGES:
                if not self.has_next_page(response):
                    break
                next_url = self.SEARCH_URL % (str(page), self.keyword)
                response = self.get_response(url=next_url, decode=True)
                result = self.process_page(response)
                if result == 1:
                    return
                page += 1


class WebNewtypeScanner(MainScanner):
    
    PAGE_PREFIX = "https://webnewtype.com/"
    SEARCH_PREFIX = "https://webnewtype.com/news/nrsearch/"
    
    def __init__(self, keyword, base_folder, last_episode=None):
        super().__init__()
        self.keyword = keyword
        self.base_folder = base_folder.replace("download/","") + "/wnt"
        self.last_episode = last_episode

    @staticmethod
    def has_results(text):
        return "<li>記事はありません</li>" not in text

    @staticmethod
    def has_next_page(text):
        return '<img src="/img/pager_right.png"' in text and '<span class="pageNumber"><img src="/img/pager_right.png"' not in text

    @staticmethod
    def get_episode_num(result):
        split1 = result[0].split('話')[0].split('第')
        if len(split1) < 2:
            return -1
        try:
            return int(split1[1])
        except:
            return -1

    @staticmethod
    def get_article_id(url):
        split1 = url.split('/')
        if len(split1) < 3:
            return ""
        return split1[len(split1)-2]
    
    def process_page(self, text):
        split1 = text.split('<div class="listBox">')
        if len(split1) < 2:
            return
        split2 = split1[1].split('</ul>')[0].split('<li>')
        for i in range(1, len(split2), 1):
            split3 = split2[i].split('<p class="newsTitle">')
            if len(split3) < 2:
                continue
            news_title = split3[1].split('</p>')[0]
            regex = '第' + '[０|１|２|３|４|５|６|７|８|９|0-9]+' + '話'
            prog = re.compile(regex)
            result = prog.findall(news_title)
            if self.keyword in news_title and '最終話' in news_title and '先行' in news_title:
                episode = 'last'
            elif self.keyword in news_title and '先行' in news_title and len(result) > 0:
                episode_num = self.get_episode_num(result)
                if episode_num < 1:
                    continue
                episode = str(episode_num).zfill(2)
            else:
                continue
            if os.path.isfile(self.base_folder + "/" + episode + "_01.jpg"):
                return 1
            split4 = split2[i].split('<a href="')
            if len(split4) < 2:
                continue
            url = split4[1].split('"')[0]
            article_id = self.get_article_id(url)
            if len(article_id) == 0:
                continue
            WebNewtypeDownload(article_id, self.base_folder, episode).run()
        return 0

    def run(self):
        if self.last_episode:
            # Stop processing if the last episode has already been downloaded
            stop = False
            for i in reversed(range(self.last_episode)):
                if self.is_image_exists(str(i + 1).zfill(2) + '_01', self.base_folder) or \
                        self.is_image_exists('last_01', self.base_folder):
                    stop = True
                    break
            if stop:
                return

        first_page_url = self.SEARCH_PREFIX + self.keyword + '/'
        first_page_response = self.get_response(url=first_page_url,decode=True)
        if self.has_results(first_page_response):
            response = first_page_response
            result = self.process_page(response)
            if result == 1:
                return
            page = 2
            while page <= self.MAXIMUM_PAGES:
                if not self.has_next_page(response):
                    break
                next_url = self.SEARCH_PREFIX + self.keyword + '/' + str(page) + '/'
                response = self.get_response(url=next_url, decode=True)
                result = self.process_page(response)
                if result == 1:
                    return
                page += 1


class MocaNewsScanner(MainScanner):

    PAGE_URL_TEMPLATE = 'https://moca-news.net/article/%s/'

    def __init__(self, keyword, base_folder, start_date, end_date, ignore_cache=False):
        super().__init__()
        self.keyword = keyword
        self.base_folder = base_folder + "/moca"
        self.start_date = datetime.strptime(start_date, '%Y%m%d')
        self.end_date = datetime.strptime(end_date, '%Y%m%d')
        self.ignore_cache = ignore_cache
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def write_cache(self, date):
        cache_filepath = self.base_folder + '/cache'
        with open(cache_filepath, 'w+') as f:
            f.write(date.strftime('%Y%m%d'))

    def read_last_read_date(self):
        date = None
        if self.ignore_cache:
            return date
        cache_filepath = self.base_folder + '/cache'
        if os.path.exists(cache_filepath):
            with open(cache_filepath, 'r') as f:
                date_str = f.read().strip()
            try:
                date = datetime.strptime(date_str, '%Y%m%d')
            except:
                pass
        return date

    @staticmethod
    def get_episode_num(result):
        split1 = result[0].split('話')[0].split('第')
        if len(split1) < 2:
            return -1
        try:
            return int(split1[1])
        except:
            return -1

    @staticmethod
    def get_article_id(text):
        split1 = text.split('/')
        if len(split1) == 6:
            return split1[2] + '/' + split1[3]
        else:
            return None

    def run(self):
        last_read_date = self.read_last_read_date()
        regex = '第' + '[０|１|２|３|４|５|６|７|８|９|0-9]+' + '話'
        curr_date = self.end_date
        while self.start_date <= curr_date and (last_read_date is None or last_read_date <= curr_date):
            date_str = curr_date.strftime('%Y%m%d')
            page_url = self.PAGE_URL_TEMPLATE % date_str
            soup = self.get_soup(page_url, decode=True, charset='shift_jisx0213')
            try:
                article_divs = soup.find('div', id='main-area').find_all('div', class_='linkblock')
                for article_div in article_divs:
                    article_title = article_div.find('div', class_='fontbold').text
                    prog = re.compile(regex)
                    result = prog.findall(article_title)
                    if self.keyword in article_title and '最終話' in article_title and '先行' in article_title:
                        episode = 'last'
                    elif self.keyword in article_title and '先行' in article_title and len(result) > 0:
                        episode_num = self.get_episode_num(result)
                        if episode_num < 1:
                            continue
                        episode = str(episode_num).zfill(2)
                    else:
                        continue
                    image_url = article_div.find('img')['src']
                    article_id = self.get_article_id(image_url)
                    MocaNewsDownload(article_id, self.base_folder.replace('download/', ''), episode).run()
            except:
                pass
            curr_date -= timedelta(days=1)

        self.write_cache(self.end_date)


class NatalieScanner(MainScanner):
    SEARCH_URL_TEMPLATE = 'https://natalie.mu/search?context=news&query=%s&g=comic&page=%s'
    ARTICLE_URL_TEMPLATE = 'https://natalie.mu/comic/news/%s'

    def __init__(self, keyword, base_folder, last_episode=None, suffix=None):
        super().__init__()
        self.keyword = keyword
        self.base_folder = base_folder.replace("download/","") + "/natalie"
        self.last_episode = last_episode
        self.suffix = suffix

    @staticmethod
    def has_results(soup):
        empty_section = soup.find('div', class_='NA_section_empty')
        return empty_section is None

    @staticmethod
    def has_next_page(soup):
        next_page = soup.find('li', class_='NA_pager_next')
        return next_page is not None

    @staticmethod
    def get_episode_num(result, suffix):
        split1 = result[0].split(suffix)[0].split('第')
        if len(split1) < 2:
            return -1
        try:
            return int(split1[1])
        except:
            return -1

    @staticmethod
    def get_article_id(url):
        split1 = url.split('/')
        if len(split1) < 1:
            return ""
        return split1[len(split1) - 1]

    def process_page(self, soup):
        cards = soup.find_all('div', 'NA_card-l')
        for card in cards:
            a_tag = card.find('a')
            if a_tag and a_tag.has_attr('href'):
                url = a_tag['href']
                article_id = self.get_article_id(url)
                if len(article_id) == 0:
                    continue
                card_title = a_tag.find('p', class_='NA_card_title')
                if card_title is None or len(card_title.text) == 0:
                    continue
                news_title = card_title.text
                suffix = self.suffix
                if suffix is None:
                    suffix = '話'

                regex = '第' + '[０|１|２|３|４|５|６|７|８|９|0-9]+' + suffix
                prog = re.compile(regex)
                result = prog.findall(news_title)
                if self.keyword in news_title and ('最終' + suffix) in news_title and len(result) == 0:
                    episode = 'last'
                elif self.keyword in news_title and len(result) > 0:
                    episode_num = self.get_episode_num(result, suffix)
                    if episode_num < 1:
                        continue
                    episode = str(episode_num).zfill(2)
                else:
                    continue
                if os.path.isfile(self.base_folder + "/" + episode + "_01.jpg"):
                    return 1

                image_title = None
                try:
                    image_title = '第' + str(int(episode)) + suffix
                except:
                    pass
                NatalieDownload(article_id, self.base_folder, episode, title=image_title).run()
        return 0

    def run(self):
        if self.last_episode:
            # Stop processing if the last episode has already been downloaded
            if self.is_image_exists(str(self.last_episode).zfill(2) + '_01', self.base_folder) or \
                    self.is_image_exists('last_01', self.base_folder):
                return

        first_page_url = self.SEARCH_URL_TEMPLATE % (self.keyword, '1')
        try:
            soup = self.get_soup(first_page_url)
            if self.has_results(soup):
                result = self.process_page(soup)
                if result == 1:
                    return
                page = 2
                while page <= self.MAXIMUM_PAGES:
                    if not self.has_next_page(soup):
                        break
                    next_url = self.SEARCH_URL_TEMPLATE % (self.keyword, str(page))
                    soup = self.get_soup(next_url)
                    result = self.process_page(soup)
                    if result == 1:
                        return
                    page += 1
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)
