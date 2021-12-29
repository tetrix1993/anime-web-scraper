import os
import anime.constants as constants
from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate3
from datetime import datetime
from scan import AniverseMagazineScanner, MocaNewsScanner, WebNewtypeScanner


# Akebi-chan no Sailor-fuku https://akebi-chan.jp/ #明日ちゃんのセーラー服 #明日ちゃん @AKEBI_chan
# Arifureta Shokugyou de Sekai Saikyou 2nd Season https://arifureta.com/ #ありふれた #ARIFURETA @ARIFURETA_info
# Fantasy Bishoujo Juniku Ojisan to https://fabiniku.com/ #ファ美肉おじさん @fabiniku
# Hakozume: Kouban Joshi no Gyakushuu https://hakozume-anime.com/ #ハコヅメ @hakozume_anime
# Kaijin Kaihatsubu no Kuroitsu-san https://kuroitsusan-anime.com/ #黒井津さん @kuroitsusan
# Karakai Jouzu no Takagi-san 3 https://takagi3.me/ #高木さんめ @takagi3_anime
# Kenja no Deshi wo Nanoru Kenja https://kendeshi-anime.com/ #賢でし @kendeshi_anime
# Leadale no Daichi nite https://leadale.net/ #leadale #リアデイル @leadale_anime
# Mahouka Koukou no Rettousei: Tsuioku-hen https://mahouka.jp/ #mahouka @mahouka_anime
# Princess Connect! Re:Dive S2 https://anime.priconne-redive.jp/ #アニメプリコネ #プリコネR #プリコネ #アニメプリコネR @priconne_anime
# Sabikui Bisco https://sabikuibisco.jp/ https://sabikuibisco.jp/ #錆喰いビスコ @SABIKUI_BISCO
# Shikkakumon no Saikyou Kenja https://shikkakumon.com/ #失格紋 @shikkakumon_PR
# Shuumatsu no Harem https://end-harem-anime.com/ #終末のハーレム @harem_official_
# Slow Loop https://slowlooptv.com/ #slowloop @slowloop_tv
# Sono Bisque Doll wa Koi wo Suru https://bisquedoll-anime.com/ #着せ恋 @kisekoi_anime
# Tensai Ouji no Akaji Kokka Saisei Jutsu: Souda, Baikoku shiyou https://tensaiouji-anime.com/ #天才王子 #天才王子の赤字国家再生術 @tensaiouji_PR


# Winter 2022 Anime
class Winter2022AnimeDownload(MainDownload):
    season = "2022-1"
    season_name = "Winter 2022"
    folder_name = '2022-1'

    def __init__(self):
        super().__init__()


# Akebi-chan no Sailor-fuku
class AkebichanDownload(Winter2022AnimeDownload, NewsTemplate):
    title = 'Akebi-chan no Sailor-fuku'
    keywords = [title, "Akebi's Sailor Uniform"]
    website = 'https://akebi-chan.jp/'
    twitter = 'AKEBI_chan'
    hashtags = ['明日ちゃんのセーラー服', '明日ちゃん']
    folder_name = 'akebichan'

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
        prefix = self.PAGE_PREFIX + '?scroll='
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.p-news-in__item',
                                    date_select='p.date', title_select='h3.title', id_select=None,
                                    id_has_id=True, a_tag_prefix=prefix)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.add_to_image_list('tz_img_kv', f'{self.PAGE_PREFIX}assets_teaser/img/img_kv.jpg')
        # self.add_to_image_list('tz_main', f'{self.PAGE_PREFIX}assets_teaser/img/main.jpg')
        self.add_to_image_list('tz_main_tw', 'https://pbs.twimg.com/media/FAmRYw-UcAkGiCO?format=jpg&name=large')
        self.add_to_image_list('kv_02_2', self.PAGE_PREFIX + 'news/SYS/CONTENTS/d9a2e879-d013-4ce6-9600-c04a78dc0135')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'assets/img/top/kv_%s.jpg'
        self.download_by_template(folder, template, 2, 1)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            chara_list = soup.select('li.p-chara__list-item a')
            self.image_list = []
            template1 = self.PAGE_PREFIX + 'assets/img/character/chara_%s.png'
            template2 = self.PAGE_PREFIX + 'assets/img/character/face_%s-01.png'
            template3 = self.PAGE_PREFIX + 'assets/img/character/face_%s-02.png'
            for chara in chara_list:
                if chara.has_attr('href') and '?chara=' in chara['href']:
                    chara_name = chara['href'].split('?chara=')[1]
                    if len(chara_name) > 1:
                        self.add_to_image_list(f'chara_{chara_name}', template1 % chara_name)
                        self.add_to_image_list(f'face_{chara_name}-01', template2 % chara_name)
                        self.add_to_image_list(f'face_{chara_name}-02', template3 % chara_name)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Arifureta Shokugyou de Sekai Saikyou 2nd Season
