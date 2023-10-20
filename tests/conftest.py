
import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():
    # Initialize the WebDriver (in this case, Chrome)
    driver = webdriver.Chrome()

    # Optional: Maximize the browser window
    driver.maximize_window()

    yield driver
    driver.quit()
