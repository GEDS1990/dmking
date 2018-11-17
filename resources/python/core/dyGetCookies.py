#coding=utf-8
import json

from selenium import webdriver
import time
dr = webdriver.Firefox(executable_path=sys.path[0]+"/driver/geckodriver")
dr.maximize_window()
# cookieBefore = dr.get_cookies()
# 打印登录前的cookie
# print("cookieBefore:")
# print(cookieBefore)
# dr.add_cookie({'name':'_ga', 'value':'GA1.2.1706073692.1532175597'})
# dr.add_cookie({'name':'pgv_pvi', 'value':'1761107968'})
# dr.add_cookie({'name':'qcloud_uid', 'value':'94e00ef539956d42abea0abe0104e099'})
# dr.add_cookie({'name':'_ga', 'value':''})
# dr.add_cookie({'name':'tencent_uid', 'value':''})
dr.get('https://www.douyu.com')
print "-------------等待60s，手动登录斗鱼-----------------"
dr.implicitly_wait(3)
cookies = open(sys.path[0]+"/resources/dy/dy-cookies.txt").read()
# print(cookies)
cookiesAfter = eval(cookies)
len1 = len(cookiesAfter)
# print("len:%d" %len1)
i = 0
while(i < len1):
    print cookiesAfter[i]
    dr.add_cookie(cookiesAfter[i])
    i = i+1
dr.implicitly_wait(2)
cookiesAfter = dr.get_cookies()
print("cookiesAfter:")
print(cookiesAfter)
# f = open(sys.path[0]+"/resources/dy-cookies.txt",'wb')
# f.truncate()   #清空文件
# f.write(cookiesAfter)
# f.write(cookiesAfter)
# f.close()

# cookies = open(sys.path[0]+"/resources/dy-cookies.txt").read()
# dr.add_cookie(cookies)
# 登录
time.sleep(30)
# dr.find_element_by_class_name("pop-zoom-hide").click()
# time.sleep(3)
# dr.find_element_by_link_text("登录").click()
# time.sleep(3)
# dr.switch_to_frame("login-passport-frame")
# dr.find_element_by_xpath(".//*[@id='loginbox']/div[2]/div[1]/div[1]").click()
# time.sleep(3)
# dr.find_element_by_name("phoneNum").send_keys("13128641782")
# dr.find_element_by_name("password").send_keys("yang729")
# dr.find_element_by_xpath("//input[@value='登录']").click()
# dr.switch_to_default_content()



# print 'Browser will close'
# dr.quit()
# print 'Browser closed'
