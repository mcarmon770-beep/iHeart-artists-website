import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def setup():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    driver_service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service, options=chrome_options)
    driver.maximize_window()

    yield driver
    driver.quit()
