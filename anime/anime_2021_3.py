import os
import anime.constants as constants
from anime.main_download import MainDownload
from datetime import datetime
from scan import AniverseMagazineScanner, MocaNewsScanner, WebNewtypeScanner


# Bokutachi no Remake http://bokurema.com/ #ぼくリメ #bokurema @bokurema_anime
# Cheat Kusushi no Slow Life: Isekai ni Tsukurou Drugstore https://www.cheat-kusushi.jp/ #チート薬師 #スローライフ @cheat_kusushi
# Genjitsu Shugi Yuusha no Oukoku Saikenki https://genkoku-anime.com/ #現国アニメ @genkoku_info
# Kobayashi-san Chi no Maid Dragon S https://maidragon.jp/2nd/ #maidragon @maidragon_anime
# Meikyuu Black Company https://meikyubc-anime.com/ #迷宮ブラックカンパニー @meikyubc_anime
# Otome Game https://hamehura-anime.com/story/ #はめふら #hamehura @hamehura
# Peach Boy Riverside https://peachboyriverside.com/ #ピーチボーイリバーサイド @peachboy_anime
# Sekai Saikou no Ansatsusha, Isekai Kizoku ni Tensei suru https://ansatsu-kizoku.jp/ #暗殺貴族 @ansatsu_kizoku
# Shin no Nakama ja Nai to Yuusha no Party wo Oidasareta node, Henkyou de Slow Life suru Koto ni Shimashita https://shinnonakama.com/ #真の仲間 @shinnonakama_tv
# Shiroi Suna no Aquatope https://aquatope-anime.com/ #白い砂のアクアトープ @aquatope_anime
# Tantei wa Mou, Shindeiru. https://tanmoshi-anime.jp/ #たんもし @tanteiwamou_


# Summer 2021 Anime
class Summer2021AnimeDownload(MainDownload):
    season = "2021-3"
    season_name = "Summer 2021"
    folder_name = '2021-3'

    def __init__(self):
        super().__init__()


# Bokutachi no Remake
class BokuremaDownload(Summer2021AnimeDownload):
    title = 'Bokutachi no Remake'
    keywords = [title, 'Bokurema', 'Remake our Life!']
    folder_name = 'bokurema'

    PAGE_PREFIX = "http://bokurema.com"

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
        news_url = self.PAGE_PREFIX + '/news/'
        stop = False
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            for page in range(1, 2, 1):
                page_url = news_url
                # if page > 1:
                #    page_url = news_url + '?p=' + str(page)
                soup = self.get_soup(page_url)
                divs = soup.select('div.p-news-headline')
                for div in divs:
                    tag_date = div.find('time')
                    tag_title = div.find('h1')
                    a_tag = div.find('a')
                    if tag_date and tag_title and a_tag and a_tag.has_attr('href'):
                        article_id = a_tag['href']
                        date = '20' + tag_date.text.strip()
                        title = tag_title.text.strip()
                        if news_obj and (news_obj['id'] == article_id or date < news_obj['date']):
                            stop = True
                            break
                        results.append(self.create_news_log_object(date, title, article_id))
                if stop:
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
        self.add_to_image_list('teaser', self.PAGE_PREFIX + '/assets/images/teaser_2/main_visual.png')
        self.add_to_image_list('kv1', self.PAGE_PREFIX + '/assets/images/index/top_keyvisual_01.png')
        self.add_to_image_list('kv1_2', self.PAGE_PREFIX + '/assets/images/uploads/2021/02/keyvisual.jpg')
        self.add_to_image_list('wakuwork_collaboration', self.PAGE_PREFIX + '/assets/images/uploads/2021/02/wakuwork_collaboration.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX + '/character/')
            lis = soup.find_all('li', 'p-character-list__item')
            for li in lis:
                label = li.find('label')
                if label and label.has_attr('class') and len(label['class']) > 0:
                    character_name = label['class'][0].replace('c-character-select-area--', '')
                    if len(character_name) > 0:
                        image_url = '%s/assets/images/character/character_visual_%s.png'\
                                    % (self.PAGE_PREFIX, character_name)
                        image_name = 'character_visual_%s' % character_name
                        self.add_to_image_list(image_name, image_url)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)
        self.download_image_list(folder)


