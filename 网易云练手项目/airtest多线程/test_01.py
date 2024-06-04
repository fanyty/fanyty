import threading
import subprocess
import os

def get_connected_devices():
    """
    获取已连接的设备列表
    """
    result = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE, text=True)
    devices = []
    for line in result.stdout.splitlines():
        if 'device' in line and 'devices' not in line:
            device_id = line.split()[0]
            devices.append(device_id)
    return devices

def run_test_on_device(device_id, script_path):
    """
    在指定设备上运行Airtest脚本
    """
    device = f"Android://127.0.0.1:5037/{device_id}"
    command = f"airtest run {script_path} --device {device}"
    subprocess.run(command, shell=True)

def run_tests_on_all_devices(script_path):
    """
    获取所有已连接设备，并在每个设备上并发运行Airtest脚本
    """
    devices = get_connected_devices()
    threads = []

    for device_id in devices:
        t = threading.Thread(target=run_test_on_device, args=(device_id, script_path))
        threads.append(t)

    # 启动所有线程
    for t in threads:
        t.start()

    # 等待所有线程完成
    for t in threads:
        t.join()

    print("所有测试完成")

# 指定Airtest脚本的绝对路径
script_path = r"C:\Users\admin\python\网易云练手项目\多人送礼_普通礼物.air"
# script_path = r"C:\Users\admin\python\网易云练手项目\房间_多人送礼_普通礼物.air"
# script_path = r"C:\Users\admin\python\网易云练手项目\房间_多人送礼_普通礼物_依次点击.air"

# 调用主函数运行测试
run_tests_on_all_devices(script_path)
