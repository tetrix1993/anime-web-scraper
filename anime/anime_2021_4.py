import os
import anime.constants as constants
from anime.main_download import MainDownload, NewsTemplate, NewsTemplate2, NewsTemplate3
from datetime import datetime
from scan import AniverseMagazineScanner, MocaNewsScanner, WebNewtypeScanner


# Isekai Shokudou 2 https://isekai-shokudo2.com/ #異世界食堂 @nekoya_PR
# Kaizoku Oujo http://fena-pirate-princess.com/ #海賊王女 @fena_pirate
# Komi-san wa, Comyushou desu. https://komisan-official.com/ #古見さん #komisan @comisanvote
# Mieruko-chan https://mierukochan.jp/ #見える子ちゃん @mierukochan_PR
# Muv-Luv Alternative https://muv-luv-alternative-anime.com/ #マブラヴ #マブラヴアニメ #muvluv @Muv_Luv_A_anime
# Saihate no Paladin https://farawaypaladin.com/ #最果てのパラディン #faraway_paladin @faraway_paladin
# Sekai Saikou no Ansatsusha, Isekai Kizoku ni Tensei suru https://ansatsu-kizoku.jp/ #暗殺貴族 @ansatsu_kizoku
# Senpai ga Uzai Kouhai no Hanashi https://senpaiga-uzai-anime.com/ #先輩がうざい後輩の話 @uzai_anime
# Shin no Nakama ja Nai to Yuusha no Party wo Oidasareta node, Henkyou de Slow Life suru Koto ni Shimashita https://shinnonakama.com/ #真の仲間 @shinnonakama_tv
# Shinka no Mi: Shiranai Uchi ni Kachigumi Jinsei https://www.shinkanomi-anime.com/ #進化の実 #勝ち組人生 #ゴリラ系女子 @shinkanomianime
# Shuumatsu no Harem https://end-harem-anime.com/ #終末のハーレム @harem_official_
# Taishou Otome Otogibanashi http://taisho-otome.com/ #大正オトメ #昭和オトメ @otome_otogi
# Tsuki to Laika to Nosferatu https://tsuki-laika-nosferatu.com/ #月とライカ @LAIKA_anime
# Yuuki Yuuna wa Yuusha de Aru: Dai Mankai no Shou https://yuyuyu.tv/season2/ #yuyuyu @anime_yukiyuna


# Fall 2021 Anime
class Fall2021AnimeDownload(MainDownload):
    season = "2021-4"
    season_name = "Fall 2021"
    folder_name = '2021-4'

    def __init__(self):
        super().__init__()


# Isekai Shokudou 2
class IsekaiShokudou2Download(Fall2021AnimeDownload, NewsTemplate3):
    title = 'Isekai Shokudou 2'
    keywords = [title, 'Restaurant to Another World']
    website = 'https://isekai-shokudo2.com/'
    twitter = 'nekoya_PR'
    hashtags = '異世界食堂'
    folder_name = 'isekai-shokudo2'

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
        self.image_list = []
        # self.add_to_image_list('kv1', self.PAGE_PREFIX + 'assets/top/main-t1/vis.jpg')
        self.add_to_image_list('vis-t1', self.PAGE_PREFIX + 'assets/top/vis-t1/vis.jpg')
        self.download_image_list(folder)

        top_url = self.PAGE_PREFIX + 'assets/top/'
        try:
            for i in ['vis-kv%s', 'vis-ep%s']:
                for j in range(1, 100, 1):
                    image_name = i % str(j)
                    image_url = top_url + image_name + '/vis.jpg'
                    image_save_path = folder + '/' + image_name
                    if self.is_image_exists(image_name, folder):
                        continue
                    result = self.download_image(image_url, image_save_path)
                    if result == -1:
                        break
        except:
            pass

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/top/character/c%s.png'
        self.download_by_template(folder, template, 1)


# Kaizoku Oujo
class KaizokuOujoDownload(Fall2021AnimeDownload, NewsTemplate):
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
        if self.has_content(constants.FOLDER_CHARACTER):
            return

        folder = self.create_character_directory()
        template1 = self.PAGE_PREFIX + 'wp/wp-content/themes/fena-pirate-princess/_assets/images/char/detail/char_%s_pc.png'
        template2 = self.PAGE_PREFIX + 'wp/wp-content/themes/fena-pirate-princess/_assets/images/char/ss/char%s.jpg'
        self.download_by_template(folder, template1, 3, 1)
        self.download_by_template(folder, template2, 2, 1)
        template3 = self.PAGE_PREFIX + 'char/char%s-%s.jpg'
        i = 1
        while i <= 50 and self.download_by_template(folder, template3 % (str(i).zfill(2), '%s'), 1):
            i += 1


