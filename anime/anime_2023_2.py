from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2


# Boku no Kokoro no Yabai Yatsu https://bokuyaba-anime.com/ #僕ヤバ #僕の心のヤバイやつ @bokuyaba_anime
# Isekai de Cheat Skill wo Te ni Shita Ore wa https://iseleve.com　@iseleve_anime
# Isekai Shoukan wa Nidome desu https://isenido.com/ #いせにど @isenido_anime
# Isekai wa Smartphone to Tomo ni. 2 http://isesuma-anime.jp/ #イセスマ @isesumaofficial
# Kawaisugi Crisis https://kawaisugi.com/ #カワイスギクライシス @kawaisugicrisis
# Kuma Kuma Kuma Bear Punch! https://kumakumakumabear.com/ #くまクマ熊ベアー #kumabear @kumabear_anime
# Megami no Cafe Terrace https://goddess-cafe.com/ #女神のカフェテラス @goddess_cafe_PR
# Oshi no Ko https://ichigoproduction.com/ #推しの子 @anime_oshinoko
# Otonari ni Ginga https://otonari-anime.com/ #おとなりに銀河 @otonariniginga
# Tensei Kizoku no Isekai Boukenroku https://www.tensei-kizoku.jp/ #転生貴族 @tenseikizoku
# Tonikaku Kawaii S2 http://tonikawa.com/ #トニカクカワイイ #tonikawa @tonikawa_anime
# Watashi no Yuri wa Oshigoto desu! https://watayuri-anime.com/ #わたゆり #私の百合はお仕事です @watayuri_anime
# Yamada-kun to Lv999 no Koi wo Suru https://yamadalv999-anime.com/ #山田999 @yamada999_anime
# Yuusha ga Shinda! https://heroisdead.com/ #勇者が死んだ @yuusyagasinda


# Spring 2023 Anime
class Spring2023AnimeDownload(MainDownload):
    season = "2023-2"
    season_name = "Spring 2023"
    folder_name = '2023-2'

    def __init__(self):
        super().__init__()


# Boku no Kokoro no Yabai Yatsu
class BokuyabaDownload(Spring2023AnimeDownload, NewsTemplate):
    title = 'Boku no Kokoro no Yabai Yatsu'
    keywords = [title, 'The Dangers in My Heart', 'Bokuyaba']
    website = 'https://bokuyaba-anime.com/'
    twitter = 'bokuyaba_anime'
    hashtags = ['僕ヤバ', '僕の心のヤバイやつ']
    folder_name = 'bokuyaba'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index', diff=5)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.p-news__list-item',
                                    date_select='.p-news_data__date', title_select='.p-news_data__title',
                                    id_select='a', a_tag_start_text_to_remove='/', a_tag_prefix=self.PAGE_PREFIX,
                                    date_func=lambda x: x[0:4] + '.' + x[5:])

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.p-hero_kv_visual__main img[src]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('./', '')
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/img/character/chara_stand_%s.png'
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            self.image_list = []
            images = soup.select('img.u-lazy[data-src]')
            for image in images:
                img_name = image['data-src'].split('/')[-1].split('.')[0].split('_')[-1]
                image_url = template % img_name
                image_name = 'chara_stand_' + img_name
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Isekai de Cheat Skill wo Te ni Shita Ore wa, Genjitsu Sekai wo mo Musou Suru: Level Up wa Jinsei wo Kaeta
class IseleveDownload(Spring2023AnimeDownload, NewsTemplate):
    title = 'Isekai de Cheat Skill wo Te ni Shita Ore wa, Genjitsu Sekai wo mo Musou Suru: Level Up wa Jinsei wo Kaeta'
    keywords = [title, 'I Got a Cheat Skill in Another World and Became Unrivaled in The Real World, Too', 'iseleve']
    website = 'https://www.iseleve.com/'
    twitter = 'iseleve_anime'
    hashtags = 'いせれべ'
    folder_name = 'iseleve'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_media()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, news_prefix='', article_select='.news a',
                                    date_select='dt', title_select='dd', id_select=None,
                                    a_tag_start_text_to_remove='./', a_tag_prefix=self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', 'https://pbs.twimg.com/media/FagU_nNVQAAy78W?format=jpg&name=medium')
        # self.add_to_image_list('tz_main_visual01', self.PAGE_PREFIX + 'img/main_visual01.jpg')
        # self.add_to_image_list('tz_main_visual02', self.PAGE_PREFIX + 'img/main_visual02.png')
        self.add_to_image_list('kv_tw', 'https://pbs.twimg.com/media/FhwPyAwUcAEKojn?format=jpg&name=4096x4096')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.accshow img[src], img[src].main_img')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_media(self):
        folder = self.create_media_directory()
        self.image_list = []
        self.add_to_image_list('teaser_coment_img01', self.PAGE_PREFIX + 'img/teaser_coment_img01.jpg')
        self.add_to_image_list('teaser_coment_img02', self.PAGE_PREFIX + 'img/teaser_coment_img02.jpg')
        self.download_image_list(folder)


