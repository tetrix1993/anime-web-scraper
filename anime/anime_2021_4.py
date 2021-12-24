import os
import anime.constants as constants
from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate3
from datetime import datetime, timedelta
from scan import AniverseMagazineScanner, MocaNewsScanner, WebNewtypeScanner
from requests.exceptions import HTTPError


# Blue Period https://blue-period.jp/ #ブルーピリオド @blueperiod_PR
# Deep Insanity: The Lost Child https://www.jp.square-enix.com/deepinsanity/anime/ #DI #ディープインサニティ @deepinsanity_pj
# Gyakuten Sekai no Denchi Shoujo https://denchi-project.com/ #電池少女 @denchi_project
# Isekai Shokudou 2 https://isekai-shokudo2.com/ #異世界食堂 @nekoya_PR
# Kaizoku Oujo http://fena-pirate-princess.com/ #海賊王女 @fena_pirate
# Komi-san wa, Comyushou desu. https://komisan-official.com/ #古見さん #komisan @comisanvote
# Mieruko-chan https://mierukochan.jp/ #見える子ちゃん @mierukochan_PR
# Muv-Luv Alternative https://muv-luv-alternative-anime.com/ #マブラヴ #マブラヴアニメ #muvluv @Muv_Luv_A_anime
# Ousama Ranking https://osama-ranking.com/ #王様ランキング @osama_ranking
# Platinum End https://anime-platinumend.com/ #プラチナエンド #PlatinumEnd @ani_platinumend
# Saihate no Paladin https://farawaypaladin.com/ #最果てのパラディン #faraway_paladin @faraway_paladin
# Sakugan http://sakugan-anime.com/ #サクガン @ANIMA_info
# Sekai Saikou no Ansatsusha, Isekai Kizoku ni Tensei suru https://ansatsu-kizoku.jp/ #暗殺貴族 @ansatsu_kizoku
# Senpai ga Uzai Kouhai no Hanashi https://senpaiga-uzai-anime.com/ #先輩がうざい後輩の話 @uzai_anime
# Shin no Nakama ja Nai to Yuusha no Party wo Oidasareta node, Henkyou de Slow Life suru Koto ni Shimashita https://shinnonakama.com/ #真の仲間 @shinnonakama_tv
# Shinka no Mi: Shiranai Uchi ni Kachigumi Jinsei https://www.shinkanomi-anime.com/ #進化の実 #勝ち組人生 #ゴリラ系女子 @shinkanomianime
# Taishou Otome Otogibanashi http://taisho-otome.com/ #大正オトメ #昭和オトメ @otome_otogi
# takt op.Destiny https://anime.takt-op.jp/ #takt_op_Destiny #タクトオーパス @takt_op_destiny
# Tsuki to Laika to Nosferatu https://tsuki-laika-nosferatu.com/ #月とライカ @LAIKA_anime
# Yuuki Yuuna wa Yuusha de Aru: Dai Mankai no Shou https://yuyuyu.tv/season2/ #yuyuyu @anime_yukiyuna


# Fall 2021 Anime
class Fall2021AnimeDownload(MainDownload):
    season = "2021-4"
    season_name = "Fall 2021"
    folder_name = '2021-4'

    def __init__(self):
        super().__init__()


