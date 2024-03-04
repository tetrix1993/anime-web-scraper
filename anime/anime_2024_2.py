from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2
from datetime import datetime

# Dekisokonai to Yobareta Motoeiyuu wa Jikka kara Tsuihou sareta node Sukikatte ni Ikiru Koto ni Shita https://dekisoko-anime.com/ #できそこ @dekisoko_pr
# Henjin no Salad Bowl https://www.tbs.co.jp/anime/hensara/ #変サラ @hensara_anime
# Kami wa Game ni Ueteiru. https://godsgame-anime.com/ #神飢え #神飢えアニメ #kamiue @kami_to_game
# Kono Sekai wa Fukanzen Sugiru https://konofuka.com/ #このふか @konofuka_QA
# Ookami to Koushinryou https://spice-and-wolf.com/ #狼と香辛料 #spice_and_wolf @Spicy_Wolf_Prj
# Re:Monster https://re-monster.com/ #remonster_anime @ReMonster_anime
# Sasayaku You ni Koi wo Utau https://sasakoi-anime.com/ #ささこい @sasakoi_anime
# Tensei Kizoku, Kantei Skill de Nariagaru https://kanteiskill.com/ #鑑定スキル @kanteiskill
# Tensei shitara Dainana Ouji Datta node, Kimama ni Majutsu wo Kiwamemasu https://dainanaoji.com/ #第七王子 @dainanaoji_pro
# Unnamed Memory https://unnamedmemory.com/ #UnnamedMemory #アンメモ @Project_UM
# Yoru no Kurage wa Oyogenai https://yorukura-anime.com/ #ヨルクラ #yorukura_anime @yorukura_anime
# Yozakura-san Chi no Daisakusen https://mission-yozakura-family.com/ #夜桜さんちの大作戦 #MissionYozakuraFamily @OfficialHitsuji


# Spring 2024 Anime
class Spring2024AnimeDownload(MainDownload):
    season = "2024-2"
    season_name = "Spring 2024"
    folder_name = '2024-2'

    def __init__(self):
        super().__init__()