# Isekai Shoukan wa Nidome desu
class IsenidoDownload(Spring2023AnimeDownload, NewsTemplate):
    title = 'Isekai Shoukan wa Nidome desu'
    keywords = [title, 'isenido']
    website = 'https://isenido.com/'
    twitter = 'isenido_anime'
    hashtags = 'いせにど'
    folder_name = 'isenido'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-lists__item',
                                    date_select='.news-lists__sub', title_select='.news-lists__text', id_select='a',
                                    date_separator='/')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv-bg', self.PAGE_PREFIX + 'img/kv-bg.jpg')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FZxImcZUIAAV8uv?format=jpg&name=4096x4096')
        self.download_image_list(folder)

        self.image_list = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.kv-main__wrap .js_kv-img img[src]')
            for image in images:
                if image.has_attr('class') and '-sp' in image['class']:
                    continue
                if not image['src'].startswith('/img/'):
                    continue
                image_url = self.PAGE_PREFIX + image['src'][1:]
                image_name = self.generate_image_name_from_url(image_url, 'img')
                self.add_to_image_list(image_name, image_url)
        except Exception as e:
            self.print_exception(e, 'Key Visual')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.c-feature__img img[src]')
            for image in images:
                if '/character/' not in image['src']:
                    continue
                image_url = self.PAGE_PREFIX + image['src']
                image_name = self.generate_image_name_from_url(image_url, 'character')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Isekai wa Smartphone to Tomo ni. 2
class Isesuma2Download(Spring2023AnimeDownload, NewsTemplate):
    title = 'Isekai wa Smartphone to Tomo ni. 2'
    keywords = [title, "In Another World With My Smartphone 2"]
    website = 'http://isesuma-anime.jp/'
    twitter = 'isesumaofficial'
    hashtags = 'イセスマ'
    folder_name = 'isesuma2'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.entryArea',
                                    date_select='.date', title_select='.subj', id_select='.notexist')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_main', self.PAGE_PREFIX + 'img/main.jpg')
        self.add_to_image_list('main2chara2', self.PAGE_PREFIX + 'img/main2chara2.png')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FYQeHycaMAIdyyN?format=jpg&name=medium')
        self.add_to_image_list('kv1', 'https://pbs.twimg.com/media/FiZQEg9acAAZ91t?format=jpg&name=large')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.charaArea img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src']
                image_name = self.generate_image_name_from_url(image_url, 'chara')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Kawaisugi Crisis https://kawaisugi.com/ #カワイスギクライシス @kawaisugicrisis
