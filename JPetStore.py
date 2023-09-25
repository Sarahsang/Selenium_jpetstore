from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Initialize WebDriver
driver = webdriver.Chrome()

# Open JPetStore website
driver.get("https://petstore.octoperf.com/actions/Catalog.action")

# Confirm page title
assert "JPetStore" in driver.title

# Find the "Enter the Store" link and click it
enter_store_link = driver.find_element_by_link_text("Enter the Store")
enter_store_link.click()

# Close the browser
driver.quit()
