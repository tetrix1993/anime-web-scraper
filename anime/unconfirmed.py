import os
import anime.constants as constants
from anime.main_download import MainDownload


# Bokutachi no Remake http://bokurema.com/ #ぼくリメ #bokurema @bokurema
# Cheat Kusushi no Slow Life: Isekai ni Tsukurou Drugstore https://www.cheat-kusushi.jp/ #チート薬師 #スローライフ @cheat_kusushi
# Iwa Kakeru!: Sport Climbing Girls http://iwakakeru-anime.com/ #いわかける #iwakakeru @iwakakeru_anime
# Kuma Kuma Kuma Bear https://kumakumakumabear.com/ #くまクマ熊ベアー #kumabear @kumabear_anime
# Kimi to Boku no Saigo no Senjou, Aruiwa Sekai ga Hajimaru Seisen #キミ戦 #kimisen @kimisen_project
# Majo no Tabitabi https://majotabi.jp/ #魔女の旅々 #魔女の旅々はいいぞ #majotabi @majotabi_PR
# Tonikaku Kawaii http://tonikawa.com/ #トニカクカワイイ #tonikawa @tonikawa_anime


# Unconfirmed Season Anime
class UnconfirmedDownload(MainDownload):
    season = "9999-9"
    season_name = "Unconfirmed"

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/unconfirmed"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)


class CheatKusushiDownload(UnconfirmedDownload):
    title = 'Cheat Kusushi no Slow Life: Isekai ni Tsukurou Drugstore'
    keywords = [title, 'Cheat Pharmacist\'s Slow Life: Making a Drugstore in Another World']

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/cheat-kusushi"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_key_visual()

    def download_key_visual(self):
        keyvisual_folder = self.base_folder + '/' + constants.FOLDER_KEY_VISUAL
        if not os.path.exists(keyvisual_folder):
            os.makedirs(keyvisual_folder)

        image_objs = [
            {'name': 'teaser', 'url': 'https://www.cheat-kusushi.jp/img/top-main.png'}]
        for image_obj in image_objs:
            if os.path.exists(keyvisual_folder + '/' + image_obj['name'] + '.png'):
                continue
            filepath_without_extension = keyvisual_folder + '/' + image_obj['name']
            self.download_image(image_obj['url'], filepath_without_extension)


# Iwa Kakeru!: Sport Climbing Girls
class IwakakeruDownload(UnconfirmedDownload):
    title = "Iwa Kakeru!: Sport Climbing Girls"
    keywords = ["Iwa Kakeru!: Sport Climbing Girls", "Iwakakeru"]

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/iwakakeru"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_key_visual()

    def download_key_visual(self):
        keyvisual_folder = self.base_folder + '/' + constants.FOLDER_KEY_VISUAL
        if not os.path.exists(keyvisual_folder):
            os.makedirs(keyvisual_folder)

        image_urls = ["http://iwakakeru-anime.com/img/index/mainvisual.png"]
        for image_url in image_urls:
            image_with_extension = self.extract_image_name_from_url(image_url, with_extension=True)
            if os.path.exists(keyvisual_folder + '/' + image_with_extension):
                continue
            image_without_extension = self.extract_image_name_from_url(image_url, with_extension=False)
            filepath_without_extension = keyvisual_folder + '/' + image_without_extension
            self.download_image(image_url, filepath_without_extension)


# Kimi to Boku no Saigo no Senjou, Aruiwa Sekai ga Hajimaru Seisen
class KimisenDownload(UnconfirmedDownload):
    title = "Kimi to Boku no Saigo no Senjou, Aruiwa Sekai ga Hajimaru Seisen"
    keywords = ["Kimi to Boku no Saigo no Senjou, Aruiwa Sekai ga Hajimaru Seisen", "Kimisen"]

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/kimisen"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_key_visual()

    def download_key_visual(self):
        keyvisual_folder = self.base_folder + '/' + constants.FOLDER_KEY_VISUAL
        if not os.path.exists(keyvisual_folder):
            os.makedirs(keyvisual_folder)

        image_objs = [
            {'name': 'teaser', 'url': 'https://kimisentv.com/teaser/images/top-main-vis.jpg'}]
        for image_obj in image_objs:
            if os.path.exists(keyvisual_folder + '/' + image_obj['name'] + '.png') or \
                    os.path.exists(keyvisual_folder + '/' + image_obj['name'] + '.jpg'):
                continue
            filepath_without_extension = keyvisual_folder + '/' + image_obj['name']
            self.download_image(image_obj['url'], filepath_without_extension)


