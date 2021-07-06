import os

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from sizolution.settings import FIREFOX_BINARY_PATH


def parse_site(url='https://freestylo.ru', tags='') -> dict:
    """ Парсинг html тегов
    :param url: str адрес ресурса
    :param tags: str теги, через запятую
    :return: dict словарь тегов
    """
    if __name__ != '__main__':
        gecko = os.path.normpath(
            os.path.join(os.path.dirname(__file__), 'geckodriver'))
        binary = FirefoxBinary(FIREFOX_BINARY_PATH)
        browser = webdriver.Firefox(firefox_binary=binary,
                                    executable_path=gecko + '.exe')
    else:
        browser = webdriver.Firefox()
    browser.get(url)
    soup = BeautifulSoup(browser.page_source, 'lxml')
    all_tags = {}
    for tag in soup.find_all():
        tag_name = tag.name
        if tag_name in all_tags:
            all_tags[tag_name] += 1
        else:
            all_tags[tag_name] = 1
    if tags:
        custom_tags = {}
        for tag in tags.split(','):
            custom_tags[tag] = all_tags[tag]
        return custom_tags
    return all_tags


if __name__ == '__main__':
    print(parse_site(url='https://django.radif.ru'))
    print(1)
