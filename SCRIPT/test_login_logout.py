from PO.Home_page import HomePage
from Data.data import USERNAME, PASSWORD


class TestLoginLogout:

    def test_login(self, setup):
        driver = setup
        home = HomePage(driver)
        
        # Navigate to Sign In page and log in
        home.click_sign_in()
        home.enter_username(USERNAME)
        home.enter_password(PASSWORD)
        home.click_login_button()
        
        # Verify if logged in successfully
        assert home.is_sign_out_displayed()
    
    def test_logout(self, setup):
        driver = setup
        home = HomePage(driver)
        
        # Navigate to Sign Out
        home.click_sign_out()
        
        # Verify if logged out successfully
        assert home.is_sign_in_displayed()
