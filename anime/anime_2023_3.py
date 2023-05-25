from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate4


# Eiyuu Kyoushitsu https://eiyukyoushitsu-anime.com/ #英雄教室 #eiyu_anime @eiyu_anime
# Higeki no Genkyou to Naru Saikyou Gedou Last Boss Joou wa Tami no Tame ni Tsukushimasu. https://lastame.com/ #ラス為 @lastame_pr
# Horimiya: Piece https://horimiya-anime.com/ #ホリミヤ #horimiya @horimiya_anime
# Jidou Hanbaiki ni Umarekawatta Ore wa Meikyuu wo Samayou https://jihanki-anime.com/ #俺自販機 @jihanki_anime
# Kanojo, Okarishimasu 3rd Season https://kanokari-official.com/ #かのかり #kanokari @kanokari_anime
# Level 1 dakedo Unique Skill de Saikyou desu https://level1-anime.com/ #レベル1だけどアニメ化です @level1_anime
# Liar Liar https://liar-liar-anime.com/ #ライアー・ライアー #ライアラ @liar2_official
# Masamune-kun no Revenge R https://masamune-tv.com/ #MASA_A @masamune_tv
# Nanatsu no Maken ga Shihai suru https://nanatsuma-pr.com/ #nanatsuma #ななつま @nanatsuma_pr
# Okashi na Tensei https://okashinatensei-pr.com/ #おかしな転生 @okashinatensei
# Ryza no Atelier: Tokoyami no Joou to Himitsu no Kakurega https://ar-anime.com/ #ライザのアトリエ @Ryza_PR
# Seija Musou: Salaryman, Isekai de Ikinokoru Tame ni Ayumu Michi https://www.tbs.co.jp/anime/seija/ #聖者無双 @seija_anime
# Shinigami Bocchan to Kuro Maid S2 https://bocchan-anime.com/ #死神坊ちゃん @bocchan_anime
# Shiro Seijo to Kuro Bokushi https://shiroseijyo-anime.com/ @shiroseijyo_tv #白聖女と黒牧師
# Suki na Ko ga Megane wo Wasureta https://anime.shochiku.co.jp/sukimega/ #好きめが @Sukimega
# Temple https://temple-anime.com/ #てんぷる #Tenpuru_anime @temple_tvanime
# Tsuyokute New Saga https://tsuyosaga-pr.com/ #つよサガ @tsuyosaga_pr
# Uchi no Kaisha no Chiisai Senpai no Hanashi https://chiisaisenpai.com/ #うちの会社の小さい先輩の話 @smallsenpai_pr
# Yumemiru Danshi wa Genjitsushugisha https://yumemirudanshi.com/ #夢見る男子 @yumemiru_anime


# Summer 2023 Anime
class Summer2023AnimeDownload(MainDownload):
    season = "2023-3"
    season_name = "Summer 2023"
    folder_name = '2023-3'

    def __init__(self):
        super().__init__()


