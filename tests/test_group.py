import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.config import Config
from config.logger import logger
from pages.login_page import LoginPage
from pages.group_page import GroupPage

@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--headless")  # 启用无头模式
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()

def test_add_group(driver):
    logger.info("Starting test: test_add_group")
    try:
        login_page = LoginPage(driver)
        group_page = GroupPage(driver)

        login_page.login(Config.USERNAME, Config.PASSWORD)
        group_page.add_group("Test Group")

        # 显式等待新创建的群组出现
        WebDriverWait(driver, Config.TIMEOUT).until(
            lambda d: "Test Group" in d.page_source
        )

        assert "Test Group" in driver.page_source
        logger.info("Completed test: test_add_group")
    except Exception as e:
        logger.error(f"Test failed: test_add_group - {e}")
        raise
