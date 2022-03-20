import requests
from anime.main_download import MainDownload, NewsTemplate


# Hataraku Maou-sama!! https://maousama.jp/ #maousama @anime_maousama
# Kanojo, Okarishimasu 2nd Season https://kanokari-official.com/ #かのかり #kanokari @kanokari_anime
# Kinsou no Vermeil: Gakeppuchi Majutsushi wa Saikyou no Yakusai to Mahou Sekai wo Tsukisusumu #ヴェルメイユ #vermeil @vermeil_animePR
# Shadows House 2nd Season https://shadowshouse-anime.com/
# Soredemo Ayumu wa Yosetekuru https://soreayu.com/ #それあゆ @soreayu_staff
# Tensei Kenja no Isekai Life: Dai-2 no Shokugyou wo Ete, Sekai Saikyou ni Narimashita https://tenseikenja.com #転生賢者 @tenseikenja_PR
# Utawarerumono: Futari no Hakuoro https://utawarerumono.jp/ #うたわれ @UtawareAnime
# Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e S2 http://you-zitsu.com/ #you_zitsu #よう実 @youkosozitsu


# Summer 2022 Anime
class Summer2022AnimeDownload(MainDownload):
    season = "2022-3"
    season_name = "Summer 2022"
    folder_name = '2022-3'

    def __init__(self):
        super().__init__()


# Hataraku Maou-sama!!
class HatarakuMaousama2Download(Summer2022AnimeDownload, NewsTemplate):
    title = 'Hataraku Maou-sama!!'
    keywords = [title, 'Maousama', 'The Devil is a Part-Timer!', '2nd']
    website = 'https://maousama.jp/'
    twitter = 'anime_maousama'
    hashtags = 'maousama'
    folder_name = 'hataraku-maousama2'

    PAGE_PREFIX = website

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
        self.add_to_image_list('teaser_tw', 'https://pbs.twimg.com/media/EvyqsA_UcAcPT9B?format=jpg&name=large')
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'assets/img/top/visual.jpg')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/FGaCXWqVUAA4-Iz?format=jpg&name=large')
        self.add_to_image_list('kv1_moca', 'https://moca-news.net/article/20211212/2021121221300a_/image/001-aiic5e.jpg', is_mocanews=True)
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'assets/img/top/visual%s.jpg'
        self.download_by_template(folder, template, 2, 1)

    def download_character(self):
        folder = self.create_character_directory()
        character_prefix = self.PAGE_PREFIX + 'assets/img/character/'
        template1 = character_prefix + 'character%s_main.png'
        template2 = character_prefix + 'character%s_face1.png'
        template3 = character_prefix + 'character%s_face2.png'
        self.download_by_template(folder, [template1, template2, template3], 2, 1)


# Kanojo, Okarishimasu 2nd Season
class Kanokari2Download(Summer2022AnimeDownload, NewsTemplate):
    title = "Kanojo, Okarishimasu 2nd Season"
    keywords = [title, "Kanokari", "Rent-a-Girlfriend"]
    website = 'https://kanokari-official.com/'
    twitter = 'kanokari_anime'
    hashtags = ['彼女お借りします', 'かのかり', 'kanokari']
    folder_name = 'kanokari2'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        soup = self.get_soup(self.PAGE_PREFIX)
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual(soup)
        self.download_character(soup)

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.md-li__news--block',
                                    title_select='h3', date_select='time', id_select='a', stop_date='2021.02.26',
                                    paging_type=0, next_page_select='ul.pagenation-list li', next_page_eval_index=-1,
                                    next_page_eval_index_class='is__current')

    def download_key_visual(self, soup=None):
        folder = self.create_key_visual_directory()
        # self.image_list = []
        # self.add_to_image_list('tz', self.PAGE_PREFIX + '2nd/wp-content/themes/kanokari-2nd/_assets/images/fv/fv_pc.jpg')

        try:
            if soup is None:
                soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.visual img[src]')
            self.image_list = []
            for image in images:
                image_url = image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

        characters = ['chizuru', 'mami', 'ruka', 'sumi']
        for chara in characters:
            image_url = f'{self.PAGE_PREFIX}2nd/wp-content/themes/kanokari-2nd/_assets/images/loader/{chara}_pc.png'
            image_name = f'loader_{chara}'
            self.add_to_image_list(image_name, image_url)
        self.download_image_list(folder)

        self.download_youtube_thumbnails(self.PAGE_PREFIX, folder)

    def download_character(self, soup=None):
        folder = self.create_character_directory()
        try:
            if soup is None:
                soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.chardata--inner img[src]')
            self.image_list = []
            for image in images:
                image_url = image['src']
                image_name = 'tz_' + self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Kinsou no Vermeil: Gakeppuchi Majutsushi wa Saikyou no Yakusai to Mahou Sekai wo Tsukisusumu