# Blue Period
class BluePeriodDownload(Fall2021AnimeDownload, NewsTemplate):
    title = 'Blue Period'
    keywords = [title]
    website = 'https://blue-period.jp/'
    twitter = 'blueperiod_PR'
    hashtags = 'ブルーピリオド'
    folder_name = 'blue-period'

    PAGE_PREFIX = website
    FINAL_EPISODE = 24

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        # self.download_episode_preview_external()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            containers = soup.select('div.ep-container')
            for container in containers:
                try:
                    episode = str(int(container.select('p.ep-num-text span')[0].text.strip())).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                images = container.select('div.ep-ss-main img')
                self.image_list = []
                for i in range(len(images)):
                    if images[i].has_attr('src'):
                        image_url = images[i]['src']
                        image_name = f'{episode}_{i + 1}'
                        self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ul.news-list li.news-item',
                                    date_select='p.news-date', title_select='p.news-title', id_select='a',
                                    next_page_select='div.pagination a.next',
                                    next_page_eval_index_class='off', next_page_eval_index=0)

    def download_episode_preview_external(self):
        jp_title = 'ブルーピリオド'
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE, min_width=750,
                                end_date='20210929', download_id=self.download_id).run()

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser-kv', self.PAGE_PREFIX + 'wp/wp-content/themes/blueperiod_honban_theme/assets/img/page/teaser-kv.jpg')
        self.add_to_image_list('1stkv', self.PAGE_PREFIX + 'wp/wp-content/themes/blueperiod_honban_theme/assets/img/page/1stkv.jpg')
        self.add_to_image_list('2ndkv', self.PAGE_PREFIX + 'wp/wp-content/themes/blueperiod_honban_theme/assets/img/page/2ndkv.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/blueperiod_honban_theme/assets/img/page/chara-pic%s.png'
        self.download_by_template(folder, template, 2, 1)


# Deep Insanity: The Lost Child
class DeepInsanityDownload(Fall2021AnimeDownload):
    title = 'Deep Insanity: The Lost Child'
    keywords = [title]
    website = 'https://www.jp.square-enix.com/deepinsanity/anime/'
    twitter = 'deepinsanity_pj'
    hashtags = ['DI', 'ディープインサニティ']
    folder_name = 'deep-insanity'

    PAGE_PREFIX = 'https://www.jp.square-enix.com/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_key_visual()

    def download_episode_preview(self):
        first_page_url = self.PAGE_PREFIX + 'deepinsanity/anime/story/1'
        try:
            soup = self.get_soup(first_page_url)
            items = soup.select('li.story-list__item')
            for item in items:
                a_tag = item.find('a')
                if a_tag and a_tag.has_attr('href'):
                    try:
                        episode = str(int(a_tag.text.strip().replace('#', ''))).zfill(2)
                    except:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    page_url = self.PAGE_PREFIX + a_tag['href'][1:]
                    if page_url == first_page_url:
                        ep_soup = soup
                    else:
                        ep_soup = self.get_soup(page_url)
                    if ep_soup:
                        images = ep_soup.select('li.splide__slide img')
                        self.image_list = []
                        for i in range(len(images)):
                            if images[i].has_attr('src'):
                                image_url = self.PAGE_PREFIX + images[i]['src'][1:].split('?')[0]
                                image_name = episode + '_' + str(i + 1)
                                self.add_to_image_list(image_name, image_url)
                        self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv_tw', 'https://pbs.twimg.com/media/E_eipEAVUAQwHQh?format=jpg&name=4096x4096')
        self.add_to_image_list('anime_kv', self.PAGE_PREFIX + 'deepinsanity/assets/images/anime/anime_kv.png')
        self.download_image_list(folder)


# Gyakuten Sekai no Denchi Shoujo
class DenchiShoujoDownload(Fall2021AnimeDownload, NewsTemplate):
    title = 'Gyakuten Sekai no Denchi Shoujo'
    keywords = [title, 'Rumble Garanndoll']
    website = 'https://denchi-project.com/'
    twitter = 'denchi_project'
    hashtags = '電池少女'
    folder_name = 'denchi-shoujo'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_media()

    def download_episode_preview(self):
        for i in range(self.FINAL_EPISODE):
            ep_num = i + 1
            episode = str(ep_num).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            template1 = self.PAGE_PREFIX + f'assets/story/{i + 1}_%s.jpg'
            template2 = self.PAGE_PREFIX + f'assets/story/{i + 1}_%s.png'
            success = False
            for j in range(6):
                image_name = f'{episode}_{j + 1}'
                for template in [template1, template2]:
                    image_url = template % str(j + 1)
                    result = self.download_image(image_url, f'{self.base_folder}/{image_name}')
                    if result != -1:
                        success = True
                        break
                if not success:
                    break
            if not success:
                break

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.content-entry',
                                    title_select='h2.entry-title span', date_select='div.entry-date span',
                                    id_select=None, id_has_id=True, news_prefix='news.html')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('vis-all', self.PAGE_PREFIX + 'assets/top/t1/vis-all.jpg')
        self.add_to_image_list('vis-t1', self.PAGE_PREFIX + 'assets/news/vis-t1.jpg')
        self.download_image_list(folder)

        template1 = self.PAGE_PREFIX + 'assets/top/t1/vis-all%s.jpg'
        self.download_by_template(folder, template1, 1, 2)

        template2 = self.PAGE_PREFIX + 'assets/news/vis-k%s.jpg'
        self.download_by_template(folder, template2, 1, 1)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/character/c/%s.png'
        self.download_by_template(folder, template, 1, 1, prefix='chara', save_zfill=2)

    def download_media(self):
        folder = self.create_media_directory()

        # Blu-ray
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bluray.html')
            images = soup.select('article img:not(h2 img, .sub-logo img)')
            self.image_list = []
            for image in images:
                if image.has_attr('src') and not image['src'].endswith('np.png'):
                    image_url = self.PAGE_PREFIX + image['src'].replace('./', '')
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Isekai Shokudou 2
class IsekaiShokudou2Download(Fall2021AnimeDownload, NewsTemplate3):
    title = 'Isekai Shokudou 2'
    keywords = [title, 'Restaurant to Another World']
    website = 'https://isekai-shokudo2.com/'
    twitter = 'nekoya_PR'
    hashtags = '異世界食堂'
    folder_name = 'isekai-shokudo2'

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
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story.html')
            episode_tags = soup.select('div.story-data')
            for episode_tag in episode_tags:
                if episode_tag.has_attr('id'):
                    try:
                        episode = str(int(episode_tag['id'].strip().replace('S', ''))).zfill(2)
                    except:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    images = episode_tag.select('div.ep-slider-sceneImage img')
                    self.image_list = []
                    for i in range(len(images)):
                        if images[i].has_attr('src'):
                            image_url = self.PAGE_PREFIX + images[i]['src'].strip().replace('./', '')
                            image_name = f'{episode}_{i + 1}'
                            self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        # self.add_to_image_list('kv1', self.PAGE_PREFIX + 'assets/top/main-t1/vis.jpg')
        self.add_to_image_list('vis-t1', self.PAGE_PREFIX + 'assets/top/vis-t1/vis.jpg')
        self.download_image_list(folder)

        top_url = self.PAGE_PREFIX + 'assets/top/'
        try:
            for i in ['vis-kv%s', 'vis-ep%s']:
                for j in range(1, 100, 1):
                    image_name = i % str(j)
                    image_url = top_url + image_name + '/vis.jpg'
                    image_save_path = folder + '/' + image_name
                    if self.is_image_exists(image_name, folder):
                        continue
                    result = self.download_image(image_url, image_save_path)
                    if result == -1:
                        break
        except:
            pass

    def download_character(self):
        folder = self.create_character_directory()
        # template = self.PAGE_PREFIX + 'assets/top/character/c%s.png'
        templates = [self.PAGE_PREFIX + 'assets/character/c/%s.png', self.PAGE_PREFIX + 'assets/character/f/%s.png']
        prefixes = ['chara', 'face']
        self.download_by_template(folder, templates, 1, 1, prefix=prefixes, save_zfill=2)

    def download_media(self):
        folder = self.create_media_directory()
        self.image_list = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bluray.html')
            images = soup.select('div.bdbox-data img')
            for image in images:
                if image.has_attr('src') and not image['src'].endswith('np.png'):
                    image_url = self.PAGE_PREFIX + image['src'].replace('./', '')
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')
        self.download_image_list(folder)


# Kaizoku Oujo
class KaizokuOujoDownload(Fall2021AnimeDownload, NewsTemplate):
    title = 'Kaizoku Oujo'
    keywords = [title, 'Fena: Pirate Princess']
    website = 'http://fena-pirate-princess.com/'
    twitter = 'fena_pirate'
    hashtags = '海賊王女'
    folder_name = 'kaizoku-oujo'

    PAGE_PREFIX = website

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.md-news__li',
                                    date_select='time', title_select='h3', id_select='a', date_separator='.&nbsp;',
                                    next_page_select='ul.pagenation-list li',
                                    next_page_eval_index_class='is__current', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('fv_pc', self.PAGE_PREFIX + 'wp/wp-content/themes/fena-pirate-princess/_assets/images/top/fv_pc.jpg')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/E4C7eKvXMAMT67c?format=jpg&name=4096x4096')
        self.download_image_list(folder)

    def download_character(self):
        if self.has_content(constants.FOLDER_CHARACTER):
            return

        folder = self.create_character_directory()
        template1 = self.PAGE_PREFIX + 'wp/wp-content/themes/fena-pirate-princess/_assets/images/char/detail/char_%s_pc.png'
        template2 = self.PAGE_PREFIX + 'wp/wp-content/themes/fena-pirate-princess/_assets/images/char/ss/char%s.jpg'
        self.download_by_template(folder, template1, 3, 1)
        self.download_by_template(folder, template2, 2, 1)
        template3 = self.PAGE_PREFIX + 'char/char%s-%s.jpg'
        i = 1
        while i <= 50 and self.download_by_template(folder, template3 % (str(i).zfill(2), '%s'), 1):
            i += 1


# Komi-san wa, Comyushou desu.
class KomisanDownload(Fall2021AnimeDownload, NewsTemplate):
    title = 'Komi-san wa, Comyushou desu.'
    keywords = [title, 'Comyushou', "Komi Can't Communicate", 'komisan']
    website = 'https://komisan-official.com/'
    twitter = 'comisanvote'
    hashtags = ['komisan', '古見さん']
    folder_name = 'komisan'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_external()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            # Requires VPN to Japan Server
            json_obj = self.get_json(self.PAGE_PREFIX + 'news/wp-json/wp/v2/pages')
            for item in json_obj:
                try:
                    episode = str(int(item['acf']['number'])).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                num = 0
                self.image_list = []
                for image in item['acf']['images']:
                    num += 1
                    image_url = image['url']
                    image_name = episode + '_' + str(num)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except HTTPError as e:
            self.print_exception(e, message=None, print_traceback=False)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.news-item',
                                    date_select='span.news-item__date', title_select='span.news-item__title',
                                    id_select='a.news-item__link', a_tag_prefix=self.PAGE_PREFIX,
                                    a_tag_start_text_to_remove='/', next_page_select='a.next.page-numbers')

    def download_episode_preview_external(self):
        jp_title = '古見さんは、コミュ症です'
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20211004', download_id=self.download_id).run()

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser_tw', 'https://pbs.twimg.com/media/E1GGa52UYAU7AJu?format=jpg&name=large')
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'news/wp/wp-content/uploads/2021/08/44a6f1c5db0201b8fa7afd6a5902c770.jpg')
        self.download_image_list(folder)
        self.download_by_template(folder, self.PAGE_PREFIX + 'img/teaser/visual_%s_pc.jpg', 2, 1)

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        try:
            json_obj = self.get_json(self.PAGE_PREFIX + 'character/chara_data.php')
            if 'charas' in json_obj and isinstance(json_obj['charas'], list):
                for chara in json_obj['charas']:
                    if 'images' in chara and 'visual' in chara['images']:
                        image_url = self.PAGE_PREFIX + chara['images']['visual']
                        image_name = self.extract_image_name_from_url(image_url)
                        self.add_to_image_list(image_name, image_url)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.download_image_list(folder)


