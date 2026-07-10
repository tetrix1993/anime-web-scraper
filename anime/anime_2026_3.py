from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate4, NewsTemplate5, NewsTemplate6
from datetime import datetime, timedelta
import os
import base64
from urllib.parse import quote


# Summer 2026 Anime
class Summer2026AnimeDownload(MainDownload):
    season = "2026-3"
    season_name = "Summer 2026"
    folder_name = '2026-3'

    def __init__(self):
        super().__init__()


# Futsutsuka na Akujo dewa Gozaimasu ga: Suuguu Chouso Torikae Den
class FutsutsukaDownload(Summer2026AnimeDownload, NewsTemplate6):
    title = 'Futsutsuka na Akujo dewa Gozaimasu ga: Suuguu Chouso Torikae Den'
    keywords = [title, 'Though I Am an Inept Villainess']
    website = 'https://futsutsuka.net/'
    twitter = 'futsutsuka_PR'
    hashtags = ['ふつつかな悪女']
    folder_name = 'futsutsuka'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'episodes/img/%s/%s.jpg'
        try:
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news('detail.html?d=')


# Gaikotsu Kishi-sama, Tadaima Isekai e Odekakechuu II
class GaikotsuKishi2Download(Summer2026AnimeDownload, NewsTemplate):
    title = 'Gaikotsu Kishi-sama, Tadaima Isekai e Odekakechuu II'
    keywords = [title, 'Skeleton Knight in Another World', 'Gaikotsukishi', '2nd']
    website = 'https://skeleton-knight.com/'
    twitter = 'gaikotsukishi02'
    hashtags = '骸骨騎士様'
    folder_name = 'gaikotsukishi2'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story')
            switch_div = soup.select('div.switch')
            for s in switch_div:
                h3_tag = s.select('h3.mds03')
                if len(h3_tag) == 0 or h3_tag[0].text != 'SEASON02':
                    continue
                a_tags = s.select('ol.switch a[href]')
                for a_tag in reversed(a_tags):
                    try:
                        episode = str(int(a_tag.text.strip().replace('第', '').replace('話', ''))).zfill(2)
                    except:
                        continue
                    ep_soup = self.get_soup(a_tag['href'])
                    if ep_soup is not None:
                        images = ep_soup.select('#story_cont img[src]')
                        self.image_list = []
                        for i in range(len(images)):
                            image_url = self.clear_resize_in_url(images[i]['src'])
                            image_name = episode + '_' + str(i + 1)
                            self.add_to_image_list(image_name, image_url)
                        self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)


# Grand Blue S3
class GrandBlue3Download(Summer2026AnimeDownload, NewsTemplate2):
    title = 'Grand Blue Season 3'
    keywords = [title, 'Grand Blue Dreaming', '3rd']
    website = 'https://www.grandblue-anime.com/'
    twitter = 'gb_anime'
    hashtags = 'ぐらんぶる'
    folder_name = 'grandblue3'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/13.html')
            stories = soup.select('table[summary="List_Type01"] a[href]')
            for story in stories:
                story_url = self.PAGE_PREFIX + story['href'].replace('../', '')
                try:
                    episode = ''
                    ep_num = story.text
                    for a in ep_num:
                        if a.isnumeric():
                            episode += a
                    if len(episode) == 0:
                        continue
                    episode = str(int(episode)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if episode == '01':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(story_url)
                if ep_soup is not None:
                    images = ep_soup.select('.ph img[src]')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = self.PAGE_PREFIX + images[i]['src'].split('?')[0]
                        image_url = self.remove_string(image_url, ['../', 'sn_'])
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url, to_jpg=True)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)


