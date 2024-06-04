对于Web UI自动化测试，使用Selenium和webdriver_manager来管理ChromeDriver是很常见的。为了避免 AttributeError: 'str' object has no attribute 'capabilities' 错误，可以参考以下代码示例：

安装必要的库：

shell
复制代码
pip install selenium webdriver-manager
使用以下代码进行测试：

python
复制代码
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 设置ChromeDriver服务
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

# 打开Google主页并打印标题
browser.get('http://www.google.com')
print(browser.title)

# 关闭浏览器
browser.quit()
关键点：
安装和导入库：确保你已安装并正确导入selenium和webdriver_manager。
使用Service类：确保ChromeDriverManager().install()返回的路径被正确传递给webdriver.Chrome()。
这个方法应该能有效避免你遇到的错误。