import os
import anime.constants as constants
from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2
from datetime import datetime
from scan import AniverseMagazineScanner, MocaNewsScanner, WebNewtypeScanner


# 100-man no Inochi no Ue ni Ore wa Tatteiru S2 http://1000000-lives.com/ #俺100 @1000000_lives
# Bokutachi no Remake http://bokurema.com/ #ぼくリメ #bokurema @bokurema_anime
# Cheat Kusushi no Slow Life: Isekai ni Tsukurou Drugstore https://www.cheat-kusushi.jp/ #チート薬師 #スローライフ @cheat_kusushi
# Deatte 5-byou de Battle https://dea5-anime.com/ #出会5 #dea5 @dea5_anime
# Genjitsu Shugi Yuusha no Oukoku Saikenki https://genkoku-anime.com/ #現国アニメ @genkoku_info
# Higurashi no Naku Koro ni Sotsu https://higurashianime.com/ #ひぐらし @higu_anime
# Jahy-sama wa Kujikenai! https://jahysama-anime.com/ #ジャヒー様はくじけない @jahysama_anime
# Kanojo mo Kanojo https://kanokano-anime.com/ #kanokano #カノジョも彼女 @kanokano_anime
# Kobayashi-san Chi no Maid Dragon S https://maidragon.jp/2nd/ #maidragon @maidragon_anime
# Mahouka Koukou no Yuutousei https://mahouka-yuutousei.jp/ #mahouka @mahouka_anime
# Megami-ryou no Ryoubo-kun. https://megamiryou.com/ #女神寮 @megamiryou
# Meikyuu Black Company https://meikyubc-anime.com/ #迷宮ブラックカンパニー @meikyubc_anime
# Otome Game https://hamehura-anime.com/story/ #はめふら #hamehura @hamehura
# Peach Boy Riverside https://peachboyriverside.com/ #ピーチボーイリバーサイド @peachboy_anime
# Seirei Gensouki https://seireigensouki.com/ #精霊幻想記 @seireigensouki
# Shinigami Bocchan to Kuro Maid https://bocchan-anime.com/ #死神坊ちゃん @bocchan_anime
# Shiroi Suna no Aquatope https://aquatope-anime.com/ #白い砂のアクアトープ @aquatope_anime
# Tantei wa Mou, Shindeiru. https://tanmoshi-anime.jp/ #たんもし @tanteiwamou_
# Tsuki ga Michibiku Isekai Douchuu #ツキミチ @tsukimichi_PR


# Summer 2021 Anime
class Summer2021AnimeDownload(MainDownload):
    season = "2021-3"
    season_name = "Summer 2021"
    folder_name = '2021-3'

    def __init__(self):
        super().__init__()


# 100-man no Inochi no Ue ni Ore wa Tatteiru 2nd Season
class HyakumanNoInochi2Download(Summer2021AnimeDownload, NewsTemplate):
    title = "100-man no Inochi no Ue ni Ore wa Tatteiru 2nd Season"
    keywords = [title, "I'm standing on 1,000,000 lives.", "Hyakuman", "1000000"]
    website = "https://1000000-lives.com/"
    twitter = '1000000_lives'
    hashtags = '俺100'
    folder_name = '100-man-no-inochi2'

    PAGE_PREFIX = 'https://1000000-lives.com'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.c-news-item',
                                   date_select='span.c-news-item__date', title_select='span.c-news-item__title',
                                   id_select='a', a_tag_prefix=self.PAGE_PREFIX, stop_date='2020',
                                   next_page_select='ul.page-numbers li a.next.page-numbers')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.add_to_image_list('teaser', self.PAGE_PREFIX + '/img/home/visual_03.jpg')
        self.download_image_list(folder)


# Bokutachi no Remake
class BokuremaDownload(Summer2021AnimeDownload, NewsTemplate):
    title = 'Bokutachi no Remake'
    keywords = [title, 'Bokurema', 'Remake our Life!']
    website = "https://bokurema.com"
    twitter = 'bokurema_anime'
    hashtags = ['bokurema', 'ぼくリメ']
    folder_name = 'bokurema'

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
            soup = self.get_soup(self.PAGE_PREFIX + '/story/')
            a_tags = soup.select('li.c-story-list__item a')
            for a_tag in a_tags:
                if 'story/' in a_tag['href']:
                    try:
                        split1 = a_tag['href'].split('story/')[1]
                        if split1[-1] == '/':
                            split1 = split1[:-1]
                        episode = str(int(split1)).zfill(2)
                    except Exception:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    if a_tag.has_attr('class') and 'is--active' in a_tag['class']:
                        ep_soup = soup
                    else:
                        ep_soup = self.get_soup(self.PAGE_PREFIX + a_tag['href'])
                    if ep_soup:
                        images = ep_soup.select('li.c-singlepage-gallery-picture-list__item img')
                        self.image_list = []
                        for i in range(len(images)):
                            if images[i].has_attr('pre-src'):
                                image_url = images[i]['pre-src']
                                image_name = episode + '_' + str(i + 1)
                                self.add_to_image_list(image_name, image_url)
                        self.download_image_list(self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='div.p-news-headline',
                                    date_select='time', title_select='h1', id_select='a', decode_response=False,
                                    date_prefix='20')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', self.PAGE_PREFIX + '/assets/images/teaser_2/main_visual.png')
        self.add_to_image_list('kv1', self.PAGE_PREFIX + '/assets/images/index/top_keyvisual_01.png')
        self.add_to_image_list('kv1_2', self.PAGE_PREFIX + '/assets/images/uploads/2021/02/keyvisual.jpg')
        self.add_to_image_list('wakuwork_collaboration', self.PAGE_PREFIX + '/assets/images/uploads/2021/02/wakuwork_collaboration.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX + '/character/')
            lis = soup.find_all('li', 'p-character-list__item')
            for li in lis:
                label = li.find('label')
                if label and label.has_attr('class') and len(label['class']) > 0:
                    character_name = label['class'][0].replace('c-character-select-area--', '')
                    if len(character_name) > 0:
                        image_url = '%s/assets/images/character/character_visual_%s.png'\
                                    % (self.PAGE_PREFIX, character_name)
                        image_name = 'character_visual_%s' % character_name
                        self.add_to_image_list(image_name, image_url)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)
        self.download_image_list(folder)

    def download_media(self):
        folder = self.create_media_directory()
        self.image_list = []
        self.add_to_image_list('music_op', self.PAGE_PREFIX + '/assets/images/uploads/2021/06/1469a0880be391b2ea29cc539c8b74b2.png')
        self.download_image_list(folder)

        # Blu-ray
        try:
            soup = self.get_soup(self.PAGE_PREFIX + '/bd/')
            images = soup.select('div.p-singlepage__inner--bd img')
            self.image_list = []
            for image in images:
                if image.has_attr('pre-src'):
                    image_url = image['pre-src'].replace('-scaled', '')
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Blu-ray")
            print(e)


