import os
import re
import requests
import urllib.parse
from anime.external_download import AnimagePlusDownload, AnimeRecorderDownload, AniverseMagazineDownload, WebNewtypeDownload, MocaNewsDownload, NatalieDownload, EeoMediaDownload
from anime.constants import EXTERNAL_FOLDER_ANIMAGE_PLUS, EXTERNAL_FOLDER_ANIME_RECORDER, EXTERNAL_FOLDER_ANIVERSE, EXTERNAL_FOLDER_EEOMEDIA, EXTERNAL_FOLDER_MOCANEWS, EXTERNAL_FOLDER_NATALIE, EXTERNAL_FOLDER_WEBNEWTYPE, HTTP_HEADER_USER_AGENT
from bs4 import BeautifulSoup as bs
from datetime import datetime
from datetime import timedelta


class MainScanner:

    MAXIMUM_PAGES = 10
    download_id = None
    
    def __init__(self, download_id):
        self.download_id = download_id
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
            result.raise_for_status()
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
            result.raise_for_status()
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

    @staticmethod
    def convert_kanji_to_number(text):
        # Only 1 to 99
        if not isinstance(text, str):
            return None
        if len(text) == 0 or len(text) > 3:
            return None

        kanjis = ['十', '一', '二', '三', '四', '五', '六', '七', '八', '九']
        eval = []
        for character in text:
            for i in range(len(kanjis)):
                if character == kanjis[i]:
                    eval.append(i)

        if len(eval) == 1:
            if eval[0] == 0:
                return 10
            else:
                return eval[0]
        elif len(eval) == 2:
            if eval[0] == 0 and eval[1] > 0:
                return 10 + eval[1]
            if eval[1] == 0 and eval[0] > 1:
                return eval[0] * 10
        elif len(eval) == 3 and eval[1] == 0 and eval[0] > 1:
            return eval[0] * 10 + eval[2]
        return None


class AnimagePlusScanner(MainScanner):
    CSRF_TOKEN = '8ee2767dd32a5ee850903f79c87a84d7'
    SEARCH_API = 'https://animageplus.jp/search/index'
    HEADERS = HTTP_HEADER_USER_AGENT
    HEADERS['content-type'] = 'application/x-www-form-urlencoded'
    COOKIES = {'CSRF_cookie': CSRF_TOKEN}

    def __init__(self, keyword, base_folder, last_episode=None, suffix=None, end_date='00000000', skip_article_ids=[], download_id=None):
        super().__init__(download_id)
        self.keyword = keyword
        self.encoded_keyword = urllib.parse.quote(self.keyword)
        self.base_folder = base_folder.replace("download/", "") + "/" + EXTERNAL_FOLDER_ANIMAGE_PLUS
        self.last_episode = last_episode
        self.suffix = suffix
        self.end_date = end_date
        self.skip_article_ids = skip_article_ids

    def run(self):
        if self.last_episode:
            if self.is_image_exists(str(self.last_episode).zfill(2) + '_01', self.base_folder) or \
                    self.is_image_exists('last_01', self.base_folder):
                return

        payload = f'CSRF_token={self.CSRF_TOKEN}&term={self.encoded_keyword}&q=1'
        try:
            r = requests.post(url=self.SEARCH_API, cookies=self.COOKIES, data=payload, headers=self.HEADERS)
            if r.status_code == 200:
                soup = bs(r.content.decode(), 'html.parser')
                self.process_page(soup)
            else:
                raise Exception('Animage Scanner status code: ' + str(r.status_code))
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def process_page(self, soup):
        if soup is None:
            return -1
        articles = soup.select('.articlesList li a[href]')
        for article in articles:
            article_id = article['href'].split('/')[-1]
            if article_id in self.skip_article_ids:
                continue

            news_date_tag = article.select('.date')
            if len(news_date_tag) > 0:
                news_date = news_date_tag[0].text.replace('.', '')
                if news_date < self.end_date:
                    return 1

            title_tag = article.select('p.tit')
            if len(title_tag) == 0:
                continue
            news_title = ' '.join(title_tag[0].text.split())
            suffix = self.suffix
            if suffix is None:
                suffix = '話'

            regex = '第[０|１|２|３|４|５|６|７|８|９|十|一|二|三|四|五|六|七|八|九|0-9]+' + suffix
            prog = re.compile(regex)
            result = prog.findall(news_title)
            if ('最終' + suffix) in news_title and len(result) == 0:
                episode = 'last'
            elif len(result) > 0:
                episode_num = self.get_episode_num(result, suffix)
                if episode_num < 1:
                    continue
                episode = str(episode_num).zfill(2)
            else:
                continue
            filepath = self.base_folder + "/" + episode + "_01.jpg"
            if not filepath.startswith("download/"):
                filepath = "download/" + filepath
            if os.path.isfile(filepath):
                return 1
            AnimagePlusDownload(article_id, self.base_folder, episode, download_id=self.download_id).run()

    @staticmethod
    def get_episode_num(result, suffix):
        split1 = result[0].split(suffix)[0].split('第')
        if len(split1) < 2:
            return -1
        try:
            return int(split1[1])
        except:
            result = MainScanner.convert_kanji_to_number(split1[1])
            if result is not None:
                return result
            return -1


