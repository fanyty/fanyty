import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.config import Config
from config.logger import logger
import os

@pytest.fixture(scope="session")
def browser():
    # 获取项目根目录
    project_root = os.path.abspath(os.path.dirname(__file__))
    # ChromeDriver 的路径
    chrome_driver_path = os.path.join(project_root, 'chromedriver.exe')

    options = Options()
    options.add_argument("--headless")  # 启用无头模式
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    # 使用指定的 ChromeDriver 路径
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def driver(browser):
    yield browser

@pytest.fixture(scope="session", autouse=True)
def setup_and_teardown():
    logger.info("Starting test session")
    yield
    logger.info("Ending test session")