# Komi-san wa, Comyushou desu.
class KomisanDownload(Fall2021AnimeDownload, NewsTemplate):
    title = 'Komi-san wa, Comyushou desu.'
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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.news-item',
                                    date_select='span.news-item__date', title_select='span.news-item__title',
                                    id_select='a.news-item__link', a_tag_prefix=self.PAGE_PREFIX,
                                    a_tag_start_text_to_remove='/', next_page_select='a.next.page-numbers')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser_tw', 'https://pbs.twimg.com/media/E1GGa52UYAU7AJu?format=jpg&name=large')
        self.add_to_image_list('kv1', self.PAGE_PREFIX + 'news/wp/wp-content/uploads/2021/08/44a6f1c5db0201b8fa7afd6a5902c770.jpg')
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


# Mieruko-chan
class MierukochanDownload(Fall2021AnimeDownload, NewsTemplate3):
    title = 'Mieruko-chan'
    keywords = [title, 'Mieruko']
    website = 'https://mierukochan.jp/'
    twitter = 'mierukochan_PR'
    hashtags = '見える子ちゃん'
    folder_name = 'mierukochan'

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
        self.add_to_image_list('tz2_tw_1', 'https://pbs.twimg.com/media/E6aARStVcAMhcZB?format=jpg&name=medium')
        self.add_to_image_list('tz2_tw_2', 'https://pbs.twimg.com/media/E6aARTMVEAMu5YQ?format=jpg&name=medium')
        self.download_image_list(folder)

        top_template1 = self.PAGE_PREFIX + 'assets/top/t%s/vis-on.png'
        top_template2 = self.PAGE_PREFIX + 'assets/top/t%s/vis-off.png'
        self.download_by_template(folder, [top_template1, top_template2], 1, 1)

        news_template = self.PAGE_PREFIX + 'assets/news/vis-t%s.jpg'
        self.download_by_template(folder, news_template, 1, 1)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'assets/character/c/%s.png'
        self.download_by_template(folder, template, 1, 1, prefix='char_')


# Muv-Luv Alternative
class MuvLuvAlternativeDownload(Fall2021AnimeDownload, NewsTemplate):
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
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index', diff=2)

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='section.u-mg_b_l5 a',
                                    date_select='span.c-thumb-list__date', title_select='span.c-thumb-list__title',
                                    id_select=None, news_prefix='news/index.php?page=',
                                    paging_type=2, a_tag_prefix=news_url, a_tag_start_text_to_remove='./',
                                    next_page_select='i.i-arrows-angle-4-r')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('visual_1b', self.PAGE_PREFIX + 'img/home/visual_1b.jpg')
        self.download_image_list(folder)
        self.download_by_template(folder, self.PAGE_PREFIX + 'img/home/visual_%s.jpg', 1, 2)

    def download_character(self):
        folder = self.create_character_directory()
        self.image_list = []
        character_url = self.PAGE_PREFIX + 'character/'
        try:
            json_obj = self.get_json(character_url + 'chara_data.php')
            if 'charas' in json_obj and isinstance(json_obj['charas'], list):
                for chara in json_obj['charas']:
                    if 'images' in chara:
                        images = chara['images']
                        image_urls = []
                        if 'face' in images and isinstance(images['face'], str):
                            image_urls.append(character_url + images['face'])
                        if 'visuals' in images and isinstance(images['visuals'], list):
                            for visual in images['visuals']:
                                if 'image' in visual:
                                    image_urls.append(character_url + visual['image'])
                        for image_url in image_urls:
                            image_name = self.extract_image_name_from_url(image_url)
                            self.add_to_image_list(image_name, image_url)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)
        self.download_image_list(folder)


# Saihate no Paladin
class SaihatenoPaladinDownload(Fall2021AnimeDownload, NewsTemplate):
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
        self.download_news()
        self.download_key_visual()
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        news_url = self.PAGE_PREFIX + 'news/'
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='#news dd', date_select='i',
                                    title_select='span', id_select='a', a_tag_prefix=news_url)

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
        template2 = self.PAGE_PREFIX + 'img/main_c%s.png'
        self.download_by_template(folder, template2, 1)


