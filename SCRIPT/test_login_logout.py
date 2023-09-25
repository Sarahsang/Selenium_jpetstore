
import pytest
from selenium import webdriver
from Base.base import Base
from PO.Home_page import HomePage
from Data.data import USERNAME, PASSWORD

@pytest.mark.usefixtures("setup")
class TestLoginLogout(Base):

    def test_login(self):
        self.driver.get(self.base_url)
        home = HomePage(self.driver)
        
        # Navigate to Sign In page and log in
        home.click_sign_in()
        home.enter_username(USERNAME)
        home.enter_password(PASSWORD)
        home.click_login_button()
        
        # Verify if logged in successfully
        assert home.is_sign_out_displayed()
    
    def test_logout(self):
        self.driver.get(self.base_url)
        home = HomePage(self.driver)
        
        # Navigate to Sign Out
        home.click_sign_out()
        
        # Verify if logged out successfully
        assert home.is_sign_in_displayed()
