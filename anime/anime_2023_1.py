from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2


# Ayakashi Triangle https://ayakashitriangle-anime.com/ #あやかしトライアングル #あやトラ @ayakashi_anime
# Benriya Saitou-san, Isekai ni Iku https://saitou-anime.com/ #便利屋斎藤さん @saitou_anime
# Eiyuuou, Bu wo Kiwameru Tame Tenseisu: Soshite, Sekai Saikyou no Minarai Kishi https://auo-anime.com/ #英雄王 @auo_anime
# Hyouken no Majutsushi ga Sekai wo Suberu http://www.tbs.co.jp/anime/hyouken/ #冰剣の魔術師 #hyouken @hyouken_pr
# Ijiranaide, Nagatoro-san 2nd Attack https://www.nagatorosan.jp/ #長瀞さん @nagatoro_tv
# Inu ni Nattara Suki na Hito ni Hirowareta. https://inuhiro-anime.com/ #犬ひろ @inuninattara
# Isekai Nonbiri Nouka https://nonbiri-nouka.com/ #のんびり農家 @nonbiri_nouka
# Kubo-san wa Mob wo Yurusanai https://kubosan-anime.jp/ #久保さん @kubosan_anime
# Kyokou Suiri S2 https://kyokousuiri.jp/ #虚構推理 @kyokou_suiri
# Oniichan wa Oshimai! https://onimai.jp/ #おにまい @onimai_anime
# Rougo ni Sonaete Isekai de 8-manmai no Kinka wo Tamemasu https://roukin8-anime.com/ #ろうきん8 #roukin8 @roukin8_anime
# Saikyou Onmyouji no Isekai Tenseiki https://saikyo-onmyouji.asmik-ace.co.jp/ #最強陰陽師 @saikyo_onmyouji
# Tomo-chan wa Onnanoko! https://tomo-chan.jp/ #tomochan @tomo_chan_ani
# Tsundere Akuyaku Reijou Liselotte to Jikkyou no Endou-kun to Kaisetsu no Kobayashi-san http://tsunlise-pr.com/ #ツンリゼ @tsunlise_pr


# Winter 2023 Anime
class Winter2023AnimeDownload(MainDownload):
    season = "2023-1"
    season_name = "Winter 2023"
    folder_name = '2023-1'

    def __init__(self):
        super().__init__()


# Ayakashi Triangle
class AyakashiTriangleDownload(Winter2023AnimeDownload, NewsTemplate):
    title = 'Ayakashi Triangle'
    keywords = [title]
    website = 'https://ayakashitriangle-anime.com/'
    twitter = 'ayakashi_anime'
    hashtags = ['あやトラ', 'あやかしトライアングル']
    folder_name = 'ayakashi-triangle'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.p-news__list-item',
                                    date_select='.p-news_data__date', title_select='.p-news_data__title',
                                    id_select='a', a_tag_start_text_to_remove='/', paging_type=1,
                                    a_tag_prefix=self.PAGE_PREFIX,
                                    next_page_select='div.c-pagination__link.-next',
                                    next_page_eval_index_class='is-disable', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        # self.add_to_image_list('announce_tw', 'https://pbs.twimg.com/media/FG33dXJagAY1HcQ?format=jpg&name=medium')
        self.add_to_image_list('announce_aniverse', 'https://aniverse-mag.com/wp-content/uploads/2021/12/img_kokuchi.jpg')
        self.add_to_image_list('announce', self.PAGE_PREFIX + 'assets/img/img_kv.png')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.p-hero_kv__visual-img img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'][1:]
                image_name = self.generate_image_name_from_url(image_url, 'img')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/img/chara/chara_%s.png'
        self.image_list = []
        self.add_to_image_list('chara01-1', template % '01-1')
        self.add_to_image_list('chara01-2', template % '01-2')
        self.download_image_list(folder)
        self.download_by_template(folder, template, 2, 2)

        # Face
        for i in range(20):
            if self.is_image_exists(f'/face_{str(i + 1).zfill(2)}-1', folder):
                continue
            face_template = self.PAGE_PREFIX + f'assets/img/chara/face_{str(i + 1).zfill(2)}-%s.jpg'
            success = self.download_by_template(folder, face_template, 1, 1)
            if not success:
                break


