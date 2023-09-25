from selenium.webdriver.common.by import By

class ProductDetailPage:

    def __init__(self, driver):
        self.driver = driver

        # Define locators for elements related to the Product Detail page
        self.return_to_product_link = (By.LINK_TEXT, "Return to FI-SW-01")
        self.add_to_cart_button = (By.XPATH, "//a[contains(@class, 'Button')]")

    def click_return_to_product(self):
        self.driver.find_element(*self.return_to_product_link).click()

    def click_add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()
