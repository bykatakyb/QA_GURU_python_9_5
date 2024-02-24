import pytest
from selene import browser

@pytest.fixture(scope='function', autouse=True)
def browser_configs():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1600
    browser.config.window_height = 720

    yield
    browser.quit()