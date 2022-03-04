from anime.main_download import MainDownload, NewsTemplate


# Kyokou Suiri S2 https://kyokousuiri.jp/ #虚構推理 @kyokou_suiri


# Fall 2022 Anime
class Fall2022AnimeDownload(MainDownload):
    season = "2022-4"
    season_name = "Fall 2022"
    folder_name = '2022-4'

    def __init__(self):
        super().__init__()


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
