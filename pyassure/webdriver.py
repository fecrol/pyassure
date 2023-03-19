import os
from pyassure.config.pyassure_config import pyassure_config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class Webdriver:

    def __init__(self):
        self.__pyassure_config = pyassure_config.get_data()
        self.__possible_drivers = ["chrome", "firefox", "edge"]
        self.__possible_driver_options = {"chrome": "chromeOptions", "firefox": "firefoxOptions", "edge": "edgeOptions"}
        self.__possible_headless_values = ["true", "false"]

        self.__driver = None
    
    def __set_driver_options(self, driver_type):
        """
        Return approporiate driver options object based on the driver type

        :param driver_type: type of webdriver being used
        :type driver_type: str
        :returns: options object
        :rtype: Options
        """

        if driver_type == "chrome":
            driver_options = ChromeOptions()
        if driver_type == "firefox":
            driver_options = FirefoxOptions()
        if driver_type == "edge":
            driver_options = EdgeOptions()
        
        return driver_options

    def __get_driver_options(self, driver_type):
        """
        Return driver options object with driver options from config file added

        :param driver_type: type of webdriver being used
        :type driver_type: str
        :returns: options object
        :rtype: Options
        """

        list_of_options = self.__pyassure_config.get("webdriver").get(self.__possible_driver_options.get(driver_type))
        list_of_options = [] if list_of_options is None else list_of_options
        headless_mode = self.__pyassure_config.get("webdriver").get("headless")
        headless_mode = False if headless_mode not in self.__possible_headless_values or headless_mode == "false" else True

        driver_options = self.__set_driver_options(driver_type)
        driver_options.headless = headless_mode

        for option in list_of_options:
            driver_options.add_argument(option)
        
        return driver_options
    
    def __set_driver(self):
        """
        Set the driver to the approporiate webdriver instances. Chrome is used as the default webdriver
        """

        driver_type = self.__pyassure_config.get("webdriver").get("driver")
        driver_type = "chrome" if driver_type not in self.__possible_drivers else driver_type

        driver_options = self.__get_driver_options(driver_type)

        if driver_type == "chrome":
            self.__driver = webdriver.Chrome(options=driver_options, service=ChromeService(ChromeDriverManager().install()))
        if driver_type == "firefox":
            self.__driver = webdriver.Firefox(options=driver_options, service=FirefoxService(GeckoDriverManager().install()))
        if driver_type == "edge":
            self.__driver = webdriver.Edge(options=driver_options, service=EdgeService(EdgeChromiumDriverManager().install()))
    
    def start(self):
        self.__set_driver()
    
    def stop(self):
        self.__driver.quit()
    
    def opne(self):
        self.__driver.get("https://www.saucedemo.com/")
        