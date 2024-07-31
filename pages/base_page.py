from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config.config import Config
from config.logger import logger

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        try:
            logger.debug(f"Finding element with locator: {locator}")
            element = WebDriverWait(self.driver, Config.TIMEOUT).until(EC.visibility_of_element_located(locator))
            logger.debug(f"Element found: {locator}")
            return element
        except TimeoutException:
            logger.error(f"Timeout while finding element with locator: {locator}")
            raise
        except NoSuchElementException:
            logger.error(f"Element not found with locator: {locator}")
            raise

    def click(self, *locator):
        try:
            logger.debug(f"Clicking on element with locator: {locator}")
            element = self.find_element(*locator)
            element.click()
            logger.debug(f"Clicked on element with locator: {locator}")
        except Exception as e:
            logger.error(f"Error clicking on element with locator: {locator} - {e}")
            raise

    def send_keys(self, text, *locator):
        try:
            logger.debug(f"Sending keys '{text}' to element with locator: {locator}")
            element = self.find_element(*locator)
            element.clear()
            element.send_keys(text)
            logger.debug(f"Sent keys '{text}' to element with locator: {locator}")
        except Exception as e:
            logger.error(f"Error sending keys '{text}' to element with locator: {locator} - {e}")
            raise