class AnimeRecorderScanner(MainScanner):
    SEARCH_URL_TEMPLATE = "https://www.anime-recorder.com/page/%s/?s=%s"

    def __init__(self, keyword, base_folder, last_episode=None, suffix=None, skip_article_ids=[], download_id=None):
        super().__init__(download_id)
        self.keyword = keyword
        self.base_folder = base_folder.replace("download/", "") + "/" + EXTERNAL_FOLDER_ANIME_RECORDER
        self.last_episode = last_episode
        self.suffix = suffix
        self.skip_article_ids = skip_article_ids

    @staticmethod
    def has_results(soup):
        if soup is None:
            return False
        article = soup.select('#post-not-found')
        return len(article) == 0

    @staticmethod
    def has_next_page(soup):
        if soup is None:
            return False
        next_page = soup.select('li a.next.page-numbers')
        return len(next_page) > 0

    @staticmethod
    def get_episode_num(result, suffix):
        split1 = result[0].split(suffix)[0].split('第')
        if len(split1) < 2:
            return -1
        try:
            return int(split1[1])
        except:
            result = MainScanner.convert_kanji_to_number(split1[1])
            if result is not None:
                return result
            return -1

    @staticmethod
    def get_article_id(url):
        eval = url
        if url.endswith('/'):
            eval = eval[0:len(eval)-1]
        if len(eval) < 1:
            return ""
        return eval.split('/')[-1]

    def process_page(self, soup):
        a_tags = soup.select('#inner-content article a')
        for a_tag in a_tags:
            if a_tag.has_attr('href') and a_tag.has_attr('title'):
                article_id = self.get_article_id(a_tag['href'])
                if article_id in self.skip_article_ids:
                    continue
                news_title = a_tag['title'].strip()
                suffix = self.suffix
                if suffix is None:
                    suffix = '話'

                regex = '第[０|１|２|３|４|５|６|７|８|９|十|一|二|三|四|五|六|七|八|九|0-9]+' + suffix
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
                filepath = self.base_folder + "/" + episode + "_01.jpg"
                if not filepath.startswith("download/"):
                    filepath = "download/" + filepath
                if os.path.isfile(filepath):
                    return 1
                AnimeRecorderDownload(article_id, self.base_folder, episode, download_id=self.download_id).run()
        return 0

    def run(self):
        if self.last_episode:
            if self.is_image_exists(str(self.last_episode).zfill(2) + '_01', self.base_folder) or \
                    self.is_image_exists('last_01', self.base_folder):
                return

        first_page_url = self.SEARCH_URL_TEMPLATE % ('1', self.keyword)
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


