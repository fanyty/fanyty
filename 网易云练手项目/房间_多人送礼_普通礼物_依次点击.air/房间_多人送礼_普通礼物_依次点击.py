# -*- encoding=utf8 -*-
__author__ = "admin"

from airtest.core.api import *

auto_setup(__file__)



# from poco.drivers.android.uiautomation import AndroidUiautomationPoco
# poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
# for i in range(10):
#     touch(Template(r"tpl1717136282515.png", record_pos=(0.399, 0.912), resolution=(720, 1600)))
#     poco("android.widget.FrameLayout").child("android.view.View").child("android.view.View")[0].child("android.view.View").child("android.view.View").child("android.view.View")[2].child("android.view.View").child("android.view.View").child("android.view.View").offspring("20").child("android.widget.ImageView")[0].click
#     touch(Template(r"tpl1717136297107.png", record_pos=(0.361, 0.918), resolution=(720, 1600)))
for i in range(10):
    touch(Template(r"tpl1717136282515.png", record_pos=(0.399, 0.912), resolution=(720, 1600)))
    sleep(1)
    touch(Template(r"tpl1717136297107.png", record_pos=(0.361, 0.918), resolution=(720, 1600)))