# Hell Mode
class HellMode2Download(Summer2026AnimeDownload, NewsTemplate):
    title = 'Hell Mode Season 2'
    keywords = [title, '2nd']
    website = 'https://hellmode-anime.com/'
    twitter = 'hellmode_anime'
    hashtags = ['ヘルモード']
    folder_name = 'hellmode2'

    PAGE_PREFIX = website
    FINAL_EPISODE = 24
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            stories = soup.select('.season-box.second .story-box')
            for story in stories:
                try:
                    episode = ''
                    ep_num = story.select('.story-title p.num')[0].text
                    for a in reversed(ep_num):
                        if a.isnumeric():
                            episode = a + episode
                    if len(episode) == 0:
                        continue
                    episode = str(int(episode)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                images = story.select('.ss-container img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_episode_preview_guess(self, print_invalid=False, download_valid=True):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_' + str(self.IMAGES_PER_EPISODE)):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wp/wp-content/uploads/%s/%s/%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        valid_urls = []
        for j in range(self.IMAGES_PER_EPISODE):
            k = 0
            while k < 20:
                if k == 0:
                    append = ''
                else:
                    append = '-' + str(k)
                image_folder = folder + '/' + year + '/' + month
                image_name = str(j + 1).zfill(2) + append
                if not self.is_image_exists(image_name, image_folder):
                    image_url = template % (year, month, image_name)
                    if self.is_valid_url(image_url, is_image=True):
                        print('VALID - ' + image_url)
                        is_successful = True
                        valid_urls.append({'name': image_name, 'url': image_url, 'folder': image_folder})
                    else:
                        if print_invalid:
                            print('INVALID - ' + image_url)
                        break
                k += 1
        if download_valid and len(valid_urls) > 0:
            for valid_url in valid_urls:
                image_name = valid_url['name']
                image_folder = valid_url['folder']
                if not os.path.exists(image_folder):
                    os.makedirs(image_folder)
                self.download_image(valid_url['url'], image_folder + '/' + image_name, to_jpg=True)
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful


# Heroine? Seijo? Iie, All Works Maid desu (Hokori)!
class AllWorksMaidDownload(Summer2026AnimeDownload, NewsTemplate):
    title = 'Heroine? Seijo? Iie, All Works Maid desu (Hokori)!'
    keywords = [title, "Heroine? Saint? No, I'm an All-Works Maid (And Proud of It)!"]
    website = 'https://all-works-maid-anime.com/'
    twitter = 'allworks_maid'
    hashtags = 'オールワークスメイド'
    folder_name = 'allworksmaid'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'episode/')
            stories = soup.select('.episode__content[id]')
            for story in stories:
                try:
                    episode = str(int(story['id'].split('-')[-1])).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                images = story.select('.episode__thumb-btn img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news__list li',
                                    date_select='.news__year', title_select='.news__link-title',
                                    id_select='a', next_page_select='.next.page-numbers', paging_type=0)


# Katainaka no Ossan, Kensei ni Naru II
class OssanKensei2Download(Summer2026AnimeDownload, NewsTemplate2):
    title = 'Katainaka no Ossan, Kensei ni Naru II'
    keywords = [title, 'From Old Country Bumpkin to Master Swordsman Season 2', '2nd']
    website = 'https://ossan-kensei.com/'
    twitter = 'ossan_kensei'
    hashtags = 'おっさん剣聖'
    folder_name = 'ossankensei2'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/01.html')
            stories = soup.select('table[summary="List_Type01"] a[href]')
            for story in stories:
                story_url = self.PAGE_PREFIX + story['href'].replace('../', '')
                try:
                    episode = str(int(story.text.replace('#', ''))).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if episode == '01':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(story_url)
                if ep_soup is not None:
                    images = ep_soup.select('.ph img[src]')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = self.PAGE_PREFIX + images[i]['src'].split('?')[0]
                        image_url = self.remove_string(image_url, ['../', 'sn_'])
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url, to_jpg=True)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)


# Kimi no Koto ga Daidaidaidaidaisuki na 100-nin no Kanojo 3rd Season
class Hyakkano3Download(Summer2026AnimeDownload, NewsTemplate):
    title = 'Kimi no Koto ga Daidaidaidaidaisuki na 100-nin no Kanojo 3rd Season'
    keywords = [title, 'The 100 Girlfriends Who Really, Really, Really, Really, Really Love You', '3rd']
    website = 'https://hyakkano.com/'
    twitter = 'hyakkano_anime'
    hashtags = '100カノ'
    folder_name = 'hyakkano3'

    PAGE_PREFIX = website
    FIRST_EPISODE = 25
    FINAL_EPISODE = 36
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/season3/')
            stories = soup.select('.story-Wrapper[id]')
            for story in stories:
                try:
                    episode = str(int(story['id'].replace('ep', '')) + self.FIRST_EPISODE - 1).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                self.image_list = []
                images = story.select('.swiper-slide img[src]')
                for i in range(len(images)):
                    image_url = self.clear_resize_in_url(images[i]['src'])
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)


