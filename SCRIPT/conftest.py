import pytest
from BaseSetup import BaseSetup  # import BaseSetup

@pytest.fixture(scope="module")
def setup():
    driver = BaseSetup.initialize_driver()  # use BaseSetup for WebDriver
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
