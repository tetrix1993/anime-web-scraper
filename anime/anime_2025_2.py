from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate4
from datetime import datetime, timedelta
from requests.exceptions import HTTPError
from scan import AniverseMagazineScanner
from bs4 import BeautifulSoup
import json
import os
import requests
from anime.constants import HTTP_HEADER_USER_AGENT
from ast import literal_eval


# Spring 2025 Anime
class Spring2025AnimeDownload(MainDownload):
    season = "2025-2"
    season_name = "Spring 2025"
    folder_name = '2025-2'

    def __init__(self):
        super().__init__()


# Aharen-san wa Hakarenai Season 2
class Aharensan2Download(Spring2025AnimeDownload, NewsTemplate):
    title = 'Aharen-san wa Hakarenai Season 2'
    keywords = [title]
    website = 'https://aharen-pr.com/'
    twitter = 'aharen_pr'
    hashtags = '阿波連さん'
    folder_name = 'aharensan2'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            styles = soup.select('style[type="text/css"]')
            self.image_list = []
            for style in styles:
                if '#js-epwrap[data-ep="1"]' not in style.text:
                    continue
                s = style.text.split('}')
                for s2 in s:
                    if '#js-epwrap[data-ep="' in s2:
                        s3 = s2.split('#js-epwrap[data-ep="')
                        for t in s3:
                            if '#js-ep-thumb' not in t:
                                continue
                            try:
                                episode = str(int(t.split('"')[0])).zfill(2)
                                img_num = str(int(t.split('#js-ep-thumb')[1].split('{')[0].strip()))
                                image_name = episode + '_' + img_num
                            except:
                                continue
                            if self.is_image_exists(image_name):
                                continue
                            if 'url(' in t and ');' in t:
                                start_idx = t.find('url(') + 4
                                end_idx = t.find(');')
                                if start_idx < end_idx:
                                    image_url = t[start_idx : end_idx]
                                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.md-li__news',
                                    date_select='time', title_select='.ttl', id_select='a',
                                    next_page_select='.pagination li', next_page_eval_index_class='is__current',
                                    next_page_eval_index=-1)

    def download_episode_preview_guess(self, print_invalid=False, download_valid=True):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_' + str(self.IMAGES_PER_EPISODE)):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + '2ndwp/wp-content/uploads/%s/%s/%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        valid_urls = []
        for j in range(self.IMAGES_PER_EPISODE):
            k = 0
            while k < 20:
                if k == 0:
                    append = ''
                else:
                    append = '-' + str(k)
                image_folder = folder + '/' + year + '/' + month
                image_name = str(j + 1).zfill(2) + append
                if not self.is_image_exists(image_name, image_folder):
                    image_url = template % (year, month, image_name)
                    if self.is_valid_url(image_url, is_image=True):
                        print('VALID - ' + image_url)
                        is_successful = True
                        valid_urls.append({'name': image_name, 'url': image_url, 'folder': image_folder})
                    else:
                        if print_invalid:
                            print('INVALID - ' + image_url)
                        break
                k += 1
        if download_valid and len(valid_urls) > 0:
            for valid_url in valid_urls:
                image_name = valid_url['name']
                image_folder = valid_url['folder']
                if not os.path.exists(image_folder):
                    os.makedirs(image_folder)
                self.download_image(valid_url['url'], image_folder + '/' + image_name, to_jpg=True)
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful


# Aru Majo ga Shinu Made
class ArumajoDownload(Spring2025AnimeDownload, NewsTemplate2):
    title = 'Aru Majo ga Shinu Made'
    keywords = [title]
    website = 'https://arumajo-anime.com/'
    twitter = 'arumajo_anime'
    hashtags = 'ある魔女が死ぬまで'
    folder_name = 'arumajo'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_external()
        self.download_episode_preview_guess()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/01.html')
            stories = soup.select('table[summary="List_Type01"] a[href]')
            for story in stories:
                story_url = self.PAGE_PREFIX + story['href'].replace('../', '')
                try:
                    episode = str(int(story.text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if episode == '01':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(story_url)
                if ep_soup is not None:
                    images = ep_soup.select('.ph img[src]')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = self.PAGE_PREFIX + images[i]['src'].split('?')[0]
                        image_url = self.remove_string(image_url, ['../', 'sn_'])
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url, to_jpg=True)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX)

    def download_episode_preview_external(self):
        keywords = ['ある魔女が死ぬまで']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20250328', download_id=self.download_id).run()

    def download_episode_preview_guess(self, print_url=False):
        self.download_guess_core_sys(self.PAGE_PREFIX, self.FINAL_EPISODE, self.IMAGES_PER_EPISODE, 18, 45, 56, 6, 6,
                                     print_url)


