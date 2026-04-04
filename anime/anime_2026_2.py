from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate3, NewsTemplate4
from datetime import datetime, timedelta
from requests.exceptions import HTTPError
from scan import AniverseMagazineScanner
import os


# Spring 2026 Anime
class Spring2026AnimeDownload(MainDownload):
    season = "2026-2"
    season_name = "Spring 2026"
    folder_name = '2026-2'

    def __init__(self):
        super().__init__()


# Aishiteru Game wo Owarasetai
class AishiteruGameDownload(Spring2026AnimeDownload, NewsTemplate):
    title = 'Aishiteru Game wo Owarasetai'
    keywords = [title, 'I Want to End This Love Game']
    website = 'https://www.aishiteru-game.com/'
    twitter = 'aishiterugame'
    hashtags = '愛してるゲームを終わらせたい'
    folder_name = 'aishiterugame'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        pass

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.content-entry',
                                    title_select='.entry-title span', date_select='.entry-date span',
                                    id_select=None, id_has_id=True, news_prefix='news.html',
                                    a_tag_prefix=self.PAGE_PREFIX + 'news.html#')


# Class de 2-banme ni Kawaii Onnanoko to Tomodachi ni Natta
class KuranikaDownload(Spring2026AnimeDownload, NewsTemplate):
    title = 'Class de 2-banme ni Kawaii Onnanoko to Tomodachi ni Natta'
    keywords = [title, 'I Made Friends with the Second Prettiest Girl in My Class', 'kuranika']
    website = 'https://kuranika.asmik-ace.co.jp/'
    twitter = 'kuranika'
    hashtags = 'クラにか'
    folder_name = 'kuranika'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        pass

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.bl_posts_item', date_select='time',
                                    title_select='.bl_posts_txt', id_select='a', next_page_select='a.next.page-numbers',
                                    paging_type=3, paging_suffix='?page=%s', date_separator='/')


# Haibara-kun no Tsuyokute Seishun New Game
class HaibarakunDownload(Spring2026AnimeDownload, NewsTemplate):
    title = 'Haibara-kun no Tsuyokute Seishun New Game'
    keywords = [title, "Haibara's Teenage New Game+"]
    website = 'https://haibarakun-anime.com/'
    twitter = 'haibara_anime'
    hashtags = '灰原くんの強くて青春ニューゲーム'
    folder_name = 'haibarakun'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        pass

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.md-li__topics li',
                                    date_select='time', title_select='.info--postttl', id_select='a',
                                    news_prefix='topics/', date_separator='-')

    def download_episode_preview_guess(self, print_invalid=False, download_valid=True):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_' + str(self.IMAGES_PER_EPISODE)):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wp/wp-content/uploads/%s/%s/%s.jpg'
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


# Himekishi wa Barbaroi no Yome
class BaruyomeDownload(Spring2026AnimeDownload):
    title = 'Himekishi wa Barbaroi no Yome'
    keywords = [title, "The Warrior Princess and the Barbaric King"]
    website = 'https://himekishi-anime.com/'
    twitter = 'himekishi_anime'
    hashtags = ['バルよめ']
    folder_name = 'baruyome'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'images/story/%s/p_%s.jpg'
        try:
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1).zfill(3), str(j + 1).zfill(3))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self, print_http_error=False):
        try:
            json_obj = self.get_json(self.PAGE_PREFIX + 'news.json')
            news_obj = self.get_last_news_log_object()
            results = []
            for item in json_obj:
                article_id = self.PAGE_PREFIX + item['url']
                date = item['day']
                date_split = date.split('.')
                if len(date_split) != 3:
                    continue
                if len(date_split[1]) == 1:
                    date_split[1] = '0' + date_split[1]
                if len(date_split[2]) == 1:
                    date_split[2] = '0' + date_split[2]
                date = '.'.join(date_split)
                title = item['title']
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


