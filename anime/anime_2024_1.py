import os
from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate4
from datetime import datetime, timedelta

# Akuyaku Reijou Level 99 https://akuyakulv99-anime.com/ #akuyakuLV99 @akuyakuLV99
# Chiyu Mahou no Machigatta Tsukaikata https://chiyumahou-anime.com/ #治癒魔法 @chiyumahou_PR
# Dosanko Gal wa Namara Menkoi https://dosankogal-pr.com/ #道産子ギャル #どさこい @dosankogal_pr
# Dungeon Meshi https://delicious-in-dungeon.com/ #ダンジョン飯 #deliciousindungeon @dun_meshi_anime
# Gekai Elise https://surgeon-elise.com/ #外科医エリーゼ #surgeon_elise @surgeon_elise
# Himesama "Goumon" no Jikan desu https://himesama-goumon.com/ #姫様拷問の時間です @himesama_goumon
# Kekkon Yubiwa Monogatari https://talesofweddingrings-anime.jp/ #結婚指輪物語 @weddingringsPR
# Jaku-Chara Tomozaki-kun 2nd Stage http://tomozaki-koushiki.com/ #友崎くん @tomozakikoshiki
# Loop 7-kaime no Akuyaku Reijou wa, Moto Tekikoku de Jiyuu Kimama na Hanayome Seikatsu wo Mankitsu suru https://7th-timeloop.com/ #ルプなな @7th_timeloop
# Mahou Shoujo ni Akogarete https://mahoako-anime.com/ #まほあこ #まほあこアニメ @mahoako_anime
# Mato Seihei no Slave https://mabotai.jp/ #魔都精兵のスレイブ #まとスレ @mabotai_kohobu
# Nozomanu Fushi no Boukensha https://nozomanufushi-anime.jp/ #望まぬ不死 #TUUA @nozomanufushiPR
# Oroka na Tenshi wa Akuma to Odoru https://kanaten-anime.com/ #かな天 #kanaten @kanaten_PR
# Pon no Michi https://ponnomichi-pr.com/ #ぽんのみち @ponnomichi_pr
# Saijaku Tamer wa Gomi Hiroi no Tabi wo Hajimemashita. https://saijakutamer-anime.com/ #最弱テイマー @saijakutamer
# Saikyou Tank no Meikyuu Kouryaku https://saikyo-tank.com/ #最強タンク @saikyo_tank
# Sasaki to Pii-chan https://sasapi-anime.com/ #ささピー @sasaki_pichan
# Sokushi Cheat ga Saikyou sugite, Isekai no Yatsura ga Marude Aite ni Naranai n desu ga. https://sokushicheat-pr.com/ #即死チート @sokushicheat_pr
# Tsuki ga Michibiku Isekai Douchuu 2nd Season https://tsukimichi.com/ #ツキミチ @tsukimichi_PR
# Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e S3 http://you-zitsu.com/ #you_zitsu #よう実 @youkosozitsu
# Yubisaki to Renren https://yubisaki-pr.com/ #ゆびさきと恋々 @yubisaki_pr


# Winter 2024 Anime
class Winter2024AnimeDownload(MainDownload):
    season = "2024-1"
    season_name = "Winter 2024"
    folder_name = '2024-1'

    def __init__(self):
        super().__init__()


