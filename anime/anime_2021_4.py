import os
import anime.constants as constants
from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate3
from datetime import datetime, timedelta
from scan import AniverseMagazineScanner, MocaNewsScanner, WebNewtypeScanner


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
# Shuumatsu no Harem https://end-harem-anime.com/ #終末のハーレム @harem_official_
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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ul.news-list li.news-item',
                                    date_select='p.news-date', title_select='p.news-title', id_select='a',
                                    next_page_select='div.pagination a.next',
                                    next_page_eval_index_class='off', next_page_eval_index=0)

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

    PAGE_PREFIX = 'https://www.jp.square-enix.com/deepinsanity/'

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
        self.add_to_image_list('kv_tw', 'https://pbs.twimg.com/media/E_eipEAVUAQwHQh?format=jpg&name=4096x4096')
        self.add_to_image_list('anime_kv', self.PAGE_PREFIX + 'assets/images/anime/anime_kv.png')
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

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

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
        self.has_website_updated(self.PAGE_PREFIX)

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
            print("Error in running " + self.__class__.__name__ + ' - Blu-ray')
            print(e)
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

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index', diff=2)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.news-item',
                                    date_select='span.news-item__date', title_select='span.news-item__title',
                                    id_select='a.news-item__link', a_tag_prefix=self.PAGE_PREFIX,
                                    a_tag_start_text_to_remove='/', next_page_select='a.next.page-numbers')

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
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)
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

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz2_tw_1', 'https://pbs.twimg.com/media/E6aARStVcAMhcZB?format=jpg&name=medium')
        self.add_to_image_list('tz2_tw_2', 'https://pbs.twimg.com/media/E6aARTMVEAMu5YQ?format=jpg&name=medium')
        self.download_image_list(folder)

        top_template1 = self.PAGE_PREFIX + 'assets/top/t%s/vis-on.png'
        top_template2 = self.PAGE_PREFIX + 'assets/top/t%s/vis-off.png'
        self.download_by_template(folder, [top_template1, top_template2], 1, 1)

        news_template = self.PAGE_PREFIX + 'assets/news/vis-t%s.jpg'
        self.download_by_template(folder, news_template, 1, 1)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/character/c/%s.png'
        self.download_by_template(folder, template, 1, 1, prefix='char_')


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

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index', diff=2)

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
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)
        self.download_image_list(folder)


# Ousama Ranking
class OsamaRankingDownload(Fall2021AnimeDownload, NewsTemplate):
    title = 'Ousama Ranking'
    keywords = [title, 'Ranking of Kings', 'Osama']
    website = 'https://osama-ranking.com/'
    twitter = 'osama_ranking'
    hashtags = '王様ランキング'
    folder_name = 'osama-ranking'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.news_list__item',
                                    date_select='p.news_date', title_select='p.news_title', id_select='a',
                                    a_tag_prefix=news_url, a_tag_start_text_to_remove='./', paging_type=1,
                                    next_page_select='p.page_next', next_page_eval_index=0,
                                    next_page_eval_index_class='none')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('img_kv', self.PAGE_PREFIX + 'assets/img/top/img_kv.jpg')
        self.add_to_image_list('img_kv_2', self.PAGE_PREFIX + 'assets/img/top/img_kv_2.jpg')
        self.download_image_list(folder)

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
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)


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
            print("Error in running " + self.__class__.__name__)
            print(e)

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
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)


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
        self.has_website_updated(self.PAGE_PREFIX, 'index')

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
            print("Error in running " + self.__class__.__name__)
            print(e)

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
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)


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

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

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


# Shin no Nakama ja Nai to Yuusha no Party wo Oidasareta node, Henkyou de Slow Life suru Koto ni Shimashita
class ShinnoNakamaDownload(Fall2021AnimeDownload, NewsTemplate):
    title = 'Shin no Nakama ja Nai to Yuusha no Party wo Oidasareta node, Henkyou de Slow Life suru Koto ni Shimashita'
    keywords = [title, 'Shinnonakama', "Banished From The Heroes' Party"]
    website = 'https://shinnonakama.com/'
    twitter = 'shinnonakama_tv'
    hashtags = '真の仲間'
    folder_name = 'shinnonakama'

    PAGE_PREFIX = website

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ul.newsListsWrap li',
                                    date_select='p.update_time', title_select='p.update_ttl',
                                    id_select='a', a_tag_prefix=news_url, a_tag_start_text_to_remove='./')

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