# Cheat Kusushi no Slow Life: Isekai ni Tsukurou Drugstore
class CheatKusushiDownload(Summer2021AnimeDownload):
    title = 'Cheat Kusushi no Slow Life: Isekai ni Tsukurou Drugstore'
    keywords = [title, 'Cheat Pharmacist\'s Slow Life: Making a Drugstore in Another World']
    website = 'https://www.cheat-kusushi.jp/'
    twitter = 'cheat_kusushi'
    hashtags = ['チート薬師', 'スローライフ']
    folder_name = 'cheat-kusushi'

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
            divs = soup.select('div.news.bg-news')
            news_obj = self.get_last_news_log_object()
            results = []
            for div in divs:
                paras = div.select('p')
                if len(paras) == 2:
                    article_id = ''
                    date = self.format_news_date(paras[0].text.replace('年', '.')
                                                 .replace('月', '.').replace('日', '').strip())
                    if len(date) == 0:
                        continue
                    title = paras[1].text.strip()
                    if news_obj and (news_obj['title'] == title or date < news_obj['date']):
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
        self.add_to_image_list('teaser', 'https://www.cheat-kusushi.jp/img/top-main.png')
        self.add_to_image_list('kv1', 'https://cheat-kusushi.jp/assets/img/bg/top.png')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/EqTAkcgU8AAe39d?format=jpg&name=large')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            article = soup.find('article', id='js-scroll-to-CHARACTER')
            if article:
                containers = article.find_all('div', class_='container')
                for container in containers:
                    if len(container['class']) > 1:
                        continue
                    images = container.find_all('img')
                    for image in images:
                        if image.has_attr('src'):
                            image_url = self.PAGE_PREFIX + image['src']
                            image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                            self.add_to_image_list(image_name, image_url)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)
        self.download_image_list(folder)


# Deatte 5-byou de Battle
class Dea5Download(Summer2021AnimeDownload, NewsTemplate):
    title = 'Deatte 5-byou de Battle'
    keywords = [title, 'Battle Game in 5 Seconds', 'Dea5']
    website = 'https://dea5-anime.com/'
    twitter = 'dea5_anime'
    hashtags = ['出会5', 'dea5']
    folder_name = 'dea5'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='div.posts div.post',
                                    date_select='p.post_date', title_select='p.post_title', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/EmjTjFDVcAAZT6L?format=jpg&name=900x900')
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'wp-content/themes/design/img/index/kv.jpg')
        self.download_image_list(folder)


# Genjitsu Shugi Yuusha no Oukoku Saikenki
class GenkokuDownload(Summer2021AnimeDownload, NewsTemplate):
    title = "Genjitsu Shugi Yuusha no Oukoku Saikenki"
    keywords = [title, "Genkoku"]
    website = 'https://genkoku-anime.com/'
    twitter = 'genkoku_info'
    hashtags = '現国アニメ'
    folder_name = 'genkoku'

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
            story_url = self.PAGE_PREFIX + 'story/'
            soup = self.get_soup(story_url)
            a_tags = soup.select('div.tab a')
            for a_tag in a_tags:
                if a_tag.text.strip().startswith('#'):
                    try:
                        episode = str(int(a_tag.text.strip().replace('#', ''))).zfill(2)
                    except Exception:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    if (a_tag.has_attr('class') and 'active' in a_tag['class']) or a_tag['href'] == './':
                        ep_soup = soup
                    else:
                        ep_soup = self.get_soup(story_url + a_tag['href'])
                    if ep_soup:
                        images = ep_soup.select('div.swiper-container.slider img')
                        self.image_list = []
                        for i in range(len(images)):
                            image_url = self.PAGE_PREFIX + images[i]['src'].replace('../', '')
                            image_name = episode + '_' + str(i + 1)
                            self.add_to_image_list(image_name, image_url)
                        self.download_image_list(self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='div.list li.info', date_select='time',
                                    title_select='p', id_select='a', a_tag_prefix=self.PAGE_PREFIX,
                                    a_tag_replace_from='../')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', 'https://genkoku-anime.com/teaser/images/mainimg.png')
        self.add_to_image_list(name='teaser_moca',
                               url='https://moca-news.net/article/20201104/2020110410000a_/image/001-i2casw.jpg',
                               is_mocanews=True)
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'images/top/mainimg.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'teaser/images/img_chara_%s.png'
        self.download_by_template(folder, template, 2)

        chara_img_template = self.PAGE_PREFIX + 'images/character/img_%s.png'
        chara_img_face_template = self.PAGE_PREFIX + 'images/character/img_face_%s.png'
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            a_tags = soup.select('#character a')
            self.image_list = []
            for a_tag in a_tags:
                if a_tag.has_attr('href'):
                    name = a_tag['href'].split('.html')[0]
                    img_name = 'img_%s' % name
                    img_face_name = 'img_face_%s' % name
                    if self.is_image_exists(img_name, folder):
                        continue
                    self.add_to_image_list(img_name, chara_img_template % name)
                    self.add_to_image_list(img_face_name, chara_img_face_template % name)
            self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)

    def download_media(self):
        folder = self.create_media_directory()
        self.image_list = []
        self.add_to_image_list('bd_box', 'https://pbs.twimg.com/media/E5NV9ZNVEAwj7v9?format=jpg&name=medium')
        self.add_to_image_list('bd_early_bonus', 'https://pbs.twimg.com/media/E5NWAxbVoAIQtnT?format=jpg&name=medium')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'blu-ray/')
            images = soup.select('#blu-ray img')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)