# Koko wa Ore ni Makasete Saki ni Ike to Itte kara 10-nen ga Tattara Densetsu ni Natteita.
class KokooreDownload(Summer2026AnimeDownload, NewsTemplate5):
    title = 'Koko wa Ore ni Makasete Saki ni Ike to Itte kara 10-nen ga Tattara Densetsu ni Natteita.'
    keywords = [title, "kokoore", 'I Became a Legend After My 10 Year-Long Last Stand.']
    website = 'https://kokoore-anime.com/'
    twitter = 'kokoore_anime'
    hashtags = ['ここ俺アニメ']
    folder_name = 'kokoore'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            api_url_prefix = 'https://api.cms.studiodesignapp.com/v2/search?q='
            uid, project_id, schema_key = self.retrieve_nuxt_keys(self.PAGE_PREFIX + 'story', 'story/:slug')
            query = '{"uid":"' + uid + '","project_id":"' + project_id + '",' + \
                    '"schema_key":"' + schema_key + '","orders":"-publishedAt","offset":0,"limit":32}'
            api_url = api_url_prefix + quote(base64.b64encode(query.encode('utf-8')).decode("utf-8"))
            json_obj = self.get_json(api_url)
            self.image_list = []
            for item in json_obj:
                try:
                    fields = item['document']['fields']['default']['mapValue']['fields']
                    image_url = fields['cover']['stringValue']
                    title = fields['title']['stringValue']
                    slug = fields['slug']['stringValue']
                    episode = None
                    img_num = None
                    if slug.lower().startswith('ep') and slug[2:].isnumeric():
                        episode = str(int(slug[2:])).zfill(2)
                        img_num = 1
                    if title.lower().startswith('ep') and '-' in title:
                        split_ = title.split('-')
                        if len(split_) != 2:
                            continue
                        if split_[0][2:].isnumeric():
                            episode = str(int(split_[0][2:])).zfill(2)
                        if split_[1].isnumeric():
                            img_num = int(split_[1])
                    if episode is None or img_num is None or len(image_url) == 0:
                        continue
                    image_name = episode + '_' + str(img_num)
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                except:
                    continue
            self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news()


# Lv999 no Murabito
class Lv999MurabitoDownload(Summer2026AnimeDownload, NewsTemplate5):
    title = 'Lv999 no Murabito'
    keywords = [title, "The Villager of Level 999"]
    website = 'https://lv999-anime.com/'
    twitter = 'lv999_anime'
    hashtags = ['LV999の村人']
    folder_name = 'lv999'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            api_url_prefix = 'https://api.cms.studiodesignapp.com/v2/search?q='
            uid, project_id, schema_key = self.retrieve_nuxt_keys(self.PAGE_PREFIX + 'story', 'story/:slug')
            query = '{"uid":"' + uid + '","project_id":"' + project_id + '",' + \
                    '"schema_key":"' + schema_key + '","orders":"-publishedAt","offset":0,"limit":32}'
            api_url = api_url_prefix + quote(base64.b64encode(query.encode('utf-8')).decode("utf-8"))
            json_obj = self.get_json(api_url)
            self.image_list = []
            for item in json_obj:
                try:
                    fields = item['document']['fields']['default']['mapValue']['fields']
                    image_url = fields['cover']['stringValue']
                    title = fields['title']['stringValue']
                    slug = fields['slug']['stringValue']
                    episode = None
                    img_num = None
                    if slug.lower().startswith('episode') and slug[7:].isnumeric():
                        episode = str(int(slug[7:])).zfill(2)
                        img_num = 1
                    if title.lower().startswith('episode') and '-' in title:
                        split_ = title.split('-')
                        if len(split_) != 2:
                            continue
                        if split_[0][7:].isnumeric():
                            episode = str(int(split_[0][7:])).zfill(2)
                        if split_[1].isnumeric():
                            img_num = int(split_[1])
                    if episode is None or img_num is None or len(image_url) == 0:
                        continue
                    image_name = episode + '_' + str(img_num)
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                except:
                    continue
            self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news()


