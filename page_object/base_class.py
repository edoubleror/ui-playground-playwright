from playwright.sync_api import Page
from enums.urls import Urls
import cfg


class BaseClass:
    def __init__(self, page: Page):
        self.page = page
        self.__url: Urls = Urls.URL_PAGE_HOME

    def set_url(self, url: Urls):
        self.__url = url

    def navigate(self):
        self.page.goto(url=f'{cfg.BASE_URL}/{self.__url.value}')
        return self
