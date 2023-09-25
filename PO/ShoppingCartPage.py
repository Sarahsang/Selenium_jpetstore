from selenium.webdriver.common.by import By

class ShoppingCartPage:

    def __init__(self, driver):
        self.driver = driver

        # Define locators for elements related to the ShoppingCartPage
        self.return_to_main_menu_link = (By.LINK_TEXT, "Return to Main Menu")
        self.proceed_to_checkout_button = (By.LINK_TEXT, "Proceed to Checkout")
        self.remove_item_button = (By.LINK_TEXT, "Remove")
        self.update_cart_button = (By.NAME, "updateCartQuantities")
        self.quantity_input = (By.NAME, "EST-1")

    def click_return_to_main_menu(self):
        self.driver.find_element(*self.return_to_main_menu_link).click()

    def click_proceed_to_checkout(self):
        self.driver.find_element(*self.proceed_to_checkout_button).click()

    def click_remove_item(self):
        self.driver.find_element(*self.remove_item_button).click()

    def click_update_cart(self):
        self.driver.find_element(*self.update_cart_button).click()

    def set_quantity(self, quantity):
        self.driver.find_element(*self.quantity_input).clear()
        self.driver.find_element(*self.quantity_input).send_keys(quantity)
