from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2
import os

# Boukensha ni Naritai to Miyako ni Deteitta Musume ga S-Rank ni Natteta
# Dekoboko Majo no Oyako Jijou https://dekoboko-majo-anime.jp/ @DEKOBOKO_anime #でこぼこ魔女の親子事情
# Hametsu no Oukoku https://hametsu-anime.com/ #はめつのおうこく #はめつ @hametsu_anime
# Hoshikuzu Telepath https://hoshitele-anime.com/ #星テレ #hoshitele @hoshitele_anime
# Kimi no Koto ga Daidaidaidaidaisuki na 100-nin no Kanojo https://hyakkano.com/ @hyakkano_anime #100カノ
# Konyaku Haki sareta Reijou wo Hirotta Ore ga, Ikenai koto wo Oshiekomu https://ikenaikyo.com/ #イケナイ教 @ikenaikyo_anime
# Potion-danomi de Ikinobimasu! https://potion-anime.com/ #ポーション頼み @potion_APR
# Shy https://shy-anime.com/ #SHY_hero @SHY_off
# Sousou no Frieren https://frieren-anime.jp/ #フリーレン #frieren @Anime_Frieren
# Tearmoon Teikoku Monogatari https://tearmoon-pr.com/ #ティアムーン @tearmoon_pr
# Toaru Ossan no VRMMO Katsudouki https://toaru-ossan.com/ #とあるおっさん @toaru_ossan_pr
# Watashi no Oshi wa Akuyaku Reijou. https://wataoshi-anime.com/ #わたおし #wataoshi #ILTV @wataoshi_anime


# Fall 2023 Anime
class Fall2023AnimeDownload(MainDownload):
    season = "2023-4"
    season_name = "Fall 2023"
    folder_name = '2023-4'

    def __init__(self):
        super().__init__()


# Boukensha ni Naritai to Miyako ni Deteitta Musume ga S-Rank ni Natteta
class SRankMusumeDownload(Fall2023AnimeDownload, NewsTemplate):
    title = 'Boukensha ni Naritai to Miyako ni Deteitta Musume ga S-Rank ni Natteta'
    keywords = [title, 'My Daughter Left the Nest and Returned an S-Rank Adventurer']
    website = 'https://s-rank-musume.com/'
    twitter = 's_rank_musume'
    hashtags = 'Sランク娘'
    folder_name = 'srankmusume'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsLists__item',
                                    date_select='.newsLists__time', title_select='.newsLists__title',
                                    id_select='a', a_tag_start_text_to_remove='/', a_tag_prefix=self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.visualListsWrap img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'][1:]
                if '/top/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'top')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.charaDetail__stand img[src], .charaDetail__faceLists img[src]')
            self.image_list = []
            for image in images:
                image_url = self.clear_resize_in_url(self.PAGE_PREFIX + image['src'][1:])
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Dekoboko Majo no Oyako Jijou
class DekobokoMajoDownload(Fall2023AnimeDownload, NewsTemplate):
    title = 'Dekoboko Majo no Oyako Jijou'
    keywords = [title]
    website = 'https://dekoboko-majo-anime.jp/'
    twitter = 'DEKOBOKO_anime'
    hashtags = ['でこぼこ魔女の親子事情']
    folder_name = 'dekoboko-majo'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='#news article', date_select='time',
                                    title_select='h3', id_select=None, id_has_id=True, news_prefix='')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        # self.image_list = []
        # self.add_to_image_list('teaser-visual', self.PAGE_PREFIX + 'images/teaser-visual.jpg')
        # self.add_to_image_list('mainimg', self.PAGE_PREFIX + 'images/mainimg.jpg')
        # self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.mainimg img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'assets/images/character/'
        template = [prefix + 'img_%s.png', prefix + 'face_%s.png']
        self.download_by_template(folder, template, 2, 1)