class Arifureta2Download(Winter2022AnimeDownload, NewsTemplate):
    title = "Arifureta Shokugyou de Sekai Saikyou 2nd Season"
    keywords = [title, "Arifureta: From Commonplace to World's Strongest 2nd Season"]
    website = 'https://arifureta.com/'
    twitter = 'ARIFURETA_info'
    hashtags = ['ARIFURETA', 'ありふれた']
    folder_name = 'arifureta2'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, diff=67)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ul.news_list li',
                                    date_select='h5', title_select='h1 a', id_select='a', stop_date='2021.03',
                                    next_page_select='ul.page-numbers li a',
                                    next_page_eval_index_class='current', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('mainvisual08', self.PAGE_PREFIX + 'wp-content/themes/arifureta-v3.2/library/img/main_visual/mainvisual08.png')
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'wp-content/uploads/2021/04/02.jpg')
        self.add_to_image_list('kv1_art', self.PAGE_PREFIX + 'wp-content/uploads/2021/04/03.jpg')
        self.add_to_image_list('mainvisual09', self.PAGE_PREFIX + 'wp-content/themes/arifureta-v3.3/library/img/main_visual/mainvisual09.jpg')
        self.add_to_image_list('kv2', self.PAGE_PREFIX + 'wp-content/uploads/2021/11/ARIFURE_Keyart-FIN.jpg')
        self.add_to_image_list('kv2_tw', 'https://pbs.twimg.com/media/FFA8J-haQAI5NvZ?format=jpg&name=4096x4096')
        self.download_image_list(folder)


# Fantasy Bishoujo Juniku Ojisan to
class FabinikuDownload(Winter2022AnimeDownload, NewsTemplate):
    title = 'Fantasy Bishoujo Juniku Ojisan to'
    keywords = [title, 'fabiniku']
    website = 'https://fabiniku.com/'
    twitter = 'fabiniku'
    hashtags = 'ファ美肉おじさん'
    folder_name = 'fabiniku'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ul.news_lists li',
                                    date_select='p.news_info_date', title_select='h3.news_title', id_select='a',
                                    date_func=lambda x: x.replace('年', '.').replace('月', '.').replace('日', ''),
                                    next_page_select='li.pager_lists_item',
                                    next_page_eval_index_class='current', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'wordpress/wp-content/uploads/2021/10/18201715/【PR】1018_fabiniku_ファ美肉おじさん完成ティザー-scaled-1.jpeg')
        self.add_to_image_list('kv1', 'https://pbs.twimg.com/media/FGeBtTLUUAAPcMG?format=jpg&name=4096x4096')
        # self.add_to_image_list('kv1', self.PAGE_PREFIX + 'wordpress/wp-content/uploads/2021/12/13162750/fabiniku_KV_1210.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wordpress/wp-content/themes/fabiniku/assets/img/character/img%s.png'
        self.download_by_template(folder, template, 1, 1)