# Sekai Saikou no Ansatsusha, Isekai Kizoku ni Tensei suru
class AnsatsuKizokuDownload(Fall2021AnimeDownload, NewsTemplate):
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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='div.news-Index li a',
                                    date_select='div.date', title_select='p', id_select=None,
                                    next_page_select='a.nextpostslink')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        #self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/Ev27c7bUUAIM_47?format=jpg&name=medium')
        #self.download_image_list(folder)
        template = self.PAGE_PREFIX + 'wp-content/themes/ansatsu-kizoku/assets/images/common/index/img_keyvisual_%s.jpg'
        self.download_by_template(folder, template, 1, 1)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp-content/themes/ansatsu-kizoku_teaser/assets/images/common/img_character_%s.png'
        self.download_by_template(folder, template, 1)


# Senpai ga Uzai Kouhai no Hanashi
class SenpaigaUzaiDownload(Fall2021AnimeDownload, NewsTemplate):
    title = 'Senpai ga Uzai Kouhai no Hanashi'
    keywords = [title]
    website = 'https://senpaiga-uzai-anime.com/'
    twitter = 'uzai_anime'
    hashtags = '先輩がうざい後輩の話'
    folder_name = 'senpaigauzai'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.foo',
                                    date_select='time', title_select='h3', id_select=None, id_has_id=True)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('main-visual', self.PAGE_PREFIX + 'img/top/main-visual.png')
        self.add_to_image_list('visual', 'https://pbs.twimg.com/media/Ez4yUbfVkAMPgny?format=jpg&name=4096x4096')
        self.add_to_image_list('mainimg', self.PAGE_PREFIX + 'images/top/mainimg.jpg')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/E8gG12BVkAEMaF_?format=jpg&name=large')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template1 = self.PAGE_PREFIX + 'images/character/img_chara_%s.png'
        template2 = self.PAGE_PREFIX + 'images/character/img_face_%s.png'
        self.download_by_template(folder, [template1, template2], 2, 1)


# Shin no Nakama ja Nai to Yuusha no Party wo Oidasareta node, Henkyou de Slow Life suru Koto ni Shimashita
class ShinnoNakamaDownload(Fall2021AnimeDownload, NewsTemplate):
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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ul.newsListsWrap li',
                                    date_select='p.update_time', title_select='p.update_ttl',
                                    id_select='a', a_tag_prefix=news_url, a_tag_start_text_to_remove='./')

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


# Shinka no Mi: Shiranai Uchi ni Kachigumi Jinsei
class ShinkanomiDownload(Fall2021AnimeDownload, NewsTemplate):
    title = 'Shinka no Mi: Shiranai Uchi ni Kachigumi Jinsei'
    keywords = [title, 'Shinkanomi']
    website = 'https://www.shinkanomi-anime.com'
    twitter = 'shinkanomianime'
    hashtags = ['進化の実', '勝ち組人生', 'ゴリラ系女子']
    folder_name = 'shinkanomi'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ul.news-list li.news-list__item',
                                    date_select='span.news-list__date', title_select='h2.news-list__title',
                                    id_select='a', next_page_select='div.pagination .page-numbers',
                                    next_page_eval_index_class='current', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/E52FLnzUcAEMg80?format=jpg&name=medium')
        self.add_to_image_list('kv1_1', self.PAGE_PREFIX + '/cms/wp-content/uploads/2021/08/2.jpg')
        self.add_to_image_list('kv1_2', self.PAGE_PREFIX + '/cms/wp-content/uploads/2021/08/3.jpg')
        self.add_to_image_list('kv2_1', self.PAGE_PREFIX + '/img/top/kv-ver2.jpg')
        self.add_to_image_list('kv2_2', self.PAGE_PREFIX + '/cms/wp-content/uploads/2021/09/KV2_.jpg')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + '/character/')
            images = soup.select('ul.character-list img')
            self.image_list = []
            for image in images:
                image_url = self.PAGE_PREFIX + image['src']
                image_name = self.extract_image_name_from_url(image_url)
                self.add_to_image_list(image_name, image_url)
            self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)


