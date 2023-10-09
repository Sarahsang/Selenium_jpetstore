import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Data.data import USERNAME, PASSWORD

class TestModifyCart:

    @pytest.fixture(scope="function")
    def login(self, setup):
        #setup.get(self.base_url)
        
        # Navigate to login page
        login_button = WebDriverWait(setup, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Sign In"))
        )
        login_button.click()
        
        # Input username and password
        username_field = WebDriverWait(setup, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        username_field.send_keys(USERNAME)
        
        password_field = setup.find_element(By.NAME, "password")
        password_field.send_keys(PASSWORD)
        
        # Click login
        login_submit = setup.find_element(By.NAME, "signon")
        login_submit.click()
        yield
        # Logout
        logout_button = WebDriverWait(setup, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Sign Out"))
        )
        logout_button.click()

    def test_modify_cart_quantity(self, setup, login):
        # Navigate to cart
        cart_button = WebDriverWait(setup, 10).until(
            EC.element_to_be_clickable((By.NAME, "img_cart"))
        )
        cart_button.click()
        
        # Update the quantity of an item in the cart
        quantity_field = WebDriverWait(setup, 10).until(
            EC.presence_of_element_located((By.NAME, "EST-1"))
        )
        quantity_field.clear()
        quantity_field.send_keys("2")
        
        # Click update cart
        update_cart_button = setup.find_element(By.NAME, "updateCartQuantities")
        update_cart_button.click()
        
        # Verify the cart is updated
        updated_quantity = setup.find_element(By.NAME, "EST-1").get_attribute("value")
        assert updated_quantity == "2", f"Expected 2, got {updated_quantity}"
