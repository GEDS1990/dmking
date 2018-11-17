#coding=utf-8
import re
import sys

from org.shzhyun.splider.common.dyHTMLParser import dyHTMLParser

reload(sys)
sys.setdefaultencoding('utf-8')

from selenium import webdriver
import time
resources = "/Users/geds/Documents/shzhyun/mashi/danmu/pyspl/resources/"
dr = webdriver.Firefox(executable_path="/Users/geds/Documents/shzhyun/mashi/danmu/pyspl/driver/geckodriver")
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
# print "-------------等待60s，手动登录斗鱼-----------------"
dr.implicitly_wait(3)
# 设置cookies
cookies = open(resources + "dy/dy-cookies.txt").read()
# print(cookies)
cookiesAfter = eval(cookies)
len1 = len(cookiesAfter)
# print("len:%d" %len1)
i = 0
while(i < len1):
    # print cookiesAfter[i]
    dr.add_cookie(cookiesAfter[i])
    i = i+1
dr.implicitly_wait(2)

elements = dr.find_elements_by_tag_name("a")
print "len:"+str(len(elements))
i = 0
while i < len(elements):
    try:
        href = str(elements[i].get_attribute("href"))
        # print str(href)
        if re.match('https://www.douyu.com/\d{1,8}\d$',href)!=None :
            dr.get('href')
            time.sleep(3)
            # 设置cookies
            cookies = open(resources + "dy/dy-cookies.txt").read()
            # print(cookies)
            cookiesAfter = eval(cookies)
            len1 = len(cookiesAfter)
            # print("len:%d" %len1)
            i = 0
            while (i < len1):
                # print cookiesAfter[i]
                dr.add_cookie(cookiesAfter[i])
                i = i + 1
            dr.implicitly_wait(2)
            print "elements:"+str(i)+":"+str(href)
            time.sleep(3)
            dr.find_element_by_css_selector(".ChatSend-txt").send_keys("666")
            dr.find_element_by_css_selector(".ChatSend-button").click()
            # elements[i].click()
            time.sleep(3)
            # break
    except :
        print "error"
    i = i+1
    print "xunhuan:"+str(i)
    # finally:
    #     print "elements:"+str(i)+":"+str(href)


# 获取html内容
# pagesource = dr.page_source
# # f = open(resources +"dy/dy-page.txt",'wb')
# # f.truncate()   #清空文件
# # f.write(str(pagesource))
# # f.close()
# hp = dyHTMLParser()
# hp.feed(pagesource)
# hp.close()
# print(hp.links)
#
# # url = "https://www.douyu.com/862439"
# # dr.get(url)
# i = 0
# while(i < len1):
#     # print cookiesAfter[i]
#     dr.add_cookie(cookiesAfter[i])
#     i = i+1
# dr.implicitly_wait(2)
# dr.find_element_by_css_selector(".ChatSend-txt").send_keys("666")
# dr.find_element_by_css_selector(".ChatSend-button").click()


# listelement = dr.find_elements_by_css_selector("div.classify:nth-child(1) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1)")
# dr.find_elements_by_tag_name("a")
# for ele in listelement:
#     print ele.get_attribute("href")




# print 'Browser will close'
# dr.quit()
# print 'Browser closed'