# Kabushikigaisha Magi-Lumière 2nd Season
class Magilumiere2Download(Summer2026AnimeDownload, NewsTemplate4):
    title = 'Kabushikigaisha Magi-Lumière 2nd Season'
    keywords = [title, 'Magilumiere Magical Girls Inc.']
    website = 'https://magilumiere-pr.com/'
    twitter = 'MagilumiereLtd'
    hashtags = 'マジルミエ'
    folder_name = 'magilumiere2'

    PAGE_PREFIX = website
    IMAGES_PER_EPISODE = 6
    FINAL_EPISODE = 12

    def __init__(self):
        super().__init__()

    def run(self):
        json_obj = self.download_episode_preview()
        self.download_news(json_obj)

    def download_episode_preview(self):
        json_obj = None
        try:
            json_obj = self.get_json(self.PAGE_PREFIX + 'api/site-data/init')
            for story in json_obj['story']:
                episode = story['episode'].zfill(2)
                self.image_list = []
                for i in range(len(story['images'])):
                    image_name = episode + '_' + str(i + 1)
                    image_url = story['images'][i]['image_path']
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)
        return json_obj

    def download_episode_preview_guess(self, print_invalid=False, download_valid=True):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_' + str(self.IMAGES_PER_EPISODE)):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + '2nd/wp-content/uploads/%s/%s/%s.png'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        valid_urls = []
        for j in range(self.IMAGES_PER_EPISODE):
            k = 0
            while k < 20:
                if k == 0:
                    append = ''
                else:
                    append = '-' + str(k)
                image_folder = folder + '/' + year + '/' + month
                image_name = str(j + 1) + append
                if not self.is_image_exists(image_name, image_folder):
                    image_url = template % (year, month, image_name)
                    if self.is_valid_url(image_url, is_image=True):
                        print('VALID - ' + image_url)
                        is_successful = True
                        valid_urls.append({'name': image_name, 'url': image_url, 'folder': image_folder})
                    else:
                        if print_invalid:
                            print('INVALID - ' + image_url)
                        break
                k += 1
        if download_valid and len(valid_urls) > 0:
            for valid_url in valid_urls:
                image_name = valid_url['name']
                image_folder = valid_url['folder']
                if not os.path.exists(image_folder):
                    os.makedirs(image_folder)
                self.download_image(valid_url['url'], image_folder + '/' + image_name, to_jpg=True)
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful

    def download_news(self, json_obj=None):
        self.download_template_news(json_url=self.PAGE_PREFIX + 'api/site-data/init')


# Mushoku Tensei III: Isekai Ittara Honki Dasu
class MushokuTensei3Download(Summer2026AnimeDownload, NewsTemplate):
    title = "Mushoku Tensei: Isekai Ittara Honki Dasu III"
    keywords = [title, 'Jobless Reincarnation', '3rd']
    website = 'https://mushokutensei.jp/'
    twitter = 'mushokutensei_A'
    hashtags = ['無職転生', 'MushokuTensei']
    folder_name = 'mushokutensei3'

    PAGE_PREFIX = website
    FINAL_EPISODE = 24

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()

    def download_episode_preview(self):
        try:
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if not self.is_image_exists(episode + '_1'):
                    ep_soup = self.get_soup(self.PAGE_PREFIX + f'story/3-{episode}/', impersonate=True)
                    if ep_soup is not None:
                        self.image_list = []
                        images = ep_soup.select('.storycontents_subimg_img[data-imgload]')
                        if len(images) == 0:
                            break
                        for j in range(len(images)):
                            image_url = images[j]['data-imgload']
                            image_name = episode + '_' + str(j + 1)
                            self.add_to_image_list(image_name, image_url)
                        self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)


