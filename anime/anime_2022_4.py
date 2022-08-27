import os
from anime.constants import HTTP_HEADER_USER_AGENT
from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2


# Akiba Meido Sensou https://akibamaidwar.com/ #アキバ冥途戦争 @akbmaidwar
# Akuyaku Reijou nanode Last Boss wo Kattemimashita https://akulas-pr.com/ #悪ラス @akulas_pr
# Bocchi the Rock! https://bocchi.rocks/ #ぼっち・ざ・ろっく #BocchiTheRock @BTR_anime
# Futoku no Guild https://futoku-no-anime.com/ #futoku_anime #不徳のギルド @futoku_anime
# Fuufu Ijou, Koibito Miman. https://fuukoi-anime.com/ #ふうこいアニメ @fuukoi_anime
# Kage no Jitsuryokusha ni Naritakute! https://shadow-garden.jp/ #陰の実力者 @Shadowgarden_PR
# Noumin Kanren no Skill bakka Agetetara Nazeka Tsuyoku Natta. https://nouminkanren.com/ #農民関連 @nouminkanren
# Renai Flops https://loveflops.com/ #恋愛フロップス @loveflops_pr
# Shinmai Renkinjutsushi no Tenpo Keiei https://shinmai-renkin.com/ #shinmai_renkin @shinmai_renkin
# Shinobi no Ittoki https://ninja-ittoki.com/ #忍の一時 #ninja @ninja_ittoki
# Tensei shitara Ken Deshita https://tenken-anime.com/ #転生したら剣でした #転剣 @tenken_official
# Uchi no Shishou wa Shippo ga Nai https://shippona-anime.com/ #しっぽな @shippona_anime
# Yama no Susume: Next Summit https://yamanosusume-ns.com/ #ヤマノススメ @yamanosusume
# Yuusha Party wo Tsuihou sareta Beast Tamer, Saikyoushu no Nekomimi Shoujo to Deau


# Fall 2022 Anime
class Fall2022AnimeDownload(MainDownload):
    season = "2022-4"
    season_name = "Fall 2022"
    folder_name = '2022-4'

    def __init__(self):
        super().__init__()


