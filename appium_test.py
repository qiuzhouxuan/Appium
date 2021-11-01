from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desire_cap = {
  "platformName": "android",
  "devicesName": "127.0.0.1:7555",
  "appPackage": "com.xueqiu.android",
  "appActivity": ".view.WelcomeActivityAlias",
    "noReset":True
}
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire_cap)
# 隐式等待
driver.implicitly_wait(5)
el2 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el2.click()
el3 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el3.send_keys("阿里巴巴")
el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]")
el4.click()
el1 = driver.find_element_by_xpath(
  "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView")
el1.click()

TouchAction(driver).press(x=437, y=329).move_to(x=428, y=983).release().perform()

TouchAction(driver).press(x=390, y=1264).move_to(x=415, y=311).release().perform()

TouchAction(driver).tap(x=755, y=677).perform()
TouchAction(driver).tap(x=381, y=1392).perform()
el3 = driver.find_element_by_id("com.xueqiu.android:id/scrollview")
el3.click()
TouchAction(driver).tap(x=191, y=1273).perform()
TouchAction(driver).tap(x=729, y=1396).perform()
TouchAction(driver).tap(x=78, y=1087).perform()
TouchAction(driver).tap(x=755, y=933).perform()
TouchAction(driver).tap(x=753, y=1327).perform()
TouchAction(driver).tap(x=758, y=330).perform()
 
