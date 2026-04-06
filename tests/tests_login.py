import pytest
from custom_driver import CustomDriver
from pages.login_page import LoginPage
@pytest.fixture
def driver():
    custom_driver = CustomDriver(headless=True)
    yield custom_driver
    custom_driver.quit()

def test_login(driver):
    # Arrange
    login_page = loginPage(driver)
    username = "testuser"
    password = "testpass"

    # Act
    login_page.open()
    login_page.login(username, password)

    # Assert
    assert login_page.is_login_successful(), "Login failed!"