# Benriya Saitou-san, Isekai ni Iku
class BenriyaSaitouDownload(Winter2023AnimeDownload, NewsTemplate2):
    title = 'Benriya Saitou-san, Isekai ni Iku'
    keywords = [title, 'Handyman Saitou in Another World']
    website = 'https://saitou-anime.com/'
    twitter = 'saitou_anime'
    hashtags = '便利屋斎藤さん'
    folder_name = 'benriya-saitou'

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
        self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'core_sys/images/news/00000003/block/00000008/00000001.jpg')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FYMHT1jVUAAUtmQ?format=jpg&name=medium')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'core_sys/images/main/tz/chara/chara_%s'
        templates = [prefix + '.png', prefix + '_face.png']
        self.download_by_template(folder, templates, 2, 1, prefix='tz_')


# Eiyuuou, Bu wo Kiwameru Tame Tenseisu: Soshite, Sekai Saikyou no Minarai Kishi
class EiyuuouDownload(Winter2023AnimeDownload, NewsTemplate):
    title = 'Eiyuuou, Bu wo Kiwameru Tame Tenseisu: Soshite, Sekai Saikyou no Minarai Kishi'
    keywords = [title]
    website = 'https://auo-anime.com/'
    twitter = 'auo_anime'
    hashtags = '英雄王'
    folder_name = 'eiyuuou'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.news-item',
                                    date_select='p.date', title_select='p.title', id_select='a',
                                    next_page_select='div.pagination a.next',
                                    next_page_eval_index_class='off', next_page_eval_index=0)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'wp/wp-content/themes/euo-teaser-theme/img/kv.jpg')
        # self.add_to_image_list('tz_news', self.PAGE_PREFIX + 'wp/wp-content/uploads/2022/02/英雄王_ティザービジュアル.jpg')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FNYCWh2VgAM1rSE?format=jpg&name=large')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/euo-teaser-theme/img/chara-pic%s.png'
        self.download_by_template(folder, template, 1, 1, prefix='tz_')


# Hyouken no Majutsushi ga Sekai wo Suberu
class HyoukenDownload(Winter2023AnimeDownload, NewsTemplate):
    title = 'Hyouken no Majutsushi ga Sekai wo Suberu'
    keywords = [title, 'The Iceblade Sorcerer Shall Rule the World']
    website = 'http://www.tbs.co.jp/anime/hyouken/'
    twitter = 'hyouken_pr'
    hashtags = ['冰剣の魔術師', 'hyouken']
    folder_name = 'hyouken'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        # self.download_media()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_episode_preview_temp(self):
        template = self.PAGE_PREFIX + 'story/img/story%s/%s.jpg'
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                continue
            for j in range(self.IMAGES_PER_EPISODE):
                image_url = template % (episode, str(j + 1).zfill(2))
                image_name = episode + '_' + str(j + 1)
                if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                    return

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsall-box',
                                    date_select='.newsall-date', title_select='a', id_select='a',
                                    a_tag_prefix=self.PAGE_PREFIX + 'news/')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.add_to_image_list('top_teaser_pc@2x', self.PAGE_PREFIX + 'img/top_teaser_pc@2x.jpg')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FdP3sZqagAIEGcr?format=jpg&name=large')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'character/img/chara_img_%s@2x.png'
        self.download_by_template(folder, template, 2, 1)

    def download_media(self):
        pass


# Ijiranaide, Nagatoro-san 2nd Attack
class Nagatorosan2Download(Winter2023AnimeDownload, NewsTemplate):
    title = 'Ijiranaide, Nagatoro-san 2nd Attack'
    keywords = [title, 'Nagatorosan', "Don't Toy with Me, Miss Nagatoro"]
    website = 'https://www.nagatorosan.jp/'
    twitter = 'nagatoro_tv'
    hashtags = '長瀞さん'
    folder_name = 'nagatorosan2'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        # self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser_img_mainimg', self.PAGE_PREFIX + 'teaser/img/mainimg.jpg')
        self.add_to_image_list('tz', 'https://pbs.twimg.com/media/FWeINYraUAEG6y9?format=jpg&name=medium')
        self.download_image_list(folder)


