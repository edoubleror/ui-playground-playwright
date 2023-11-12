import pytest

from page_object.click import ClickPage


@pytest.mark.click
def test_click(new_incognito_page):
    context_page = new_incognito_page()
    page = ClickPage(context_page).navigate()

    page.bad_button_click()