# Ballpark de Tsukamaete!]
class BallparkDownload(Spring2025AnimeDownload, NewsTemplate):
    title = 'Ballpark de Tsukamaete!'
    keywords = [title, 'The Catcher in the Ballpark!']
    website = 'https://anime-ballpark.com/'
    twitter = 'ballpark_PR'
    hashtags = 'アニメボルパ'
    folder_name = 'ballpark'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'dist/img/story/ep%s/img%s.jpg'
        try:
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    prev_name = str(i).zfill(2) + '_' + str(j + 1)
                    if (i > 0 and j == 0 and self.is_content_length_same_as_existing(image_url, prev_name))\
                            or self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.c-Post__listItem',
                                    date_select='.c-Post__date', title_select='.c-Post__textHover', id_select='a')


# Chotto dake Ai ga Omoi Dark Elf ga Isekai kara Oikaketekita
class AiomoDarkElfDownload(Spring2025AnimeDownload, NewsTemplate):
    title = 'Chotto dake Ai ga Omoi Dark Elf ga Isekai kara Oikaketekita'
    keywords = [title, 'Yandere Dark Elf: She Chased Me All the Way From Another World!']
    website = 'https://aiomodarkelf.deregula.com/'
    twitter = 'aiomodarkelf'
    hashtags = '愛重ダークエルフ'
    folder_name = 'aiomodarkelf'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            eps = soup.select('.contents_head_story_btn[data-num]')
            lis = soup.select('#js_story>li')
            for ep in eps:
                episode = ''
                add_enabled = False
                for i in ep.text:
                    if i.isnumeric():
                        episode += i
                        add_enabled = True
                    elif add_enabled:
                        break
                if len(episode) == 0:
                    continue
                episode = episode.zfill(2)
                if self.is_image_exists(episode + '_1'):
                    continue
                try:
                    data_num = int(ep['data-num'])
                except:
                    continue
                if data_num < 0 or len(lis) < data_num + 1:
                    continue
                li = lis[data_num]
                images = li.select('.story_body_thumb a[data-imgload]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = self.PAGE_PREFIX + images[i]['data-imgload'][1:]
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.l_newslist a',
                                    date_select='.newslist_date', title_select='.newslist_ttl', id_select=None,
                                    next_page_select='.pagination', next_page_eval_index_compare_page=True,
                                    next_page_eval_index=-1)

    def download_episode_preview_guess(self, print_invalid=False, download_valid=True):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_' + str(self.IMAGES_PER_EPISODE)):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + '2ndwp/wp-content/uploads/%s/%s/%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        valid_urls = []
        for j in range(self.IMAGES_PER_EPISODE):
            k = 0
            while k < 20:
                if k == 0:
                    append = ''
                else:
                    append = '-' + str(k)
                image_folder = folder + '/' + year + '/' + month
                image_name = str(j + 1).zfill(2) + append
                if not self.is_image_exists(image_name, image_folder):
                    image_url = template % (year, month, image_name)
                    if self.is_valid_url(image_url, is_image=True):
                        print('VALID - ' + image_url)
                        is_successful = True
                        valid_urls.append({'name': image_name, 'url': image_url, 'folder': image_folder})
                    else:
                        if print_invalid:
                            print('INVALID - ' + image_url)
                        break
                k += 1
        if download_valid and len(valid_urls) > 0:
            for valid_url in valid_urls:
                image_name = valid_url['name']
                image_folder = valid_url['folder']
                if not os.path.exists(image_folder):
                    os.makedirs(image_folder)
                self.download_image(valid_url['url'], image_folder + '/' + image_name, to_jpg=True)
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful


# Danjo no Yuujou wa Seiritsu suru? (Iya, Shinai!!)
class DanjoruDownload(Spring2025AnimeDownload, NewsTemplate):
    title = 'Danjo no Yuujou wa Seiritsu suru? (Iya, Shinai!!)'
    keywords = [title, 'danjoru']
    website = 'https://www.danjoru.com/'
    twitter = 'danjoru_'
    hashtags = 'だんじょる'
    folder_name = 'danjoru'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 5

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'dist/img/story/ep%s/img%s.webp'
        try:
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news_item', date_select='.year',
                                    title_select='.ttl', id_select='a')


# Gorilla no Kami kara Kago sareta Reijou wa Ouritsu Kishidan de Kawaigarareru
class GorillaLadyDownload(Spring2025AnimeDownload, NewsTemplate2):
    title = 'Gorilla no Kami kara Kago sareta Reijou wa Ouritsu Kishidan de Kawaigarareru'
    keywords = [title]
    website = 'https://gorillalady-anime.com/'
    twitter = 'gorilla_bless'
    hashtags = 'ゴリラの加護令嬢'
    folder_name = 'gorillalady'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/01.html')
            stories = soup.select('table[summary="List_Type01"] a[href]')
            for story in stories:
                story_url = self.PAGE_PREFIX + story['href'].replace('../', '')
                try:
                    episode = str(int(story.text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if episode == '01':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(story_url)
                if ep_soup is not None:
                    images = ep_soup.select('.ph img[src]')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = self.PAGE_PREFIX + images[i]['src'].split('?')[0]
                        image_url = self.remove_string(image_url, ['../', 'sn_'])
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url, to_jpg=True)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX)


# Haite Kudasai, Takamine-san
class TakaminesanDownload(Spring2025AnimeDownload, NewsTemplate2):
    title = 'Haite Kudasai, Takamine-san'
    keywords = [title, 'Please Put Them On, Takamine-san']
    website = 'https://takaminesan.com/'
    twitter = 'takamine_anime'
    hashtags = '鷹峰さん'
    folder_name = 'takaminesan'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_external()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/01.html')
            stories = soup.select('table[summary="List_Type01"] a[href]')
            for story in stories:
                story_url = self.PAGE_PREFIX + story['href'].replace('../', '')
                try:
                    episode = str(int(story.text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if episode == '01':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(story_url)
                if ep_soup is not None:
                    images = ep_soup.select('.ph img[src]')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = self.PAGE_PREFIX + images[i]['src'].split('?')[0]
                        image_url = self.remove_string(image_url, ['../', 'sn_'])
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url, to_jpg=True)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX)

    def download_episode_preview_external(self):
        keywords = ['履いてください、鷹峰さん']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20250328', download_id=self.download_id).run()


# Hibi wa Sugiredo Meshi Umashi
class HibimeshiDownload(Spring2025AnimeDownload, NewsTemplate):
    title = 'Hibi wa Sugiredo Meshi Umashi'
    keywords = [title, 'Food for the Soul']
    website = 'https://hibimeshi.com/'
    twitter = 'hibimeshi_anime'
    hashtags = 'ひびめし'
    folder_name = 'hibimeshi'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        prefix = self.PAGE_PREFIX + 'story/'
        try:
            soup = self.get_soup(prefix)
            stories = soup.select('.tab_list li')
            for story in stories:
                try:
                    episode = ''
                    ep_num = story.select('p')[0].text
                    for a in ep_num:
                        if a.isnumeric():
                            episode += a
                    if len(episode) == 0:
                        continue
                    episode = str(int(episode)).zfill(2)
                except:
                    continue
                if 'is-current' in story['class']:
                    ep_soup = soup
                else:
                    try:
                        ep_soup = self.get_soup(prefix + story.select('a[href]')[0]['href'].replace('./', ''))
                    except:
                        continue
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('ul.swiper-wrapper img[src]')
                for i in range(len(images)):
                    image_url = prefix + images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.p-news__list-item',
                                    date_select='.p-news_article__date', title_select='.p-news_article__title',
                                    id_select='a', a_tag_start_text_to_remove='/', a_tag_prefix=self.PAGE_PREFIX,
                                    next_page_select='.c-pagination__list-item', next_page_eval_index=-1,
                                    next_page_eval_index_class='is-current')


