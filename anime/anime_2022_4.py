from anime.main_download import MainDownload, NewsTemplate


# Akuyaku Reijou nanode Last Boss wo Kattemimashita https://akulas-pr.com/ #悪ラス @akulas_pr
# Kage no Jitsuryokusha ni Naritakute! https://shadow-garden.jp/ #陰の実力者 @Shadowgarden_PR
# Kyokou Suiri S2 https://kyokousuiri.jp/ #虚構推理 @kyokou_suiri
# Tensei shitara Ken Deshita https://tenken-anime.com/ #転生したら剣でした #転剣 @tenken_official
# Uchi no Shishou wa Shippo ga Nai https://shippona-anime.com/ #しっぽな @shippona_anime
# Yama no Susume: Next Summit https://yamanosusume-ns.com/ #ヤマノススメ @yamanosusume


# Fall 2022 Anime
class Fall2022AnimeDownload(MainDownload):
    season = "2022-4"
    season_name = "Fall 2022"
    folder_name = '2022-4'

    def __init__(self):
        super().__init__()


# Akuyaku Reijou nanode Last Boss wo Kattemimashita
class AkulasDownload(Fall2022AnimeDownload, NewsTemplate):
    title = 'Akuyaku Reijou nanode Last Boss wo Kattemimashita'
    keywords = [title, "I'm the Villainess, So I'm Taming the Final Boss", 'akulas']
    website = 'https://akulas-pr.com/'
    twitter = 'akulas_pr'
    hashtags = '悪ラス'
    folder_name = 'akulas'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.md-list__news li',
                                    title_select='h4', date_select='dt', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        aniverse_prefix = 'https://aniverse-mag.com/wp-content/uploads/2022/03/'
        teaser_prefix = self.PAGE_PREFIX + 'wp/wp-content/themes/akulas-teaser/_assets/images/fv/visual/'
        self.add_to_image_list('tz_aniverse_1', aniverse_prefix + '63a9443ca79764c441208e49969001b0.jpg')
        self.add_to_image_list('tz_aniverse_2', aniverse_prefix + '54e791dc7275325f19a662ad9bf0fad5.jpg')
        self.add_to_image_list('tz_fv_pc1', teaser_prefix + 'fv_pc1.png')
        self.add_to_image_list('tz_fv_pc2', teaser_prefix + 'fv_pc2.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/akulas-teaser/_assets/images/char/detail/char_%s_pc.png'
        self.download_by_template(folder, template, 3, 1, prefix='tz_')


# Kage no Jitsuryokusha ni Naritakute!
class KagenoJitsuryokushaDownload(Fall2022AnimeDownload, NewsTemplate):
    title = 'Kage no Jitsuryokusha ni Naritakute!'
    keywords = [title, 'The Eminence in Shadow']
    website = 'https://shadow-garden.jp/'
    twitter = 'Shadowgarden_PR'
    hashtags = '陰の実力者'
    folder_name = 'kagenojitsuryoku'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.newsList',
                                    date_select='time', title_select='p.newsList--ttl', id_select='a',
                                    a_tag_prefix=self.PAGE_PREFIX + 'news', a_tag_start_text_to_remove='./')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'news/img/20211027_03_1.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'assets/img/top/character/chara'
        self.download_by_template(folder, [prefix + '%s_main1.png', prefix + '%s_main2.png'], 2, 1)


