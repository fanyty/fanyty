
# solox version : >= 2.8.5
from solox.public.apm import AppPerformance  # pip install --upgrade --force-reinstall tidevice==0.9.7Monitor
from solox.public.common import Devices

d = Devices()
processList = d.getPid(deviceId='0351A08S04100153(RMX3231)', pkgName='com.everysing.music.test') # for android
print(processList) # ['{pid}:{packagename}',...]，一个app可能会有多个进程，如果需要指定pid，可以从这里获取

apm = AppPerformanceMonitor(pkgName='com.bilibili.app.in',platform='Android', deviceId='ca6bd5a5', surfaceview=True, 
                            noLog=False, pid=None, record=False, collect_all=False)
# apm = AppPerformanceMonitor(pkgName='com.bilibili.app.in', platform='iOS')
# surfaceview： 为False时是使用gfxinfo方式，需要在手机上设置：(手机开发者 - GPU渲染模式 - adb shell dumpsys gfxinfo)
# noLog : False (保存测试数据到log文件中)

# ************* 收集单个性能参数 ************* #
cpu = apm.collectCpu() # %
memory = apm.collectMemory() # MB
memory_detail = apm.collectMemoryDetail() # MB
network = apm.collectNetwork(wifi=True) # KB , wifi=False时是收集移动网络，手机要切换数据流量
fps = apm.collectFps() # HZ
battery = apm.collectBattery() # level:% temperature:°C current:mA voltage:mV power:w
gpu = apm.collectGpu() # % 只支持ios

# ************* 收集所有性能参数 ************* #
 
if __name__ == '__main__':  #必须要在__name__ == '__main__'里面执行
  apm = AppPerformanceMonitor(pkgName='com.bilibili.app.in',platform='Android', deviceId='ca6bd5a5', surfaceview=True, 
                              noLog=False, pid=None, record=False, collect_all=True, duration=0)
  # apm = AppPerformanceMonitor(pkgName='com.bilibili.app.in', platform='iOS',  deviceId='xxxx', noLog=False, record=False, collect_all=True, duration=0)
  #duration: 执行时长（秒），只有>0的时候才生效，=0时会持续执行
  #record: 是否录制
  apm.collectAll() # 结束会生成测试报告

# 在另外的python脚本中可以主动终止solox服务，无需等待设置的执行时长结束
from solox.public.apm import initPerformanceService  

initPerformanceService.stop()