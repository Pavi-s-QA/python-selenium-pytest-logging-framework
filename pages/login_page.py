from selenium.webdriver.common.by import By
import logging
from conftest import *
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        
        self.url = "file:///C:/Python-Selenium/Nov-11/Project1/test.html"  # Update this path
        self.username_field = (By.ID, "username")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "loginBtn")
        self.welcome_msg = (By.ID, "welcomeMsg")
        self.logger = logging.getLogger(__name__)

    def open(self):
        self.driver.get(self.url)
        self.logger.info("Opened login page.")

    def login(self, username, password):
        self.driver.send_keys(*self.username_field, text=username)
        self.driver.send_keys(*self.password_field, text=password)
        self.driver.click(*self.login_button)
        self.logger.info("Login button clicked.")

    def is_login_successful(self):
        result = self.driver.is_visible(*self.welcome_msg)
        if result:
            self.logger.info("Login successful.")
        else:
            self.logger.warning("Login failed.")
        return result