# Otome Game Sekai wa Mob ni Kibishii Sekai desu 2
class Mobseka2Download(Summer2026AnimeDownload, NewsTemplate):
    title = 'Otome Game Sekai wa Mob ni Kibishii Sekai desu 2'
    keywords = [title, 'Trapped in a Dating Sim: The World of Otome Games is Tough for Mobs', 'Mobseka', 'Mobuseka',
                '2nd']
    website = 'https://mobseka.com/'
    twitter = 'mobseka_anime'
    hashtags = ['モブせか', 'mobseka', 'mobuseka']
    folder_name = 'mobseka2'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            stories = soup.select('section.story__episode')
            for story in stories:
                try:
                    episode = ''
                    ep_num = story.select('.story__episode-num')[0].text
                    for a in ep_num:
                        if a.isnumeric():
                            episode += a
                    if len(episode) == 0:
                        continue
                    episode = str(int(episode)).zfill(2)
                except:
                    continue
                self.image_list = []
                images = story.select('.story__episode-images .story__episode-thumb img[src]')
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-item',
                                    date_select='.news-item__date', title_select='.news-item__title',
                                    id_select='a', paging_type=0, next_page_select='.news-pagination__list li',
                                    next_page_eval_index=-1, next_page_eval_index_class='is-current')


# Rakudai Kenja no Gakuin Musou
class RakudaiKenjaDownload(Summer2026AnimeDownload, NewsTemplate2):
    title = 'Rakudai Kenja no Gakuin Musou'
    keywords = [title, "Nidome no Tensei, S-Rank Cheat Majutsushi Boukenroku",
                'From Overshadowed to Overpowered: Second Reincarnation of a Talentless Sage']
    website = 'https://rakudai-anime.com/'
    twitter = 'rakudai_anime'
    hashtags = ['落第賢者']
    folder_name = 'rakudaikenja'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'story/01.html')
            stories = soup.select('table[summary="List_Type01"] a[href]')
            for story in stories:
                story_url = self.PAGE_PREFIX + story['href'].replace('../', '')
                try:
                    episode = ''
                    ep_num = story.text
                    for a in ep_num:
                        if a.isnumeric():
                            episode += a
                    if len(episode) == 0:
                        continue
                    episode = str(int(episode)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                if episode == '01':
                    ep_soup = soup
                else:
                    ep_soup = self.get_soup(story_url)
                if ep_soup is not None:
                    images = ep_soup.select('.ph img[src]')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = self.PAGE_PREFIX + images[i]['src'].split('?')[0]
                        image_url = self.remove_string(image_url, ['../', 'sn_'])
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url, to_jpg=True)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX)

    def download_episode_preview_guess(self, print_url=False):
        self.download_guess_core_sys(self.PAGE_PREFIX, self.FINAL_EPISODE, self.IMAGES_PER_EPISODE, 4, 21, 29, 4,
                                     self.IMAGES_PER_EPISODE, print_url)


# Ryoumin 0-nin Start no Henkyou Ryoushu-sama
class Ryomin0Download(Summer2026AnimeDownload, NewsTemplate6):
    title = 'Ryoumin 0-nin Start no Henkyou Ryoushu-sama'
    keywords = [title, "ryomin0", 'The Frontier Lord Begins with Zero Subjects']
    website = 'https://ryomin0-anime.com/'
    twitter = 'ryomin0_anime'
    hashtags = ['ryomin0anime', 'アニメ領民０人']
    folder_name = 'ryomin0'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 8

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'story/img/%s/%s.jpg'
        try:
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news('detail.html?d=')


