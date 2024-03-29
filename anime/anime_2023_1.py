from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2
from scan import AnimagePlusScanner, AniverseMagazineScanner
from datetime import datetime, timedelta
import os


# Ars no Kyojuu https://ars-giant.com/ #アルスの巨獣 @ars_giant
# Ayakashi Triangle https://ayakashitriangle-anime.com/ #あやかしトライアングル #あやトラ @ayakashi_anime
# Benriya Saitou-san, Isekai ni Iku https://saitou-anime.com/ #便利屋斎藤さん @saitou_anime
# Buddy Daddies https://buddy-animeproject.com/ #バディダディ @BuddyD_project
# Eiyuuou, Bu wo Kiwameru Tame Tenseisu: Soshite, Sekai Saikyou no Minarai Kishi https://auo-anime.com/ #英雄王 @auo_anime
# Hyouken no Majutsushi ga Sekai wo Suberu http://www.tbs.co.jp/anime/hyouken/ #冰剣の魔術師 #hyouken @hyouken_pr
# Ijiranaide, Nagatoro-san 2nd Attack https://www.nagatorosan.jp/ #長瀞さん @nagatoro_tv
# Inu ni Nattara Suki na Hito ni Hirowareta. https://inuhiro-anime.com/ #犬ひろ @inuninattara
# Isekai Nonbiri Nouka https://nonbiri-nouka.com/ #のんびり農家 @nonbiri_nouka
# Itai no wa https://bofuri.jp/story/ #防振り #bofuri @bofuri_anime
# Kaiko sareta Ankoku Heishi (30-dai) no Slow na Second Life https://ankokuheishi-anime.com/ #暗黒兵士 @ankokuheishi_PR
# Kami-tachi ni Hirowareta Otoko 2 https://kamihiro-anime.com/ #神達に拾われた男 @kamihiro_anime
# Koori Zokusei Danshi to Cool na Douryou Joshi https://icpc-anime.com/ #氷属性男子 @ice_cool_anime
# Kubo-san wa Mob wo Yurusanai https://kubosan-anime.jp/ #久保さん @kubosan_anime
# Kyokou Suiri S2 https://kyokousuiri.jp/ #虚構推理 @kyokou_suiri
# Maou Gakuin no Futekigousha 2nd Season https://maohgakuin.com/ #魔王学院 @maohgakuin
# Mononogatari https://mononogatari-pr.com #もののがたり @mononogatari_pr
# NieR:Automata Ver1.1a #ニーア https://nierautomata-anime.com/ #NieR #ニーアオートマタ @NieR_A_ANIME
# Ningen Fushin no Boukensha-tachi ga Sekai wo Sukuu you desu https://www.ningenfushin-anime.jp/ #人間不信 @ningenfushinPR
# Oniichan wa Oshimai! https://onimai.jp/ #おにまい @onimai_anime
# Ooyukiumi no Kaina https://ooyukiumi.net/ #大雪海のカイナ @ooyukiumi_kaina
# Otonari no Tenshi-sama ni Itsunomanika Dame Ningen ni Sareteita Ken https://otonarino-tenshisama.jp/ #お隣の天使様 @tenshisama_PR
# Rougo ni Sonaete Isekai de 8-manmai no Kinka wo Tamemasu https://roukin8-anime.com/ #ろうきん8 #roukin8 @roukin8_anime
# Saikyou Onmyouji no Isekai Tenseiki https://saikyo-onmyouji.asmik-ace.co.jp/ #最強陰陽師 @saikyo_onmyouji
# Shin Shinka no Mi: Shiranai Uchi ni Kachigumi Jinsei https://shinkanomi-anime.com/ #進化の実 #勝ち組人生 #ゴリラ系女子 @shinkanomianime
# Spy Kyoushitsu https://spyroom-anime.com/ #スパイ教室 #spyroom #SpyClassroom @spyroom_anime
# Sugar Apple Fairy Tale https://sugarapple-anime.com/ #砂糖林檎 @sugarapple_PR
# Tensei Oujo to Tensai Reijou no Mahou Kakumei https://tenten-kakumei.com/ #転天アニメ @tenten_kakumei
# Tomo-chan wa Onnanoko! https://tomo-chan.jp/ #tomochan @tomo_chan_ani
# Tondemo Skill de Isekai Hourou Meshi https://tondemoskill-anime.com/ #とんでもスキル #tondemo_skill @tonsuki_anime
# Tsundere Akuyaku Reijou Liselotte to Jikkyou no Endou-kun to Kaisetsu no Kobayashi-san http://tsunlise-pr.com/ #ツンリゼ @tsunlise_pr
# Vinland Saga S2 https://vinlandsaga.jp/


# Winter 2023 Anime
class Winter2023AnimeDownload(MainDownload):
    season = "2023-1"
    season_name = "Winter 2023"
    folder_name = '2023-1'

    def __init__(self):
        super().__init__()