# Shuumatsu no Harem
class ShuumatsuNoHaremDownload(Fall2021AnimeDownload, NewsTemplate2):
    title = 'Shuumatsu no Harem'
    keywords = [title, "World's End Harem"]
    website = 'https://end-harem-anime.com/'
    twitter = 'harem_official_'
    hashtags = '終末のハーレム'
    folder_name = 'shuumatsu-no-harem'

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
        self.download_template_news(self.PAGE_PREFIX, 'news/list00010000.html')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('announce', 'https://pbs.twimg.com/media/EXzkif6VAAAxqJI?format=png&name=900x900')
        self.add_to_image_list('teaser', self.PAGE_PREFIX + 'core_sys/images/news/00000002/block/00000005/00000001.jpg')
        # self.add_to_image_list('teaser', 'https://pbs.twimg.com/media/EoYL6tMVgAADou1?format=jpg&name=large')
        # self.add_to_image_list('teaser_char', self.PAGE_PREFIX + 'core_sys/images/main/top/kv_char.png')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/E9Ma_mBVUAQoM9t?format=jpg&name=4096x4096')
        self.add_to_image_list('kv1_char', self.PAGE_PREFIX + 'core_sys/images/main/top/kv_char.png')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        cache_filepath = folder + '/cache'
        processed = []
        num_processed = 0
        if os.path.exists(cache_filepath):
            with open(cache_filepath, 'r', encoding='utf-8') as f:
                inputs = f.read()
            processed = inputs.split(';')
            num_processed = len(processed)

        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'character/reito.html')
            chara_list = soup.find('div', id='ContentsListUnit01')
            if chara_list:
                a_tags = chara_list.find_all('a')
                for a_tag in a_tags:
                    if a_tag.has_attr('href') and '/' in a_tag['href']:
                        chara_name = a_tag['href'].split('/')[-1].split('.html')[0]
                        if chara_name in processed:
                            continue
                        if chara_name == 'reito':  # First character
                            chara_soup = soup
                        else:
                            chara_soup = self.get_soup(self.PAGE_PREFIX + a_tag['href'].replace('../', ''))
                        self.image_list = []
                        divs = ['standWrap', 'faceWrap']
                        for div in divs:
                            wraps = chara_soup.find_all('div', class_=div)
                            for wrap in wraps:
                                if wrap:
                                    image = wrap.find('img')
                                    if image and image.has_attr('src'):
                                        image_url = self.PAGE_PREFIX + image['src'].replace('../', '')
                                        image_name = self.extract_image_name_from_url(image_url, with_extension=False)
                                        self.add_to_image_list(image_name, image_url)
                        self.download_image_list(folder)
                        processed.append(chara_name)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + " - Character")
            print(e)

        if len(processed) > num_processed:
            with open(cache_filepath, 'w+', encoding='utf-8') as f:
                for i in range(len(processed)):
                    if i > 0:
                        f.write(';')
                    f.write(processed[i])

    def download_media(self):
        folder = self.create_media_directory()
        self.image_list = []
        self.add_to_image_list('music_op', 'https://pbs.twimg.com/media/E9yvFCOUUAc43_i?format=jpg&name=large')
        self.download_image_list(folder)


# Taishou Otome Otogibanashi
class TaishoOtomeDownload(Fall2021AnimeDownload, NewsTemplate):
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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='ul.newslist li',
                                    date_select='div.newslist_date', title_select='h2.newslist_ttl', id_select='a',
                                    date_func=lambda x: x.replace('年', '.').replace('月', '.').replace('日', ''),
                                    next_page_select='li.pagination_list_item__next')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/taisho-otome/img/index/%s.jpg'
        template_name = 'img_kv%s'
        self.image_list = []
        self.add_to_image_list(template_name % '01', template % (template_name % '01'))
        self.add_to_image_list(template_name % '02', template % (template_name % '02'))
        self.add_to_image_list(template_name % '03', template % (template_name % '03'))
        self.add_to_image_list('kv03_tw', 'https://pbs.twimg.com/media/E5TLvmFVkAAV8Oj?format=jpg&name=medium')
        self.download_image_list(folder)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'wp/wp-content/themes/taisho-otome/img/character/img_chara%s.png'
        self.download_by_template(folder, template, 2)