class VermeilDownload(Summer2022AnimeDownload):
    title = 'Kinsou no Vermeil: Gakeppuchi Majutsushi wa Saikyou no Yakusai to Mahou Sekai wo Tsukisusumu'
    keywords = [title, 'Vermeil in Gold']
    website = 'https://vermeilingold.jp/'
    twitter = 'vermeil_animePR'
    hashtags = ['ヴェルメイユ', 'vermeil']
    folder_name = 'vermeil'

    PAGE_PREFIX = website

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
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FNdPFJ6VgAA2C0l?format=jpg&name=4096x4096')
        self.add_to_image_list('tz_tmp_img_off', self.PAGE_PREFIX + 'images/tmp_img_off.png')
        self.add_to_image_list('tz_tmp_img_on', self.PAGE_PREFIX + 'images/tmp_img_on.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'images/pre_h%s.png'
        self.download_by_template(folder, template, 2, 1)


# Shadows House 2nd Season
class ShadowsHouse2Download(Summer2022AnimeDownload):
    title = "Shadows House 2nd Season"
    keywords = [title]
    website = 'https://shadowshouse-anime.com/'
    twitter = 'shadowshouse_yj'
    hashtags = 'シャドーハウス'
    folder_name = 'shadows-house2'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        # self.add_to_image_list('tz_modal', self.PAGE_PREFIX + 'assets/img/kv_modal.png')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FIT7cvQaUAUw-RP?format=jpg&name=large')
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'assets/img/main_00.jpg')
        self.download_image_list(folder)


# Soredemo Ayumu wa Yosetekuru
class SoreayuDownload(Summer2022AnimeDownload, NewsTemplate):
    title = "Soredemo Ayumu wa Yosetekuru"
    keywords = [title, "Soreayu"]
    website = 'https://soreayu.com/'
    twitter = 'soreayu_staff'
    hashtags = 'それあゆ'
    folder_name = 'soreayu'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='div.news-page-news',
                                    date_select='div.date-label span', title_select='div.page-link h2',
                                    id_select='div.nullclass')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', self.PAGE_PREFIX + '_nuxt/img/key_visual.7d7640c.jpg')
        self.add_to_image_list('teaser_big', 'https://firebasestorage.googleapis.com/v0/b/pj-ayumu.appspot.com/o/articles%2F1625582107153?alt=media&token=2561cd21-5081-471b-9019-11f379fff1f7')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character')
            links = soup.select('link')
            if len(links) == 0:
                return
            js_file = self.PAGE_PREFIX + links[-1]['href'][1:]
            r = requests.get(js_file)
            r.raise_for_status()
            results = r.content.decode().split('"img/')
            self.image_list = []
            for i in range(len(results)):
                if i == 0:
                    continue
                image_name_with_extension = results[i].split('"')[0]
                if '_full' in image_name_with_extension or '_expression' in image_name_with_extension:
                    image_url = self.PAGE_PREFIX + '_nuxt/img/' + image_name_with_extension
                    image_name = self.extract_image_name_from_url(image_name_with_extension)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Tensei Kenja no Isekai Life: Dai-2 no Shokugyou wo Ete, Sekai Saikyou ni Narimashita