# Ars no Kyojuu
class ArsGiantDownload(Winter2023AnimeDownload, NewsTemplate):
    title = 'Ars no Kyojuu'
    keywords = [title, 'Giant Beasts of Ars']
    website = 'https://ars-giant.com/'
    twitter = 'ars_giant'
    hashtags = ['アルスの巨獣', 'ars_giant']
    folder_name = 'arsgiant'

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
            soup = self.get_soup(story_url, decode=True)
            li_tags = soup.select('.story nav li')
            for li in li_tags:
                a_tag = li.find('a')
                if a_tag is not None:
                    try:
                        episode = str(int(a_tag.text)).zfill(2)
                    except:
                        continue
                else:
                    continue
                if self.is_image_exists(episode + '_5'):
                    continue
                if li.has_attr('class') and 'is__current' in li['class']:
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(a_tag['href'])
                if ep_soup is not None and episode is not None:
                    images = ep_soup.select('.ssslider img[src]')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = images[i]['src']
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.md-list__news li',
                                    date_select='.date', title_select='.ttl',
                                    id_select='a', next_page_select='.item-next__link')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('ars_kv_logo_c', self.PAGE_PREFIX + 'wp/wp-content/uploads/2022/12/ars_kv_logo_c.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + '_assets/images/char/detail/char_%s.png'
        self.download_by_template(folder, template, 3, 1)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bd/')
            images = soup.select('#Main img[src], #Main image[src]')
            self.image_list = []
            for image in images:
                image_url = image['src'].split('?')[0]
                image_name = self.extract_image_name_from_url(image_url)
                if image_name.startswith('np_'):
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


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
        self.download_media()

    def download_episode_preview(self):
        story_url = self.PAGE_PREFIX + 'story/'
        yt_folder, yt_episodes = self.init_youtube_thumbnail_variables(['01'])
        try:
            soup = self.get_soup(story_url, decode=True)
            li_tags = soup.select('li.story_pager__list')
            for li in li_tags:
                a_tag = li.find('a')
                if a_tag is not None:
                    try:
                        episode = str(int(a_tag.text)).zfill(2)
                    except:
                        continue
                else:
                    continue
                if self.is_image_exists(episode + '_5') and episode in yt_episodes:
                    continue
                if li.has_attr('class') and 'is_current' in li['class']:
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(story_url + a_tag['href'].replace('./', ''))
                if ep_soup is not None and episode is not None:
                    images = ep_soup.select('.main_slide img[src]')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = story_url + images[i]['src']
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
                    yt_tag = ep_soup.select('.p-story_movie_data[data-modal]')
                    if len(yt_tag) > 0:
                        yt_id = yt_tag[0]['data-modal'].split(':')[-1]
                        self.download_youtube_thumbnail_by_id(yt_id, yt_folder, episode)
        except Exception as e:
            self.print_exception(e)

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

    def download_media(self):
        folder = self.create_media_directory()

        # Blu-ray
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        bd_urls = ['shop', '01', '02', '03', '04', '05', '06']
        try:
            for i in range(len(bd_urls)):
                bd_url = self.PAGE_PREFIX + 'bddvd/?no=' + bd_urls[i]
                if i > 0 and str(i) in processed:
                    continue
                soup = self.get_soup(bd_url)
                if soup is not None:
                    images = soup.select('.p-bddvd img[src]')
                    self.image_list = []
                    for image in images:
                        if '/bddvd/' in image['src'] and not image['src'].endswith('jk_np.jpg'):
                            image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                            image_name = 'bddvd_' + self.generate_image_name_from_url(image_url, 'bddvd')
                            self.add_to_image_list(image_name, image_url)
                    if i >= 1:
                        if len(self.image_list) > 1:
                            processed.append(str(i))
                        elif len(self.image_list) == 0:
                            break
                    self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Benriya Saitou-san, Isekai ni Iku
class BenriyaSaitouDownload(Winter2023AnimeDownload, NewsTemplate2):
    title = 'Benriya Saitou-san, Isekai ni Iku'
    keywords = [title, 'Handyman Saitou in Another World']
    website = 'https://saitou-anime.com/'
    twitter = 'saitou_anime'
    hashtags = '便利屋斎藤さん'
    folder_name = 'benriya-saitou'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_episode_preview_guess()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        yt_folder, yt_episodes = self.init_youtube_thumbnail_variables()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/01.html')
            trs = soup.select('#ContentsListUnit02 tr[class]')
            for tr in trs:
                a_tags = tr.select('a[href]')
                if len(a_tags) == 0:
                    continue
                try:
                    episode = str(int(a_tags[0].text.replace('#', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1') and episode in yt_episodes:
                    continue
                if episode == '01':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(self.PAGE_PREFIX + a_tags[0]['href'].replace('../', ''))
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('ul.tp5 img[src]')
                for i in range(len(images)):
                    image_url = self.PAGE_PREFIX + images[i]['src'].split('?')[0].replace('../', '').replace('sn_', '')
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)

                yt_tag = ep_soup.select('.atl_inner iframe[src]')
                if len(yt_tag) > 0 and 'youtube' in yt_tag[0]['src']:
                    yt_id = yt_tag[0]['src'].split('/')[-1]
                    self.download_youtube_thumbnail_by_id(yt_id, yt_folder, episode)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        keywords = ['便利屋斎藤さん、異世界に行く']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20220909', download_id=self.download_id).run()

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'core_sys/images/contents/%s/block/%s/%s.jpg'
        is_successful = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            is_success = False
            first = 20 + i
            second = 27 + 3 * i
            third = 36 + self.IMAGES_PER_EPISODE * i
            for j in range(self.IMAGES_PER_EPISODE):
                image_url = template % (str(first).zfill(8), str(second).zfill(8), str(third + j).zfill(8))
                image_name = episode + '_' + str(j + 1)
                result = self.download_image(image_url, folder + '/' + image_name)
                if result == 0:
                    is_success = True
                    is_successful = True
                elif result == -1:
                    break
            if is_success:
                print(self.__class__.__name__ + ' - Guessed successfully!')
            else:
                if len(os.listdir(folder)) == 0:
                    os.rmdir(folder)
                return
        if len(os.listdir(folder)) == 0:
            os.rmdir(folder)
        return is_successful

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'core_sys/images/news/00000003/block/00000008/00000001.jpg')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FYMHT1jVUAAUtmQ?format=jpg&name=medium')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.kvSlide__img.-kv1 img[src]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src']
                if '/main/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'main')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        # prefix = self.PAGE_PREFIX + 'core_sys/images/main/tz/chara/chara_%s'
        # templates = [prefix + '.png', prefix + '_face.png']
        # self.download_by_template(folder, templates, 2, 1, prefix='tz_')

        template = self.PAGE_PREFIX + 'core_sys/images/main/cont/chara/chara_%s.png'
        self.download_by_template(folder, template, 2, 1)

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['privilege', 'campaign', '01', '02', '03']:
            try:
                if page != 'privilege' and page in processed:
                    continue
                page_url = self.PAGE_PREFIX + 'bd/'
                if page != '01':
                    page_url += page + '.html'
                soup = self.get_soup(page_url)
                images = soup.select('.block_inner img[src]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                    if '/bddvd/' in image_url:
                        image_name = self.generate_image_name_from_url(image_url, 'bddvd')
                    else:
                        image_name = self.extract_image_name_from_url(image_url)
                    if self.is_image_exists(image_name, folder):
                        continue
                    if (page.isnumeric() and not self.is_not_matching_content_length(image_url, 198224))\
                            or (page == 'privilege' and not self.is_not_matching_content_length(image_url, 198434)):
                        continue
                    self.add_to_image_list(image_name, image_url)
                if page != 'privilege' and len(self.image_list) > 0:
                    processed.append(page)
                if page.isnumeric() and len(self.image_list) == 0:
                    break
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Buddy Daddies
class BuddyDaddiesDownload(Winter2023AnimeDownload, NewsTemplate):
    title = 'Buddy Daddies'
    keywords = [title]
    website = 'https://buddy-animeproject.com/'
    twitter = 'BuddyD_project'
    hashtags = 'バディダディ'
    folder_name = 'buddy-daddies'

    PAGE_PREFIX = website
    FINAL_EPISODE = 13

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        story_url = self.PAGE_PREFIX + 'story/'
        yt_folder, yt_episodes = self.init_youtube_thumbnail_variables()
        try:
            soup = self.get_soup(story_url, decode=True)
            story_list = soup.select('.story_tabLists')
            if len(story_list) > 0:
                a_tags = story_list[0].select('a[href]')
                for a_tag in a_tags:
                    span_tag = a_tag.select('span')
                    try:
                        ep_num = int(span_tag[0].text.replace('#', ''))
                        if ep_num is None or ep_num < 1:
                            continue
                        episode = str(ep_num).zfill(2)
                    except:
                        continue
                    if self.is_image_exists(episode + '_1') and episode in yt_episodes:
                        continue
                    if a_tag.has_attr('class') and 'is-current' in a_tag['class']:
                        ep_soup = soup
                    else:
                        ep_soup = self.get_soup(story_url + a_tag['href'].replace('./', ''))
                    if ep_soup is not None:
                        images = ep_soup.select('.swiper-wrapper img[src]')
                        self.image_list = []
                        for i in range(len(images)):
                            image_url = story_url + images[i]['src']
                            image_name = episode + '_' + str(i + 1)
                            self.add_to_image_list(image_name, image_url)
                        self.download_image_list(self.base_folder)

                        # You-Tube thumbnails
                        button_tag = ep_soup.select('.story_movieWrap button[onclick]')
                        if len(button_tag) > 0:
                            onclick = button_tag[0]['onclick']
                            if onclick.startswith("moviePlay('") and onclick.endswith("');"):
                                self.download_youtube_thumbnail_by_id(onclick[11:-3], yt_folder, episode)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        keywords = ['Buddy Daddies']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20221225', download_id=self.download_id).run()

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, paging_type=1, article_select='.newsList',
                                    date_select='.newsList__date time', title_select='.newsList__ttl span',
                                    id_select='a', a_tag_prefix=news_url, next_page_select='.pagination__next')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_news', self.PAGE_PREFIX + 'news/SYS/CONTENTS/4f4398ff-a52c-4179-8717-7e3963739508')
        self.add_to_image_list('kv', self.PAGE_PREFIX + 'assets/img/top/visual/mv2/mv2_visual.jpg')
        self.add_to_image_list('kv_news', self.PAGE_PREFIX + 'news/SYS/CONTENTS/5f4446c0-248d-42ac-97e7-4db68bb21042')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.chara_img img[src]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('./', '')
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        bd_prefix = self.PAGE_PREFIX + 'bddvd/'
        for page in ['tokuten', 'vol1', 'vol2', 'vol3', 'vol4', 'vol5', 'vol6']:
            try:
                if page != 'tokuten' and page in processed:
                    continue
                bd_url = bd_prefix
                if page != 'vol1':
                    bd_url += page + '.html'
                soup = self.get_soup(bd_url)
                images = soup.select('.bddvd_Article img[src]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'][1:]
                    if '/bddvd/' in image_url:
                        image_name = self.generate_image_name_from_url(image_url, 'bddvd')
                    else:
                        image_name = self.extract_image_name_from_url(image_url)
                    if image_name == 'img_np' or image_name == 'bnr_event':
                        continue
                    if self.is_image_exists(image_name, folder):
                        continue
                    self.add_to_image_list(image_name, image_url)
                if page.startswith('vol'):
                    if len(self.image_list) == 0:
                        break
                    else:
                        processed.append(page)
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Eiyuuou, Bu wo Kiwameru Tame Tenseisu: Soshite, Sekai Saikyou no Minarai Kishi
class EiyuuouDownload(Winter2023AnimeDownload, NewsTemplate):
    title = 'Eiyuuou, Bu wo Kiwameru Tame Tenseisu: Soshite, Sekai Saikyou no Minarai Kishi'
    keywords = [title]
    website = 'https://auo-anime.com/'
    twitter = 'auo_anime'
    hashtags = '英雄王'
    folder_name = 'eiyuuou'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_episode_preview_guess()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        yt_folder, yt_episodes = self.init_youtube_thumbnail_variables(['13'])
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/', decode=True)
            stories = soup.select('.story-box')
            for story in stories:
                try:
                    episode = str(int(story.select('.story-title span.num')[0].text.replace('#', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1') and episode in yt_episodes:
                    continue
                images = story.select('.story-pic img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)

                # YouTube thumbnail
                try:
                    yt_tag = story.select('.story-movie iframe[src]')
                    if len(yt_tag) > 0 and len(yt_tag[0]['src']) > 0:
                        yt_id = yt_tag[0]['src'].split('/')[-1]
                        self.download_youtube_thumbnail_by_id(yt_id, yt_folder, episode)
                except:
                    pass
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        keywords = ['英雄王、武を極めるため転生す']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20230106', download_id=self.download_id).run()

    def download_episode_preview_guess(self):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_1'):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wp/wp-content/uploads/%s/%s/%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        sub_folder = f'{folder}/{year}/{month}'
        if not os.path.exists(sub_folder):
            os.makedirs(sub_folder)
        is_successful = False
        for i in range(1, self.IMAGES_PER_EPISODE + 1, 1):
            j = -1
            while j < 10:
                j += 1
                image_name = f'{i}-{j}'
                if self.is_image_exists(image_name, sub_folder):
                    continue
                if j == 0:
                    img_name = str(i).zfill(2)
                else:
                    img_name = str(i).zfill(2) + '-' + str(j)
                image_url = template % (year, month, img_name)
                result = self.download_image(image_url, sub_folder + '/' + image_name)
                if result == -1:
                    break
                is_successful = True
            if not is_successful:
                break
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.news-item',
                                    date_select='p.date', title_select='p.title', id_select='a',
                                    next_page_select='.next-button',
                                    next_page_eval_index_class='off', next_page_eval_index=0)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'wp/wp-content/themes/euo-teaser-theme/img/kv.jpg')
        # self.add_to_image_list('tz_news', self.PAGE_PREFIX + 'wp/wp-content/uploads/2022/02/英雄王_ティザービジュアル.jpg')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FNYCWh2VgAM1rSE?format=jpg&name=large')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/FfkoAcKUYAEtkVS?format=jpg&name=4096x4096')
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'wp/wp-content/themes/euo-honban-theme/images/kv-pc.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'chara/')
            self.image_list = []
            images = soup.select('.pic-box img[src]')
            for image in images:
                image_url = image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

        # template = self.PAGE_PREFIX + 'wp/wp-content/themes/euo-honban-theme/images/chara-pic%s.png'
        # self.download_by_template(folder, template, 2, 1)

        # template = self.PAGE_PREFIX + 'wp/wp-content/themes/euo-teaser-theme/img/chara-pic%s.png'
        # self.download_by_template(folder, template, 1, 1, prefix='tz_')

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bluray/')
            self.image_list = []
            images = soup.select('.section-contents img[src]')
            for image in images:
                image_url = image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


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
        self.download_episode_preview_external()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'story/img/story%s/%s.jpg'
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

        yt_folder, yt_episodes = self.init_youtube_thumbnail_variables()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            stories = soup.select('.story-nav a[href]')
            for story in stories:
                img_tag = story.select('img[alt]')
                if len(img_tag) == 0:
                    continue
                try:
                    episode = str(int(img_tag[0]['alt'].replace('#', ''))).zfill(2)
                except:
                    continue
                if episode in yt_episodes:
                    continue
                ep_soup = self.get_soup(self.PAGE_PREFIX + story['href'].replace('../', ''))
                if ep_soup is None:
                    continue
                yt_tag = ep_soup.select('.story-yokoku-block a[href]')
                if len(yt_tag) > 0 and 'youtube' in yt_tag[0]['href'] and '=' in yt_tag[0]['href']:
                    yt_id = yt_tag[0]['href'].split('=')[-1]
                    self.download_youtube_thumbnail_by_id(yt_id, yt_folder, episode)
        except Exception as e:
            self.print_exception(e, 'YouTube thumbnails')

    def download_episode_preview_external(self):
        keywords = ['冰剣の魔術師が世界を統べる']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20230103', download_id=self.download_id).run()

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsall-box',
                                    date_select='.newsall-date', title_select='a', id_select='a',
                                    a_tag_prefix=self.PAGE_PREFIX + 'news/')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.add_to_image_list('top_teaser_pc@2x', self.PAGE_PREFIX + 'img/top_teaser_pc@2x.jpg')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FdP3sZqagAIEGcr?format=jpg&name=large')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/Fi4YSm9acAA2q3N?format=jpg&name=large')
        self.add_to_image_list('kv1_news', self.PAGE_PREFIX + 'news/img/news20221201_01.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'character/img/chara_img_%s@2x.png'
        self.download_by_template(folder, template, 2, 1)

    def download_media(self):
        folder = self.create_media_directory()
        bd_url = self.PAGE_PREFIX + 'disc/'
        try:
            soup = self.get_soup(bd_url)
            images = soup.select('.music-artist-img img[src], .news-img img[src], .disc-oritoku-img img[src]')
            self.image_list = []
            for image in images:
                if not image['src'].startswith('img/'):
                    continue
                temp_name = image['src'].split('/')[-1]
                if 'nowprint' in temp_name:
                    continue
                image_url = bd_url + image['src']
                image_name = self.generate_image_name_from_url(image_url, 'img')
                if image_name.startswith('gentei_sample'):
                    if self.is_image_exists(image_name, folder):
                        continue
                    if not self.is_content_length_in_range(image_url, more_than_amount=7300):
                        continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


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
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        story_url = self.PAGE_PREFIX + 'story/'
        try:
            soup = self.get_soup(story_url, decode=True)
            a_tags = soup.select('.tab a[href]')
            for a_tag in a_tags:
                try:
                    episode = str(int(a_tag.text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_8'):
                    continue
                if a_tag['href'] == './':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(story_url + a_tag['href'].replace('./', ''))
                if ep_soup is not None:
                    images = ep_soup.select('.thumb .swiper-wrapper img[src]')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = self.PAGE_PREFIX + images[i]['src'].replace('../', '')
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.list li',
                                    date_select='time', title_select='p', id_select='a',
                                    a_tag_prefix=self.PAGE_PREFIX + 'news/')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser_img_mainimg', self.PAGE_PREFIX + 'teaser/img/mainimg.jpg')
        self.add_to_image_list('tz', 'https://pbs.twimg.com/media/FWeINYraUAEG6y9?format=jpg&name=medium')
        self.add_to_image_list('img_top_mainimg', self.PAGE_PREFIX + 'assets/img/top/mainimg.jpg')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/FflFw89UcAIGEf9?format=jpg&name=medium')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/img/character/img_%s.png'
        self.download_by_template(folder, template, 2, 1)

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['tokuten', '01', '02', '03', '04']:
            try:
                if page != 'tokuten' and page in processed:
                    continue
                page_url = self.PAGE_PREFIX + 'blu-ray/' + page + '.html'
                soup = self.get_soup(page_url)
                images = soup.select('.jacket img[src], .tokuten img[src]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                    if 'nowprinting' in image_url:
                        continue
                    if '/blu-ray/' in image_url:
                        image_name = self.generate_image_name_from_url(image_url, 'blu-ray')
                    elif '/common/' in image_url:
                        image_name = self.generate_image_name_from_url(image_url, 'common')
                    else:
                        continue
                    if self.is_image_exists(image_name, folder):
                        continue
                    self.add_to_image_list(image_name, image_url)
                if page.isnumeric():
                    if len(self.image_list) == 0:
                        break
                    else:
                        processed.append(page)
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Inu ni Nattara Suki na Hito ni Hirowareta.
class InuhiroDownload(Winter2023AnimeDownload, NewsTemplate):
    title = "Inu ni Nattara Suki na Hito ni Hirowareta."
    keywords = [title, 'Inuhiro']
    website = 'https://inuhiro-anime.com/'
    twitter = 'inuninattara'
    hashtags = '犬ひろ'
    folder_name = 'inuhiro'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'assets/images/story/%s_%s.jpg'
        try:
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1).zfill(2), str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1)
                    result = self.download_image(image_url, self.base_folder + '/' + image_name)
                    if result == -1:
                        return
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        AnimagePlusScanner('犬ひろ', self.base_folder, last_episode=self.FINAL_EPISODE,
                           end_date='20221227', download_id=self.download_id).run()

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='#news article',
                                    date_select='time', title_select='h3', id_select=None, id_has_id=True)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FNybC1EaAAEoRmq?format=jpg&name=large')
        self.add_to_image_list('tz_mainimg_pc', self.PAGE_PREFIX + 'teaser/images/mainimg_pc.png')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/FZyBd0xVEAAz4kn?format=jpg&name=medium')
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'teaser/images/mainimg.jpg')
        self.add_to_image_list('kv2_tw', 'https://pbs.twimg.com/media/FgduJ2uaEAEPqiy?format=jpg&name=4096x4096')
        # self.add_to_image_list('kv2', self.PAGE_PREFIX + 'assets/images/top/mainimg.jpg')
        self.add_to_image_list('kv3_tw', 'https://pbs.twimg.com/media/FhRGNtKUAAAT8ea?format=jpg&name=4096x4096')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.mainimg .slider img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src']
                if '/images/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'images')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/images/character/img_%s.png'
        self.download_by_template(folder, template, 2, 1)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'blu-ray/')
            images = soup.select('.jacket img[src], .tokuten img[src]')
            self.image_list = []
            for image in images:
                if '/blu-ray/' not in image['src']:
                    continue
                temp_name = image['src'].split('/')[-1]
                if temp_name.startswith('nowprinting'):
                    continue
                image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                image_name = self.generate_image_name_from_url(image_url, 'blu-ray')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Isekai Nonbiri Nouka