# Akiba Meido Sensou
class AkibaMaidWarDownload(Fall2022AnimeDownload):
    title = 'Akiba Meido Sensou'
    keywords = [title, 'Akiba Maid War']
    website = 'https://akibamaidwar.com/'
    twitter = 'akbmaidwar'
    hashtags = 'アキバ冥途戦争'
    folder_name = 'akibamaidwar'

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
            json_obj = self.get_json_obj_from_api('news')
            if json_obj is None:
                return

            results = []
            news_obj = self.get_last_news_log_object()
            for content in json_obj['contents']:
                if 'id' in content and 'date' in content and 'title' in content:
                    article_id = self.PAGE_PREFIX + 'news/detail?i=' + content['id']
                    if news_obj is not None and news_obj['id'] == article_id:
                        break
                    date = content['date'][0:10].replace('-', '.')
                    title = content['title']
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
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FWAaCg-UEAAJ5sw?format=jpg&name=4096x4096')
        self.add_to_image_list('tz_kv', self.PAGE_PREFIX + 'assets/images/pc/kv.png')
        self.add_to_image_list('kv_tw', 'https://pbs.twimg.com/media/FbDjkZAUcAANv9o?format=jpg&name=large')
        self.add_to_image_list('top_kv', self.PAGE_PREFIX + 'assets/images/pc/top/kv.png')
        self.add_to_image_list('special_kv', 'https://images.microcms-assets.io/assets/cf7267b9b8d74564a1239e1d0515090a/53a656f88fe146b9bd88a24da741fc97/special_kv.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        self.add_to_image_list('tz_chara_image', self.PAGE_PREFIX + 'assets/images/pc/chara_image.png')
        self.download_image_list(folder)

        try:
            json_obj = self.get_json_obj_from_api('character')
            if json_obj is None:
                return

            self.image_list = []
            for content in json_obj['contents']:
                if 'main_img' in content and 'url' in content['main_img']:
                    image_url = content['main_img']['url']
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

    def get_json_obj_from_api(self, name):
        api_url = 'https://'
        bundle = self.get_response(self.PAGE_PREFIX + f'assets/js/{name}.bundle.js')
        keyword = '"https://".concat('
        index = bundle.find(keyword)
        if index <= 0:
            return None
        bundle_split = bundle[len(keyword) + index:]
        next_index = bundle_split.find(')')
        if next_index <= 0:
            return None
        items = bundle_split[0:next_index].split(',')
        for item in items:
            api_url += item.replace('"', '')
        api_url += f"{name}?limit=1000&fields="
        microcms_keyword = '"X-MICROCMS-API-KEY":"'
        microcms_index = bundle.find(microcms_keyword)
        if microcms_index <= 0:
            return None
        bundle_split2 = bundle[len(microcms_keyword) + microcms_index:]
        microcms_next_index = bundle_split2.find('"')
        if microcms_next_index <= 0:
            return None
        microcms_key = bundle_split2[0:microcms_next_index]
        headers = HTTP_HEADER_USER_AGENT
        headers['x-microcms-api-key'] = microcms_key
        return self.get_json(api_url, headers)


# Akuyaku Reijou nanode Last Boss wo Kattemimashita
class AkulasDownload(Fall2022AnimeDownload, NewsTemplate):
    title = 'Akuyaku Reijou nanode Last Boss wo Kattemimashita'
    keywords = [title, "I'm the Villainess, So I'm Taming the Final Boss", 'akulas']
    website = 'https://akulas-pr.com/'
    twitter = 'akulas_pr'
    hashtags = '悪ラス'
    folder_name = 'akulas'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news article',
                                    title_select='.ttl', date_select='.release', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            self.image_list = []
            images = soup.select('.visual img[src]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'][1:]
                if '/top/' in image_url:
                    image_name = self.generate_image_name_from_url(image_url, 'top')
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

        self.image_list = []
        aniverse_prefix = 'https://aniverse-mag.com/wp-content/uploads/2022/03/'
        teaser_prefix = self.PAGE_PREFIX + 'wp/wp-content/themes/akulas-teaser/_assets/images/fv/visual/'
        self.add_to_image_list('tz_aniverse_1', aniverse_prefix + '63a9443ca79764c441208e49969001b0.jpg')
        self.add_to_image_list('tz_aniverse_2', aniverse_prefix + '54e791dc7275325f19a662ad9bf0fad5.jpg')
        self.add_to_image_list('tz_fv_pc1', teaser_prefix + 'fv_pc1.png')
        self.add_to_image_list('tz_fv_pc2', teaser_prefix + 'fv_pc2.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            images = soup.select('.chardata img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'][1:]
                image_name = self.generate_image_name_from_url(image_url, 'detail')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')

        template = self.PAGE_PREFIX + 'wp/wp-content/themes/akulas-teaser/_assets/images/char/detail/char_%s_pc.png'
        self.download_by_template(folder, template, 3, 1, prefix='tz_')


# Bocchi the Rock!
class BocchiTheRockDownload(Fall2022AnimeDownload, NewsTemplate):
    title = 'Bocchi the Rock!'
    keywords = [title, 'bozaro']
    website = 'https://bocchi.rocks/'
    twitter = 'BTR_anime'
    hashtags = ['BocchiTheRock', 'bozaro', 'ぼっち・ざ・ろっく', 'ぼざろ']
    folder_name = 'bocchi-the-rock'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.newsmodal__articles__list__item',
                                    date_select='.date', title_select='.ttl', id_select='a', news_prefix='')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        css_url = self.PAGE_PREFIX + 'assets/css/top.css'
        try:
            content = self.get_response(css_url)
            if content is None or len(content) == 0:
                return
            content_split = content.split('.mv__main {')
            self.image_list = []
            for i in range(1, len(content_split), 1):
                r_index = content_split[i].find(')')
                if r_index > 0:
                    l_index = content_split[i][0:r_index].find('url(../../')
                    if l_index > 0:
                        image_url = self.PAGE_PREFIX + content_split[i][l_index + 10:r_index]
                        image_name = self.generate_image_name_from_url(image_url, 'top')
                        self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            images = soup.select('.modal_ch__faceup__main img[src],.modal_ch__info__ph img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'][1:]
                image_name = self.generate_image_name_from_url(image_url, 'detail')
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Futoku no Guild
class FutokunoGuildDownload(Fall2022AnimeDownload, NewsTemplate2):
    title = 'Futoku no Guild'
    keywords = [title]
    website = 'https://futoku-no-anime.com/'
    twitter = 'futoku_anime'
    hashtags = ['futoku_anime', '不徳のギルド']
    folder_name = 'futoku-no-guild'

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
        self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FNfyKsbVcAMufgT?format=jpg&name=medium')
        self.add_to_image_list('tz_kv', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.png')
        self.add_to_image_list('top_kv', self.PAGE_PREFIX + 'core_sys/images/main/top/kv.jpg')
        self.download_image_list(folder)


# Fuufu Ijou, Koibito Miman.
class FuukoiDownload(Fall2022AnimeDownload, NewsTemplate2):
    title = 'Fuufu Ijou, Koibito Miman.'
    keywords = [title, 'More Than a Married Couple, But Not Lovers', 'fuukoi']
    website = 'https://fuukoi-anime.com/'
    twitter = 'fuukoi_anime'
    hashtags = 'ふうこいアニメ'
    folder_name = 'fuukoi'

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
        image_prefix = self.PAGE_PREFIX + 'core_sys/images/'
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FRbNkGEakAEHfD5?format=jpg&name=4096x4096')
        self.add_to_image_list('tz_kv_webp', image_prefix + 'main/tz/kv.webp')
        self.add_to_image_list('tz_kv', image_prefix + 'main/tz/kv.jpg')
        self.add_to_image_list('tz_news', image_prefix + 'news/00000003/block/00000006/00000001.jpg')
        self.add_to_image_list('kv1', image_prefix + 'news/00000007/block/00000013/00000004.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'chara/')
            a_tags = soup.select('#ContentsListUnit01 a[href]')
            for a_tag in a_tags:
                if not a_tag['href'].endswith('.html'):
                    continue
                page = a_tag['href'].split('/')[-1].split('.html')[0]
                if page in processed:
                    continue
                if page == 'index':
                    chara_soup = soup
                else:
                    chara_soup = self.get_soup(self.PAGE_PREFIX + a_tag['href'].replace('../', ''))
                if chara_soup is None:
                    continue
                self.image_list = []
                images = chara_soup.select('.chara__img img[src], .chara__face img[src]')
                for image in images:
                    if '/chara/' not in image['src']:
                        continue
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                    image_name = self.generate_image_name_from_url(image_url, 'chara')
                    self.add_to_image_list(image_name, image_url)
                if len(self.image_list) > 0:
                    processed.append(page)
                self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Kage no Jitsuryokusha ni Naritakute!
class KagenoJitsuryokushaDownload(Fall2022AnimeDownload, NewsTemplate):
    title = 'Kage no Jitsuryokusha ni Naritakute!'
    keywords = [title, 'The Eminence in Shadow']
    website = 'https://shadow-garden.jp/'
    twitter = 'Shadowgarden_PR'
    hashtags = '陰の実力者'
    folder_name = 'kagenojitsuryoku'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.newsList',
                                    date_select='time', title_select='p.newsList--ttl', id_select='a',
                                    a_tag_prefix=self.PAGE_PREFIX + 'news', a_tag_start_text_to_remove='./')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'news/img/20211027_03_1.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        prefix = self.PAGE_PREFIX + 'assets/img/top/character/chara'
        self.download_by_template(folder, [prefix + '%s_main1.png', prefix + '%s_main2.png'], 2, 1)


# Noumin Kanren no Skill bakka Agetetara Nazeka Tsuyoku Natta.
class NouminKanrenDownload(Fall2022AnimeDownload, NewsTemplate):
    title = 'Noumin Kanren no Skill bakka Agetetara Nazeka Tsuyoku Natta.'
    keywords = [title]
    website = 'https://nouminkanren.com/'
    twitter = 'nouminkanren'
    hashtags = '農民関連'
    folder_name = 'nouminkanren'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.sw-NewsArchive_Item',
                                    title_select='.title', date_select='.date', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz', self.PAGE_PREFIX + 'wordpress/wp-content/uploads/2022/05/24112348/Noumin_KV1tate_RGB150.jpg')
        self.download_image_list(folder)

        template = self.PAGE_PREFIX + 'wordpress/wp-content/themes/nouminkanren/assets/images/pc/index/img_kv_%s.jpg'
        self.download_by_template(folder, template, 1, 1)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            images = soup.select('.character-Index_List a img[src]')
            for image in images:
                image_url = image['src'].replace('thumb.png', 'img.png')
                index = image_url.rfind('/')
                back = image_url[index + 1:]
                front = image_url[0:index]
                file_name = back
                while back != 'character':
                    file_name = back + '_' + file_name
                    index = front.rfind('/')
                    back = front[index + 1:]
                    front = front[0:index]
                image_name = file_name.split('.')[0]
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')


# Renai Flops
class RenaiFlopsDownload(Fall2022AnimeDownload, NewsTemplate):
    title = 'Renai Flops'
    keywords = [title, 'Love Flops']
    website = 'https://loveflops.com/'
    twitter = 'loveflops_pr'
    hashtags = '恋愛フロップス'
    folder_name = 'renai-flops'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='.news_list article',
                                    date_select='.news_list_day', title_select='.ne', id_select='a',
                                    date_separator='/', news_prefix='news.html', a_tag_prefix=self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_tw', 'https://pbs.twimg.com/media/FOrTLwXagAE6Q-C?format=jpg&name=large')
        self.add_to_image_list('tz_aniverse', 'https://aniverse-mag.com/wp-content/uploads/2022/03/6a1f645dc99cda5844a8d86a77f24193-e1648196815379.jpg')
        self.download_image_list(folder)

        self.download_by_template(folder, self.PAGE_PREFIX + 'images/top/visual/v%s.jpg', 3, prefix='top_visual_')
        self.download_by_template(folder, self.PAGE_PREFIX + 'images/news/p_%s.jpg', 3, prefix='news_')

    def download_character(self):
        folder = self.create_character_directory()
        template_prefix = self.PAGE_PREFIX + 'images/chara/'
        templates = [template_prefix + 'b_%s.png', template_prefix + 'a_%s.png']
        self.download_by_template(folder, templates, 3, 1)

    def download_media(self):
        folder = self.create_media_directory()

        # Sample Voices
        voice_folder = folder + '/voice'
        if not os.path.exists(voice_folder):
            os.makedirs(voice_folder)
        for chara in ['asahi', 'aoi', 'amelia', 'ilya', 'mongfa', 'karin', 'yoshio']:
            name_template = f'{chara}_mix_%s.mp3'
            template_prefix = self.PAGE_PREFIX + f'chara/mp3/'
            for i in range(3):
                audio_name = name_template % str(i + 1).zfill(3)
                audio_url = template_prefix + audio_name
                audio_filepath = voice_folder + '/' + audio_name
                result = self.download_content(audio_url, audio_filepath)
                if result == -1:
                    break


# Shinmai Renkinjutsushi no Tenpo Keiei
class ShinmaiRenkinDownload(Fall2022AnimeDownload, NewsTemplate2):
    title = 'Shinmai Renkinjutsushi no Tenpo Keiei'
    keywords = [title, 'Management of Novice Alchemist']
    website = 'https://shinmai-renkin.com/'
    twitter = 'shinmai_renkin'
    hashtags = 'shinmai_renkin'
    folder_name = 'shinmai-renkin'

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
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'special/visual.html')
            images = soup.select('ul.tp5 img[src]')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Key Visual')

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'core_sys/images/main/cont/character/%s.png'
        self.download_by_template(folder, template, 2, 1)


# Shinobi no Ittoki
class ShinobinoIttoki(Fall2022AnimeDownload, NewsTemplate):
    title = 'Shinobi no Ittoki'
    keywords = [title]
    website = 'https://ninja-ittoki.com/'
    twitter = 'ninja_ittoki'
    hashtags = ['忍の一時', 'ninja']
    folder_name = 'shinobi-ittoki'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.newsLists__item',
                                    date_select='time', title_select='.newsLists--title', id_select='a',
                                    next_page_select='.wp-pagenavi *', next_page_eval_index_class='current',
                                    next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('top_main_visual', self.PAGE_PREFIX + 'assets/img/top/main_visual.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/img/character/character%s_main.png'
        self.download_by_template(folder, template, 2, 1)


# Tensei shitara Ken Deshita
class TenkenDownload(Fall2022AnimeDownload, NewsTemplate):
    title = 'Tensei shitara Ken Deshita'
    keywords = [title, 'Reincarnated as a Sword', 'tenken']
    website = 'https://tenken-anime.com/'
    twitter = 'tenken_official'
    hashtags = ['転生したら剣でした', '転剣']
    folder_name = 'tenken'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.content-entry',
                                    title_select='h2.entry-title span', date_select='div.entry-date',
                                    id_select=None, id_has_id=True, news_prefix='news.html',
                                    date_func=lambda x: x[0:4] + '.' + x[4:])

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/FOcR3ESaMAIIZAo?format=jpg&name=4096x4096')
        # self.add_to_image_list('kv1_vis', self.PAGE_PREFIX + 'assets/top/vis.png')
        self.add_to_image_list('kv1_vis-t1', self.PAGE_PREFIX + 'assets/news/vis-t1.jpg')
        self.download_image_list(folder)

        for i in range(1, 10, 1):
            image_name = f'top_t{i}_vis'
            if self.is_image_exists(image_name, folder):
                continue
            is_successful = False
            for j in ['jpg', 'png']:
                image_url = self.PAGE_PREFIX + f'assets/top/t{i}/vis.' + j
                result = self.download_image(image_url, folder + '/' + image_name)
                if result == -1:
                    continue
                else:
                    is_successful = True
                    break
            if not is_successful:
                break

    def download_character(self):
        folder = self.create_character_directory()
        template_prefix = self.PAGE_PREFIX + 'assets/character/'
        templates = [template_prefix + 'c%s.png', template_prefix + 'f%s.png']
        self.download_by_template(folder, templates, 1, 1, prefix='tz_')


# Uchi no Shishou wa Shippo ga Nai
class ShipponaDownload(Fall2022AnimeDownload, NewsTemplate):
    title = 'Uchi no Shishou wa Shippo ga Nai'
    keywords = [title, 'My Master Has No Tail', 'Shippona']
    website = 'https://shippona-anime.com/'
    twitter = 'shippona_anime'
    hashtags = 'しっぽな'
    folder_name = 'shippona'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='a.news-list-item',
                                    date_select='.news-list-item__date', title_select='.news-list-item__title',
                                    id_select=None, a_tag_start_text_to_remove='/', a_tag_prefix=self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tz_natalie', 'https://ogre.natalie.mu/media/news/comic/2022/0106/shippona_teaser.jpg')
        self.download_image_list(folder)

        template_prefix = self.PAGE_PREFIX + 'img/home/visual_%s.'
        templates = [template_prefix + 'jpg', template_prefix + 'png']
        self.download_by_template(folder, templates, 2, 1)

    def download_character(self):
        folder = self.create_character_directory()
        char_url = self.PAGE_PREFIX + 'character'
        json_url = char_url + '/chara_data.php'
        self.image_list = []
        try:
            json_obj = self.get_json(json_url)
            if 'charas' in json_obj and isinstance(json_obj['charas'], list):
                for chara in json_obj['charas']:
                    if 'images' in chara and 'visuals' in chara['images']\
                            and isinstance(chara['images']['visuals'], list):
                        for visual in chara['images']['visuals']:
                            if 'image' in visual:
                                image_url = char_url + visual['image'][1:].split('?')[0]
                                image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                                self.add_to_image_list(image_name, image_url)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)
        self.download_image_list(folder)


