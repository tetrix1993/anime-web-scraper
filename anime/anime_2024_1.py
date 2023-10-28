from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate4

# Akuyaku Reijou Level 99 https://akuyakulv99-anime.com/ #akuyakuLV99 @akuyakuLV99
# Chiyu Mahou no Machigatta Tsukaikata https://chiyumahou-anime.com/ #治癒魔法 @chiyumahou_PR
# Dosanko Gal wa Namara Menkoi https://dosankogal-pr.com/ #道産子ギャル #どさこい @dosankogal_pr
# Dungeon Meshi https://delicious-in-dungeon.com/ #ダンジョン飯 #deliciousindungeon @dun_meshi_anime
# Himesama "Goumon" no Jikan desu https://himesama-goumon.com/ #姫様拷問の時間です @himesama_goumon
# Kekkon Yubiwa Monogatari https://talesofweddingrings-anime.jp/ #結婚指輪物語 @weddingringsPR
# Jaku-Chara Tomozaki-kun 2nd Stage http://tomozaki-koushiki.com/ #友崎くん @tomozakikoshiki
# Mato Seihei no Slave https://mabotai.jp/ #魔都精兵のスレイブ #まとスレ @mabotai_kohobu
# Pon no Michi https://ponnomichi-pr.com/ #ぽんのみち @ponnomichi_pr
# Saikyou Tank no Meikyuu Kouryaku https://saikyo-tank.com/ #最強タンク @saikyo_tank
# Sasayaku You ni Koi wo Utau https://sasakoi-anime.com/ #ささこい @sasakoi_anime


# Winter 2024 Anime
class Winter2024AnimeDownload(MainDownload):
    season = "2024-1"
    season_name = "Winter 2024"
    folder_name = '2024-1'

    def __init__(self):
        super().__init__()


# Akuyaku Reijou Level 99
class AkuyakuLv99Download(Winter2024AnimeDownload, NewsTemplate2):
    title = 'Akuyaku Reijou Level 99'
    keywords = [title, 'Villainess Level 99']
    website = 'https://akuyakulv99-anime.com/'
    twitter = 'akuyakuLV99'
    hashtags = 'akuyakuLV99'
    folder_name = 'akuyakulv99'

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
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fr-S3r0aQAAH2xA?format=jpg&name=medium')
        self.add_to_image_list('tzkv', self.PAGE_PREFIX + 'core_sys/images/main/home/tzkv.png')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.mainImg__kv source[type][srcset]')
            self.image_list = []
            for image in images:
                if '/main/' not in image['srcset']:
                    continue
                image_name = self.extract_image_name_from_url(image['srcset'])
                if 'kv' not in image_name:
                    continue
                image_name = self.generate_image_name_from_url(image['srcset'], 'main')
                image_url = self.PAGE_PREFIX + image['srcset'].split('?')[0].replace('./', '')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.charaStand source[type][srcset], .charaFace source[type][srcset]')
            self.image_list = []
            for image in images:
                if '/chara/' not in image['srcset']:
                    continue
                image_name = self.generate_image_name_from_url(image['srcset'], 'chara')
                image_url = self.PAGE_PREFIX + image['srcset'].split('?')[0].replace('./', '')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Chiyu Mahou no Machigatta Tsukaikata
class ChiyuMahouDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Chiyu Mahou no Machigatta Tsukaikata'
    keywords = [title, 'The Wrong Way to Use Healing Magic']
    website = 'https://chiyumahou-anime.com/'
    twitter = 'chiyumahou_PR'
    hashtags = ['治癒魔法']
    folder_name = 'chiyumahou'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index', diff=150)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsArchive-Item',
                                    date_select='.date', title_select='.title', id_select='a',
                                    next_page_select='.nextpostslink')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        # self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FwP_QYPaQAMBkyd?format=jpg&name=medium')
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'wp-content/themes/chiyumahou-anime_teaser/assets/images/pc/index/img_hero.jpg')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.visual img[src]')
            self.image_list = []
            for image in images:
                if '/pc/' not in image['src']:
                    continue
                image_url = image['src'].split('?')[0]
                image_name = self.generate_image_name_from_url(image_url, 'pc')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            a_tags = soup.select('.character-List li>a[href]')
            for a_tag in a_tags:
                chara_url = a_tag['href']
                if chara_url.endswith('/'):
                    chara_name = chara_url[:-1].split('/')[-1]
                else:
                    chara_name = chara_url.split('/')[-1]
                if chara_name in processed:
                    continue
                chara_soup = self.get_soup(self.PAGE_PREFIX + chara_url[1:])
                if chara_soup is not None:
                    images = chara_soup.select('.character-Detail img[src]')
                    for image in images:
                        image_url = image['src']
                        if '/character/' not in image_url:
                            continue
                        image_name = self.generate_image_name_from_url(image_url, 'character')
                        self.add_to_image_list(image_name, image_url)
                    if len(self.image_list) > 0:
                        processed.append(chara_name)
                    self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Dosanko Gal wa Namara Menkoi
class DosankoGalDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Dosanko Gal wa Namara Menkoi'
    keywords = [title, 'Hokkaido Gals Are Super Adorable!', 'dosakoi']
    website = 'https://dosankogal-pr.com/'
    twitter = 'dosankogal_pr'
    hashtags = ['道産子ギャル', 'どさこい']
    folder_name = 'dosankogal'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        soup = self.download_key_visual()
        self.download_character(soup)

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        # Paging logic not known
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.md-list__news li',
                                    date_select='.txt--date', title_select='.txt--ttl', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        # self.image_list = []
        # self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FkJnLbAVUAERF5S?format=jpg&name=4096x4096')
        # self.add_to_image_list('tz_news', self.PAGE_PREFIX + 'wp/wp-content/uploads/2022/12/dosankogal_teaser_logoc-scaled-1.jpg')
        # self.download_image_list(folder)

        soup = None
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.fvslide source[srcset]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'][1:]
                if '/images/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'images')
                if image_name.endswith('_sp'):
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')
        return soup

    def download_character(self, soup=None):
        folder = self.create_character_directory()
        try:
            if soup is None:
                soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.chardata--inner source[srcset]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'][1:]
                if '/images/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'images')
                if image_name.endswith('_sp'):
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Dungeon Meshi
class DungeonMeshiDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Dungeon Meshi'
    keywords = [title, 'Delicious in Dungeon']
    website = 'https://delicious-in-dungeon.com/'
    twitter = 'dun_meshi_anime'
    hashtags = ['ダンジョン飯', 'deliciousindungeon']
    folder_name = 'dungeon-meshi'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.content-entry',
                                    title_select='.entry-title span', date_select='.entry-date span',
                                    id_select=None, id_has_id=True, news_prefix='news.html')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.vis img[src]')
            self.image_list = []
            for image in images:
                if '/assets/' not in image['src']:
                    continue
                image_url = image['src']
                if image_url.startswith('./'):
                    image_url = self.PAGE_PREFIX + image_url[2:]
                image_name = self.generate_image_name_from_url(image_url, 'assets')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        templates = [
            self.PAGE_PREFIX + 'assets/character/%sc.png',
            self.PAGE_PREFIX + 'assets/character/%sf.png'
        ]
        self.download_by_template(folder, templates, 1, 1)


# Himesama "Goumon" no Jikan desu
class HimesamaGoumonDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Himesama "Goumon" no Jikan desu'
    keywords = [title, '\'Tis Time for "Torture," Princess']
    website = 'https://himesama-goumon.com/'
    twitter = 'himesama_goumon'
    hashtags = ['姫様拷問の時間です']
    folder_name = 'himesamagoumon'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.md-li__post article',
                                    date_select='time', title_select='.ttl', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.fvimg source[srcset]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'][1:]
                if '/top/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'top')
                if image_name.endswith('_sp'):
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')


