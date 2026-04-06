# python-selenium-pytest-logging-framework
Advanced Python Selenium framework using Pytest &amp; Page Object Model. Features centralized logging, custom WebDriver wrappers, and automated HTML reporting with failure screenshots.
# Python Selenium Automation Framework with Pytest & Logging

A scalable web automation framework built with **Python**, **Selenium**, and **Pytest**. This project demonstrates industry best practices including the **Page Object Model (POM)**, centralized configuration via `conftest.py`, and advanced logging mechanisms.

## 🚀 Key Features
* **Page Object Model (POM):** Enhances test maintenance and reduces code duplication.
* **Custom Driver Wrapper:** A centralized `CustomDriver` class to handle synchronization (Explicit Waits) and logging automatically.
* **Comprehensive Logging:** Uses Python's `logging` module to generate `automation.log` with timestamps and log levels.
* **Data-Driven Testing:** Utilizes `@pytest.mark.parametrize` for testing multiple login scenarios (positive/negative).
* **Automatic Failure Recovery:** Captures screenshots automatically in the `logs/` folder when a test fails via `pytest_runtest_makereport`.
* **Professional Reporting:** Generates self-contained HTML reports using `pytest-html`.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Browser Automation:** Selenium WebDriver
* **Driver Management:** Webdriver-Manager (Auto-downloads ChromeDriver)
* **Test Runner:** Pytest
* **Reporting:** Pytest-HTML

## 📂 Project Structure
```text
project/
├── pages/             # Page Objects (UI Locators & Actions)
├── tests/             # Test Scripts
├── logs/              # Log files and failure screenshots
├── reports/           # Generated HTML Test Reports
├── custom_driver.py   # Selenium Wrapper with built-in logging
├── conftest.py        # Global Pytest fixtures and hooks
└── test.html          # Local HTML file for testing purposes