# Honzuki no Gekokujou: Ryoushu no Youjo
class Honzuki4Download(Spring2026AnimeDownload, NewsTemplate):
    title = "Honzuki no Gekokujou: Ryoushu no Youjo"
    keywords = [title, "Ascendance of a Bookworm", '4th', 'Season 4']
    website = 'http://booklove-anime.jp/'
    twitter = 'anime_booklove'
    hashtags = '本好きの下剋上'
    folder_name = 'honzuki4'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            stories = self.get_json(self.PAGE_PREFIX + 'data/story.json')
            for story in stories:
                try:
                    episode_int = self.convert_kanji_to_number(story['data']['episode'])
                    episode = str(episode_int).zfill(2)
                except Exception:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if 'content_pic' not in story['data']:
                    continue
                images = story['data']['content_pic']
                self.image_list = []
                for i in range(len(images)):
                    if 'pic' not in images[i]:
                        continue
                    image_url = self.PAGE_PREFIX + images[i]['pic'][1:]
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)


# Ichijouma Mankitsugurashi!
class IchijyomaDownload(Spring2026AnimeDownload, NewsTemplate):
    title = 'Ichijouma Mankitsugurashi!'
    keywords = [title, "Ichijyoma Mankitsu Gurashi!"]
    website = 'https://ichijyoma-anime.com/'
    twitter = 'ichijyoma_anime'
    hashtags = ['まんきつ暮らし']
    folder_name = 'ichijyoma'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        pass

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-a',
                                    date_select='.news-div', title_select='.news-div2', id_select=None)


# Isekai Nonbiri Nouka 2
class NonbiriNouka2Download(Spring2026AnimeDownload, NewsTemplate):
    title = 'Isekai Nonbiri Nouka 2'
    keywords = [title, "jihanki", 'Farming Life in Another World Season 2']
    website = 'https://nonbiri-nouka2.com/'
    twitter = 'nonbiri_nouka'
    hashtags = ['のんびり農家']
    folder_name = 'nonbirinouka2'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 4

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/nonbiri-nouka2/assets/img/story/episode/ep%s_%s.jpg'
        try:
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_1'):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        news_url = 'https://up-info.news/jihanki-anime/3rd/'
        self.download_template_news(page_prefix=news_url, article_select='.modListNews li', title_select='h3',
                                    date_select='time', id_select='a', date_separator='/', news_prefix='')


# Jidou Hanbaiki ni Umarekawatta Ore wa Meikyuu wo Samayou S3
class Jihanki3Download(Spring2026AnimeDownload, NewsTemplate):
    title = 'Jidou Hanbaiki ni Umarekawatta Ore wa Meikyuu wo Samayou 3rd Season'
    keywords = [title, "jihanki", 'Reborn as a Vending Machine, I Now Wander the Dungeon']
    website = 'https://jihanki-anime.com/'
    twitter = 'jihanki_anime'
    hashtags = ['jihanki', '俺自販機']
    folder_name = 'jihanki3'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 5

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'assets/img/story/%s/story_%s_%s.jpg'
        try:
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
        news_url = 'https://up-info.news/jihanki-anime/3rd/'
        self.download_template_news(page_prefix=news_url, article_select='.modListNews li', title_select='h3',
                                    date_select='time', id_select='a', date_separator='/', news_prefix='')


# Jishou Akuyaku Reijou na Konyakusha no Kansatsu Kiroku.
class JishoAkuyakuDownload(Spring2026AnimeDownload, NewsTemplate):
    title = 'Jishou Akuyaku Reijou na Konyakusha no Kansatsu Kiroku.'
    keywords = [title, "An Observation Log of My Fiancée Who Calls Herself a Villainess"]
    website = 'https://jisho-akuyaku-anime.jp/'
    twitter = 'jisho_akuyakuPR'
    hashtags = ['自称悪役令嬢']
    folder_name = 'jishoakuyaku'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 5

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'assets/img/story/episode/ep%s/img%s.webp'
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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.bl_news__article_item',
                                    date_select='time', title_select='.bl_news__article_body', id_select='a',
                                    next_page_select='a.next.page-numbers', paging_type=3, paging_suffix='?page=%s')


