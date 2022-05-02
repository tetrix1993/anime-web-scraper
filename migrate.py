import os
import shutil
import traceback
from anime import MainDownload, ExternalDownload
from anime.constants import FOLDER_OUTPUT

VERSION_NUMBER = 59
DOWNLOAD_DIR = 'download'
UNCONFIRMED_DIR = DOWNLOAD_DIR + '/unconfirmed'
MIGRATION_ERROR_LOG = 'migration_error.log'

VERSION_FILE = 'migrate_version'
MOVING_FOLDER_TEMPLATE = 'Moved folder %s to %s'
MOVING_FILE_TEMPLATE = 'Moved file %s to %s'

is_successful = True


def migrate_folders():
    migrate_folder_by_name('2020-2', '2020-3', 'oregairu3')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2020-3', 'oregairu3')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2020-3', 'maohgakuin')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2020-3', 'rezero2')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2020-3', 'hxeros')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2020-3', 'kanokari')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2020-3', 'mon-isha')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2020-3', 'petergrill')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2020-3', 'uzakichan')
    migrate_folder_by_name('2020-3', '2020-4', 'ochifuru')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2020-4', 'ochifuru')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2020-4', '100-man-no-inochi')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2020-4', 'danmachi3')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2020-4', 'gochiusa3')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2020-4', 'higurashi2020')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2020-4', 'iwakakeru')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2020-4', 'kamisama-ni-natta-hi')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2020-4', 'kamihiro')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2020-4', 'kimisen')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2020-4', 'kumabear')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2020-4', 'mahouka2')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2020-4', 'majotabi')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2020-4', 'maoujo')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2020-4', 'rail-romanesque')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2020-4', 'sigrdrifa')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2020-4', 'tonikawa')
    migrate_folder_by_name('2020-4', '2021-1', 'lasdan')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2021-1', 'lasdan')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2021-1', 'gotoubun2')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2021-1', 'kakushi-dungeon')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2021-1', 'mushoku-tensei')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2021-1', 'kaiyari')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2021-2', 'nagatoro-san')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2021-2', 'higehiro')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2021-3', 'cheat-kusushi')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2021-2', 'shadows-house')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2021-3', 'maidragon2')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2021-2', 'osamake')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2021-2', 'seijyonomaryoku')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2022-2', 'tate-no-yuusha2')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2021-3', 'bokurema')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2021-3', 'tanmoshi')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2021-3', 'shinnonakama')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2021-3', 'kanokano')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2021-3', 'seirei-gensouki')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2021-3', 'megamiryou')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2021-3', 'mahouka-yuutousei')
    migrate_folder_by_name('2021-3', '2021-4', 'shinnonakama')
    migrate_folder_by_name('2021-3', '2021-4', 'ansatsu-kizoku')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2022-1', 'slow-loop')
    migrate_folder_by_name('2021-4', '2022-2', 'tate-no-yuusha2')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2021-4', 'tsuki-laika-nosferatu')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2021-4', 'isekai-shokudo2')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2022-1', 'leadale')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2022-1', 'tensaiouji')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2022-1', 'priconne2')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2021-4', 'shuumatsu-no-harem')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2022-1', 'kendeshi')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2022-1', 'shikkakumon')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2022-3', 'hataraku-maousama2')
    migrate_folder_by_name('2021-4', '2022-1', 'shuumatsu-no-harem')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2022-2', 'spy-family')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2022-2', 'summertime-render')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2022-2', 'shokeishoujo')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2022-2', 'kunoichi-tsubaki')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2022-2', 'koiseka')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2022-2', 'kono-healer')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2022-2', 'kakkou-no-iinazuke')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2022-2', 'gaikotsukishi')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2022-2', 'deaimon')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2022-2', 'rpg-fudousan')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2022-2', 'shachisaretai')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2022-4', 'kyokou-suiri2')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2022-3', 'tenseikenja')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2022-4', 'kagenojitsuryoku')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2022-3', 'isekaiojisan')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2022-3', 'primadoll')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2022-3', 'kumichomusume')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2022-4', 'yamanosusume4')
    migrate_folder_by_name(UNCONFIRMED_DIR, '2022-3', 'tsurekano')
    migrate_folder_by_name('2022-4', '2023-1', 'kyokou-suiri2')
    # migrate_external_folder()


def rename_folders():
    rename_folder('download/2020-2/tamayomi/other', 'download/2020-2/tamayomi/bd')
    rename_folder('download/2020-2/hachinan/other', 'download/2020-2/hachinan/bd')
    rename_folder('download/2020-2/kaguya-sama2/other', 'download/2020-2/kaguya-sama2/bd')
    rename_folder('download/2020-2/shachibato/other', 'download/2020-2/shachibato/bd')

    rename_folder('download/2021-1/gotoubun2/bd', 'download/2021-1/gotoubun2/media')
    rename_folder('download/2021-1/horimiya/bd', 'download/2021-1/horimiya/media')
    rename_folder('download/2021-1/tomozakikun/bd', 'download/2021-1/tomozakikun/media')
    rename_folder('download/2021-1/kaiyari/bd', 'download/2021-1/kaiyari/media')
    rename_folder('download/2021-1/mushoku-tensei/bd', 'download/2021-1/mushoku-tensei/media')
    rename_folder('download/2021-1/non-non-biyori3/bd', 'download/2021-1/non-non-biyori3/media')
    rename_folder('download/2021-1/kakushi-dungeon/bd', 'download/2021-1/kakushi-dungeon/media')
    rename_folder('download/2021-1/lasdan/bd', 'download/2021-1/lasdan/media')
    rename_folder('download/2021-1/urasekai-picnic/bd', 'download/2021-1/urasekai-picnic/media')
    rename_folder('download/2021-1/wonder-egg-priority/bd', 'download/2021-1/wonder-egg-priority/media')
    rename_folder('download/2021-1/yurucamp2/bd', 'download/2021-1/yurucamp2/media')
    rename_folder('download/2021-2/yakumo/bd', 'download/2021-2/yakumo/media')

    rename_folder('download/2021-4/senpaiga-uzai', 'download/2021-4/senpaigauzai')