# Cheat Kusushi no Slow Life: Isekai ni Tsukurou Drugstore
class CheatKusushiDownload(Summer2021AnimeDownload):
    title = 'Cheat Kusushi no Slow Life: Isekai ni Tsukurou Drugstore'
    keywords = [title, 'Cheat Pharmacist\'s Slow Life: Making a Drugstore in Another World']
    folder_name = 'cheat-kusushi'

    PAGE_PREFIX = 'https://www.cheat-kusushi.jp/'

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
        news_url = self.PAGE_PREFIX
        try:
            soup = self.get_soup(news_url, decode=True)
            divs = soup.select('div.news.bg-news')
            news_obj = self.get_last_news_log_object()
            results = []
            for div in divs:
                paras = div.select('p')
                if len(paras) == 2:
                    article_id = ''
                    date = self.format_news_date(paras[0].text.replace('年', '.')
                                                 .replace('月', '.').replace('日', '').strip())
                    if len(date) == 0:
                        continue
                    title = paras[1].text.strip()
                    if news_obj and (news_obj['title'] == title or date < news_obj['date']):
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
        self.add_to_image_list('teaser', 'https://www.cheat-kusushi.jp/img/top-main.png')
        self.add_to_image_list('kv1', 'https://cheat-kusushi.jp/assets/img/bg/top.png')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/EqTAkcgU8AAe39d?format=jpg&name=large')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            article = soup.find('article', id='js-scroll-to-CHARACTER')
            if article:
                containers = article.find_all('div', class_='container')
                for container in containers:
                    if len(container['class']) > 1:
                        continue
                    images = container.find_all('img')
                    for image in images:
                        if image.has_attr('src'):
                            image_url = self.PAGE_PREFIX + image['src']
                            image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                            self.add_to_image_list(image_name, image_url)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)
        self.download_image_list(folder)


# Genjitsu Shugi Yuusha no Oukoku Saikenki
class GenkokuDownload(Summer2021AnimeDownload):
    title = "Genjitsu Shugi Yuusha no Oukoku Saikenki"
    keywords = [title, "Genkoku"]
    folder_name = 'genkoku'

    PAGE_PREFIX = 'https://genkoku-anime.com/'

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
        self.add_to_image_list('teaser', 'https://genkoku-anime.com/teaser/images/mainimg.png')
        self.add_to_image_list(name='teaser_moca',
                               url='https://moca-news.net/article/20201104/2020110410000a_/image/001-i2casw.jpg',
                               is_mocanews=True)
        self.download_image_list(folder)

    def download_character(self):
        pass


# Kobayashi-san Chi no Maid Dragon S
class KobayashiMaidDragon2Download(Summer2021AnimeDownload):
    title = 'Kobayashi-san Chi no Maid Dragon S'
    keywords = [title, "Miss Kobayashi's Maid Dragon"]
    folder_name = 'maidragon2'

    PAGE_PREFIX = 'https://maidragon.jp/2nd/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index', diff=2)

    def download_news(self):
        prefix = 'https://maidragon.jp'
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
                articles = soup.select('article.c-news-item')
                for article in articles:
                    tag_date = article.find('span', class_='c-news-item__date')
                    tag_title = article.find('span', class_='c-news-item__title')
                    a_tag = article.find('a')
                    if tag_date and tag_title and a_tag and a_tag.has_attr('href'):
                        article_id = prefix + a_tag['href']
                        date = self.format_news_date(tag_date.text.strip())
                        if len(date) == 0:
                            continue
                        title = tag_title.text.strip()
                        if date.startswith('2019') or (news_obj and
                                                       (news_obj['id'] == article_id or date < news_obj['date'])):
                            stop = True
                            break
                        results.append(self.create_news_log_object(date, title, article_id))
                if stop:
                    break
                pagination_lis = soup.select('ul.page-numbers li a.next.page-numbers')
                if len(pagination_lis) == 0:
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
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/EfEVvJEUwAI6LmD?format=jpg&name=large')
        self.add_to_image_list('teaser_covid', 'https://pbs.twimg.com/media/EfEVvJEUwAI6LmD?format=jpg&name=large')
        self.add_to_image_list('newyear_2021', 'https://pbs.twimg.com/media/EqkvG-lUcAInMkK?format=jpg&name=4096x4096')
        self.add_to_image_list('kv1_1', 'https://pbs.twimg.com/media/Ervaz89VEAkqjT-?format=jpg&name=900x900')
        self.add_to_image_list('kv1_2', 'https://maidragon.jp/2nd/img/pre/visual_02.png')
        self.download_image_list(folder)


