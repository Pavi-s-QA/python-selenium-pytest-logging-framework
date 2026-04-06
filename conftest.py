import logging
import pytest

@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    logging.basicConfig(
        filename="file:///C:/Python-Selenium/Nov-11/Project1/logs/auto.log",
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )
    logging.info("Logging configured.")
