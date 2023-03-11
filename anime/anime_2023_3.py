from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2


# Higeki no Genkyou to Naru Saikyou Gedou Last Boss Joou wa Tami no Tame ni Tsukushimasu. https://lastame.com/ #ラス為 @lastame_pr
# Kanojo, Okarishimasu 3rd Season https://kanokari-official.com/ #かのかり #kanokari @kanokari_anime
# Level 1 dakedo Unique Skill de Saikyou desu https://level1-anime.com/ #レベル1だけどアニメ化です @level1_anime
# Liar Liar https://liar-liar-anime.com/ #ライアー・ライアー #ライアラ @liar2_official
# Masamune-kun no Revenge R https://masamune-tv.com/ #MASA_A @masamune_tv
# Okashi na Tensei https://okashinatensei-pr.com/ #おかしな転生 @okashinatensei
# Shinigami Bocchan to Kuro Maid S2 https://bocchan-anime.com/ #死神坊ちゃん @bocchan_anime
# Shiro Seijo to Kuro Bokushi https://shiroseijyo-anime.com/ @shiroseijyo_tv #白聖女と黒牧師
# Tsuyokute New Saga https://tsuyosaga-pr.com/ #つよサガ @tsuyosaga_pr


# Summer 2023 Anime
class Summer2023AnimeDownload(MainDownload):
    season = "2023-3"
    season_name = "Summer 2023"
    folder_name = '2023-3'

    def __init__(self):
        super().__init__()


# Higeki no Genkyou to Naru Saikyou Gedou Last Boss Joou wa Tami no Tame ni Tsukushimasu.
class LastameDownload(Summer2023AnimeDownload, NewsTemplate):
    title = 'Higeki no Genkyou to Naru Saikyou Gedou Last Boss Joou wa Tami no Tame ni Tsukushimasu.'
    keywords = [title, 'The Most Heretical Last Boss Queen: From Villainess to Savior', 'Lastame']
    website = 'https://lastame.com/'
    twitter = 'lastame_pr'
    hashtags = 'ラス為'
    folder_name = 'lastame'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsBox li',
                                    date_select='small', title_select='p', id_select='a',
                                    date_func=lambda x: x.replace('年', '.').replace('月', '.').replace('日', ''))

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FgH9hRHVEAAZFyz?format=jpg&name=large')
        self.add_to_image_list('tz_mv_pc', self.PAGE_PREFIX + 'wp/wp-content/themes/original/assets/img/mv_pc.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/original/assets/img/character01-main%s.png'
        self.download_by_template(folder, template, 2, start=1, end=3)


# Kanojo, Okarishimasu 3rd Season
class Kanokari3Download(Summer2023AnimeDownload, NewsTemplate):
    title = "Kanojo, Okarishimasu 3rd Season"
    keywords = [title, "Kanokari", "Rent-a-Girlfriend"]
    website = 'https://kanokari-official.com/'
    twitter = 'kanokari_anime'
    hashtags = ['彼女お借りします', 'かのかり', 'kanokari']
    folder_name = 'kanokari3'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-item',
                                    title_select='.news-title', date_select='.news-date', id_select='a',
                                    paging_type=0, next_page_select='ul.pagenation-list li', next_page_eval_index=-1,
                                    next_page_eval_index_class='is__current')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            divs = soup.select('.firstview>div[class]')
            self.image_list = []
            for div in divs:
                has_visual_class = False
                for _class in div['class']:
                    if 'visual' in _class:
                        has_visual_class = True
                        break
                if not has_visual_class:
                    continue
                images = div.select('img[src]')
                for image in images:
                    image_url = image['src']
                    if '/images/' not in image_url:
                        continue
                    image_name = self.generate_image_name_from_url(image_url, 'images')
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'chara/')
            images = soup.select('.chara-stand img[src]')
            self.image_list = []
            for image in images:
                image_url = image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Level 1 dakedo Unique Skill de Saikyou desu
class Level1Download(Summer2023AnimeDownload, NewsTemplate):
    title = 'Level 1 dakedo Unique Skill de Saikyou desu'
    keywords = [title, 'My Unique Skill Makes Me OP Even at Level 1']
    website = 'https://level1-anime.com/'
    twitter = 'level1_anime'
    hashtags = 'レベル1だけどアニメ化です'
    folder_name = 'level1'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-item',
                                    date_select='.date', title_select='.title', id_select='a',
                                    next_page_select='div.pagination .page-numbers',
                                    next_page_eval_index_class='current', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FeSNHVXaYAEXR1w?format=jpg&name=medium')
        self.add_to_image_list('tz_kv-pc', self.PAGE_PREFIX + 'wp/wp-content/themes/level1_teaser/images/kv-pc.jpg')
        self.add_to_image_list('tz_kv-sp', self.PAGE_PREFIX + 'wp/wp-content/themes/level1_teaser/images/kv-sp.jpg')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/FqmF5NgaIAE4lDX?format=jpg&name=4096x4096')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.fv-slider img[src]')
            for image in images:
                image_url = image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/level1_teaser/images/chara-pic%s.png'
        self.download_by_template(folder, template, 1, 1, prefix='tz_')


