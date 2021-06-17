import os
import anime.constants as constants
from anime.main_download import MainDownload, NewsTemplate1
from datetime import datetime
from scan import AniverseMagazineScanner, MocaNewsScanner, WebNewtypeScanner


# Kaizoku Oujo http://fena-pirate-princess.com/ #海賊王女 @fena_pirate
# Komi-san wa, Komyushou desu. https://komisan-official.com/ #古見さん #komisan @comisanvote
# Muv-Luv Alternative https://muv-luv-alternative-anime.com/ #マブラヴ #マブラヴアニメ #muvluv @Muv_Luv_A_anime
# Saihate no Paladin https://farawaypaladin.com/ #最果てのパラディン #faraway_paladin @faraway_paladin
# Sekai Saikou no Ansatsusha, Isekai Kizoku ni Tensei suru https://ansatsu-kizoku.jp/ #暗殺貴族 @ansatsu_kizoku
# Senpai ga Uzai Kouhai no Hanashi https://senpaiga-uzai-anime.com/ #先輩がうざい後輩の話 @uzai_anime
# Shin no Nakama ja Nai to Yuusha no Party wo Oidasareta node, Henkyou de Slow Life suru Koto ni Shimashita https://shinnonakama.com/ #真の仲間 @shinnonakama_tv
# Taishou Otome Otogibanashi http://taisho-otome.com/ #大正オトメ #昭和オトメ @otome_otogi
# Tate no Yuusha S2 http://shieldhero-anime.jp/ #shieldhero #盾の勇者の成り上がり @shieldheroanime
# Yuuki Yuuna wa Yuusha de Aru: Dai Mankai no Shou https://yuyuyu.tv/season2/ #yuyuyu @anime_yukiyuna


# Fall 2021 Anime
class Fall2021AnimeDownload(MainDownload):
    season = "2021-4"
    season_name = "Fall 2021"
    folder_name = '2021-4'

    def __init__(self):
        super().__init__()


# Kaizoku Oujo
class KaizokuOujoDownload(Fall2021AnimeDownload, NewsTemplate1):
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
        folder = self.create_character_directory()
        template1 = self.PAGE_PREFIX + 'wp/wp-content/themes/fena-pirate-princess/_assets/images/char/detail/char_%s_pc.png'
        template2 = self.PAGE_PREFIX + 'wp/wp-content/themes/fena-pirate-princess/_assets/images/char/ss/char%s.jpg'
        self.download_by_template(folder, template1, 3, 1)
        self.download_by_template(folder, template2, 2, 1)
        template3 = self.PAGE_PREFIX + 'char/char%s-%s.jpg'
        i = 1
        while i <= 50 and self.download_by_template(folder, template3 % (str(i).zfill(2), '%s'), 1):
            i += 1


