import pytest
from appium import webdriver
import time
class TestDW():
    def setup(self):
        desired_caps = {}
        # 跳过一些安装和权限的设置，可以大大提升脚本执行时间
        desired_caps["skipDeviceInitialization"] = "true"
        desired_caps["platformName"] = "Android"
        desired_caps["devicesName"] = "127.0.0.1:7555"
        desired_caps["appPackage"] = "com.xueqiu.android"
        desired_caps["appActivity"] = ".view.WelcomeActivityAlias"
        desired_caps["skipDeviceInitialization"] = "true"
        # 屏蔽弹窗
        desired_caps["noReset"] = "true"
        # 首次启动之后不关闭APP
        desired_caps["dontStopAppOnReset"] = "true"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        # 隐式等待五秒
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.back()
        self.driver.quit()
    def test_search(self):
        print("这是一条搜索用例")
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")

if __name__ == '__main__':
    pytest.main()