# Hakozume: Kouban Joshi no Gyakushuu
class HakozumeDownload(Winter2022AnimeDownload, NewsTemplate3):
    title = 'Hakozume: Kouban Joshi no Gyakushuu'
    keywords = [title, 'Police in a Pod']
    website = 'https://hakozume-anime.com/'
    twitter = 'hakozume_anime'
    hashtags = 'ハコヅメ'
    folder_name = 'hakozume'

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
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/E7tsWw7VUAIhRav?format=jpg&name=medium')
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'assets/top/t1/vis.jpg')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/FEi5uNYaUAIOmIY?format=jpg&name=medium')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'assets/top/k%s/vis.jpg'
        for i in range(1, 11, 1):
            image_name = f'kv{i}'
            if self.is_image_exists(image_name, folder):
                continue
            image_url = template % str(i)
            result = self.download_image(image_url, f'{folder}/{image_name}')
            if result == -1:
                break

        template2 = self.PAGE_PREFIX + 'assets/news/vis-k%s.jpg'
        self.download_by_template(folder, template2, 1, 1)

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'assets/character/'
        templates = [prefix + 'c/%s.png', prefix + 'f/%s.png']
        self.download_by_template(folder, templates, 1, 1, prefix=['c_', 'f_'])


# Kaijin Kaihatsubu no Kuroitsu-san
class KuroitsusanDownload(Winter2022AnimeDownload, NewsTemplate):
    title = 'Kaijin Kaihatsubu no Kuroitsu-san'
    keywords = [title]
    website = 'https://kuroitsusan-anime.com/'
    twitter = 'kuroitsusan'
    hashtags = '黒井津さん'
    folder_name = 'kuroitsusan'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.list-item',
                                    date_select='.item-date', title_select='.text-row', id_select='a',
                                    date_separator='_')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FA_AHLfVEAMNrqD?format=jpg&name=4096x4096')
        self.add_to_image_list('top_pc_img_01', self.PAGE_PREFIX + 'img/top/top_pc_img_01.png')
        self.add_to_image_list('top_pc_img_02', self.PAGE_PREFIX + 'img/top/top_pc_img_02.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'img/character/detail/pc/pc_img_%s.png'
        self.download_by_template(folder, template, 2, 1)


# Karakai Jouzu no Takagi-san 3
class Takagisan3Download(Winter2022AnimeDownload, NewsTemplate):
    title = 'Karakai Jouzu no Takagi-san 3'
    keywords = [title, 'Takagisan', 'Teasing Master Takagi-san']
    website = 'https://takagi3.me/'
    twitter = 'takagi3_anime'
    hashtags = '高木さんめ'
    folder_name = 'takagisan3'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.newsList', date_select='time',
                                    title_select='span.newsList__name', id_select='a', a_tag_prefix=news_url,
                                    a_tag_start_text_to_remove='./')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/E-MCnEaUYAc-D9X?format=jpg&name=900x900')
        self.add_to_image_list('top_story__pcvs', self.PAGE_PREFIX + 'assets/img/top/top_story__pcvs.jpg')
        self.add_to_image_list('mainvisual_tw', 'https://pbs.twimg.com/media/FGJ5bxYVgAAs0k8?format=jpg&name=large')
        self.download_image_list(folder)

        prefix = self.PAGE_PREFIX + 'assets/img/top/'
        templates = [prefix + 'fv_mv%s.jpg', prefix + 'footer_mv%s.jpg']
        self.download_by_template(folder, templates, 1, 1)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            a_tags = soup.select('li.charaList a')
            self.image_list = []
            template = self.PAGE_PREFIX + 'assets/img/top/character/character-main%s.jpg'
            for a_tag in a_tags:
                if a_tag.has_attr('href') and a_tag['href'].startswith("javascript:chara('") and \
                        a_tag['href'].endswith("');"):
                    href = a_tag['href']
                    image_url = template % href[18:len(href) - 3]
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Kenja no Deshi wo Nanoru Kenja
class KendeshiDownload(Winter2022AnimeDownload, NewsTemplate):
    title = 'Kenja no Deshi wo Nanoru Kenja'
    keywords = [title, 'Kendeshi', 'She Professed Herself Pupil of the Wise Man']
    website = 'https://kendeshi-anime.com/'
    twitter = 'kendeshi_anime'
    hashtags = '賢でし'
    folder_name = 'kendeshi'

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
        story_url = self.PAGE_PREFIX + 'story/'
        try:
            soup = self.get_soup(story_url)
            a_tags = soup.select('ul.blurayList li a')
            for a_tag in a_tags:
                if a_tag.has_attr('href') and a_tag['href'].endswith('.html') and a_tag['href'].startswith('./'):
                    i_tag = a_tag.find('i')
                    if i_tag is not None:
                        try:
                            episode = str(int(i_tag.text.strip().replace('第', '').replace('話', ''))).zfill(2)
                        except:
                            continue
                        if self.is_image_exists(f'{episode}_1'):
                            continue
                        ep_soup = self.get_soup(story_url + a_tag['href'][2:])
                        if ep_soup is not None:
                            images = ep_soup.select('ul.sliderlay img')
                            self.image_list = []
                            for i in range(len(images)):
                                if images[i].has_attr('src'):
                                    image_url = story_url + images[i]['src']
                                    image_name = f'{episode}_{i + 1}'
                                    self.add_to_image_list(image_name, image_url)
                            self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='#news li', date_select=None,
                                    title_select='span', id_select='a', a_tag_prefix=news_url,
                                    date_func=lambda x: x[0:10])

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv1', 'https://pbs.twimg.com/media/ExX8OtZVcAs2aEk?format=jpg&name=4096x4096')
        self.add_to_image_list('main_pc', self.PAGE_PREFIX + '_img/main_pc.jpg')
        self.add_to_image_list('kv2_tw', 'https://pbs.twimg.com/media/E5Cte8ZVIAY8TJg?format=jpg&name=4096x4096')
        self.add_to_image_list('kv4_tw', 'https://pbs.twimg.com/media/FFrgHL8agAEv0Lj?format=jpg&name=4096x4096')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'news/_image/keyvisual%s.png'
        self.download_by_template(folder, template, 2, 2)

    def download_character(self):
        folder = self.create_character_directory()
        # template = self.PAGE_PREFIX + '_img/cha%s.png'
        # self.download_by_template(folder, template)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('div.pop.mfp-hide img')
            self.image_list = []
            for image in images:
                if image.has_attr('srcset'):
                    image_url = self.PAGE_PREFIX + image['srcset']
                    if image_url.endswith(' 2x'):
                        image_url = image_url[0:-3]
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        self.image_list = []
        self.add_to_image_list('music_op', 'https://pbs.twimg.com/media/FGzLrAkagAUwPew?format=jpg&name=4096x4096')
        self.add_to_image_list('music_ed', self.PAGE_PREFIX + '_image/music_cd05.jpg')
        self.download_image_list(folder)

        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)

        pages = ['bluray_shop', 'bluray_camp', 'bluray', 'bluray01', 'bluray02', 'bluray03']
        for i in range(len(pages)):
            if i > 2 and pages[i] in processed:
                continue
            page_url = f'{self.PAGE_PREFIX}{pages[i]}.html'
            try:
                soup = self.get_soup(page_url)
                images = soup.select('#bluray img')
                self.image_list = []
                for image in images:
                    if image.has_attr('src') and 'nowprinting' not in image['src']:
                        image_url = self.PAGE_PREFIX + image['src']
                        image_name = self.extract_image_name_from_url(image_url)
                        self.add_to_image_list(image_name, image_url)
                if i > 2 and len(self.image_list) > 0:
                    processed.append(pages[i])
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray: {page_url}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Leadale no Daichi nite
class LeadaleDownload(Winter2022AnimeDownload, NewsTemplate3):
    title = 'Leadale no Daichi nite'
    keywords = [title, 'World of Leadale']
    website = 'https://leadale.net/'
    twitter = 'leadale_anime'
    hashtags = ['leadale', 'リアデイル']
    folder_name = 'leadale'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_character()
        self.download_key_visual()
        self.download_media()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'assets/story/%s_%s.jpg'
        try:
            for i in range(12):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_1'):
                    continue
                for j in range(8):
                    image_url = template % (str(i + 1), str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    result = self.download_image(image_url, self.base_folder + '/' + image_name)
                    if result == -1:
                        return
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/character/c/%s.png'
        self.download_by_template(folder, template, 1, 1, prefix='c', save_zfill=2)

        template2 = self.PAGE_PREFIX + 'assets/character/%sc.png'
        self.download_by_template(folder, template2, 1, 1, prefix='chara_', save_zfill=2)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'assets/top/main-t1/vis.jpg')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/Ezi8NqIVkAMv0Yv?format=jpg&name=medium')
        self.add_to_image_list('kv2_tw', 'https://pbs.twimg.com/media/E8Ouua3UUAIFSvH?format=jpg&name=medium')
        self.add_to_image_list('kv3_tw', 'https://pbs.twimg.com/media/FEmTgkJUcAUk9kQ?format=jpg&name=4096x4096')
        self.add_to_image_list('kv4_tw', 'https://pbs.twimg.com/media/FG9Syr-agAAH7-D?format=jpg&name=4096x4096')
        self.add_to_image_list('kv4_aniverse', 'https://aniverse-mag.com/wp-content/uploads/2021/12/288f98f39ec491c839eca0d9f9d273d8-e1639894389795.jpg')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'assets/news/kv-t%s.jpg'
        template2 = self.PAGE_PREFIX + 'assets/special/vis/%s.jpg'
        self.download_by_template(folder, template, 1, 1)
        self.download_by_template(folder, template2, 1, 1, prefix='kv_s')

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bddvd.html')
            images = soup.select('#BdData img:not(h3 img)')
            self.image_list = []
            for image in images:
                if image.has_attr('src') and not image['src'].endswith('np.png') and image['src'].startswith('./'):
                    image_url = self.PAGE_PREFIX + image['src'][2:].split('?')[0]
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Mahouka Koukou no Rettousei: Tsuioku-hen
class Mahouka3Download(Winter2022AnimeDownload, NewsTemplate):
    title = "Mahouka Koukou no Rettousei: Tsuioku-hen"
    keywords = [title, "The Irregular at Magic High School: Reminiscence Arc", "3rd"]
    website = 'https://mahouka.jp/'
    twitter = 'mahouka_anime'
    hashtags = 'mahouka'
    folder_name = 'mahouka3'

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
        # Next page logic may need updates
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, paging_type=1, article_select='li.c-list__item',
                                    date_select='div.c-list__item-date', title_select='div.c-list__item-title',
                                    id_select='a', a_tag_prefix=news_url, a_tag_replace_from='./',
                                    date_func=lambda x: x[0:4] + '.' + x[5:].replace('/', '.'),
                                    next_page_select='div.c-pagination__arrow.-next',
                                    next_page_eval_index_class='is-disable')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'assets/img/top/img_main.jpg')
        # self.add_to_image_list('kv1', self.PAGE_PREFIX + 'news/SYS/CONTENTS/5618109f-c116-4a2a-96d1-43644cce1fa3/w850')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            images = soup.select('div.p-in-main img')
            self.image_list = []
            for image in images:
                if image.has_attr('src'):
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Princess Connect! Re:Dive Season 2
class Priconne2Download(Winter2022AnimeDownload, NewsTemplate):
    title = "Princess Connect! Re:Dive Season 2"
    keywords = [title, "Priconne"]
    website = "https://anime.priconne-redive.jp/"
    twitter = 'priconne_anime'
    hashtags = ['プリコネ', 'プリコネR', 'アニメプリコネ', 'アニメプリコネR']
    folder_name = 'priconne2'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        # Handles only the first story page, need update logic in the future
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            article = soup.select('article.mainContents__inner')
            if len(article) == 0:
                return
            span = article[0].select('div.storyNumber span')
            try:
                episode = str(int(span[0].text)).zfill(2)
            except:
                return
            if not os.path.exists(episode + '_01'):
                images = article[0].select('div.mainSlider li.swiper-slide img')
                self.image_list = []
                i = 0
                for image in images:
                    if image.has_attr('src'):
                        i += 1
                        image_url = self.PAGE_PREFIX + (image['src'][1:] if image['src'].startswith('/') else image['src'])
                        image_name = episode + '_' + str(i).zfill(2)
                        self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ul.newsList li',
                                    date_select='time', title_select='div.desc', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'assets/images/top_kv.png')
        self.add_to_image_list('kv_bg_pc', self.PAGE_PREFIX + 'assets/images/top/kv_bg_pc.png')
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'app/wp-content/uploads/2021/08/b34c29383da0e37a1104e94492001b1a.png')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'assets/images/top/kv_chara%s_pc.png'
        self.download_by_template(folder, template, 2, 1, 4)