# Mieruko-chan
class MierukochanDownload(Fall2021AnimeDownload, NewsTemplate3):
    title = 'Mieruko-chan'
    keywords = [title, 'Mieruko']
    website = 'https://mierukochan.jp/'
    twitter = 'mierukochan_PR'
    hashtags = '見える子ちゃん'
    folder_name = 'mierukochan'

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
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story.html')
            episode_tags = soup.select('div.story-data')
            for episode_tag in episode_tags:
                if episode_tag.has_attr('id'):
                    try:
                        episode = str(int(episode_tag['id'].strip().replace('S', ''))).zfill(2)
                    except:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    images = episode_tag.select('div.ep-slider-sceneImage img')
                    self.image_list = []
                    for i in range(len(images)):
                        if images[i].has_attr('src'):
                            image_url = self.PAGE_PREFIX + images[i]['src'].strip().replace('./', '')
                            image_name = f'{episode}_{i + 1}'
                            self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz2_tw_1', 'https://pbs.twimg.com/media/E6aARStVcAMhcZB?format=jpg&name=medium')
        self.add_to_image_list('tz2_tw_2', 'https://pbs.twimg.com/media/E6aARTMVEAMu5YQ?format=jpg&name=medium')
        self.add_to_image_list('tz2_tw_3', 'https://pbs.twimg.com/media/FAg3dhRVgAI30y-?format=jpg&name=medium')
        self.add_to_image_list('halloween', self.PAGE_PREFIX + 'assets/top/hlwn/vis-on.png')
        self.add_to_image_list('halloween_tw', 'https://pbs.twimg.com/media/FC9KtmfagAAKVAc?format=jpg&name=large')
        self.add_to_image_list('halloween_tw2', 'https://pbs.twimg.com/media/FC9LAJcaQAAxjm_?format=jpg&name=large')
        self.download_image_list(folder)

        top_template1 = self.PAGE_PREFIX + 'assets/top/t%s/vis-on.png'
        top_template2 = self.PAGE_PREFIX + 'assets/top/t%s/vis-off.png'
        self.download_by_template(folder, [top_template1, top_template2], 1, 1)

        template = self.PAGE_PREFIX + 'assets/top/k%s/vis-on.png'
        self.download_by_template(folder, template, 1, 1, prefix='k_')

        news_template = self.PAGE_PREFIX + 'assets/news/vis-t%s.jpg'
        self.download_by_template(folder, news_template, 1, 1)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/character/c/%s.png'
        self.download_by_template(folder, template, 1, 1, prefix='char_')

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bddvd.html')
            images = soup.select('div.cont-singles img')
            self.image_list = []
            for image in images:
                if image.has_attr('src') and not image['src'].endswith('np.png'):
                    if image['src'].startswith('./'):
                        image_url = self.PAGE_PREFIX + image['src'][2:]
                    else:
                        image_url = self.PAGE_PREFIX
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Muv-Luv Alternative
class MuvLuvAlternativeDownload(Fall2021AnimeDownload, NewsTemplate):
    title = 'Muv-Luv Alternative'
    keywords = [title]
    website = 'https://muv-luv-alternative-anime.com/'
    twitter = 'Muv_Luv_A_anime'
    hashtags = ['muvluv', 'マブラヴ', 'マブラヴアニメ']
    folder_name = 'muv-luv-alt'

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
        api45_url = self.PAGE_PREFIX + 'php/avex/api.php?mode=45'
        api46_prefix = self.PAGE_PREFIX + 'php/avex/api.php?mode=46&id='
        try:
            json_obj = self.get_json(api45_url)
            if 'item' in json_obj and isinstance(json_obj['item'], list):
                for item in reversed(json_obj['item']):
                    if 'id' in item and 'title' in item:
                        id_ = item['id']
                        if len(id_) == 0:
                            continue
                        try:
                            episode = str(int(item['title'])).zfill(2)
                        except:
                            continue
                        if self.is_image_exists(episode + '_1'):
                            continue
                        try:
                            ep_obj = self.get_json(api46_prefix + str(id_))
                        except:
                            continue
                        if 'item' in ep_obj and 'contents' in ep_obj['item']:
                            contents = ep_obj['item']['contents']
                            split1 = contents.split('"')
                            if len(split1) > 2:
                                image_url = split1[-2]
                                image_name = episode + '_1'
                                self.download_image(image_url, self.base_folder + '/' + image_name)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='section.u-mg_b_l5 a',
                                    date_select='span.c-thumb-list__date', title_select='span.c-thumb-list__title',
                                    id_select=None, news_prefix='news/index.php?page=',
                                    paging_type=2, a_tag_prefix=news_url, a_tag_start_text_to_remove='./',
                                    next_page_select='i.i-arrows-angle-4-r')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('visual_1b', self.PAGE_PREFIX + 'img/home/visual_1b.jpg')
        self.download_image_list(folder)
        self.download_by_template(folder, self.PAGE_PREFIX + 'img/home/visual_%s.jpg', 1, 2)

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        character_url = self.PAGE_PREFIX + 'character/'
        try:
            json_obj = self.get_json(character_url + 'chara_data.php')
            if 'charas' in json_obj and isinstance(json_obj['charas'], list):
                for chara in json_obj['charas']:
                    if 'images' in chara:
                        images = chara['images']
                        image_urls = []
                        if 'face' in images and isinstance(images['face'], str):
                            image_urls.append(character_url + images['face'])
                        if 'visuals' in images and isinstance(images['visuals'], list):
                            for visual in images['visuals']:
                                if 'image' in visual:
                                    image_urls.append(character_url + visual['image'])
                        for image_url in image_urls:
                            image_name = self.extract_image_name_from_url(image_url)
                            self.add_to_image_list(image_name, image_url)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.download_image_list(folder)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'product/detail.php?id=1018616')
            images = soup.select('article.c-style_product img')
            self.image_list = []
            for image in images:
                if image.has_attr('src'):
                    image_url = image['src']
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Ousama Ranking
class OsamaRankingDownload(Fall2021AnimeDownload, NewsTemplate):
    title = 'Ousama Ranking'
    keywords = [title, 'Ranking of Kings', 'Osama']
    website = 'https://osama-ranking.com/'
    twitter = 'osama_ranking'
    hashtags = '王様ランキング'
    folder_name = 'osama-ranking'

    PAGE_PREFIX = website
    FINAL_EPISODE = 24

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        # self.download_episode_preview_external()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            story_url = self.PAGE_PREFIX + 'story/'
            soup = self.get_soup(story_url)
            page_lists = soup.select('ul.page_list li')
            for page_list in page_lists:
                a_tag = page_list.find('a')
                if a_tag and a_tag.has_attr('href'):
                    try:
                        episode = str(int(a_tag.text.strip())).zfill(2)
                    except:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    if page_list.has_attr('class') and 'current' in page_list['class']:
                        ep_soup = soup
                    else:
                        try:
                            a_tag_url = '?' + a_tag['href'].split('?')[1]
                        except:
                            continue
                        ep_soup = self.get_soup(story_url + a_tag_url)
                    if ep_soup:
                        images = ep_soup.select('div.slider_images img')
                        self.image_list = []
                        for i in range(len(images)):
                            if images[i].has_attr('src'):
                                image_url = story_url + images[i]['src']
                                image_name = episode + '_' + str(i + 1)
                                self.add_to_image_list(image_name, image_url)
                        self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.news_list__item',
                                    date_select='p.news_date', title_select='p.news_title', id_select='a',
                                    a_tag_prefix=news_url, a_tag_start_text_to_remove='./', paging_type=1,
                                    next_page_select='p.page_next', next_page_eval_index=0,
                                    next_page_eval_index_class='none')

    def download_episode_preview_external(self):
        jp_title = '王様ランキング'
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20211001', download_id=self.download_id).run()

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('img_kv', self.PAGE_PREFIX + 'assets/img/top/img_kv.jpg')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'assets/img/top/img_kv_%s.jpg'
        self.download_by_template(folder, template, 1, 2)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            last_id_elem = soup.select('li.chara_list__item:last-child a')
            if len(last_id_elem) > 0:
                try:
                    last_id = int(last_id_elem[len(last_id_elem) - 1]['href'].split('=')[1])
                except:
                    return
                prefix = f'{self.PAGE_PREFIX}assets/img/character/detail/'
                for i in range(last_id):
                    num = i + 1
                    filename1 = f'img_chara{str(num).zfill(2)}.png'
                    filename2 = f'cha_sub{str(num).zfill(2)}.png'
                    filename3 = f'img_scene_{num}.jpg'
                    if self.is_image_exists(filename3[0:len(filename3) - 4], folder)\
                            or self.is_image_exists(filename2[0:len(filename2) - 4], folder)\
                            or self.is_image_exists(filename1[0:len(filename1) - 4], folder):
                        continue
                    self.download_image(prefix + filename1, folder + '/' + filename1[0:len(filename1) - 4])
                    self.download_image(prefix + filename2, folder + '/' + filename2[0:len(filename2) - 4])
                    template = f'{prefix}cha_sub{str(num).zfill(2)}_%s.png'
                    self.download_by_template(folder, template, 1, 1)
                    self.download_image(prefix + filename3, folder + '/' + filename3[0:len(filename3) - 4])
        except Exception as e:
            self.print_exception(e, 'Character')


