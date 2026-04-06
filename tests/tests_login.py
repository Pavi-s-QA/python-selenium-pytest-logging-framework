import pytest
from custom_driver import CustomDriver
from pages.login_page import LoginPage
from conftest import *
@pytest.fixture
def driver():
    custom_driver = CustomDriver(headless=False)
    yield custom_driver
    custom_driver.quit()

def test_login(driver):
    # Arrange
    login_page = LoginPage(driver)
    username = "testuser"
    password = "testpass"

    # Act
    login_page.open()
    login_page.login(username, password)

    # Assert
    assert login_page.is_login_successful(), "Login failed!"