class KawaisugiCrisisDownload(Spring2023AnimeDownload, NewsTemplate):
    title = 'Kawaisugi Crisis'
    keywords = [title, 'Too Cute Crisis']
    website = 'https://kawaisugi.com/'
    twitter = 'kawaisugicrisis'
    hashtags = 'カワイスギクライシス'
    folder_name = 'kawaisugicrisis'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.kwsg_contents_top_news_list_item',
                                    date_select='.kwsg_contents_top_news_list_item_left',
                                    title_select='.kwsg_contents_top_news_list_item_right', id_select='a',
                                    next_page_select='.page-numbers', next_page_eval_index=-1,
                                    next_page_eval_index_class='current')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        template = self.PAGE_PREFIX + 'common/images/top_kv%s.jpg'
        self.download_by_template(folder, template, 2, 2)

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character')
            a_tags = soup.select('#kwsg_contents_character_list a[href]')
            for a_tag in a_tags:
                if '/character/' not in a_tag['href']:
                    continue
                page = a_tag['href'].split('/')[-1]
                if page in processed:
                    continue
                chara_soup = self.get_soup(a_tag['href'])
                if chara_soup is None:
                    continue
                self.image_list = []
                images = chara_soup.select('#kwsg_contents_character_body img[src]')
                for image in images:
                    image_url = image['src']
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
                if len(self.image_list) > 0:
                    processed.append(page)
                self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Kuma Kuma Kuma Bear Punch!
class KumaBear2Download(Spring2023AnimeDownload, NewsTemplate2):
    title = 'Kuma Kuma Kuma Bear Punch!'
    keywords = [title, "2nd"]
    website = 'https://kumakumakumabear.com/'
    twitter = 'kumabear_anime'
    hashtags = ['くまクマ熊ベアー', 'kumabear']
    folder_name = 'kumabear2'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/01.html')
            trs = soup.select('#ContentsListUnit01 tr[class]')
            for tr in trs:
                a_tags = tr.select('a[href]')
                if len(a_tags) == 0:
                    continue
                try:
                    episode = str(int(a_tags[0].text.replace('#', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if episode == '01':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(self.PAGE_PREFIX + a_tags[0]['href'].replace('../', ''))
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('ul.tp5 img[src]')
                for i in range(len(images)):
                    image_url = self.PAGE_PREFIX + images[i]['src'].split('?')[0].replace('../', '').replace('sn_', '')
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv_aniverse', 'https://aniverse-mag.com/wp-content/uploads/2022/11/96785c9962f5ef9863dc77113ebdf26f.jpg')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.loading__kv-img img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src']
                if '/main/' in image_url:
                    image_name = self.generate_image_name_from_url(image_url, 'main')
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        self.add_to_image_list('tz_yuna', 'https://aniverse-mag.com/wp-content/uploads/2022/11/aade6f0c762346c7e43719675da36208.png')
        self.add_to_image_list('tz_fina', 'https://aniverse-mag.com/wp-content/uploads/2022/11/de14b80b290bdc786e18e6150c323d0e.png')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'core_sys/images/main/tz/chara_%s.png'
        self.download_by_template(folder, template, 2, 1, prefix='tz_')


# Megami no Café Terrace
class MegamiCafeDownload(Spring2023AnimeDownload, NewsTemplate):
    title = 'Megami no Café Terrace'
    keywords = [title, 'Cafe', 'The Cafe Terrace and its Goddesses']
    website = 'https://goddess-cafe.com/'
    twitter = 'goddess_cafe_PR'
    hashtags = '女神のカフェテラス'
    folder_name = 'megami-cafe'

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
                                    title_select='.news-item-title', date_select='.news-item-pubdate', id_select='a',
                                    date_func=lambda x: x.replace('年', '.').replace('月', '.').replace('日', ''),
                                    next_page_select='.pagination a', next_page_eval_index=-1,
                                    next_page_eval_index_class='disabled')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FhMLJOMUUAAlbav?format=jpg&name=large')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.main-visual-large img[src]')
            self.image_list = []
            for image in images:
                image_url = image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.character-image img[src]')
            self.image_list = []
            for image in images:
                image_url = image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Oshi no Ko
class OshinokoDownload(Spring2023AnimeDownload, NewsTemplate2):
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
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FU0bJsjaAAAE7Bf?format=jpg&name=large')
        self.add_to_image_list('tz_kv', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.jpg')
        self.add_to_image_list('tz_kv2', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv2/kv.jpg')
        self.add_to_image_list('tz_kv3', self.PAGE_PREFIX + 'core_sys/images/main/kv3/kv3.jpg')
        self.download_image_list(folder)

        sub_folder = self.create_custom_directory(folder.split('/')[-1] + '/news')
        cache_filepath = sub_folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'news/')
            while True:
                stop = False
                items = soup.select('#list_01 a[href]')
                for item in items:
                    if not item['href'].startswith('../') or '/news/' not in item['href'] \
                            or not item['href'].endswith('.html'):
                        continue
                    page_name = item['href'].split('/')[-1].split('.html')[0]
                    if page_name in processed:
                        stop = True
                        break
                    title = item.text.strip()
                    if 'ビジュアル' in title:
                        news_soup = self.get_soup(self.PAGE_PREFIX + item['href'].replace('../', ''))
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

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'chara/')
            a_tags = soup.select('#ContentsListUnit01 a[href]')
            for a_tag in a_tags:
                chara_url = self.PAGE_PREFIX + a_tag['href'].replace('../', '')
                chara_name = chara_url.split('/')[-1].replace('.html', '')
                if chara_name in processed:
                    continue
                if chara_name == 'index':
                    chara_soup = soup
                else:
                    chara_soup = self.get_soup(chara_url)
                if chara_soup is not None:
                    images = chara_soup.select('.ph img[src]')
                    for image in images:
                        image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                        image_name = self.extract_image_name_from_url(image_url)
                        self.add_to_image_list(image_name, image_url)
                    if len(self.image_list) > 0:
                        processed.append(chara_name)
                    self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Otonari ni Ginga
class OtonariniGingaDownload(Spring2023AnimeDownload, NewsTemplate):
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
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='#news article',
                                    title_select='h3', date_select='time', id_select=None, id_has_id=True,
                                    date_func=lambda x: x[0:4] + '.' + x[4:])

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FRV6mlUVIAAa9xK?format=jpg&name=medium')
        self.add_to_image_list('tz_mainimg', self.PAGE_PREFIX + 'teaser/images/mainimg.png')
        self.add_to_image_list('kv_tw', 'https://pbs.twimg.com/media/FgjBzJOaAAADdI_?format=jpg&name=medium')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'assets/images/top/mainimg%s.jpg'
        self.download_by_template(folder, template, 1, 1, prefix='top_')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/images/character/img_%s.png'
        self.download_by_template(folder, template, 2, 1)