# Platinum End
class PlatinumEndDownload(Fall2021AnimeDownload, NewsTemplate):
    title = 'Platinum End'
    keywords = [title]
    website = 'https://anime-platinumend.com/'
    twitter = 'ani_platinumend'
    hashtags = ['プラチナエンド', 'PlatinumEnd']
    folder_name = 'platinum-end'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 8

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_guess()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            a_tags = soup.select('li.story_List_Item a')
            for a_tag in a_tags:
                if a_tag.has_attr('href'):
                    try:
                        episode = str(int(a_tag.text.strip())).zfill(2)
                    except:
                        continue
                    if self.is_image_exists(f'{episode}_1'):
                        continue
                    if a_tag.has_attr('class') and 'current' in a_tag['class']:
                        ep_soup = soup
                    else:
                        ep_soup = self.get_soup(a_tag['href'])
                    images = ep_soup.select('div.story_Img img')
                    self.image_list = []
                    for i in range(len(images)):
                        if images[i].has_attr('src'):
                            image_url = self.clear_resize_in_url(images[i]['src'])
                            image_name = f'{episode}_{i + 1}'
                            self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wp/wp-content/uploads/%s/%s/%s.png'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        for i in range(self.FINAL_EPISODE):
            if self.is_image_exists(f'{year}{month}_{i}_1', folder):
                continue
            stop = False
            for j in range(self.IMAGES_PER_EPISODE):
                img_name = str(j + 1).zfill(2)
                if i == 0:
                    image_url = template % (year, month, img_name)
                else:
                    image_url = template % (year, month, img_name + '-' + str(i))
                image_name = f'{year}{month}_{i}_{j + 1}'
                result = self.download_image(image_url, folder + '/' + image_name)
                if result == -1:
                    stop = True
                    break
                is_successful = True
            if stop:
                break
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.sw-News_List_Item',
                                    date_select='p.date', title_select='p.ttl-txt', id_select='a',
                                    next_page_select='a.nextpostslink')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv2', self.PAGE_PREFIX + 'wp/wp-content/uploads/2021/06/Platinum_End_KV02_WEB.jpg')
        self.add_to_image_list('kv3', self.PAGE_PREFIX + 'wp/wp-content/uploads/2021/08/Platinum_End_KV3_b.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            a_tags = soup.select('li.character_List_Item a')
            prefix = self.PAGE_PREFIX + 'wp/wp-content/themes/platinumend_v0/assets/images/common/character/'
            template1 = prefix + 'body_%s.png'
            template2 = prefix + 'face_%s.png'
            for a_tag in a_tags:
                if a_tag.has_attr('href'):
                    if 'character/' in a_tag['href']:
                        name = a_tag['href'].split('character/')[1]
                        if name.endswith('/'):
                            name = name[0:len(name) - 1]
                        if self.is_image_exists(f'body_{name}'):
                            continue
                        result = self.download_image(template1 % name, f'{folder}/body_{name}')
                        if result != -1:
                            template_url = template1 % (name + '%s')
                            self.download_by_template(folder, template_url, 1, 2)
                        self.download_image(template2 % name, f'{folder}/face_{name}')
        except Exception as e:
            self.print_exception(e, 'Character')


# Saihate no Paladin
class SaihatenoPaladinDownload(Fall2021AnimeDownload, NewsTemplate):
    title = 'Saihate no Paladin'
    keywords = [title, 'The Faraway Paladin']
    website = 'https://farawaypaladin.com/'
    twitter = 'faraway_paladin'
    hashtags = ['faraway_paladin', '最果てのパラディン']
    folder_name = 'saihate-no-paladin'

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
            soup = self.get_soup(self.PAGE_PREFIX + 'story')
            posts = soup.select('div.post')
            for post in posts:
                h1_tag = post.find('h1')
                try:
                    episode = str(int(h1_tag.text.strip().split('第')[1].split('話')[0])).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                ul = post.find('ul')  # Get first ul tag
                if ul:
                    images = ul.select('img')
                    self.image_list = []
                    for i in range(len(images)):
                        if images[i].has_attr('src'):
                            image_url = self.clear_resize_in_url(images[i]['src'])
                            image_name = episode + '_' + str(i + 1)
                            self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='#news dd', date_select='i',
                                    title_select='span', id_select='a', a_tag_prefix=news_url)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv1', 'https://pbs.twimg.com/media/EzKrTkqVkAMxXZW?format=jpg&name=large')
        self.add_to_image_list('main_visual-min', self.PAGE_PREFIX + 'img/main_visual-min.png')
        self.add_to_image_list('kv2', 'https://aniverse-mag.com/wp-content/uploads/2021/09/KV2_anime.jpg')
        self.add_to_image_list('kv2_tw', 'https://pbs.twimg.com/media/FAMziUqVgAk-p8A?format=jpg&name=large')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'img/cara%s.png'
        self.download_by_template(folder, template, 1)
        template2 = self.PAGE_PREFIX + 'img/main_c%s.png'
        self.download_by_template(folder, template2, 1)


