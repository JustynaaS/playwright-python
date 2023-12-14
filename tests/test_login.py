from playwright.sync_api import Playwright, expect
import pytest
import re


@pytest.mark.smoke
def test_login_page(set_up):
    page = set_up
    expect(page).to_have_url(re.compile("google"))
