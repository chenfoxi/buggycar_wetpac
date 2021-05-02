"""
This module contains all common function, shared fixtures
"""

from selenium.webdriver import Chrome

import pytest

@pytest.fixture
def getBrowser():

    # local debug env
    browser = Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()