# Liar Liar
class LiarLiarDownload(Summer2023AnimeDownload, NewsTemplate):
    title = 'Liar Liar'
    keywords = [title]
    website = 'https://liar-liar-anime.com/'
    twitter = 'liar2_official'
    hashtags = ['ライアー・ライアー', 'ライアラ']
    folder_name = 'liarliar'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.archives_ul_li',
                                    date_select='.archives_ul_li_date', title_select='.archives_ul_li_text',
                                    id_select='a', date_separator='/')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fhu9_4VUYAAz0MW?format=jpg&name=4096x4096')
        self.download_image_list(folder)

        prefix = self.PAGE_PREFIX + 'common/images/contents_top_fv_stand%s'
        templates = [prefix + '.jpg', prefix + 'b.jpg']
        self.download_by_template(folder, templates, 2, 1, prefix='tz_')

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'common/images/contents_character_'
        prefix2 = self.PAGE_PREFIX + 'common/images/contents_character02_'
        templates = [prefix + 'stand%s.png', prefix + 'face%s.png']
        templates2 = [prefix2 + 'stand%s.png', prefix2 + 'face%s.png']
        self.download_by_template(folder, templates, 2, 1)
        self.download_by_template(folder, templates2, 2, 1)


# Masamune-kun no Revenge R
class Masamunekun2Download(Summer2023AnimeDownload, NewsTemplate):
    title = 'Masamune-kun no Revenge R'
    keywords = [title, "Masamune's Revenge", "2nd"]
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
                                    date_select='.txt--date', title_select='.txt--ttl', id_select='a',
                                    next_page_select='ul.pagenation-list li', next_page_eval_index=-1,
                                    next_page_eval_index_class='is__current')

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


# Okashi na Tensei
class OkashinaTenseiDownload(Summer2023AnimeDownload, NewsTemplate):
    title = 'Okashi na Tensei'
    keywords = [title, 'Sweet Reincarnation']
    website = 'https://okashinatensei-pr.com/'
    twitter = 'okashinatensei'
    hashtags = 'おかしな転生'
    folder_name = 'okashinatensei'

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
        self.add_to_image_list('tz_natalie', 'https://ogre.natalie.mu/media/news/comic/2022/1215/okashinatensei_teaser.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/okashinatensei/static/character/%s/main.png'
        for i in range(10):
            number = str(i + 1).zfill(2)
            image_name = 'tz_char' + number
            if self.is_image_exists(image_name, folder):
                continue
            image_url = template % number
            result = self.download_image(image_url, folder + '/' + image_name)
            if result == -1:
                break


# Shinigami Bocchan to Kuro Maid S2
class ShinigamiBocchan2Download(Summer2023AnimeDownload, NewsTemplate2):
    title = 'Shinigami Bocchan to Kuro Maid 2nd Season'
    keywords = [title, 'The Duke of Death and His Maid']
    website = 'https://bocchan-anime.com/'
    twitter = 'bocchan_anime'
    hashtags = '死神坊ちゃん'
    folder_name = 'shinigami-bocchan2'

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
        self.download_template_news(self.PAGE_PREFIX, stop_date='2022.05.13')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        sub_folder = self.create_custom_directory(folder.split('/')[-1] + '/news')
        cache_filepath = sub_folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'news/', decode=True)
            while True:
                stop = False
                items = soup.select('#list_01 .bg_a, #list_01 .bg_b')
                for item in items:
                    date = item.select('.day')
                    if len(date) == 0 or date[0].text.startswith('2022'):
                        stop = True
                        break
                    a_tag = item.select('a[href]')
                    if len(a_tag) == 0:
                        continue
                    if not a_tag[0]['href'].startswith('../') or '/news/' not in a_tag[0]['href'] \
                            or not a_tag[0]['href'].endswith('.html'):
                        continue
                    page_name = a_tag[0]['href'].split('/')[-1].split('.html')[0]
                    if page_name in processed:
                        stop = True
                        break
                    title = a_tag[0].text.strip()
                    if 'ビジュアル' in title:
                        news_soup = self.get_soup(self.PAGE_PREFIX + a_tag[0]['href'].replace('../', ''))
                        if news_soup is not None:
                            images = news_soup.select('#news_block img[src]')
                            self.image_list = []
                            for image in images:
                                image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                                if '/news/' not in image_url:
                                    continue
                                image_name = self.generate_image_name_from_url(image_url, 'news') \
                                    .replace('_block_', '_')
                                self.add_to_image_list(image_name, image_url)
                            self.download_image_list(sub_folder)
                    processed.append(page_name)
                if stop:
                    break
                next_page = soup.select('.nb_nex a[href]')
                if len(next_page) == 0:
                    break
                soup = self.get_soup(self.PAGE_PREFIX + next_page[0]['href'].replace('../', ''))
        except Exception as e:
            self.print_exception(e, 'Key Visual News')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Shiro Seijo to Kuro Bokushi
class ShiroSeijoDownload(Summer2023AnimeDownload, NewsTemplate):
    title = 'Shiro Seijo to Kuro Bokushi'
    keywords = [title, "Saint Cecilia and Pastor Lawrence", 'shiroseijyo']
    website = 'https://shiroseijyo-anime.com/'
    twitter = 'shiroseijyo_tv'
    hashtags = '白聖女と黒牧師'
    folder_name = 'shiroseijyo'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.newsList',
                                    date_select='.newsList__date', title_select='.newsList__title span', id_select='a',
                                    a_tag_prefix=self.PAGE_PREFIX + 'news/')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FdZsEiyWYAA1hfB?format=jpg&name=4096x4096')
        self.add_to_image_list('top_mv_character', self.PAGE_PREFIX + 'assets/img/top/mv_character.png')
        self.add_to_image_list('kv_tw', 'https://pbs.twimg.com/media/Fj7f8HNUUAASOrr?format=jpg&name=4096x4096')
        self.add_to_image_list('top_mv2_character', self.PAGE_PREFIX + 'assets/img/top/mv2_character.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.characterList img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'][2:]
                image_name = self.generate_image_name_from_url(image_url, 'img')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Tsuyokute New Saga
class TsuyosagaDownload(Summer2023AnimeDownload, NewsTemplate):
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