# Kanan-sama wa Akumade Choroi
class KanachoroDownload(Spring2026AnimeDownload, NewsTemplate):
    title = 'Kanan-sama wa Akumade Choroi'
    keywords = [title, "Mistress Kanan is Devilishly Easy"]
    website = 'https://kanachoro-anime.com/'
    twitter = 'Kanan_Choroi'
    hashtags = ['カナチョロ', 'kanan_choroi']
    folder_name = 'kanachoro'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 4

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'images/story/img_%s_%s.jpg'
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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article',
                                    date_select='.news-date', title_select='h3', id_select=None, id_has_id=True,
                                    a_tag_prefix=self.PAGE_PREFIX + 'news.html#',
                                    date_func=lambda x: x[0:4] + '.' + x[5:])


# Kuroneko to Majo no Kyoushitsu
class NekomajoDownload(Spring2026AnimeDownload, NewsTemplate):
    title = 'Kuroneko to Majo no Kyoushitsu'
    keywords = [title, "The Classroom of a Black Cat and a Witch"]
    website = 'https://witch-classroom.com/'
    twitter = 'witch_classroom'
    hashtags = ['猫魔女', '黒猫と魔女の教室']
    folder_name = 'nekomajo'

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
            eps = soup.select('.episode')
            for ep in eps:
                try:
                    episode = str(int(ep.select('.episode__number .number')[0].text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                images = ep.select('.slide__image img.episode_image[src]')
                for i in range(len(images)):
                    image_url = self.clear_resize_in_url(images[i]['src'])
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.entry-title',
                                    date_select='.news__date', title_select='.news__text', id_select='a',
                                    next_page_select='.pagination .next')

    def download_episode_preview_guess(self, print_invalid=False, download_valid=True):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_' + str(self.IMAGES_PER_EPISODE)):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wp-content/uploads/%s/%s/episode%s_%s.webp'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        valid_urls = []
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            is_success = False
            for j in range(self.IMAGES_PER_EPISODE):
                image_url = template % (year, month, str(i + 1), str(j + 1).zfill(2))
                image_name = episode + '_' + str(j + 1)
                if self.is_valid_url(image_url, is_image=True):
                    print('VALID - ' + image_url)
                    is_successful = True
                    is_success = True
                    valid_urls.append({'name': image_name, 'url': image_url})
                else:
                    if print_invalid:
                        print('INVALID - ' + image_url)
                    break
            if not is_success:
                break
        if download_valid and len(valid_urls) > 0:
            for valid_url in valid_urls:
                image_name = valid_url['name']
                if not os.path.exists(folder):
                    os.makedirs(folder)
                self.download_image(valid_url['url'], folder + '/' + image_name, to_jpg=True)
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful


# Liar Game
class LiarGameDownload(Spring2026AnimeDownload, NewsTemplate):
    title = 'Liar Game'
    keywords = [title]
    website = 'https://www.liargame-anime.com/'
    twitter = 'liargame_anime'
    hashtags = ['ライアーゲーム', 'LiarGame']
    folder_name = 'liargame'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        pass

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.archive__item',
                                    date_select='.archive__item-date', title_select='.archive__item-title',
                                    id_select='a', next_page_select='.wp-pagenavi *',
                                    next_page_eval_index_class='current', next_page_eval_index=-1)