# Sabikui Bisco
class SabikuiBiscoDownload(Winter2022AnimeDownload, NewsTemplate):
    title = 'Sabikui Bisco'
    keywords = [title]
    website = 'https://sabikuibisco.jp/'
    twitter = 'SABIKUI_BISCO'
    hashtags = '錆喰いビスコ'
    folder_name = 'sabikuibisco'

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
            a_tags = soup.select('#l-nav li a')
            for a_tag in a_tags:
                if a_tag.has_attr('href'):
                    try:
                        episode = str(int(a_tag.text)).zfill(2)
                    except:
                        continue
                    if self.is_image_exists(episode + '_5'):
                        continue
                    ep_soup = self.get_soup(a_tag['href'])
                    if ep_soup is not None:
                        images = ep_soup.select('.gallery-slider img')
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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='#news li',
                                    date_select='dt', title_select='dd', id_select='a',
                                    date_func=lambda x: x[0:4] + '.' + x[4:])

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('key-vs', self.PAGE_PREFIX + 'wp/wp-content/themes/sabikuibisco/images/top/key-vs.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            chara_list = soup.select('#character li a')
            for chara in chara_list:
                if chara.has_attr('href'):
                    href = chara['href']
                    if href.endswith('/'):
                        href = href[0:len(href)-1]
                    chara_name = href.split('/')[-1]
                    if len(chara_name) > 1 and chara_name not in processed:
                        chara_soup = self.get_soup(href)
                        if chara_soup is not None:
                            images = chara_soup.select('.characterMainContents img')
                            self.image_list = []
                            for image in images:
                                if image.has_attr('src'):
                                    if image['src'].startswith('/'):
                                        image_url = self.PAGE_PREFIX + image['src'][1:]
                                    else:
                                        image_url = self.PAGE_PREFIX + image['src']
                                    image_name = self.extract_image_name_from_url(image_url)
                                    self.add_to_image_list(image_name, image_url)
                            if len(self.image_list) > 0:
                                processed.append(chara_name)
                            self.download_image_list(folder)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Shikkakumon no Saikyou Kenja
class ShikkakumonDownload(Winter2022AnimeDownload, NewsTemplate2):
    title = 'Shikkakumon no Saikyou Kenja'
    keywords = [title, 'The Strongest Sage of Disqualified Crest']
    website = 'https://shikkakumon.com/'
    twitter = 'shikkakumon_PR'
    hashtags = '失格紋'
    folder_name = 'shikkakumon'

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
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.png')
        self.add_to_image_list('teaser_tw', 'https://pbs.twimg.com/media/EtDguMkU0AQjk4b?format=jpg&name=4096x4096')
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'core_sys/images/main/top/kv.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'core_sys/images/main/tz/char'
        templates = [prefix + '%s_stand.png', prefix + '%s_face.png']
        self.download_by_template(folder, templates, 2, 1, prefix='tz_')

        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'chara/')
            chara_links = soup.select('div.list_type06 a')
            for link in chara_links:
                if link.has_attr('href') and link['href'].endswith('.html'):
                    chara_name = link['href'].split('/')[-1].split('.html')[0]
                    if chara_name in processed:
                        continue
                    if chara_name == 'index':
                        chara_soup = soup
                    else:
                        chara_soup = self.get_soup(self.PAGE_PREFIX + link['href'].replace('../', ''))
                    if chara_soup is not None:
                        images = chara_soup.select('div.charaImg img')
                        self.image_list = []
                        for image in images:
                            if image.has_attr('src'):
                                image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                                image_name = 'chara_' + self.extract_image_name_from_url(image_url)
                                self.add_to_image_list(image_name, image_url)
                        if len(self.image_list) > 0:
                            processed.append(chara_name)
                        self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Shuumatsu no Harem
