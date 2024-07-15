# -*- encoding=utf8 -*-
__author__ = "admin"

from airtest.core.api import *

auto_setup(__file__)
touch(Template(r"tpl1717126117090.png", record_pos=(0.281, 0.812), resolution=(1080, 1920)))
if touch(Template(r"tpl1717126127575.png", record_pos=(0.371, 0.818), resolution=(1080, 1920))):
    for i in range(10):
        touch(Template(r"tpl1717126243695.png", record_pos=(0.381, 0.643), resolution=(1080, 1920)))