# Maid-san wa Taberu dake
class MeitabeDownload(Spring2026AnimeDownload, NewsTemplate):
    title = 'Maid-san wa Taberu dake'
    keywords = [title, "The Food Diary of Miss Maid"]
    website = 'https://meitabe-anime.com/'
    twitter = 'lovetoeat_maid'
    hashtags = ['メイ食べ']
    folder_name = 'meitabe'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 5

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'assets/img/story/ep%s/img%s.jpg'
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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.bl_posts_item',
                                    date_select='time', title_select='.bl_posts_txt', id_select='a',
                                    next_page_select='a.next.page-numbers', paging_type=3, paging_suffix='?page=%s')


# Mata Korosarete Shimatta no desu ne, Tantei-sama
class MatakoroDownload(Spring2026AnimeDownload, NewsTemplate):
    title = 'Mata Korosarete Shimatta no desu ne, Tantei-sama'
    keywords = [title, "Killed Again, Mr. Detective.", 'matakoro']
    website = 'https://www.tbs.co.jp/anime/matakoro/'
    twitter = 'matakoro_anime'
    hashtags = ['またころ']
    folder_name = 'matakoro'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'story/img/v%s_%s.jpg'
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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='#news-list>li',
                                    date_select='dt', title_select='dd', id_select='a',
                                    a_tag_prefix='https://www.tbs.co.jp')


# Nigashita Sakana wa Ookikatta ga Tsuriageta Sakana ga Ookisugita Ken
class NigetsuriDownload(Spring2026AnimeDownload, NewsTemplate):
    title = 'Nigashita Sakana wa Ookikatta ga Tsuriageta Sakana ga Ookisugita Ken'
    keywords = [title, "Always a Catch!", 'nigetsuri']
    website = 'https://nigetsuri-anime.com/'
    twitter = 'nigetsuri_anime'
    hashtags = ['逃げ釣り']
    folder_name = 'nigetsuri'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            story_url = self.PAGE_PREFIX + 'story/'
            soup = self.get_soup(story_url)
            stories = soup.select('ol.list a[href]')
            for story in stories:
                try:
                    episode = ''
                    ep_num = story.select('h2 span')[0].text
                    for a in reversed(ep_num):
                        if a.isnumeric():
                            episode = a + episode
                    if len(episode) == 0:
                        continue
                    episode = str(int(episode)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                ep_soup = self.get_soup(story_url + story['href'])
                if ep_soup is None:
                    continue
                images = ep_soup.select('.scene li img[src]')
                for i in range(len(images)):
                    image_url = self.PAGE_PREFIX + images[i]['src'].replace('../', '')
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news article',
                                    date_select='time', title_select='h2', id_select='a',
                                    a_tag_start_text_to_remove='./', a_tag_prefix=self.PAGE_PREFIX + 'news/')


# Otaku ni Yasashii Gal wa Inai!?
class OtagalDownload(Spring2026AnimeDownload, NewsTemplate):
    title = 'Otaku ni Yasashii Gal wa Inai!?'
    keywords = [title, "Gals Can't Be Kind to Otaku!?", 'otagal']
    website = 'https://otagal.jp/'
    twitter = 'OtaGal_official'
    hashtags = ['オタギャル']
    folder_name = 'otagal'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            stories = soup.select('.story-tab__box')
            for story in stories:
                try:
                    episode = ''
                    ep_num = story.select('.story-heading__episode')[0].text
                    for a in reversed(ep_num):
                        if a.isnumeric():
                            episode = a + episode
                    if len(episode) == 0:
                        continue
                    episode = str(int(episode)).zfill(2)
                except:
                    continue
                images = story.select('.swiper-main img[src]')
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news__list li',
                                    date_select='.home__news-date span:nth-child(2)', title_select='.home__news-text',
                                    id_select='a', next_page_select='.wp-pagenavi *',
                                    next_page_eval_index_class='current', next_page_eval_index=-1)


