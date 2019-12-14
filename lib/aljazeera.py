from urllib.request import urlopen
from bs4 import BeautifulSoup

from lib import helper

# Global Variables
CACHE = 3  # minutes
url_aj = 'http://www.aljazeera.com'
raw_html = 'html/aj.html'
output_html = 'html/simplenews.html'


class Aljazeera:
    _url = ''
    _data = ''
    _log = None
    _soup = None

    def __init__(self, url, log):
        self._url = url
        self._log = log

    def retrieve_webpage(self):
        try:
            html = urlopen(self._url)
        except Exception as e:
            print(e)
            self._log.report(str(e))
        else:
            self._data = html.read()
            if len(self._data) > 0:
                print("Retrieved Successfully")

    def write_webpage_as_html(self,
                              filepath=raw_html, data=''):
        if data == '':
            data = self._data
        helper.write_webpage_as_html(filepath, data)

    def read_webpage_as_html(self, filepath=raw_html):
        self._data = helper.read_webpage_from_html(filepath)

    def change_url(self, url):
        self._url = url

    def print_data(self):
        print(self._data)

    def convert_data_to_bs4(self):
        self._soup = BeautifulSoup(self._data, "html.parser")

    def parse_soup_to_simple_html(self):
        news_list = self._soup.find_all(
            ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])  # h1

        htmltext = '''
<html>
    <head><title>Simple News Link Scrapper</title></head>
    <body>{NEWS_LINK}</body>
</html>
'''
        news_links = '<ol>'

        for tag in news_list:
            if tag.parent.get('href'):
                #print (self._url + tag.parent.get('href'),tag.string)
                link = self._url + tag.parent.get('href')
                title = tag.string
                news_links += "<li><a href='{}'target='_blank'>{}</a></li>\n".format(
                    link, title)

        news_links += '</ol>'
        htmltext = htmltext.format(NEWS_LINK=news_links)

        self.write_webpage_as_html(
            filepath=output_html, data=htmltext.encode())

    def print_beautiful_soup(self):
        #print (self._soup.title.string)
        news_list = self._soup.find_all(['h1', 'h2', 'h4'])  # h1

        # print(news_list)
        for tag in news_list:
            if tag.parent.get('href'):
                print(self._url + tag.parent.get('href'), tag.string)