# Sakugan
class SakuganDownload(Fall2021AnimeDownload, NewsTemplate):
    title = 'Sakugan'
    keywords = [title]
    website = 'http://sakugan-anime.com/'
    twitter = 'ANIMA_info'
    hashtags = 'サクガン'
    folder_name = 'sakugan'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        first_episode_url = self.PAGE_PREFIX + 'story/story01.html'
        try:
            soup = self.get_soup(first_episode_url)
            a_tags = soup.select('ul.num li a')
            for a_tag in a_tags:
                if not a_tag.has_attr('href'):
                    continue
                try:
                    episode = str(int(a_tag.text.strip())).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if a_tag['href'] != first_episode_url:
                    ep_soup = self.get_soup(a_tag['href'])
                else:
                    ep_soup = soup
                images = ep_soup.select('ul.story_slider img')
                self.image_list = []
                for i in range(len(images)):
                    if images[i].has_attr('src'):
                        src = images[i]['src']
                        image_url = self.PAGE_PREFIX + (src[1:] if src.startswith('/') else src)
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ul.tile li',
                                    date_select='time', title_select='p.txt a', id_select='a',
                                    news_prefix='topics/', next_page_select='a.nextpostslink')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('mv', self.PAGE_PREFIX + 'wp-content/themes/sakugan_theme/img/top/mv.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character')
            images = soup.select('ul.character_slider img')
            self.image_list = []
            for image in images:
                if image.has_attr('src'):
                    image_url = self.PAGE_PREFIX + (image['src'][1:] if image['src'].startswith('/') else image['src'])
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Sekai Saikou no Ansatsusha, Isekai Kizoku ni Tensei suru
class AnsatsuKizokuDownload(Fall2021AnimeDownload, NewsTemplate):
    title = 'Sekai Saikou no Ansatsusha, Isekai Kizoku ni Tensei suru'
    keywords = [title, "The world's best assassin, To reincarnate in a different world aristocrat"]
    website = 'https://ansatsu-kizoku.jp/'
    twitter = 'ansatsu_kizoku'
    hashtags = '暗殺貴族'
    folder_name = 'ansatsu-kizoku'

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
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            divs = soup.select('div.episode')
            for div in divs:
                span_tag = div.select('span.number')
                try:
                    episode = str(int(span_tag[0].text.strip().replace('#', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                images = div.select('li.swiper-slide img')
                self.image_list = []
                for i in range(len(images)):
                    if images[i].has_attr('src'):
                        image_src = images[i]['src']
                        image_url = self.PAGE_PREFIX + \
                            self.clear_resize_in_url(image_src[1:] if image_src.startswith('/') else image_src)
                        image_name = f'{episode}_{i + 1}'
                        self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='div.news-Index li a',
                                    date_select='div.date', title_select='p', id_select=None,
                                    next_page_select='a.nextpostslink')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        #self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/Ev27c7bUUAIM_47?format=jpg&name=medium')
        #self.download_image_list(folder)
        template = self.PAGE_PREFIX + 'wp-content/themes/ansatsu-kizoku/assets/images/common/index/img_keyvisual_%s.jpg'
        self.download_by_template(folder, template, 1, 1)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp-content/themes/ansatsu-kizoku_teaser/assets/images/common/img_character_%s.png'
        self.download_by_template(folder, template, 1)

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)

        # Blu-ray Bonus
        try:
            for page in ['shopbonus', 'vol1', 'vol2', 'vol3']:
                if page[-1].isnumeric() and int(page[-1]) > 1 and page in processed:
                    continue
                soup = self.get_soup(f'{self.PAGE_PREFIX}goods/bd-dvd/{page}')
                if soup:
                    images = soup.select('.subpage-Body img')
                    self.image_list = []
                    for image in images:
                        if image.has_attr('src'):
                            image_url = image['src']
                            image_name = self.extract_image_name_from_url(image_url)
                            if self.is_image_exists(image_name, folder):
                                if not self.is_content_length_same_as_existing(
                                        image_url, image_name, folder):
                                    print(f'{self.__class__.__name__} - {image_name} has different size')
                                continue
                            self.add_to_image_list(image_name, image_url)
                    if page[-1].isnumeric() and int(page[-1]) > 1 and len(self.image_list) > 0:
                        processed.append(page)
                    self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray Bonus')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Senpai ga Uzai Kouhai no Hanashi
class SenpaigaUzaiDownload(Fall2021AnimeDownload, NewsTemplate):
    title = 'Senpai ga Uzai Kouhai no Hanashi'
    keywords = [title]
    website = 'https://senpaiga-uzai-anime.com/'
    twitter = 'uzai_anime'
    hashtags = '先輩がうざい後輩の話'
    folder_name = 'senpaigauzai'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 8

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            template = f'{self.PAGE_PREFIX}images/story/img_{episode}_%s.jpg'
            for j in range(self.IMAGES_PER_EPISODE):
                image_url = template % str(j + 1).zfill(2)
                image_name = episode + '_' + str(j + 1)
                result = self.download_image(image_url, f'{self.base_folder}/{image_name}')
                if result == -1:
                    return

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.foo',
                                    date_select='time', title_select='h3', id_select=None, id_has_id=True)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('main-visual', self.PAGE_PREFIX + 'img/top/main-visual.png')
        self.add_to_image_list('visual', 'https://pbs.twimg.com/media/Ez4yUbfVkAMPgny?format=jpg&name=4096x4096')
        self.add_to_image_list('mainimg', self.PAGE_PREFIX + 'images/top/mainimg.jpg')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/E8gG12BVkAEMaF_?format=jpg&name=large')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template1 = self.PAGE_PREFIX + 'images/character/img_chara_%s.png'
        template2 = self.PAGE_PREFIX + 'images/character/img_face_%s.png'
        self.download_by_template(folder, [template1, template2], 2, 1)

    def download_media(self):
        folder = self.create_media_directory()
        self.image_list = []
        self.add_to_image_list('img_jacket_op', self.PAGE_PREFIX + 'images/music/img_jacket_op.jpg')
        self.add_to_image_list('img_photo_op', self.PAGE_PREFIX + 'images/music/img_photo_op.jpg')
        self.download_image_list(folder)

        # Blu-ray
        bd_prefix = self.PAGE_PREFIX + 'blu-ray/'
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            for i in range(5):
                if i > 1:
                    page_name = str(i).zfill(2) + '.html'
                    if page_name in processed:
                        continue
                elif i == 0:
                    page_name = 'tokuten.html'
                else:
                    page_name = ''
                bd_url = bd_prefix + page_name
                bd_soup = self.get_soup(bd_url)
                if bd_soup:
                    images = bd_soup.select('section.blu-ray img')
                    self.image_list = []
                    for image in images:
                        if image.has_attr('src') and 'nowprinting' not in image['src']:
                            image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                            image_name = self.extract_image_name_from_url(image_url)
                            self.add_to_image_list(image_name, image_url)
                    if i > 1 and len(self.image_list) > 0:
                        processed.append(page_name)
                    if i > 0 and len(self.image_list) == 0:
                        break
        except Exception as e:
            self.print_exception(e, 'Blu-ray')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Shin no Nakama ja Nai to Yuusha no Party wo Oidasareta node, Henkyou de Slow Life suru Koto ni Shimashita
