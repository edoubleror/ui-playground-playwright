from page_object.base_class import BaseClass
from playwright.sync_api import Page
from enums.urls import Urls


class ClickPage(BaseClass):
    def __init__(self, page: Page):
        super().__init__(page)
        self.set_url(url=Urls.URL_PAGE_CLICK)

        """ ЛОКАТОРЫ """

        # кнопки
        self.__bad_button = self.page.locator('xpath=//button[@id="badButton"]')

    """ МЕТОДЫ ДЛЯ ВЗАИМОДЕЙСТВИЯ СО СТРАНИЦЕЙ """

    def bad_button_click(self):
        self.__bad_button.click()
