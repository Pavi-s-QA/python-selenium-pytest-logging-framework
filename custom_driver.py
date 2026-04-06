import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from conftest import *
class CustomDriver:
    def __init__(self, browser="chrome", headless=False):
        self.browser = browser
        self.headless = headless
        self.driver = self._init_driver()
        self.logger = logging.getLogger(__name__)

    def _init_driver(self):
        if self.browser == "chrome":
            options = webdriver.ChromeOptions()
            if self.headless:
                options.add_argument("--headless")
            return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        else:
            raise ValueError("Only Chrome is supported for now.")

    def get(self, url):
        self.logger.info(f"Navigating to {url}")
        self.driver.get(url)

    def find_element(self, by, value, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))
            self.logger.info(f"Element {value} found.")
            return element
        except TimeoutException:
            self.logger.error(f"Element {value} not found!")
            raise

    def click(self, by, value):
        self.find_element(by, value).click()
        self.logger.info(f"Clicked on element {value}.")

    def send_keys(self, by, value, text):
        self.find_element(by, value).send_keys(text)
        self.logger.info(f"Entered text '{text}' in {value}.")

    def is_visible(self, by, value, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by, value)))
            self.logger.info(f"Element {value} is visible.")
            return True
        except TimeoutException:
            self.logger.error(f"Element {value} not visible!")
            return False

    def quit(self):
        self.driver.quit()
        self.logger.info("Driver closed.")
