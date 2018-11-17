#!/usr/bin/env python
#coding=utf-8
# -*- coding: utf-8 -*-
# alix @ 2018-10-21 21:33:05
from kombu.utils import json
from selenium import webdriver
import time
from time import sleep, ctime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Properties import *
from redisUtil import redisUtil
import sys
import threading
import ast
import datetime
import platform

reload(sys)
sys.setdefaultencoding('utf8')

# 自动登录虎牙直播平台
# 获取虎牙直播中所有正在直播的房间数及房间号，名称
# 获取虎牙直播的所有正在直播的房间；
# 在正在直播的房间中自动发送弹幕

# # 连续循环发送直播房间数
# roomNums = sys.argv[1]
# # 每个房间连续发送的参数
# sendNum = sys.argv[2]
# # 每个房间发送消息的间隔
# sendSpaces = sys.argv[3]
# # 发送内容
# context = sys.argv[4]
# # 固定控件点击间隔
# timeNor = sys.argv[5]
# 发送线程数
# threadNor = sys.argv[6]

def autodm(loop):
    db = redisUtil()
    # 通用设置
    beanSetStr = db.get("beanSet")
    norSetStr = db.get("norSet")
    beanSet = json.loads(str(beanSetStr))
    norSet = json.loads(str(norSetStr))
    os = platform.system()
    # Windows

    for key in norSet :
        # driverPath
        # driverPath = norSet["driverPath"]
        driverPath = sys.path[0]
        # enginePath
        # enginePath = norSet["enginePath"]
        enginePath = sys.path[0]
        # isShow
        isShow = norSet["isShow"]
    for key in beanSet :
        # 连续循环发送直播房间数
        roomNums = beanSet["roomNums"]
        # 每个房间连续发送的次数
        sendNum = beanSet["sendNum"]
        # 每个房间发送消息的间隔
        sendSpaces = beanSet["sendSpaces"]
        # 固定控件点击间隔（3秒）
        timeNor = beanSet["timeNor"]
        # 发送线程数
        threadNor = beanSet["threadNor"]
    # 用户信息
    userinfos = db.lrange("userinfos",0,15)
    # 弹幕内容
    contexts = db.lrange("contexts",0,15)
    for user in userinfos:
        # userinfos
        us = ast.literal_eval(user)
        mobile = us['MOBILE'].encode('utf-8')
        passwd = us['PASSWD']
        # driver
        if isShow == 'true':
            if os != 'Windows':
                dr = webdriver.Chrome(executable_path=str(driverPath) + "/driver/chrome2.43/mac/chromedriver")
            else:
                dr = webdriver.Chrome(executable_path=str(driverPath) + "/driver/chrome2.43/win/chromedriver.exe")
        else:
            if os != 'Windows':
                dr = webdriver.PhantomJS(
                    executable_path=str(driverPath) + "/driver/phantomsjs/mac/bin/phantomjs")
            else:
                dr = webdriver.PhantomJS(
                    executable_path=str(driverPath) + "/driver/phantomsjs/win/bin/phantomjs")
        # dr.maximize_window()
        dr.get('https://www.huya.com')
        # print "dr.firefox_profile"+str(dr.firefox_profile.path)
        #获得当前窗口的句柄
        homehandle = dr.current_window_handle
        time.sleep(timeNor)
        # 登录
        locator = (By.CSS_SELECTOR, "#nav-login")
        WebDriverWait(dr, 20, 0.5).until(EC.presence_of_element_located(locator))
        dr.find_element_by_css_selector("#nav-login").click()
        time.sleep(timeNor)
        dr.find_element_by_css_selector("body > div.UDBSdkLgn > div.UDBSdkLgn-box > div:nth-child(2) > div.UDBSdkLgn-switch.UDBSdkLgn-webQuick > img").click()
        # 用户框
        dr.implicitly_wait(timeNor)
        dr.find_element_by_css_selector("body > div.UDBSdkLgn > div.UDBSdkLgn-box > div.UDBSdkLgn-inner.account.login > div.UDBSdkLgn-body > div.UDBSdkLgn-main > div.UDBSdkLgn-login.J_UDBSdkLgnPane > div:nth-child(1) > div.UDBSdkLgn-modal > div.UDBSdkLgn-common > div:nth-child(1) > span > input").send_keys(mobile)
        # 密码框
        dr.implicitly_wait(timeNor)
        dr.find_element_by_css_selector("body > div.UDBSdkLgn > div.UDBSdkLgn-box > div.UDBSdkLgn-inner.account.login > div.UDBSdkLgn-body > div.UDBSdkLgn-main > div.UDBSdkLgn-login.J_UDBSdkLgnPane > div:nth-child(1) > div.UDBSdkLgn-modal > div.UDBSdkLgn-common > div:nth-child(2) > span > input").send_keys(passwd)
        # 登录按钮
        dr.implicitly_wait(timeNor)
        dr.find_element_by_css_selector("body > div.UDBSdkLgn > div.UDBSdkLgn-box > div.UDBSdkLgn-inner.account.login > div.UDBSdkLgn-body > div.UDBSdkLgn-main > div.UDBSdkLgn-login.J_UDBSdkLgnPane > div:nth-child(1) > div.UDBSdkLgn-modal > div.UDBSdkLgn-mt20.clearfix > a").click()
        # 不升级按钮
        try:
            dr.implicitly_wait(timeNor)
            dr.find_element_by_css_selector("body > div.upgrade-account-wrap > div.no-up-tips > span").click()
        except:
            print ("无 不升级 按钮")
        # 刷新页面
        dr.refresh()
        dr.implicitly_wait(timeNor)
        li_s = dr.find_elements_by_tag_name("li")
        # 点击直播按钮
        dr.implicitly_wait(timeNor)
        dr.find_element_by_css_selector("#duya-header > div > div > div.duya-header-nav > div:nth-child(2) > a").click()
        time.sleep(timeNor)
        #初始化状态 start
        db.set('runswitch_hy','start')
        # switchfile = Properties('/Users/geds/Documents/shzhyun/mashi/danmu/pyspl/org/shzhyun/splider/core/runswitch.properties')   #读取文件
        # switchfile.put('runswitch', 'start')    #初始化状态  #运行状态开关   start：开始pause：暂停；restart：继续；stop：退出；
        #初始化状态 end
        # 所有正在直播的房间数
        locator = (By.XPATH, "//*[@id='js-live-list']/li")
        WebDriverWait(dr, 20, 0.5).until(EC.presence_of_element_located(locator))
        counts = dr.find_elements_by_xpath("//*[@id='js-live-list']/li")
        c = 1
        # 循环访问直播间 start
        while c<len(counts):
            #读取运行状态终端 start

            switch = str(db.get('runswitch_hy'))
            # switchfile = Properties('/Users/geds/Documents/shzhyun/mashi/danmu/pyspl/org/shzhyun/splider/core/runswitch.properties')  # 读取文件
            # switch = switchfile.get('runswitch')    #运行状态开关   start：开始pause：暂停；restart：继续；stop：退出；
            # 根据runswitch判断是否继续执行
            if switch == "start":
                print("开始...")
            elif switch == "pause":
                print("暂停程序...")
                time.sleep(5)
                continue
            elif switch == "restart":
                print("程序重新开始...")
            elif switch == "stop":
                print("停止程序...")
                # switchfile.put('runswitch','start')
                db.set('runswitch_hy', 'start')
                print '将要关闭浏览器'
                dr.quit()
                print '关闭浏览器'
                sys.exit(0)
            #读取运行状态终端 end
            # 判断是否完成指定数量房间的发送 start
            if c > roomNums:
                print ("完成:"+str(roomNums)+"个房间的自动发送")
                c = 1   #再次从第一个房间开始发送
                # switchfile.put('runswitch', 'start')
                # print '将要关闭浏览器'
                # dr.quit()
                # print '关闭浏览器'
                # sys.exit(0)
            else:
                print("开始发送第："+str(c)+"个房间")
            # 判断是否完成指定数量房间的发送 end
            dr.find_element_by_xpath("//*[@id='js-live-list']/li["+str(c)+"]/a[2]").click()
            # //*[@id='js-live-list']/li[变量]/a[2]
            time.sleep(timeNor)
            # 正常只有两个窗口被打开
            allhandles = dr.window_handles
            for handle in allhandles:
                if handle != homehandle:
                    dr.switch_to.window(handle)
                    sn = 0  #发送次数
                    count = 1
                    while sn < sendNum:
                        for context in contexts:
                            # contexts
                            cot = ast.literal_eval(context)
                            co = cot['conts'].encode('utf-8')
                            locator = (By.XPATH, "//*[@id='pub_msg_input']")
                            WebDriverWait(dr, 20, 0.5).until(EC.presence_of_element_located(locator))
                            dr.find_element_by_xpath("//*[@id='pub_msg_input']").send_keys(unicode(str(co)))
                            locator = (By.XPATH, "//*[@id='msg_send_bt']")
                            WebDriverWait(dr, 20, 0.5).until(EC.presence_of_element_located(locator))
                            dr.find_element_by_xpath("//*[@id='msg_send_bt']").click()
                            print("第"+str(count)+"次发送成功,房间链接:"+str(dr.current_url)+";发送信息:"+unicode(str(co)))
                            count = count + 1
                            logs = {'num': str(count), 'contx': unicode(str(co)), 'href': str(dr.current_url), 'createtime': str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))}
                            db.rpush("logs",logs)
                            # print("第"+str(sn)+"次发送成功,发送信息:"+context)
                            time.sleep(sendSpaces)  #发送间隔
                        sn = sn + 1
                    dr.close()
                    time.sleep(sendSpaces)  #发送间隔
                    dr.switch_to_window(homehandle)
            c = c+1
        # print 'Browser will close'
        # dr.quit()
        # print 'Browser closed'

threads = []
# 创建线程t1，并添加到线程数组
t1 = threading.Thread(target=autodm, args=('2'))
threads.append(t1)
# 创建线程t2，并添加到线程数组
t2 = threading.Thread(target=autodm, args=('2'))
threads.append(t2)

if __name__ == '__main__':
    autodm(2)
    # 启动线程
    # for t in threads:
    #     t.start()
    #     t.join()
    #     print('all end:', ctime())