# Otonari no Tenshi-sama ni Itsunomanika Dame Ningen ni Sareteita Ken 2
class Tenshisama2Download(Spring2026AnimeDownload):
    title = "Otonari no Tenshi-sama ni Itsunomanika Dame Ningen ni Sareteita Ken 2"
    keywords = [title, "The Angel Next Door Spoils Me Rotten 2"]
    folder_name = 'tenshisama2'
    website = 'https://otonarino-tenshisama.jp/'
    twitter = 'tenshisama_PR'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 4

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/', impersonate=True)
            stories = soup.select('section.episode')
            for story in stories:
                if not story.has_attr('id') or not story['id'].startswith('ep') or not story['id'][2:].isnumeric():
                    continue
                ep_num = int(story['id'][2:])
                if ep_num < 13:
                    continue
                episode = str(ep_num - 12).zfill(2)
                if self.is_image_exists(episode + '_1'):
                    continue
                images = story.select('picture img[src]')
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_guess(self, print_invalid=False, download_valid=True):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_' + str(self.IMAGES_PER_EPISODE)):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wordpress/wp-content/uploads/%s/%s/story-episode%s-cut%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        valid_urls = []
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            is_success = False
            for j in range(self.IMAGES_PER_EPISODE):
                image_url = template % (year, month, str(i + 13), str(j + 1))
                image_name = episode + '_' + str(j + 1)
                if self.is_valid_url(image_url, is_image=True):
                    print('VALID - ' + image_url)
                    is_successful = True
                    is_success = True
                    valid_urls.append({'name': image_name, 'url': image_url})
                else:
                    if print_invalid:
                        print('INVALID - ' + image_url)
                    break
            if not is_success:
                break
        if download_valid and len(valid_urls) > 0:
            for valid_url in valid_urls:
                image_name = valid_url['name']
                if not os.path.exists(folder):
                    os.makedirs(folder)
                self.download_image(valid_url['url'], folder + '/' + image_name, to_jpg=True)
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful


# Re:Zero kara Hajimeru Isekai Seikatsu 4th Season
class ReZero4Download(Spring2026AnimeDownload):
    title = "Re:Zero kara Hajimeru Isekai Seikatsu 4th Season"
    keywords = [title, "rezero", "Re:Zero - Starting Life in Another World"]
    folder_name = 'rezero4'
    website = 'http://re-zero-anime.jp/tv/'
    twitter = 'Rezero_official'

    PAGE_PREFIX = website
    FIRST_EPISODE = 67
    FINAL_EPISODE = 85
    IMAGES_PER_EPISODE = 10

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'assets/episode/%s/%s.webp'
            stop = False
            for i in range(self.FIRST_EPISODE, self.FINAL_EPISODE + 1, 1):
                episode = str(i).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE).zfill(2)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, str(j + 1))
                    image_name = episode + '_' + str(j + 1).zfill(2)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)


# Replica datte, Koi wo Suru.
class ReplicoDownload(Spring2026AnimeDownload):
    title = 'Replica datte, Koi wo Suru.'
    keywords = [title, "Even a Replica Can Fall in Love", 'replico']
    website = 'https://replico.jp/'
    twitter = 'REPLICO_dengeki'
    hashtags = 'レプリコ'
    folder_name = 'replico'

    PAGE_PREFIX = website
    FINAL_EPISODE = 13
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'story/img/ep%s/ep%s_%s.jpg'
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
                if 'datetime' in item and 'uniqueId' in item and 'title' in item:
                    try:
                        date = item['datetime'].replace('-', '.')
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


# Saikyou no Shokugyou wa Yuusha demo Kenja demo Naku Kanteishi (Kari) Rashii desu yo?
class KanteishiKariDownload(Spring2026AnimeDownload, NewsTemplate):
    title = 'Saikyou no Shokugyou wa Yuusha demo Kenja demo Naku Kanteishi (Kari) Rashii desu yo?'
    keywords = [title, "The Strongest Job is Apparently Not a Hero or a Sage, but an Appraiser (Provisional)!"]
    website = 'https://kanteishikari-anime.com/'
    twitter = 'kanteishi_anime'
    hashtags = ['アニメ鑑定士仮']
    folder_name = 'kanteishikari'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 9

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'common/images/story/%s/%s.jpg'
        try:
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_1'):
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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news_list_item',
                                    title_select='.news_list_item_title', date_select='.news_list_item_date',
                                    id_select='a', a_tag_prefix=self.PAGE_PREFIX, a_tag_start_text_to_remove='./',
                                    date_func=lambda x: x[0:4] + '.' + x[4:6] + '.' + x[7:], news_prefix='')


