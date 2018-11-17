#coding=utf-8
from selenium import webdriver
import time


profileDir = "/Users/geds/Library/Application Support/Firefox/Profiles/d17llgmb.default"
profile = webdriver.FirefoxProfile(profileDir)
profile.set_preference('extensions.blocklist.enabled','false')
dr = webdriver.Firefox(executable_path="/Users/geds/Documents/shzhyun/mashi/danmu/pyspl/driver/geckodriver", firefox_profile=profile)

# dr = webdriver.Chrome(executable_path="/Users/geds/Documents/shzhyun/mashi/danmu/pyspl/driver/chrome2.43/chromedriver")
# dr.maximize_window()
dr.get('https://www.huya.com')
#获得当前窗口的句柄
nowwhandle = dr.current_window_handle
time.sleep(20)
# 登录
dr.refresh()
time.sleep(3)
# send
li_s = dr.find_elements_by_tag_name("li")
# print(len(li_s))
# li_s[20].click()

i = 0
for l in li_s:
    li_s[i].click()
    time.sleep(5)
    dr.switch_to_active_element()
    # 切换窗口
    # 获取所有窗口的句柄
    allhandles = dr.window_handles
    # print len(allhandles)
    # 循环判断窗口是否为当前窗口
    for handle in allhandles:
        if handle != nowwhandle:
            dr.switch_to.window(handle)
            time.sleep(5)
            dr.find_element_by_css_selector(".ui-dialog-close").click()
            time.sleep(3)
            dr.refresh()
            time.sleep(5)
            try:
                dr.find_element_by_css_selector(".ui-dialog-close").click()
            except:
                print "error"
            time.sleep(5)
            dr.find_element_by_css_selector("#pub_msg_input").send_keys("666")
            time.sleep(5)
            try:
                dr.find_element_by_css_selector(".ui-dialog-close").click()
            except:
                print "error"
            dr.find_element_by_css_selector("#msg_send_bt").click()
            time.sleep(5)
            print "click send button"
            dr.close()
    # 返回原先到的窗口
    dr.switch_to_window(nowwhandle)


# print 'Browser will close'
# dr.quit()
# print 'Browser closed'
