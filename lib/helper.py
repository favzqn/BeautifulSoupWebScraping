import os
import ssl
from lib import log

from datetime import datetime

# Https verify issue solution
# http://bit.ly/2KKXIQD


def verify_https_issue():
    if (not os.environ.get('PYTHONHTTPSVERIFY', '')
        and
            getattr(ssl,
                    '_create_unverified_context', None)):
        ssl._create_default_https_context = ssl._create_unverified_context


def write_webpage_as_html(filename, data=""):
    try:
        with open(filename, 'wb') as fobj:
            fobj.write(data)
    except Exception as e:
        print(e)
        log.report(e)
        return False
    else:
        return True


def read_webpage_from_html(filename):
    try:
        with open(filename) as fobj:
            data = fobj.read()
    except Exception as e:
        print(e)
        log.report(e)
        return False
    else:
        return data


def get_last_scraped_time(filename):
    if not os.path.exists(filename):
        return - 1  # File Doesn't Exist

    file_time = os.path.getmtime(filename)
    now = datetime.timestamp(datetime.now())
    diff = now - file_time
    minutes = int(round(diff / 60))
    return minutes


def check_cache(filename, cache_time):
    scraping_time = get_last_scraped_time(filename)

    if scraping_time < 0 or scraping_time > cache_time:
        return True

    return False