class ShuumatsuNoHaremDownload(Winter2022AnimeDownload, NewsTemplate2):
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
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/', decode=True)
            a_tags = soup.select('table a')
            for a_tag in a_tags:
                if a_tag.has_attr('href'):
                    try:
                        episode = str(int(a_tag.text.strip().replace('第', '').replace('話', ''))).zfill(2)
                    except Exception as e:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    url = self.PAGE_PREFIX + a_tag['href'].replace('../', '')
                    ep_soup = self.get_soup(url)
                    if ep_soup:
                        images = ep_soup.select('ul.tp5 img')
                        self.image_list = []
                        for i in range(len(images)):
                            image_url = self.PAGE_PREFIX + images[i]['src'].split('?')[0].replace('../', '')
                            image_name = episode + '_' + str(i + 1)
                            self.add_to_image_list(image_name, image_url)
                        self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

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
            self.print_exception(e, 'Character')

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
            self.print_exception(e, 'Blu-ray Bonus')

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
            self.print_exception(e, 'Blu-ray')


# Slow Loop
class SlowLoopDownload(Winter2022AnimeDownload, NewsTemplate):
    title = 'Slow Loop'
    keywords = [title]
    website = 'https://slowlooptv.com/'
    twitter = 'slowloop_tv'
    hashtags = 'slowloop'
    folder_name = 'slow-loop'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, news_prefix='news.html', article_select='article',
                                    date_select='div.news_list_day', title_select='div.news_list_title',
                                    id_select='a', a_tag_prefix=self.PAGE_PREFIX, date_separator='/')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('announce', 'https://pbs.twimg.com/media/Ep5-SoLUUAAHq36?format=jpg&name=4096x4096')
        self.add_to_image_list('announce_2', self.PAGE_PREFIX + 'images/top/v_001.jpg')
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'images/top/v_002_02.jpg')
        self.add_to_image_list('teaser_tw', 'https://pbs.twimg.com/media/E15YSghVgAIdgJf?format=jpg&name=medium')
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'images/top/v_003.jpg')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/E9eeba0VIAYQ3-l?format=jpg&name=medium')
        self.add_to_image_list('kv2_tw', 'https://pbs.twimg.com/media/FEyFu9eaIAE9mfc?format=jpg&name=large')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'images/top/v_%s.jpg'
        self.download_by_template(folder, template, 3, 4)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'images/chara/p_%s.png'
        self.download_by_template(folder, template, 3, 1)

        template2 = self.PAGE_PREFIX + 'images/news/p_%s.jpg'
        self.download_by_template(folder, template2, 3, 8, 10, prefix='news_')