class ShinnoNakamaDownload(Fall2021AnimeDownload, NewsTemplate):
    title = 'Shin no Nakama ja Nai to Yuusha no Party wo Oidasareta node, Henkyou de Slow Life suru Koto ni Shimashita'
    keywords = [title, 'Shinnonakama', "Banished From The Heroes' Party"]
    website = 'https://shinnonakama.com/'
    twitter = 'shinnonakama_tv'
    hashtags = '真の仲間'
    folder_name = 'shinnonakama'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_external()
        self.download_episode_preview_guess()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + '/story/')
            a_tags = soup.select('li.story_tabList a')
            for index in range(len(a_tags)):
                try:
                    episode = str(int(a_tags[index].text.replace('第', '').replace('話', '').strip())).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if a_tags[index].has_attr('data-tab'):
                    images = soup.select(f'li.story_tabDetail.{a_tags[index]["data-tab"]} img')
                    self.image_list = []
                    for i in range(len(images)):
                        if images[i].has_attr('src'):
                            image_url = self.PAGE_PREFIX + images[i]['src'].replace('../', '')
                            image_name = f'{episode}_{i + 1}'
                            self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ul.newsListsWrap li',
                                    date_select='p.update_time', title_select='p.update_ttl',
                                    id_select='a', a_tag_prefix=news_url, a_tag_start_text_to_remove='./')

    def download_episode_preview_external(self):
        jp_title = '真の仲間じゃないと勇者のパーティーを追い出されたので、辺境でスローライフすることにしました'
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20210922', download_id=self.download_id).run()

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        is_successful = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            template = f'{self.PAGE_PREFIX}assets/img/story/story{episode}_%s.jpg'
            for j in range(self.IMAGES_PER_EPISODE):
                image_url = template % str(j + 1).zfill(2)
                image_name = episode + '_' + str(j + 1)
                result = self.download_image(image_url, f'{folder}/{image_name}')
                if result == -1:
                    return
                elif result == 0:
                    is_successful = True
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed successfully!')
        return is_successful

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', 'https://ogre.natalie.mu/media/news/comic/2021/0120/shin_no_nakama_teaser.jpg')
        self.add_to_image_list('kv2_tw', 'https://pbs.twimg.com/media/E1zuDLNVcAcaAwX?format=jpg&name=4096x4096')
        self.add_to_image_list('kv2', self.PAGE_PREFIX + 'assets/img/top/kv2.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/img/top/character/chara_%s.png'
        self.download_by_template(folder, template, 1, 1)

    def download_media(self):
        folder = self.create_media_directory()
        # Blu-ray
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bddvd/')
            images = soup.select('.inPageContent img')
            self.image_list = []
            for image in images:
                if image.has_attr('src') and not image['src'].endswith('/now.jpg'):
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Shinka no Mi: Shiranai Uchi ni Kachigumi Jinsei
class ShinkanomiDownload(Fall2021AnimeDownload, NewsTemplate):
    title = 'Shinka no Mi: Shiranai Uchi ni Kachigumi Jinsei'
    keywords = [title, 'Shinkanomi']
    website = 'https://www.shinkanomi-anime.com'
    twitter = 'shinkanomianime'
    hashtags = ['進化の実', '勝ち組人生', 'ゴリラ系女子']
    folder_name = 'shinkanomi'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 5

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_guess()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + '/story/')
            ep_nums = soup.select('.js_episode-num .episode-num__item')
            ep_list = soup.select('.js_episode-list .episode-list__item')
            if len(ep_nums) == len(ep_list):
                for index in range(len(ep_nums)):
                    try:
                        episode = str(int(ep_nums[index].text.strip()[1:3])).zfill(2)
                    except:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    images = ep_list[index].select('img')
                    self.image_list = []
                    for i in range(len(images)):
                        if images[i].has_attr('src'):
                            image_url = images[i]['src']
                            image_name = f'{episode}_{i + 1}'
                            self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
            else:
                raise Exception("Expected ep_num == ep_list")
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + '/cms/wp-content/uploads/%s/%s/%s_%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            stop = False
            for j in range(self.IMAGES_PER_EPISODE):
                image_url = template % (year, month, episode, str(j + 1).zfill(3))
                image_name = f'{episode}_{j + 1}'
                result = self.download_image(image_url, folder + '/' + image_name)
                if result == -1:
                    stop = True
                    break
                is_successful = True
            if stop:
                break
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ul.news-list li.news-list__item',
                                    date_select='span.news-list__date', title_select='h2.news-list__title',
                                    id_select='a', next_page_select='div.pagination .page-numbers',
                                    next_page_eval_index_class='current', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/E52FLnzUcAEMg80?format=jpg&name=medium')
        self.add_to_image_list('kv1_1', self.PAGE_PREFIX + '/cms/wp-content/uploads/2021/08/2.jpg')
        self.add_to_image_list('kv1_2', self.PAGE_PREFIX + '/cms/wp-content/uploads/2021/08/3.jpg')
        self.add_to_image_list('kv2_1', self.PAGE_PREFIX + '/img/top/kv-ver2.jpg')
        self.add_to_image_list('kv2_2', self.PAGE_PREFIX + '/cms/wp-content/uploads/2021/09/KV2_.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + '/character/')
            images = soup.select('ul.character-list img')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Taishou Otome Otogibanashi
class TaishoOtomeDownload(Fall2021AnimeDownload, NewsTemplate):
    title = 'Taishou Otome Otogibanashi'
    keywords = [title, 'Taisho Otome']
    website = 'http://taisho-otome.com/'
    twitter = 'otome_otogi'
    hashtags = ['大正オトメ', '昭和オトメ']
    folder_name = 'taisho-otome'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        # self.download_episode_preview_external()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            first_episode_url = self.PAGE_PREFIX + 'story/01'
            soup = self.get_soup(first_episode_url)
            a_tags = soup.select('ul.l_storynav a')
            for a_tag in a_tags:
                if a_tag.has_attr('href'):
                    try:
                        ep_num = self.convert_kanji_to_number(a_tag.text.strip().replace('第', '').replace('話', ''))
                        episode = str(ep_num).zfill(2)
                    except:
                        continue
                    episode_url = a_tag['href']
                    if self.is_image_exists(episode + '_1'):
                        continue
                    if episode_url == first_episode_url:
                        ep_soup = soup
                    else:
                        ep_soup = self.get_soup(episode_url)
                    if ep_soup:
                        images = ep_soup.select('ul.js_previewslider img')
                        self.image_list = []
                        for i in range(len(images)):
                            if images[i].has_attr('src'):
                                src = images[i]['src']
                                image_url = self.PAGE_PREFIX + (src[1:] if src.startswith('/') else src)
                                image_name = episode + '_' + str(i + 1)
                                self.add_to_image_list(image_name, image_url)
                        self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ul.newslist li',
                                    date_select='div.newslist_date', title_select='h2.newslist_ttl', id_select='a',
                                    date_func=lambda x: x.replace('年', '.').replace('月', '.').replace('日', ''),
                                    next_page_select='li.pagination_list_item__next')

    def download_episode_preview_external(self):
        jp_title = '大正オトメ御伽話'
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20211005', download_id=self.download_id).run()

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/taisho-otome/img/index/%s.jpg'
        template_name = 'img_kv%s'
        self.image_list = []
        self.add_to_image_list(template_name % '01', template % (template_name % '01'))
        self.add_to_image_list(template_name % '02', template % (template_name % '02'))
        self.add_to_image_list(template_name % '03', template % (template_name % '03'))
        self.add_to_image_list('kv03_tw', 'https://pbs.twimg.com/media/E5TLvmFVkAAV8Oj?format=jpg&name=medium')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/taisho-otome/img/character/img_chara%s.png'
        self.download_by_template(folder, template, 2)

    def download_media(self):
        folder = self.create_media_directory()
        for page in ['bluray/store-benefits', 'bluray/vol1', 'bluray/vol2',
                     'music/1st-op1', 'music/1st-ed1', 'music/soundtrack']:
            page_url = f'{self.PAGE_PREFIX}{page}/'
            try:
                soup = self.get_soup(page_url)
                images = soup.select('.productinfo .js_imgload')
                self.image_list = []
                for image in images:
                    if image.has_attr('data-imgload') and 'comingsoon' not in image['data-imgload']:
                        image_url = image['data-imgload']
                        if image_url.startswith('/'):
                            image_url = self.PAGE_PREFIX + image_url[1:]
                        image_name = self.extract_image_name_from_url(image_url)
                        self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Media {page_url}')