# Hametsu no Oukoku
class HametsuDownload(Fall2023AnimeDownload, NewsTemplate):
    title = 'Hametsu no Oukoku'
    keywords = [title, 'The Kingdoms of Ruin']
    website = 'https://hametsu-anime.com/'
    twitter = 'hametsu_anime'
    hashtags = ['はめつのおうこく', 'はめつ']
    folder_name = 'hametsu'

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
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fn261mwaQAAWJst?format=jpg&name=4096x4096')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.vis source[srcset]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'].replace('./', '')
                if '/assets/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'assets')
                if image_name.endswith('-sp'):
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        templates = [
            self.PAGE_PREFIX + 'assets/character/%sc.webp',
            self.PAGE_PREFIX + 'assets/character/%sf.webp',
            self.PAGE_PREFIX + 'assets/character/%ss.webp'
        ]
        self.download_by_template(folder, templates, 1, 1)


# Hoshikuzu Telepath
class HoshiteleDownload(Fall2023AnimeDownload, NewsTemplate):
    title = 'Hoshikuzu Telepath'
    keywords = [title, 'Hoshitele']
    website = 'https://hoshitele-anime.com/'
    twitter = 'hoshitele_anime'
    hashtags = ['星テレ', 'hoshitele']
    folder_name = 'hoshitele'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.bl_vertPosts_item',
                                    date_select='.bl_vertPosts_date', title_select='.bl_vertPosts_txt',
                                    id_select='a', a_tag_prefix=news_url, a_tag_start_text_to_remove='./')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.tp_hero img[src]')
            self.image_list = []
            for image in images:
                if '/top/' not in image['src']:
                    continue
                image_name = self.extract_image_name_from_url(image['src'])
                if 'kv' not in image_name:
                    continue
                image_name = self.generate_image_name_from_url(image['src'], 'top')
                image_url = self.PAGE_PREFIX + image['src'].replace('./', '')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

        sub_folder = self.create_custom_directory(folder.split('/')[-1] + '/news')
        cache_filepath = sub_folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        news_url = self.PAGE_PREFIX + 'news/'
        try:
            soup = self.get_soup(news_url)
            items = soup.select('.bl_vertPosts_item a[href]')
            for item in items:
                if not item['href'].startswith('./') or '?id=' not in item['href']:
                    continue
                page_name = item['href'].split('?id=')[-1]
                if len(page_name) == 0:
                    continue
                if page_name in processed:
                    break
                title = item.text.strip()
                if 'ビジュアル' in title:
                    news_soup = self.get_soup(news_url + item['href'].replace('./', ''))
                    if news_soup is not None:
                        images = news_soup.select('.bl_news img[src]')
                        self.image_list = []
                        for image in images:
                            image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                            if '/news/' not in image_url:
                                continue
                            image_name = self.generate_image_name_from_url(image_url, 'news')
                            self.add_to_image_list(image_name, image_url)
                        self.download_image_list(sub_folder)
                processed.append(page_name)
        except Exception as e:
            self.print_exception(e, 'Key Visual News')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Kimi no Koto ga Daidaidaidaidaisuki na 100-nin no Kanojo
class HyakkanoDownload(Fall2023AnimeDownload, NewsTemplate):
    title = 'Kimi no Koto ga Daidaidaidaidaisuki na 100-nin no Kanojo'
    keywords = [title, 'The 100 Girlfriends Who Really, Really, Really, Really, Really Love You']
    website = 'https://hyakkano.com/'
    twitter = 'hyakkano_anime'
    hashtags = '100カノ'
    folder_name = 'hyakkano'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-List li',
                                    date_select='.date', title_select='.title', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'xUtUy1FY/wp-content/themes/hyakkano_v0/assets/images/common/index/img_mainvisual.png')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FrGH-A3aUAA0dVE?format=jpg&name=medium')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.index-Mainvisual-Inner img[src]')
            for image in images:
                if '/images/' not in image['src']:
                    continue
                image_url = image['src']
                image_name = self.generate_image_name_from_url(image_url, 'images')
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
            charas = soup.select('.chara-select-Btn a[href][class]')
            for chara in charas:
                if chara['href'].endswith('/'):
                    page_url = chara['href'][:-1]
                else:
                    page_url = chara['href']
                if 'current' in chara['class']:
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(page_url)
                if ep_soup is None:
                    continue
                images = ep_soup.select('.character-Item img[src]')
                self.image_list = []
                for image in images:
                    image_url = image['src']
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Konyaku Haki sareta Reijou wo Hirotta Ore ga, Ikenai koto wo Oshiekomu
class IkenaikyoDownload(Fall2023AnimeDownload, NewsTemplate):
    title = 'Konyaku Haki sareta Reijou wo Hirotta Ore ga, Ikenai koto wo Oshiekomu'
    keywords = [title, "ikenaikyo", "I’m Giving the Disgraced Noble Lady I Rescued a Crash Course in Naughtiness"]
    website = 'https://ikenaikyo.com/'
    twitter = 'ikenaikyo_anime'
    hashtags = ['イケナイ教']
    folder_name = 'ikenaikyo'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.infoList a',
                                    date_select='span', title_select='li', id_select=None)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'manage/wp-content/uploads/2023/04/KV.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        chara_prefix = self.PAGE_PREFIX + 'images/character/chara'
        templates = [
            chara_prefix + '%s.png',
            chara_prefix + '%s-1.png',
            chara_prefix + '%s-2.png'
        ]
        self.download_by_template(folder, templates, 2, 1)


