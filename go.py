from lib import log
from lib import aljazeera
from lib import helper

if __name__ == '__main__':
    log.set_custom_log_info('html/error.log')

    helper.verify_https_issue()

    aljazeera_scrap = aljazeera.Aljazeera(aljazeera.url_aj, log)

    if helper.check_cache(aljazeera.raw_html, aljazeera.CACHE):
        aljazeera_scrap.retrieve_webpage()
        aljazeera_scrap.write_webpage_as_html()

    aljazeera_scrap.read_webpage_as_html()
    aljazeera_scrap.convert_data_to_bs4()
    aljazeera_scrap.parse_soup_to_simple_html()