# Isshun de Chiryou shiteita noni Yakutatazu to Tsuihou sareta Tensai Chiyushi, Yami Healer toshite Tanoshiku Ikiru
class YamiHealerDownload(Spring2025AnimeDownload, NewsTemplate):
    title = 'Isshun de Chiryou shiteita noni Yakutatazu to Tsuihou sareta Tensai Chiyushi, Yami Healer toshite Tanoshiku Ikiru'
    keywords = [title, "The Brilliant Healer's New Life in the Shadows", 'yamihealer']
    website = 'https://sh-anime.shochiku.co.jp/yamihealer/'
    twitter = 'yamihealer'
    hashtags = '闇ヒーラー'
    folder_name = 'yamihealer'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 8

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_external()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'assets/img/episode/%s/episode%s_%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, episode, str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.p-news__item',
                                    date_select='.p-news__item__date', title_select='.p-news__item__ttl',
                                    id_select=None, next_page_select='.c-pager__number', next_page_eval_index=-1,
                                    next_page_eval_index_class='is-active')

    def download_episode_preview_external(self):
        keywords = ['一瞬で治療していたのに役立たずと追放された天才治癒師、闇ヒーラーとして楽しく生きる']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20250407', download_id=self.download_id).run()


# Kakushite! Makina-san!!
class MakinasanDownload(Spring2025AnimeDownload, NewsTemplate):
    title = 'Kakushite! Makina-san!!'
    keywords = [title, "Makina-san's a Love Bot?!"]
    website = 'https://makinasan-anime.com/'
    twitter = 'makinasan_anime'
    hashtags = 'マキナさん'
    folder_name = 'makinasan'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_external()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story.html')
            eps = soup.select('label.tab_menu[for]')
            for ep in eps:
                episode = ''
                add_enabled = False
                for i in ep.text:
                    if i.isnumeric():
                        episode += i
                        add_enabled = True
                    elif add_enabled:
                        break
                if len(episode) == 0:
                    continue
                episode = episode.zfill(2)
                if self.is_image_exists(episode + '_1'):
                    continue
                lbl_for = ep['for']
                if len(lbl_for) == 0:
                    continue
                images = soup.select('#' + lbl_for + ' .gallery img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = self.PAGE_PREFIX + images[i]['src']
                    image_name = episode + '_' + str(i + 1).zfill(2)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-list__item', title_select='a',
                                    date_select='.news-list__item-data', id_select='a', news_prefix='news.html',
                                    a_tag_prefix=self.PAGE_PREFIX, date_separator='/')

    def download_episode_preview_external(self):
        keywords = ['かくして！ マキナさん']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20250403', download_id=self.download_id).run()


# Kanchigai no Atelier Meister
class KanchigaiAtelierDownload(Spring2025AnimeDownload, NewsTemplate4):
    title = 'Kanchigai no Atelier Meister'
    keywords = [title, 'The Unaware Atelier Master']
    website = 'https://kanchigai-pr.com/'
    twitter = 'kanchigai_pr'
    hashtags = '勘違いの工房主'
    folder_name = 'kanchigaiatelier'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_guess()

    def download_episode_preview(self):
        json_obj = None
        try:
            json_obj = self.get_json(self.PAGE_PREFIX + 'api/site-data/init')
            if 'stories' not in json_obj:
                return
            for story in json_obj['stories']:
                episode = story['episode'].zfill(2)
                self.image_list = []
                for i in range(len(story['images'])):
                    image_name = episode + '_' + str(i + 1)
                    image_url = story['images'][i]['image_path']
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)
        return json_obj

    def download_news(self, json_obj=None):
        self.download_template_news(json_url=self.PAGE_PREFIX + 'api/site-data/init')

    def download_episode_preview_guess(self, print_url=False, print_invalid=False):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_1'):
            return
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wp/wp-content/uploads/%s/%s/kanchigai_ep%s-%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1') or self.is_image_exists(episode + '_1', folder):
                continue
            is_success = False
            for j in range(self.IMAGES_PER_EPISODE):
                image_name = episode + '_' + str(j + 1)
                image_url = template % (year, month, episode, str(j + 1))
                if print_url:
                    print(image_url)
                if self.is_valid_url(image_url, is_image=True):
                    print('VALID - ' + image_url)
                    self.download_image(image_url, folder + '/' + image_name, to_jpg=True)
                    is_successful = True
                    is_success = True
                elif print_invalid:
                    print('INVALID - ' + image_url)
                if not is_success:
                    break
            if not is_success:
                break
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful


# Kanpeki Sugite Kawaige ga Nai to Konyaku Haki sareta Seijo wa Ringoku ni Urareru
class KanpekiSeijoDownload(Spring2025AnimeDownload, NewsTemplate):
    title = 'Kanpeki Sugite Kawaige ga Nai to Konyaku Haki sareta Seijo wa Ringoku ni Urareru'
    keywords = [title, 'The Too-Perfect Saint: Tossed Aside by My Fiancé and Sold to Another Kingdom']
    website = 'https://kanpekiseijo-anime.com/'
    twitter = 'kanpekiseijo_pr'
    hashtags = '完璧聖女'
    folder_name = 'kanpekiseijo'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 10

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'wp-content/themes/kanpeki/dist/img/story/ep%s/img%s.webp'
        try:
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), str(j + 1))
                    image_name = episode + '_' + str(j + 1).zfill(2)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news_item',
                                    date_select='.date_inner', title_select='.ttl', id_select='a',
                                    next_page_select='.next.page-numbers',
                                    date_func=lambda x: x[0:4] + '.' + x[4:9])


# Katainaka no Ossan, Kensei ni Naru
class OssanKenseiDownload(Spring2025AnimeDownload, NewsTemplate2):
    title = 'Katainaka no Ossan, Kensei ni Naru'
    keywords = [title, 'From Old Country Bumpkin to Master Swordsman']
    website = 'https://ossan-kensei.com/'
    twitter = 'ossan_kensei'
    hashtags = 'おっさん剣聖'
    folder_name = 'ossankensei'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_external()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/01.html')
            stories = soup.select('table[summary="List_Type01"] a[href]')
            for story in stories:
                story_url = self.PAGE_PREFIX + story['href'].replace('../', '')
                try:
                    episode = str(int(story.text.replace('#', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if episode == '01':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(story_url)
                if ep_soup is not None:
                    images = ep_soup.select('.ph img[src]')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = self.PAGE_PREFIX + images[i]['src'].split('?')[0]
                        image_url = self.remove_string(image_url, ['../', 'sn_'])
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url, to_jpg=True)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX)

    def download_episode_preview_external(self):
        keywords = ['片田舎のおっさん、剣聖になる']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20250407', download_id=self.download_id).run()


# Mono
class MonoDownload(Spring2025AnimeDownload, NewsTemplate):
    title = 'Mono'
    keywords = [title]
    website = 'https://mono-weekend.photo/'
    twitter = 'mono_weekend'
    hashtags = 'mono'
    folder_name = 'mono'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        prefix = self.PAGE_PREFIX + 'story/'
        try:
            soup = self.get_soup(prefix)
            stories = soup.select('.storyNavList a[href]')
            for story in stories:
                try:
                    episode = str(int(story.text.replace('#', ''))).zfill(2)
                except:
                    continue
                if '--is-current' in story['class']:
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(prefix + story['href'])
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.storyImageList img[src]')
                for i in range(len(images)):
                    image_url = prefix + images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, paging_type=1, article_select='.newsList',
                                    date_select='.newsList__date', title_select='.newsList__title', id_select='a',
                                    a_tag_prefix=self.PAGE_PREFIX + 'news/', next_page_select='.pagination__next')


