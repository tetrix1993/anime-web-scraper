import datetime
from aniverse_guess import run


if __name__ == '__main__':
    timenow = datetime.datetime.now() + datetime.timedelta(hours=1)
    year = timenow.strftime('%Y')
    month = timenow.strftime('%m')
    run(year, month)