# Eiyuu Kyoushitsu
class EiyuKyoushitsuDownload(Summer2023AnimeDownload, NewsTemplate):
    title = 'Eiyuu Kyoushitsu'
    keywords = [title, 'Classroom for Heroes']
    website = 'https://eiyukyoushitsu-anime.com/'
    twitter = 'eiyu_anime'
    hashtags = ['英雄教室', 'eiyu_anime']
    folder_name = 'eiyukyoushitsu'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newslist li',
                                    date_select='.newstime', title_select='p', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.mobmw img[src]')
            self.image_list = []
            for image in images:
                if 'kv' not in image['src'].lower():
                    continue
                image_url = self.PAGE_PREFIX + image['src'][1:]
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        # template = self.PAGE_PREFIX + 'images/chara_%s.png'
        # self.download_by_template(folder, template, 2, 1, prefix='tz_')
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            images = soup.select('.chara_pre_main img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


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
        self.add_to_image_list('kv', self.PAGE_PREFIX + 'wp/wp-content/uploads/2023/04/ラス為キービジュアル.jpg')
        # self.add_to_image_list('tz_mv_pc', self.PAGE_PREFIX + 'wp/wp-content/themes/original/assets/img/mv_pc.png')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.mv__mainSlider img[src]')
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
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            images = soup.select('.imageArea img[src], .thumbnailArea img[src]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'][1:]
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Horimiya: Piece
class Horimiya2Download(Summer2023AnimeDownload, NewsTemplate):
    title = "Horimiya: Piece"
    keywords = [title]
    website = 'https://horimiya-anime.com/'
    twitter = 'horimiya_anime'
    hashtags = ['ホリミヤ', 'horimiya']
    folder_name = 'horimiya2'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        # self.download_news()
        self.download_key_visual()
        # self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fr_j-0eWAAEq9Id?format=jpg&name=4096x4096')
        self.download_image_list(folder)



# Jidou Hanbaiki ni Umarekawatta Ore wa Meikyuu wo Samayou
class JihankiDownload(Summer2023AnimeDownload, NewsTemplate):
    title = 'Jidou Hanbaiki ni Umarekawatta Ore wa Meikyuu wo Samayou'
    keywords = [title, "jihanki", 'Reborn as a Vending Machine, I Now Wander the Dungeon']
    website = 'https://jihanki-anime.com/'
    twitter = 'jihanki_anime'
    hashtags = ['jihanki', '俺自販機']
    folder_name = 'jihanki'

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
        news_url = 'https://up-info.news/jihanki-anime/'
        self.download_template_news(page_prefix=news_url, article_select='.modListNews li', title_select='h3',
                                    date_select='time', id_select='a', date_separator='/', news_prefix='')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FqhSbfPaYAIYg4i?format=jpg&name=4096x4096')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            divs = soup.select('.l-jihanki-kv__inner>div[class]')
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
                    image_url = self.PAGE_PREFIX + image['src'].replace('./', '')
                    if '/img/' not in image_url:
                        continue
                    image_name = self.generate_image_name_from_url(image_url, 'img')
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/img/chara/img_chara%s.png'
        self.download_by_template(folder, template, 1, 1)


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
        self.add_to_image_list('kv', self.PAGE_PREFIX + 'common/media/24d9f99eea98f74d6add5b03db11dcd9.jpg')
        self.download_image_list(folder)

        prefix = self.PAGE_PREFIX + 'common/images/contents_top_fv_stand%s'
        templates = [prefix + '.jpg', prefix + 'b.jpg']
        self.download_by_template(folder, templates, 2, 1, prefix='tz_')

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'common/images/contents_character_'
        prefix2 = self.PAGE_PREFIX + 'common/images/contents_character02_'
        prefix3 = self.PAGE_PREFIX + 'common/images/contents_character03_'
        templates = [prefix + 'stand%s.png', prefix + 'face%s.png']
        templates2 = [prefix2 + 'stand%s.png', prefix2 + 'face%s.png']
        templates3 = [prefix3 + 'stand%s.png', prefix3 + 'face%s.png']
        self.download_by_template(folder, templates, 2, 1)
        self.download_by_template(folder, templates2, 2, 1)
        self.download_by_template(folder, templates3, 2, 1)


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
        # self.image_list = []
        # self.add_to_image_list('tz_kv', self.PAGE_PREFIX + '_assets/images/fv/fv@2x.png')
        # self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.fv--img__slider source[srcset]')
            for image in images:
                image_url = image['srcset']
                if '_sp' in image_url:
                    continue
                if image_url.startswith('/'):
                    image_url = self.PAGE_PREFIX + image_url[1:]
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

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


# Nanatsu no Maken ga Shihai suru
class NanatsumaDownload(Summer2023AnimeDownload, NewsTemplate):
    title = 'Nanatsu no Maken ga Shihai suru'
    keywords = [title, 'Reign of the Seven Spellblades']
    website = 'https://nanatsuma-pr.com/'
    twitter = 'nanatsuma_pr'
    hashtags = ['nanatsuma', 'ななつま']
    folder_name = 'nanatsuma'

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
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/FqyTIkYaAAUAKWT?format=jpg&name=large')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            divs = soup.select('main div[class]')
            for div in divs:
                has_visual_class = False
                for _class in div['class']:
                    if 'visual' in _class.lower():
                        has_visual_class = True
                        break
                if not has_visual_class:
                    continue
                images = div.select('picture *[srcset]')
                for image in images:
                    image_url = self.PAGE_PREFIX + image['srcset'][1:]
                    if '/static/' not in image_url:
                        continue
                    image_name = self.generate_image_name_from_url(image_url, 'static')
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'wp/wp-content/themes/ssd/static/character/'
        for i in range(30):
            num = str(i + 1).zfill(2)
            if self.is_image_exists(num + '_full', folder) and self.is_image_exists(num + '_close_01', folder):
                continue
            chara_prefix = prefix + num + '/'
            full_name = num + '_full'
            result = self.download_image(chara_prefix + 'full.png', folder + '/' + full_name)
            if result == -1:
                break
            template = chara_prefix + 'close/%s.png'
            for j in range(3):
                close_url = template % str(j + 1).zfill(2)
                close_name = num + '_close_' + str(j + 1).zfill(2)
                result2 = self.download_image(close_url, folder + '/' + close_name)
                if result2 == -1:
                    break


# Okashi na Tensei
class OkashinaTenseiDownload(Summer2023AnimeDownload, NewsTemplate4):
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
        self.download_template_news('okashinatensei')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        # self.image_list = []
        # self.add_to_image_list('tz_natalie', 'https://ogre.natalie.mu/media/news/comic/2022/1215/okashinatensei_teaser.jpg')
        # self.download_image_list(folder)

        static_url = self.PAGE_PREFIX + 'wp/wp-content/themes/okashinatensei/static/'
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            scripts = soup.select('script[src*="pages/index-"]')
            if len(scripts) > 0:
                js_url = scripts[0]['src']
                if js_url.startswith('/'):
                    js_url = self.PAGE_PREFIX + js_url[1:]
                js_page = self.get_response(js_url)
                split1 = js_page.split('"mainvisual/')
                self.image_list = []
                for i in range(1, len(split1), 1):
                    s = split1[i].split('"')[0]
                    if len(s) == 0 or not s.endswith('.webp') or s == 'copy.webp' or 'switch_icon' in s:
                        continue
                    image_url = static_url + 'mainvisual/' + s
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

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


# Ryza no Atelier: Tokoyami no Joou to Himitsu no Kakurega
class AtelierRyzaDownload(Summer2023AnimeDownload, NewsTemplate):
    title = 'Ryza no Atelier: Tokoyami no Joou to Himitsu no Kakurega'
    keywords = [title, 'Atelier Ryza: Ever Darkness & the Secret Hideout']
    website = 'https://ar-anime.com/'
    twitter = 'Ryza_PR'
    hashtags = 'ライザのアトリエ'
    folder_name = 'atelier-ryza'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.p-news_in__content-list-item',
                                    date_select='.p-in-data', title_select='.p-in-title',
                                    id_select='a', a_tag_start_text_to_remove='/', a_tag_prefix=self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'news/SYS/CONTENTS/afaf78fb-2da9-4a38-85e8-36282052d381')
        self.add_to_image_list('kv', self.PAGE_PREFIX + 'assets/img/top/kv.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        self.download_by_template(folder, self.PAGE_PREFIX + 'assets/img/character/chara_%s.png', 2, 1)


# Seija Musou: Salaryman, Isekai de Ikinokoru Tame ni Ayumu Michi
class SeijaMusouDownload(Summer2023AnimeDownload, NewsTemplate):
    title = 'Seija Musou: Salaryman, Isekai de Ikinokoru Tame ni Ayumu Michi'
    keywords = [title, 'The Great Cleric']
    website = 'https://www.tbs.co.jp/anime/seija/'
    twitter = 'seija_anime'
    hashtags = '聖者無双'
    folder_name = 'seijamusou'

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
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsall-box',
                                    date_select='.newsall-date', title_select='.newsall-text',
                                    id_select='a', a_tag_prefix=news_url)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FpJpjE6acAEXVFF?format=jpg&name=large')
        self.add_to_image_list('kv_tw', 'https://pbs.twimg.com/media/FwUYw_PaMAA8jF0?format=jpg&name=4096x4096')
        self.add_to_image_list('topimg_key@2x', self.PAGE_PREFIX + 'img/topimg_key@2x.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'img/chara_img_%s@2x.png'
        self.download_by_template(folder, template, 2, 1)


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


# Suki na Ko ga Megane wo Wasureta
class SukimegaDownload(Summer2023AnimeDownload, NewsTemplate):
    title = 'Suki na Ko ga Megane wo Wasureta'
    keywrods = [title, 'The Girl I Like Forgot Her Glasses']
    website = 'https://anime.shochiku.co.jp/sukimega/'
    twitter = 'Sukimega'
    hashtags = '好きめが'
    folder_name = 'sukimega'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='section .list_item',
                                    date_select='.date', title_select='.title', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv_tw', 'https://pbs.twimg.com/media/FrLPIEiakAA_j0O?format=jpg&name=4096x4096')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.skmg_top_fv_kv_box_item_image img[src]')
            self.image_list = []
            self.image_list = []
            for image in images:
                image_url = image['src']
                if '/images/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'images')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e)


# Temple
class TempleDownload(Summer2023AnimeDownload, NewsTemplate):
    title = 'Temple'
    keywords = [title, 'TenPuru: No One Can Live on Loneliness']
    website = 'https://temple-anime.com/'
    twitter = 'temple_tvanime'
    hashtags = ['てんぷる', 'Tenpuru_anime']
    folder_name = 'temple'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, news_prefix='', article_select='#news article',
                                    date_select='time', title_select='h3', id_select=None, id_has_id=True)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/FmrextbacAMbNvi?format=jpg&name=large')
        self.add_to_image_list('mainimg', self.PAGE_PREFIX + 'images/mainimg.jpg')
        self.add_to_image_list('img_story', self.PAGE_PREFIX + 'images/img_story.jpg')
        self.download_image_list(folder)

        image_prefix = self.PAGE_PREFIX + 'assets/'
        css_url = image_prefix + 'css/style.min.css'
        try:
            self.image_list = []
            css_page = self.get_response(css_url)
            search_text = '.mainimg{background:url('
            split1 = css_page.split(search_text)
            for i in range(1, len(split1), 1):
                right_idx = split1[i].find(')')
                if right_idx > 0:
                    image_url = split1[i][0:right_idx]
                    if image_url.startswith('../'):
                        image_url = image_prefix + image_url[3:]
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')


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


