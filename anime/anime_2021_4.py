import os
import anime.constants as constants
from anime.main_download import MainDownload
from datetime import datetime
from scan import AniverseMagazineScanner, MocaNewsScanner, WebNewtypeScanner


# Tate no Yuusha S2 http://shieldhero-anime.jp/ #shieldhero #盾の勇者の成り上がり @shieldheroanime

# Fall 2021 Anime
class Fall2021AnimeDownload(MainDownload):
    season = "2021-4"
    season_name = "Fall 2021"
    folder_name = '2021-4'

    def __init__(self):
        super().__init__()


# Tate no Yuusha no Nariagari S2
class TateNoYuusha2Download(Fall2021AnimeDownload):
    title = "Tate no Yuusha no Nariagari 2nd Season"
    keywords = [title, "The Rising of the Shield Hero"]
    folder_name = 'tate-no-yuusha2'

    PAGE_PREFIX = "http://shieldhero-anime.jp"

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
