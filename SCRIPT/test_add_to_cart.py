from PO.Home_page import HomePage
from PO.FishCategoryPage import FishCategoryPage
from PO.ProductListPage import ProductListPage
from PO.ProductDetailPage import ProductDetailPage
from PO.ShoppingCartPage import ShoppingCartPage


def test_add_to_cart(setup, login):  # login fixture
    driver = setup
    home_page = HomePage(driver)
    fish_category_page = FishCategoryPage(driver)
    product_list_page = ProductListPage(driver)
    product_detail_page = ProductDetailPage(driver)
    shopping_cart_page = ShoppingCartPage(driver)


    # Navigate to home page
    home_page.navigate_to_home_page()

    # Navigate to Fish Category
    home_page.click_fish_category()
    assert fish_category_page.is_at_fish_category()
    
    # Click on the product

    fish_category_page.click_product_by_name("Angelfish")
    assert product_list_page.is_at_product_list_for("Angelfish"), "Not at the Product List Page for Angelfish"


    # Add item to cart
    product_detail_page.add_to_cart()
    assert shopping_cart_page.is_title_matches()

    # Verify item added to cart
    assert shopping_cart_page.is_item_added()