def do_other_tasks():
    move_kunoichi_tsubaki_audio_files()


def run():
    try:
        if is_latest_version():
            return
        print('Running migration script version ' + str(VERSION_NUMBER))
        if not os.path.exists(UNCONFIRMED_DIR):
            os.makedirs(UNCONFIRMED_DIR)
        if not os.path.exists(FOLDER_OUTPUT):
            os.makedirs(FOLDER_OUTPUT)
        migrate_to_output_folder()
        migrate_folders()
        rename_folders()
        do_other_tasks()
        delete_empty_folders()
        update_version()
        print('Migration completed.')
    except Exception as e:
        with open(MIGRATION_ERROR_LOG, 'a+') as f:
            f.write(traceback.format_exc())
        print('Migration failed. See error log - ' + MIGRATION_ERROR_LOG)


def is_latest_version():
    version = 0
    if os.path.exists(VERSION_FILE):
        with open(VERSION_FILE, 'r') as f:
            value = f.read()
        try:
            version = int(value)
        except:
            version = 0
    return version >= VERSION_NUMBER


def update_version():
    if is_successful:
        with open(VERSION_FILE, 'w+') as f:
            f.write(str(VERSION_NUMBER))


def migrate_folder(old_dir, new_dir):
    global is_successful
    if len(old_dir) > 9 and old_dir[0:9] != "download/":
        old_dir = DOWNLOAD_DIR + '/' + old_dir
    if len(new_dir) > 9 and new_dir[0:9] != "download/":
        new_dir = DOWNLOAD_DIR + '/' + new_dir
    if os.path.exists(old_dir):
        if os.path.exists(new_dir):
            print('Failed to migrate %s to %s - Folder to be migrated exists' % (old_dir, new_dir))
            is_successful = False
            return
        shutil.move(old_dir, new_dir)
        message = MOVING_FOLDER_TEMPLATE % (old_dir, new_dir)
        print(message)


def migrate_folder_by_name(old_dir, new_dir, name):
    migrate_folder(old_dir + '/' + name, new_dir + '/' + name)


def migrate_external_folder():
    for download in MainDownload.__subclasses__():
        if download is ExternalDownload:
            continue
        for sub_download in download.__subclasses__():
            dl = sub_download()
            base_folder = dl.base_folder
            exts = ['aniverse', 'moca', 'wnt']
            for ext in exts:
                for j in ['-', '_']:
                    folder = base_folder + j + ext
                    if os.path.exists(folder):
                        migrate_folder(folder, base_folder + '/' + ext)


def rename_folder(old_dir, new_dir):
    global is_successful
    if os.path.exists(old_dir):
        if os.path.exists(new_dir):
            print('Failed in renaming ' + old_dir + ' to ' + new_dir + ' - ' + new_dir + ' already exists.')
            is_successful = False
        else:
            try:
                os.rename(old_dir, new_dir)
                print('Renamed ' + old_dir + ' to ' + new_dir)
            except:
                is_successful = False


def delete_empty_folders():
    if os.path.exists(DOWNLOAD_DIR):
        items = os.listdir(DOWNLOAD_DIR)
        for item in items:
            item_dir = DOWNLOAD_DIR + '/' + item
            if os.path.isdir(item_dir):
                subitem = os.listdir(item_dir)
                if len(subitem) == 0:
                    os.rmdir(item_dir)
                    print('Removed empty folder ' + item_dir)


# Move all files in root directory ending with '.tsv' and '.xlsx'
def migrate_to_output_folder():
    global is_successful
    files = os.listdir()
    for file in files:
        if os.path.isfile(file) and (file.endswith('.tsv') or file.endswith('.xlsx')):
            old_dir = file
            new_dir = FOLDER_OUTPUT + '/' + file
            if os.path.exists(new_dir):
                print('Failed to migrate %s to %s - Folder to be migrated exists' % (old_dir, new_dir))
                is_successful = False
                return
            os.rename(old_dir, new_dir)
            message = MOVING_FILE_TEMPLATE % (old_dir, new_dir)
            print(message)


def move_kunoichi_tsubaki_audio_files():
    digicon_folder = 'download/2022-2/kunoichi-tsubaki/media/digicon'
    if os.path.exists(digicon_folder):
        countdown_voice_folder = 'download/2022-2/kunoichi-tsubaki/media/countdown-voice'
        if not os.path.exists(countdown_voice_folder):
            os.makedirs(countdown_voice_folder)
        files = os.listdir(digicon_folder)
        for file in files:
            if os.path.isfile(digicon_folder + '/' + file) and file.endswith('.wav'):
                old_filepath = digicon_folder + '/' + file
                new_filepath = countdown_voice_folder + '/' + file
                os.rename(old_filepath, new_filepath)
                message = MOVING_FILE_TEMPLATE % (old_filepath, new_filepath)
                print(message)


if __name__ == '__main__':
    run()