# Yama no Susume: Next Summit
class YamaNoSusume4Download(Fall2022AnimeDownload):
    title = 'Yama no Susume: Next Summit'
    keywords = [title, "Encouragement of Climb", "4th"]
    website = 'https://yamanosusume-ns.com/'
    twitter = 'yamanosusume'
    hashtags = 'ヤマノススメ'
    folder_name = 'yamanosusume4'

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
        news_url = self.PAGE_PREFIX
        try:
            soup = self.get_soup(news_url, decode=True)
            articles = soup.select('#nwu_001_t tr')
            news_obj = self.get_last_news_log_object()
            results = []
            for article in articles:
                tag_date = article.find('td', class_='day')
                tag_title = article.find('div', class_='title')
                a_tag = article.find('a')
                if tag_date and tag_title:
                    article_id = ''
                    if a_tag and a_tag.has_attr('href'):
                        article_id = self.PAGE_PREFIX + a_tag['href']
                    date = self.format_news_date(tag_date.text.strip().replace('/', '.'))
                    if len(date) == 0:
                        continue
                    title = tag_title.text.strip()
                    if news_obj and ((news_obj['id'] == article_id and news_obj['title'] == title)
                                     or date < news_obj['date']):
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
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv.png')
        self.add_to_image_list('tz_kv2_kv', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv2/kv.jpg')
        self.add_to_image_list('tz_kv2_kv_tw', 'https://pbs.twimg.com/media/FQ6oxppakAEMP4C?format=jpg&name=4096x4096')
        self.add_to_image_list('home_kv', self.PAGE_PREFIX + 'core_sys/images/main/home/kv.jpg')
        self.add_to_image_list('kv2', 'https://pbs.twimg.com/media/FZ1oVZQaIAA0DOr?format=jpg&name=4096x4096')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'chara/')
            a_tags = soup.select('#ContentsListUnit01 a[href]')
            for a_tag in a_tags:
                if not a_tag['href'].endswith('.html'):
                    continue
                page = a_tag['href'].split('/')[-1].split('.html')[0]
                if page in processed:
                    continue
                if page == 'index':
                    chara_soup = soup
                else:
                    chara_soup = self.get_soup(self.PAGE_PREFIX + a_tag['href'].replace('../', ''))
                if chara_soup is None:
                    continue
                self.image_list = []
                images = chara_soup.select('.chara__img img[src]')
                for image in images:
                    if '/chara/' not in image['src']:
                        continue
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                    image_name = self.generate_image_name_from_url(image_url, 'chara')
                    self.add_to_image_list(image_name, image_url)
                if len(self.image_list) > 0:
                    processed.append(page)
                self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')
        self.create_cache_file(cache_filepath, processed, num_processed)