# Komi-san wa, Komyushou desu.
class KomisanDownload(Fall2021AnimeDownload):
    title = 'Komi-san wa, Komyushou desu.'
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
        news_url = self.PAGE_PREFIX + 'news/'
        stop = False
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            for page in range(1, 2, 1):
                page_url = news_url
                if page > 1:
                    page_url = news_url + 'page/' + str(page) + '/'
                soup = self.get_soup(page_url, decode=True)
                articles = soup.select('article.news-item')
                for article in articles:
                    tag_date = article.find('span', class_='news-item__date')
                    tag_title = article.find('span', class_='news-item__title')
                    a_tag = article.find('a')
                    if tag_date and tag_title and a_tag.has_attr('href'):
                        if a_tag['href'].startswith('/'):
                            article_id = self.PAGE_PREFIX + a_tag['href'][1:]
                        else:
                            article_id = self.PAGE_PREFIX + a_tag['href']
                        date = self.format_news_date(tag_date.text.strip())
                        if len(date) == 0:
                            continue
                        title = ' '.join(tag_title.text.split())
                        if news_obj and (news_obj['id'] == article_id or date < news_obj['date']):
                            stop = True
                            break
                        results.append(self.create_news_log_object(date, title, article_id))
                if stop:
                    break
                # pagination = soup.select('ul.c-pagenation li.c-pagenation__item')
                # if len(pagination) == 0:
                #     break
                # if pagination[-1].has_attr('class') and 'is__current' in pagination[-1]['class']:
                #     break
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - News')
            print(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser_tw', 'https://pbs.twimg.com/media/E1GGa52UYAU7AJu?format=jpg&name=large')
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


# Muv-Luv Alternative
class MuvLuvAlternativeDownload(Fall2021AnimeDownload):
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

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index', diff=2)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        stop = False
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            for page in range(1, 2, 1):
                page_url = news_url
                if page > 1:
                    page_url = news_url + 'page/' + str(page) + '/'
                soup = self.get_soup(page_url, decode=True)
                articles = soup.select('section.u-mg_b_l5 a')
                for article in articles:
                    tag_date = article.find('span', class_='c-thumb-list__date')
                    tag_title = article.find('span', class_='c-thumb-list__title')
                    if tag_date and tag_title and article.has_attr('href'):
                        article_id = news_url + article['href'].replace('./', '')
                        date = self.format_news_date(tag_date.text.strip())
                        if len(date) == 0:
                            continue
                        title = tag_title.text.strip()
                        if news_obj and (news_obj['id'] == article_id or date < news_obj['date']):
                            stop = True
                            break
                        results.append(self.create_news_log_object(date, title, article_id))
                if stop:
                    break
                # pagination = soup.select('ul.c-pagenation li.c-pagenation__item')
                # if len(pagination) == 0:
                #     break
                # if pagination[-1].has_attr('class') and 'is__current' in pagination[-1]['class']:
                #     break
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - News')
            print(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('visual_1b', self.PAGE_PREFIX + 'img/teaser/visual_1b.jpg')
        self.download_image_list(folder)
        self.download_by_template(folder, self.PAGE_PREFIX + 'img/teaser/visual_%s.jpg', 1, 2)


# Saihate no Paladin
class SaihatenoPaladinDownload(Fall2021AnimeDownload):
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
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv1', 'https://pbs.twimg.com/media/EzKrTkqVkAMxXZW?format=jpg&name=large')
        self.add_to_image_list('main_visual-min', self.PAGE_PREFIX + 'img/main_visual-min.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'img/cara%s.png'
        self.download_by_template(folder, template, 1)


# Sekai Saikou no Ansatsusha, Isekai Kizoku ni Tensei suru
class AnsatsuKizokuDownload(Fall2021AnimeDownload):
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
        news_url = self.PAGE_PREFIX + 'news/'
        try:
            soup = self.get_soup(news_url, decode=True)
            lis = soup.select('ul.list li')
            news_obj = self.get_last_news_log_object()
            results = []
            for li in lis:
                tag_date = li.find('p', class_='date')
                tag_title = li.find('div', class_='title')
                a_tag = li.find('a')
                if tag_date and tag_title and a_tag and a_tag.has_attr('href'):
                    article_id = a_tag['href']
                    date = tag_date.text.strip().replace('-', '.')
                    title = tag_title.text.strip()
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
            print("Error in running " + self.__class__.__name__ + ' - News')
            print(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/Ev27c7bUUAIM_47?format=jpg&name=medium')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp-content/themes/ansatsu-kizoku_teaser/assets/images/common/img_character_%s.png'
        self.download_by_template(folder, template, 1)


# Senpai ga Uzai Kouhai no Hanashi
class SenpaigaUzaiDownload(Fall2021AnimeDownload):
    title = 'Senpai ga Uzai Kouhai no Hanashi'
    keywords = [title]
    website = 'https://senpaiga-uzai-anime.com/'
    twitter = 'uzai_anime'
    hashtags = '先輩がうざい後輩の話'
    folder_name = 'senpaiga-uzai'

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
        try:
            soup = self.get_soup(news_url, decode=True)
            articles = soup.select('article.article_contents article')
            news_obj = self.get_last_news_log_object()
            results = []
            for article in articles:
                if not article.has_attr('id'):
                    continue
                tag_date = article.find('time')
                tag_title = article.find('h3')
                if tag_date and tag_title:
                    article_id = article['id']
                    date = self.format_news_date(tag_date.text)
                    if len(date) == 0:
                        continue
                    title = tag_title.text
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
            print("Error in running " + self.__class__.__name__ + ' - News')
            print(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('main-visual', self.PAGE_PREFIX + 'img/top/main-visual.png')
        self.add_to_image_list('visual', 'https://pbs.twimg.com/media/Ez4yUbfVkAMPgny?format=jpg&name=4096x4096')
        self.download_image_list(folder)


# Shin no Nakama ja Nai to Yuusha no Party wo Oidasareta node, Henkyou de Slow Life suru Koto ni Shimashita
class ShinnoNakamaDownload(Fall2021AnimeDownload):
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
        try:
            soup = self.get_soup(news_url, decode=True)
            lis = soup.select('ul.newsListsWrap li')
            news_obj = self.get_last_news_log_object()
            results = []
            for li in lis:
                tag_date = li.find('p', class_='update_time')
                tag_title = li.find('p', class_='update_ttl')
                a_tag = li.find('a')
                if tag_date and tag_title and a_tag and a_tag.has_attr('href'):
                    article_id = news_url + a_tag['href'].replace('./', '')
                    date = tag_date.text.strip()
                    title = tag_title.text.strip()
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
            print("Error in running " + self.__class__.__name__ + ' - News')
            print(e)

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


# Taishou Otome Otogibanashi
class TaishoOtomeDownload(Fall2021AnimeDownload):
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
        news_url = self.PAGE_PREFIX + 'news/'
        try:
            soup = self.get_soup(news_url, decode=True)
            lis = soup.select('ul.newslist li')
            news_obj = self.get_last_news_log_object()
            results = []
            for li in lis:
                tag_date = li.find('div', class_='newslist_date')
                tag_title = li.find('h2', class_='newslist_ttl')
                a_tag = li.find('a')
                if tag_date and tag_title and a_tag and a_tag.has_attr('href'):
                    article_id = news_url + a_tag['href'].replace('./', '')
                    date = self.format_news_date(tag_date.text.strip().replace('年', '.').replace('月', '.').replace('日', ''))
                    if len(date) == 0:
                        continue
                    title = tag_title.text.strip()
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
            print("Error in running " + self.__class__.__name__ + ' - News')
            print(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/taisho-otome/img/index/%s.jpg'
        template_name = 'img_kv%s'
        self.image_list = []
        self.add_to_image_list(template_name % '01', template % (template_name % '01'))
        self.add_to_image_list(template_name % '02', template % (template_name % '02'))
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/taisho-otome/img/character/img_chara%s.png'
        self.download_by_template(folder, template, 2)


# Tate no Yuusha no Nariagari S2
class TateNoYuusha2Download(Fall2021AnimeDownload):
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
            print("Error in running " + self.__class__.__name__ + ' - News')
            print(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('announce', 'https://pbs.twimg.com/media/EDag4MkUwAAQnf0?format=jpg&name=medium')
        self.add_to_image_list('kv1', 'https://pbs.twimg.com/media/EhHFvyVU4AA7cUw?format=jpg&name=large')
        self.add_to_image_list('mv_lg', self.PAGE_PREFIX + '/assets/img/2nd/mv_lg.jpg')
        self.download_image_list(folder)


# Yuuki Yuuna wa Yuusha de Aru: Dai Mankai no Shou
class Yuyuyu3Download(Fall2021AnimeDownload):
    title = "Yuuki Yuuna wa Yuusha de Aru: Dai Mankai no Shou"
    keywords = [title, "Yuyuyu", "Yuki Yuna is a Hero"]
    website = 'https://yuyuyu.tv/season2/'
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

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        prefix = 'https://yuyuyu.tv'
        news_url = prefix + '/news/'
        stop = False
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            for page in range(1, 100, 1):
                page_url = news_url
                if page > 1:
                    page_url = news_url + 'page/' + str(page)
                soup = self.get_soup(page_url, decode=True)
                articles = soup.find_all('article', class_='c-entry-item')
                for article in articles:
                    tag_date = article.find('span', class_='c-entry-date')
                    tag_title = article.find('h1', class_='c-entry-item__title')
                    a_tag = article.find('a', class_='c-entry-item__link')
                    if tag_date and tag_title and a_tag and a_tag.has_attr('href'):
                        article_id = prefix + a_tag['href']
                        date = self.format_news_date(tag_date.text)
                        if len(date) == 0:
                            continue
                        title = tag_title.text.strip()
                        if news_obj and (news_obj['id'] == article_id or date < news_obj['date']):
                            stop = True
                            break
                        results.append(self.create_news_log_object(date, title, article_id))
                        if article_id == (news_url + 'archives/1770'):
                            stop = True
                            break
                if stop or soup.find('i', class_='i-arrows-angle-2-r') is None:
                    break
            success_count = 0
            for result in reversed(results):
                process_result = self.create_news_log_from_news_log_object(result)
                if process_result == 0:
                    success_count += 1
            if len(results) > 0:
                self.create_news_log_cache(success_count, results[0])
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - News')
            print(e)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tw_visual1', 'https://pbs.twimg.com/media/EeUu6NHVAAAqYgu?format=jpg&name=large')
        self.add_to_image_list('tw_visual2', 'https://pbs.twimg.com/media/E0L1PAhVEAICS7o?format=jpg&name=4096x4096')
        self.download_image_list(folder)
        self.download_by_template(folder, self.PAGE_PREFIX + 'img/home/visual_%s.jpg', 2, 10)