# Higurashi no Naku Koro ni Sotsu
class HigurashiSotsuDownload(Summer2021AnimeDownload):
    title = "Higurashi no Naku Koro ni Sotsu"
    keywords = [title, "When They Cry"]
    website = 'https://higurashianime.com/'
    twitter = 'higu_anime'
    hashtags = ['ひぐらし', 'higurashi']
    folder_name = 'higurashi-sotsu'

    PAGE_PREFIX = website
    IMAGE_FIRST_EPISODE = 25
    IMAGE_FINAL_EPISODE = 39
    FINAL_EPISODE = IMAGE_FINAL_EPISODE - IMAGE_FIRST_EPISODE + 1

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_bluray()

    def download_episode_preview(self):
        if self.is_image_exists(str(self.FINAL_EPISODE) + '_1'):
            return

        image_url_template = 'https://higurashianime.com/images/story/%s/p_%s.jpg'
        for i in range(self.IMAGE_FIRST_EPISODE, self.IMAGE_FINAL_EPISODE + 1, 1):
            episode = i - self.IMAGE_FIRST_EPISODE + 1
            for j in range(1, 7, 1):
                image_name = str(episode).zfill(2) + '_' + str(j)
                if self.is_image_exists(image_name):
                    continue
                image_url = image_url_template % (str(i).zfill(3), str(j).zfill(3))
                result = self.download_image(image_url, self.base_folder + '/' + image_name)
                if result == -1:
                    return

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news.html'
        try:
            soup = self.get_soup(news_url, decode=True)
            articles = soup.select('article')
            news_obj = self.get_last_news_log_object()
            results = []
            for article in articles:
                tag_title = article.find('div', 'title')
                tag_year = article.find('div', 'year')
                tag_day = article.find('div', 'day')
                a_tag = article.find('a')
                if tag_title and tag_year and tag_day and a_tag:
                    article_id = self.PAGE_PREFIX + a_tag['href']
                    date = self.format_news_date(tag_year.text.strip() + '.' + tag_day.text.strip())
                    if len(date) == 0:
                        continue
                    title = ' '.join(tag_title.text.strip().split())
                    if (news_obj and (news_obj['id'] == article_id or date < news_obj['date'])) or date < '2021.03.19':
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
        self.add_to_image_list('kv', self.PAGE_PREFIX + 'images/index2/v_003.jpg')
        self.add_to_image_list('kv_tw', 'https://pbs.twimg.com/media/E1w6chJUUAAP723?format=jpg&name=medium')
        self.download_image_list(folder)

    def download_bluray(self):
        folder = self.create_bluray_directory()
        try:
            soup = self.get_soup('https://higurashianime.com/package_sotsu.html')
            kiji_wraps = soup.find_all('div', class_='kiji_wrap')
            for kiji_wrap in kiji_wraps:
                image_tags = kiji_wrap.find_all('img')
                self.image_list = []
                for image_tag in image_tags:
                    if image_tag.has_attr('src'):
                        image_url = self.PAGE_PREFIX + image_tag['src']
                        split1 = image_url.split('/')
                        number = None
                        if len(split1) > 2 and len(split1[-2]) == 3:
                            try:
                                int(split1[-2])
                                number = split1[-2]
                            except:
                                pass
                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                        if number:
                            image_name = number + '_' + image_name
                        self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Blu-ray')
            print(e)


# Jahy-sama wa Kujikenai!
class JahysamaDownload(Summer2021AnimeDownload, NewsTemplate):
    title = 'Jahy-sama wa Kujikenai!'
    keywords = [title, 'Jahysama']
    website = 'https://jahysama-anime.com/'
    twitter = 'jahysama_anime'
    hashtags = 'ジャヒー様はくじけない'
    folder_name = 'jahysama'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='li.news_list_item',
                                    date_select='time', title_select='p.article_ttl', id_select='a')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('announce', 'https://pbs.twimg.com/media/EzFk_c7VUAUPh5I?format=jpg&name=large')
        self.add_to_image_list('announce2', self.PAGE_PREFIX + 'img/ogp/ogp.jpg')
        self.add_to_image_list('kv', self.PAGE_PREFIX + 'news/wp-content/uploads/2021/05/mv.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            self.image_list = []
            main_images = soup.select('ul.character_list img')
            container_images = soup.select('div.container_img img')
            container_details_images = soup.select('div.container_details ul.faces.pc_only img')
            images = main_images + container_images + container_details_images
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)


# Kanojo mo Kanojo
class KanokanoDownload(Summer2021AnimeDownload, NewsTemplate):
    title = 'Kanojo mo Kanojo'
    keywords = [title, 'Kanokano']
    website = 'https://kanokano-anime.com'
    twitter = 'kanokano_anime'
    hashtags = ['kanokano', 'カノジョも彼女']
    folder_name = 'kanokano'

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
            soup = self.get_soup(self.PAGE_PREFIX + '/story/')
            blocks = soup.select('div.story-main__detail__block')
            for block in blocks:
                if block.has_attr('id') and block['id'].startswith('StoryBlock'):
                    try:
                        episode = str(int(block['id'].split('StoryBlock')[1].strip())).zfill(2)
                    except Exception:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    images = block.select('div.swiper-slide img')
                    self.image_list = []
                    for i in range(len(images)):
                        image_url = self.PAGE_PREFIX + images[i]['src']
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.news-lineup__block',
                                    date_select='dt', title_select='h2', id_select='a', a_tag_prefix=self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        # self.add_to_image_list('teaser', self.PAGE_PREFIX + 'assets/img/mv-img.png')
        self.add_to_image_list('kv1', self.PAGE_PREFIX + '/assets/img/mv-img@2x.png')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/ExivmbSVEAMCkMG?format=jpg&name=large')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + '/assets/img/character-detail-img%s@2x.png'
        self.download_by_template(folder, template, 2)

    def download_media(self):
        folder = self.create_media_directory()
        self.image_list = []
        self.add_to_image_list('music_ed', 'https://pbs.twimg.com/media/E4tIKfwVEAMKBft?format=jpg&name=large')
        self.download_image_list(folder)

        try:
            soup = self.get_soup(self.PAGE_PREFIX + '/bluraydvd/')
            images = soup.select('div.bluraydvd-wrap img')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src']
                image_name = self.extract_image_name_from_url(image_url)
                if image_name != 'bluraydvd-pic01':
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Blu-ray')
            print(e)