# Uchi no Kaisha no Chiisai Senpai no Hanashi
class ChiisaiSenpaiDownload(Summer2023AnimeDownload, NewsTemplate):
    title = 'Uchi no Kaisha no Chiisai Senpai no Hanashi'
    keywords = [title]
    website = 'https://chiisaisenpai.com/'
    twitter = 'smallsenpai_pr'
    hashtags = 'うちの会社の小さい先輩の話'
    folder_name = 'chiisaisenpai'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, date_separator='-',
                                    article_select='.jet-listing-grid__item[data-post-id]',
                                    date_select='.elementor-heading-title', title_select='a', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        css_prefix = self.PAGE_PREFIX + 'wp-content/uploads/elementor/css/post-'
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            elements = soup.select('#tpca_front_page .plus-slide-content .elementor[data-elementor-id]')
            for element in elements:
                element_id = element['data-elementor-id']
                css_response = self.get_response(css_prefix + element_id + '.css', decode=True)
                split1 = css_response.split('background-image:url("')
                image_urls = []
                for i in range(1, len(split1), 1):
                    image_urls.append(split1[i].split('"')[0].replace('-scaled', ''))
                for image_url in image_urls:
                    if not image_url.startswith(self.PAGE_PREFIX):
                        continue
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

        # self.image_list = []
        # self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FrY-UPcaAAAxGJO?format=jpg&name=medium')
        # self.add_to_image_list('PC-フロントビュー-1', self.PAGE_PREFIX + 'wp-content/uploads/2023/03/PC-フロントビュー-1.jpg')
        # self.add_to_image_list('SP-フロントビュー-1', self.PAGE_PREFIX + 'wp-content/uploads/2023/03/SP-フロントビュー-1.jpg')
        # self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('#character img[src]')
            for image in images:
                image_url = self.clear_resize_in_url(image['src'])
                image_name = self.extract_image_name_from_url(image_url)
                if image_name.startswith('cv'):
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Yumemiru Danshi wa Genjitsushugisha
class YumemiruDanshiDownload(Summer2023AnimeDownload, NewsTemplate):
    title = 'Yumemiru Danshi wa Genjitsushugisha'
    keywords = [title]
    website = 'https://yumemirudanshi.com/'
    twitter = 'yumemiru_anime'
    hashtags = '夢見る男子'
    folder_name = 'yumemirudanshi'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-list a',
                                    date_select='.news-list-item__date', title_select='.news-list-item__title',
                                    id_select=None, a_tag_start_text_to_remove='/', a_tag_prefix=self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.home-visual__visual img[src]')
            for image in images:
                if '/img/' in image['src']:
                    image_url = self.PAGE_PREFIX + image['src'].split('?')[0].replace('./', '')
                    image_name = self.generate_image_name_from_url(image_url, 'img')
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

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