# Inu ni Nattara Suki na Hito ni Hirowareta.
class InuhiroDownload(Winter2023AnimeDownload, NewsTemplate):
    title = "Inu ni Nattara Suki na Hito ni Hirowareta."
    keywords = [title, 'Inuhiro']
    website = 'https://inuhiro-anime.com/'
    twitter = 'inuninattara'
    hashtags = '犬ひろ'
    folder_name = 'inuhiro'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='#news article',
                                    date_select='time', title_select='h3', id_select=None,
                                    id_has_id=True, news_prefix='')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FNybC1EaAAEoRmq?format=jpg&name=large')
        self.add_to_image_list('tz_mainimg_pc', self.PAGE_PREFIX + 'teaser/images/mainimg_pc.png')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/FZyBd0xVEAAz4kn?format=jpg&name=medium')
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'teaser/images/mainimg.jpg')
        self.download_image_list(folder)


# Isekai Nonbiri Nouka
class IsekaiNonbiriNoukaDownload(Winter2023AnimeDownload):
    title = 'Isekai Nonbiri Nouka'
    keywords = [title]
    website = 'https://nonbiri-nouka.com/'
    twitter = 'nonbiri_nouka'
    hashtags = 'のんびり農家'
    folder_name = 'nonbiri-nouka'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', 'https://ogre.natalie.mu/media/news/comic/2022/0826/nonbiri-nouka_Teaser.jpg')
        self.download_image_list(folder)


# Kubo-san wa Mob wo Yurusanai
class KubosanDownload(Winter2023AnimeDownload, NewsTemplate2):
    title = 'Kubo-san wa Mob wo Yurusanai'
    keywords = [title, "Kubo Won't Let Me Be Invisible"]
    website = 'https://kubosan-anime.jp/'
    twitter = 'kubosan_anime'
    hashtags = '久保さん'
    folder_name = 'kubosan'

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
        self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'core_sys/images/news/00000002/block/00000008/00000002.jpg')
        self.add_to_image_list('tz2', self.PAGE_PREFIX + 'core_sys/images/news/00000006/block/00000014/00000007.png')
        self.add_to_image_list('img_kv1', 'https://pbs.twimg.com/media/FXsiHJWaQAU3UsM?format=jpg&name=large')
        # self.add_to_image_list('img_kv2', 'https://pbs.twimg.com/media/Fcmcmk2acAAd4mc?format=jpg&name=large')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        self.add_to_image_list('tz_chara_kubo', self.PAGE_PREFIX + 'core_sys/images/main/tz/chara_kubo.png')
        self.add_to_image_list('tz_chara_shiraishi', self.PAGE_PREFIX + 'core_sys/images/main/tz/chara_shiraishi.png')
        self.download_image_list(folder)


# Kyokou Suiri S2
class KyokouSuiri2Download(Winter2023AnimeDownload, NewsTemplate):
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


# Oniichan wa Oshimai!
class OnimaiDownload(Winter2023AnimeDownload, NewsTemplate):
    title = 'Oniichan wa Oshimai!'
    keywords = [title, 'Onimai']
    website = 'https://onimai.jp/'
    twitter = 'onimai_anime'
    hashtags = 'おにまい'
    folder_name = 'onimai'

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
                                    date_select='.newsList__date', title_select='.newsList__title', id_select='a',
                                    a_tag_prefix=self.PAGE_PREFIX + 'news/', a_tag_start_text_to_remove='./')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('top_visual_mahiro', self.PAGE_PREFIX + 'assets/img/top/visual_mahiro.png')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FQ6O8FgVIAEp7rm?format=jpg&name=4096x4096')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        chara_url = self.PAGE_PREFIX + 'character/'
        try:
            soup = self.get_soup(chara_url)
            a_tags = soup.select('.characterList a[href]')
            for a_tag in a_tags:
                if not a_tag['href'].endswith('.html'):
                    continue
                page = a_tag['href'].split('/')[-1].split('.html')[0]
                if page in processed:
                    continue
                chara_soup = self.get_soup(chara_url + a_tag['href'].replace('./', ''))
                if chara_soup is None:
                    continue
                self.image_list = []
                images = chara_soup.select('.characterDetail_img img[src]')
                for image in images:
                    if '/character/' not in image['src']:
                        continue
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                    image_name = self.generate_image_name_from_url(image_url, 'character')
                    self.add_to_image_list(image_name, image_url)
                if len(self.image_list) > 0:
                    processed.append(page)
                self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Rougo ni Sonaete Isekai de 8-manmai no Kinka wo Tamemasu