# Yuusha Party wo Tsuihou sareta Beast Tamer, Saikyoushu no Nekomimi Shoujo to Deau
class BeastTamerDownload(Fall2022AnimeDownload, NewsTemplate):
    title = 'Yuusha Party wo Tsuihou sareta Beast Tamer, Saikyoushu no Nekomimi Shoujo to Deau'
    keywords = [title, 'Beast Tamer']
    website = 'https://beasttamer.jp/'
    twitter = 'beasttamer_off'
    hashtags = ['ビステマ']
    folder_name = 'beast-tamer'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.news-atl-bg',
                                    date_select='.entry-date', title_select='.entry-title', id_select=None,
                                    id_has_id=True, id_attr='id', news_prefix='news.html')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv_tw', 'https://pbs.twimg.com/media/FUtiIgLaQAEcqA2?format=jpg&name=4096x4096')
        self.add_to_image_list('kv2_tw', 'https://pbs.twimg.com/media/FZJK9EzaUAA1-sW?format=jpg&name=4096x4096')
        self.download_image_list(folder)

        for i in range(10):
            image_url = self.PAGE_PREFIX + f'assets/top/t{i + 1}/vis.jpg'
            image_name = f'top_t{i + 1}_vis'
            if not self.is_image_exists(image_name, folder):
                result = self.download_image(image_url, folder + '/' + image_name)
                if result == -1:
                    break

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character.html')
            images = soup.select('.character-data img[data-src]')
            for image in images:
                image_url = self.PAGE_PREFIX + image['data-src'].replace('./', '')
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            self.print_exception(e, 'Character')
            print(e)
        self.download_image_list(folder)
