import unittest
from base.base_setup import initialize_driver
from po.home_page import HomePage

class PetStoreTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = initialize_driver()
        self.driver.get("https://petstore.octoperf.com/actions/Catalog.action")
        self.home_page = HomePage(self.driver)

    def test_click_fish(self):
        self.home_page.click_fish_link()
        self.assertIn("Fish", self.driver.page_source)

    def tearDown(self):
        self.driver.close()
