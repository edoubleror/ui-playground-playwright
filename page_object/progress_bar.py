from page_object.base_class import BaseClass
from playwright.sync_api import Page
from enums.urls import Urls


class ProgressBar(BaseClass):
    def __init__(self, page: Page):
        super().__init__(page)
        self.set_url(url=Urls.URL_PAGE_PROGRESS_BAR)

        """ ЛОКАТОРЫ """

        # кнопки
        self.__start_button = self.page.get_by_role(role='button', name='Start')
        self.__stop_button = self.page.get_by_role(role='button', name='Stop')

        # прогресс бары
        self.__progress_bar = self.page.get_by_role(role="progressbar")

        # текстовые элементы
        self.__result = self.page.locator('xpath=//p[@id="result"]')

    """ МЕТОДЫ ДЛЯ ВЗАИМОДЕЙСТВИЯ СО СТРАНИЦЕЙ """

    def start_button_click(self):
        self.__start_button.click()

    def stop_button_click(self):
        self.__stop_button.click()

    def get_progress_bar_value(self) -> int:
        return int(self.__progress_bar.get_attribute('aria-valuenow'))

    def get_result(self) -> dict:
        return dict((a.strip(), int(b.strip()))
                    for a, b in (element.split(':')
                                 for element in self.__result.inner_text().split(', ')))
