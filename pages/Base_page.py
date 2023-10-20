"""This class i sparent of all the pages
Its contains all the Generic method s and utilities for all the pages"""
from telnetlib import EC

from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __int__(self, driver):
        self.driver = driver

    def click_element(self, by, value):
        element = self.driver.find_element(by, value)
        element.click()

    def enter_text(self, by, value, text):
        element = self.driver.find_element(by, value)
        element.clear()
        element.send_keys(text)

    def get_element_text(self, by, value):
        element = self.driver.find_element(by, value)
        return element.text

    def get_page_title(self):
        return self.driver.title

    def is_element_visible(self, by, value):
        elements = self.driver.find_elements(by, value)
        return len(elements) > 0 and elements[0].is_displayed()

    def is_element_present(self, by, value):
        elements = self.driver.find_elements(by, value)
        return len(elements) > 0

    def wait_for_element_to_be_visible(self, by, value, timeout=10):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located((by, value)))

    def wait_for_element_to_be_clickable(self, by, value, timeout=10):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable((by, value)))

    def switch_to_frame(self, by, value):
        frame = self.driver.find_element(by, value)
        self.driver.switch_to.frame(frame)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)