# Tsuki to Laika to Nosferatu
class TsukiLaikaNosferatuDownload(Fall2021AnimeDownload, NewsTemplate):
    title = 'Tsuki to Laika to Nosferatu'
    keywords = [title]
    website = 'https://tsuki-laika-nosferatu.com/'
    twitter = 'LAIKA_anime'
    hashtags = '月とライカ'
    folder_name = 'tsuki-laika-nosferatu'

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
        self.download_template_news(page_prefix=self.PAGE_PREFIX, article_select='article.news-box',
                                    date_select='p.news-box-date', title_select='h3.news-box-ttl', id_select='a',
                                    next_page_select='ul.pagenation-list li',
                                    next_page_eval_index_class='is__current', next_page_eval_index=-1)

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        template = self.PAGE_PREFIX + 'Nr7R6svx/wp-content/themes/laika_tpl_v%s/assets/img/top/visual.jpg'
        self.add_to_image_list('teaser', template % '0')
        self.add_to_image_list('teaser_tw', 'https://pbs.twimg.com/media/EwpkNbsUUAAX00O?format=jpg&name=medium')
        self.add_to_image_list('kv1_tw', 'https://pbs.twimg.com/media/E6uztaAVUAU40vC?format=jpg&name=medium')
        self.download_image_list(folder)

        try:
            for i in range(20):
                image_url = template % str(i + 1)
                image_name = 'kv' + str(i + 1)
                result = self.download_image(image_url, folder + '/' + image_name)
                if result == -1:
                    break
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Key Visual')
            print(e)

    def download_character(self):
        folder = self.create_character_directory()
        template = self.PAGE_PREFIX + 'Nr7R6svx/wp-content/themes/laika_tpl_v1/assets/img/character/%s.png'
        self.download_by_template(folder, template, 1, 0, prefix='char_')

    def download_media(self):
        folder = self.create_media_directory()
        try:
            soup = self.get_soup(self.PAGE_PREFIX + 'products/cd')
            a_tags = soup.select('a.products-box-link')
            for a_tag in a_tags:
                if a_tag.has_attr('href'):
                    cover_image = a_tag.find('img')
                    if cover_image and cover_image.has_attr('src') and 'nowprinting' not in cover_image['src']:
                        cd_soup = self.get_soup(a_tag['href'])
                        if cd_soup:
                            images = cd_soup.select('#contents-main img')
                            self.image_list = []
                            for image in images:
                                if image.has_attr('src') and 'nowprinting' not in image['src']:
                                    image_url = image['src']
                                    image_name = self.extract_image_name_from_url(image_url)
                                    self.add_to_image_list(image_name, image_url)
                            self.download_image_list(folder)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Music')
            print(e)


# Yuuki Yuuna wa Yuusha de Aru: Dai Mankai no Shou
class Yuyuyu3Download(Fall2021AnimeDownload, NewsTemplate):
    title = "Yuuki Yuuna wa Yuusha de Aru: Dai Mankai no Shou"
    keywords = [title, "Yuyuyu", "Yuki Yuna is a Hero"]
    website = 'https://yuyuyu.tv/daimankai/'
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
        self.download_character()

    def download_episode_preview(self):
        self.has_website_updated(self.PAGE_PREFIX, 'index')

    def download_news(self):
        prefix = 'https://yuyuyu.tv'
        self.download_template_news(page_prefix=prefix, article_select='article.c-entry-item',
                                    date_select='span.c-entry-date', title_select='h1.c-entry-item__title',
                                    id_select='a', stop_date='2021.01.29', a_tag_prefix=prefix,
                                    next_page_select='a.next.page-numbers')

    def download_key_visual(self):
        folder = self.create_key_visual_directory()
        self.image_list = []
        self.add_to_image_list('tw_visual1', 'https://pbs.twimg.com/media/EeUu6NHVAAAqYgu?format=jpg&name=large')
        self.add_to_image_list('tw_visual2', 'https://pbs.twimg.com/media/E0L1PAhVEAICS7o?format=jpg&name=4096x4096')
        self.download_image_list(folder)
        self.download_by_template(folder, 'https://yuyuyu.tv/season2/img/home/visual_%s.jpg', 2, 10)
        self.download_by_template(folder, self.PAGE_PREFIX + 'img/home/visual_%s.jpg', 2, 1)

    def download_character(self):
        folder = self.create_character_directory()
        chara_url = self.PAGE_PREFIX + 'character/'
        self.image_list = []
        try:
            json_obj = self.get_json(chara_url + 'chara_data.php')
            if 'charas' in json_obj and isinstance(json_obj['charas'], list):
                for chara in json_obj['charas']:
                    if 'images' in chara and 'visuals' in chara['images'] and \
                            isinstance(chara['images']['visuals'], list):
                        for visual in chara['images']['visuals']:
                            if 'image' in visual:
                                image_url = chara_url + visual['image']
                                image_name = self.extract_image_name_from_url(image_url)
                                self.add_to_image_list(image_name, image_url)
        except Exception as e:
            print("Error in running " + self.__class__.__name__ + ' - Character')
            print(e)
        self.download_image_list(folder)