# Dekisokonai to Yobareta Motoeiyuu wa Jikka kara Tsuihou sareta node Sukikatte ni Ikiru Koto ni Shita
class DekisokoDownload(Spring2024AnimeDownload, NewsTemplate):
    title = 'Dekisokonai to Yobareta Motoeiyuu wa Jikka kara Tsuihou sareta node Sukikatte ni Ikiru Koto ni Shita'
    keywords = [title, 'The Banished Former Hero Lives as He Pleases']
    website = 'https://dekisoko-anime.com/'
    twitter = 'dekisoko_pr'
    hashtags = 'できそこ'
    folder_name = 'dekisoko'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news_item',
                                    title_select='.ttl', date_select='.year,.day', date_tag_count=2,
                                    id_select='a', a_tag_start_text_to_remove='../', a_tag_prefix=self.PAGE_PREFIX,
                                    date_func=lambda x: x[0:4] + '.' + x[4:6] + '.' + x[7:])

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        prefix = self.PAGE_PREFIX + 'dist/img/news/detail/'
        self.image_list = []
        self.add_to_image_list('tz', prefix + 'news0620-1.jpg')
        self.add_to_image_list('kv1', prefix + 'news0124-1.jpg')
        self.add_to_image_list('kv2', prefix + 'news0301-1.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'dist/img/character/chara%s/stand.webp'
        try:
            for i in range(1, 20, 1):
                image_url = template % i
                image_name = 'chara' + str(i)
                result = self.download_image(image_url, folder + '/' + image_name)
                if result == -1:
                    break
        except Exception as e:
            self.print_exception(e, 'Character')


# Henjin no Salad Bowl
class HensaraDownload(Spring2024AnimeDownload, NewsTemplate):
    title = 'Henjin no Salad Bowl'
    keywords = [title, 'Salad Bowl of Eccentrics']
    website = 'https://www.tbs.co.jp/anime/hensara/'
    twitter = 'hensara_anime'
    hashtags = '変サラ'
    folder_name = 'hensara'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='#nw-ind-list li',
                                    date_select='.date', title_select='.txt', id_select='a', a_tag_prefix=news_url)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        # self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/F7lu7ArboAAFbIl?format=jpg&name=large')
        # self.add_to_image_list('teaser_hero', self.PAGE_PREFIX + 'img/teaser/hero.jpg')
        self.add_to_image_list('top_hero', self.PAGE_PREFIX + 'img/top/hero.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'img/character/chara%s_st.png'
        self.download_by_template(folder, template, 1, 1)


# Kami wa Game ni Ueteiru.
class KamiueDownload(Spring2024AnimeDownload, NewsTemplate):
    title = 'Kami wa Game ni Ueteiru.'
    keywords = [title, "Gods' Game We Play"]
    website = 'https://godsgame-anime.com/'
    twitter = 'kami_to_game'
    hashtags = ['神飢え', '神飢えアニメ', 'kamiue']
    folder_name = 'kamiue'

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
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            json_obj = self.get_json(self.PAGE_PREFIX + 'news.json')
            for item in json_obj:
                if 'day' in item and 'url' in item and 'title' in item:
                    try:
                        date = datetime.strptime(item['day'], "%Y/%m/%d").strftime("%Y.%m.%d")
                    except:
                        continue
                    title = item['title']
                    url = self.PAGE_PREFIX + item['url']
                    if news_obj is not None and (news_obj['id'] == url or news_obj['title'] == title
                                                 or date < news_obj['date']):
                        break
                    results.append(self.create_news_log_object(date, title, url))
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
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.visual_wrap .img_100 img[src*="/visual/"]')
            self.image_list = []
            for image in images:
                image_name = self.extract_image_name_from_url(image['src'])
                image_url = self.PAGE_PREFIX + image['src']
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'images/chara/'
        template = prefix + 'c_%s.png'
        self.download_by_template(folder, template, 3, 1)
        templates = [prefix + 'a%s_left.png', prefix + 'a%s_center.png', prefix + 'a%s_right.png']
        self.download_by_template(folder, templates, 2, 1)

    def download_media(self):
        folder = self.create_media_directory()
        special_folder = self.create_custom_directory(folder.split('/')[-1] + '/special')
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'special.html?cat=visual')
            images = soup.select('article.visual a[href^="images/"]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['href']
                image_name = self.generate_image_name_from_url(image_url, 'images')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(special_folder)
        except Exception as e:
            self.print_exception(e, 'Special')


# Kono Sekai wa Fukanzen Sugiru
class KonofukaDownload(Spring2024AnimeDownload, NewsTemplate):
    title = 'Kono Sekai wa Fukanzen Sugiru'
    keywords = [title, "Quality Assurance in Another World"]
    website = 'https://konofuka.com/'
    twitter = 'konofuka_QA'
    hashtags = ['このふか', 'konofuka']
    folder_name = 'konofuka'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.top-news a',
                                    title_select='.news-ttl', date_select='.news-date', id_select=None,
                                    next_page_select='ul.page-numbers li span', next_page_eval_index=-1,
                                    next_page_eval_index_class='current',
                                    date_func=lambda x: x.replace('(', '').replace(')', ''))

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'pDK2yjkH/wp-content/themes/konofuka_v0.1/assets/img/top/mv.png')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fr85Cb4aAAAgWlS?format=jpg&name=4096x4096')
        self.download_image_list(folder)