# Akuyaku Reijou Level 99
class AkuyakuLv99Download(Winter2024AnimeDownload, NewsTemplate2):
    title = 'Akuyaku Reijou Level 99'
    keywords = [title, 'Villainess Level 99']
    website = 'https://akuyakulv99-anime.com/'
    twitter = 'akuyakuLV99'
    hashtags = 'akuyakuLV99'
    folder_name = 'akuyakulv99'

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
            soup = self.get_soup(self.PAGE_PREFIX + 'story/01.html')
            a_tags = soup.select('#ContentsListUnit02 a[href]')
            for a_tag in a_tags:
                try:
                    episode = str(int(a_tag.text.replace('#', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if episode == '01':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(self.PAGE_PREFIX + a_tag['href'].replace('../', ''))
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('.tp5 img[src]')
                for i in range(len(images)):
                    image_url = self.PAGE_PREFIX + images[i]['src'].split('?')[0].replace('../', '').replace('sn_', '')
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fr-S3r0aQAAH2xA?format=jpg&name=medium')
        self.add_to_image_list('tzkv', self.PAGE_PREFIX + 'core_sys/images/main/home/tzkv.png')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.mainImg__kv source[type][srcset]')
            self.image_list = []
            for image in images:
                if '/main/' not in image['srcset']:
                    continue
                image_name = self.extract_image_name_from_url(image['srcset'])
                if 'kv' not in image_name:
                    continue
                image_name = self.generate_image_name_from_url(image['srcset'], 'main')
                image_url = self.PAGE_PREFIX + image['srcset'].split('?')[0].replace('./', '')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.charaStand source[type][srcset], .charaFace source[type][srcset]')
            self.image_list = []
            for image in images:
                if '/chara/' not in image['srcset']:
                    continue
                image_name = self.generate_image_name_from_url(image['srcset'], 'chara')
                image_url = self.PAGE_PREFIX + image['srcset'].split('?')[0].replace('./', '')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Chiyu Mahou no Machigatta Tsukaikata
class ChiyuMahouDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Chiyu Mahou no Machigatta Tsukaikata'
    keywords = [title, 'The Wrong Way to Use Healing Magic']
    website = 'https://chiyumahou-anime.com/'
    twitter = 'chiyumahou_PR'
    hashtags = ['治癒魔法']
    folder_name = 'chiyumahou'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index', diff=150)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsArchive-Item',
                                    date_select='.date', title_select='.title', id_select='a',
                                    next_page_select='.nextpostslink')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        # self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FwP_QYPaQAMBkyd?format=jpg&name=medium')
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'wp-content/themes/chiyumahou-anime_teaser/assets/images/pc/index/img_hero.jpg')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.visual img[src]')
            self.image_list = []
            for image in images:
                if '/pc/' not in image['src']:
                    continue
                image_url = image['src'].split('?')[0]
                image_name = self.generate_image_name_from_url(image_url, 'pc')
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
            a_tags = soup.select('.character-List li>a[href]')
            for a_tag in a_tags:
                chara_url = a_tag['href']
                if chara_url.endswith('/'):
                    chara_name = chara_url[:-1].split('/')[-1]
                else:
                    chara_name = chara_url.split('/')[-1]
                if chara_name in processed:
                    continue
                chara_soup = self.get_soup(self.PAGE_PREFIX + chara_url[1:])
                if chara_soup is not None:
                    images = chara_soup.select('.character-Detail img[src]')
                    for image in images:
                        image_url = image['src']
                        if '/character/' not in image_url:
                            continue
                        image_name = self.generate_image_name_from_url(image_url, 'character')
                        self.add_to_image_list(image_name, image_url)
                    if len(self.image_list) > 0:
                        processed.append(chara_name)
                    self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Dosanko Gal wa Namara Menkoi
class DosankoGalDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Dosanko Gal wa Namara Menkoi'
    keywords = [title, 'Hokkaido Gals Are Super Adorable!', 'dosakoi']
    website = 'https://dosankogal-pr.com/'
    twitter = 'dosankogal_pr'
    hashtags = ['道産子ギャル', 'どさこい']
    folder_name = 'dosankogal'

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
        # Paging logic not known
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.md-list__news li',
                                    date_select='.txt--date', title_select='.txt--ttl', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        # self.image_list = []
        # self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FkJnLbAVUAERF5S?format=jpg&name=4096x4096')
        # self.add_to_image_list('tz_news', self.PAGE_PREFIX + 'wp/wp-content/uploads/2022/12/dosankogal_teaser_logoc-scaled-1.jpg')
        # self.download_image_list(folder)

        soup = None
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.fvslide source[srcset]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'][1:]
                if '/images/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'images')
                if image_name.endswith('_sp'):
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')
        return soup

    def download_character(self, soup=None):
        folder = self.create_character_directory()
        try:
            if soup is None:
                soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.chardata--inner source[srcset]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'][1:]
                if '/images/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'images')
                if image_name.endswith('_sp'):
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Dungeon Meshi
class DungeonMeshiDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Dungeon Meshi'
    keywords = [title, 'Delicious in Dungeon']
    website = 'https://delicious-in-dungeon.com/'
    twitter = 'dun_meshi_anime'
    hashtags = ['ダンジョン飯', 'deliciousindungeon']
    folder_name = 'dungeon-meshi'

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
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.vis img[src]')
            self.image_list = []
            for image in images:
                if '/assets/' not in image['src']:
                    continue
                image_url = image['src']
                if image_url.startswith('./'):
                    image_url = self.PAGE_PREFIX + image_url[2:]
                image_name = self.generate_image_name_from_url(image_url, 'assets')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        templates = [
            self.PAGE_PREFIX + 'assets/character/%sc.png',
            self.PAGE_PREFIX + 'assets/character/%sf.png'
        ]
        self.download_by_template(folder, templates, 1, 1)


# Gekai Elise
class GekaiEliseDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Gekai Elise'
    keywords = [title, 'Surgeon Elise']
    website = 'https://surgeon-elise.com/'
    twitter = 'surgeon_elise'
    hashtags = ['外科医エリーゼ', 'surgeon_elise']
    folder_name = 'gekaielise'

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
            self.image_list = []
            images = soup.select('.visual_wrap img[src*="/visual/"]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src']
                if '/top/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'top')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'images/chara/'
        templates = [prefix + 'a_%s.png', prefix + 'b_%s.png']
        self.download_by_template(folder, templates, 3, 1)


# Himesama "Goumon" no Jikan desu
class HimesamaGoumonDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Himesama "Goumon" no Jikan desu'
    keywords = [title, '\'Tis Time for "Torture," Princess']
    website = 'https://himesama-goumon.com/'
    twitter = 'himesama_goumon'
    hashtags = ['姫様拷問の時間です']
    folder_name = 'himesamagoumon'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.md-li__news li',
                                    date_select='.date', title_select='.ttl', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        soup = None
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.fv--visual source[srcset]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'][1:]
                if '/webp/' not in image_url:
                    continue
                image_name = self.extract_image_name_from_url(image_url)
                if image_name.endswith('_sp'):
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')
        return soup

    def download_character(self, soup=None):
        folder = self.create_character_directory()
        try:
            if soup is None:
                soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.chardata--inner .visual source[srcset]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'][1:]
                if '/webp/' not in image_url:
                    continue
                image_name = self.extract_image_name_from_url(image_url)
                if image_name.endswith('_sp'):
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Kekkon Yubiwa Monogatari
class KekkonYubiwaDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Kekkon Yubiwa Monogatari'
    keywords = [title, 'Tales of Wedding Rings']
    website = 'https://talesofweddingrings-anime.jp/'
    twitter = 'weddingringsPR'
    hashtags = '結婚指輪物語'
    folder_name = 'kekkonyubiwa'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, news_prefix='', article_select='.newsinlist li',
                                    date_select='.newstime', title_select='a', id_select='a', id_has_id=True,
                                    id_attr='data-cl')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'images/mob02/per_bg.png')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FsCGtvQaMAEldYZ?format=jpg&name=large')
        self.download_image_list(folder)

        sub_folder = self.create_custom_directory(folder.split('/')[-1] + '/news')
        cache_filepath = sub_folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX, decode=True)
            items = soup.select('.newsinlist li a[data-cl]')
            for item in items:
                page_name = item['data-cl']
                if page_name in processed:
                    break
                title = item.text.strip()
                if 'ビジュアル' in title or 'イラスト' in title:
                    images = soup.select(f'.lbox_com.{page_name} img[src]')
                    self.image_list = []
                    for image in images:
                        image_url = self.PAGE_PREFIX + image['src'].replace('./', '').split('?')[0]
                        if '/news/' not in image_url or image_url.endswith('.svg'):
                            continue
                        image_name = self.generate_image_name_from_url(image_url, 'news')
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(sub_folder)
                processed.append(page_name)
        except Exception as e:
            self.print_exception(e, 'Key Visual News')
        self.create_cache_file(cache_filepath, processed, num_processed)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'images/mob02/chara_%s.png'
        self.download_by_template(folder, template, 2, 1)