class IsekaiNonbiriNoukaDownload(Winter2023AnimeDownload):
    title = 'Isekai Nonbiri Nouka'
    keywords = [title]
    website = 'https://nonbiri-nouka.com/'
    twitter = 'nonbiri_nouka'
    hashtags = 'のんびり農家'
    folder_name = 'nonbiri-nouka'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 5

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'story/episode%s/images/img_%s.jpg'
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
        news_url = self.PAGE_PREFIX + 'news/'
        try:
            soup = self.get_soup(news_url, decode=True)
            dts = soup.select('dl#newsList dt')
            dds = soup.select('dl#newsList dd')
            if len(dts) != len(dds):
                raise Exception('Tags not matched')
            news_obj = self.get_last_news_log_object()
            results = []
            for i in range(len(dts)):
                date = dts[i].text
                title = ' '.join(dds[i].text.strip().split())
                article_id = ''
                a_tag = dds[i].find('a')
                if a_tag is not None and a_tag.has_attr('href') and a_tag['href'].startswith('/'):
                    article_id = self.PAGE_PREFIX + a_tag['href'][1:]
                if news_obj and (news_obj['id'] == article_id or date < news_obj['date']):
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
        self.add_to_image_list('tz', 'https://ogre.natalie.mu/media/news/comic/2022/0826/nonbiri-nouka_Teaser.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'character/%s/images/img_character.png'
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            charas = soup.select('#characterNavList a[href]')
            self.image_list = []
            for chara in charas:
                split1 = chara['href'].split('/')
                if len(split1) > 1:
                    image_name = split1[-2]
                    image_url = template % image_name
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'media/blu-ray/index.html')
            images = soup.select('#contentsBg img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'][1:]
                if self.is_content_length_in_range(image_url, more_than_amount=22919):
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Itai no wa Iya nano de Bougyoryoku ni Kyokufuri Shitai to Omoimasu. 2nd Season
class Bofuri2Download(Winter2023AnimeDownload):
    title = "Itai no wa Iya nano de Bougyoryoku ni Kyokufuri Shitai to Omoimasu. 2"
    keywords = [title, 'bofuri', "BOFURI: I Don't Want to Get Hurt, so I'll Max Out My Defense.", '2nd']
    website = "https://bofuri.jp/"
    twitter = 'bofuri_anime'
    hashtags = ['bofuri', '#防振り']
    folder_name = 'bofuri2'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            template = self.PAGE_PREFIX + 'assets/story/%s/%s.jpg'
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

        # YouTube thumbnails
        yt_folder, yt_episodes = self.init_youtube_thumbnail_variables()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'news/')
            items = soup.select('section.news-data')
            for item in items:
                tag_title = item.find('div', class_='title')
                a_tag = item.select('a[href]')
                if tag_title is not None and len(a_tag) > 0:
                    title = tag_title.text.strip()
                    if '予告' not in title:
                        continue
                    dai_index = title.find('第')
                    wa_index = title.find('話')
                    if dai_index >= 0 and wa_index >= 0 and dai_index + 1 < wa_index:
                        try:
                            episode = str(int(title[dai_index + 1:wa_index])).zfill(2)
                        except:
                            continue
                        if episode in yt_episodes:
                            break
                        news_soup = self.get_soup(self.PAGE_PREFIX + 'news/' + a_tag[0]['href'].replace('./', ''))
                        if news_soup is not None:
                            tags = news_soup.select('.news-body a[href]')
                            for tag in tags:
                                if 'youtube' in tag['href'] and 'watch?v=' in tag['href']:
                                    yt_id = tag['href'].split('=')[-1]
                                    self.download_youtube_thumbnail_by_id(yt_id, yt_folder, episode)
                                    break
        except Exception as e:
            self.print_exception(e, 'YouTube thumbnails')

    def download_episode_preview_external(self):
        keywords = ['痛いのは嫌なので防御力に極振りしたいと思います']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20230110', download_id=self.download_id).run()

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        try:
            soup = self.get_soup(news_url, decode=True)
            articles = soup.select('section.news-data')
            news_obj = self.get_last_news_log_object()
            results = []
            for article in articles:
                tag_date = article.find('div', class_='date')
                tag_title = article.find('div', class_='title')
                a_tag = article.find('a')
                if tag_date and tag_title and a_tag and a_tag.has_attr('href'):
                    article_id = news_url + a_tag['href'].replace('./', '')
                    date = self.format_news_date(tag_date.text.strip().replace('/', '.'))
                    if len(date) == 0:
                        continue
                    title = tag_title.text.strip()
                    if date.startswith('2021.01.04') or (news_obj and
                                                         (news_obj['id'] == article_id or date < news_obj['date'])):
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
        self.add_to_image_list('animation_works', 'https://pbs.twimg.com/media/ErSRQUmVoAAkgt7?format=jpg&name=large')
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/ErSKnRwW8AAjOyU?format=jpg&name=4096x4096')
        self.add_to_image_list('aprilfools_tw', 'https://pbs.twimg.com/media/FPOV5F5agAE3czc?format=jpg&name=4096x4096')
        self.add_to_image_list('aprilfools_news', self.PAGE_PREFIX + 'assets/news/65a.jpg')
        self.add_to_image_list('aprilfools_top', self.PAGE_PREFIX + 'images/top-visual/2022apr/all.jpg')
        self.add_to_image_list('vis-s2', self.PAGE_PREFIX + 'assets/news/vis-s2.jpg')
        self.download_image_list(folder)

        sub_folder = self.create_custom_directory(folder.split('/')[-1] + '/news')
        cache_filepath = sub_folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'news/')
            items = soup.select('section.news-data a[href]')
            for item in items:
                if not item['href'].endswith('.html'):
                    continue
                page_name = item['href'].split('/')[-1].split('.html')[0]
                if page_name in processed:
                    break
                title = item.text.strip()
                if 'ビジュアル' in title:
                    news_soup = self.get_soup(self.PAGE_PREFIX + 'news/' + item['href'].replace('./', ''))
                    if news_soup is not None:
                        images = news_soup.select('section.news-entry img[src]')
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

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/character/%s.png'
        self.download_by_template(folder, template, 1, 1)

    def download_media(self):
        folder = self.create_media_directory()

        # Blu-ray
        try:
            self.image_list = []
            soup = self.get_soup(self.PAGE_PREFIX + 'bluray/')
            images = soup.select('.bd-img img[src]')
            for image in images:
                if '/bluray/' in image['src'] and not image['src'].endswith('/np.png'):
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                    image_name = self.generate_image_name_from_url(image_url, 'bluray')
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')

        # Blu-ray Bonus
        try:
            self.image_list = []
            soup = self.get_soup(self.PAGE_PREFIX + 'bluray/campaign.html')
            images = soup.select('.bd-cp-img img[src], .bd-shopbnf-img img[src]')
            for image in images:
                if '/bluray/' in image['src'] and not image['src'].endswith('/np.png'):
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                    image_name = self.generate_image_name_from_url(image_url, 'bluray')
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray Bonus')


