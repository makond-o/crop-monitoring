import json
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from config.config import TestData


@pytest.fixture
def get_chrome_options():
    options = ChromeOptions()
    options.add_argument('chrome')
    options.add_argument('--start-fullscreen')
    options.add_argument('--new-window')
    return options


@pytest.fixture
def get_chrome_webdriver(get_chrome_options):
    options = get_chrome_options
    driver_location = 'chromedriver/chromedriver'
    driver = webdriver.Chrome(executable_path=driver_location, options=options)
    return driver


@pytest.fixture
def get_unregistered_email(request):
    with open('config/unregistered_email.json', 'r') as file:
        data = json.load(file)
    valid_email = data["User Name"] + data["Increment"] + data["Domain"]
    next_increment = str(int(data["Increment"]) + 1)
    data["Increment"] = next_increment
    with open('config/unregistered_email.json', 'w') as file:
        json.dump(data, file, indent=2)
    request.cls.valid_email = valid_email


@pytest.fixture()
def setup(request, get_chrome_webdriver):
    driver = get_chrome_webdriver
    url = TestData.BASE_URL
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.close()
    driver.quit()