# Ookami to Koushinryou
class OokamitoKoushinryou(Spring2024AnimeDownload, NewsTemplate):
    title = 'Ookami to Koushinryou'
    keywords = [title, 'Spice and Wolf']
    website = 'https://spice-and-wolf.com/'
    twitter = 'Spicy_Wolf_Prj'
    hashtags = ['狼と香辛料', 'spice_and_wolf']
    folder_name = 'spicewolf'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        news_soup = self.download_news()
        self.download_key_visual(news_soup)
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        xml_page = self.PAGE_PREFIX + '_inc/page/newslists.news.xml'
        soup = None
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            soup = self.get_soup(xml_page, decode=True)
            items = soup.select('item')
            for item in items:
                title_tags = item.select('title')
                date_y_tags = item.select('date_y')
                date_m_tags = item.select('date_m')
                date_d_tags = item.select('date_d')
                permalink_tags = item.select('permalink')
                if len(date_y_tags) > 0 and len(date_m_tags) > 0 and len(date_d_tags) > 0 and len(title_tags) > 0\
                        and len(permalink_tags) > 0:
                    date = date_y_tags[0].text.strip() + '.'\
                           + date_m_tags[0].text.strip() + '.'\
                           + date_d_tags[0].text.strip()
                    title = title_tags[0].text.strip()
                    url = self.PAGE_PREFIX + 'news/' + permalink_tags[0].text.strip()
                    if news_obj is not None and (news_obj['id'] == url or news_obj['title'] == title
                                                 or date < news_obj['date']):
                        break
                    results.append(self.create_news_log_object(date, title, url))
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            self.print_exception(e, 'News')
        return soup

    def download_key_visual(self, news_soup=None):
        folder = self.create_key_visual_directory()
        sub_folder = self.create_custom_directory(folder.split('/')[-1] + '/news')
        cache_filepath = sub_folder + '/cache'
        news_url = self.PAGE_PREFIX + 'news/'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        xml_page = self.PAGE_PREFIX + '_inc/page/newslists.news.xml'
        try:
            if news_soup is None:
                news_soup = self.get_soup(xml_page, decode=True)
            items = news_soup.select('item')
            for item in items:
                permalink_tag = item.select('permalink')
                if len(permalink_tag) == 0:
                    continue
                permalink = permalink_tag[0].text
                page_name = permalink.replace('.html', '')
                if page_name in processed:
                    break
                title_tag = item.select('title')
                if len(title_tag) == 0:
                    continue
                title = title_tag[0].text.strip()
                if 'ビジュアル' in title or 'イラスト' in title:
                    page_soup = self.get_soup(news_url + permalink)
                    if page_soup is not None:
                        images = page_soup.select('.newsArticle img[src]')
                        self.image_list = []
                        for image in images:
                            if not image['src'].startswith('img/'):
                                continue
                            image_url = news_url + image['src'].split('?')[0]
                            image_name = self.generate_image_name_from_url(image_url, 'img')
                            self.add_to_image_list(image_name, image_url)
                        self.download_image_list(sub_folder)
                processed.append(page_name)
        except Exception as e:
            self.print_exception(e, 'Key Visual News')
        self.create_cache_file(cache_filepath, processed, num_processed)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.characterDetailList img[src]')
            self.image_list = []
            for image in images:
                image_url = image['src']
                if image_url.startswith('./'):
                    image_url = self.PAGE_PREFIX + image_url[2:]
                if '/character/' in image_url:
                    image_name = self.generate_image_name_from_url(image_url, 'character')
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Re:Monster
class ReMonsterDownload(Spring2024AnimeDownload, NewsTemplate):
    title = 'Re:Monster'
    keyword = [title]
    website = 'https://re-monster.com/'
    twitter = 'ReMonster_anime'
    hashtags = 'remonster_anime'
    folder_name = 'remonster'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.newsList',
                                    date_select='.news__date', title_select='.newsTitle', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        soup = None
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.visualList source[srcset*="/top/"][type="image/webp"]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'].replace('./', '').split('?')[0]
                image_name = self.extract_image_name_from_url(image_url)
                if image_name.endswith('-s') or 'catch' in image_name:
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')
        return soup

    def download_character(self, soup=None):
        folder = self.create_character_directory()
        self.image_list = []
        try:
            if soup is None:
                soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.characterList img[src*="/character/"]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('./', '').split('?')[0]
                image_name = self.generate_image_name_from_url(image_url, 'character')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Sasayaku You ni Koi wo Utau