# Sono Bisque Doll wa Koi wo Suru
class KisekoiDownload(Winter2022AnimeDownload, NewsTemplate):
    title = 'Sono Bisque Doll wa Koi wo Suru'
    keywords = [title, 'kisekoi', 'My Dress-Up Darling']
    website = 'https://bisquedoll-anime.com/'
    twitter = 'kisekoi'
    hashtags = '着せ恋'
    folder_name = 'kisekoi'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.p-news__list-item',
                                    date_select='div.p-in-date', title_select='div.p-in-title',
                                    id_select='a', a_tag_start_text_to_remove='./',
                                    a_tag_prefix=self.PAGE_PREFIX + 'news/', date_func=lambda x: x[0:4] + '.' + x[4:],
                                    next_page_select='div.c-pagination__link.-next',
                                    next_page_eval_index_class='is-disable', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/FBs3mm8VUAAoYEo?format=jpg&name=4096x4096')
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'assets/teaser/img/kv_image.png')
        self.add_to_image_list('kv2', self.PAGE_PREFIX + 'assets/img/top/kv.jpg')
        # self.add_to_image_list('kv2', 'https://pbs.twimg.com/media/FFw753magAU4-YH?format=jpg&name=4096x4096')
        # self.add_to_image_list('kv2_tw', 'https://pbs.twimg.com/media/FFw21hLUcAIcKmK?format=jpg&name=large')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        # template = self.PAGE_PREFIX + 'assets/teaser/img/chara_%s.png'
        # self.download_by_template(folder, template, 1, 1, prefix='tz_')

        template = self.PAGE_PREFIX + 'assets/img/character/chara_%s.png'
        self.download_by_template(folder, template, 1, 1)

    def download_media(self):
        folder = self.create_media_directory()

        # Special Pages
        special_filepath = folder + '/special'
        processed, num_processed = self.get_processed_items_from_cache_file(special_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'special/', decode=True)
            items = soup.select('li.p-special__list-item')
            for item in items:
                title = item.select('div.p-in-title')
                if len(title) == 0:
                    continue
                if '壁紙' in title[0].text:
                    a_tag = item.find('a')
                    if a_tag is not None and a_tag.has_attr('href'):
                        href = a_tag['href']
                        if len(href) > 2 and href.startswith('/') and href.endswith('/'):
                            page_name = href[1:-1]
                            if page_name in processed:
                                continue
                            page_url = self.PAGE_PREFIX + page_name
                            page_soup = self.get_soup(page_url)
                            if page_soup is not None:
                                images = page_soup.select('figure img')
                                self.image_list = []
                                for image in images:
                                    if image.has_attr('src'):
                                        image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                                        image_name = f'{page_name}_' + self.extract_image_name_from_url(image_url)
                                        self.add_to_image_list(image_name, image_url)
                                if len(self.image_list) > 0:
                                    processed.append(page_name)
                                self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Media')
        self.create_cache_file(special_filepath, processed, num_processed)


