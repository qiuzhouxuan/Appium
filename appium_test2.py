"""
1打开雪球APP首页
2.定位首页搜索框
3.判断搜索框是否可用，并查看搜索框name属性值
4.打印搜索框这个元素的左上角坐标和他的宽高
5，向搜索框输入：alibaba
6,判断【阿里巴巴】是否可见
7，如果可见，打印“搜索成功”，如果不可见，打印【搜索失败】
"""
import pytest
from appium import webdriver
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
        desired_caps["unicodeKeyBoard"] = "true"
        desired_caps["resetKeyBoard"] = "true"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        # 隐式等待五秒
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.back()
        self.driver.quit()

    def test_attr(self):

        element = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(element.is_enabled())



if __name__ == '__main__':
    pytest.main()