import time

from appium import webdriver

desired_caps = {}
# 跳过一些安装和权限的设置，可以大大提升脚本执行时间
desired_caps["skipDeviceInitialization"]="true"
desired_caps["platformName"]="Android"
desired_caps["devicesName"]="127.0.0.1:7555"
desired_caps["appPackage"]="com.xueqiu.android"
desired_caps["appActivity"]=".view.WelcomeActivityAlias"
desired_caps["skipDeviceInitialization"]="true"
# 屏蔽弹窗
desired_caps["noReset"]="true"
# 首次启动之后不关闭APP
desired_caps["dontStopAppOnReset"]="true"