# Shinka no Mi: Shiranai Uchi ni Kachigumi Jinsei
class ShinkanomiDownload(Fall2021AnimeDownload, NewsTemplate):
    title = 'Shinka no Mi: Shiranai Uchi ni Kachigumi Jinsei'
    keywords = [title, 'Shinkanomi']
    website = 'https://www.shinkanomi-anime.com'
    twitter = 'shinkanomianime'
    hashtags = ['進化の実', '勝ち組人生', 'ゴリラ系女子']
    folder_name = 'shinkanomi'

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
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)


# Shuumatsu no Harem
class ShuumatsuNoHaremDownload(Fall2021AnimeDownload, NewsTemplate2):
    title = 'Shuumatsu no Harem'
    keywords = [title, "World's End Harem"]
    website = 'https://end-harem-anime.com/'
    twitter = 'harem_official_'
    hashtags = '終末のハーレム'
    folder_name = 'shuumatsu-no-harem'

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
        self.download_template_news(self.PAGE_PREFIX, 'news/list00010000.html')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('announce', 'https://pbs.twimg.com/media/EXzkif6VAAAxqJI?format=png&name=900x900')
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'core_sys/images/news/00000002/block/00000005/00000001.jpg')
        # self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/EoYL6tMVgAADou1?format=jpg&name=large')
        # self.add_to_image_list('teaser_char', self.PAGE_PREFIX + 'core_sys/images/main/top/kv_char.png')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/E9Ma_mBVUAQoM9t?format=jpg&name=4096x4096')
        self.add_to_image_list('kv1_char', self.PAGE_PREFIX + 'core_sys/images/main/top/kv_char.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed = []
        num_processed = 0
        if os.path.exists(cache_filepath):
            with open(cache_filepath, 'r', encoding='utf-8') as f:
                inputs = f.read()
            processed = inputs.split(';')
            num_processed = len(processed)

        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/reito.html')
            chara_list = soup.find('div', id='ContentsListUnit01')
            if chara_list:
                a_tags = chara_list.find_all('a')
                for a_tag in a_tags:
                    if a_tag.has_attr('href') and '/' in a_tag['href']:
                        chara_name = a_tag['href'].split('/')[-1].split('.html')[0]
                        if chara_name in processed:
                            continue
                        if chara_name == 'reito':  # First character
                            chara_soup = soup
                        else:
                            chara_soup = self.get_soup(self.PAGE_PREFIX + a_tag['href'].replace('../', ''))
                        self.image_list = []
                        divs = ['standWrap', 'faceWrap']
                        for div in divs:
                            wraps = chara_soup.find_all('div', class_=div)
                            for wrap in wraps:
                                if wrap:
                                    image = wrap.find('img')
                                    if image and image.has_attr('src'):
                                        image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                                        self.add_to_image_list(image_name, image_url)
                        self.download_image_list(folder)
                        processed.append(chara_name)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)

        if len(processed) > num_processed:
            with open(cache_filepath, 'w+', encoding='utf-8') as f:
                for i in range(len(processed)):
                    if i > 0:
                        f.write(';')
                    f.write(processed[i])

    def download_media(self):
        folder = self.create_media_directory()
        self.image_list = []
        self.add_to_image_list('music_op', 'https://pbs.twimg.com/media/E9yvFCOUUAc43_i?format=jpg&name=large')
        self.add_to_image_list('music_ed', 'https://pbs.twimg.com/media/FAMztXhVUAADMY7?format=jpg&name=large')
        self.download_image_list(folder)

        # Blu-ray Bonus
        try:
            soup = self.get_soup(f'{self.PAGE_PREFIX}bd/tokuten.html')
            images = soup.select('div.earlyBooking img, div.shopDet img')
            self.image_list = []
            for image in images:
                if image.has_attr('src') and not image['src'].endswith('nowpri.jpg'):
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Blu-ray Bonus")
            print(e)

        # Blu-ray
        url_template = self.PAGE_PREFIX + 'core_sys/images/contents/%s/block/%s/%s.jpg'
        first = 33
        second = 106
        third = 85
        try:
            for i in range(4):
                image_name = str(third + i).zfill(8)
                if self.is_image_exists(image_name, folder):
                    continue
                num1 = str(first + i).zfill(8)
                num2 = str(second + i * 5).zfill(8)
                image_url = url_template % (num1, num2, image_name)
                if self.is_matching_content_length(image_url, 5630):
                    break
                result = self.download_image_list(folder + '/' + image_name, image_url)
                if result == -1:
                    break
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Blu-ray")
            print(e)


