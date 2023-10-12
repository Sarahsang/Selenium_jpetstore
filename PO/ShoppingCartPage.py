from selenium.webdriver.common.by import By

class ShoppingCartPage:

    def __init__(self, driver):
        self.driver = driver

        # Define locators for elements related to the ShoppingCartPage
        self.return_to_main_menu_link = (By.LINK_TEXT, "Return to Main Menu")
        self.proceed_to_checkout_button = (By.LINK_TEXT, "Proceed to Checkout")
        self.remove_item_button = (By.LINK_TEXT, "Remove")
        self.update_cart_button = (By.NAME, "updateCartQuantities")

    def click_return_to_main_menu(self):
        self.driver.find_element(*self.return_to_main_menu_link).click()

    def click_proceed_to_checkout(self):
        self.driver.find_element(*self.proceed_to_checkout_button).click()

    def click_remove_item(self):
        self.driver.find_element(*self.remove_item_button).click()

    def click_update_cart(self):
        self.driver.find_element(*self.update_cart_button).click()

    def set_quantity(self, item_id, quantity):
        quantity_input = (By.NAME, item_id)
        self.driver.find_element(*quantity_input).clear()
        self.driver.find_element(*quantity_input).send_keys(quantity)

    def is_cart_empty(self):
        try:
            self.driver.find_element(By.XPATH, "//td[contains(text(), 'Your cart is empty.')]")
            return True
        except:
            return False

    def is_item_added(self, item_id):
        item_elements = self.driver.find_elements(By.XPATH, "//table//tr//td[1]")
        for item_element in item_elements:
            if item_element.text == item_id:
                return True
        return False

    def is_at_shopping_cart_page(self):
        try:
            self.driver.find_element(By.XPATH, "//h2[text()='Shopping Cart']")
            return True
        except:
            return False
