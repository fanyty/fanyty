# -*- encoding=utf8 -*-
__author__ = "admin"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir="C:/Users/admin/python/unitest脚本/登录-加入家族.air/unitest.log", devices=["android://127.0.0.1:5037/emulator-5554?",])

    
    

# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath="C:/Users/admin/python/unitest脚本/登录-加入家族.air/unitest.log")