# Kobayashi-san Chi no Maid Dragon S
class KobayashiMaidDragon2Download(Summer2021AnimeDownload, NewsTemplate):
    title = 'Kobayashi-san Chi no Maid Dragon S'
    keywords = [title, "Miss Kobayashi's Maid Dragon"]
    website = 'https://maidragon.jp/2nd/'
    twitter = 'maidragon_anime'
    hashtags = 'maidragon'
    folder_name = 'maidragon2'

    PAGE_PREFIX = website
    BASE_PREFIX = 'https://maidragon.jp/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()

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
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_news(self):
        prefix = 'https://maidragon.jp'
        self.download_template_news(page_prefix=prefix, article_select='article.c-news-item',
                                    date_select='span.c-news-item__date', title_select='span.c-news-item__title',
                                    id_select='a', a_tag_prefix=prefix, stop_date='2019',
                                    next_page_select='ul.page-numbers li a.next.page-numbers')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        news_prefix = self.BASE_PREFIX + 'news/wordpress/wp-content/uploads/'
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/EfEVvJEUwAI6LmD?format=jpg&name=large')
        self.add_to_image_list('teaser_covid', 'https://pbs.twimg.com/media/EfEVvJEUwAI6LmD?format=jpg&name=large')
        self.add_to_image_list('newyear_2021', 'https://pbs.twimg.com/media/EqkvG-lUcAInMkK?format=jpg&name=4096x4096')
        self.add_to_image_list('kv1_1', 'https://pbs.twimg.com/media/Ervaz89VEAkqjT-?format=jpg&name=900x900')
        self.add_to_image_list('kv1_2', self.PAGE_PREFIX + 'img/pre/visual_02.png')
        self.add_to_image_list('kv2', news_prefix + '2021/06/KV2.jpg')
        self.add_to_image_list('onair_visual01', news_prefix + '2021/04/maidragonS_onair_visual01.jpg')
        self.add_to_image_list('onair_visual02', news_prefix + '2021/05/E0nNpJtUcAI5EU5.jpeg')
        self.add_to_image_list('onair_visual03', news_prefix + '2021/05/maidragonS_onair_visual03.jpg')
        self.add_to_image_list('onair_visual04', news_prefix + '2021/05/maidragonS_onair_visual04.jpg')
        self.add_to_image_list('onair_visual05', news_prefix + '2021/05/maidragonS_onair_visual05.jpg')
        self.download_image_list(folder)


# Mahouka Koukou no Yuutousei
class MahoukaYuutouseiDownload(Summer2021AnimeDownload, NewsTemplate):
    title = 'Mahouka Koukou no Yuutousei'
    keywords = [title, 'The Honor Student at Magic High School']
    website = "https://mahouka-yuutousei.jp/"
    twitter = 'mahouka_anime'
    hashtags = 'mahouka'
    folder_name = 'mahouka-yuutousei'

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
            story_url = self.PAGE_PREFIX + 'story/'
            soup = self.get_soup(story_url, decode=True)
            lis = soup.select('div.p-story__header li')
            for li in lis:
                a_tag = li.find('a')
                if a_tag and a_tag.has_attr('href'):
                    try:
                        episode = str(int(a_tag.text.strip()[:-1])).zfill(2)
                    except Exception:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    if li.has_attr('class') and 'is-current' in li['class']:
                        ep_soup = soup
                    else:
                        ep_soup = self.get_soup(self.PAGE_PREFIX + a_tag['href'][1:])
                    if ep_soup:
                        images = ep_soup.select('div.p-story__img-slider img')
                        self.image_list = []
                        for i in range(len(images)):
                            if images[i].has_attr('src'):
                                image_url = story_url + images[i]['src']
                                image_name = episode + '_' + str(i + 1)
                                self.add_to_image_list(image_name, image_url)
                        self.download_image_list(self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ul.p-news__list li.p-news__list-item',
                                    date_select='div.p-news_data__date', title_select='div.p-news_data__title',
                                    id_select='a', paging_type=1, a_tag_prefix=self.PAGE_PREFIX, date_separator=' ',
                                    a_tag_start_text_to_remove='/')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'teaser/img/top/kv_character.png')
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'teaser/img/top/kv.jpg')
        self.add_to_image_list('kv2', self.PAGE_PREFIX + 'assets/img/top/img_main.jpg')
        self.add_to_image_list('kv2_tw', 'https://pbs.twimg.com/media/E4JzZN9VUAAY8hZ?format=jpg&name=4096x4096')
        self.download_image_list(folder)

        frozen_template = self.PAGE_PREFIX + 'assets/img/freeze/img_main_frozen_%s.jpg'
        self.download_by_template(folder, frozen_template, 2, 1, 16)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            thumb_images = soup.select('div.p-chara_nav__data-img img')
            names = []
            for thumb in thumb_images:
                if thumb.has_attr('src') and '/thumb_' in thumb['src'] and thumb['src'].endswith('.png'):
                    names.append(thumb['src'].split('/thumb_')[1].split('.png')[0])
            template = self.PAGE_PREFIX + 'assets/img/character/img_%s.png'
            self.image_list = []
            for name in names:
                image_url = template % name
                image_name = 'img_' + name
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)

    def download_media(self):
        folder = self.create_media_directory()
        self.image_list = []
        self.add_to_image_list('music_op', 'https://pbs.twimg.com/media/E4PDegKUYAU61Lz?format=jpg&name=large')
        self.download_image_list(folder)

        # Blu-ray
        bd_url_template = self.PAGE_PREFIX + 'bddvd/%s'
        for page in ['special', '01', '02', '03', '04', '05']:
            if page == '01':
                bd_url = bd_url_template % ''
            else:
                bd_url = bd_url_template % (page + '.html')
            try:
                soup = self.get_soup(bd_url)
                images = soup.select('div.p-bddvd img')
                self.image_list = []
                for image in images:
                    if image.has_attr('src') and not image['src'].endswith('_np.jpg'):
                        if image['src'].startswith('/'):
                            image_url = self.PAGE_PREFIX + image['src'][1:]
                        else:
                            image_url = self.PAGE_PREFIX + image['src']
                        image_name = self.extract_image_name_from_url(image_url)
                        self.add_to_image_list(image_name, image_url)
                if len(self.image_list) == 0:
                    break
                self.download_image_list(folder)
            except Exception as e:
                print("Error in running " + self.__class__.__name__ + ' - Blu-ray %s.html' % page)
                print(e)


# Megami-ryou no Ryoubo-kun.
class MegamiryouDownload(Summer2021AnimeDownload, NewsTemplate2):
    title = 'Megami-ryou no Ryoubo-kun'
    keywords = [title, 'Megamiryou', "Mother of the Goddess' Dormitory"]
    website = 'https://megamiryou.com/'
    twitter = 'megamiryou'
    hashtags = '女神寮'
    folder_name = 'megamiryou'

    PAGE_PREFIX = website

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')
        # Episode 1 only
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'news/index00100000.html')
            images = soup.select('ul.tp5 img')
            self.image_list = []
            for i in range(len(images)):
                image_url = self.PAGE_PREFIX + images[i]['src'].split('?')[0].replace('../', '')
                image_name = '01_' + str(i + 1)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser_tw', 'https://pbs.twimg.com/media/EsTnmn-U0Acx83l?format=jpg&name=large')
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv_pc.png')
        self.add_to_image_list('tzOriginImg', self.PAGE_PREFIX + 'core_sys/images/main/tz/tzOriginImg.png')
        self.add_to_image_list('teaser2_tw', 'https://pbs.twimg.com/media/Exi4zBeXMAEsbA2?format=jpg&name=4096x4096')
        self.add_to_image_list('teaser2', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv_pc2.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        try:
            soup = self.get_soup(self.PAGE_PREFIX)
            char_wraps = soup.find_all('div', class_='charWrap')
            for char_wrap in char_wraps:
                for char in ['charImg', 'charStand']:
                    char_class = char_wrap.find('div', class_=char)
                    if char_class:
                        images = char_class.find_all('img')
                        for image in images:
                            if image and image.has_attr('src'):
                                image_url = self.PAGE_PREFIX + image['src']
                                image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                                self.add_to_image_list(image_name, image_url)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)
        self.download_image_list(folder)


