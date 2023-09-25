
from selenium import webdriver

class BaseSetup:

    @staticmethod
    def initialize_driver(browser="chrome"):
        if browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "firefox":
            driver = webdriver.Firefox()
        else:
            raise ValueError("Unsupported browser: {}".format(browser))
        
        driver.get("https://petstore.octoperf.com/actions/Catalog.action")
        driver.maximize_window()
        return driver