# Isekai de Mofumofu Nadenade suru Tame ni Ganbattemasu.
class MofunadeDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Isekai de Mofumofu Nadenade suru Tame ni Ganbattemasu.'
    keywords = [title, 'Fluffy Paradise']
    website = 'https://mohunadeanime.com/'
    twitter = 'mohunade_anime'
    hashtags = 'もふなで'
    folder_name = 'mofunade'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 5

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'dist/img/story/ep%s/img%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.c-news__item',
                                    date_select='.c-news__date', title_select='.c-news__ttl',
                                    id_select='.c-news__link', a_tag_prefix=news_url, paging_type=1,
                                    a_tag_start_text_to_remove='./', next_page_select='.c-Pager__item',
                                    next_page_eval_index_class='-current', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FrwZ2u4aQAMVhBo?format=jpg&name=4096x4096')
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'dist/img/top/kv_img.webp')
        self.download_image_list(folder)


# Jaku-Chara Tomozaki-kun 2nd Stage
class TomozakiKun2Download(Winter2024AnimeDownload, NewsTemplate):
    title = "Jaku-Chara Tomozaki-kun 2nd Stage"
    keywords = [title, 'Bottom-Tier Character Tomozaki', 'Tomozaki-kun']
    website = 'http://tomozaki-koushiki.com/'
    twitter = 'tomozakikoshiki'
    hashtags = '友崎くん'
    folder_name = 'tomozakikun2'

    PAGE_PREFIX = website
    FINAL_EPISODE = 13
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'img/story/story2-%s/img%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.box_main',
                                    date_select='time', title_select='.box_title', id_select='nothing')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        template = self.PAGE_PREFIX + 'img/index/vis_img%s.jpg'
        self.download_by_template(folder, template, 1, 1)


