# GAMMA2用户中心登录模块
import time

from appium import webdriver
# def environment():
desired_caps = {}
# 跳过一些安装和权限的设置，可以大大提升脚本执行时间
desired_caps["skipDeviceInitialization"]="true"
desired_caps["platformName"]="Android"
desired_caps["devicesName"]="623060c0"
desired_caps["appPackage"]="ecarx.membercenter"
desired_caps["appActivity"]=".app.login.LoginActivity"
desired_caps["skipDeviceInitialization"]="true"
# 屏蔽弹窗
desired_caps["noReset"]="true"
# 首次启动之后不关闭APP
desired_caps["dontStopAppOnReset"]="true"
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

# 隐式等待五秒
driver.implicitly_wait(5)
from appium.webdriver.common.touch_action import TouchAction
# 找到用户名输入框并且点击
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.LinearLayout").click()
# 输入用户名
driver.find_element_by_id("ecarx.membercenter:id/et_account_number").send_keys("15527114645")
# 收起键盘
TouchAction(driver).tap(x=255, y=617).perform()
driver.implicitly_wait(5)
# 找到密码输入框
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout")
# 输入密码
driver.find_element_by_id("ecarx.membercenter:id/et_account_pwd").send_keys("qzx159357")
TouchAction(driver).tap(x=255, y=617).perform()
# 勾选用户注册协议
driver.find_element_by_id("ecarx.membercenter:id/cb_agreement").click()
# 点击登录
driver.find_element_by_id("ecarx.membercenter:id/btn_account_login").click()
time.sleep(3)
# 返回到上一个页面
# driver.back()
driver.quit()