# Ninja to Koroshiya no Futarigurashi
class NinkoroDownload(Spring2025AnimeDownload, NewsTemplate2):
    title = 'Ninja to Koroshiya no Futarigurashi'
    keywords = [title]
    website = 'https://ninkoro.jp/'
    twitter = 'ninkoro_anime'
    hashtags = ['にんころ', 'ninkoro']
    folder_name = 'ninkoro'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/01.html', decode=True)
            stories = soup.select('table[summary="List_Type01"] a[href]')
            for story in stories:
                story_url = self.PAGE_PREFIX + story['href'].replace('../', '')
                try:
                    episode = str(self.convert_kanji_to_number(story.text.replace('第', '').replace('葉', ''))).zfill(2)
                    if episode is None:
                        continue
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if episode == '01':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(story_url)
                if ep_soup is not None:
                    images = ep_soup.select('.ph img[src]')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = self.PAGE_PREFIX + images[i]['src'].split('?')[0]
                        image_url = self.remove_string(image_url, ['../', 'sn_'])
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url, to_jpg=True)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX)


# Ore wa Seikan Kokka no Akutoku Ryoushu!
class SeikanKokkaDownload(Spring2025AnimeDownload, NewsTemplate):
    title = 'Ore wa Seikan Kokka no Akutoku Ryoushu!'
    keywords = [title, "I'm the Evil Lord of an Intergalactic Empire!"]
    website = 'https://seikankokka-anime.com/'
    twitter = 'akutoku_ryoushu'
    hashtags = '星間国家'
    folder_name = 'seikankokka'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/latest/')
            divs = soup.select('div.max-w-\\[880px\\]')
            for div in divs:
                h2 = div.select('h2')
                if len(h2) == 0:
                    continue
                episode = ''
                add_enabled = False
                for i in h2[0].text:
                    if i.isnumeric():
                        episode += i
                        add_enabled = True
                    elif add_enabled:
                        break
                if len(episode) == 0:
                    continue
                episode = str(episode).zfill(2)
                images = div.select('img[data-story-image][src]')
                self.image_list = []
                for j in range(len(images)):
                    image_url = self.PAGE_PREFIX + images[j]['src'][1:]
                    image_name = episode + '_' + str(j + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.border-newsBorder',
                                    date_select='a .absolute', title_select='.line-clamp-2',
                                    id_select='a', a_tag_start_text_to_remove='/', a_tag_prefix=self.PAGE_PREFIX,
                                    paging_type=2, next_page_select='a[href] .rotate-180')


