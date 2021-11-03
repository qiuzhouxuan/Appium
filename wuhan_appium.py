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
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

# 隐式等待五秒
driver.implicitly_wait(5)
driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]").click()
time.sleep(3)
# 返回到上一个页面
driver.back()
driver.quit()


