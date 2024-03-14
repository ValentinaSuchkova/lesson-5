import pytest
from selene import browser


@pytest.fixture(autouse=True)
def browser_size():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.window_width = 1896
    browser.config.window_height = 1080
    browser.config.timeout = 12.0

    yield

    browser.quit()