# Saijo no Osewa
class SaijonoOsewaDownload(Summer2026AnimeDownload, NewsTemplate):
    title = 'Saijo no Osewa'
    keywords = [title, "Rich Girl Caretaker"]
    website = 'https://saijonoosewa-anime.com/'
    twitter = 'saijonoosewa_pr'
    hashtags = ['才女のお世話']
    folder_name = 'saijonoosewa'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'episodes/')
            stories = soup.select('.episodes--nav__links a[href]')
            for story in stories:
                try:
                    episode = ''
                    ep_num = story.text
                    for a in reversed(ep_num):
                        if a.isnumeric():
                            episode = a + episode
                    if len(episode) == 0:
                        continue
                    episode = str(int(episode)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                ep_soup = self.get_soup(story['href'])
                if ep_soup is None:
                    continue
                images = ep_soup.select('.episodes--contents__carousel img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article', date_select='time',
                                    title_select='.info--txt__ttl', id_select='a', paging_type=0,
                                    next_page_select='.pagination li', next_page_eval_index=-1,
                                    next_page_eval_index_class='is__current')

    def download_episode_preview_guess(self, print_invalid=False, download_valid=True):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_' + str(self.IMAGES_PER_EPISODE)):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wp/wp-content/uploads/%s/%s/%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        valid_urls = []
        for j in range(self.IMAGES_PER_EPISODE):
            k = 0
            while k < 20:
                if k == 0:
                    append = ''
                else:
                    append = '-' + str(k)
                image_folder = folder + '/' + year + '/' + month
                image_name = str(j + 1).zfill(2) + append
                if not self.is_image_exists(image_name, image_folder):
                    image_url = template % (year, month, image_name)
                    if self.is_valid_url(image_url, is_image=True):
                        print('VALID - ' + image_url)
                        is_successful = True
                        valid_urls.append({'name': image_name, 'url': image_url, 'folder': image_folder})
                    else:
                        if print_invalid:
                            print('INVALID - ' + image_url)
                        break
                k += 1
        if download_valid and len(valid_urls) > 0:
            for valid_url in valid_urls:
                image_name = valid_url['name']
                image_folder = valid_url['folder']
                if not os.path.exists(image_folder):
                    os.makedirs(image_folder)
                self.download_image(valid_url['url'], image_folder + '/' + image_name, to_jpg=True)
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful


# Saikyou Degarashi Ouji no Anyaku Teii Arasoi
class DegarashiOujiDownload(Summer2026AnimeDownload, NewsTemplate):
    title = 'Saikyou Degarashi Ouji no Anyaku Teii Arasoi'
    keywords = [title, "The Insipid Prince's Furtive Grab for The Throne"]
    website = 'https://degarashiouji.com/'
    twitter = 'sn_degarashi'
    hashtags = ['出涸らし', '出涸らし皇子']
    folder_name = 'degarashiouji'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            stories = soup.select('.story-box')
            for story in stories:
                try:
                    episode = ''
                    ep_num = story.select('.story-title p.num')[0].text
                    for a in reversed(ep_num):
                        if a.isnumeric():
                            episode = a + episode
                    if len(episode) == 0:
                        continue
                    episode = str(int(episode)).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                images = story.select('.ss-container img[src]')
                self.image_list = []
                for i in range(len(images)):
                    image_url = images[i]['src']
                    image_name = episode + '_' + str(i + 1)
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
                self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news-item', date_select='.date',
                                    title_select='.title', id_select='a')

    def download_episode_preview_guess(self, print_invalid=False, download_valid=True):
        if self.is_image_exists(str(self.FINAL_EPISODE).zfill(2) + '_' + str(self.IMAGES_PER_EPISODE)):
            return

        folder = self.create_custom_directory('guess')
        template = self.PAGE_PREFIX + 'wp/wp-content/uploads/%s/%s/%s.jpg'
        current_date = datetime.now() + timedelta(hours=1)
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        is_successful = False
        valid_urls = []
        for j in range(self.IMAGES_PER_EPISODE):
            k = 0
            while k < 20:
                if k == 0:
                    append = ''
                else:
                    append = '-' + str(k)
                image_folder = folder + '/' + year + '/' + month
                image_name = str(j + 1).zfill(2) + append
                if not self.is_image_exists(image_name, image_folder):
                    image_url = template % (year, month, image_name)
                    if self.is_valid_url(image_url, is_image=True):
                        print('VALID - ' + image_url)
                        is_successful = True
                        valid_urls.append({'name': image_name, 'url': image_url, 'folder': image_folder})
                    else:
                        if print_invalid:
                            print('INVALID - ' + image_url)
                        break
                k += 1
        if download_valid and len(valid_urls) > 0:
            for valid_url in valid_urls:
                image_name = valid_url['name']
                image_folder = valid_url['folder']
                if not os.path.exists(image_folder):
                    os.makedirs(image_folder)
                self.download_image(valid_url['url'], image_folder + '/' + image_name, to_jpg=True)
        if is_successful:
            print(self.__class__.__name__ + ' - Guessed correctly!')
        return is_successful