# Tensei Kizoku no Isekai Boukenroku
class TenseiKizokuDownload(Spring2023AnimeDownload, NewsTemplate):
    title = 'Tensei Kizoku no Isekai Boukenroku'
    keywords = [title, "Chronicles of an Aristocrat Reborn in Another World"]
    website = 'https://www.tensei-kizoku.jp/'
    twitter = 'tenseikizoku'
    hashtags = '転生貴族'
    folder_name = 'tenseikizoku'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-list li',
                                    date_select='.news-date', title_select='.news-title', id_select='a',
                                    news_prefix='news.html', reverse_article_list=True)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv', self.PAGE_PREFIX + 'img/kv.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + '/character.html')
            self.image_list = []
            images = soup.select('ul[name=chara] img[src]')
            for image in images:
                if '/chara/' in image['src'] and '/name/' not in image['src']:
                    image_url = self.PAGE_PREFIX + image['src']
                    image_name = self.generate_image_name_from_url(image_url, 'chara')
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Tonikaku Kawaii S2
class Tonikawa2Download(Spring2023AnimeDownload, NewsTemplate):
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
        self.add_to_image_list('kv_seifuku', self.PAGE_PREFIX + 'assets/images/common/news/news-67/img_kv_l.jpg')
        self.add_to_image_list('tz2_tw', 'https://pbs.twimg.com/media/FiE3-1yVIAA8Scs?format=jpg&name=large')
        self.add_to_image_list('tz2', self.PAGE_PREFIX + 'assets/images/common/news/news-70/thumb_kv3_l.jpg')
        self.add_to_image_list('kv_tw', 'https://pbs.twimg.com/media/Fo6mnWmaYAE8cfj?format=jpg&name=large')
        self.download_image_list(folder)


