# test_01.py
from appium import webdriver
from get_message import get_device_info
from time import sleep

# 获取设备信息
device_info = get_device_info()

# 打印设备信息（可选）
print(device_info)

# 使用设备信息配置 Desired Capabilities
desired_caps = {
    "platformName": device_info["platformName"],
    "deviceName": device_info["deviceName"],
    "appPackage": device_info["appPackage"],
    "appActivity": device_info["appActivity"],
    "automationName": device_info["automationName"]
}

# 启动 Appium 会话
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 等待应用启动
sleep(5)

# 示例操作，如点击一个按钮
button = driver.find_element_by_id("com.example:id/button")
button.click()

# 关闭 Appium 会话
driver.quit()