# Sekai Saikyou no Kouei
class RearguardDownload(Summer2026AnimeDownload, NewsTemplate):
    title = 'Sekai Saikyou no Kouei'
    keywords = [title, "The World's Strongest Rearguard"]
    website = 'https://strongestrearguard-anime.com/'
    twitter = 'Rearguard_PR'
    hashtags = ['世界最強の後衛']
    folder_name = 'rearguard'

    PAGE_PREFIX = website
    IMAGES_PER_EPISODE = 6
    FINAL_EPISODE = 12

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'assets/images/story/%s_%s.jpg'
        try:
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (episode, str(j + 1).zfill(2))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article', date_select='time',
                                    title_select='h3', id_select=None, id_has_id=True,
                                    a_tag_prefix=self.PAGE_PREFIX + 'news/#')


# Tenkou-saki no Seiso Karen na Bishoujo ga, Mukashi Danshi to Omotte Issho ni Asonda Osananajimi Datta Ken
class TenbinDownload(Summer2026AnimeDownload, NewsTemplate):
    title = 'Tenkou-saki no Seiso Karen na Bishoujo ga, Mukashi Danshi to Omotte Issho ni Asonda Osananajimi Datta Ken'
    keywords = [title, "tenbin", 'Oh Boy, Was I Wrong About Her']
    website = 'https://tenbin-anime.asmik-ace.co.jp/'
    twitter = 'tenbin_anime'
    hashtags = ['てんびん']
    folder_name = 'tenbin'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 5

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'assets/img/story/ep%s/img%s-large.webp'
        try:
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.p-sub-news__main li',
                                    date_select='.c-post__date', title_select='.c-post__clamp', id_select='a',
                                    date_func=lambda x: x[0:4] + '.' + x[5:7] + '.' + x[8:10],
                                    next_page_select='a.next.page-numbers', paging_type=3, paging_suffix='?page=%s')


# Tsuihou sareta Tensei Juukishi wa Game Chishiki de Musou suru
class JukishiDownload(Summer2026AnimeDownload, NewsTemplate):
    title = 'Tsuihou sareta Tensei Juukishi wa Game Chishiki de Musou suru'
    keywords = [title, "jukishi", 'The Exiled Heavy Knight Knows How to Game the System']
    website = 'https://sh-anime.shochiku.co.jp/jukishi-anime/'
    twitter = 'jukishi_anime'
    hashtags = ['転生重騎士']
    folder_name = 'jukishi'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            stories = soup.select('.story_panel[data-chapter]')
            for story in stories:
                try:
                    episode = str(int(story['data-chapter'])).zfill(2)
                except:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                images = story.select('.swiper-slide img[src]')
                for i in range(len(images)):
                    image_name = episode + '_' + str(i + 1)
                    image_url = self.PAGE_PREFIX + images[i]['src']
                    self.add_to_image_list(image_name, image_url, to_jpg=True)
            self.download_image_list(self.base_folder)
        except Exception as e:
            self.print_exception(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.p-news__item',
                                    date_select='.p-news__item__date', title_select='.p-news__item__ttl',
                                    id_select=None, next_page_select='.c-pager__number', next_page_eval_index=-1,
                                    next_page_eval_index_class='is-active')


# Youjo Senki II
class YoujoSenki2Download(Summer2026AnimeDownload, NewsTemplate6):
    title = 'Youjo Senki II'
    keywords = [title, "Saga of Tanya the Evil II"]
    website = 'https://youjo-senki.jp/'
    twitter = 'youjosenki'
    hashtags = ['幼女戦記', 'youjosenki']
    folder_name = 'youjosenki2'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12
    IMAGES_PER_EPISODE = 6

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        template = self.PAGE_PREFIX + 'assets/story/%s/%s.webp'
        try:
            stop = False
            for i in range(self.FINAL_EPISODE):
                episode = str(i + 1).zfill(2)
                if self.is_image_exists(episode + '_' + str(self.IMAGES_PER_EPISODE)):
                    continue
                for j in range(self.IMAGES_PER_EPISODE):
                    image_url = template % (str(i + 1), str(j + 1))
                    image_name = episode + '_' + str(j + 1)
                    if self.download_image(image_url, self.base_folder + '/' + image_name, to_jpg=True) == -1:
                        stop = True
                        break
                if stop:
                    break
        except Exception as e:
            self.print_exception(e)