class AniverseMagazineScanner(MainScanner):
    
    # Example prefix: https://aniverse-mag.com/page/2?s=プランダラ
    SEARCH_URL = "https://aniverse-mag.com/page/%s?s=%s"
    enabled = True
    
    def __init__(self, keywords, base_folder, last_episode=None, suffix=None,
                 min_width=None, end_date='00000000', check_resize=False, download_id=None, prefix=None,
                 class_name=None):
        super().__init__(download_id)

        if isinstance(keywords, str):
            self.keywords = [keywords]
        elif isinstance(keywords, list):
            self.keywords = keywords
        else:
            raise Exception('Unexpected type for keywords')

        self.base_folder = base_folder.replace("download/","") + "/" + EXTERNAL_FOLDER_ANIVERSE
        self.last_episode = last_episode
        self.suffix = suffix
        self.min_width = min_width
        self.end_date = end_date
        self.prefix = prefix
        self.check_resize = check_resize
        self.class_name = class_name

    @staticmethod
    def has_results(text):
        return len(text) > 0 and "<h2>Sorry, nothing found.</h2>" not in text

    @staticmethod
    def has_next_page(text):
        return len(text) > 0 and '<i class="fa fa-long-arrow-right">' in text

    @staticmethod
    def get_episode_num(result, prefix, suffix):
        if len(prefix) > 0:
            if len(suffix) == 0:
                split1 = result[0].split(prefix)
            else:
                split1 = result[0].split(suffix)[0].split(prefix)
            if len(split1) < 2:
                return -1
            episode = split1[1]
        else:
            if len(suffix) == 0:
                episode = result[0]
            else:
                episode = result[0].split(suffix)[0]
        if len(episode) == 0:
            return -1
        
        try:
            return int(episode)
        except:
            result = MainScanner.convert_kanji_to_number(episode)
            if result is not None:
                return result
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
            split4 = split1[i].split('<time datetime="')
            if len(split4) < 2:
                continue
            news_date = split4[1].split('"')[0].replace('-', '')
            if news_date < self.end_date:
                return 1

            suffix = self.suffix
            if suffix is None:
                suffix = '話'

            prefix = self.prefix
            if prefix is None:
                prefix = '第'

            regex = prefix + '[０|１|２|３|４|５|６|７|８|９|十|一|二|三|四|五|六|七|八|九|0-9]+' + suffix
            prog = re.compile(regex)
            result = prog.findall(news_title)

            episode = None
            for keyword in self.keywords:
                if keyword in news_title and ('最終' + suffix) in news_title and len(result) == 0:
                    episode = 'last'
                    break
                elif keyword in news_title and len(result) > 0:
                    episode_num = self.get_episode_num(result, prefix, suffix)
                    if episode_num < 1:
                        break
                    episode = str(episode_num).zfill(2)
                    break
            if episode is None:
                continue

            #if self.keyword not in news_title or '先行' not in news_title or '第' not in news_title or '話' not in news_title:
            #    continue
            #episode_num = self.get_episode_num(news_title)
            #if episode_num < 1:
            #    continue
            #episode = str(episode_num).zfill(2)
            filepath = self.base_folder + "/" + episode + "_01.jpg"
            if not filepath.startswith("download/"):
                filepath = "download/" + filepath
            if os.path.isfile(filepath):
                return 1
            split3 = split2[0].split('<a href="')
            if len(split3) < 2:
                continue
            url = split3[1]
            article_id = self.get_article_id(url)
            if len(article_id) == 0:
                continue
            if self.class_name is not None:
                print(self.class_name + ' - Process Aniverse ' + AniverseMagazineDownload.PAGE_PREFIX + article_id)
            AniverseMagazineDownload(article_id, self.base_folder, episode,
                                     min_width=self.min_width, check_resize=self.check_resize,
                                     download_id=self.download_id).run()
        
    def run(self):
        if not self.enabled:
            return

        if self.last_episode:
            # Stop processing if the last episode has already been downloaded
            if self.is_image_exists(str(self.last_episode).zfill(2) + '_01', self.base_folder) or\
                    self.is_image_exists('last_01', self.base_folder):
                return

        keywords_str = '+'.join(self.keywords)
        first_page_url = self.SEARCH_URL % ("1", keywords_str)
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
                next_url = self.SEARCH_URL % (str(page), keywords_str)
                response = self.get_response(url=next_url, decode=True)
                result = self.process_page(response)
                if result == 1:
                    return
                page += 1


class WebNewtypeScanner(MainScanner):
    
    PAGE_PREFIX = "https://webnewtype.com/"
    SEARCH_PREFIX = "https://webnewtype.com/news/nrsearch/"
    
    def __init__(self, keyword, base_folder, last_episode=None, first_episode=0, download_id=None):
        super().__init__(download_id)
        self.keyword = keyword
        self.base_folder = base_folder.replace("download/","") + "/" + EXTERNAL_FOLDER_WEBNEWTYPE
        self.last_episode = last_episode
        self.first_episode = first_episode

    @staticmethod
    def has_results(text):
        return len(text) > 0 and "<li>記事はありません</li>" not in text

    @staticmethod
    def has_next_page(text):
        return len(text) > 0 and '<img src="/img/pager_right.png"' in text and '<span class="pageNumber"><img src="/img/pager_right.png"' not in text

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
            regex = '第[０|１|２|３|４|５|６|７|８|９|0-9]+話'
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
            filepath = self.base_folder + "/" + episode + "_01.jpg"
            if not filepath.startswith("download/"):
                filepath = "download/" + filepath
            if os.path.isfile(filepath):
                return 1
            is_first_episode = False
            if self.first_episode != 0 and episode != 'last':
                if int(episode) < self.first_episode:
                    return 1
                elif int(episode) == self.first_episode:
                    is_first_episode = True
            split4 = split2[i].split('<a href="')
            if len(split4) < 2:
                continue
            url = split4[1].split('"')[0]
            article_id = self.get_article_id(url)
            if len(article_id) == 0:
                continue
            WebNewtypeDownload(article_id, self.base_folder, episode, download_id=self.download_id).run()
            if is_first_episode:
                return 1
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

    def __init__(self, keyword, base_folder, start_date, end_date, ignore_cache=False, download_id=None):
        super().__init__(download_id)
        self.keyword = keyword
        self.base_folder = base_folder + "/" + EXTERNAL_FOLDER_MOCANEWS
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
        regex = '第[０|１|２|３|４|５|６|７|８|９|0-9]+話'
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
                    MocaNewsDownload(article_id, self.base_folder.replace('download/', ''), episode,
                                     download_id=self.download_id).run()
            except:
                pass
            curr_date -= timedelta(days=1)

        self.write_cache(self.end_date)