# Meikyuu Black Company
class MeikyuBCDownload(Summer2021AnimeDownload):
    title = 'Meikyuu Black Company'
    keywords = [title, "The Dungeon of Black Company"]
    website = 'https://meikyubc-anime.com/'
    twitter = 'meikyubc_anime'
    hashtags = '迷宮ブラックカンパニー'
    folder_name = 'meikyubc'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12

    def run(self):
        self.download_episode_preview()
        self.download_episode_preview_external()
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        image_url_template = self.PAGE_PREFIX + '_image/story/story%s_%s.png'
        for i in range(1, self.FINAL_EPISODE + 1, 1):
            episode = str(i).zfill(2)
            if self.is_image_exists(episode + '_1'):
                continue
            for j in range(1, 7, 1):
                image_name = episode + '_' + str(j)
                image_url = image_url_template % (episode, str(j))
                if self.download_image(image_url, self.base_folder + '/' + image_name) == -1:
                    return

    def download_episode_preview_external(self):
        jp_title = '迷宮ブラックカンパニー'
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE, min_width=800,
                                end_date='20210628', download_id=self.download_id).run()

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news.html'
        try:
            soup = self.get_soup(news_url, decode=True)
            news_obj = self.get_last_news_log_object()
            results = []
            dts = soup.select('dt')
            for dt in dts:
                dd = dt.find_next('dd')
                if dd:
                    article_id = ''
                    date = self.format_news_date(dt.text.strip().replace('\n', ''))
                    if len(date) == 0:
                        continue
                    title = dd.text.strip().replace('\n', '')
                    if news_obj and (news_obj['title'] == title or date < news_obj['date']):
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
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/Es40z-1UYAAg7_x?format=jpg&name=medium')
        self.add_to_image_list('kv1', self.PAGE_PREFIX + '_image/keyvisual_2.png')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/ExX7gEEVIAcPU1v?format=jpg&name=medium')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + '_image/charaPop_%s.png'
        self.download_by_template(folder, template, 2)


# Otome Game no Hametsu Flag shika Nai Akuyaku Reijou ni Tensei shiteshimatta... X
class Hamehura2Download(Summer2021AnimeDownload, NewsTemplate):
    title = "Otome Game no Hametsu Flag shika Nai Akuyaku Reijou ni Tensei shiteshimatta... X"
    keywords = [title, "Hamehura", "Hamefura", "My Next Life as a Villainess: All Routes Lead to Doom!", "2nd"]
    website = 'https://hamehura-anime.com/'
    twitter = 'hamehura'
    hashtags = ['はめふら', 'hamehura']
    folder_name = 'hamehura2'

    PAGE_PREFIX = website
    IMAGE_PREFIX = 'https://hamehura-anime.com/2nd/'

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()
        self.download_key_visual()
        self.download_media()

    def download_episode_preview(self):
        try:
            story_url = self.PAGE_PREFIX + 'story/'
            soup = self.get_soup(story_url, decode=True)
            lis = soup.select('ul.ver__archive li')
            for li in lis:
                a_tag = li.find('a')
                if a_tag and a_tag.has_attr('href'):
                    try:
                        episode = str(int(a_tag.text.strip())).zfill(2)
                    except Exception:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    ep_soup = self.get_soup(a_tag['href'])
                    if ep_soup:
                        images = ep_soup.select('div.story--main__slider--inner img')
                        self.image_list = []
                        for i in range(len(images)):
                            if images[i].has_attr('src'):
                                image_url = images[i]['src']
                                image_name = episode + '_' + str(i + 1)
                                self.add_to_image_list(image_name, image_url)
                        self.download_image_list(self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.md-newsblock',
                                    date_select='dt', title_select='h3', id_select='a',
                                    next_page_select='ul.pagenation-list li',
                                    next_page_eval_index_class='is__current', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', self.IMAGE_PREFIX + 'wp-content/uploads/2021/01/はめふらX_ティザービジュアル-1.jpg')
        self.add_to_image_list('kv1', self.IMAGE_PREFIX + 'wp-content/uploads/2021/03/第1弾キービジュアル.jpg')
        #self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/EsJL9ZQVkAEDktJ?format=jpg&name=large')
        self.download_image_list(folder)

    def download_media(self):
        folder = self.create_media_directory()
        cache_filepath = folder + '/cache'
        processed, num_processed = self.get_processed_items_from_cache_file(cache_filepath)
        music_url_template = self.PAGE_PREFIX + 'music-%s/'
        for i in ['op', 'ed']:
            if i in processed:
                continue
            music_url = music_url_template % i
            try:
                soup = self.get_soup(music_url)
                images = soup.select('#Music img')
                for image in images:
                    image_url = image['src']
                    if 'nowprinting' not in image_url:
                        image_name = self.extract_image_name_from_url(image_url)
                        self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
                processed.append(i)
            except Exception as e:
                print("Error in running " + self.__class__.__name__ + ' - Music')
                print(e)
        self.create_cache_file(cache_filepath, processed, num_processed)

        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'package/')
            images = soup.select('#Package img')
            self.image_list = []
            for image in images:
                image_url = image['src']
                if 'nowprinting' not in image_url:
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Blu-ray')
            print(e)


