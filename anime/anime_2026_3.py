from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate3, NewsTemplate4
from datetime import datetime, timedelta
from requests.exceptions import HTTPError
from scan import AniverseMagazineScanner
import os


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
