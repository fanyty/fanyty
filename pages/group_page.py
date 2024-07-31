from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage

class GroupPage(BasePage):
    # 先点击项目，把群组拉出来 xpath定位：/html/body/div[1]/div[2]/div[2]/div/div/button/svg
    TOGGLE_PROJECT_BUTTON = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/button/svg")

    # 点击群组 xpath定位：/html/body/div[1]/div[1]/nav/div[2]/div[1]/div[4]/ul/li[2]/a/div[3]
    GROUP_NAV_BUTTON = (By.XPATH, "/html/body/div[1]/div[1]/nav/div[2]/div[1]/div[4]/ul/li[2]/a/div[3]")

    # 点击创建群组 xpath定位：//a[@data-testid='new-group-button']
    NEW_GROUP_BUTTON = (By.XPATH, "//a[@data-testid='new-group-button']")

    # 点击创建 css定位：html > body > div:nth-of-type(1) > div:nth-of-type(2) > div:nth-of-type(3) > main > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(2) > div > div:nth-of-type(1) > a > div:nth-of-type(2) > h3
    CREATE_GROUP_NAV_BUTTON = (By.CSS_SELECTOR, "html > body > div:nth-of-type(1) > div:nth-of-type(2) > div:nth-of-type(3) > main > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(2) > div > div:nth-of-type(1) > a > div:nth-of-type(2) > h3")

    # 输入群组名称 xpath定位：//*[@id='group_name']
    GROUP_NAME_INPUT = (By.XPATH, "//*[@id='group_name']")

    # 滑动浏览器页面 ，直到这个元素出现 js定位：document.querySelector("#group_jobs_to_be_done") 点击
    GROUP_JOBS_TO_BE_DONE = "document.querySelector('#group_jobs_to_be_done')"

    # 创建群组 button[data-testid='create-group-button'] span
    CREATE_GROUP_BUTTON = (By.CSS_SELECTOR, "button[data-testid='create-group-button'] span")

    def add_group(self, group_name):
        # 点击项目按钮展开群组
        self.click(*self.TOGGLE_PROJECT_BUTTON)

        # 点击群组导航按钮
        self.click(*self.GROUP_NAV_BUTTON)

        # 点击创建群组按钮
        self.click(*self.NEW_GROUP_BUTTON)

        # 点击创建导航按钮
        self.click(*self.CREATE_GROUP_NAV_BUTTON)

        # 输入群组名称
        self.send_keys(group_name, *self.GROUP_NAME_INPUT)

        # 滑动浏览器页面，直到群组任务出现
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.execute_script(self.GROUP_JOBS_TO_BE_DONE))

        # 点击群组任务
        self.driver.execute_script("arguments[0].click();", self.driver.execute_script(self.GROUP_JOBS_TO_BE_DONE))

        # 点击创建群组按钮
        self.click(*self.CREATE_GROUP_BUTTON)