# Peach Boy Riverside
class PeachBoyRiversideDownload(Summer2021AnimeDownload, NewsTemplate):
    title = 'Peach Boy Riverside'
    keywords = [title]
    website = 'https://peachboyriverside.com/'
    twitter = 'peachboy_anime'
    hashtags = 'ピーチボーイリバーサイド'
    folder_name = 'peachboyriverside'

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
            story_url = self.PAGE_PREFIX + 'story/'
            soup = self.get_soup(story_url, decode=True)
            lis = soup.select('ul.ver__archive li')
            for li in lis:
                a_tag = li.find('a')
                if a_tag and a_tag.has_attr('href'):
                    try:
                        episode = str(int(a_tag.text.strip())).zfill(2)
                    except Exception:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    ep_soup = self.get_soup(a_tag['href'])
                    if ep_soup:
                        images = ep_soup.select('div.story--slider__inner img')
                        self.image_list = []
                        for i in range(len(images)):
                            if images[i].has_attr('src'):
                                image_url = images[i]['src']
                                image_name = episode + '_' + str(i + 1)
                                self.add_to_image_list(image_name, image_url)
                        self.download_image_list(self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ul.md--articleblock.ver__pages li',
                                    date_select='h3', title_select='h4.ttl', id_select='a',
                                    next_page_select='ul.pagenation-list li',
                                    next_page_eval_index_class='is__current', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        #self.image_list = []
        #self.add_to_image_list('kv1', self.PAGE_PREFIX + 'wp/wp-content/themes/peachboyriverside_main/_assets/images/top/fv/fv_pc.jpg')
        #self.download_image_list(folder)
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/peachboyriverside_main/_assets/images/top/fv/fv_pc_%s.jpg'
        self.download_by_template(folder, template, 3, 1)

    def download_character(self):
        folder = self.create_character_directory()
        image_name_template = 'char_main_%s@2x'
        url_template = self.PAGE_PREFIX + 'wp/wp-content/themes/peachboyriverside_main/_assets/images/pages/char/main/'\
            + image_name_template + '.png'
        try:
            for i in range(1, 100, 1):
                image_name = image_name_template % str(i).zfill(3)
                if self.is_image_exists(image_name, folder):
                    continue
                url = url_template % str(i).zfill(3)
                result = self.download_image(url, folder + '/' + image_name)
                if result == -1:
                    break
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)


# Seirei Gensouki
class SeireiGensoukiDownload(Summer2021AnimeDownload, NewsTemplate):
    title = "Seirei Gensouki"
    keywords = [title, "Spirit Chronicles"]
    website = "https://seireigensouki.com/"
    twitter = 'seireigensouki'
    hashtags = '精霊幻想記'
    folder_name = 'seirei-gensouki'

    PAGE_PREFIX = website
    FINAL_EPISODE = 12

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
            soup = self.get_soup(self.PAGE_PREFIX + 'story/')
            story_boxes = soup.select('div.story-box')
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
                images = story_box.select('div.ss-display img')
                self.image_list = []
                for i in range(len(images)):
                    if images[i].has_attr('src'):
                        image_url = images[i]['src']
                        image_name = episode + '_' + str(i + 1)
                        self.add_to_image_list(image_name, image_url)
                self.download_image_list(self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Music')
            print(e)

    def download_episode_preview_external(self):
        jp_title = '精霊幻想記'
        AniverseMagazineScanner(jp_title, self.base_folder, last_episode=self.FINAL_EPISODE, min_width=750,
                                end_date='20210702', download_id=self.download_id).run()

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ul.news-list li.news-item',
                                    date_select='p.news-date', title_select='p.news-title', id_select='a',
                                    news_prefix='news-list/', next_page_select='div.pagination div.next',
                                    next_page_eval_index_class='off', next_page_eval_index=0)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/EnytdwVVQAESUct?format=jpg&name=large')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/EzFiWEmVUAI4bdm?format=jpg&name=4096x4096')
        # self.add_to_image_list('teaser', self.PAGE_PREFIX + 'wp/wp-content/uploads/2020/11/SG_teaser_logoc.png')
        self.download_image_list(folder)

        templates = []
        for i in ['jpg', 'png']:
            templates.append(self.PAGE_PREFIX + 'wp/wp-content/themes/seirei_honban/assets/img/page/mainvisual%s.' + i)
            self.download_by_template(folder, templates, 1)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/seirei_honban/assets/img/page/chara-pic%s.png'
        self.download_by_template(folder, template, 2)

        self.image_list = []
        self.add_to_image_list('celia_claire', 'https://seireigensouki.com/wp/wp-content/uploads/2021/03/セリアクレール.jpg')
        self.add_to_image_list('aishia', 'https://seireigensouki.com/wp/wp-content/uploads/2021/03/アイシア.jpg')
        self.add_to_image_list('latifa', 'https://seireigensouki.com/wp/wp-content/uploads/2021/04/ラティーファ.jpg')
        self.add_to_image_list('ayase_miharu', 'https://seireigensouki.com/wp/wp-content/uploads/2021/04/綾瀬美春.jpg')
        self.download_image_list(folder)

    def download_media(self):
        folder = self.create_media_directory()
        for page in ['bddvd', 'music']:
            try:
                soup = self.get_soup(self.PAGE_PREFIX + page + '/')
                images = soup.select('div.page-content img')
                self.image_list = []
                for image in images:
                    if image.has_attr('src') and len(image['src'].strip()) > 0:
                        image_url = image['src']
                        image_name = self.extract_image_name_from_url(image_url)
                        self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
            except Exception as e:
                if page == 'bddvd':
                    page_name = 'Blu-ray'
                else:
                    page_name = 'Music'
                print("Error in running " + self.__class__.__name__ + ' - %s' % page_name)
                print(e)