# Meikyuu Black Company
class MeikyuBCDownload(Summer2021AnimeDownload):
    title = 'Meikyuu Black Company'
    keywords = [title, "The Dungeon of Black Company"]
    folder_name = 'meikyubc'

    PAGE_PREFIX = 'https://meikyubc-anime.com/'

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
            dl = soup.select('#news dl')
            if len(dl) == 0:
                return
            news_obj = self.get_last_news_log_object()
            results = []
            dts = dl[0].select('dt')
            for dt in dts:
                dd = dt.find_next('dd')
                if dd:
                    article_id = ''
                    date = self.format_news_date(dt.text.strip().replace('\n', ''))
                    if len(date) == 0:
                        continue
                    title = dd.text.strip().replace('\n', '')
                    if news_obj and (news_obj['title'] == title or date < news_obj['date']):
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
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/Es40z-1UYAAg7_x?format=jpg&name=medium')
        self.add_to_image_list('kv1', self.PAGE_PREFIX + '_image/keyvisual_2.png')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/ExX7gEEVIAcPU1v?format=jpg&name=medium')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + '_image/charaPop_%s.png'
        self.download_by_template(folder, template, 2)


# Otome Game no Hametsu Flag shika Nai Akuyaku Reijou ni Tensei shiteshimatta... X
class Hamehura2Download(Summer2021AnimeDownload):
    title = "Otome Game no Hametsu Flag shika Nai Akuyaku Reijou ni Tensei shiteshimatta... X"
    keywords = [title, "Hamehura", "Hamefura", "My Next Life as a Villainess: All Routes Lead to Doom!", "2nd"]
    folder_name = 'hamehura2'

    PAGE_PREFIX = 'https://hamehura-anime.com/'
    IMAGE_PREFIX = 'https://hamehura-anime.com/2nd/'

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
                articles = soup.find_all('article', class_='md-newsblock')
                for article in articles:
                    tag_date = article.find('dt')
                    tag_title = article.find('h3')
                    a_tag = article.find('a')
                    if tag_date and tag_title and a_tag and a_tag.has_attr('href'):
                        article_id = a_tag['href']
                        date = tag_date.text.strip()
                        title = tag_title.text.strip()
                        if news_obj and (news_obj['id'] == article_id or date < news_obj['date']):
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
        self.add_to_image_list('teaser', self.IMAGE_PREFIX + 'wp-content/uploads/2021/01/はめふらX_ティザービジュアル-1.jpg')
        self.add_to_image_list('kv1', self.IMAGE_PREFIX + 'wp-content/uploads/2021/03/第1弾キービジュアル.jpg')
        #self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/EsJL9ZQVkAEDktJ?format=jpg&name=large')
        self.download_image_list(folder)


