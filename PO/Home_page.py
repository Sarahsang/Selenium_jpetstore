from selenium.webdriver.common.by import By
'''clicks in home page'''
class HomePage:

    def __init__(self, driver):
        self.driver = driver

        # Define locators for elements on the home page
        self.sign_in_link = (By.LINK_TEXT, "Sign In")
        self.sign_out_link = (By.LINK_TEXT, "Sign Out")
        self.login_button = (By.NAME, "signon")
        self.my_account_link = (By.LINK_TEXT, "My Account")
        self.search_box = (By.NAME, "keyword")
        self.search_button = (By.NAME, "searchProducts")


        # Categories
        self.fish_category = (By.XPATH, "//a[@href='/actions/Catalog.action?viewCategory=&categoryId=FISH']")
        self.dogs_category = (By.XPATH, "//a[@href='/actions/Catalog.action?viewCategory=&categoryId=DOGS']")
        self.cats_category = (By.XPATH, "//a[@href='/actions/Catalog.action?viewCategory=&categoryId=CATS']")
        self.reptiles_category = (By.XPATH, "//a[@href='/actions/Catalog.action?viewCategory=&categoryId=REPTILES']")
        self.birds_category = (By.XPATH, "//a[@href='/actions/Catalog.action?viewCategory=&categoryId=BIRDS']")

    def click_sign_in(self):
        self.driver.find_element(*self.sign_in_link).click()
    
    def click_sign_out(self):
        self.driver.find_element(*self.sign_out_link).click()
        
    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def click_my_account(self):
        self.driver.find_element(*self.my_account_link).click()

    def perform_search(self, keyword):
        self.driver.find_element(*self.search_box).send_keys(keyword)
        self.driver.find_element(*self.search_button).click()

    def click_fish_category(self):
        self.driver.find_element(*self.fish_category).click()

    def click_dogs_category(self):
        self.driver.find_element(*self.dogs_category).click()

    def click_cats_category(self):
        self.driver.find_element(*self.cats_category).click()

    def click_reptiles_category(self):
        self.driver.find_element(*self.reptiles_category).click()

    def click_birds_category(self):
        self.driver.find_element(*self.birds_category).click()

    def navigate_to_home_page(self):
        self.driver.get("https://petstore.octoperf.com/actions/Catalog.action")
        
    def click_sign_in(self):
        """
        Click the "Sign In" link on the home page.

        Raises:
            NoSuchElementException: If the "Sign In" link is not found.
        """
        try:
            self.driver.find_element(*self.sign_in_link).click()
        except Exception as e:
            print(f"Exception occurred while clicking 'Sign In': {e}")
            raise
    
    def is_sign_in_displayed(self):
        """
        Check if the "Sign In" link is displayed.

        Returns:
            bool: True if displayed, False otherwise.
        """
        try:
            return self.driver.find_element(*self.sign_in_link).is_displayed()
        except Exception as e:
            print(f"Exception occurred while checking if 'Sign In' is displayed: {e}")
            return False