# Tensai Ouji no Akaji Kokka Saisei Jutsu: Souda, Baikoku shiyou
class TensaiOujiDownload(Winter2022AnimeDownload, NewsTemplate2):
    title = 'Tensai Ouji no Akaji Kokka Saisei Jutsu: Souda, Baikoku shiyou'
    keywords = [title, 'tensaiouji']
    website = 'https://tensaiouji-anime.com/'
    twitter = 'tensaiouji_PR'
    hashtags = ['天才王子', '天才王子の赤字国家再生術']
    folder_name = 'tensaiouji'

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
        self.add_to_image_list('kv', self.PAGE_PREFIX + 'core_sys/images/main/home/kv.jpg')
        self.add_to_image_list('kv1_5', self.PAGE_PREFIX + 'core_sys/images/main/home/kv_1_5.jpg')
        self.add_to_image_list('kv1_5_tw', 'https://pbs.twimg.com/media/E_PAfkYVgAc6n2Q?format=jpg&name=large')
        self.add_to_image_list('kv2_tw', 'https://pbs.twimg.com/media/FEfLUMjVIAg-mP5?format=jpg&name=4096x4096')
        self.download_image_list(folder)

        template = f'{self.PAGE_PREFIX}core_sys/images/main/home/kv%s.jpg'
        self.download_by_template(folder, template, 1, 2)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'core_sys/images/main/cont/char/c%s_%s.png'
        templates = [template % ('%s', '01'), template % ('%s', '02')]
        self.download_by_template(folder, templates, 2, 1)