# Taishou Otome Otogibanashi
class TaishoOtomeDownload(Fall2021AnimeDownload, NewsTemplate):
    title = 'Taishou Otome Otogibanashi'
    keywords = [title, 'Taisho Otome']
    website = 'http://taisho-otome.com/'
    twitter = 'otome_otogi'
    hashtags = ['大正オトメ', '昭和オトメ']
    folder_name = 'taisho-otome'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ul.newslist li',
                                    date_select='div.newslist_date', title_select='h2.newslist_ttl', id_select='a',
                                    date_func=lambda x: x.replace('年', '.').replace('月', '.').replace('日', ''),
                                    next_page_select='li.pagination_list_item__next')

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
            print(f"Error in running {self.__class__.__name__}")
            print(e)

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
            print(f"Error in running {self.__class__.__name__} - Character")
            print(e)


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
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story')
            nav_btns = soup.select('a.story-nav-btn')
            for btn in nav_btns:
                if btn.has_attr('href'):
                    try:
                        episode = str(int(btn['href'].split('/')[-1])).zfill(2)
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
            print("Error in running " + self.__class__.__name__)
            print(e)

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
            print("Error in running " + self.__class__.__name__ + ' - Key Visual')
            print(e)

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
                                    image_url = image['src']
                                    image_name = self.extract_image_name_from_url(image_url)
                                    self.add_to_image_list(image_name, image_url)
                            if len(self.image_list) > 0:
                                processed.append(page_id)
                            self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Music')
            print(e)
        self.create_cache_file(cache_filepath, processed, num_processed)


# Yuuki Yuuna wa Yuusha de Aru: Dai Mankai no Shou
class Yuyuyu3Download(Fall2021AnimeDownload, NewsTemplate):
    title = "Yuuki Yuuna wa Yuusha de Aru: Dai Mankai no Shou"
    keywords = [title, "Yuyuyu", "Yuki Yuna is a Hero"]
    website = 'https://yuyuyu.tv/daimankai/'
    twitter = 'anime_yukiyuna'
    hashtags = 'yuyuyu'
    folder_name = 'yuyuyu3'

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
        prefix = 'https://yuyuyu.tv'
        self.download_template_news(page_prefix=prefix, article_select='article.c-entry-item',
                                    date_select='span.c-entry-date', title_select='h1.c-entry-item__title',
                                    id_select='a', stop_date='2021.01.29', a_tag_prefix=prefix,
                                    next_page_select='a.next.page-numbers')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tw_visual1', 'https://pbs.twimg.com/media/EeUu6NHVAAAqYgu?format=jpg&name=large')
        self.add_to_image_list('tw_visual2', 'https://pbs.twimg.com/media/E0L1PAhVEAICS7o?format=jpg&name=4096x4096')
        self.download_image_list(folder)
        self.download_by_template(folder, 'https://yuyuyu.tv/season2/img/home/visual_%s.jpg', 2, 10)
        self.download_by_template(folder, self.PAGE_PREFIX + 'img/home/visual_%s.jpg', 2, 1)

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
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)
        self.download_image_list(folder)
