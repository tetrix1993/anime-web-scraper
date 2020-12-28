import os
import shutil
import traceback
from anime import MainDownload, ExternalDownload

VERSION_NUMBER = 13
DOWNLOAD_DIR = 'download'
UNCONFIRMED_DIR = DOWNLOAD_DIR + '/unconfirmed'
MIGRATION_ERROR_LOG = 'migration_error.log'

VERSION_FILE = 'migrate_version'
MOVING_IMAGE_TEMPLATE = 'Moved folder %s to %s'

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
    migrate_external_folder()


def rename_folders():
    rename_folder('download/2020-2/tamayomi/other', 'download/2020-2/tamayomi/bd')
    rename_folder('download/2020-2/hachinan/other', 'download/2020-2/hachinan/bd')
    rename_folder('download/2020-2/kaguya-sama2/other', 'download/2020-2/kaguya-sama2/bd')
    rename_folder('download/2020-2/shachibato/other', 'download/2020-2/shachibato/bd')


def run():
    try:
        if is_latest_version():
            return
        print('Running migration script version ' + str(VERSION_NUMBER))
        if not os.path.exists(UNCONFIRMED_DIR):
            os.makedirs(UNCONFIRMED_DIR)
        migrate_folders()
        rename_folders()
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
        message = MOVING_IMAGE_TEMPLATE % (old_dir, new_dir)
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


if __name__ == '__main__':
    run()
