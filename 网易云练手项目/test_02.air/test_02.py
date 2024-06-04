# -*- encoding=utf8 -*-
__author__ = "llw"

from airtest.core.api import *

auto_setup(__file__)
# -*- encoding=utf8 -*-
__author__ = "llw"

from airtest.core.api import *

auto_setup(__file__)

# 设置要循环的次数
loop_count = 2

# 使用for循环执行测试步骤
# 定义等待模板出现的超时时间
timeout = 50  # 单位为秒

while not exists(Template(r"tpl1716568382996.png", record_pos=(-0.008, -0.426), resolution=(1440, 3200))):
    if time.time() - start_time > timeout:
        print("等待超时，未找到模板")
        break
    else:
        print("等待模板出现...")
        sleep(1)
if exists(Template(r"tpl1716568382996.png", record_pos=(-0.008, -0.426), resolution=(1440, 3200))):
    for i in range(loop_count):

        touch(Template(r"tpl1716566780814.png", record_pos=(-0.306, -0.036), resolution=(1440, 3200)))

        sleep(50)
        


ifexists(Template(r"tpl1716568382996.png", record_pos=(-0.008, -0.426), resolution=(1440, 3200))):
    for i in range(loop_count):
        touch(Template(r"tpl1716567524961.png", record_pos=(-0.094, -0.034), resolution=(1440, 3200)))

        sleep(50)
        
ifexists(Template(r"tpl1716568382996.png", record_pos=(-0.008, -0.426), resolution=(1440, 3200))):

    for i in range(loop_count):
        touch(Template(r"tpl1716567578931.png", record_pos=(0.119, -0.026), resolution=(1440, 3200)))
        sleep(50)

    
for i in range(loop_count):
    touch(Template(r"tpl1716567624511.png", record_pos=(0.325, -0.079), resolution=(1440, 3200)))
    sleep(50)
sleep(10)
for i in range(loop_count):
    touch(Template(r"tpl1716567659197.png", record_pos=(-0.304, 0.251), resolution=(1440, 3200)))
    sleep(50)
sleep(10)    
    
    
for i in range(loop_count):
    touch(Template(r"tpl1716567677527.png", record_pos=(-0.1, 0.256), resolution=(1440, 3200)))
    sleep(50)
sleep(10)
for i in range(loop_count):
    touch(Template(r"tpl1716567699603.png", record_pos=(0.115, 0.268), resolution=(1440, 3200)))
    sleep(50)
sleep(10)   
for i in range(loop_count):
    touch(Template(r"tpl1716567720560.png", record_pos=(0.335, 0.263), resolution=(1440, 3200)))
    sleep(50)



    
    