# Kuma Kuma Kuma Bear
class KumaBearDownload(UnconfirmedDownload):
    title = "Kuma Kuma Kuma Bear"
    keywords = ["Kuma Kuma Kuma Bear"]

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/kumabear"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_key_visual()

    def download_key_visual(self):
        keyvisual_folder = self.base_folder + '/' + constants.FOLDER_KEY_VISUAL
        if not os.path.exists(keyvisual_folder):
            os.makedirs(keyvisual_folder)

        image_urls = ["https://kumakumakumabear.com/core_sys/images/main/tz/main_img.jpg",
                      "https://kumakumakumabear.com/core_sys/images/main/tz/main_img_2.jpg",
                      "https://kumakumakumabear.com/core_sys/images/main/tz/main_img_3.jpg"]
        for image_url in image_urls:
            image_with_extension = self.extract_image_name_from_url(image_url, with_extension=True)
            if os.path.exists(keyvisual_folder + '/' + image_with_extension):
                continue
            image_without_extension = self.extract_image_name_from_url(image_url, with_extension=False)
            filepath_without_extension = keyvisual_folder + '/' + image_without_extension
            self.download_image(image_url, filepath_without_extension)


class MajotabiDownload(UnconfirmedDownload):
    title = "Majo no Tabitabi"
    keywords = [title, "Wandering Witch: The Journey of Elaina", "Majotabi"]

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/majotabi"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_key_visual()

    def download_key_visual(self):
        keyvisual_folder = self.base_folder + '/' + constants.FOLDER_KEY_VISUAL
        if not os.path.exists(keyvisual_folder):
            os.makedirs(keyvisual_folder)

        image_objs = [
            {'name': 'kv1', 'url': 'https://pbs.twimg.com/media/EHPjPtFU8AAHo9S?format=jpg&name=large'},
            {'name': 'kv2', 'url': 'https://pbs.twimg.com/media/ESahsP9UEAAhzgn?format=jpg&name=large'},
            {'name': 'kv3', 'url': 'https://pbs.twimg.com/media/EUqV9B7UcAAOCeE?format=jpg&name=medium'},
            {'name': 'kv4', 'url': 'https://pbs.twimg.com/media/EW64PYgUMAAGDIk?format=jpg&name=4096x4096'}]
        for image_obj in image_objs:
            if os.path.exists(keyvisual_folder + '/' + image_obj['name'] + '.png'):
                continue
            filepath_without_extension = keyvisual_folder + '/' + image_obj['name']
            self.download_image(image_obj['url'], filepath_without_extension)


# Tonikaku Kawaii
class TonikawaDownload(UnconfirmedDownload):
    title = "Tonikaku Kawaii"
    keywords = ["Tonikaku Kawaii", "Cawaii", "Fly Me to the Moon"]

    def __init__(self):
        super().__init__()
        self.base_folder = self.base_folder + "/tonikawa"
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

    def run(self):
        self.download_key_visual()

    def download_key_visual(self):
        keyvisual_folder = self.base_folder + '/' + constants.FOLDER_KEY_VISUAL
        if not os.path.exists(keyvisual_folder):
            os.makedirs(keyvisual_folder)

        image_objs = [
            {'name': 'w_teaser_1', 'url': 'https://pbs.twimg.com/media/EXzj-iYVcAElclE?format=jpg&name=large'},
            {'name': 'w_teaser_2', 'url': 'https://pbs.twimg.com/media/EXzj-iaU0AATNM7?format=jpg&name=large'},
            {'name': 'w_teaser_3', 'url': 'http://tonikawa.com/assets/images/common/news/news-1/img.jpg'}]
        for image_obj in image_objs:
            if os.path.exists(keyvisual_folder + '/' + image_obj['name'] + '.png') or \
                    os.path.exists(keyvisual_folder + '/' + image_obj['name'] + '.jpg'):
                continue
            filepath_without_extension = keyvisual_folder + '/' + image_obj['name']
            self.download_image(image_obj['url'], filepath_without_extension)