# Saikyou no Ousama, Nidome no Jinsei wa Nani wo Suru?
class Saikyo2domeDownload(Spring2025AnimeDownload, NewsTemplate):
    title = 'Saikyou no Ousama, Nidome no Jinsei wa Nani wo Suru?'
    keywords = [title, "The Beginning After the End"]
    website = 'https://saikyo2dome-tbate.com/'
    twitter = 'saikyo2dome'
    hashtags = ['最強の王様', 'TBATE']
    folder_name = 'saikyo2dome'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        # self.download_news()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        prefix = 'https://firestore.googleapis.com/google.firestore.v1.Firestore/Listen/channel?database=projects%2Fsaikyo2dome-prod%2Fdatabases%2F(default)&'
        post_url = prefix + 'VER=8&RID=9822&CVER=22&X-HTTP-Session-Id=gsessionid&%24httpHeaders=X-Goog-Api-Client%3Agl-js%2F%20fire%2F8.0.0%0D%0AContent-Type%3Atext%2Fplain%0D%0A&zx=4dfvse3tiweq&t=1'
        payload = {'count': '1', 'ofs': '0',
                   'req0___data__': '{"database":"projects/saikyo2dome-prod/databases/(default)","addTarget":{"query":{"structuredQuery":{"from":[{"collectionId":"lists"}],"where":{"fieldFilter":{"field":{"fieldPath":"publication_date"},"op":"LESS_THAN_OR_EQUAL","value":{"timestampValue":"2025-03-15T15:31:14.271000000Z"}}},"orderBy":[{"field":{"fieldPath":"publication_date"},"direction":"DESCENDING"},{"field":{"fieldPath":"__name__"},"direction":"DESCENDING"}],"limit":1},"parent":"projects/saikyo2dome-prod/databases/(default)/documents/pages/news"},"targetId":2}}'}
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            news_prefix = self.PAGE_PREFIX + 'news/'

            # Firebase - first post to get gsessionid and SID
            r = requests.post(url=post_url, headers=HTTP_HEADER_USER_AGENT, data=payload)
            ssid = r.headers["X-HTTP-Session-Id"]
            sid = literal_eval(r.text[r.text.find('\n') + 1:])[0][1][1]

            # Get actual data - takes the longest time here
            get_url = prefix + f'gsessionid={ssid}&VER=8&RID=rpc&SID={sid}&CI=0&AID=0&TYPE=xmlhttp&zx=903hqape89t1&t=1'
            r2 = requests.get(get_url)

            # Process data to find the news segment
            c1 = r2.text[r2.text.find('\n') + 1:]
            art_idx = c1.find('"articles": {')
            c2 = c1[art_idx + 13:]
            val_idx = c2.find('"values": [')
            c3 = c2[val_idx + 10:]

            # Find index of the last closing "]" for the end of array
            track = 0
            last_index = -1
            for i in range(len(c3)):
                if c3[i] == '[':
                    track += 1
                elif c3[i] == ']':
                    track -= 1
                if track == 0:
                    last_index = i
                    break
            if last_index == -1:
                return
            content = c3[0:last_index + 1]

            # Finally process news data
            items = literal_eval(content)
            for item in items:
                fields = item['mapValue']['fields']
                date = fields['publication_date']['timestampValue'][0:10].replace('-', '.')
                title = fields['title']['stringValue']
                url = news_prefix + fields['id']['stringValue']
                if news_obj is not None and (news_obj['id'] == url or news_obj['title'] == title
                                             or date < news_obj['date']):
                    break
                results.append(self.create_news_log_object(date, title, url))
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            self.print_exception(e, 'News')


# Shiunji-ke no Kodomotachi
class ShinunjiDownload(Spring2025AnimeDownload):
    title = 'Shiunji-ke no Kodomotachi'
    keywords = [title, 'The Shiunji Family Children']
    website = 'https://shiunjifamily.com/'
    twitter = 'shiunji_anime'
    hashtags = ['紫雲寺家の子供たち', 'shiunjifamily']
    folder_name = 'shiunji'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 8

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'story/img/ep%s/%s_%s.jpg'
        try:
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, episode, str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            news_prefix = self.PAGE_PREFIX + 'news/'
            json_obj = self.get_json(news_prefix + 'newslist.json')
            for item in json_obj:
                if 'date' in item and 'uniqueId' in item and 'title' in item:
                    try:
                        date = item['date']
                    except:
                        continue
                    title = item['title']
                    unique_id = item['uniqueId']
                    if len(unique_id) == 0 and 'directLinkUrl' in item and len(item['directLinkUrl']) > 1:
                        url = self.PAGE_PREFIX + item['directLinkUrl'][1:]
                    else:
                        url = news_prefix + '?id=' + item['uniqueId']
                    if news_obj is not None and (news_obj['id'] == url or news_obj['title'] == title
                                                 or date < news_obj['date']):
                        break
                    results.append(self.create_news_log_object(date, title, url))
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            self.print_exception(e, 'News')


# Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita: Sono Ni
class Slime3002Download(Spring2025AnimeDownload, NewsTemplate):
    title = "Slime Taoshite 300-nen, Shiranai Uchi ni Level Max ni Nattemashita: Sono Ni"
    keywords = [title, "I've Been Killing Slimes for 300 Years and Maxed Out My Level", "Slime 300", "slime300", '2nd']
    website = 'https://slime300-anime.com/'
    twitter = 'slime300_PR'
    hashtags = 'スライム倒して300年'
    folder_name = 'slime300-2'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 5

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'assets/images/story/ep%s/img%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-list li',
                                    date_select='.date', title_select='p:nth-child(2)', id_select='a')