# Loop 7-kaime no Akuyaku Reijou wa, Moto Tekikoku de Jiyuu Kimama na Hanayome Seikatsu wo Mankitsu suru
class Loop7KaimeDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Loop 7-kaime no Akuyaku Reijou wa, Moto Tekikoku de Jiyuu Kimama na Hanayome Seikatsu wo Mankitsu suru'
    keywords = [title, '7th Time Loop: The Villainess Enjoys a Carefree Life Married to Her Worst Enemy!']
    website = 'https://7th-timeloop.com/'
    twitter = '7th_timeloop'
    hashtags = ['ルプなな']
    folder_name = 'loop7kaime'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.ef',
                                    date_select='.article__listsTime', title_select='.article__listsFullTitle',
                                    id_select='a[a]')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.kv__imgList img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].split('?')[0][1:]
                if '/img/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'img')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wordpress/wp-content/themes/7th-timeloop/assets/img/character/c%s_main.png'
        self.download_by_template(folder, template, 1, 1)


# Mahou Shoujo ni Akogarete
class MahoakoDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Mahou Shoujo ni Akogarete'
    keywords = [title, 'Gushing over Magical Girls', 'mahoako']
    website = 'https://mahoako-anime.com/'
    twitter = 'mahoako_anime'
    hashtags = ['まほあこ' ,'まほあこアニメ']
    folder_name = 'mahoako'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='#Entries article',
                                    title_select='.entry-title span', date_select='.entry-date span',
                                    id_select=None, id_has_id=True, news_prefix='news.html', date_separator='-')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.vis source[srcset]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'].replace('./', '').split('?')[0]
                if not image_url.endswith('.webp') or '/top/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'top')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/character/%sc.webp'
        self.download_by_template(folder, template, 1, 1, prefix='chara_')