# takt op.Destiny
class TaktOpDestinyDownload(Fall2021AnimeDownload, NewsTemplate):
    title = 'takt op.Destiny'
    keywords = [title]
    website = 'https://anime.takt-op.jp/'
    twitter = 'takt_op_destiny'
    hashtags = ['takt_op_Destiny', 'タクトオーパス']
    folder_name = 'takt-op'

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
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            a_tags = soup.select('div.archive li a')
            for a_tag in a_tags:
                if a_tag.has_attr('href'):
                    try:
                        episode = str(int(a_tag['href'].split('-')[-1])).zfill(2)
                    except:
                        continue
                    if self.is_image_exists(f'{episode}_1'):
                        continue
                    ep_soup = self.get_soup(a_tag['href'])
                    if ep_soup:
                        images = ep_soup.select('div.swiper li.swiper-slide img')
                        self.image_list = []
                        for i in range(len(images)):
                            if images[i].has_attr('src'):
                                image_url = self.clear_resize_in_url(images[i]['src'])
                                image_name = f'{episode}_{i + 1}'
                                self.add_to_image_list(image_name, image_url)
                        self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='div.sw-NewsArchive li',
                                    date_select='div.date', title_select='div.title p', id_select='a',
                                    date_func=lambda x: x[0:4] + '.' + x[4:],
                                    next_page_select='a.nextpostslink')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.add_to_image_list('teaser_tw', 'https://pbs.twimg.com/media/E44RbYeVIAIlAFB?format=jpg&name=4096x4096')
        self.add_to_image_list('main_visual', 'https://pbs.twimg.com/media/E-hPi0mVkAY0K_g?format=jpg&name=4096x4096')
        self.add_to_image_list('img_kv_2', self.PAGE_PREFIX + 'wp-content/themes/takt-op/assets/images/common/index/img_kv_2.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            a_tags = soup.select('div.character-Index a')
            prefix = self.PAGE_PREFIX + 'wp-content/themes/takt-op/assets/images/common/character/'
            template1 = prefix + '%s/img.png'
            template2 = prefix + '%s/img_close-up.png'
            for a_tag in a_tags:
                if a_tag.has_attr('href'):
                    if 'character/' in a_tag['href']:
                        name = a_tag['href'].split('character/')[1]
                        if name.endswith('/'):
                            name = name[0:len(name) - 1]
                        if self.is_image_exists(f'img_{name}'):
                            continue
                        self.download_image(template1 % name, f'{folder}/img_{name}')
                        self.download_image(template2 % name, f'{folder}/img_close-up_-{name}')
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        self.download_media_helper('category/bd/', 'div.archive img', 'Blu-ray', folder)
        self.download_media_helper('item-bluray01', 'div.body img', 'Blu-ray Bonus', folder)
        self.download_media_helper('category/cd-streaming/', 'div.archive img', 'Music', folder)

    def download_media_helper(self, url, select, message, folder):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'products/' + url)
            images = soup.select(select)
            self.image_list = []
            for image in images:
                if image.has_attr('src') and not image['src'].endswith('/thumb.jpg'):
                    image_url = self.clear_resize_in_url(image['src'])
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, message)


# Tsuki to Laika to Nosferatu
class TsukiLaikaNosferatuDownload(Fall2021AnimeDownload, NewsTemplate):
    title = 'Tsuki to Laika to Nosferatu'
    keywords = [title]
    website = 'https://tsuki-laika-nosferatu.com/'
    twitter = 'LAIKA_anime'
    hashtags = '月とライカ'
    folder_name = 'tsuki-laika-nosferatu'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 8

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_guess()
        self.download_episode_preview_external()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story')
            nav_btns = soup.select('a.story-nav-btn')
            for btn in nav_btns:
                if btn.has_attr('href'):
                    try:
                        episode = str(int(btn.text.strip().replace('第', '').replace('話', ''))).zfill(2)
                    except:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    ep_soup = self.get_soup(btn['href'])
                    images = ep_soup.select('li.story-detail-thumb-box img')
                    self.image_list = []
                    for i in range(len(images)):
                        if images[i].has_attr('src'):
                            image_url = images[i]['src']
                            image_name = f'{episode}_{(i + 1)}'
                            self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_guess(self):
        # Can only run this in year 2021
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'Nr7R6svx/wp-content/uploads/2021/%s/%s.jpg'
        is_successful = False
        curr_month = (datetime.now() + timedelta(hours=1)).strftime('%m')
        for k in range(9, 13, 1):
            month = str(k).zfill(2)
            if curr_month > month and self.is_image_exists(f'{k + 1}_0_1', folder):
                continue
            for i in range(self.FINAL_EPISODE):
                if self.is_image_exists(f'{month}_{i}_1', folder):
                    continue
                stop = False
                for j in range(self.IMAGES_PER_EPISODE):
                    img_name = 'main' if j == 0 else f'sub{j}'
                    if i == 0:
                        image_url = template % (month, img_name)
                    else:
                        image_url = template % (month, f'{img_name}-{i}')
                    image_name = f'{month}_{i}_{j + 1}'
                    result = self.download_image(image_url, folder + '/' + image_name)
                    if j == 0 and result == -1:
                        stop = True
                        break
                    is_successful = True
                if stop:
                    break
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful

    def download_episode_preview_external(self):
        jp_title = '月とライカと吸血姫'
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20210917', download_id=self.download_id).run()

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.news-box',
                                    date_select='p.news-box-date', title_select='h3.news-box-ttl', id_select='a',
                                    next_page_select='ul.pagenation-list li',
                                    next_page_eval_index_class='is__current', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        template = self.PAGE_PREFIX + 'Nr7R6svx/wp-content/themes/laika_tpl_v%s/assets/img/top/visual.jpg'
        self.add_to_image_list('teaser', template % '0')
        self.add_to_image_list('teaser_tw', 'https://pbs.twimg.com/media/EwpkNbsUUAAX00O?format=jpg&name=medium')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/E6uztaAVUAU40vC?format=jpg&name=medium')
        self.download_image_list(folder)

        try:
            for i in range(20):
                image_url = template % str(i + 1)
                image_name = 'kv' + str(i + 1)
                result = self.download_image(image_url, folder + '/' + image_name)
                if result == -1:
                    break
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'Nr7R6svx/wp-content/themes/laika_tpl_v1/assets/img/character/%s.png'
        self.download_by_template(folder, template, 1, 0, prefix='char_')

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'products/cd')
            a_tags = soup.select('a.products-box-link')
            for a_tag in a_tags:
                if a_tag.has_attr('href'):
                    cover_image = a_tag.find('img')
                    if cover_image and cover_image.has_attr('src') and 'nowprinting' not in cover_image['src']:
                        try:
                            page_id = a_tag['href'].split('?p=')[1]
                        except:
                            continue
                        if page_id in processed:
                            continue
                        cd_soup = self.get_soup(a_tag['href'])
                        if cd_soup:
                            images = cd_soup.select('li.products-detail-thumb-nav-box img')
                            self.image_list = []
                            for image in images:
                                if image.has_attr('src') and len(image['src']) > 0\
                                        and 'nowprinting' not in image['src']:
                                    image_url = image['src'].replace('-scaled.jpg', '.jpg')
                                    image_name = self.extract_image_name_from_url(image_url)
                                    self.add_to_image_list(image_name, image_url)
                            if len(self.image_list) > 0:
                                processed.append(page_id)
                            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Music')
        self.create_cache_file(cache_filepath, processed, num_processed)

        # Blu-ray
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'products/bd')
            a_tags = soup.select('a.products-box-link')
            count = 0
            for a_tag in a_tags:
                count += 1
                if a_tag.has_attr('href'):
                    cover_image = a_tag.find('img')
                    if cover_image and cover_image.has_attr('src') and 'nowprinting' not in cover_image['src'].lower():
                        cover_image_url = cover_image['src']
                        cover_image_name = self.extract_image_name_from_url(cover_image_url)
                        if count > 1 and self.is_image_exists(cover_image_name, folder):  # Always evaluate first one
                            continue
                        bd_soup = self.get_soup(a_tag['href'])
                        if bd_soup:
                            selector = 'li.products-detail-thumb-nav-box img, .products-detail-tokuten-container img'
                            images = bd_soup.select(selector)
                            self.image_list = []
                            for image in images:
                                if image.has_attr('src') and len(image['src']) > 0\
                                        and 'nowprinting' not in image['src']:
                                    image_url = self.clear_resize_in_url(image['src'])
                                    image_name = self.extract_image_name_from_url(image_url)
                                    self.add_to_image_list(image_name, image_url)
                            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Yuuki Yuuna wa Yuusha de Aru: Dai Mankai no Shou
