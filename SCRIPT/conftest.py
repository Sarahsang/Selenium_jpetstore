import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Data.data import USERNAME, PASSWORD
from Base.base import BaseSetup  # import BaseSetup if not already imported

@pytest.fixture(scope="module")
def setup():
    driver = BaseSetup.initialize_driver()  # use BaseSetup for WebDriver
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def login(setup):
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
