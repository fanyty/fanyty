import threading
import subprocess

# 定义测试函数
def run_test(device):
    # 设置环境变量
    command = f"airtest run test_04.air --device {device}"
    subprocess.run(command, shell=True)

# 定义设备列表
devices = ["Android://127.0.0.1:5037/0351A08S04100153", "Android://127.0.0.1:5037/emulator-5554"]

# 创建线程
threads = []
for device in devices:
    t = threading.Thread(target=run_test, args=(device,))
    threads.append(t)

# 启动所有线程
for t in threads:
    t.start()

# 等待所有线程完成
for t in threads:
    t.join()

print("所有测试完成")