# Kekkon Yubiwa Monogatari
class KekkonYubiwaDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Kekkon Yubiwa Monogatari'
    keywords = [title, 'Tales of Wedding Rings']
    website = 'https://talesofweddingrings-anime.jp/'
    twitter = 'weddingringsPR'
    hashtags = '結婚指輪物語'
    folder_name = 'kekkonyubiwa'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, news_prefix='', article_select='.newsinlist li',
                                    date_select='.newstime', title_select='a', id_select='a', id_has_id=True,
                                    id_attr='data-cl')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'images/mob02/per_bg.png')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FsCGtvQaMAEldYZ?format=jpg&name=large')
        self.download_image_list(folder)

        sub_folder = self.create_custom_directory(folder.split('/')[-1] + '/news')
        cache_filepath = sub_folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX, decode=True)
            items = soup.select('.newsinlist li a[data-cl]')
            for item in items:
                page_name = item['data-cl']
                if page_name in processed:
                    break
                title = item.text.strip()
                if 'ビジュアル' in title or 'イラスト' in title:
                    images = soup.select(f'.lbox_com.{page_name} img[src]')
                    self.image_list = []
                    for image in images:
                        image_url = self.PAGE_PREFIX + image['src'].replace('./', '').split('?')[0]
                        if '/news/' not in image_url or image_url.endswith('.svg'):
                            continue
                        image_name = self.generate_image_name_from_url(image_url, 'news')
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(sub_folder)
                processed.append(page_name)
        except Exception as e:
            self.print_exception(e, 'Key Visual News')
        self.create_cache_file(cache_filepath, processed, num_processed)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'images/mob02/chara_%s.png'
        self.download_by_template(folder, template, 2, 1)


# Jaku-Chara Tomozaki-kun 2nd Stage
class TomozakiKun2Download(Winter2024AnimeDownload, NewsTemplate):
    title = "Jaku-Chara Tomozaki-kun 2nd Stage"
    keywords = [title, 'The Low Tier Character "Tomozaki-kun"', 'Tomozaki-kun']
    website = 'http://tomozaki-koushiki.com/'
    twitter = 'tomozakikoshiki'
    hashtags = '友崎くん'
    folder_name = 'tomozakikun2'

    PAGE_PREFIX = website
    FINAL_EPISODE = 13

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.box_main',
                                    date_select='time', title_select='.box_title', id_select='nothing')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        template = self.PAGE_PREFIX + 'img/index/vis_img%s.jpg'
        self.download_by_template(folder, template, 1, 1)


# Mato Seihei no Slave
class MatoSlaveDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Mato Seihei no Slave'
    keywords = [title, 'Chained Soldier', 'matoslave', 'mabotai']
    website = 'https://mabotai.jp/'
    twitter = 'mabotai_kohobu'
    hashtags = ['魔都精兵のスレイブ', 'まとスレ']
    folder_name = 'matoslave'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        # self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    # def download_news(self):
    #    self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        # self.image_list = []
        # self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FEiqZdFaUAQyOy4?format=jpg&name=900x900')
        # self.download_image_list(folder)

        teaser_template = self.PAGE_PREFIX + 'img/home/visual_%s.webp'
        for i in range(1, 11, 1):
            image_name = f'home_visual_{i}'
            if self.is_image_exists(image_name, folder):
                continue
            image_url = teaser_template % str(i).zfill(2)
            result = self.download_image(image_url, f'{folder}/{image_name}')
            if result == -1:
                break

    def download_character(self):
        folder = self.create_character_directory()
        char_url = self.PAGE_PREFIX + 'character'
        json_url = char_url + '/chara_data.php'
        self.image_list = []
        try:
            json_obj = self.get_json(json_url)
            if 'charas' in json_obj and isinstance(json_obj['charas'], list):
                for chara in json_obj['charas']:
                    if 'images' in chara:
                        if 'visuals' in chara['images'] and isinstance(chara['images']['visuals'], list):
                            for visual in chara['images']['visuals']:
                                if 'image' in visual:
                                    image_url = char_url + visual['image'][1:].split('?')[0]
                                    image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                                    self.add_to_image_list(image_name, image_url)
                        if 'faces' in chara['images'] and isinstance(chara['images']['faces'], list):
                            for face in chara['images']['faces']:
                                image_url = char_url + face[1:].split('?')[0]
                                image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                                self.add_to_image_list(image_name, image_url)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.download_image_list(folder)