# Potion-danomi de Ikinobimasu!
class PotionDanomiDownload(Fall2023AnimeDownload, NewsTemplate):
    title = 'Potion-danomi de Ikinobimasu!'
    keywords = [title, 'I Shall Survive Using Potions!']
    website = 'https://potion-anime.com/'
    twitter = 'potion_APR'
    hashtags = 'ポーション頼み'
    folder_name = 'potiondanomi'

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
            images = soup.select('.home-visual__visual source[srcset]')
            for image in images:
                if '/img/' in image['srcset']:
                    image_url = self.PAGE_PREFIX + image['srcset'].split('?')[0].replace('./', '')
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


# Shy
class ShyDownload(Fall2023AnimeDownload, NewsTemplate):
    title = 'Shy'
    keywords = [title]
    website = 'https://shy-anime.com/'
    twitter = 'SHY_off'
    hashtags = 'SHY_hero'
    folder_name = 'shy'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-box',
                                    title_select='.news-txt-box', date_select='.news-box-date', id_select='a',
                                    paging_type=0, next_page_select='span.page-numbers', next_page_eval_index=-1,
                                    next_page_eval_index_class='current')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FeTEERvaEAAJmXS?format=jpg&name=large')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('#kv>img[src]')
            for image in images:
                image_url = image['src']
                if '/img/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'img')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        self.add_to_image_list('tz_shy', self.PAGE_PREFIX + 'nE2aBbsJ/wp-content/themes/v0/assets/img/kv/shy.webp')
        self.add_to_image_list('tz_tel', self.PAGE_PREFIX + 'nE2aBbsJ/wp-content/themes/v0/assets/img/kv/tel.webp')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'nE2aBbsJ/wp-content/themes/v1/assets/img/character/%s/%s.png'
        for i in range(30):
            is_successful = False
            for j in ['img', 'face']:
                image_name = str(i).zfill(2) + '_' + j
                if self.is_image_exists(image_name, folder):
                    is_successful = True
                    continue
                image_url = template % (str(i), j)
                result = self.download_image(image_url, folder + '/' + image_name)
                if result != -1:
                    is_successful = True
            if not is_successful:
                break


# Sousou no Frieren
class FrierenDownload(Fall2023AnimeDownload, NewsTemplate):
    title = 'Sousou no Frieren'
    keywords = [title, "Frieren: Beyond Journey's End"]
    website = 'https://frieren-anime.jp/'
    twitter = 'Anime_Frieren'
    hashtags = ['フリーレン', 'frieren']
    folder_name = 'frieren'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.newsLists__item',
                                    date_select='.newsLists__time', title_select='.newsLists__title', id_select='a',
                                    a_tag_start_text_to_remove='./', a_tag_prefix=self.PAGE_PREFIX + 'news/')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FcgQDbKaAAAEBu_?format=jpg&name=4096x4096')
        self.add_to_image_list('tz2_tw', 'https://pbs.twimg.com/media/FqqKOB3aQAMhTCs?format=jpg&name=4096x4096')
        self.add_to_image_list('index_visual', self.PAGE_PREFIX + 'assets/img/index/visual.jpg')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.visualLists__imgWrap img[src]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('./', '')
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'assets/img/character/chara'
        templates = [
            prefix + '%s_full1.png', prefix + '%s_full2.png', prefix + '%s_full.png',
            prefix + '%s_face1.jpg', prefix + '%s_face2.jpg', prefix + '%s_face.jpg'
        ]
        self.download_by_template(folder, templates, 1, 1)


