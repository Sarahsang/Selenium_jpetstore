
def test_login_fixture(setup, login):  # Note I added the `setup` fixture
    # Using setup (the WebDriver instance) to check for elements on the page
    assert "My Account" in setup.page_source, "Login was not successful"
