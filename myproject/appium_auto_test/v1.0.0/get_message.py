import subprocess

def get_device_info():
    # 获取设备ID
    result = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE)
    devices_output = result.stdout.decode('utf-8').strip().split('\n')
    device_id = devices_output[1].split()[0] if len(devices_output) > 1 else None
    
    if not device_id:
        raise Exception("No devices found")

    # 获取当前运行的应用包名和Activity
    result = subprocess.run(['adb', 'shell', 'dumpsys', 'window', '|', 'findstr', 'mCurrentFocus'], stdout=subprocess.PIPE, shell=True)
    current_focus_output = result.stdout.decode('utf-8').strip()
    if not current_focus_output:
        raise Exception("No running application found")
    
    package_activity = current_focus_output.split()[-1].strip().split('/')
    app_package = package_activity[0]
    app_activity = package_activity[1] if len(package_activity) > 1 else ''
    
    # 去掉Activity中的右括号
    if app_activity.endswith('}'):
        app_activity = app_activity[:-1]

    return {
        "platformName": "Android",
        "deviceName": device_id,
        "appPackage": app_package,
        "appActivity": app_activity,
        "automationName": "UiAutomator2"
    }

if __name__ == "__main__":
    device_info = get_device_info()
    print(device_info)