# Tearmoon Teikoku Monogatari
class TearmoonDownload(Fall2023AnimeDownload, NewsTemplate):
    title = 'Tearmoon Teikoku Monogatari'
    keywords = [title, 'Tearmoon Empire']
    website = 'https://tearmoon-pr.com/'
    twitter = 'tearmoon_pr'
    hashtags = 'ティアムーン'
    folder_name = 'tearmoon'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ul.news--list li',
                                    date_select='.txt--date', title_select='.txt--ttl', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fb9eKCbaIAAj66L?format=jpg&name=large')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + '_assets/images/top/fv/webp/fv_%s_pc.webp'
        self.download_by_template(folder, template, 3, 1)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.chardata img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'][1:]
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Toaru Ossan no VRMMO Katsudouki
class ToaruOssanDownload(Fall2023AnimeDownload, NewsTemplate):
    title = 'Toaru Ossan no VRMMO Katsudouki'
    keywords = [title, "A Playthrough of a Certain Dude’s VRMMO Life"]
    website = 'https://toaru-ossan.com/'
    twitter = 'toaru_ossan_pr'
    hashtags = ['とあるおっさん']
    folder_name = 'toaruossan'

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
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='#news li',
                                    date_select='time', title_select='p', id_select='a', a_tag_prefix=news_url)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('img_teaser', self.PAGE_PREFIX + 'assets/images/top/img_teaser.jpg')
        self.add_to_image_list('mainimg', self.PAGE_PREFIX + 'assets/images/top/mainimg.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'assets/images/character/'
        templates = [prefix + 'img_%s.png', prefix + 'face_%s.png']
        self.download_by_template(folder, templates, 2, 1)


# Watashi no Oshi wa Akuyaku Reijou.
class WataoshiDownload(Fall2023AnimeDownload, NewsTemplate):
    title = 'Watashi no Oshi wa Akuyaku Reijou.'
    keywords = [title, 'I\'m in Love with the Villainess']
    website = 'https://wataoshi-anime.com/'
    twitter = 'wataoshi_anime'
    hashtags = ['わたおし', 'wataoshi', 'ILTV']
    folder_name = 'wataoshi'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, news_prefix='', article_select='#news li',
                                    date_select='time', title_select='p', id_select='a', a_tag_prefix=self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fj120y9VIAAx9Jp?format=jpg&name=medium')
        self.add_to_image_list('kv1', 'https://pbs.twimg.com/media/Fv6DLpYaQAACtjt?format=jpg&name=large')
        self.add_to_image_list('img_visual1.jpg', self.PAGE_PREFIX + 'images/img_visual1.jpg')
        self.download_image_list(folder)

        css_url = self.PAGE_PREFIX + 'css/style.min.css'
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            mainslides = soup.select('.mainimg .mainslide[class]')
            _classes = []
            for slide in mainslides:
                for _class in slide['class']:
                    if _class not in ['mainslide', 'swiper-slide']:
                        _classes.append(_class)
                        break
            if len(_classes) > 0:
                self.image_list = []
                css_page = self.get_response(css_url)
                for _class in _classes:
                    search_text = '.mainslide.' + _class + '{background:url('
                    idx = css_page.find(search_text)
                    if idx > 0:
                        right_idx = css_page[idx + len(search_text):].find(')')
                        if right_idx > 0:
                            start_idx = idx + len(search_text)
                            image_url = css_page[start_idx:start_idx + right_idx]
                            if image_url.startswith('../'):
                                image_url = self.PAGE_PREFIX + image_url[3:]
                            image_name = self.extract_image_name_from_url(image_url)
                            self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'images/img_chara_'
        templates = [prefix + '%s.png', prefix + 'face_%s.png']
        self.download_by_template(folder, templates, 2, 1)

    def download_media(self):
        folder = self.create_media_directory()

        # Voices
        voice_folder = folder + '/voice'
        if not os.path.exists(voice_folder):
            os.makedirs(voice_folder)
        for i in range(99):
            audio_name = f'chara_{str(i + 1).zfill(2)}.mp3'
            audio_url = self.PAGE_PREFIX + 'mp3/' + audio_name
            result = self.download_content(audio_url, voice_folder + '/' + audio_name)
            if result == -1:
                break
