import pytest


@pytest.fixture(scope="function")
def browser_context_args(browser_context_args):
    """
    Переопределение глобальной фикстуры browser_context_args
    """
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
        "ignore_https_errors": True
    }


@pytest.fixture(scope="function", autouse=False)
def new_incognito_page(context):
    """
    Шаблон фабрики-фикстуры для использования функции _new_incognito_page несколько раз в одном тесте

    Parameters
    ----------
    context: Generator
        Фикстура "context" из pytest_playwright.
        Создает browser и затем на его основе создает context
        Подробнее о Pytest Plugin Fixtures https://playwright.dev/python/docs/test-runners

    Returns
    -------
    Функция возвращает функцию _browser_context, чтобы ею можно было воспользоваться несколько раз
    Подробнее о шаблоне фабрики-текстуры https://docs-python.ru/packages/frejmvork-pytest/shablon-fikstura-fabrika/
    """
    def _new_incognito_page():
        """
        Функция создает новую инкогнито-страницу внутри browser contexts
        На этой странице проводятся действия в рамках каждого теста

        Returns
        -------
        Функция возвращает новую инкогнито-страницу браузера (clean-slate environments)
        """
        return context.new_page()
    yield _new_incognito_page
