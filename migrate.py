import os
import shutil

VERSION_NUMBER = 1
DOWNLOAD_DIR = 'download'
UNCONFIRMED_DIR = DOWNLOAD_DIR + '/unconfirmed'

VERSION_FILE = 'migrate_version'
MOVING_IMAGE_TEMPLATE = 'Moved folder %s to %s'


def run():
    if is_latest_version():
        return
    print('Running migration script version ' + str(VERSION_NUMBER))
    if not os.path.exists('download/unconfirmed'):
        os.makedirs(UNCONFIRMED_DIR)
    migrate_oregairu3()
    migrate_maohgakuin()
    migrate_rezero2()
    delete_empty_folders()
    update_version()
    print('Migration completed.')


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
    with open(VERSION_FILE, 'w+') as f:
        f.write(str(VERSION_NUMBER))


def print_moving_message(old_dir, new_dir):
    message = MOVING_IMAGE_TEMPLATE % (old_dir, new_dir)
    print(message)


def migrate_oregairu3():
    old_dir = 'download/2020-2/oregairu3'
    if os.path.exists(old_dir):
        new_dir = UNCONFIRMED_DIR + '/oregairu3'
        shutil.move(old_dir, new_dir)
        print_moving_message(old_dir, new_dir)


def migrate_maohgakuin():
    old_dir = 'download/2020-3/maohgakuin'
    if os.path.exists(old_dir):
        new_dir = UNCONFIRMED_DIR + '/maohgakuin'
        shutil.move(old_dir, new_dir)
        print_moving_message(old_dir, new_dir)


def migrate_rezero2():
    old_dir = 'download/2020-3/rezero2'
    if os.path.exists(old_dir):
        new_dir = UNCONFIRMED_DIR + '/rezero2'
        shutil.move(old_dir, new_dir)
        print_moving_message(old_dir, new_dir)


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
