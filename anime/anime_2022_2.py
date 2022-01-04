import requests
from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2


# Aharen-san wa Hakarenai https://aharen-pr.com/ #阿波連さん @aharen_pr
# Honzuki S3 http://booklove-anime.jp/story/ #本好きの下剋上 @anime_booklove
# Kawaii dake ja Nai Shikimori-san https://shikimori-anime.com/ #式守さん @anime_shikimori
# Machikado Mazoku: 2-choume http://www.tbs.co.jp/anime/machikado/ #まちカドまぞく #MachikadoMazoku @machikado_staff
# Mahoutsukai Reimeiki https://www.tbs.co.jp/anime/reimeiki/ #魔法使い黎明期 @reimeiki_pr
# Otome Game Sekai wa Mob ni Kibishii Sekai desu https://mobseka.com/ #モブせか #mobseka @mobseka_anime
# Shijou Saikyou no Daimaou, Murabito A ni Tensei suru https://murabito-a-anime.com/ #村人Aに転生 @murabitoA_anime
# Shokei Shoujo no Virgin Road http://virgin-road.com/ #処刑少女 #shokei_anime @VirginroadAnime
# Spy x Family https://spy-family.net/ #SPY_FAMILY #スパイファミリー @spyfamily_anime
# Summertime Render https://summertime-anime.com/ #サマータイムレンダ #サマレン @summertime_PR
# Tate no Yuusha S2 http://shieldhero-anime.jp/ #shieldhero #盾の勇者の成り上がり @shieldheroanime
# Yuusha, Yamemasu https://yuuyame.com/ #yuuyame #勇やめ @yuuyame_anime


# Summer 2022 Anime
class Spring2022AnimeDownload(MainDownload):
    season = "2022-2"
    season_name = "Spring 2022"
    folder_name = '2022-2'

    def __init__(self):
        super().__init__()


# Aharen-san wa Hakarenai
class AharensanDownload(Spring2022AnimeDownload, NewsTemplate):
    title = 'Aharen-san wa Hakarenai'
    keywords = [title]
    website = 'https://aharen-pr.com/'
    twitter = 'aharen_pr'
    hashtags = '阿波連さん'
    folder_name = 'aharensan'

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
        # Paging logic might be wrong
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.md-news__li',
                                    date_select='time', title_select='h3', id_select='a', date_separator='.&nbsp;',
                                    next_page_select='ul.pagenation-list li',
                                    next_page_eval_index_class='is__current', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'wp/wp-content/themes/aharen-teaser/_assets/images/kv/kv_pc.jpg')
        # self.add_to_image_list('tz_2', self.PAGE_PREFIX + 'wp/wp-content/uploads/2021/07/阿波連さんははかれない_ティザービジュアル.jpg')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/E7ohr6yVIAEQI6z?format=jpg&name=large')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/FFqAiWPaAAA-7gz?format=jpg&name=large')
        # self.add_to_image_list('kv1', self.PAGE_PREFIX + 'wp/wp-content/uploads/2021/12/阿波連さん_第1弾KV.jpg')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'wp/wp-content/themes/aharen-teaser/_assets/images/kv/kv%s_pc.jpg'
        self.download_by_template(folder, template, 1, 2)


    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('picture.chardetail--img img')
            for image in images:
                if image.has_attr('src'):
                    image_url = image['src']
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.download_image_list(folder)


