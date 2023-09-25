from selenium import webdriver

class BaseSetup:

    @staticmethod
    def initialize_driver(browser="chrome"):
        if browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "firefox":
            driver = webdriver.Firefox(executable_path="path/to/geckodriver")
        else:
            raise ValueError("Unsupported browser: {}".format(browser))
        
        driver.get("https://petstore.octoperf.com/actions/Catalog.action")
        driver.maximize_window()
        return driver


'''more:
Screenshot capabilities:For capturing screenshots automatically when a test fails.
'''