class Yuyuyu3Download(Fall2021AnimeDownload, NewsTemplate):
    title = "Yuuki Yuuna wa Yuusha de Aru: Dai Mankai no Shou"
    keywords = [title, "Yuyuyu", "Yuki Yuna is a Hero"]
    website = 'https://yuyuyu.tv/daimankai/'
    twitter = 'anime_yukiyuna'
    hashtags = 'yuyuyu'
    folder_name = 'yuyuyu3'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_external()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        story_url = self.PAGE_PREFIX + 'story/'
        try:
            stories = self.get_json(self.PAGE_PREFIX + 'story/episode_data.php')
            for story in stories:
                try:
                    episode = str(int(story['id'])).zfill(2)
                except Exception:
                    continue
                stories = story['images']
                self.image_list = []
                for i in range(len(stories)):
                    image_url = story_url + stories[i].split('?')[0]
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        prefix = 'https://yuyuyu.tv'
        self.download_template_news(page_prefix=prefix, article_select='article.c-entry-item',
                                    date_select='span.c-entry-date', title_select='h1.c-entry-item__title',
                                    id_select='a', stop_date='2021.01.29', a_tag_prefix=prefix,
                                    next_page_select='a.next.page-numbers')

    def download_episode_preview_external(self):
        jp_title = '結城友奈は勇者である'
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20210930', download_id=self.download_id).run()

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tw_visual1', 'https://pbs.twimg.com/media/EeUu6NHVAAAqYgu?format=jpg&name=large')
        self.add_to_image_list('tw_visual2', 'https://pbs.twimg.com/media/E0L1PAhVEAICS7o?format=jpg&name=4096x4096')
        self.download_image_list(folder)
        self.download_by_template(folder, 'https://yuyuyu.tv/season2/img/home/visual_%s.jpg', 2, 10)
        # self.download_by_template(folder, self.PAGE_PREFIX + 'img/home/visual_%s.jpg', 2, 1)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('visual-image')
            self.image_list = []
            for image in images:
                if image.has_attr('image'):
                    image_url = self.PAGE_PREFIX + image['image']
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        chara_url = self.PAGE_PREFIX + 'character/'
        self.image_list = []
        try:
            json_obj = self.get_json(chara_url + 'chara_data.php')
            if 'charas' in json_obj and isinstance(json_obj['charas'], list):
                for chara in json_obj['charas']:
                    if 'images' in chara and 'visuals' in chara['images'] and \
                            isinstance(chara['images']['visuals'], list):
                        for visual in chara['images']['visuals']:
                            if 'image' in visual:
                                image_url = chara_url + visual['image']
                                image_name = self.extract_image_name_from_url(image_url)
                                self.add_to_image_list(image_name, image_url)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.download_image_list(folder)

    def download_media(self):
        folder = self.create_media_directory()
        product_url = self.PAGE_PREFIX + 'product/'
        try:
            soup = self.get_soup(product_url)
            cards = soup.select('article.c-card')
            for card in cards:
                a_tag = card.find('a')
                image_tag = card.find('img')
                has_valid_image = False
                head_image_url = head_image_name = ''
                if image_tag is not None and image_tag.has_attr('data-src') and len(image_tag['data-src']) > 0:
                    data_src = image_tag['data-src']
                    if data_src.startswith('./'):
                        head_image_url = product_url + data_src[2:]
                    elif data_src.startswith('../'):
                        head_image_url = self.PAGE_PREFIX + data_src[3:]
                    else:
                        head_image_url = data_src
                    head_image_name = self.extract_image_name_from_url(head_image_url)
                    if 'np_bd' not in head_image_name:
                        has_valid_image = True

                # Blu-ray Page
                if a_tag is not None and a_tag.has_attr('href') and a_tag['href'].startswith('bd/') and has_valid_image:
                    bd_url = product_url + a_tag['href']
                    bd_soup = self.get_soup(bd_url)
                    if bd_soup is not None:
                        self.image_list = []
                        images = bd_soup.select('article img')
                        for image in images:
                            if image.has_attr('data-src'):
                                image_url = bd_url + image['data-src']
                                image_name = self.extract_image_name_from_url(image_url)
                                self.add_to_image_list(image_name, image_url)
                        spans = bd_soup.select('span.c-bgimg')
                        for span in spans:
                            if span.has_attr('data-bg') and span['data-bg'].startswith('../../../'):
                                image_url = self.PAGE_PREFIX + span['data-bg'][9:]
                                image_name = self.extract_image_name_from_url(image_url)
                                if 'np_cd' not in image_name:
                                    self.add_to_image_list(image_name, image_url)
                        self.download_image_list(folder)
                elif has_valid_image and len(head_image_url) > 0 and len(head_image_name) > 0\
                        and not self.is_image_exists(head_image_name, folder):
                    self.download_image(head_image_url, f'{folder}/{head_image_name}')
        except Exception as e:
            self.print_exception(e, 'Media')
