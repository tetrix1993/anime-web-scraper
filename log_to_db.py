import pyodbc
import anime.constants as constants
import os

# The server must have Microsoft SQL Server installed
# The database must exists in the SQL server.

server = ''
database = 'AnimeWebScraper'
connection_string = 'DRIVER={SQL Server};SERVER=%s;DATABASE=%s;Trusted_Connection=yes;' % (server, database)


def run():
    conn = pyodbc.connect(connection_string)
    init_db(conn)
    add_to_db(conn)


def init_db(conn):
    cursor = conn.cursor()
    create_table_query = '''
    IF NOT EXISTS
    (
        SELECT [name]
        FROM sys.tables
        WHERE [name] = 'DownloadLog'
    )
    CREATE TABLE DownloadLog (
        ObjectID UNIQUEIDENTIFIER PRIMARY KEY,
        LoggedDateTime DATETIME,
        BaseFolder NVARCHAR(255),
        FilePath NVARCHAR(255),
        FullPath NVARCHAR(255),
        ImageURL NVARCHAR(255),
        CreatedDateTime DATETIME
    )
    '''
    cursor.execute(create_table_query)
    conn.commit()


def add_to_db(conn):
    if not os.path.exists(constants.GLOBAL_DOWNLOAD_LOG_FILE):
        print('File %s not found' % constants.GLOBAL_DOWNLOAD_LOG_FILE)
        return
    with open(constants.GLOBAL_DOWNLOAD_LOG_FILE, 'r', encoding='utf-8') as f2:
        lines = f2.readlines()

    latest_date = get_latest_date(conn)
    processed = 0
    cursor = conn.cursor()
    for line in lines:
        split1 = line.split('\t')
        if len(split1) != 4:
            continue
        timestamp = split1[0]
        if latest_date and latest_date >= timestamp:
            continue
        base_folder = split1[1].replace(constants.FOLDER_DOWNLOAD + '/', '')
        split2 = base_folder.split('/')
        if len(split2) < 2:
            continue
        filepath = split1[2]
        if len(filepath) > 1 and filepath[0] == '/':
            filepath = filepath[1:]
        fullpath = base_folder + '/' + filepath
        url = split1[3].replace('\n', '')
        query = "INSERT INTO DownloadLog VALUES (NEWID(), '%s', '%s', '%s', '%s', '%s', GETDATE())"\
                % (timestamp, base_folder, filepath, fullpath, url)
        cursor.execute(query)
        processed += 1
    conn.commit()
    print('Records added: %s' % str(processed))


def get_latest_date(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT MAX(LoggedDateTime) FROM DownloadLog')
    for row in cursor:
        if row[0] is None:
            return None
        else:
            return str(row[0])


if __name__ == "__main__":
    run()