# Mato Seihei no Slave
class MatoSlaveDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Mato Seihei no Slave'
    keywords = [title, 'Chained Soldier', 'matoslave', 'mabotai']
    website = 'https://mabotai.jp/'
    twitter = 'mabotai_kohobu'
    hashtags = ['魔都精兵のスレイブ', 'まとスレ']
    folder_name = 'matoslave'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-list-item',
                                    date_select='.news-list-item__date', title_select='.news-list-item__title',
                                    id_select='a', a_tag_start_text_to_remove='/', a_tag_prefix=self.PAGE_PREFIX,
                                    date_func=lambda x: x.replace('年', '.').replace('月', '.').replace('日', ''))

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        # self.image_list = []
        # self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FEiqZdFaUAQyOy4?format=jpg&name=900x900')
        # self.download_image_list(folder)

        teaser_template = self.PAGE_PREFIX + 'img/home/visual_%s.webp'
        for i in range(1, 11, 1):
            image_name = f'home_visual_{i}'
            if self.is_image_exists(image_name, folder):
                continue
            image_url = teaser_template % str(i).zfill(2)
            result = self.download_image(image_url, f'{folder}/{image_name}')
            if result == -1:
                break

    def download_character(self):
        folder = self.create_character_directory()
        char_url = self.PAGE_PREFIX + 'character'
        json_url = char_url + '/chara_data.php'
        self.image_list = []
        try:
            json_obj = self.get_json(json_url)
            if 'charas' in json_obj and isinstance(json_obj['charas'], list):
                for chara in json_obj['charas']:
                    if 'images' in chara:
                        if 'visuals' in chara['images'] and isinstance(chara['images']['visuals'], list):
                            for visual in chara['images']['visuals']:
                                if 'image' in visual:
                                    image_url = char_url + visual['image'][1:].split('?')[0]
                                    image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                                    self.add_to_image_list(image_name, image_url)
                        if 'faces' in chara['images'] and isinstance(chara['images']['faces'], list):
                            for face in chara['images']['faces']:
                                image_url = char_url + face[1:].split('?')[0]
                                image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                                self.add_to_image_list(image_name, image_url)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.download_image_list(folder)