# Peach Boy Riverside
class PeachBoyRiversideDownload(Summer2021AnimeDownload):
    title = 'Peach Boy Riverside'
    keywords = [title]
    folder_name = 'peachboyriverside'

    PAGE_PREFIX = 'https://peachboyriverside.com/'

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
        stop = False
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            for page in range(1, 2, 1):
                page_url = news_url
                if page > 1:
                    page_url = news_url + 'page/' + str(page) + '/'
                soup = self.get_soup(page_url, decode=True)
                lis = soup.select('ul.md--articleblock.ver__pages li')
                for li in lis:
                    tag_date = li.find('h3')
                    tag_title = li.find('h4', class_='ttl')
                    a_tag = li.find('a')
                    if tag_date and tag_title and a_tag and a_tag.has_attr('href'):
                        article_id = a_tag['href']
                        date = tag_date.text.strip()
                        title = tag_title.text.strip()
                        if news_obj and (news_obj['id'] == article_id or date < news_obj['date']):
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
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'wp/wp-content/themes/peachboyriverside_main/_assets/images/top/fv/fv_pc.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        image_name_template = 'char_main_%s@2x'
        url_template = self.PAGE_PREFIX + 'wp/wp-content/themes/peachboyriverside_main/_assets/images/pages/char/main/'\
            + image_name_template + '.png'
        try:
            for i in range(1, 100, 1):
                image_name = image_name_template % str(i).zfill(3)
                if self.is_image_exists(image_name, folder):
                    continue
                url = url_template % str(i).zfill(3)
                result = self.download_image(url, folder + '/' + image_name)
                if result == -1:
                    break
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)


# Sekai Saikou no Ansatsusha, Isekai Kizoku ni Tensei suru
class AnsatsuKizokuDownload(Summer2021AnimeDownload):
    title = 'Sekai Saikou no Ansatsusha, Isekai Kizoku ni Tensei suru'
    keywords = [title, "The world's best assassin, To reincarnate in a different world aristocrat"]
    folder_name = 'ansatsu-kizoku'

    PAGE_PREFIX = 'https://ansatsu-kizoku.jp/'

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
            lis = soup.select('ul.list li')
            news_obj = self.get_last_news_log_object()
            results = []
            for li in lis:
                tag_date = li.find('p', class_='date')
                tag_title = li.find('div', class_='title')
                a_tag = li.find('a')
                if tag_date and tag_title and a_tag and a_tag.has_attr('href'):
                    article_id = news_url + a_tag['href']
                    date = tag_date.text.strip().replace('-', '.')
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
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/Ev27c7bUUAIM_47?format=jpg&name=medium')
        self.download_image_list(folder)


# Shin no Nakama ja Nai to Yuusha no Party wo Oidasareta node, Henkyou de Slow Life suru Koto ni Shimashita
class ShinnoNakamaDownload(Summer2021AnimeDownload):
    title = 'Shin no Nakama ja Nai to Yuusha no Party wo Oidasareta node, Henkyou de Slow Life suru Koto ni Shimashita'
    keywords = [title, 'Shinnonakama', "Banished From The Heroes' Party"]
    folder_name = 'shinnonakama'

    PAGE_PREFIX = 'https://shinnonakama.com/'

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
            lis = soup.select('ul.newsListsWrap li')
            news_obj = self.get_last_news_log_object()
            results = []
            for li in lis:
                tag_date = li.find('p', class_='update_time')
                tag_title = li.find('p', class_='update_ttl')
                a_tag = li.find('a')
                if tag_date and tag_title and a_tag and a_tag.has_attr('href'):
                    article_id = news_url + a_tag['href'].replace('./', '')
                    date = tag_date.text.strip()
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
        self.image_list = []
        self.add_to_image_list('teaser', 'https://ogre.natalie.mu/media/news/comic/2021/0120/shin_no_nakama_teaser.jpg')
        self.download_image_list(folder)