class SasakoiDownload(Spring2024AnimeDownload, NewsTemplate):
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


# Tensei Kizoku, Kantei Skill de Nariagaru
class KanteiSkillDownload(Spring2024AnimeDownload, NewsTemplate):
    title = 'Tensei Kizoku, Kantei Skill de Nariagaru'
    keywords = [title, 'kanteiskill', "As a Reincarnated Aristocrat, I’ll Use My Appraisal Skill to Rise in the World"]
    website = 'https://kanteiskill.com/'
    twitter = 'kanteiskill'
    hashtags = '鑑定スキル'
    folder_name = 'kanteiskill'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.c-news-item',
                                    title_select='.c-news-item__title', date_select='.c-news-item__date',
                                    id_select=None, a_tag_start_text_to_remove='/', a_tag_prefix=self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FvmXW8HakAAhiY6?format=jpg&name=large')
        self.add_to_image_list('home_visual_1_pc', self.PAGE_PREFIX + 'wordpress/wp-content/themes/kanteiskill_20231110/img/home/visual_1_pc.webp')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        json_url = self.PAGE_PREFIX + 'chara_data'
        self.image_list = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            if soup is None:
                return
            prefix = soup.select('body[data-theme-url]')[0]['data-theme-url']

            json_obj = self.get_json(json_url)
            if 'charas' in json_obj and isinstance(json_obj['charas'], list):
                for chara in json_obj['charas']:
                    if 'images' in chara:
                        if 'visuals' in chara['images'] and isinstance(chara['images']['visuals'], list):
                            for visual in chara['images']['visuals']:
                                if 'image' in visual:
                                    image_url = prefix + visual['image'].split('?')[0]
                                    image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                                    self.add_to_image_list(image_name, image_url)
                        if 'faces' in chara['images'] and isinstance(chara['images']['faces'], list):
                            for face in chara['images']['faces']:
                                image_url = prefix + face.split('?')[0]
                                image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                                self.add_to_image_list(image_name, image_url)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.download_image_list(folder)


# Tensei shitara Dainana Ouji Datta node, Kimama ni Majutsu wo Kiwamemasu
class DainanaojiDownload(Spring2024AnimeDownload, NewsTemplate):
    title = 'Tensei shitara Dainana Ouji Datta node, Kimama ni Majutsu wo Kiwamemasu'
    keywords = [title, 'I Was Reincarnated as the 7th Prince so I Can Take My Time Perfecting My Magical Ability']
    website = 'https://dainanaoji.com/'
    twitter = 'dainanaoji_pro'
    hashtags = '第七王子'
    folder_name = 'dainanaoji'

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

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='#news-container article',
                                    date_select='.news-box-date', title_select='.news-txt-box', id_select='a',
                                    next_page_select='.pagination .page-numbers',
                                    next_page_eval_index_class='current', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fgo-UydUAAAq3qH?format=jpg&name=medium')
        self.add_to_image_list('tz_visual_img', self.PAGE_PREFIX + 'd81Ft6ye/wp-content/themes/v0/assets/img/top/visual/img.webp')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        # template = self.PAGE_PREFIX + 'd81Ft6ye/wp-content/themes/v0/assets/img/character/%s.webp'
        # self.download_by_template(folder, template, 1, 0, prefix='tz_')
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.character-img-box>img[src]')
            for image in images:
                if '/img/' not in image['src']:
                    continue
                image_url = image['src']
                image_name = self.generate_image_name_from_url(image_url, 'img')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Unnamed Memory