# Nozomanu Fushi no Boukensha #望まぬ不死 #TUUA @nozomanufushiPR
class NozomanuFushiDownload(Winter2024AnimeDownload, NewsTemplate2):
    title = 'Nozomanu Fushi no Boukensha'
    keywords = [title, 'The Unwanted Undead Adventurer']
    twitter = 'nozomanufushiPR'
    website = 'https://nozomanufushi-anime.jp/'
    hashtags = ['望まぬ不死', 'TUUA']
    folder_name = 'nozomanufushi'

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
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.mainImg__kv source[srcset]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'].split('?')[0]
                if '/images/' not in image_url or not image_url.endswith('.webp'):
                    continue
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
            pages = soup.select('#list_06 .title a[href]')
            for page in pages:
                if not page['href'].endswith('.html') or not page['href'].startswith('../'):
                    continue
                page_url = self.PAGE_PREFIX + page['href'].replace('../', '')
                page_name = page_url.split('/')[-1].split('.html')[0]
                if page_name in processed:
                    continue
                ep_soup = self.get_soup(page_url)
                if ep_soup is None:
                    continue
                images = ep_soup.select('.chara__stand img[src],.chara__face img[src]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                    if '/chara/' not in image_url:
                        continue
                    image_name = self.generate_image_name_from_url(image_url, 'chara')
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
                processed.append(page_name)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Oroka na Tenshi wa Akuma to Odoru
class KanatenDownload(Winter2024AnimeDownload, NewsTemplate2):
    title = 'Oroka na Tenshi wa Akuma to Odoru'
    keywords = [title, 'The Foolish Angel Dances with the Devil', 'kanaten']
    website = 'https://kanaten-anime.com/'
    twitter = 'kanaten_PR'
    hashtags = ['かな天', 'kanaten']
    folder_name = 'kanaten'

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
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.head__kv source[srcset]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'].split('?')[0]
                if '/images/' not in image_url or not image_url.endswith('.webp'):
                    continue
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
            soup = self.get_soup(self.PAGE_PREFIX + 'chara/')
            pages = soup.select('#ContentsListUnit01 a[href]')
            for page in pages:
                if not page['href'].endswith('.html') or not page['href'].startswith('../'):
                    continue
                page_url = self.PAGE_PREFIX + page['href'].replace('../', '')
                page_name = page_url.split('/')[-1].split('.html')[0]
                if page_name in processed:
                    continue
                if page_name == 'index':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(page_url)
                if ep_soup is None:
                    continue
                images = ep_soup.select('.chara__img img[src]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
                processed.append(page_name)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Pon no Michi
class PonnoMichiDownload(Winter2024AnimeDownload, NewsTemplate4):
    title = 'Pon no Michi'
    keywords = [title, "Pon no Michi"]
    website = 'https://ponnomichi-pr.com/'
    twitter = 'ponnomichi_pr'
    hashtags = ['ぽんのみち', 'ponnomichi']
    folder_name = 'ponnomichi'

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
        self.download_template_news('ponnomichi')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/Fwy-ZH3aYAAUzwg?format=jpg&name=large')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('div[class*="Visual"] img[srcSet*="kv_"]')
            for image in images:
                image_url = image['srcset']
                if '/static/' not in image_url:
                    continue
                if image_url.startswith('/'):
                    image_url = self.PAGE_PREFIX + image_url[1:]
                image_name = self.generate_image_name_from_url(image_url, 'static')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character')
            self.image_list = []
            images = soup.select('img[src][class*="CharacterImage"]')
            for image in images:
                image_url = image['src']
                if '/static/' not in image_url:
                    continue
                if image_url.startswith('/'):
                    image_url = self.PAGE_PREFIX + image_url[1:]
                image_name = self.generate_image_name_from_url(image_url, 'static')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Saijaku Tamer wa Gomi Hiroi no Tabi wo Hajimemashita.
class SaijakuTamerDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Saijaku Tamer wa Gomi Hiroi no Tabi wo Hajimemashita.'
    keywords = [title, "The Weakest Tamer Began a Journey to Pick Up Trash"]
    website = 'https://saijakutamer-anime.com/'
    twitter = 'saijakutamer'
    hashtags = ['最弱テイマー']
    folder_name = 'saijakutamer'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.c-Post__list',
                                    title_select='.c-Post__title', date_select='.c-Post__date',
                                    id_select='.c-Post__link')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        template = self.PAGE_PREFIX + 'dist/img/top/KV_visual_%s.jpg'
        self.download_by_template(folder, template, 1, 1)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'dist/img/top/visual_chara_%s.webp'
        self.download_by_template(folder, template, 1, 1)


# Saikyou Tank no Meikyuu Kouryaku
class SaikyoTankDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Saikyou Tank no Meikyuu Kouryaku'
    keywords = [title, "The Strongest Tank's Labyrinth Raids"]
    website = 'https://saikyo-tank.com/'
    twitter = 'saikyo_tank'
    hashtags = ['最強タンク']
    folder_name = 'saikyotank'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.p-News__postList a',
                                    date_select='.c-Post__date', title_select='.c-Post__title', id_select=None,
                                    date_func=lambda x: x[0:4] + '.' + x[5:])

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_kv', self.PAGE_PREFIX + 'news/wp-content/uploads/2023/10/STM_01_ティザービジュアル_1@0.3x.png')
        self.add_to_image_list('fv_kv_1', self.PAGE_PREFIX + 'dist/img/top/fv/kv_1.webp')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.p-Chara__charMain source[type][srcset]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset']
                if '/chara/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'chara')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Sasaki to Pii-chan
class SasapiDownload(Winter2024AnimeDownload, NewsTemplate):
    title = 'Sasaki to Pii-chan'
    keywords = [title, 'Sasaki and Peeps', 'Sasapi']
    website = 'https://sasapi-anime.com/'
    twitter = 'sasaki_pichan'
    hashtags = ['ささピー']
    folder_name = 'sasapi'

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
            images = soup.select('.visual_wrap .style_pc img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src']
                if '/images/' in image_url:
                    image_name = self.generate_image_name_from_url(image_url, 'images')
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self, soup=None):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'images/chara/'
        templates = [prefix + 'list_%s.png', prefix + 'a_%s.png']
        self.download_by_template(folder, templates, 3, 1)
        templates = [prefix + 'd_%s_01.png', prefix + 'd_%s_02.png', prefix + 'd_%s_03.png']
        self.download_by_template(folder, templates, 2, 1)


