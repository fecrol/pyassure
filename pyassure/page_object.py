from pyassure.webdriver import Webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import *
from selenium.webdriver.remote.webelement import WebElement

class PageObject(Webdriver):

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
        super().__init__()
        self.__timeout = 5
        self.__explicit_timeout = 10
        self.__implicit_timeout = 0

    def __getattr__(self, locator):

        if locator in self.find_by.keys():
            loc = (self.LOCATOR_TYPES.get(self.find_by.get(locator)[0]), self.find_by.get(locator)[1])

            try:
                WebDriverWait(self.get_driver(), self.__timeout).until(ec.presence_of_element_located(loc))
                WebDriverWait(self.get_driver(), self.__timeout).until(ec.visibility_of_element_located(loc))
            except (StaleElementReferenceException, NoSuchElementException, TimeoutException) as err:
                raise Exception(
                    f"{type(err).__name__} occured when trying to locate {locator} by {self.find_by.get(locator)[0].upper()} {self.find_by.get(locator)[1]}"
                    )

            return self.__get_web_element(loc)
        
        if locator in self.find_all.keys():
            loc = (self.LOCATOR_TYPES.get(self.find_all.get(locator)[0]), self.find_all.get(locator)[1])

            try:
                WebDriverWait(self.get_driver(), self.__timeout).until(ec.presence_of_element_located(loc))
                WebDriverWait(self.get_driver(), self.__timeout).until(ec.visibility_of_element_located(loc))
            except (StaleElementReferenceException, NoSuchElementException, TimeoutException) as err:
                raise Exception(
                    f"{type(err).__name__} occured when trying to locate {locator} by {self.find_all.get(locator)[0].upper()} {self.find_all.get(locator)[1]}"
                    )

            return self.__get_web_elements(loc)
    
    def __get_web_element(self, locator):
        """
        Return a WebElement located by a locator type and locator

        :param locator: tuple holidg the locator type and locator
        :type: tuple
        :returns: WebElement located by a locator type and locator
        :rtype: WebElement
        """

        element = self.get_driver().find_element(*locator)
        return element
    
    def __get_web_elements(self, locator):
        """
        Return a list of WebElements located by a locator type and locator

        :param locator: tuple holidg the locator type and locator
        :type: tuple
        :returns: a list of WebElements located by a locator type and locator
        :rtype: list[WebElements]
        """

        elements = self.get_driver().find_elements(*locator)
        return elements
    
    def click_on(self, webelement):
        webelement.click()

    def type_into(self, webelement, string):
        webelement.send_keys(string)
    
    def clear(self, webelement):
        webelement.clear()

    def get_text(self, webelement=None, webelements=None):
        """
        :param: webelement: A WebElement from which the text is to be extracted
        :type: WebElement
        :param: webelements: A list of WebElement elements from which test is to be extracted
        :type: list[WebElement]
        :returns: Text extracted from a WebElement, or a list of texts extracted from a list of WebElements
        :rtype: str or list[str]
        """

        if webelement is not None and webelements is not None:
            raise Exception(f"Found a value of {webelement} for the webelement parameter and a value of {webelements} for the webelements parameter. You can specify one or the other, but not both.")

        if webelements is not None:
            return [element.text for element in webelements]

        return webelement.text