class UnnamedMemoryDownload(Spring2024AnimeDownload, NewsTemplate):
    title = 'Unnamed Memory'
    keywords = [title]
    website = 'https://unnamedmemory.com/'
    twitter = 'Project_UM'
    hashtags = ['UnnamedMemory', 'アンメモ']
    folder_name = 'unnamedmemory'

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
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fj2aPSZVIAEC9LY?format=jpg&name=4096x4096')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.vis source[srcset], .vis img[src]')
            self.image_list = []
            for image in images:
                if image.has_attr('srcset'):
                    image_url = image['srcset']
                else:
                    image_url = image['src']
                if image_url.startswith('./'):
                    image_url = self.PAGE_PREFIX + image_url[2:]
                if '/assets/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'assets')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

        sub_folder = self.create_custom_directory(folder.split('/')[-1] + '/news')
        cache_filepath = sub_folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        temp_processed = set()  # Some of the id is not unique
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'news.html')
            items = soup.select('article article')
            for item in items:
                page_name = item['id']
                if page_name in processed:
                    break
                title = item.select('.entry-title span')[0].text.strip()
                if 'ビジュアル' in title or 'イラスト' in title:
                    images = item.select('img[data-src]')
                    self.image_list = []
                    for image in images:
                        image_url = self.PAGE_PREFIX + image['data-src'].replace('./', '').split('?')[0]
                        if '/news/' not in image_url:
                            continue
                        image_name = self.generate_image_name_from_url(image_url, 'news')
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(sub_folder)
                temp_processed.add(page_name)
        except Exception as e:
            self.print_exception(e, 'Key Visual News')
        for page_name in temp_processed:
            processed.append(page_name)
        self.create_cache_file(cache_filepath, processed, num_processed)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/character/%s.webp'
        self.download_by_template(folder, template, 1, 1)


# Yoru no Kurage wa Oyogenai
class YorukuraDownload(Spring2024AnimeDownload, NewsTemplate):
    title = 'Yoru no Kurage wa Oyogenai'
    keywords = [title, 'Jellyfish Can’t Swim in the Night']
    website = 'https://yorukura-anime.com/'
    twitter = 'yorukura_anime'
    hashtags = ['ヨルクラ', 'yorukura_anime']
    folder_name = 'yorukura'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, news_prefix='', article_select='#news article',
                                    date_select='time', title_select='h3', id_select=None, id_has_id=True)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        # self.image_list = []
        # self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fr6oNgXaIAIDcgR?format=jpg&name=large')
        # self.add_to_image_list('tz', self.PAGE_PREFIX + 'images/mainimg.jpg')
        # self.download_image_list(folder)

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
        prefix = self.PAGE_PREFIX + 'images/character/'
        templates = [prefix + 'img_%s.png', prefix + 'face_%s.png']
        self.download_by_template(folder, templates, 2, 1)


# Yozakura-san Chi no Daisakusen
class YozakurasanDownload(Spring2024AnimeDownload, NewsTemplate2):
    title = 'Yozakura-san Chi no Daisakusen'
    keywords = [title, 'Mission: Yozakura Family']
    website = 'https://mission-yozakura-family.com/'
    twitter = 'OfficialHitsuji'
    hashtags = ['夜桜さんちの大作戦', 'MissionYozakuraFamily']
    folder_name = 'yozakurasan'

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
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FkJB8aSVEAA5Xd1?format=jpg&name=medium')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.kv__img img[src]')
            self.image_list = []
            for image in images:
                if '/images/' in image['src']:
                    image_url = self.PAGE_PREFIX + image['src']
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
            soup = self.get_soup(self.PAGE_PREFIX + 'character/taiyo.html')
            pages = soup.select('#ContentsListUnit01 a[href]')
            for page in pages:
                if not page['href'].endswith('.html') or not page['href'].startswith('../'):
                    continue
                page_url = self.PAGE_PREFIX + page['href'].replace('../', '')
                page_name = page_url.split('/')[-1].split('.html')[0]
                if page_name in processed:
                    continue
                if page_name == 'taiyo':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(page_url)
                if ep_soup is None:
                    continue
                images = ep_soup.select('.charaVisual__img source[srcset]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['srcset'].replace('../', '')
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
                processed.append(page_name)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)
