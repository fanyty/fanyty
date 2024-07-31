from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # 使用 CSS 定位符更新元素定位
    USERNAME_INPUT = (By.CSS_SELECTOR, "input[data-testid='username-field']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[data-testid='password-field']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-testid='sign-in-button'] span")

    def login(self, username, password):
        self.send_keys(username, *self.USERNAME_INPUT)
        self.send_keys(password, *self.PASSWORD_INPUT)
        self.click(*self.LOGIN_BUTTON)
