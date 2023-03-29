from pyassure.webdriver import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement

class PageObject():

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
        self.__driver = driver
        self.__timeout = 5
        self.__explicit_timeout = 10
        self.__implicit_timeout = 0

    def __getattr__(self, locator:tuple[str]):

        try:
            if locator in self.find_by.keys():
                loc = (self.LOCATOR_TYPES.get(self.find_by.get(locator)[0]), self.find_by.get(locator)[1])

                try:
                    WebDriverWait(self.get_driver(), self.__timeout).until(ec.presence_of_element_located(loc))
                    WebDriverWait(self.get_driver(), self.__timeout).until(ec.visibility_of_element_located(loc))
                except (StaleElementReferenceException, NoSuchElementException, TimeoutException) as err:
                    raise Exception(
                        f"{type(err).__name__} occured when trying to locate {locator} by {self.find_by.get(locator)[0].upper()} {self.find_by.get(locator)[1]}"
                        )

                webelement = self.__get_web_element(loc)
                webelement.locator = loc
                return webelement
        except:
            pass
        
        try:
            if locator in self.find_all.keys():
                loc = (self.LOCATOR_TYPES.get(self.find_all.get(locator)[0]), self.find_all.get(locator)[1])

                try:
                    WebDriverWait(self.get_driver(), self.__timeout).until(ec.presence_of_element_located(loc))
                    WebDriverWait(self.get_driver(), self.__timeout).until(ec.visibility_of_element_located(loc))
                except (StaleElementReferenceException, NoSuchElementException, TimeoutException) as err:
                    raise Exception(
                        f"{type(err).__name__} occured when trying to locate {locator} by {self.find_all.get(locator)[0].upper()} {self.find_all.get(locator)[1]}"
                        )

                webelements = self.__get_web_elements(loc)
                for webel in webelements:
                    webel.locator = loc

                return webelements
        except:
            pass
    
    def get_driver(self):
        return self.__driver.get_driver()
    
    def __get_web_element(self, locator:tuple[str]):
        """
        Return a WebElement located by a locator type and locator

        :param locator: tuple holidg the locator type and locator
        :type: tuple
        :returns: WebElement located by a locator type and locator
        :rtype: WebElement
        """

        element = self.get_driver().find_element(*locator)
        return element
    
    def __get_web_elements(self, locator:tuple[str]):
        """
        Return a list of WebElements located by a locator type and locator

        :param locator: tuple holidg the locator type and locator
        :type: tuple
        :returns: a list of WebElements located by a locator type and locator
        :rtype: list[WebElements]
        """

        elements = self.get_driver().find_elements(*locator)
        return elements
    
    def __element_not_present(self, webelement:WebElement):
        """
        Custom expected condition to check if element is no longer present on the screen
        """

        def predicate(_):
            webelements = self.get_driver().find_elements(*webelement.locator)
            if len(webelements) == 0:
                return True
            return False
        
        return predicate
    
    def open(self, url:str=None):
        self.__driver.open(url)
    
    def quit(self):
        self.__driver.quit()
    
    def click_on(self, webelement:WebElement):
        webelement.click()
    
    def right_click_on(self, webelement:WebElement):
        ActionChains(self.get_driver()).context_click(webelement).perform()

    def type_into(self, webelement:WebElement, string:str):
        webelement.send_keys(string)
    
    def clear(self, webelement):
        webelement.clear()

    def get_text(self, webelement:WebElement=None, webelements:list[WebElement]=None):
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
    
    def select_element_by_text(self, webelement:WebElement, text:str):
        select = Select(webelement)
        select.select_by_visible_text(text)

    def select_element_by_index(self, webelement:WebElement, index:int):
        select = Select(webelement)
        select.select_by_index(index)
    
    def select_element_by_value(self, webelement:WebElement, value:str):
        select = Select(webelement)
        select.select_by_value(value)
    
    def wait_until_present(self, webelement:WebElement):
        return WebDriverWait(self.get_driver(), self.__explicit_timeout).until(
            ec.presence_of_element_located(webelement.locator)
        )

    def wait_until_visible(self, webelement:WebElement):
        return WebDriverWait(self.get_driver(), self.__explicit_timeout).until(
            ec.visibility_of(webelement)
        )

    def wait_until_clickable(self, webelement:WebElement):
        return WebDriverWait(self.get_driver(), self.__explicit_timeout).until(
            ec.element_to_be_clickable(webelement)
        )

    def wait_until_not_present(self, webelement:WebElement):
        return WebDriverWait(self.get_driver(), self.__explicit_timeout).until(
            self.__element_not_present(webelement)
        )

    def wait_until_not_visible(self, webelement:WebElement):
        return WebDriverWait(self.get_driver(), self.__explicit_timeout).until(
            ec.invisibility_of_element(webelement)
        )

    def wait_for_staleness_of(self, webelement:WebElement):
        return WebDriverWait(self.get_driver(), self.__explicit_timeout).until(
            ec.staleness_of(webelement)
        )

class PageComponent(PageObject):

    def __init__(self):
        super().__init__()
