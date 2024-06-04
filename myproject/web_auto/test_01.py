from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
# 设置ChromeDriver服务
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

# 打开Google主页并打印标题
browser.get('http://www.google.com')

time.sleep(5)
print(browser.title)

# 关闭浏览器
browser.quit()
