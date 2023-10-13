from selenium import webdriver

class BaseSetup:

    @staticmethod
    def initialize_driver(browser="chrome"):
        if browser == "chrome":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            chrome_options.add_experimental_option('useAutomationExtension', False)
            chrome_options.add_argument("--disable-autofill-keyboard-accessory-view[8]")
            driver = webdriver.Chrome(options=chrome_options)
        elif browser == "firefox":
            driver = webdriver.Firefox()
        else:
            raise ValueError("Unsupported browser: {}".format(browser))
        
        driver.get("https://petstore.octoperf.com/actions/Catalog.action")
        driver.maximize_window()
        return driver


'''more:
Screenshot capabilities:For capturing screenshots automatically when a test fails.
'''