# Tongari Boushi no Atelier
class TongariDownload(Spring2026AnimeDownload, NewsTemplate):
    title = 'Tongari Boushi no Atelier'
    keywords = [title, "Witch Hat Atelier"]
    website = 'https://tongari-anime.com/'
    twitter = 'tongari_anime'
    hashtags = ['とんがり帽子のアトリエ', 'WitchHatAtelier']
    folder_name = 'tongari'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        story_url = self.PAGE_PREFIX + 'story/'
        try:
            soup = self.get_soup(story_url)
            eps = soup.select('.p-story__list-item')
            for ep in eps:
                a_tag = ep.select('a[href]')
                if len(a_tag) == 0:
                    continue
                try:
                    ep_title = ep.select('.p-story_card__title')[0].text
                    ep_num = ''
                    append_num = False
                    for i in ep_title:
                        if not append_num and i.isnumeric():
                            append_num = True
                            ep_num = ep_num + i
                        elif append_num:
                            if i.isnumeric():
                                ep_num = ep_num + i
                            else:
                                break
                    if len(ep_num) == 0:
                        continue
                    episode = str(ep_num).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_01'):
                    continue
                ep_soup = self.get_soup(story_url + a_tag[0]['href'])
                if ep_soup is None:
                    continue
                images = ep_soup.select('.p-story_single__text img[src]')
                for j in range(len(images)):
                    image_url = images[j]['src']
                    image_name = episode + '_' + str(j + 1).zfill(2)
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.p-news__list-item',
                                    date_select='.p-news_data__date', title_select='.p-news_data__title',
                                    id_select='a', a_tag_prefix=self.PAGE_PREFIX, a_tag_start_text_to_remove='/',
                                    paging_type=1, next_page_select='.c-pagination__list li', next_page_eval_index=-1,
                                    next_page_eval_index_class='is-current')


# Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e 4th Season: 2-nensei-hen 1 Gakki
class Youzitsu4Download(Spring2026AnimeDownload, NewsTemplate):
    title = "Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e 4th Season: 2-nensei-hen 1 Gakki"
    keywords = ["Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e", "Youzitsu", "Youjitsu",
                "Classroom of the Elite"]
    website = 'http://you-zitsu.com/'
    twitter = 'youkosozitsu'
    hashtags = ['you_zitsu', 'よう実', 'ClassroomOfTheElite']
    folder_name = 'youzitsu4'

    PAGE_PREFIX = website
    FINAL_EPISODE = 16
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'assets/story/%s/%s.webp'
            stop = False
            for i in range(5, self.FINAL_EPISODE + 1, 1):
                episode = str(i).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_name = episode + '_' + str(j + 1)
                    image_url = template % (str(i), str(j + 1))
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)


# Yowayowa Sensei
class YowayowaSenseiDownload(Spring2026AnimeDownload, NewsTemplate):
    title = 'Yowayowa Sensei'
    keywords = [title, "Yowayowa Teacher"]
    website = 'https://www.yowayowasensei-anime.com/'
    twitter = 'yowayowa_anime'
    hashtags = ['よわよわ先生']
    folder_name = 'yowayowasensei'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        pass

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.content-entry',
                                    title_select='.entry-title span', date_select='.entry-date span',
                                    id_select=None, id_has_id=True, news_prefix='news.html',
                                    a_tag_prefix=self.PAGE_PREFIX + 'news.html#')
