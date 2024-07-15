# -*- encoding=utf8 -*-
__author__ = "admin"

from airtest.core.api import *

auto_setup(__file__)
# -*- encoding=utf8 -*-
__author__ = "llw"

from airtest.core.api import *

auto_setup(__file__)

elements = [
    Template(r"tpl1716569113646.png", record_pos=(-0.317, -0.051), resolution=(1440, 3200)),
    Template(r"tpl1716569129959.png", record_pos=(-0.096, -0.061), resolution=(1440, 3200)),
    Template(r"tpl1716569420447.png", record_pos=(0.102, -0.055), resolution=(1440, 3200)),
    Template(r"tpl1716569435898.png", record_pos=(0.326, -0.079), resolution=(1440, 3200)),
    Template(r"tpl1716569449634.png", record_pos=(-0.31, 0.269), resolution=(1440, 3200)),
    Template(r"tpl1716569460334.png", record_pos=(-0.105, 0.274), resolution=(1440, 3200)),
    Template(r"tpl1716569474790.png", record_pos=(0.113, 0.263), resolution=(1440, 3200)),
    Template(r"tpl1716569485715.png", record_pos=(0.328, 0.278), resolution=(1440, 3200))



    
]


loop_count = 50

for element in elements:
    # 打印当前进行到的次数
    for i in range(loop_count):
        print(f"循环次数：{i + 1}")

        # 等待两个模板之一出现
        while not (exists(Template(r"tpl1716635473487.png", record_pos=(-0.035, 0.271), resolution=(1080, 1920)))):
            print("等待模板出现...")
#             sleep(1)  # 每秒检查一次

        # 模板之一出现，等待5秒
#         print("模板之一出现，等待20秒...")

        sleep(6)
        
        # 点击元素
        print("点击元素")
        touch(element)
        
        
        
        
        

#     while  exists(Template(r"tpl1716568382996.png", record_pos=(-0.008, -0.426), resolution=(1440, 3200))):
#         if time.time() - start_time > timeout:
#             print("等待超时，未找到模板")
#             break
#         else:
#             print("等待模板出现...")
#             sleep(1)
#开始时间:12:00 -12：30
# case 30分钟 30局 12:00 -12：30
#case  12:37 60分钟 60局 
#case  12:50
# 设置要循环的次数
# loop_count = 50
# #40s的时候点击 
# for element in elements:
#         #打印当前进行到的次数
#     for i in range(loop_count):
        
#         while not exists(exists(Template(r"tpl1716628851540.png", record_pos=(-0.004, -0.477), resolution=(1080, 1920))) or exists(Template(r"tpl1716628910237.png", record_pos=(-0.008, -0.47), resolution=(1080, 1920))):
#                   sleep(5)
#                   touch(element)
# )

        

