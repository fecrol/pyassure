from pyassure.webdriver import driver
from selenium.webdriver.common.by import By

class PageObject:

    LOCATOR_TYPES = {
        "class_name": By.CLASS_NAME,
        "css": By.CSS_SELECTOR,
        "id": By.ID,
        "link_text": By.LINK_TEXT,
        "name": By.NAME,
        "partial_link_text": By.PARTIAL_LINK_TEXT,
        "tag": By.TAG_NAME,
        "xpath": By.XPATH
    }

    def __init__(self):
        pass

    def __getattr__(self, locator):
        pass

    def get_driver(self):
        return driver.get_driver()
    
    def open(self, url=None):
        driver.open(url)