# Shinigami Bocchan to Kuro Maid
class ShinigamiBocchanDownload(Summer2021AnimeDownload, NewsTemplate2):
    title = 'Shinigami Bocchan to Kuro Maid'
    keywords = [title, 'The Duke of Death and His Maid']
    website = 'https://bocchan-anime.com/'
    twitter = 'bocchan_anime'
    hashtags = '死神坊ちゃん'
    folder_name = 'shinigami-bocchan'

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
            a_tags = soup.select('#ContentsListUnit01 a')
            for a_tag in a_tags:
                if 'index' not in a_tag['href'] and a_tag['href'].endswith('.html') and '/' in a_tag['href']:
                    try:
                        episode = str(int(a_tag['href'].split('/')[-1].split('.html')[0])).zfill(2)
                    except Exception:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    ep_soup = self.get_soup(self.PAGE_PREFIX + a_tag['href'].replace('../', ''))
                    if ep_soup:
                        images = ep_soup.select('ul.tp5 img')
                        self.image_list = []
                        for i in range(len(images)):
                            image_url = self.PAGE_PREFIX + images[i]['src'].replace('../', '').split('?')[0]
                            image_name = episode + '_' + str(i + 1)
                            self.add_to_image_list(image_name, image_url)
                        self.download_image_list(self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'core_sys/images/main/home/kv_tz.png')
        self.add_to_image_list('kv', self.PAGE_PREFIX + 'core_sys/images/main/home/kv.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'chara/')
            a_tags = soup.select('td.l_wdp01 a')
            self.image_list = []
            for a_tag in a_tags:
                if a_tag.has_attr('href') and '/' in a_tag['href'] and a_tag['href'].endswith('.html'):
                    href = a_tag['href']
                    image_name = href.split('/')[-1].split('.html')[0]
                    if image_name == 'index':
                        image_name = 'bocchan'
                    image = a_tag.find('img')
                    if not image or not image.has_attr('src'):
                        continue
                    src = image['src']
                    src_name = src.split('/')[-1]
                    image_url = self.PAGE_PREFIX + (src[0:len(src) - len(src_name)] + '001.png').replace('../', '')
                    self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)

    def download_media(self):
        folder = self.create_media_directory()
        music_url_template = self.PAGE_PREFIX + 'music/%s'
        for page in ['', 'ost']:
            if len(page) == 0:
                music_url = music_url_template % ''
            else:
                music_url = music_url_template % (page + '.html')
            try:
                soup = self.get_soup(music_url)
                images = soup.select('#cms_block img')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                    image_name = self.extract_image_name_from_url(image_url)
                    if 'nowprinting' in image_url:
                        continue
                    if self.is_image_exists(image_name):
                        continue
                    if self.is_matching_content_length(image_url, 218502):
                        continue
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
            except Exception as e:
                print("Error in running " + self.__class__.__name__ + ' - Music %s' % music_url)
                print(e)

        # Blu-ray
        bd_url_template = self.PAGE_PREFIX + 'bd/%s'
        for page in ['privilege', 'campaign', '01', '02', '03', '04', '05']:
            if page == '01':
                bd_url = bd_url_template % ''
            else:
                bd_url = bd_url_template % (page + '.html')
            try:
                soup = self.get_soup(bd_url)
                if page.isnumeric():
                    images = soup.select('div.block.line_01 img')
                else:
                    images = soup.select('#cms_block img')
                self.image_list = []
                for image in images:
                    if image.has_attr('src'):
                        image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                        image_name = self.extract_image_name_from_url(image_url)
                        if self.is_image_exists(image_name):
                            continue
                        if image_url.endswith('.gif'):
                            continue
                        if self.is_matching_content_length(image_url, [65898, 57601]):
                            continue
                        self.add_to_image_list(image_name, image_url)
                if len(self.image_list) == 0:
                    break
                self.download_image_list(folder)
            except Exception as e:
                print("Error in running " + self.__class__.__name__ + ' - Blu-ray %s.html' % page)
                print(e)


# Shiroi Suna no Aquatope
class AquatopeDownload(Summer2021AnimeDownload, NewsTemplate):
    title = 'Shiroi Suna no Aquatope'
    keywords = [title, 'Aquatope of White Sand']
    website = 'https://aquatope-anime.com/'
    twitter = 'aquatope_anime'
    hashtags = '白い砂のアクアトープ'
    folder_name = 'aquatope'

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
            story_url = self.PAGE_PREFIX + 'story/'
            soup = self.get_soup(story_url, decode=True)
            lis = soup.select('ul.ver__archive li')
            for li in lis:
                a_tag = li.find('a')
                if a_tag and a_tag.has_attr('href'):
                    try:
                        episode = str(int(a_tag.text.strip())).zfill(2)
                    except Exception:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    ep_soup = self.get_soup(a_tag['href'])
                    if ep_soup:
                        images = ep_soup.select('div.story--main__ss--slider__img img')
                        self.image_list = []
                        for i in range(len(images)):
                            if images[i].has_attr('src'):
                                image_url = images[i]['src']
                                image_name = episode + '_' + str(i + 1)
                                self.add_to_image_list(image_name, image_url)
                        self.download_image_list(self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.md-archive__news',
                                    date_select='time.txt--date', title_select='h3.txt--ttl',
                                    id_select='a', next_page_select='ul.pagenation-list li',
                                    next_page_eval_index_class='is__current', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser_tw', 'https://pbs.twimg.com/media/ErwuT7rVQAISak1?format=jpg&name=large')
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'wp/wp-content/themes/aquatope-teaser/_assets/images/kv/kv_pc@2x.jpg')
        self.add_to_image_list('kv1', 'https://pbs.twimg.com/media/EyR238pVgAQLNej?format=jpg&name=large')
        self.add_to_image_list('kv2', self.PAGE_PREFIX + 'wp/wp-content/themes/aquatope-main/_assets/images/top/fv/fv_003@2x.jpg')
        self.add_to_image_list('kv2_big', self.PAGE_PREFIX + 'wp/wp-content/uploads/2021/05/【白い砂のアクアトープ】第2弾キービジュアル.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        self.add_to_image_list('kukuru_design', self.PAGE_PREFIX + 'wp/wp-content/themes/aquatope-teaser/_assets/images/char/design/kukuru_design.png')
        self.add_to_image_list('fuuka_design', self.PAGE_PREFIX + 'wp/wp-content/themes/aquatope-teaser/_assets/images/char/design/fuuka_design.png')
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/')
            images = soup.select('picture.chardata--photo__img img')
            images = images + soup.select('picture.photo img')
            for image in images:
                image_url = image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)
        self.download_image_list(folder)

    def download_media(self):
        folder = self.create_media_directory()

        # Music
        self.image_list = []
        for i in ['music-op', 'music-ed']:
            url = self.PAGE_PREFIX + i + '/'
            soup = self.get_soup(url)
            images = soup.select('picture img')
            images = images + soup.select('article.data--block img')
            for image in images:
                if 'nowprinting' not in image['src']:
                    image_url = image['src']
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
        self.download_image_list(folder)


