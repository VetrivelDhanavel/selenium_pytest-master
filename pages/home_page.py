from automation.testdata.testdata import TestData

class AlphaPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(TestData.CHROME_EXE_PATH)