# Kyokou Suiri S2
class KyokouSuiri2Download(Fall2022AnimeDownload, NewsTemplate):
    title = 'Kyokou Suiri Season 2'
    keywords = ['Kyokou Suiri', 'In/Spectre', '2nd']
    website = 'https://kyokousuiri.jp/'
    twitter = 'kyokou_suiri'
    hashtags = '虚構推理'
    folder_name = 'kyokou-suiri2'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ul.p-news__list li.p-news__list-item',
                                    date_select='div.p-article__header', title_select='div.p-article__text',
                                    id_select='a', date_separator=' ', stop_date='2021.03.17',
                                    next_page_select='div.c-pagination__nav.-next', next_page_eval_index=-1,
                                    next_page_eval_index_class='is-disable')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        image_prefix = self.PAGE_PREFIX + 'wp/wp-content/uploads/'
        self.add_to_image_list('tz', image_prefix + '2021/11/6271138d893814b7a21c84b078fca0b9.jpg')
        self.add_to_image_list('kv1', image_prefix + '2022/03/cefd7ddc49fafe239a53b1721361c61e.jpg')
        self.add_to_image_list('img_main_kv2', self.PAGE_PREFIX + 'assets_2t/img/top/main/img_main_kv2.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.p-chara_data__visual-img img.is-pc')
            for image in images:
                if image.has_attr('src') and image['src'].startswith('/'):
                    image_url = self.PAGE_PREFIX + image['src'][1:]
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Tensei shitara Ken Deshita
class TenkenDownload(Fall2022AnimeDownload, NewsTemplate):
    title = 'Tensei shitara Ken Deshita'
    keywords = [title, 'Reincarnated as a Sword', 'tenken']
    website = 'https://tenken-anime.com/'
    twitter = 'tenken_official'
    hashtags = ['転生したら剣でした', '転剣']
    folder_name = 'tenken'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.content-entry',
                                    title_select='h2.entry-title span', date_select='div.entry-date',
                                    id_select=None, id_has_id=True, news_prefix='news.html',
                                    date_func=lambda x: x[0:4] + '.' + x[4:])

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/FOcR3ESaMAIIZAo?format=jpg&name=4096x4096')
        self.add_to_image_list('kv1_vis', self.PAGE_PREFIX + 'assets/top/vis.png')
        self.add_to_image_list('kv1_vis-t1', self.PAGE_PREFIX + 'assets/news/vis-t1.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template_prefix = self.PAGE_PREFIX + 'assets/character/'
        templates = [template_prefix + 'c%s.png', template_prefix + 'f%s.png']
        self.download_by_template(folder, templates, 1, 1, prefix='tz_')


# Uchi no Shishou wa Shippo ga Nai
class ShipponaDownload(Fall2022AnimeDownload, NewsTemplate):
    title = 'Uchi no Shishou wa Shippo ga Nai'
    keywords = [title, 'My Master Has No Tail', 'Shippona']
    website = 'https://shippona-anime.com/'
    twitter = 'shippona_anime'
    hashtags = 'しっぽな'
    folder_name = 'shippona'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='a.news-list-item',
                                    date_select='.news-list-item__date', title_select='.news-list-item__title',
                                    id_select=None, a_tag_start_text_to_remove='/', a_tag_prefix=self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_natalie', 'https://ogre.natalie.mu/media/news/comic/2022/0106/shippona_teaser.jpg')
        self.download_image_list(folder)

        template_prefix = self.PAGE_PREFIX + 'img/home/visual_%s.'
        templates = [template_prefix + 'jpg', template_prefix + 'png']
        self.download_by_template(folder, templates, 2, 1)

    def download_character(self):
        folder = self.create_character_directory()
        char_url = self.PAGE_PREFIX + 'character'
        json_url = char_url + '/chara_data.php'
        self.image_list = []
        try:
            json_obj = self.get_json(json_url)
            if 'charas' in json_obj and isinstance(json_obj['charas'], list):
                for chara in json_obj['charas']:
                    if 'images' in chara and 'visuals' in chara['images']\
                            and isinstance(chara['images']['visuals'], list):
                        for visual in chara['images']['visuals']:
                            if 'image' in visual:
                                image_url = char_url + visual['image'][1:].split('?')[0]
                                image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                                self.add_to_image_list(image_name, image_url)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)
        self.download_image_list(folder)


# Yama no Susume: Next Summit
class YamaNoSusume4Download(Fall2022AnimeDownload):
    title = 'Yama no Susume: Next Summit'
    keywords = [title, "Encouragement of Climb"]
    website = 'https://yamanosusume-ns.com/'
    twitter = 'yamanosusume'
    hashtags = 'ヤマノススメ'
    folder_name = 'yamanosusume4'

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
        news_url = self.PAGE_PREFIX
        try:
            soup = self.get_soup(news_url, decode=True)
            articles = soup.select('#nwu_001_t tr')
            news_obj = self.get_last_news_log_object()
            results = []
            for article in articles:
                tag_date = article.find('td', class_='day')
                tag_title = article.find('div', class_='title')
                a_tag = article.find('a')
                if tag_date and tag_title:
                    article_id = ''
                    if a_tag and a_tag.has_attr('href'):
                        article_id = self.PAGE_PREFIX + a_tag['href']
                    date = self.format_news_date(tag_date.text.strip().replace('/', '.'))
                    if len(date) == 0:
                        continue
                    title = tag_title.text.strip()
                    if news_obj and ((news_obj['id'] == article_id and news_obj['title'] == title)
                                     or date < news_obj['date']):
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
            self.print_exception(e, 'News')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.png')
        self.add_to_image_list('tz_kv2_kv', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv2/kv.jpg')
        self.add_to_image_list('tz_kv2_kv_tw', 'https://pbs.twimg.com/media/FQ6oxppakAEMP4C?format=jpg&name=4096x4096')
        self.download_image_list(folder)