# Honzuki no Gekokujou: Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen 3rd Season
class Honzuki3Download(Spring2022AnimeDownload, NewsTemplate):
    title = "Honzuki no Gekokujou: Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen 3rd Season"
    keywords = [title, "Ascendance of a Bookworm"]
    website = 'http://booklove-anime.jp/'
    twitter = 'anime_booklove'
    hashtags = '本好きの下剋上'
    folder_name = 'honzuki3'

    PAGE_PREFIX = website
    FIRST_EPISODE = 27
    FINAL_EPISODE = 40

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_guess()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            box_stories = soup.select('#third div.box_story')
            for box_story in box_stories:
                if box_story.has_attr('class') and box_story['class'][0].startswith('storyNo'):
                    try:
                        episode = str(int(box_story['class'][0][7:].strip())).zfill(2)
                    except:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    images = box_story.select('ul.img_thum img')
                    self.image_list = []
                    for i in range(len(images)):
                        if images[i].has_attr('src'):
                            image_url = self.PAGE_PREFIX + images[i]['src'].split('?')[0].replace('../', '')
                            image_name = episode + '_' + str(i + 1)
                            self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ol.list_news li',
                                    date_select='time', title_select='p.ttl', id_select='a')

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'img/story/ep%s/img%s.jpg'
        try:
            for i in range(self.FIRST_EPISODE, self.FINAL_EPISODE + 1, 1):
                episode = str(i).zfill(2)
                if self.is_image_exists(episode + '_1'):
                    continue
                img_template = template % (episode, '%s')
                if not self.download_by_template(folder, img_template, 2, 1, end=6, prefix=episode + '_'):
                    break
        except Exception as e:
            self.print_exception(e, 'Guess')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'news/wp/wp-content/uploads/2021/08/「本好きの下剋上」ティザービジュアル（ロゴ入り）軽.jpg')
        self.download_image_list(folder)


# Kaguya-sama wa Kokurasetai: Ultra Romantic
class Kaguyasama3Download(Spring2022AnimeDownload, NewsTemplate):
    title = "Kaguya-sama wa Kokurasetai: Ultra Romantic"
    keywords = [title, "Kaguya", "Kaguyasama", "Kaguya-sama: Love is War 3rd Season"]
    website = 'https://kaguya.love/'
    twitter = 'anime_kaguya'
    hashtags = 'かぐや様'
    folder_name = 'kaguya-sama3'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.c-news_list__item',
                                    title_select='div.c-news_list__ttl', date_select='div.c-news_list__date',
                                    id_select='a', a_tag_prefix=news_url, paging_type=1, stop_date='2021.10.16',
                                    date_func=lambda x: x[0:4] + '.' + x[5:].replace('/', '.'),
                                    next_page_select='div.c-pagination__nav-button.-next',
                                    next_page_eval_index_class='is-disabled', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'assets/3rd/t/img/top/main/img_main.jpg')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FCKDRzxVkAAIwMv?format=jpg&name=4096x4096')
        self.download_image_list(folder)


# Kawaii dake ja Nai Shikimori-san
class ShikimorisanDownload(Spring2022AnimeDownload, NewsTemplate2):
    title = 'Kawaii dake ja Nai Shikimori-san'
    keywords = [title]
    website = 'https://shikimori-anime.com/'
    twitter = 'anime_shikimori'
    hashtags = '式守さん'
    folder_name = 'shikimorisan'

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
        self.download_template_news(self.PAGE_PREFIX, 'news/list00010000.html')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'core_sys/images/main/home/kv.jpg')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FAiftmBVIAASbjk?format=jpg&name=large')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'core_sys/images/main/home/kv%s.jpg'
        self.download_by_template(folder, template, 1, 2)

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        self.add_to_image_list('shikimori', self.PAGE_PREFIX + 'core_sys/images/main/cont/chara/shikimori.jpg')
        self.add_to_image_list('shikimori_face', self.PAGE_PREFIX + 'core_sys/images/main/cont/chara/shikimori_face.jpg')
        self.add_to_image_list('izumi', self.PAGE_PREFIX + 'core_sys/images/main/cont/chara/izumi.jpg')
        self.add_to_image_list('izumi_face', self.PAGE_PREFIX + 'core_sys/images/main/cont/chara/izumi_face.jpg')
        self.download_image_list(folder)


