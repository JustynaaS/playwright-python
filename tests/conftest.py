import pytest
from playwright.sync_api import Playwright

@pytest.fixture
def set_up(page): # page is a fixture from playwright
    # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # context = browser.new_context()
    # page = context.new_page()
    page.goto("https://google.com")

    yield page

    page.close()