from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate5


# Summer 2026 Anime
class Summer2026AnimeDownload(MainDownload):
    season = "2026-3"
    season_name = "Summer 2026"
    folder_name = '2026-3'

    def __init__(self):
        super().__init__()


# Heroine? Seijo? Iie, All Works Maid desu (Hokori)!
class AllWorksMaidDownload(Summer2026AnimeDownload, NewsTemplate):
    title = 'Heroine? Seijo? Iie, All Works Maid desu (Hokori)!'
    keywords = ["Heroine? Saint? No, I'm an All-Works Maid (And Proud of It)!"]
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


# Koko wa Ore ni Makasete Saki ni Ike to Itte kara 10-nen ga Tattara Densetsu ni Natteita.
class KokooreDownload(Summer2026AnimeDownload, NewsTemplate5):
    title = 'Koko wa Ore ni Makasete Saki ni Ike to Itte kara 10-nen ga Tattara Densetsu ni Natteita.'
    keywords = ["kokoore", 'I Became a Legend After My 10 Year-Long Last Stand.']
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
        pass

    def download_news(self):
        self.download_template_news()


# Lv999 no Murabito
class Lv999MurabitoDownload(Summer2026AnimeDownload, NewsTemplate5):
    title = 'Lv999 no Murabito'
    keywords = ["The Villager of Level 999"]
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
        pass

    def download_news(self):
        self.download_template_news()


# Rakudai Kenja no Gakuin Musou
class RakudaiKenjaDownload(Summer2026AnimeDownload, NewsTemplate2):
    title = 'Rakudai Kenja no Gakuin Musou'
    keywords = ["Nidome no Tensei, S-Rank Cheat Majutsushi Boukenroku",
                'From Overshadowed to Overpowered: Second Reincarnation of a Talentless Sage']
    website = 'https://rakudai-anime.com/'
    twitter = 'rakudai_anime'
    hashtags = ['落第賢者']
    folder_name = 'rakudaikenja'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        pass

    def download_news(self):
        self.download_template_news(page_prefix=self.PAGE_PREFIX)


# Ryoumin 0-nin Start no Henkyou Ryoushu-sama
class Ryomin0Download(Summer2026AnimeDownload):
    title = 'Ryoumin 0-nin Start no Henkyou Ryoushu-sama'
    keywords = ["ryomin0", 'The Frontier Lord Begins with Zero Subjects']
    website = 'https://ryomin0-anime.com/'
    twitter = 'ryomin0_anime'
    hashtags = ['ryomin0anime', 'アニメ領民０人']
    folder_name = 'ryomin0'

    PAGE_PREFIX = website

    def __init__(self):
        super().__init__()

    def run(self):
        self.download_episode_preview()
        self.download_news()

    def download_episode_preview(self):
        pass

    def download_news(self):
        try:
            results = []
            news_obj = self.get_last_news_log_object()
            news_prefix = self.PAGE_PREFIX + 'news/'
            json_obj = self.get_json(news_prefix + 'newslist.json')
            for item in json_obj:
                if 'date' in item and 'uniqueId' in item and 'title' in item:
                    date = item['date']
                    title = item['title']
                    unique_id = item['uniqueId']
                    if len(unique_id) == 0 and 'directLinkUrl' in item and len(item['directLinkUrl']) > 1:
                        url = self.PAGE_PREFIX + item['directLinkUrl'][1:]
                    else:
                        url = news_prefix + 'detail.html?d=' + item['uniqueId']
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