# Summer Pockets
class SamapokeDownload(Spring2025AnimeDownload, NewsTemplate):
    title = 'Summer Pockets'
    keywords = [title, 'samapoke']
    website = 'https://summerpockets-anime.jp/'
    twitter = 'samapoke_anime'
    hashtags = 'サマポケアニメ'
    folder_name = 'samapoke'

    PAGE_PREFIX = website
    FINAL_EPISODE = 24
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'wp_summer/wp-content/themes/summerpocket_thema/img/story/%s/%s.jpg'
        try:
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.News-cont2',
                                    date_select='.News-cont-date2', title_select='.News-cont-txt2', id_select='a')


# Witch Watch
class WitchWatchDownload(Spring2025AnimeDownload, NewsTemplate):
    title = "Witch Watch"
    keywords = [title]
    website = 'https://witchwatch-anime.com/'
    twitter = 'WITCHWATCHanime'
    hashtags = 'ウィッチウォッチ'
    folder_name = 'witchwatch'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            eps = soup.select('.story--nav a[href]')
            for ep in eps:
                try:
                    episode = str(ep.text).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                ep_soup = self.get_soup(ep['href'])
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.story--main__ss--slider img[src]')
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.md-li__topics', title_select='.ttl',
                                    date_select='time', id_select='a', news_prefix='topics')


# Your Forma
class YourFormaDownload(Spring2025AnimeDownload):
    title = 'Your Forma'
    keywords = [title]
    website = 'https://www.yourforma-anime.com/'
    twitter = 'yourforma'
    hashtags = ['ユア・フォルマ', 'your_forma']
    folder_name = 'yourforma'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self, print_http_error=False):
        api_url = 'https://www.news.yourforma-anime.com/wp-json/wp/v2/story?acf_format=standard&context=embed'
        try:
            objs = self.get_json(api_url)
            for obj in objs:
                if 'acf' in obj:
                    acf = obj['acf']
                    if 'story_num' in acf and 'story_imgs' in acf and isinstance(acf['story_imgs'], list):
                        try:
                            episode = ''
                            ep_num = acf['story_num']
                            for a in ep_num:
                                if a.isnumeric():
                                    episode += a
                            if len(episode) == 0:
                                continue
                            episode = str(int(episode)).zfill(2)
                        except:
                            continue
                        for i in range(len(acf['story_imgs'])):
                            image_obj = acf['story_imgs'][i]
                            if 'story_img' in image_obj and 'url' in image_obj['story_img']:
                                image_url = image_obj['story_img']['url']
                                image_name = episode + '_' + str(i + 1)
                                self.add_to_image_list(image_name, image_url, to_jpg=True)
                        self.download_image_list(self.base_folder)
        except HTTPError as e:
            if print_http_error:
                print(self.__class__.__name__ + ' - 403 Error when retrieving news API.')
        except Exception as e:
            self.print_exception(e)

    def download_news(self, print_http_error=False):
        news_url = self.PAGE_PREFIX + 'news/detail.html?id='
        api_url = 'https://www.news.yourforma-anime.com/wp-json/wp/v2/posts?acf_format=standard&per_page=10&page='
        try:
            page = 1
            page_url = api_url + str(page)
            json_obj = self.get_json(page_url)
            news_obj = self.get_last_news_log_object()
            results = []
            for item in json_obj:
                article_id = news_url + str(item['id'])
                date = item['date'][0:10].replace('-', '.')
                title = item['title']['rendered']
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
        except HTTPError as e:
            if print_http_error:
                print(self.__class__.__name__ + ' - 403 Error when retrieving news API.')
        except Exception as e:
            self.print_exception(e, 'News')


# Zatsu Tabi: That's Journey
class ZatsuTabiDownload(Spring2025AnimeDownload, NewsTemplate):
    title = "Zatsu Tabi: That's Journey"
    keywords = [title]
    website = 'https://zatsutabi.com/'
    twitter = 'zatsutabi_anime'
    hashtags = 'ざつ旅'
    folder_name = 'zatsutabi'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'assets/story/%s/%s.webp'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article', title_select='.entry-title',
                                    date_select='.entry-date', id_select=None, id_has_id=True, news_prefix='news.html',
                                    a_tag_prefix=self.PAGE_PREFIX + 'news.html#',
                                    date_func=lambda x: x.replace('年', '.').replace('月', '.').replace('日', ''))