class TenseiKenjaDownload(Summer2022AnimeDownload, NewsTemplate):
    title = 'Tensei Kenja no Isekai Life: Dai-2 no Shokugyou wo Ete, Sekai Saikyou ni Narimashita'
    keywords = [title, 'tenseikenja', 'My Isekai Life']
    website = 'https://tenseikenja.com/'
    twitter = 'tenseikenja_PR'
    hashtags = '転生賢者'
    folder_name = 'tenseikenja'

    PAGE_PREFIX = website

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_news(self):
        # May need change paging logic
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='div.sw-News_Archive li',
                                    date_select='.date', title_select='.title p', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/E_cSGeTVQAIKvu2?format=jpg&name=medium')
        self.add_to_image_list('kv1_aniverse', 'https://aniverse-mag.com/wp-content/uploads/2022/01/396ee90ad1118539e82a6b4caab11c11.jpg')
        # self.add_to_image_list('img_kv_teaser', self.PAGE_PREFIX + 'wp/wp-content/themes/tenseikenja/assets/images/common/index/img_kv_teaser.jpg')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('div.visual-Content img')
            self.image_list = []
            for image in images:
                if image.has_attr('src'):
                    image_url = image['src'].split('?')[0]
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            chara_list = soup.select('div.character-Index li a')
            self.image_list = []
            template = self.PAGE_PREFIX + 'wp/wp-content/themes/tenseikenja/assets/images/common/character/%s/img.png'
            for chara in chara_list:
                if chara.has_attr('href'):
                    href = chara['href']
                    if href.endswith('/'):
                        href = href[0:len(href)-1]
                    chara_name = href.split('/')[-1]
                    if len(chara_name) > 1:
                        self.add_to_image_list(f'img_{chara_name}', template % chara_name)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Utawarerumono: Futari no Hakuoro
class Utawarerumono3Download(Summer2022AnimeDownload, NewsTemplate):
    title = 'Utawarerumono: Futari no Hakuoro'
    keywords = [title, 'Utawarerumono: Mask of Truth', '3rd']
    website = 'https://utawarerumono.jp/'
    twitter = 'UtawareAnime'
    hashtags = 'うたわれ'
    folder_name = 'utawarerumono3'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.md-list__article--li',
                                    title_select='h4', date_select='dt', id_select='a', news_prefix='topics/',)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FE9Ma5NaAAABavo?format=jpg&name=4096x4096')
        self.add_to_image_list('fv@2x', self.PAGE_PREFIX + 'manage/wp-content/themes/hakuoro/_assets/images/fv/fv@2x.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'manage/wp-content/themes/hakuoro/_assets/images/char/detail/char%s_pc.png'
        self.download_by_template(folder, template, 2, 1)


# Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e S2
class Youzitsu2Download(Summer2022AnimeDownload, NewsTemplate):
    title = "Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e 2nd Season"
    keywords = ["Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e", "Youzitsu", "Youjitsu",
                "Classroom of the Elite"]
    website = 'http://you-zitsu.com/'
    twitter = 'youkosozitsu'
    hashtags = ['you_zitsu', 'よう実', 'ClassroomOfTheElite']
    folder_name = 'youzitsu2'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.content-entry',
                                    title_select='h2.entry-title span', date_select='div.entry-date span',
                                    id_select=None, id_has_id=True, news_prefix='news.html')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        top_template_prefix = self.PAGE_PREFIX + 'assets/top/t%s/vis.'
        news_template_prefix = self.PAGE_PREFIX + 'assets/news/vis-t%s.'

        top_templates = [top_template_prefix + 'jpg', top_template_prefix + 'png']
        news_templates = [news_template_prefix + 'jpg', news_template_prefix + 'png']

        self.download_by_template(folder, news_templates, 1, 1, prefix='news_')

        try:
            for i in range(1, 11, 1):
                is_success = False
                for top_template in top_templates:
                    image_url = top_template % str(i)
                    image_name = 'top_vis-t' + str(i)
                    result = self.download_image(image_url, folder + '/' + image_name)
                    if result != -1:
                        is_success = True
                        break
                if not is_success:
                    break
        except Exception as e:
            self.print_exception(e, 'Key Visual')

