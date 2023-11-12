import pytest

from page_object.progress_bar import ProgressBar


@pytest.mark.progress_bar
def test_progress_bar(new_incognito_page):
    context_page = new_incognito_page()
    page = ProgressBar(context_page).navigate()
    loading_percentage = 75

    page.start_button_click()
    while page.get_progress_bar_value() < 100:
        if page.get_progress_bar_value() == loading_percentage:
            page.stop_button_click()
            break

    assert page.get_result()['Result'] == 0
