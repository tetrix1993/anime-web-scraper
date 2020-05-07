import os
import shutil
import traceback

VERSION_NUMBER = 1
DOWNLOAD_DIR = 'download'
UNCONFIRMED_DIR = DOWNLOAD_DIR + '/unconfirmed'
MIGRATION_ERROR_LOG = 'migration_error.log'

VERSION_FILE = 'migrate_version'
MOVING_IMAGE_TEMPLATE = 'Moved folder %s to %s'

is_successful = True


def migrate_folders():
    migrate_folder('2020-2/oregairu3', UNCONFIRMED_DIR + '/oregairu3')
    migrate_folder('2020-3/maohgakuin', UNCONFIRMED_DIR + '/maohgakuin')
    migrate_folder('2020-3/rezero2', UNCONFIRMED_DIR + '/rezero2')


def run():
    print('Running migration script version ' + str(VERSION_NUMBER))
    try:
        if is_latest_version():
            return
        if not os.path.exists('download/unconfirmed'):
            os.makedirs(UNCONFIRMED_DIR)
        migrate_folders()
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