# Kaiko sareta Ankoku Heishi (30-dai) no Slow na Second Life
class AnkokuHeishiDownload(Winter2023AnimeDownload, NewsTemplate):
    title = 'Kaiko sareta Ankoku Heishi (30-dai) no Slow na Second Life'
    keywords = [title]
    website = 'https://ankokuheishi-anime.com/'
    twitter = 'ankokuheishi_PR'
    hashtags = '暗黒兵士'
    folder_name = 'ankokuheishi'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 8

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_guess()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/story01/')
            stories = soup.select('.story_nav a[href]')
            for story in stories:
                try:
                    episode = str(int(story.text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if story.has_attr('class') and 'active' in story['class']:
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(story['href'])
                if ep_soup is None:
                    continue
                images = ep_soup.select('.wp-swiper__slide-content img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = self.clear_resize_in_url(images[i]['src'])
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news_item',
                                    date_select='.post_date', title_select='a', id_select='a')

    def download_episode_preview_guess(self):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_1'):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wp-content/uploads/%s/%s/%s.png'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        skip_filenames = self.get_skip_filenames(folder, year, month)
        sub_folder = f'{folder}/{year}/{month}'
        if not os.path.exists(sub_folder):
            os.makedirs(sub_folder)
        is_successful = False
        for i in range(1, self.IMAGES_PER_EPISODE + 1, 1):
            j = -1
            while j < 10:
                j += 1
                image_name = f'{i}-{j}'
                skip_name = f'{year}-{month}-{i}-{j}'
                if self.is_image_exists(image_name, sub_folder) or skip_name in skip_filenames:
                    continue
                if j == 0:
                    img_name = str(i).zfill(2)
                else:
                    img_name = str(i).zfill(2) + '-' + str(j)
                image_url = template % (year, month, img_name)
                result = self.download_image(image_url, sub_folder + '/' + image_name)
                if result == -1:
                    break
                is_successful = True
            if not is_successful:
                break
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful

    @staticmethod
    def get_skip_filenames(folder, year, month):
        skip_filenames = []
        if year == '2023' and month == '01':
            for i in range(8):
                for j in range(2):
                    skip_filenames.append(f'2023-01-{i + 1}-{j}')
        return skip_filenames

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', 'https://pbs.twimg.com/media/FagSmPnUEAA4PNg?format=jpg&name=medium')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.header_area p.mv img[src]')
            for image in images:
                if '/img/' in image['src']:
                    image_url = image['src']
                    image_name = self.generate_image_name_from_url(image_url, 'img')
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'wp-content/themes/ankokuheishi/img/chara'
        templates = [prefix + '%s_a.png', prefix + '%s_b.png']
        self.download_by_template(folder, templates, 2, 1)

    def download_media(self):
        folder = self.create_media_directory()

        # Blu-ray
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bd/')
            images = soup.select('.bd_item__jacket img[src], .bd_item img[src]')
            self.image_list = []
            for image in images:
                image_url = image['src']
                image_name = self.extract_image_name_from_url(image_url)
                if 'now_printing' in image_name:
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')

        self.image_list = []
        self.add_to_image_list('comment_img', self.PAGE_PREFIX + 'img/comment_img.png')
        self.download_image_list(folder)

        # Modal PV
        modal_folder = folder + '/modal'
        if not os.path.exists(modal_folder):
            os.makedirs(modal_folder)
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            modal_tag = soup.select('a[href].modal_pv2')
            if len(modal_tag) > 0 and 'youtube' in modal_tag[0]['href']:
                yt_id = modal_tag[0]['href'].split('/')[-1]
                yt_image_url = f'https://img.youtube.com/vi/{yt_id}/maxresdefault.jpg'
                if not self.is_image_exists(yt_id, modal_folder):
                    self.download_image(yt_image_url, modal_folder + '/' + yt_id)
        except Exception as e:
            self.print_exception(e, 'Modal')


# Kami-tachi ni Hirowareta Otoko 2
class Kamihiro2Download(Winter2023AnimeDownload, NewsTemplate):
    title = 'Kami-tachi ni Hirowareta Otoko 2'
    keywords = [title, 'Kamihiro', 'Kamitachi', '2nd', 'By the Grace of the Gods']
    website = 'https://kamihiro-anime.com/'
    twitter = 'kamihiro_anime'
    hashtags = '神達に拾われた男'
    folder_name = 'kamihiro2'

    PAGE_PREFIX = website
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_episode_preview_guess()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            stories = soup.select('.story nav a[href]')
            for story in stories:
                try:
                    episode = str(int(story.text)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                ep_soup = self.get_soup(story['href'])
                if ep_soup is None:
                    continue
                images = ep_soup.select('.ssslider--cont img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        # Paging logic not known
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.md-list__news li',
                                    date_select='.date', title_select='.ttl', id_select='a')

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + '2nd/wp-content/uploads/%s/%s/%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        curr_month = current_date.strftime('%m')
        is_successful = False
        for year in ['2022', '2023']:
            months = []
            if year == '2022':
                months.append('12')
            else:
                k = 0
                while k <= 12:
                    k += 1
                    months.append(str(k).zfill(2))
                    if curr_month == str(k).zfill(2):
                        break
            for month in months:
                sub_folder = f'{folder}/{year}/{month}'
                if not os.path.exists(sub_folder):
                    os.makedirs(sub_folder)
                for i in range(1, self.IMAGES_PER_EPISODE + 1, 1):
                    j = -1
                    while j < 13:
                        j += 1
                        image_name = f'{i}-{j}'
                        if self.is_image_exists(image_name, sub_folder):
                            continue
                        if j == 0:
                            img_name = str(i).zfill(2)
                        else:
                            img_name = str(i).zfill(2) + '-' + str(j)
                        image_url = template % (year, month, img_name)
                        result = self.download_image(image_url, sub_folder + '/' + image_name)
                        if result == -1:
                            break
                        is_successful = True
                    if not is_successful:
                        break
                if len(os.listdir(sub_folder)) == 0:
                    break
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        news_prefix = self.PAGE_PREFIX + '2nd/wp-content/uploads/'
        self.image_list = []
        self.add_to_image_list('news_tz', news_prefix + '2022/09/logoc_GFF_TeaserVisual_s.jpg')
        self.add_to_image_list('news_kv1', news_prefix + '2022/11/GFF_KeyVisual_logoc.jpg')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.fvslide img[src]')
            for image in images:
                if '/images/' in image['src']:
                    image_url = image['src']
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + '2nd/wp-content/themes/kamihiro2-teaser/_assets/images/char/detail/char%s_pc.png'
        self.download_by_template(folder, template, 2, 1)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bd/')
            self.image_list = []
            images = soup.select('.packageimg img[src], .tokutenimg img[src]')
            for image in images:
                if 'np_square' in image['src']:
                    continue
                image_url = self.clear_resize_in_url(image['src'])
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Koori Zokusei Danshi to Cool na Douryou Joshi
class KooriZokuseiDanshiDownload(Winter2023AnimeDownload, NewsTemplate):
    title = 'Koori Zokusei Danshi to Cool na Douryou Joshi'
    keywords = [title, 'The Ice Guy and His Cool Female Colleague']
    website = 'https://icpc-anime.com/'
    twitter = 'ice_cool_anime'
    hashtags = '氷属性男子'
    folder_name = 'koori-zokusei-danshi'

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
        self.download_media()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'dist/img/story/ep%s/img%s.webp'
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                continue
            stop = False
            for j in range(self.IMAGES_PER_EPISODE):
                image_url = template % (str(i + 1), str(j + 1))
                image_name = episode + '_' + str(j + 1)
                if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                    stop = True
                    break
                webp_image_file = self.base_folder + '/' + episode + '_' + str(j + 1) + '.webp'
                if os.path.exists(webp_image_file):
                    try:
                        self.convert_image_to_jpg(webp_image_file)
                    except Exception as e:
                        self.print_exception(e, 'Error in converting webp to jpg.')
            if stop:
                break

        # YouTube thumbnails
        yt_folder, yt_episodes = self.init_youtube_thumbnail_variables(['01'])
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'special/')
            items = soup.select('.p-MovieList__item')
            for item in reversed(items):
                title = item.select('.p-figcatiopn-text')
                image = item.select('.p-Movie__figure img[src]')
                if len(title) == 0 or len(image) == 0:
                    continue
                try:
                    index1 = title[0].text.find('第')
                    index2 = title[0].text.find('話')
                    if index1 == -1 or index2 == -1 or index1 >= index2:
                        continue
                    episode = str(int(title[0].text[index1 + 1: index2])).zfill(2)
                except:
                    continue
                if episode in yt_episodes:
                    continue
                yt_id = image[0]['src'].split('/')[-2]
                self.download_youtube_thumbnail_by_id(yt_id, yt_folder, episode)
        except Exception as e:
            self.print_exception(e, 'YouTube thumbnail')

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, paging_type=3, paging_suffix='?page=%s',
                                    article_select='.c-News__item', date_select='.c-News__date', date_separator=' ',
                                    title_select='.c-News__title', id_select='a', a_tag_start_text_to_remove='./',
                                    a_tag_prefix=news_url, next_page_select='.c-Pager__item', next_page_eval_index=-1,
                                    next_page_eval_index_class='-current')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv', self.PAGE_PREFIX + 'dist/img/top/kv.jpg')
        self.add_to_image_list('kv_news', self.PAGE_PREFIX + 'dist/img/news/article/news34/kv.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        data_modal_names = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            divs = soup.select('.p-Character__item')
            self.image_list = []
            for div in divs:
                images = div.select('img[src].p-image-item')
                if len(images) == 0:
                    continue
                image = images[0]
                image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)

                # Modal
                if div.has_attr('data-modal_name'):
                    data_modal_names.append(div['data-modal_name'])
                else:
                    modal_divs = div.select('div[data-modal_name]')
                    if len(modal_divs) > 0:
                        data_modal_names.append(modal_divs[0]['data-modal_name'])
            self.download_image_list(folder)

            for data_modal_name in data_modal_names:
                modal_image_url_base = self.PAGE_PREFIX + f'dist/img/character/chara_modal_{data_modal_name}'
                modal_image_url = modal_image_url_base + '.png'
                modal_image_name = f'chara_modal_{data_modal_name}'
                if self.is_image_exists(modal_image_name, folder):
                    continue
                modal_image_filepath = folder + '/' + modal_image_name
                result = self.download_image(modal_image_url, modal_image_filepath)
                if result == -1:
                    new_image_url = modal_image_url_base + '.jpg'
                    self.download_image(new_image_url, modal_image_filepath)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        bd_prefix = self.PAGE_PREFIX + 'bd/'
        for page in ['vol1', 'vol2', 'vol3', 'vol4']:
            try:
                if page in processed:
                    continue
                page_url = bd_prefix + page + '.php'
                soup = self.get_soup(page_url)
                images = soup.select('.p-BdDetail__content img[src]')
                now_printing = False
                is_image_downloaded = False
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                    if '/bd/' not in image_url:
                        continue
                    image_name = self.generate_image_name_from_url(image_url, 'bd')
                    if self.is_image_exists(image_name, folder):
                        is_image_downloaded = True
                        continue
                    if self.is_not_matching_content_length(image_url, 16854):
                        self.add_to_image_list(image_name, image_url)
                    else:
                        now_printing = True
                if len(self.image_list) > 0:
                    is_image_downloaded = True
                self.download_image_list(folder)
                if not now_printing:
                    processed.append(page)
                elif not is_image_downloaded:
                    break
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Kubo-san wa Mob wo Yurusanai
class KubosanDownload(Winter2023AnimeDownload, NewsTemplate2):
    title = 'Kubo-san wa Mob wo Yurusanai'
    keywords = [title, "Kubo Won't Let Me Be Invisible"]
    website = 'https://kubosan-anime.jp/'
    twitter = 'kubosan_anime'
    hashtags = '久保さん'
    folder_name = 'kubosan'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_episode_preview_guess()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/01.html')
            trs = soup.select('#ContentsListUnit02 tr[class]')
            for tr in trs:
                a_tags = tr.select('a[href]')
                if len(a_tags) == 0:
                    continue
                try:
                    episode = str(int(a_tags[0].text.replace('#', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if episode == '01':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(self.PAGE_PREFIX + a_tags[0]['href'].replace('../', ''))
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('ul.tp5 img[src]')
                for i in range(len(images)):
                    image_url = self.PAGE_PREFIX + images[i]['src'].split('?')[0].replace('../', '').replace('sn_', '')
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        keywords = ['久保さんは僕を許さない']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20230104', download_id=self.download_id).run()

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'core_sys/images/contents/%s/block/%s/%s.jpg'
        is_successful = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            is_success = False
            first = 18 + i
            second = 34 + 4 * i
            third = 45 + self.IMAGES_PER_EPISODE * i
            break_inner_loop = False
            for k in [0, -1, 1]:
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(first).zfill(8), str(second + k).zfill(8), str(third + j).zfill(8))
                    image_name = episode + '_' + str(j + 1)
                    if not self.is_content_length_in_range(image_url, more_than_amount=11000):
                        break
                    result = self.download_image(image_url, folder + '/' + image_name)
                    if result == 0:
                        is_success = True
                        is_successful = True
                        break_inner_loop = True
                    elif result == -1:
                        break
                if break_inner_loop:
                    break
            if is_success:
                print(self.__class__.__name__ + ' - Guessed successfully!')
            else:
                if len(os.listdir(folder)) == 0:
                    os.rmdir(folder)
                return
        if len(os.listdir(folder)) == 0:
            os.rmdir(folder)
        return is_successful

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

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.kvSlide__img img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src']
                if '/kv/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'kv')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        self.add_to_image_list('tz_chara_kubo', self.PAGE_PREFIX + 'core_sys/images/main/tz/chara_kubo.png')
        self.add_to_image_list('tz_chara_shiraishi', self.PAGE_PREFIX + 'core_sys/images/main/tz/chara_shiraishi.png')
        self.download_image_list(folder)

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['privilege', 'campaign', '01', '02']:
            try:
                if page != 'privilege' and page != 'campaign' and page in processed:
                    continue
                page_url = self.PAGE_PREFIX + 'bd/'
                if page != '01':
                    page_url += page + '.html'
                soup = self.get_soup(page_url)
                images = soup.select('.block_inner img[src]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                    if '/bddvd/' in image_url:
                        image_name = self.generate_image_name_from_url(image_url, 'bddvd')
                    else:
                        image_name = self.extract_image_name_from_url(image_url)
                    if self.is_image_exists(image_name, folder):
                        continue
                    if (page.isnumeric() and not self.is_not_matching_content_length(image_url, 14750))\
                            or (page == 'privilege' and not self.is_not_matching_content_length(image_url, 30208)):
                        continue
                    self.add_to_image_list(image_name, image_url)
                if page.isnumeric():
                    if len(self.image_list) == 0:
                        break
                    else:
                        processed.append(page)
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


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
        self.download_media()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            stories = soup.select('.p-story_list__item')
            for story in stories:
                try:
                    episode = str(int(story.select('.p-story_ep__no')[0].text.replace('第', '')
                                      .replace('話', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                images = story.select('.p-img_slide__item img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

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
        self.add_to_image_list('kv2_tw', 'https://pbs.twimg.com/media/FjQT78GaEAIK2Fs?format=jpg&name=medium')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'assets_2t/img/top/main/img_main_kv%s.png'
        self.download_by_template(folder, template, 1, 2)

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

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        bd_prefix = self.PAGE_PREFIX + 'bd/'
        for page in ['store', 'vol1', 'vol2', 'vol3', 'vol4']:
            try:
                if page != 'store' and page in processed:
                    continue
                page_url = bd_prefix + page + '/'
                soup = self.get_soup(page_url)
                images = soup.select('.p-bddvd__inner img[src]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'][1:]
                    image_name = self.extract_image_name_from_url(image_url)
                    if 'nowpri' == image_name or self.is_image_exists(image_name, folder):
                        continue
                    self.add_to_image_list(image_name, image_url)
                if page.startswith('vol'):
                    if len(self.image_list) > 0:
                        processed.append(page)
                    else:
                        break
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Maou Gakuin no Futekigousha: Shijou Saikyou no Maou no Shiso, Tensei shite Shison-tachi no Gakkou e II
class Maohgakuin2Download(Winter2023AnimeDownload, NewsTemplate):
    title = "Maou Gakuin no Futekigousha: Shijou Saikyou no Maou no Shiso, Tensei shite Shison-tachi no Gakkou e II"
    keywords = [title, 'Maohgakuin', 'The Misfit of Demon King Academy', '2nd']
    website = "https://maohgakuin.com/"
    twitter = 'maohgakuin'
    hashtags = '魔王学院'
    folder_name = 'maohgakuin2'

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
        yt_folder, yt_episodes = self.init_youtube_thumbnail_variables()
        try:
            soup = self.get_soup(self.PAGE_PREFIX, decode=True)
            li_tags = soup.select('.story_list__item')
            for li in li_tags:
                p_tags = li.select('p')
                p_tag = None
                for tag in p_tags:
                    if tag.has_attr('class') and '-no' in tag['class']:
                        p_tag = tag
                        break
                if p_tag is None:
                    continue
                try:
                    episode = str(int(p_tag.text.upper().replace('EPISODE', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1') and episode in yt_episodes:
                    continue
                a_tag = li.find('a')
                if a_tag is None:
                    continue
                ep_soup = self.get_soup(self.PAGE_PREFIX + a_tag['href'])
                if ep_soup is not None:
                    images = ep_soup.select('.image_slide img[src]')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = story_url + images[i]['src']
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)

                    # YouTube thumbnail
                    yt_tag = ep_soup.select('.movie_item[data-modal]')
                    if len(yt_tag) > 0 and len(yt_tag[0]['data-modal']) > 0:
                        yt_id = yt_tag[0]['data-modal'].split(':')[-1]
                        self.download_youtube_thumbnail_by_id(yt_id, yt_folder, episode)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news_list__item',
                                    date_select='.news_date', title_select='.news_title', id_select='a',
                                    a_tag_prefix=news_url, a_tag_start_text_to_remove='./',
                                    date_func=lambda x: x[6:10] + '.' + x[0:5], next_page_select='.btn_next',
                                    next_page_eval_index=-1, next_page_eval_index_class='none')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        # self.image_list = []
        # self.add_to_image_list('teaser', self.PAGE_PREFIX + 'assets/img/img_main.jpg')
        # self.add_to_image_list('teaser_tw', 'https://pbs.twimg.com/media/EvylQFOVkAID_0B?format=jpg&name=medium')
        # self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/FdRkMFnaMAImkFJ?format=jpg&name=large')
        # self.add_to_image_list('kv1', self.PAGE_PREFIX + 'assets/img/img_main_fix.jpg')
        # self.add_to_image_list('kv2_tw', 'https://pbs.twimg.com/media/FsCeMyIaQAI_Vkk?format=jpg&name=4096x4096')
        # self.download_image_list(folder)
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.main_image .img_fixed img[src]')
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
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.chara_image img[src], .chara_face img[src]')
            for image in images:
                if '/character/' not in image['src']:
                    continue
                image_url = self.PAGE_PREFIX + image['src']
                image_name = self.generate_image_name_from_url(image_url, 'character')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        bd_url = self.PAGE_PREFIX + 'bddvd/'
        try:
            soup = self.get_soup(bd_url)
            tabs = soup.select('.page_tab__item')
            page_names = []
            pages = []
            current_page_name = None
            for tab in tabs:
                atag = tab.select('a[href]')
                if len(atag) > 0 and '/?page=' in atag[0]['href']:
                    page_name = atag[0]['href'].split('=')[-1]
                    if 'is_current' in tab['class']:
                        current_page_name = page_name
                    if page_name.isnumeric() and page_name not in processed:
                        page_names.append(page_name)
                    else:  # Process Blu-ray Bonus page first
                        pages.append(page_name)
            for name in page_names:
                pages.append(name)
            for page in pages:
                if current_page_name == page:
                    bd_soup = soup
                else:
                    bd_soup = self.get_soup(bd_url + '?page=' + page)
                    if bd_soup is None:
                        continue
                images = bd_soup.select('.image_jk img[src],.novelty_wrapper img[src]')
                self.image_list = []
                for image in images:
                    if image['src'].startswith('../'):
                        image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                    elif image['src'].startswith('/'):
                        image_url = self.PAGE_PREFIX + image['src'][1:].split('?')[0]
                    else:
                        image_url = image['src'].split('?')[0]
                    if 'img_np' in image_url or 'jk_np' in image_url or '/bddvd/' not in image_url:
                        continue
                    image_name = self.generate_image_name_from_url(image_url, 'bddvd')
                    self.add_to_image_list(image_name, image_url)
                if page.isnumeric():
                    if len(self.image_list) > 0:
                        processed.append(page)
                    else:
                        break
                self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, f'Blu-ray')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Mononogatari
class MononogatariDownload(Winter2023AnimeDownload):
    title = 'Mononogatari'
    keywords = [title, 'Malevolent Spirits']
    website = 'https://mononogatari-pr.com/'
    twitter = 'mononogatari_pr'
    hashtags = ['もののがたり', 'mononogatari']
    folder_name = 'mononogatari'

    PAGE_PREFIX = website
    FINAL_EPISODE = 24

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_media()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/', decode=True)
            stories = soup.select('.Story_panel')
            for story in stories:
                try:
                    ep_num = int(story.select('h3 span')[0].text.replace('#', ''))
                    if ep_num is None or ep_num < 1:
                        continue
                    episode = str(ep_num).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                images = story.select('.storyThum img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = self.PAGE_PREFIX + images[i]['src'].replace('../', '')
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            response = self.get_response(self.PAGE_PREFIX, decode=True)
            index = response.find('//配列を宣言')
            if index == -1:
                return
            end_index = response[index:].find('];')
            if end_index == -1:
                return
            arr = response[index + 7:][0:end_index].split('},')
            for i in range(len(arr)):
                try:
                    content = arr[i].split('{')[1].split('}')[0]
                    cont_split = content.split(',')
                    year = month = day = title = None
                    for cont in cont_split:
                        subcontent = cont.strip()
                        if subcontent.startswith("'y':'"):
                            year = subcontent[5:9]
                        elif subcontent.startswith("'m':"):
                            month = subcontent[5:7]
                        elif subcontent.startswith("'d':"):
                            day = subcontent[5:7]
                        elif subcontent.startswith("'txt':'"):
                            last_index = subcontent.rfind("'")
                            if last_index != -1:
                                title = subcontent[7:last_index]
                    if year is None or month is None or day is None or title is None:
                        continue
                    date = year + '.' + month + '.' + day
                    title = ' '.join(title.split())
                    if news_obj and (title == news_obj['title'] or date < news_obj['date']):
                        break
                    results.append(self.create_news_log_object(date, title, ''))
                except:
                    continue
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
        self.add_to_image_list('kv_aniverse', 'https://aniverse-mag.com/wp-content/uploads/2022/12/sub5-2.jpg')
        self.download_image_list(folder)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'blu-ray/')
            self.image_list = []
            images = soup.select('#Blu-ray img[src]')
            for image in images:
                if '/blu-ray/' not in image['src']:
                    continue
                image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                image_name = self.generate_image_name_from_url(image_url, 'blu-ray')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')
            

# NieR:Automata Ver1.1a
class NierAutomataDownload(Winter2023AnimeDownload, NewsTemplate):
    title = 'NieR:Automata Ver1.1a'
    keywords = [title]
    website = 'https://nierautomata-anime.com/'
    twitter = 'NieR_A_ANIME'
    hashtags = ['ニーア', 'NieR', 'ニーアオートマタ']
    folder_name = 'nier'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        story_url = self.PAGE_PREFIX + 'story/'
        try:
            soup = self.get_soup(story_url, decode=True)
            stories = soup.select('.p-story_nav__list-item')
            for story in stories:
                a_tags = story.select('a[href]')
                if len(a_tags) < 1:
                    continue
                try:
                    ep_num_tag = a_tags[0].select('.p-story_nav__link-text')
                    ep_num = int(ep_num_tag[0].text)
                    if ep_num is None or ep_num < 1:
                        continue
                    episode = str(ep_num).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if story.has_attr('class') and 'is-current' in story['class']:
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(story_url + a_tags[0]['href'].replace('./', ''))
                if ep_soup is not None:
                    images = ep_soup.select('.p-story_visual__data-img img[src]')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = story_url + images[i]['src']
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.p-news__list-item',
                                    date_select='.p-news_data__date', title_select='.p-news_data__title',
                                    id_select='.p-news_data', a_tag_prefix=self.PAGE_PREFIX, paging_type=1,
                                    a_tag_start_text_to_remove='/', next_page_select='.c-pagination__list-item',
                                    next_page_eval_index_class='is-current', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.p-kv_slide__all img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'][1:]
                if '/kv/' not in image_url:
                    continue
                image_name = self.generate_image_name_from_url(image_url, 'kv')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')


# Ningen Fushin no Boukensha-tachi ga Sekai wo Sukuu you desu
class NingenFushinDownload(Winter2023AnimeDownload, NewsTemplate):
    title = 'Ningen Fushin no Boukensha-tachi ga Sekai wo Sukuu you desu'
    keywords = [title, 'Apparently, Disillusioned Adventurers Will Save the World']
    website = 'https://www.ningenfushin-anime.jp/'
    twitter = 'ningenfushinPR'
    hashtags = '人間不信'
    folder_name = 'ningenfushin'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'wp-content/themes/ningenfushin/dist/img/story/ep%s/img%s.jpg'
        for i in range(self.FINAL_EPISODE):
            ep_num = str(i + 1)
            episode = ep_num.zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            is_success = False
            for j in range(self.IMAGES_PER_EPISODE):
                image_url = template % (ep_num, str(j + 1))
                if self.is_not_matching_content_length(image_url, 447760):
                    image_name = episode + '_' + str(j + 1)
                    self.download_image(image_url, self.base_folder + '/' + image_name)
                    is_success = True
            if not is_success:
                return

    def download_episode_preview_external(self):
        keywords = ['人間不信の冒険者たちが世界を救うようです']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20230106', download_id=self.download_id).run()

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.c-News__articleLink',
                                    date_select='.c-date-line', title_select='.c-text-hover', id_select=None,
                                    date_func=lambda x: '2022.' + x[0:2] + '.' + x[3:])

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'wp-content/themes/ningenfushin/dist/img/top/kv.png')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FextUiWaEAEBfcR?format=jpg&name=4096x4096')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/Fi4XvsPaEAEKl4i?format=jpg&name=4096x4096')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'wp-content/themes/ningenfushin/dist/img/character/body_char_'
        self.download_by_template(folder, [prefix + '%s.png', prefix + '%s_on.png'], 1, 1)

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        bd_prefix = self.PAGE_PREFIX + 'products/'
        for page in ['bd3', 'bd', 'bd2']:
            try:
                if page != 'bd3' and page in processed:
                    continue
                bd_url = bd_prefix + page
                soup = self.get_soup(bd_url)
                images = soup.select('.p-Products__column img[src]')
                self.image_list = []
                for image in images:
                    image_url = image['src']
                    image_name = self.extract_image_name_from_url(image_url)
                    if image_name == 'now_printing':
                        continue
                    self.add_to_image_list(image_name, image_url)
                if page != 'bd3':
                    if len(self.image_list) == 0:
                        break
                    else:
                        processed.append(page)
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Oniichan wa Oshimai!
class OnimaiDownload(Winter2023AnimeDownload, NewsTemplate):
    title = 'Oniichan wa Oshimai!'
    keywords = [title, 'Onimai']
    website = 'https://onimai.jp/'
    twitter = 'onimai_anime'
    hashtags = 'おにまい'
    folder_name = 'onimai'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'episode/img/%s_%s.jpg'
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_09'):
                continue
            ep_template = template % (episode, '%s')
            if self.is_valid_url(ep_template % '09', is_image=True):
                old_folder = self.base_folder + '/old'
                if not os.path.exists(old_folder):
                    os.makedirs(old_folder)
                for j in range(8):
                    image_name = episode + '_' + str(j + 1).zfill(2) + '.jpg'
                    try:
                        os.rename(self.base_folder + '/' + image_name, old_folder + '/' + image_name)
                    except:
                        pass
            elif self.is_image_exists(episode + '_01'):
                continue
            stop = False
            is_successful = False
            for j in range(20):
                image_url = ep_template % str(j + 1).zfill(2)
                image_name = episode + '_' + str(j + 1).zfill(2)
                result = self.download_image(image_url, self.base_folder + '/' + image_name)
                if result == -1:
                    if not is_successful:
                        stop = True
                    break
                is_successful = True
            if stop:
                break

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.newsList',
                                    date_select='.newsList__date', title_select='.newsList__title', id_select='a',
                                    a_tag_prefix=self.PAGE_PREFIX + 'news/', a_tag_start_text_to_remove='./')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('top_visual_mahiro', self.PAGE_PREFIX + 'assets/img/top/visual_mahiro.png')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FQ6O8FgVIAEp7rm?format=jpg&name=4096x4096')
        self.add_to_image_list('kv_tw', 'https://pbs.twimg.com/media/FjLP6ngagAA3zrm?format=jpg&name=4096x4096')
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

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        bd_prefix = self.PAGE_PREFIX + 'bdbox/'
        for page in ['tokuten', 'vol1', 'vol2']:
            try:
                if page != 'tokuten' and page in processed:
                    continue
                page_url = bd_prefix + page + '.html'
                soup = self.get_soup(page_url)
                images = soup.select('.bdboxContent img[src]')
                self.image_list = []
                for image in images:
                    image_url = bd_prefix + image['src']
                    if '/img/' in image_url:
                        image_name = self.generate_image_name_from_url(image_url, 'img')
                    else:
                        image_name = self.extract_image_name_from_url(image_url)
                    if self.is_image_exists(image_name, folder):
                        continue
                    if not self.is_content_length_in_range(image_url, more_than_amount=10000):
                        continue
                    self.add_to_image_list(image_name, image_url)
                if (page != 'vol1' and page != 'privilege' and len(self.image_list) > 0) \
                        or (page == 'vol1' and len(self.image_list) > 1):
                    processed.append(page)
                if page.startswith('vol') and len(self.image_list) == 0:
                    break
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Ooyukiumi no Kaina
class OoyukiumiDownload(Winter2023AnimeDownload, NewsTemplate):
    title = 'Ooyukiumi no Kaina'
    keywords = [title, 'Kaina of the Great Snow Sea']
    website = 'https://ooyukiumi.net/'
    twitter = 'ooyukiumi_kaina'
    hashtags = '大雪海のカイナ'
    folder_name = 'ooyukiumi'

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
        story_url = self.PAGE_PREFIX + 'episodes/'
        try:
            soup = self.get_soup(story_url)
            stories = soup.select('.episodes__list a[href]')
            for story in stories:
                et_num = story.select('.et--num')
                if len(et_num) == 0:
                    continue
                try:
                    episode = str(int(et_num[0].text.replace('第', '').replace('話', ''))).zfill(2)
                except:
                    continue
                ep_soup = self.get_soup(story_url + story['href'].replace('./', ''))
                if ep_soup is None:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                images = ep_soup.select('.episode__imgList img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = story_url + images[i]['src'].replace('./', '')
                    image_name = f'{episode}_{i + 1}'
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.article__list',
                                    title_select='.article__listtitle', date_select='.article__listtime',
                                    id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv', self.PAGE_PREFIX + 'assets/img/top/kv.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/img/character/character%s_main.jpg'
        self.download_by_template(folder, template, 1, 1)

    def download_media(self):
        folder = self.create_media_directory()
        bd_url = self.PAGE_PREFIX + 'bdbox/'
        try:
            soup = self.get_soup(bd_url)
            images = soup.select('#bdCont img[src]')
            self.image_list = []
            for image in images:
                if not image['src'].endswith('nowprinting.png'):
                    image_url = bd_url + image['src'][2:].split('?')[0]
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Otonari no Tenshi-sama ni Itsunomanika Dame Ningen ni Sareteita Ken
class OtonarinoTenshisamaDownload(Winter2023AnimeDownload, NewsTemplate):
    title = 'Otonari no Tenshi-sama ni Itsunomanika Dame Ningen ni Sareteita Ken'
    keywords = [title, 'The Angel Next Door Spoils Me Rotten']
    website = 'https://otonarino-tenshisama.jp/'
    twitter = 'tenshisama_PR'
    hashtags = 'お隣の天使様'
    folder_name = 'otonarino-tenshisama'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 4

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_guess()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        yt_folder, yt_episodes = self.init_youtube_thumbnail_variables(['01'])
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            sections = soup.select('.story__episode section.episode[id]')
            for section in sections:
                try:
                    ep_num = section.select('.episode__number')[0].text.replace('第', '').replace('話', '')
                    episode = str(int(ep_num)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1') and episode in yt_episodes:
                    continue
                images = section.select('img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)

                # YouTube thumbnail
                yt_tag = section.select('.youtube-embed iframe[src]')
                if len(yt_tag) > 0:
                    yt_id = yt_tag[0]['src'].split('?')[0].split('/')[-1]
                    self.download_youtube_thumbnail_by_id(yt_id, yt_folder, episode)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wordpress/wp-content/uploads/%s/%s/%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1') or self.is_image_exists(episode + '_1', folder):
                continue
            stop = False
            for j in range(self.IMAGES_PER_EPISODE):
                img_name = 'story-episode' + str(i + 1) + '-cut' + str(j + 1)
                image_url = template % (year, month, img_name)
                image_name = episode + '_' + str(j + 1)
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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.allNews__item',
                                    title_select='.allNews__title', date_select='.allNews__date',
                                    id_select='a', next_page_select='a.next.page-numbers')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        theme_prefix = self.PAGE_PREFIX + 'wordpress/wp-content/themes/otonari/images/'
        upload_prefix = self.PAGE_PREFIX + 'wordpress/wp-content/uploads/'
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FIQhzRlagAAxK-X?format=jpg&name=large')
        self.add_to_image_list('tz', theme_prefix + 'mainvisual.jpg')
        self.add_to_image_list('tz2_tw', 'https://pbs.twimg.com/media/FOtPcAMVkAcoYzY?format=jpg&name=4096x4096')
        self.add_to_image_list('aprilfool_0331_A', upload_prefix + '2022/03/aprilfool_0331_A.jpg')
        self.add_to_image_list('aprilfool_all', upload_prefix + '2022/03/aprilfool_all.jpg')
        self.add_to_image_list('tz3', theme_prefix + 'mainvisual-v2.jpg')
        self.add_to_image_list('tz3_pc', theme_prefix + '/mainvisual-v2_pc.jpg')
        self.add_to_image_list('tz3_news', upload_prefix + '2022/05/tenshisama_teser3_title.jpg')
        self.add_to_image_list('mainvisual-v3_pc', theme_prefix + 'mainvisual-v3_pc.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wordpress/wp-content/themes/otonari/images/character-%s.png'
        self.download_by_template(folder, template, 1, prefix='tz_')

    def download_media(self):
        folder = self.create_media_directory()

        # Blu-ray
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        bd_prefix = self.PAGE_PREFIX + 'bddvd/'
        for page in ['spacial', 'vol1', 'vol2', 'vol3', 'vol4']:
            try:
                if page.startswith('vol') and page in processed:
                    continue
                bd_url = bd_prefix + page + '/'
                soup = self.get_soup(bd_url)
                images = soup.select('.page-bddvd img[src]')
                self.image_list = []
                for image in images:
                    image_url = image['src']
                    image_name = self.extract_image_name_from_url(image_url)
                    if 'comming' in image_url:
                        continue
                    if self.is_image_exists(image_name, folder):
                        continue
                    self.add_to_image_list(image_name, image_url)
                if page.startswith('vol'):
                    if len(self.image_list) == 0:
                        break
                    else:
                        processed.append(page)
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)

        # self.add_to_image_list('valentine_tw', 'https://pbs.twimg.com/media/FLfDFR8aQAIWt1u?format=jpg&name=large')
        self.add_to_image_list('valentine_chara', 'https://aniverse-mag.com/wp-content/uploads/2022/02/8e5cda5d29024d4bf78d1e9452225fb6-e1644755501739.png')
        self.add_to_image_list('valentine_pos', self.PAGE_PREFIX + 'wordpress/wp-content/uploads/2022/02/valentine_pos.jpg')
        self.add_to_image_list('valentine', self.PAGE_PREFIX + 'wordpress/wp-content/uploads/2022/02/valentine_sp-kabegami.jpg')
        self.download_image_list(folder)

        # Special
        special_folder = folder + '/special'
        if not os.path.exists(special_folder):
            os.makedirs(special_folder)
        special_cache_filepath = special_folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(special_cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'special/')
            a_tags = soup.select('li.card a[href]')
            for a_tag in reversed(a_tags):
                href = a_tag['href']
                if '/special/' not in href:
                    continue
                if href.endswith('/'):
                    href = href[:-1]
                page_name = href.split('/')[-1]
                if page_name in processed:
                    continue
                page_soup = self.get_soup(a_tag['href'])
                if page_soup is not None:
                    images = page_soup.select('article img[src]')
                    self.image_list = []
                    for image in images:
                        image_url = self.clear_resize_in_url(image['src'])
                        image_name = self.extract_image_name_from_url(image_url)
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(special_folder)
                processed.append(page_name)
        except Exception as e:
            self.print_exception(e, 'Special')
        self.create_cache_file(special_cache_filepath, processed, num_processed)

        # With You
        withyou_prefix = self.PAGE_PREFIX + 'withyou/'
        withyou_page = withyou_prefix + 'prefectures/prefectures.html'
        withyou_folder = folder + '/withyou'
        if not os.path.exists(withyou_folder):
            os.makedirs(withyou_folder)
        try:
            soup = self.get_soup(withyou_page)
            images = soup.select('.slide-items .slide-img img[src]')
            self.image_list = []
            for image in images:
                image_url = withyou_prefix + image['src'].replace('../', '')
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
                self.add_to_image_list('2' + image_name, image_url.replace(image_name, '2' + image_name))
            self.download_image_list(withyou_folder)
        except Exception as e:
            self.print_exception(e, 'With You')

    def download_media_withyou_guess(self):
        folder = self.create_media_directory()
        withyou_folder = folder + '/withyou'
        if not os.path.exists(withyou_folder):
            os.makedirs(withyou_folder)
        areas = [
            {
                'name': 'hokkaido-tohoku',
                'prefectures': ['hokkaido', 'aomori', 'iwate', 'miyagi', 'akita', 'yamagata', 'fukushima']
            },
            {
                'name': 'kanto',
                'prefectures': ['ibaraki', 'tochigi', 'gunma', 'saitama', 'chiba', 'tokyo', 'kanagawa']
            },
            {
                'name': 'chubu',
                'prefectures': ['niigata', 'toyama', 'ishikawa', 'fukui', 'yamanashi', 'nagano', 'gifu', 'shizuoka', 'aichi']
            },
            {
                'name': 'kinki',
                'prefectures': ['mie', 'shiga', 'kyoto', 'osaka', 'hyogo', 'nara', 'wakayama']
            },
            {
                'name': 'chugoku',
                'prefectures': ['tottori', 'shimane', 'okayama', 'hiroshima', 'yamaguchi']
            },
            {
                'name': 'shikoku',
                'prefectures': ['tokushima', 'kagawa', 'ehime', 'kochi']
            },
            {
                'name': 'kyushu-okinawa',
                'prefectures': ['fukuoka', 'saga', 'nagasaki', 'kumamoto', 'oita', 'miyazaki', 'kagoshima', 'okinawa']
            }
        ]
        current_files = os.listdir(withyou_folder)
        count = 0
        template = self.PAGE_PREFIX + 'withyou/assets/img/common/kv/%s/%s.jpg'
        success_download = 0
        for area in areas:
            first_num = count + 1
            last_num = count + len(area['prefectures'])
            count += len(area['prefectures'])
            is_successful = False
            prefectures = area['prefectures']
            for i in range(first_num, last_num + 1, 1):
                number = str(i).zfill(2)
                file_exist = False
                for file in current_files:
                    if file.startswith(f'2w{number}') or file.startswith(f'w{number}'):
                        file_exist = True
                        break
                if file_exist:
                    is_successful = True
                    continue
                prefecture_to_remove = None
                for prefecture in prefectures:
                    image_name = f'w{number}_{prefecture}'
                    image_url = template % (area['name'], image_name)
                    result = self.download_image(image_url, withyou_folder + '/' + image_name)
                    if result == -1:
                        print('FAILED - ' + image_url)
                        continue
                    is_successful = True
                    success_download += 1
                    image_name = f'2w{number}_{prefecture}'
                    image_url = template % (area, image_name)
                    self.download_image(image_url, withyou_folder + '/' + image_name)
                    prefecture_to_remove = prefecture
                    break
                if prefecture_to_remove is not None:
                    prefectures.remove(prefecture_to_remove)
            if not is_successful:
                break
        return -1 if success_download == 0 else 0


# Rougo ni Sonaete Isekai de 8-manmai no Kinka wo Tamemasu
class Roukin8Download(Winter2023AnimeDownload, NewsTemplate):
    title = 'Rougo ni Sonaete Isekai de 8-manmai no Kinka wo Tamemasu'
    keywords = [title, 'roukin8', 'Saving 80,000 Gold in Another World for My Retirement']
    website = 'https://roukin8-anime.com/'
    twitter = 'roukin8_anime'
    hashtags = ['roukin8', 'ろうきん8']
    folder_name = 'roukin8'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 4

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'dist/assets/img/story/ep%s/img%s.'
        template1 = template + 'png'
        template2 = template + 'jpg'
        try:
            for i in range(1, self.FINAL_EPISODE + 1, 1):
                episode = str(i).zfill(2)
                if self.is_image_exists(episode + '_1'):
                    continue
                for j in range(1, self.IMAGES_PER_EPISODE + 1, 1):
                    image_url = template1 % (str(i), str(j))
                    image_name = episode + '_' + str(j)
                    result = self.download_image(image_url, self.base_folder + '/' + image_name)
                    if result == -1:
                        image_url = template2 % (str(i), str(j))
                        result = self.download_image(image_url, self.base_folder + '/' + image_name)
                        if result == -1:
                            return
        except Exception as e:
            self.print_exception(e, 'Episode Preview')

    def download_episode_preview_external(self):
        keywords = ['⽼後に備えて異世界で8万枚の⾦貨を貯めます']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20221226', download_id=self.download_id).run()

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.bl_vertPosts_item',
                                    date_select='time', title_select='.bl_vertPosts_txt',
                                    id_select='.bl_vertPosts_link', a_tag_prefix=self.PAGE_PREFIX,
                                    a_tag_start_text_to_remove='../')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('top_kv', self.PAGE_PREFIX + 'dist/assets/img/top/kv.jpg')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FZkU-3hagAAU3fg?format=jpg&name=medium')
        self.add_to_image_list('kv', self.PAGE_PREFIX + 'dist/assets/img/news/news07/img01.jpeg')
        self.add_to_image_list('kv_tw', 'https://pbs.twimg.com/media/FiV4ujAakAAeWZZ?format=jpg&name=4096x4096')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'dist/assets/img/top/'
        for i in range(1, 21, 1):
            image_name = 'char_body'
            if i > 1:
                image_name += str(i)
            if self.is_image_exists(image_name, folder):
                continue
            image_url = prefix + image_name + '.png'
            result = self.download_image(image_url, folder + '/' + image_name)
            if result == -1:
                break

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.bdbox_imgitem img[src], .tp_bdshop_img img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('./', '')
                image_name = self.extract_image_name_from_url(image_url)
                if 'bd_shop' in image_name:
                    continue
                if 'bd_box' == image_name:
                    if self.is_image_exists('bd_box', folder)\
                            or not self.is_content_length_in_range(image_url, more_than_amount=8000):
                        continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Saikyou Onmyouji no Isekai Tenseiki
class SaikyoOnmyoujiDownload(Winter2023AnimeDownload, NewsTemplate):
    title = 'Saikyou Onmyouji no Isekai Tenseiki'
    keywords = [title]
    website = 'https://saikyo-onmyouji.asmik-ace.co.jp/'
    twitter = 'saikyo_onmyouji'
    hashtags = '最強陰陽師'
    folder_name = 'saikyo-onmyouji'

    PAGE_PREFIX = website
    FINAL_EPISODE = 13
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_episode_preview_guess()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/', decode=True)
            li_tags = soup.select('ul[data-type="archive"] li')
            for li in li_tags:
                a_tag = li.find('a')
                if a_tag is not None:
                    try:
                        episode = str(int(a_tag.text)).zfill(2)
                    except:
                        continue
                else:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if li.has_attr('class') and 'is_current' in li['class']:
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(a_tag['href'])
                if ep_soup is not None and episode is not None:
                    images = ep_soup.select('.ssslider img[src]')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = images[i]['src']
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        keywords = ['最強陰陽師の異世界転生記']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20230105', download_id=self.download_id).run()

    def download_episode_preview_guess(self):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_1'):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wp/wp-content/uploads/%s/%s/%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        curr_month = current_date.strftime('%m')
        is_successful = False
        for year in ['2022', '2023']:
            months = []
            if year == '2022':
                months.append('12')
            else:
                k = 0
                while k <= 12:
                    k += 1
                    months.append(str(k).zfill(2))
                    if curr_month == str(k).zfill(2):
                        break
            for month in reversed(months):
                sub_folder = f'{folder}/{year}/{month}'
                if not os.path.exists(sub_folder):
                    os.makedirs(sub_folder)
                for i in range(1, self.IMAGES_PER_EPISODE + 1, 1):
                    j = -1
                    while j < 20:
                        j += 1
                        image_name = f'{i}-{j}'
                        if self.is_image_exists(image_name, sub_folder):
                            continue
                        if j == 0:
                            img_name = str(i).zfill(2)
                        else:
                            img_name = str(i).zfill(2) + '-' + str(j)
                        image_url = template % (year, month, img_name)
                        result = self.download_image(image_url, sub_folder + '/' + image_name)
                        if result == -1:
                            break
                        is_successful = True
                    if not is_successful:
                        break
                if len(os.listdir(sub_folder)) == 0:
                    break
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news--lineup li',
                                    date_select='.date', title_select='.ttl', id_select='a',
                                    paging_type=0, next_page_select='ul.pagenation-list li', next_page_eval_index=-1,
                                    next_page_eval_index_class='is__current')

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

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'bd/')
            images = soup.select('#Main img[src]')
            self.image_list = []
            for image in images:
                if image['src'].endswith('.svg'):
                    continue
                image_url = image['src']
                image_name = self.extract_image_name_from_url(image_url)
                if image_name.startswith('np_'):
                    continue
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Shin Shinka no Mi: Shiranai Uchi ni Kachigumi Jinsei
class Shinkanomi2Download(Winter2023AnimeDownload, NewsTemplate):
    title = 'Shin Shinka no Mi: Shiranai Uchi ni Kachigumi Jinsei'
    keywords = [title, 'Shinkanomi', '2nd']
    website = 'https://shinkanomi-anime.com/'
    twitter = 'shinkanomianime'
    hashtags = ['進化の実', '勝ち組人生', 'ゴリラ系女子']
    folder_name = 'shinkanomi2'

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
            ep_nums = soup.select('.jsEpisodeNum .episodeNumItem')
            ep_list = soup.select('.jsEpisodeList .episodeListItem')
            if len(ep_nums) == len(ep_list):
                for index in range(len(ep_nums)):
                    try:
                        episode = str(int(ep_nums[index].text.strip()[1:3])).zfill(2)
                    except:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    images = ep_list[index].select('img[src]')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = images[i]['src']
                        image_name = f'{episode}_{i + 1}'
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
            else:
                raise Exception("Expected ep_num == ep_list")
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsArchive .block',
                                    date_select='.date', title_select='h2', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv_tw', 'https://pbs.twimg.com/media/FdY2SacakAECMAq?format=jpg&name=medium')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.kv .bg img[src]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'][1:].split('?')[0]
                image_name = self.generate_image_name_from_url(image_url, 'img')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            p_tags = soup.select('.general p.img')
            self.image_list = []
            for p_tag in p_tags:
                if 'sp' in p_tag['class']:
                    continue
                image = p_tag.find('img')
                if image is not None:
                    if not image.has_attr('src') or (image.has_attr('class') and 'sp' in image['class']):
                        continue
                    image_url = self.PAGE_PREFIX + image['src'][1:]
                    image_name = self.generate_image_name_from_url(image_url, 'character')
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'blu-ray/')
            images = soup.select('.mainContent img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'][1:]
                if self.is_content_length_in_range(image_url, more_than_amount=32100):
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


# Spy Kyoushitsu
class SpyroomDownload(Winter2023AnimeDownload, NewsTemplate2):
    title = "Spy Kyoushitsu"
    keywords = [title, "Spy Classroom", "Spyroom"]
    website = 'https://spyroom-anime.com/'
    twitter = 'spyroom_anime'
    hashtags = ['スパイ教室', 'spyroom', 'SpyClassroom']
    folder_name = 'spyroom'

    PAGE_PREFIX = website
    FINAL_EPISODE = 24
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_episode_preview_guess()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/01.html')
            trs = soup.select('#ContentsListUnit01 tr[class]')
            for tr in trs:
                a_tags = tr.select('a[href]')
                if len(a_tags) == 0:
                    continue
                try:
                    episode = str(int(a_tags[0].text.replace('#', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if episode == '01':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(self.PAGE_PREFIX + a_tags[0]['href'].replace('../', ''))
                if ep_soup is None:
                    continue
                self.image_list = []
                images = ep_soup.select('ul.tp5 img[src]')
                for i in range(len(images)):
                    image_url = self.PAGE_PREFIX + images[i]['src'].split('?')[0].replace('../', '').replace('sn_', '')
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        keywords = ['スパイ教室', 'カット']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20230104', prefix='#', suffix='', download_id=self.download_id).run()

    def download_episode_preview_guess(self):
        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'core_sys/images/contents/%s/block/%s/%s.jpg'
        is_successful = False
        for i in range(self.FINAL_EPISODE):
            episode = str(i + 1).zfill(2)
            if self.is_image_exists(episode + '_1') or self.is_image_exists(episode + '_1', folder):
                continue
            is_success = False
            first = 20 + i
            second = 46 + 4 * i
            if i > 3:
                second += 1
            third = 62 + self.IMAGES_PER_EPISODE * i
            for j in range(self.IMAGES_PER_EPISODE):
                image_url = template % (str(first).zfill(8), str(second).zfill(8), str(third + j).zfill(8))
                if not self.is_content_length_in_range(image_url, more_than_amount=16000):
                    break
                image_name = episode + '_' + str(j + 1)
                result = self.download_image(image_url, folder + '/' + image_name)
                if result == 0:
                    is_success = True
                    is_successful = True
                elif result == -1:
                    break
            if is_success:
                print(self.__class__.__name__ + ' - Guessed successfully!')
            else:
                if len(os.listdir(folder)) == 0:
                    os.rmdir(folder)
                return
        if len(os.listdir(folder)) == 0:
            os.rmdir(folder)
        return is_successful

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_kv_chara', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv_chara.png')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FNuvFFSaAAkbDy3?format=jpg&name=4096x4096')
        self.add_to_image_list('home_kv', self.PAGE_PREFIX + 'core_sys/images/main/home/kv.png')
        self.add_to_image_list('tz_kv', self.PAGE_PREFIX + 'core_sys/images/news/00000015/block/00000031/00000005.jpg')
        self.download_image_list(folder)

        sub_folder = self.create_custom_directory(folder.split('/')[-1] + '/news')
        cache_filepath = sub_folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'news/')
            while True:
                stop = False
                items = soup.select('#list_01 a[href]')
                for item in items:
                    if not item['href'].startswith('../') or '/news/' not in item['href']\
                            or not item['href'].endswith('.html'):
                        continue
                    page_name = item['href'].split('/')[-1].split('.html')[0]
                    if page_name in processed:
                        stop = True
                        break
                    title = item.text.strip()
                    if 'ビジュアル' in title:
                        news_soup = self.get_soup(self.PAGE_PREFIX + item['href'].replace('../', ''))
                        if news_soup is not None:
                            images = news_soup.select('#news_block img[src]')
                            self.image_list = []
                            for image in images:
                                image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                                if '/news/' not in image_url:
                                    continue
                                image_name = self.generate_image_name_from_url(image_url, 'news')\
                                    .replace('_block_', '_')
                                self.add_to_image_list(image_name, image_url)
                            self.download_image_list(sub_folder)
                    processed.append(page_name)
                if stop:
                    break
                next_page = soup.select('.nb_nex a[href]')
                if len(next_page) == 0:
                    break
                soup = self.get_soup(self.PAGE_PREFIX + next_page[0]['href'].replace('../', ''))
        except Exception as e:
            self.print_exception(e, 'Key Visual News')
        self.create_cache_file(cache_filepath, processed, num_processed)

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'chara/lily.html')
            a_tags = soup.select('#ContentsListUnit02 a[href]')
            for a_tag in a_tags:
                chara_url = self.PAGE_PREFIX + a_tag['href'].replace('../', '')
                chara_name = chara_url.split('/')[-1].replace('.html', '')
                if chara_name in processed:
                    continue
                if chara_name == 'lily':
                    chara_soup = soup
                else:
                    chara_soup = self.get_soup(chara_url)
                if chara_soup is not None:
                    images = chara_soup.select('.chara__img img[src]')
                    for image in images:
                        image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                        image_name = self.extract_image_name_from_url(image_url)
                        self.add_to_image_list(image_name, image_url)
                    if len(self.image_list) > 0:
                        processed.append(chara_name)
                    self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        privilege_names = ['amazon', 'animate', 'gamers', 'kadokawa', 'sofmap', 'rakuten']
        for i in range(len(privilege_names)):
            privilege_names[i] = '2nd_' + privilege_names[i]
        for page in ['privilege2', 'campaign2', 'privilege', 'campaign', '01', '02', '03', '04']:
            try:
                if page != 'privilege2' and page in processed:
                    continue
                page_url = self.PAGE_PREFIX + 'bd/'
                if page != '01':
                    page_url += page + '.html'
                soup = self.get_soup(page_url)
                images = soup.select('.block_inner img[src]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                    if '/bddvd/' in image_url:
                        image_name = self.generate_image_name_from_url(image_url, 'bddvd')
                    else:
                        image_name = self.extract_image_name_from_url(image_url)
                    if self.is_image_exists(image_name, folder):
                        if page.startswith('privilege') and image_name in privilege_names:
                            self.download_image_with_different_length(image_url, image_name, 'old', folder)
                        else:
                            continue
                    if not self.is_content_length_in_range(image_url, more_than_amount=88800):
                        continue
                    self.add_to_image_list(image_name, image_url)
                if page in ['privilege', 'campaign', '01', '02']:
                    processed.append(page)
                else:
                    if (page != '03' and page != 'privilege2' and len(self.image_list) > 0)\
                            or (page == '03' and len(self.image_list) > 1):
                        processed.append(page)
                    if page.isnumeric():
                        if len(self.image_list) == 0:
                            break
                        else:
                            processed.append(page)
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Sugar Apple Fairy Tale
class SugarAppleDownload(Winter2023AnimeDownload, NewsTemplate):
    title = 'Sugar Apple Fairy Tale'
    keywords = [title]
    website = 'https://sugarapple-anime.com/'
    twitter = 'sugarapple_PR'
    hashtags = '砂糖林檎'
    folder_name = 'sugarapple'

    PAGE_PREFIX = website
    FINAL_EPISODE = 24
    IMAGES_PER_EPISODE = 6

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'story/img/ep%s_img%s.jpg'
        try:
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_1'):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1)
                    result = self.download_image(image_url, self.base_folder + '/' + image_name)
                    if result == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_external(self):
        keywords = ['シュガーアップル・フェアリーテイル']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20221225', download_id=self.download_id).run()

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newslist_contents li',
                                    date_select='.date', title_select='a', id_select='a',
                                    date_func=lambda x: x[0:4] + '.' + x[4:6] + '.' + x[7:9],
                                    a_tag_prefix=self.PAGE_PREFIX + 'news/')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FgJTYu-aUAEF8u_?format=jpg&name=large')
        self.add_to_image_list('kv_tw', 'https://pbs.twimg.com/media/Fh0EdYWUAAAScuD?format=jpg&name=large')
        self.add_to_image_list('main_img02_pc', self.PAGE_PREFIX + 'img/main_img02_pc.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'img/chara/body_%s.png'
        self.download_by_template(folder, template, 2, 1)

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['', 'season1']:
            try:
                page_url = self.PAGE_PREFIX + 'bluray/'
                if len(page) > 0:
                    if page in processed:
                        continue
                    page_url += page + '.html'
                soup = self.get_soup(page_url)
                images = soup.select('.page_wrapper img[src]')
                self.image_list = []
                for image in images:
                    if '/bluray/' not in image['src'] or image['src'].endswith('img_cs_02.jpg'):
                        continue
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                    image_name = self.generate_image_name_from_url(image_url, 'bluray')
                    self.add_to_image_list(image_name, image_url)
                if len(page) > 0 and len(self.image_list) > 0:
                    processed.append(page)
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Tensei Oujo to Tensai Reijou no Mahou Kakumei
class TentenKakumeiDownload(Winter2023AnimeDownload, NewsTemplate):
    title = 'Tensei Oujo to Tensai Reijou no Mahou Kakumei'
    keywords = [title, 'tenten kakumei', 'The Magical Revolution of the Reincarnated Princess and the Genius Young Lady']
    website = 'https://tenten-kakumei.com/'
    twitter = 'tenten_kakumei'
    hashtags = '転天アニメ'
    folder_name = 'tenten-kakumei'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_news()
        self.download_key_visual()
        self.download_character()
        self.download_media()

    def download_episode_preview(self):
        # template = self.PAGE_PREFIX + 'images/story/%s/p_%s.jpg'
        # for i in range(self.FINAL_EPISODE):
        #     episode = str(i + 1).zfill(2)
        #     if self.is_image_exists(episode + '_1'):
        #         continue
        #     ep_template = template % (str(i + 1).zfill(3), '%s')
        #     stop = False
        #     for j in range(self.IMAGES_PER_EPISODE):
        #         image_url = ep_template % str(j + 1).zfill(3)
        #         image_name = episode + '_' + str(j + 1)
        #         result = self.download_image(image_url, self.base_folder + '/' + image_name)
        #         if result == -1:
        #             stop = True
        #             break
        #     if stop:
        #         break

        yt_folder, yt_episodes = self.init_youtube_thumbnail_variables(['01'])
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story.html')
            stories = soup.select('.content_wrap a[href]')
            for story in stories:
                try:
                    episode = str(int(story['href'].split('/')[-1].replace('story', '').replace('.html', ''))).zfill(2)
                    if self.is_image_exists(episode + '_1') and episode in yt_episodes:
                        continue
                except:
                    continue
                story_url = self.PAGE_PREFIX + story['href']
                story_soup = self.get_soup(story_url)
                if story_soup is not None:
                    self.image_list = []
                    images = story_soup.select('.thumbnail-list img[src]')
                    for i in range(len(images)):
                        image_url = self.PAGE_PREFIX + images[i]['src'].replace('../', '')
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)

                    # YouTube thumbnail
                    yt_tag = story_soup.select('.yt_movie iframe[src]')
                    if len(yt_tag) > 0:
                        yt_id = yt_tag[0]['src'].split('?')[0].split('/')[-1]
                        self.download_youtube_thumbnail_by_id(yt_id, yt_folder, episode)
        except Exception as e:
            self.print_exception(e, 'YouTube thumbnails')

    def download_episode_preview_external(self):
        keywords = ['転生王女と天才令嬢の魔法革命']
        AniverseMagazineScanner(keywords, self.base_folder, last_episode=self.FINAL_EPISODE,
                                end_date='20221202', download_id=self.download_id).run()

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.element',
                                    title_select='.title', date_select='.day', id_select='a',
                                    date_separator='/', news_prefix='news.html', a_tag_prefix=self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('top_visual_01_v_001_pc', self.PAGE_PREFIX + 'images/top/visual_01/v_001_pc.jpg')
        # self.add_to_image_list('top_visual_02_v_002', self.PAGE_PREFIX + 'images/top/visual_02/v_002.jpg')
        self.download_image_list(folder)

        # template = self.PAGE_PREFIX + 'images/news/p_%s.jpg'
        # self.download_by_template(folder, template, 3, 1, prefix='news_')

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.visual_wrap.pc img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src']
                if '/images/' not in image_url or 'visual' not in image_url:
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
            soup = self.get_soup(self.PAGE_PREFIX + 'chara.html')
            a_tags = soup.select('.chara_list_wrap a[href], .chara_sub_wrap a[href]')
            for a_tag in a_tags:
                link = a_tag['href']
                page = link.split('/')[-1].split('.html')[0]
                if page in processed:
                    continue
                chara_soup = self.get_soup(self.PAGE_PREFIX + link)
                if chara_soup is None:
                    continue
                images = chara_soup.select('.chara_calc img[src],.chara_face img[src],.chara_face2 img[src]')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
                if len(self.image_list) > 0:
                    processed.append(page)
                self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'package.html')
            images = soup.select('.package_content img[src]')
            self.image_list = []
            for image in images:
                if '/package/' not in image['src']:
                    continue
                temp_name = image['src'].split('/')[-1]
                if temp_name.startswith('nowpri'):
                    continue
                image_url = self.PAGE_PREFIX + image['src']
                image_name = self.generate_image_name_from_url(image_url, 'package')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')


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
        self.download_media()

    def download_episode_preview(self):
        story_url = self.PAGE_PREFIX + 'story/'
        # yt_folder, yt_episodes = self.init_youtube_thumbnail_variables()
        try:
            soup = self.get_soup(story_url, decode=True)
            stories = soup.select('.p-story__nav li')
            for story in stories:
                a_tags = story.select('a[href]')
                if len(a_tags) == 0:
                    continue
                try:
                    ep_num = int(a_tags[0].text.replace('#', ''))
                    if ep_num is None or ep_num < 1:
                        continue
                    episode = str(ep_num).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):  # and episode in yt_episodes:
                    continue
                if story.has_attr('class') and 'is-current' in story['class']:
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(story_url + a_tags[0]['href'].replace('./', ''))
                if ep_soup is not None:
                    images = ep_soup.select('.swiper-wrapper img[src]')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = story_url + images[i]['src']
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)

                # yt_tag = ep_soup.select('.md-movie[data-youtubeid]')
                # if len(yt_tag) > 0 and len(yt_tag[0]['data-youtubeid']) > 0:
                #     yt_id = yt_tag[0]['data-youtubeid']
                #     self.download_youtube_thumbnail_by_id(yt_id, yt_folder, episode)
        except Exception as e:
            self.print_exception(e)

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
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'assets/t/img/main/img_main-illust.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/t/img/chara/img_chara%s.png'
        self.download_by_template(folder, template, 2, 1)

    def download_media(self):
        folder = self.create_media_directory()

        # Blu-ray
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            for i in range(6):
                bd_url = self.PAGE_PREFIX + 'bddvd/'
                if i > 0:
                    bd_no = str(i + 1).zfill(2)
                    if bd_no in processed:
                        continue
                    else:
                        bd_url += bd_no + '.html'
                soup = self.get_soup(bd_url)
                if soup is not None:
                    images = soup.select('.p-bddvd img[src]')
                    self.image_list = []
                    for image in images:
                        src = image['src']
                        if '/bd-dvd/' not in src:
                            continue
                        if not src.endswith('img_novelty_np.jpg') and not src.endswith('img_package_np.jpg'):
                            image_url = self.PAGE_PREFIX + src.replace('../', '')
                            image_name = self.generate_image_name_from_url(image_url, 'bd-dvd')
                            self.add_to_image_list(image_name, image_url)
                    if i > 0:
                        if len(self.image_list) > 0:
                            processed.append(str(i))
                        else:
                            break
                    self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Blu-ray')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Tondemo Skill de Isekai Hourou Meshi
