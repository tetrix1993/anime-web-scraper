import os
import shutil


# Migration Version 1
DOWNLOAD_DIR = 'download'
UNCONFIRMED_DIR = DOWNLOAD_DIR + '/unconfirmed'


def run():
    if not os.path.exists('download/unconfirmed'):
        os.makedirs(UNCONFIRMED_DIR)
    migrate_oregairu3()
    migrate_maohgakuin()
    migrate_rezero2()
    delete_empty_folders()


def migrate_oregairu3():
    old_dir = 'download/2020-2/oregairu3'
    if os.path.exists(old_dir):
        new_dir = UNCONFIRMED_DIR + '/oregairu3'
        shutil.move(old_dir, new_dir)


def migrate_maohgakuin():
    old_dir = 'download/2020-3/maohgakuin'
    if os.path.exists(old_dir):
        new_dir = UNCONFIRMED_DIR + '/maohgakuin'
        shutil.move(old_dir, new_dir)


def migrate_rezero2():
    old_dir = 'download/2020-3/rezero2'
    if os.path.exists(old_dir):
        new_dir = UNCONFIRMED_DIR + '/rezero2'
        shutil.move(old_dir, new_dir)


def delete_empty_folders():
    if os.path.exists(DOWNLOAD_DIR):
        items = os.listdir(DOWNLOAD_DIR)
        for item in items:
            item_dir = DOWNLOAD_DIR + '/' + item
            if os.path.isdir(item_dir):
                subitem = os.listdir(item_dir)
                if len(subitem) == 0:
                    os.rmdir(item_dir)


if __name__ == '__main__':
    run()