class Roukin8Download(Winter2023AnimeDownload, NewsTemplate):
    title = 'Rougo ni Sonaete Isekai de 8-manmai no Kinka wo Tamemasu'
    keywords = [title, 'roukin8', 'Saving 80,000 Gold in Another World for My Retirement']
    website = 'https://roukin8-anime.com/'
    twitter = 'roukin8_anime'
    hashtags = ['roukin8', 'ろうきん8']
    folder_name = 'roukin8'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        # self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.bl_vertPosts_item',
                                    date_select='time', title_select='.bl_vertPosts_txt',
                                    id_select='.bl_vertPosts_link', a_tag_prefix=self.PAGE_PREFIX,
                                    a_tag_start_text_to_remove='../')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('top_kv', self.PAGE_PREFIX + 'assets/img/top/kv.jpg')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FZkU-3hagAAU3fg?format=jpg&name=medium')
        self.download_image_list(folder)


# Saikyou Onmyouji no Isekai Tenseiki
class SaikyoOnmyoujiDownload(Winter2023AnimeDownload, NewsTemplate):
    title = 'Saikyou Onmyouji no Isekai Tenseiki'
    keywords = [title]
    website = 'https://saikyo-onmyouji.asmik-ace.co.jp/'
    twitter = 'saikyo_onmyouji'
    hashtags = '最強陰陽師'
    folder_name = 'saikyo-onmyouji'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        # self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        pass

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('fv_fv_pc', self.PAGE_PREFIX + 'assets/images/fv/fv_pc.png')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FYj0CqraUAAQhht?format=jpg&name=4096x4096')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.chardata .v img[src]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'][1:]
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Tomo-chan wa Onnanoko!
class TomochanDownload(Winter2023AnimeDownload, NewsTemplate):
    title = 'Tomo-chan wa Onnanoko!'
    keywords = [title, 'tomochan', 'Tomo Is a Girl!']
    website = 'https://tomo-chan.jp/'
    twitter = 'tomo_chan_ani'
    hashtags = 'tomochan'
    folder_name = 'tomochan'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.p-news__list-item',
                                    date_select='.p-news__list-date', title_select='.p-news__list-ttl',
                                    id_select='a', a_tag_start_text_to_remove='./', paging_type=1,
                                    a_tag_prefix=self.PAGE_PREFIX + 'news/',
                                    next_page_select='.c-pagination__nav-button.-next')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FWw4blxagAEvI9K?format=jpg&name=medium')
        self.add_to_image_list('main_img_main-illust', self.PAGE_PREFIX + 'assets/t/img/main/img_main-illust.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/t/img/chara/img_chara%s.png'
        self.download_by_template(folder, template, 2, 1, prefix='tz_')


# Tsundere Akuyaku Reijou Liselotte to Jikkyou no Endou-kun to Kaisetsu no Kobayashi-san
class TsunliseDownload(Winter2023AnimeDownload, NewsTemplate):
    title = 'Tsundere Akuyaku Reijou Liselotte to Jikkyou no Endou-kun to Kaisetsu no Kobayashi-san'
    keywords = [title, 'tsunlise', 'Endo and Kobayashi Live! The Latest on Tsundere Villainess Lieselotte']
    website = 'https://tsunlise-pr.com/'
    twitter = 'tsunlise_pr'
    hashtags = 'ツンリゼ'
    folder_name = 'tsunlise'

    PAGE_PREFIX = website

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_news(self):
        # Paging logic need update
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-item',
                                    date_select='.date', title_select='.title', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv1_1', self.PAGE_PREFIX + 'wp/wp-content/uploads/2022/07/01_ツンリゼ_第1弾KV_ツンver..jpg')
        self.add_to_image_list('kv1_2', self.PAGE_PREFIX + 'wp/wp-content/uploads/2022/07/02_ツンリゼ_第1弾KV_デレver..jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/tunlise-teaser-theme/img/chara-pic%s.png'
        self.download_by_template(folder, template, 1, 1, prefix='tz_')
