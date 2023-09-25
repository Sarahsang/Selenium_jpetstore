from selenium.webdriver.common.by import By

class ProductListPage:

    def __init__(self, driver):
        self.driver = driver

        # Define locators for elements related to the Product List page
        self.return_to_category_link = (By.LINK_TEXT, "Return to FISH")
        self.item_links = (By.XPATH, "//div[@id='Catalog']//tr/td[1]/a")
        self.add_to_cart_buttons = (By.XPATH, "//div[@id='Catalog']//a[contains(@class, 'Button')]")

    def click_return_to_category(self):
        self.driver.find_element(*self.return_to_category_link).click()

    def click_item_by_id(self, item_id):
        elements = self.driver.find_elements(*self.item_links)
        for element in elements:
            if element.text == item_id:
                element.click()
                return

    def click_add_to_cart_by_item_id(self, item_id):
        elements = self.driver.find_elements(*self.item_links)
        for index, element in enumerate(elements):
            if element.text == item_id:
                self.driver.find_elements(*self.add_to_cart_buttons)[index].click()
                return
