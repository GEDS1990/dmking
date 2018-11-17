#!/usr/bin/env python
#coding=utf-8
# alix @ 2018-10-21 21:33:05
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import sys
from redisUtil import redisUtil
reload(sys)
sys.setdefaultencoding('utf8')

# 自动登录虎牙直播平台
# 获取虎牙直播中所有正在直播的房间数及房间号，名称
# 获取虎牙直播的所有正在直播的房间；
# 在正在直播的房间中自动发送弹幕

# 连续循环发送直播房间数
roomNums = 10
# 每个房间连续发送的次数
sendNum = 2
# 每个房间发送消息的间隔
sendSpaces = 10
# 发送内容
context = "666"
# 固定控件点击间隔（3秒）
timeNor = 3
# 发送线程数
threadNor = 2

dr = webdriver.Chrome(executable_path="/Users/geds/Documents/shzhyun/mashi/danmu/pyspl/driver/chrome2.43/chromedriver")
# dr.maximize_window()
dr.get('https://www.huya.com/l')
time.sleep(timeNor)
# 所有正在直播的房间数
locator = (By.XPATH, "//*[@id='js-live-list']/li")
WebDriverWait(dr, 20, 0.5).until(EC.presence_of_element_located(locator))
counts = dr.find_elements_by_xpath("//*[@id='js-live-list']/li")
c = 1
locator = (By.XPATH, "")
# 循环访问直播间 start
while c<len(counts):
    ele = dr.find_element_by_xpath("// *[ @ id = 'js-live-list'] / li["+str(c)+"]")
    roomid = ele.get_attribute("gid")
    ele = dr.find_element_by_xpath("//*[@id='js-live-list']/li["+str(c)+"]/a[2]")
    title = ele.get_attribute("title")
    href = ele.get_attribute("href")
    ele = dr.find_element_by_xpath("// *[ @ id = 'js-live-list'] / li["+str(c)+"] / span / span[3] / i[2]")
    renq = ele.text

    roominfos = {'roomid': roomid, 'title': title, 'href': href, 'renq': renq}
    db = redisUtil()
    db.rpush("roominfos", roominfos)
    c = c + 1

print 'Browser will close'
dr.quit()
print 'Browser closed'
