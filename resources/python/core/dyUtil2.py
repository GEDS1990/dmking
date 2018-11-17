#coding=utf-8
import sys

from org.shzhyun.splider.common.dyHTMLParser import dyHTMLParser

reload(sys)
sys.setdefaultencoding('utf-8')

from selenium import webdriver
import time
resources = "/Users/geds/Documents/shzhyun/mashi/danmu/pyspl/resources/"
dr = webdriver.Firefox(executable_path="/Users/geds/Documents/shzhyun/mashi/danmu/pyspl/driver/geckodriver")
dr.maximize_window()

url = "https://www.douyu.com/862439"
dr.get(url)
time.sleep(3)
dr.find_element_by_css_selector("#js-player-asideMain > div > div.layout-Player-chat > div > div.ChatSpeak > div.ChatSend > div.MuteStatus.is-noLogin > span").click()
time.sleep(3)
dr.switch_to_frame("login-passport-frame")
dr.find_element_by_xpath(".//*[@id='loginbox']/div[2]/div[1]/div[1]").click()
time.sleep(3)
dr.find_element_by_name("phoneNum").send_keys("13128641782")
dr.find_element_by_name("password").send_keys("yang729")
dr.find_element_by_xpath("//input[@value='登录']").click()
dr.switch_to_default_content()
dr.find_element_by_css_selector("#js-player-asideMain > div > div.layout-Player-chat > div > div.ChatSpeak > div.ChatSend > textarea").send_keys("666")
dr.find_element_by_css_selector("#js-player-asideMain > div > div.layout-Player-chat > div > div.ChatSpeak > div.ChatSend > div").click()

# listelement = dr.find_elements_by_css_selector("div.classify:nth-child(1) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1)")
# dr.find_elements_by_tag_name("a")
# for ele in listelement:
#     print ele.get_attribute("href")




# print 'Browser will close'
# dr.quit()
# print 'Browser closed'