class TondemoSkillDownload(Winter2023AnimeDownload, NewsTemplate):
    title = 'Tondemo Skill de Isekai Hourou Meshi'
    keywords = [title, 'Campfire Cooking in Another World with My Absurd Skill', 'Tonsuki']
    website = 'https://tondemoskill-anime.com/'
    twitter = 'tonsuki_anime'
    hashtags = ['とんでもスキル', 'tondemo_skill']
    folder_name = 'tondemo-skill'

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
            json_obj = self.get_json(self.PAGE_PREFIX + 'data/')
            if json_obj is None:
                return
            if 'story' not in json_obj or 'items' not in json_obj['story']\
                    or not isinstance(json_obj['story']['items'], list):
                return
            for item in json_obj['story']['items']:
                if 'no' in item:
                    try:
                        episode = str(int(item['no'])).zfill(2)
                    except:
                        continue
                    if self.is_image_exists(episode + '_5'):
                        continue
                    if 'thumbnails' in item and isinstance(item['thumbnails'], list) and len(item['thumbnails']) > 0:
                        self.image_list = []
                        for i in range(len(item['thumbnails'])):
                            image_url = item['thumbnails'][i].split('?')[0]
                            image_name = episode + '_' + str(i + 1)
                            self.add_to_image_list(image_name, image_url)
                        self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ul.p-news__list li.p-news__list-item',
                                    date_select='.p-news_data__date', title_select='.p-news_data__title',
                                    id_select='a', date_func=lambda x: x[0:4] + '.' + x[4:],
                                    next_page_select='div.c-pagination__nav.-next', next_page_eval_index=-1,
                                    next_page_eval_index_class='is-disable')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        # self.add_to_image_list('tz', self.PAGE_PREFIX + 'wordpress/wp-content/themes/tondemoskill/assets/img/top/kv.jpg')
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FgNCmj5aMAE1Hv6?format=jpg&name=4096x4096')
        self.add_to_image_list('kv_tw', 'https://pbs.twimg.com/media/FjcAFh5akAAt0c5?format=jpg&name=4096x4096')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.js-kv_visual img[src]')
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
        prefix = self.PAGE_PREFIX + 'wordpress/wp-content/themes/tondemoskill/assets/img/character/'
        templates = [prefix + 'ch%s_stand.png', prefix + 'ch%s_look.png']
        self.download_by_template(folder, templates, 2, 1)

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        for page in ['bd-store', 'vol01', 'vol02', 'vol03']:
            try:
                if page.startswith('vol'):
                    if page in processed:
                        continue
                    bd_url = self.PAGE_PREFIX + 'bd/' + page + '/'
                else:
                    bd_url = self.PAGE_PREFIX + 'bd-store/'
                soup = self.get_soup(bd_url)
                if page.startswith('vol'):
                    images = soup.select('.p-bd_thumb__visual img[src]')
                else:
                    images = soup.select('.p-bd_special_data__thumb img[src]')
                self.image_list = []
                for image in images:
                    image_url = image['src']
                    if image_url.startswith('/'):
                        image_url = self.PAGE_PREFIX + image_url[1:]
                    if '/common/cs.png' in image_url:
                        continue
                    image_name = self.extract_image_name_from_url(image_url)
                    if self.is_image_exists(image_name, folder):
                        continue
                    self.add_to_image_list(image_name, image_url)
                if page.startswith('vol'):
                    if len(self.image_list) == 0:
                        break
                    else:
                        processed.append(page)
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Tsundere Akuyaku Reijou Liselotte to Jikkyou no Endou-kun to Kaisetsu no Kobayashi-san
class TsunliseDownload(Winter2023AnimeDownload, NewsTemplate):
    title = 'Tsundere Akuyaku Reijou Liselotte to Jikkyou no Endou-kun to Kaisetsu no Kobayashi-san'
    keywords = [title, 'tsunlise', 'Endo and Kobayashi Live! The Latest on Tsundere Villainess Lieselotte']
    website = 'https://tsunlise-pr.com/'
    twitter = 'tsunlise_pr'
    hashtags = 'ツンリゼ'
    folder_name = 'tsunlise'

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
            story_boxes = soup.select('.story-box')
            for story_box in story_boxes:
                episode = None
                if story_box.has_attr('class'):
                    for _class in story_box['class']:
                        if _class.startswith('story') and _class[5:].strip().isnumeric():
                            episode = str(int(_class[5:].strip())).zfill(2)
                            break
                if episode is None:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                images = story_box.select('.story-pic img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        # Paging logic need update
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-item',
                                    date_select='.date', title_select='.title', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv1_1', self.PAGE_PREFIX + 'wp/wp-content/uploads/2022/07/01_ツンリゼ_第1弾KV_ツンver..jpg')
        self.add_to_image_list('kv1_2', self.PAGE_PREFIX + 'wp/wp-content/uploads/2022/07/02_ツンリゼ_第1弾KV_デレver..jpg')
        self.add_to_image_list('kv2', self.PAGE_PREFIX + 'wp/wp-content/uploads/2022/11/ツンリゼ第2弾KV_ロゴ入り.jpg')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.firstview img[src].pc')
            for image in images:
                if '/tunlise-honban-theme/images/' in image['src']:
                    image_url = image['src']
                    image_name = self.generate_image_name_from_url(image_url, 'tunlise-honban-theme')
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/tunlise-honban-theme/images/chara-pic%s.png'
        self.download_by_template(folder, template, 1, 1)

    def download_media(self):
        folder = self.create_media_directory()
        for page in ['privilege', 'bluray']:
            try:
                page_url = self.PAGE_PREFIX + page + '/'
                soup = self.get_soup(page_url)
                images = soup.select('.bluray-page img[src]')
                self.image_list = []
                for image in images:
                    image_url = image['src']
                    image_name = self.extract_image_name_from_url(image_url)
                    if self.is_image_exists(image_name, folder):
                        continue
                    if page == 'bluray' and not self.is_content_length_in_range(image_url, more_than_amount=8000):
                        continue
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
            except Exception as e:
                self.print_exception(e, f'Blu-ray - {page}')


# Vinland Saga Season 2
class VinlandSaga2Download(Winter2023AnimeDownload):
    title = 'Vinland Saga Season 2'
    keywords = [title, '2nd']
    website = 'https://vinlandsaga.jp/'
    twitter = 'V_SAGA_ANIME'
    hashtags = ['VINLAND_SAGA', 'ヴィンランド・サガ']
    folder_name = 'vinlandsaga2'

    PAGE_PREFIX = website
    FINAL_EPISODE = 24

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview_external()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX)

    def download_episode_preview_external(self):
        AnimagePlusScanner('ヴィンランド・サガ', self.base_folder, last_episode=self.FINAL_EPISODE,
                           end_date='20221219', download_id=self.download_id).run()