# Machikado Mazoku: 2-choume
class MachikadoMazoku2Download(Spring2022AnimeDownload, NewsTemplate):
    title = 'Machikado Mazoku: 2-choume'
    keywords = ["Machikado Mazoku", "The Demon Girl Next Door", "2nd"]
    website = 'http://www.tbs.co.jp/anime/machikado/'
    twitter = 'machikado_staff'
    hashtags = ['まちカドまぞく', 'MachikadoMazoku']
    folder_name = 'machikado-mazoku2'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ul.newslist li',
                                    date_select='time', title_select='p', id_select='a',
                                    a_tag_prefix=self.PAGE_PREFIX + 'news/')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/E__DujoVcAktN1i?format=jpg&name=large')
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'img/machikado_top_pc@2x.jpg')
        self.download_image_list(folder)


# Mahoutsukai Reimeiki
class ReimeikiDownload(Spring2022AnimeDownload, NewsTemplate):
    title = 'Mahoutsukai Reimeiki'
    keywords = [title, 'The Dawn of the Witch']
    website = 'https://www.tbs.co.jp/anime/reimeiki/'
    twitter = 'reimeiki_pr'
    hashtags = '魔法使い黎明期'
    folder_name = 'reimeiki'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='dl.update-box',
                                    date_select='.update-date', title_select='a', id_select='a',
                                    a_tag_prefix=self.PAGE_PREFIX + 'news/')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.add_to_image_list('tz', 'https://pbs.twimg.com/media/FCy4SbFVgBETtHo?format=jpg&name=large')
        self.add_to_image_list('teaser_visual_chara', self.PAGE_PREFIX + 'img/teaser_visual_chara.png')
        self.add_to_image_list('teaser_visual_chara_bg', self.PAGE_PREFIX + 'img/teaser_visual_chara.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'img/chara'
        templates = [prefix + '_%s_on.png', prefix + 'img_%s.jpg']
        self.download_by_template(folder, templates, 2, 1)


# Otome Game Sekai wa Mob ni Kibishii Sekai desu
class MobsekaDownload(Spring2022AnimeDownload, NewsTemplate):
    title = 'Otome Game Sekai wa Mob ni Kibishii Sekai desu'
    keywords = [title, 'Trapped in a Dating Sim: The World of Otome Games is Tough for Mobs', 'Mobseka', 'Mobuseka']
    website = 'https://mobseka.com/'
    twitter = 'mobseka_anime'
    hashtags = ['モブせか', 'mobseka']
    folder_name = 'mobseka'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, news_prefix='news.html', article_select='#news dl',
                                    title_select='a', date_select='dt', id_select='a', a_tag_prefix=self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FFBOuWKaMAQzQbY?format=jpg&name=large')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'img/top_mv_%s.jpg'
        self.download_by_template(folder, template, 2, 1)

    def download_character(self):
        folder = self.create_character_directory()
        body_template = self.PAGE_PREFIX + 'img/chara/illust_%s.png'
        face_template = self.PAGE_PREFIX + 'img/chara/face_%s.png'
        self.download_by_template(folder, [body_template, face_template], 2, 1)


# Shijou Saikyou no Daimaou, Murabito A ni Tensei suru
class MurabitoADownload(Spring2022AnimeDownload, NewsTemplate):
    title = 'Shijou Saikyou no Daimaou, Murabito A ni Tensei suru'
    keywords = [title, 'The Greatest Demon Lord Is Reborn as a Typical Nobody']
    website = 'https://murabito-a-anime.com/'
    twitter = 'murabitoA_anime'
    hashtags = '村人Aに転生'
    folder_name = 'murabito-a'

    PAGE_PREFIX = website

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        # Need update page logic
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ul.newsLists__list li',
                                    title_select='.newsLists__list--title', date_select='.f_roc', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        template = self.PAGE_PREFIX + 'assets/img/top/fv_visual%s.jpg'
        self.download_by_template(folder, template, 1, 1)

        self.image_list = []
        self.add_to_image_list('kv1_news', self.PAGE_PREFIX + 'news/wp-content/uploads/2021/12/211216_01.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'assets/img/character/character%s_'
        templates = [prefix + 'main.png', prefix + 'face1.jpg', prefix + 'face2.jpg', prefix + 'thumb.jpg']
        self.download_by_template(folder, templates, 1, 1)


# Shokei Shoujo no Virgin Road
class ShokeiShoujoDownload(Spring2022AnimeDownload, NewsTemplate):
    title = 'Shokei Shoujo no Virgin Road'
    keywords = [title, 'The Executioner and Her Way of Life']
    website = 'http://virgin-road.com/'
    twitter = 'VirginroadAnime'
    hashtags = ['shokei_anime', '処刑少女']
    folder_name = 'shokeishoujo'

    PAGE_PREFIX = website

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        # Paging logic need update
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='#list_07 dd',
                                    title_select='.title', date_select='.day', id_select='a', date_separator='/',
                                    a_tag_replace_from='../', a_tag_replace_to=self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.png')
        self.add_to_image_list('teaser_tw', 'https://pbs.twimg.com/media/EtDn9lYU0AAKje-?format=jpg&name=4096x4096')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/E6Ur9dWVIAEE3Ee?format=jpg&name=4096x4096')
        self.add_to_image_list('main_kv', 'https://pbs.twimg.com/media/FIP1l-HaMEAKxOE?format=jpg&name=4096x4096')
        self.download_image_list(folder)

        kv_template = self.PAGE_PREFIX + 'core_sys/images/main/tz/kv%s'
        kv_template1 = kv_template + '.jpg'
        kv_template2 = kv_template + '.png'
        self.download_by_template(folder, [kv_template1, kv_template2], 1, 1)

    def download_character(self):
        folder = self.create_character_directory()
        template1 = self.PAGE_PREFIX + 'core_sys/images/main/tz/char_%s.png'
        template2 = self.PAGE_PREFIX + 'core_sys/images/main/tz/char_%sface.png'
        self.download_by_template(folder, [template1, template2], 1, 1, prefix='tz_')

        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'chara/')
            a_tags = soup.select('#ContentsListUnit01 a')
            for a_tag in a_tags:
                if a_tag.has_attr('href'):
                    get_chara_soup = False
                    if a_tag['href'].endswith('.html'):
                        chara_name = a_tag['href'].split('/')[-1][:-5]
                        get_chara_soup = True
                    else:
                        chara_name = 'menou'
                    if chara_name in processed:
                        continue
                    if get_chara_soup:
                        chara_soup = self.get_soup(self.PAGE_PREFIX + a_tag['href'].replace('../', ''))
                    else:
                        chara_soup = soup
                    if chara_soup is not None:
                        images = chara_soup.select('.charWrap img')
                        self.image_list = []
                        for image in images:
                            if image.has_attr('src'):
                                image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                                image_name = self.extract_image_name_from_url(image_url)
                                self.add_to_image_list(image_name, image_url)
                        if len(self.image_list) > 0:
                            processed.append(chara_name)
                        self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Spy x Family
class SpyFamilyDownload(Spring2022AnimeDownload, NewsTemplate):
    title = 'Spy x Family'
    keywords = [title]
    website = 'https://spy-family.net/'
    twitter = 'spyfamily_anime'
    hashtags = ['SPY_FAMILY', 'スパイファミリー']
    folder_name = 'spy-family'

    PAGE_PREFIX = website

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index', diff=2)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.newsLists__item',
                                    date_select='time', title_select='.newsLists--title', id_select='a',
                                    paging_type=3, paging_suffix='?paged=%s', next_page_select='.wp-pagenavi *',
                                    next_page_eval_index_class='current', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz1', 'https://pbs.twimg.com/media/FDCUAXsagAArKcA?format=jpg&name=4096x4096')
        self.add_to_image_list('tz2', 'https://pbs.twimg.com/media/FDCUBF7akAEMcUM?format=jpg&name=4096x4096')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.charaImgLists__imgWrap img')
            self.image_list = []
            for image in images:
                if image.has_attr('src'):
                    image_url = self.PAGE_PREFIX + image['src'].replace('./', '')
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Summertime Render
class SummertimeRenderDownload(Spring2022AnimeDownload, NewsTemplate):
    title = 'Summertime Render'
    keywords = [title]
    website = 'https://summertime-anime.com/'
    twitter = 'summertime_PR'
    hashtags = ['サマータイムレンダ', 'サマレン']
    folder_name = 'summertime-render'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.md-article__li',
                                    date_select='time', title_select='h5', id_select='a',
                                    next_page_select='ul.pagenation-list li',
                                    next_page_eval_index_class='is__current', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        # self.add_to_image_list('tz', self.PAGE_PREFIX + 'wp/wp-content/themes/summertime-teaser/_assets/images/kv/kv_pc.jpg')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/E63h3z-VEAMtJYy?format=jpg&name=medium')
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'wp/wp-content/uploads/2021/11/サマータイムレンダ_KV1_logomini.jpg')
        # self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/FG8lGwpaMAc7Aj3?format=jpg&name=large')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'wp/wp-content/themes/summertime-teaser/_assets/images/kv/kv_%s_pc.png'
        self.download_by_template(folder, template, 3, 1)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.chardata--v--img img')
            self.image_list = []
            for image in images:
                if image.has_attr('src'):
                    image_url = image['src']
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Tate no Yuusha no Nariagari S2
class TateNoYuusha2Download(Spring2022AnimeDownload):
    title = "Tate no Yuusha no Nariagari 2nd Season"
    keywords = [title, "The Rising of the Shield Hero"]
    website = "http://shieldhero-anime.jp"
    twitter = 'shieldheroanime'
    hashtags = ['shieldhero', '盾の勇者の成り上がり']
    folder_name = 'tate-no-yuusha2'

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
        news_url = self.PAGE_PREFIX + '/news/'
        try:
            soup = self.get_soup(news_url, decode=True)
            articles = soup.select('article.p-newspage_item')
            news_obj = self.get_last_news_log_object()
            results = []
            for article in articles:
                tag_date = article.find('span', class_='a')
                tag_title = article.find('h2', class_='txt')
                if tag_date and tag_title and tag_title.has_attr('id'):
                    article_id = tag_title['id'].strip()
                    date = self.format_news_date(tag_date.text.strip())
                    if len(date) == 0:
                        continue
                    title = tag_title.text.strip()
                    if date.startswith('2019.08') or (news_obj
                                                      and (news_obj['id'] == article_id or date < news_obj['date'])):
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
        self.add_to_image_list('announce', 'https://pbs.twimg.com/media/EDag4MkUwAAQnf0?format=jpg&name=medium')
        self.add_to_image_list('kv1', 'https://pbs.twimg.com/media/EhHFvyVU4AA7cUw?format=jpg&name=large')
        self.add_to_image_list('mv_lg', self.PAGE_PREFIX + '/assets/img/2nd/mv_lg.jpg')
        self.download_image_list(folder)


# Yuusha, Yamemasu
class YuuyameDownload(Spring2022AnimeDownload, NewsTemplate):
    title = 'Yuusha, Yamemasu'
    keywords = [title, "I'm Quitting Heroing", 'yuuyame']
    website = 'https://yuuyame.com/'
    twitter = 'yuuyame_anime'
    hashtags = ['yuuyame', '勇やめ']
    folder_name = 'yuuyame'

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
        # Need update for paging
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='div.newsPaging article',
                                    title_select='div.news_list_title', date_select='div.news_list_day',
                                    id_select='a', a_tag_prefix=self.PAGE_PREFIX, date_separator='/',
                                    news_prefix='news.html')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/FCEakgUXMAYyVuC?format=jpg&name=large')
        self.add_to_image_list('kv1_1', self.PAGE_PREFIX + 'images/news/p_001.jpg')
        self.add_to_image_list('kv1_2', self.PAGE_PREFIX + 'images/top/v_001.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'images/chara/'
        templates = [prefix + 'p_%s.png', prefix + 'f_%s_01.png', prefix + 'f_%s_02.png']
        self.download_by_template(folder, templates, 3, 1)
