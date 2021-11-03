import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestDW():
    def setup(self):
        desired_caps = {}
        # 跳过一些安装和权限的设置，可以大大提升脚本执行时间
        # desired_caps["skipDeviceInitialization"] = "true"
        desired_caps["platformName"] = "Android"
        desired_caps["devicesName"] = "623060c0"
        desired_caps["appPackage"] = "ecarx.membercenter"
        desired_caps["appActivity"] = ".app.login.LoginActivity"
        desired_caps["skipDeviceInitialization"] = "true"
        # 屏蔽弹窗
        desired_caps["noReset"] = "true"
        # 首次启动之后不关闭APP
        desired_caps["dontStopAppOnReset"] = "true"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        # 隐式等待五秒
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_login(self):
        print("这是一条搜索测试用例")
        # 找到用户名输入框并且点击
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.LinearLayout").click()
        # 输入用户名
        self.driver.find_element_by_id("ecarx.membercenter:id/et_account_number").send_keys("15527114645")
        # 收起键盘
        TouchAction(self.driver).tap(x=255, y=617).perform()
        self.driver.implicitly_wait(5)
        # 找到密码输入框
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout")
        # 输入密码
        self.driver.find_element_by_id("ecarx.membercenter:id/et_account_pwd").send_keys("qzx159357")
        TouchAction(self.driver).tap(x=255, y=617).perform()
        # 勾选用户注册协议
        self.driver.find_element_by_id("ecarx.membercenter:id/cb_agreement").click()
        # 点击登录
        self.driver.find_element_by_id("ecarx.membercenter:id/btn_account_login").click()


if __name__ == '__main__':
    pytest.main()