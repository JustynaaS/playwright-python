import os

from playwright.sync_api import expect
import pytest
import re

# PASSWORD = os.environ['PASSWORD']


@pytest.mark.smoke
def test_login_page(set_up, assert_snapshot):
    page = set_up
    expect(page).to_have_url(re.compile("google"))
    assert_snapshot(page.screenshot(full_page=True))
    # page.fill("input filed selector", os.environ['PASSWORD'])
