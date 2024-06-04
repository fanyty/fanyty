# -*- encoding=utf8 -*-
__author__ = "admin"

from airtest.core.api import *

auto_setup(__file__)
touch(Template(r"tpl1717134671798.png", record_pos=(0.406, 0.821), resolution=(1080, 1920)))
if exists(Template(r"tpl1717134724217.png", record_pos=(-0.337, 0.691), resolution=(1080, 1920))):
    sleep(2)
    touch(Template(r"tpl1717134792875.png", record_pos=(0.361, 0.817), resolution=(1080, 1920)))
    for i in range(10):
        touch(Template(r"tpl1717134806582.png", record_pos=(0.37, 0.624), resolution=(1080, 1920)))
    

else:
    touch(Template(r"tpl1717134713769.png", record_pos=(-0.347, 0.812), resolution=(1080, 1920)))
    touch(Template(r"tpl1717134724217.png", record_pos=(-0.337, 0.691), resolution=(1080, 1920)))

    touch(Template(r"tpl1717134792875.png", record_pos=(0.361, 0.817), resolution=(1080, 1920)))
    for i in range(10):
        touch(Template(r"tpl1717134806582.png", record_pos=(0.37, 0.624), resolution=(1080, 1920)))
