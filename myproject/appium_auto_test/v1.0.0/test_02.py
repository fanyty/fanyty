from appium import webdriver
from time import sleep
from appium.options.android import UiAutomator2Options

# Desired Capabilities
desired_caps = {
    "platformName": "Android",
    "deviceName": "0351A08S04100153",
    "appPackage": "com.everysing.music.test",
    "appActivity": "com.chuhai.everysing.MainActivity",
    "automationName": "UiAutomator2"
}

# 启动 Appium 会话
options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options) # 启动app



# 等待应用启动
sleep(5)

# 登录输入框：	//android.view.View[@content-desc="By signing up, you agree to our & ."]/android.widget.EditText
# 登录按钮	//android.widget.Button[@content-desc="login"] 
# 房间按钮 /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView[4]
# 入口 	//android.view.View[@content-desc="Select a song"]/android.view.View[7]
# 关闭 Appium 会话
driver.quit()