# Sokushi Cheat ga Saikyou sugite, Isekai no Yatsura ga Marude Aite ni Naranai n desu ga.
class SokushiCheatDownload(Winter2024AnimeDownload, NewsTemplate):
    title = "Sokushi Cheat ga Saikyou sugite, Isekai no Yatsura ga Marude Aite ni Naranai n desu ga."
    keywords = [title, "My Instant Death Ability Is So Overpowered, No One in This Other World Stands a Chance Against Me!"]
    website = 'https://sokushicheat-pr.com/'
    twitter = '即死チート'
    hashtags = 'ツキミチ'
    folder_name = 'sokushicheat'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-item',
                                    date_select='.date', title_select='.title', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/sokushicheat_teaser/images/kv%s.jpg'
        self.download_by_template(folder, template, 1, 1)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/sokushicheat_teaser/images/chara-pic%s.png'
        self.download_by_template(folder, template, 2, 1)


# Tsuki ga Michibiku Isekai Douchuu 2nd Season
class Tsukimichi2Download(Winter2024AnimeDownload, NewsTemplate):
    title = "Tsuki ga Michibiku Isekai Douchuu 2nd Season"
    keywords = [title, "Tsukimichi", "Moonlit Fantasy"]
    website = 'https://tsukimichi.com/'
    twitter = 'tsukimichi_PR'
    hashtags = 'ツキミチ'
    folder_name = 'tsukimichi2'

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
        # Paging logic unknown
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news article',
                                    date_select='.date', title_select='.ttl', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.fvslide source[srcset][type]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'][1:]
                if not image_url.endswith('.webp') or image_url.endswith('_sp.webp'):
                    continue
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            images = soup.select('.chardata--inner .v source[srcset]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['srcset'][1:]
                if not image_url.endswith('.webp'):
                    continue
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e S3
class Youzitsu3Download(Winter2024AnimeDownload, NewsTemplate):
    title = "Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e 3rd Season"
    keywords = ["Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e", "Youzitsu", "Youjitsu",
                "Classroom of the Elite"]
    website = 'http://you-zitsu.com/'
    twitter = 'youkosozitsu'
    hashtags = ['you_zitsu', 'よう実', 'ClassroomOfTheElite']
    folder_name = 'youzitsu3'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_media()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.content-entry',
                                    title_select='h2.entry-title span', date_select='div.entry-date span',
                                    id_select=None, id_has_id=True, news_prefix='news.html')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.vis img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('./', '').split('?')[0]
                if not image_url.endswith('.webp') or '/top/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'top')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_media(self):
        folder = self.create_media_directory()

        # Calendar project
        calendar_folder = folder + '/calendar'
        if not os.path.exists(calendar_folder):
            os.makedirs(calendar_folder)
        template = self.PAGE_PREFIX + 'assets/special-calendar/%s.jpg'
        year = 2022
        month = 12
        stop = False
        while year < 2025 and not stop:
            while month <= 12 and not stop:
                image_name = str(year) + str(month).zfill(2)
                month += 1
                if self.is_image_exists(image_name, calendar_folder):
                    continue
                image_url = template % image_name
                result = self.download_image(image_url, calendar_folder + '/' + image_name)
                if result == -1:
                    stop = True
                    break
            month = 1
            year += 1


# Yubisaki to Renren
class YubisakitoRenrenDownload(Winter2024AnimeDownload, NewsTemplate):
    title = "Yubisaki to Renren"
    keywords = ["A Sign of Affection"]
    website = 'https://yubisaki-pr.com/'
    twitter = 'yubisaki_pr'
    hashtags = ['ゆびさきと恋々']
    folder_name = 'yubisakitorenren'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-item',
                                    date_select='.date', title_select='.title', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.kv img[src]')
            self.image_list = []
            for image in images:
                image_url = image['src']
                if '/images/' not in image_url or 'logo' in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'images')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/yubisaki_teaser/images/chara-pic%s.png'
        self.download_by_template(folder, template, 1, 1)