# Shiroi Suna no Aquatobe
class AquatopeDownload(Summer2021AnimeDownload):
    title = 'Shiroi Suna no Aquatope'
    keywords = [title, 'Aquatope of White Sand']
    folder_name = 'aquatope'

    PAGE_PREFIX = 'https://aquatope-anime.com/'

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
        stop = False
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            for page in range(1, 2, 1):
                page_url = news_url
                if page > 1:
                    page_url = news_url + 'page/' + str(page) + '/'
                soup = self.get_soup(page_url, decode=True)
                articles = soup.select('article.news--lineup--block')
                for article in articles:
                    tag_date = article.find('dt')
                    tag_title = article.find('h3')
                    a_tag = article.find('a')
                    if tag_date and tag_title and a_tag and a_tag.has_attr('href'):
                        article_id = a_tag['href']
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
        self.add_to_image_list('teaser_tw', 'https://pbs.twimg.com/media/ErwuT7rVQAISak1?format=jpg&name=large')
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'wp/wp-content/themes/aquatope-teaser/_assets/images/kv/kv_pc@2x.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            articles = soup.find_all('article', class_='char--slider--block')
            for article in articles:
                pictures = article.find_all('picture')
                for picture in pictures:
                    source = picture.find('source')
                    if source and source.has_attr('srcset'):
                        try:
                            image_url = source['srcset'].split(',')[-1].split(' ')[0]
                            image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                            self.add_to_image_list(image_name, image_url)
                        except:
                            continue
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)
        self.download_image_list(folder)


# Tantei wa Mou, Shindeiru.
class TanmoshiDownload(Summer2021AnimeDownload):
    title = "Tantei wa Mou, Shindeiru."
    keywords = [title, "Tanmoshi", "The Detective Is Already Dead"]
    folder_name = 'tanmoshi'

    PAGE_PREFIX = 'https://tanmoshi-anime.jp/'

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
        news_url = self.PAGE_PREFIX + 'news/'
        stop = False
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            page_url = news_url
            for page in range(1, 100, 1):
                soup = self.get_soup(page_url, decode=True)
                list_div = soup.find('div', id='list_01')
                if not list_div:
                    continue
                trs = list_div.find_all('tr')
                for tr in trs:
                    tag_date = tr.find('td', class_='day')
                    tag_title = tr.find('div', class_='title')
                    a_tag = tr.find('a')
                    if tag_date and tag_title:
                        article_id = ''
                        if a_tag and a_tag.has_attr('href'):
                            article_id = self.PAGE_PREFIX + a_tag['href'].replace('../', '')
                        date = tag_date.text.replace('/', '.')
                        title = tag_title.text.strip()
                        if news_obj and ((news_obj['id'] == article_id and news_obj['title'] == title)
                                         or date < news_obj['date']):
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
        self.add_to_image_list('kv1', 'https://pbs.twimg.com/media/EsCTT1KXAAUGy6V?format=jpg&name=4096x4096')
        self.add_to_image_list('kv2', 'https://pbs.twimg.com/media/Eug1UGwUYAcgxON?format=jpg&name=4096x4096')
        self.add_to_image_list('kv3', 'https://pbs.twimg.com/media/Ew13JI0UYAMwHm6?format=jpg&name=4096x4096')
        template = self.PAGE_PREFIX + 'core_sys/images/main/tz/%s.png'
        for name in ['umbouzu', 'mugiko', 'poni', 'moyashi']:
            image_name = 'illust_' + name
            self.add_to_image_list(image_name, template % image_name)
        self.download_image_list(folder)

        for i in range(1, 11, 1):
            file_name = 'kv' + str(i)
            if self.is_image_exists(file_name, folder):
                continue
            if i == 1:
                image_url = template % 'kv'
            else:
                image_url = template % ('kv' + str(i))
            if self.is_valid_url(image_url, is_image=True):
                print('URL exists: ' + image_url)
            else:
                break

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            wraps = soup.find_all('div', class_='charListWrap')
            for wrap in wraps:
                images = wrap.find_all('img')
                for image in images:
                    if image.has_attr('src'):
                        image_url = self.PAGE_PREFIX + image['src']
                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                        self.add_to_image_list(image_name, image_url)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)
        self.download_image_list(folder)

    def download_media(self):
        folder = self.create_media_directory()
        template = self.PAGE_PREFIX + 'core_sys/images/main/cont/special/audio/%s.mp3'
        for i in ('01_kimizuka', '02_siesta', '03_nagisa', '04_yui', '05_charlotte'):
            url = template % i
            self.download_content(url, folder + '/' + i + '.mp3')