# Tantei wa Mou, Shindeiru.
class TanmoshiDownload(Summer2021AnimeDownload, NewsTemplate2):
    title = "Tantei wa Mou, Shindeiru."
    keywords = [title, "Tanmoshi", "The Detective Is Already Dead"]
    website = 'https://tanmoshi-anime.jp/'
    twitter = 'tanteiwamou_'
    hashtags = ['tanmoshi', 'たんもし']
    folder_name = 'tanmoshi'

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
            a_tags = soup.select('#ContentsListUnit01 a')
            for a_tag in a_tags:
                if 'index' not in a_tag['href'] and a_tag['href'].endswith('.html') and '/' in a_tag['href']:
                    try:
                        episode = str(int(a_tag['href'].split('/')[-1].split('.html')[0])).zfill(2)
                    except Exception:
                        continue
                    if self.is_image_exists(episode + '_1'):
                        continue
                    ep_soup = self.get_soup(self.PAGE_PREFIX + a_tag['href'].replace('../', ''))
                    if ep_soup:
                        images = ep_soup.select('ul.tp5 img')
                        self.image_list = []
                        for i in range(len(images)):
                            image_url = self.PAGE_PREFIX + images[i]['src'].replace('../', '').split('?')[0]
                            image_name = episode + '_' + str(i + 1)
                            self.add_to_image_list(image_name, image_url)
                        self.download_image_list(self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_news(self):
        self.download_template_news(self.PAGE_PREFIX)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('kv1', 'https://pbs.twimg.com/media/EsCTT1KXAAUGy6V?format=jpg&name=4096x4096')
        self.add_to_image_list('kv2', 'https://pbs.twimg.com/media/Eug1UGwUYAcgxON?format=jpg&name=4096x4096')
        self.add_to_image_list('kv3', 'https://pbs.twimg.com/media/Ew13JI0UYAMwHm6?format=jpg&name=4096x4096')
        self.add_to_image_list('kv4', 'https://pbs.twimg.com/media/EzVZyckVIAQsrG3?format=jpg&name=4096x4096')
        self.add_to_image_list('kv5', self.PAGE_PREFIX + 'core_sys/images/main/tz/kv5.png')
        self.add_to_image_list('kv6', 'https://pbs.twimg.com/media/E32w0I2UcAMfmZe?format=jpg&name=4096x4096')
        template = self.PAGE_PREFIX + 'core_sys/images/main/tz/%s.png'
        for name in ['umbouzu', 'mugiko', 'poni', 'moyashi']:
            image_name = 'illust_' + name
            self.add_to_image_list(image_name, template % image_name)
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'core_sys/images/main/cont/char/%s.png'
        for i in range(20):
            base_name = str(i + 1).zfill(2)
            name = base_name + '_a'
            if self.is_image_exists(name, folder) or self.is_image_exists(base_name, folder):
                continue
            result = self.download_image(template % name, folder + '/' + name)
            if result == -1:
                result2 = self.download_image(template % base_name, folder + '/' + base_name)
                if result2 == -1:
                    return
            else:
                name = base_name + '_b'
                if self.is_image_exists(name, folder):
                    continue
                self.download_image(template % name, folder + '/' + name)

        # Old Logic
        #self.image_list = []
        #try:
        #    soup = self.get_soup(self.PAGE_PREFIX)
        #    wraps = soup.find_all('div', class_='charListWrap')
        #    for wrap in wraps:
        #        images = wrap.find_all('img')
        #        for image in images:
        #            if image.has_attr('src'):
        #                image_url = self.PAGE_PREFIX + image['src']
        #                image_name = self.extract_image_name_from_url(image_url, with_extension=False)
        #                self.add_to_image_list(image_name, image_url)
        #except Exception as e:
        #    print("Error in running " + self.__class__.__name__ + " - Character")
        #    print(e)
        #self.download_image_list(folder)

    def download_media(self):
        folder = self.create_media_directory()
        template = self.PAGE_PREFIX + 'core_sys/images/main/cont/special/audio/%s.mp3'
        for i in ('01_kimizuka', '02_siesta', '03_nagisa', '04_yui', '05_charlotte'):
            url = template % i
            self.download_content(url, folder + '/' + i + '.mp3')
        template2 = self.PAGE_PREFIX + 'core_sys/images/main/cont/special/audio/0420/%s.mp3'
        for i in ('01_kimizuka', '02_siesta', '03_nagisa', '04_yui', '05_charlotte'):
            url = template2 % i
            self.download_content(url, folder + '/' + i + '_2.mp3')

        # Blu-rays
        pages = ['privilege.html', 'campaign.html', '', '02.html', '03.html']
        bd_template = self.PAGE_PREFIX + 'bd/%s'
        for i in range(len(pages)):
            url = bd_template % pages[i]
            try:
                soup = self.get_soup(url)
                images = soup.select('#cms_block img')
                self.image_list = []
                for image in images:
                    image_url = self.PAGE_PREFIX + image['src'].replace('../', '').split('?')[0]
                    if 'nowprinting' in image_url:
                        continue
                    image_name = self.extract_image_name_from_url(image_url)
                    self.add_to_image_list(image_name, image_url)
                self.download_image_list(folder)
                if i > 1 and len(self.image_list) == 0:
                    break
            except Exception as e:
                print("Error in running " + self.__class__.__name__ + " - Blu-Ray %s" % url)
                print(e)


# Tsuki ga Michibiku Isekai Douchuu
class TsukimichiDownload(Summer2021AnimeDownload, NewsTemplate):
    title = "Tsuki ga Michibiku Isekai Douchuu"
    keywords = [title, "Tsukimichi", "Moonlit Fantasy"]
    website = 'https://tsukimichi.com/'
    twitter = 'tsukimichi_PR'
    hashtags = 'ツキミチ'
    folder_name = 'tsukimichi'

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
            a_tags = soup.select('ul.ver__archive a')
            for a_tag in a_tags:
                if not a_tag.has_attr('href'):
                    continue
                try:
                    episode = str(int(a_tag.text.strip())).zfill(2)
                except Exception:
                    continue
                if self.is_image_exists(episode + '_1'):
                    continue
                ep_soup = self.get_soup(a_tag['href'])
                if ep_soup:
                    images = ep_soup.select('div.story--main__ss--slider__img img')
                    self.image_list = []
                    for i in range(len(images)):
                        if images[i].has_attr('src'):
                            image_url = images[i]['src']
                            image_name = episode + '_' + str(i + 1)
                            self.add_to_image_list(image_name, image_url)
                    self.download_image_list(self.base_folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__)
            print(e)

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.md-article__block',
                                    date_select='time', title_select='h3', id_select='a',
                                    next_page_select='ul.pagenation-list li',
                                    next_page_eval_index_class='is__current', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/ElZibOAU0AQ8ewu?format=jpg&name=large')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/E0dDrRqVgAQ3cH9?format=jpg&name=4096x4096')
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'wp/wp-content/themes/tsukimichi-main/_assets/images/top/visual/pc.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        base_url = self.PAGE_PREFIX + 'wp/wp-content/themes/tsukimichi-main/_assets/images/pages/char/'
        main_template = base_url + 'main/char_%s_pc.png'
        face_template = base_url + 'face/face_%s.png'
        self.download_by_template(folder, [main_template, face_template], 3, start=1)

    def download_media(self):
        pass