# Watashi no Yuri wa Oshigoto desu!
class WatayuriDownload(Spring2023AnimeDownload, NewsTemplate):
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
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsList',
                                    date_select='time', title_select='.news__title', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FStxiD1VIAEX1nk?format=jpg&name=4096x4096')
        self.add_to_image_list('tz_mv1', self.PAGE_PREFIX + 'assets/img/top/mv1.jpg')
        self.add_to_image_list('tz_mv2', self.PAGE_PREFIX + 'assets/img/top/mv2.jpg')
        self.download_image_list(folder)


# Yamada-kun to Lv999 no Koi wo Suru
class Yamada999Download(Spring2023AnimeDownload, NewsTemplate):
    title = 'Yamada-kun to Lv999 no Koi wo Suru'
    keywords = [title, 'My Love Story with Yamada-kun at Lv999']
    website = 'https://yamadalv999-anime.com/'
    twitter = 'yamada999_anime'
    hashtags = '山田999'
    folder_name = 'yamada999'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.c-news__item',
                                    date_select='.c-news__item-date', title_select='.c-news__item-ttl',
                                    id_select='.c-news__item-link', a_tag_prefix=news_url, paging_type=1,
                                    date_func=lambda x: '20' + x, a_tag_start_text_to_remove='./',
                                    next_page_select='.c-pagination__count-item',
                                    next_page_eval_index_class='is-current', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_aniverse', 'https://aniverse-mag.com/wp-content/uploads/2022/09/259436eb01ba6f500f1c86345c70f63d.jpg')
        self.add_to_image_list('teaser_kv', self.PAGE_PREFIX + 'teaser/img/top/kv.jpg')
        self.download_image_list(folder)


# Yuusha ga Shinda!
class YuushagaShindaDownload(Spring2023AnimeDownload, NewsTemplate):
    title = 'Yuusha ga Shinda!'
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
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-list-item',
                                    date_select='.news-list-item__date', title_select='.news-list-item__title',
                                    id_select='a', a_tag_start_text_to_remove='/', a_tag_prefix=self.PAGE_PREFIX,
                                    date_func=lambda x: x.replace('年', '.').replace('月', '.').replace('日', ''))

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_aniverse', 'https://aniverse-mag.com/wp-content/uploads/2022/04/4576fa0e88a0464f6a9b6e8844e05dbd-e1651058246996.jpg')
        self.add_to_image_list('tz_visual_01_chara', self.PAGE_PREFIX + 'img/teaser/visual_01_chara.png')
        self.add_to_image_list('vis_kneesock', 'https://pbs.twimg.com/media/FilDh8XagAQnZU0?format=jpg&name=large')
        self.add_to_image_list('kv2_tw', 'https://pbs.twimg.com/media/FkGRdxEUcAECPlX?format=jpg&name=large')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'img/home/visual_%s_chara.png'
        self.download_by_template(folder, template, 2, 1, prefix='home_')

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'character/'
        self.image_list = []
        try:
            obj = self.get_json(prefix + 'chara_data.php')
            if 'charas' in obj:
                for chara in obj['charas']:
                    if 'images' in chara:
                        if 'visuals' in chara['images']:
                            for visual in chara['images']['visuals']:
                                if 'image' in visual:
                                    image_url = prefix + visual['image'].replace('./', '').split('?')[0]
                                    image_name = self.extract_image_name_from_url(image_url)
                                    self.add_to_image_list(image_name, image_url)
                        if 'faces' in chara['images']:
                            for face in chara['images']['faces']:
                                image_url = prefix + face.replace('./', '').split('?')[0]
                                image_name = self.extract_image_name_from_url(image_url)
                                self.add_to_image_list(image_name, image_url)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.download_image_list(folder)