class NatalieScanner(MainScanner):
    SEARCH_URL_TEMPLATE = 'https://natalie.mu/search?context=news&query=%s&g=comic&page=%s'
    ARTICLE_URL_TEMPLATE = 'https://natalie.mu/comic/news/%s'

    def __init__(self, keyword, base_folder, last_episode=None, suffix=None, download_id=None):
        super().__init__(download_id)
        self.keyword = keyword
        self.base_folder = base_folder.replace("download/","") + "/" + EXTERNAL_FOLDER_NATALIE
        self.last_episode = last_episode
        self.suffix = suffix

    @staticmethod
    def has_results(soup):
        if soup is None:
            return False
        empty_section = soup.find('div', class_='NA_section_empty')
        return empty_section is None

    @staticmethod
    def has_next_page(soup):
        if soup is None:
            return False
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
            result = MainScanner.convert_kanji_to_number(split1[1])
            if result is not None:
                return result
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
            a_tags = card.find_all('a')
            news_info = None
            for a_tag in a_tags:
                if a_tag.has_attr('href') and 'news' in a_tag['href']:
                    news_info = a_tag
                    break
            if news_info:
                url = news_info['href']
                article_id = self.get_article_id(url)
                if len(article_id) == 0:
                    continue
                card_title = news_info.find('p', class_='NA_card_title')
                if card_title is None or len(card_title.text) == 0:
                    continue
                news_title = card_title.text
                suffix = self.suffix
                if suffix is None:
                    suffix = '話'

                regex = '第[０|１|２|３|４|５|６|７|８|９|十|一|二|三|四|五|六|七|八|九|0-9]+' + suffix
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
                filepath = self.base_folder + "/" + episode + "_01.jpg"
                if not filepath.startswith("download/"):
                    filepath = "download/" + filepath
                if os.path.isfile(filepath):
                    return 1

                image_title = None
                try:
                    image_title = '第' + str(int(episode)) + suffix
                except:
                    pass
                NatalieDownload(article_id, self.base_folder, episode, title=image_title,
                                download_id=self.download_id).run()
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


class EeoMediaScanner(MainScanner):
    PAGE_PREFIX = 'https://eeo.today/media/'
    SEARCH_PREFIX = PAGE_PREFIX + '?s='

    def __init__(self, keywords, base_folder, prefix='第', suffix='話',
                 last_episode=None, first_episode=0, download_id=None):
        super().__init__(download_id)
        if isinstance(keywords, str):
            self.keywords = [keywords]
        elif isinstance(keywords, list):
            self.keywords = keywords
        else:
            raise Exception('Unexpected type for keywords')
        self.base_folder = base_folder.replace("download/", "") + "/" + EXTERNAL_FOLDER_EEOMEDIA

        if prefix is None or len(prefix) == 0:
            raise Exception('Prefix is required.')
        self.prefix = prefix

        if suffix is None or len(suffix) == 0:
            raise Exception('Suffix is required.')
        self.suffix = suffix
        self.first_episode = first_episode
        self.last_episode = last_episode

    def run(self):
        if self.last_episode:
            # Stop processing if the last episode has already been downloaded
            if self.is_image_exists(str(self.last_episode).zfill(2) + '_01', self.base_folder) or \
                    self.is_image_exists('last_01', self.base_folder):
                return

        first_page_url = self.SEARCH_PREFIX + '+'.join(self.keywords)
        try:
            soup = self.get_soup(first_page_url)
            a_tags = soup.select('.article_panel_article_list a.article_title[href]')
            for a_tag in a_tags:
                title = a_tag.text
                prefix_index = title.find(self.prefix)
                suffix_index = title.find(self.suffix)
                if prefix_index == -1 or suffix_index == -1 or prefix_index >= suffix_index:
                    continue
                try:
                    episode = int(title[prefix_index + 1:suffix_index])
                except:
                    try:
                        episode = self.convert_kanji_to_number(title[prefix_index + 1:suffix_index])
                        if episode is None:
                            continue
                    except:
                        continue
                if episode < self.first_episode or (self.last_episode is not None and episode > self.last_episode):
                    continue
                article_id = a_tag['href'][len(self.PAGE_PREFIX):]
                EeoMediaDownload(article_id, self.base_folder, episode, self.download_id).run()
        except:
            return
