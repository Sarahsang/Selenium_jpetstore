from PO.Home_page import HomePage
from Data.data import USERNAME, PASSWORD


class TestLogout:

    def test_logout(self, setup):
        driver = setup
        home = HomePage(driver)
        
        # Navigate to Sign Out
        home.click_sign_out()
        
        # Verify if logged out successfully
        assert home.is_sign_in_displayed()