# Pon no Michi
class PonnoMichiDownload(Winter2024AnimeDownload, NewsTemplate4):
    title = 'Pon no Michi'
    keywords = [title, "Whisper Me a Love Song"]
    website = 'https://ponnomichi-pr.com/'
    twitter = 'ponnomichi_pr'
    hashtags = ['ぽんのみち', 'ponnomichi']
    folder_name = 'ponnomichi'

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
        self.download_template_news('ponnomichi')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fwy-ZH3aYAAUzwg?format=jpg&name=large')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('div[class*="Visual"] img[srcSet*="kv_"]')
            for image in images:
                image_url = image['srcset']
                if '/static/' not in image_url:
                    continue
                if image_url.startswith('/'):
                    image_url = self.PAGE_PREFIX + image_url[1:]
                image_name = self.generate_image_name_from_url(image_url, 'static')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character')
            self.image_list = []
            images = soup.select('img[src][class*="CharacterImage"]')
            for image in images:
                image_url = image['src']
                if '/static/' not in image_url:
                    continue
                if image_url.startswith('/'):
                    image_url = self.PAGE_PREFIX + image_url[1:]
                image_name = self.generate_image_name_from_url(image_url, 'static')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Sasayaku You ni Koi wo Utau
class SasakoiDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Sasayaku You ni Koi wo Utau'
    keywords = [title, "Whisper Me a Love Song"]
    website = 'https://sasakoi-anime.com/'
    twitter = 'sasakoi_anime'
    hashtags = ['ささこい', 'sasakoi']
    folder_name = 'sasakoi'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news__list tr', news_prefix='',
                                    date_select='.day', title_select='.title', id_select='a', date_separator='/',
                                    a_tag_prefix=self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_kv', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.webp')
        self.add_to_image_list('tz_teaser', self.PAGE_PREFIX + 'core_sys/images/main/tz/teaser.jpg')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.kv__img source[srcset]')
            self.image_list = []
            for image in images:
                if '/main/' not in image['srcset']:
                    continue
                image_name = self.extract_image_name_from_url(image['srcset'])
                if 'kv' not in image_name:
                    continue
                image_name = self.generate_image_name_from_url(image['srcset'], 'main')
                image_url = self.PAGE_PREFIX + image['srcset']
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'core_sys/images/main/tz/chara/c%s_face.jpg'
        self.download_by_template(folder, template, 2, 1, prefix='tz_')


# Saikyou Tank no Meikyuu Kouryaku
class SaikyoTankDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Saikyou Tank no Meikyuu Kouryaku'
    keywords = [title, "The Strongest Tank's Labyrinth Raids"]
    website = 'https://saikyo-tank.com/'
    twitter = 'saikyo_tank'
    hashtags = ['最強タンク']
    folder_name = 'saikyotank'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.p-News__postList a',
                                    date_select='.c-Post__date', title_select='.c-Post__title', id_select=None,
                                    date_func=lambda x: x[0:4] + '.' + x[5:])

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_kv', self.PAGE_PREFIX + 'news/wp-content/uploads/2023/10/STM_01_ティザービジュアル_1@0.3x.png')
        self.add_to_image_list('fv_kv_1', self.PAGE_PREFIX + 'dist/img/top/fv/kv_1.webp')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.p-Chara__charMain source[type][srcset]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset']
                if '/chara/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'chara')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')
