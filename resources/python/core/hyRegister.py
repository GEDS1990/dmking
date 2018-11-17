#!/usr/bin/env python
# -*- coding: utf-8 -*-
# alix @ 2018-10-21 21:33:05
import re

from kombu.utils import json
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import urllib2
from redisUtil import redisUtil
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class hyregister(object):
    def __init__(self,ptai,timeNor,hasTel):
        self._ptai = ptai
        self.timeNor = timeNor
        self.TOKEN = '009751090cc181d5268c9e0c6f178bb5cd38653dc601'  # 输入TOKEN
        self.header_dict = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
        self.ITEMID = '8103'  # 项目编号
        self.MOBILE = ""
        self.ic = ""
        self.counts = 0
        self.hasTel = hasTel #是否已知手机号

    def getTel(self):
        print("获取的话号码...start")
        # 获取手机号码
        ITEMID = self.ITEMID  # 项目id
        EXCLUDENO = ''  # 排除号段170_171
        url = 'http://api.fxhyd.cn/UserInterface.aspx?action=getmobile&token=' + \
              self.TOKEN + '&itemid=' + ITEMID + '&excludeno=' + EXCLUDENO
        MOBILE1 = urllib2.urlopen(urllib2.Request(
            url=url, headers=self.header_dict)).read().decode(encoding='utf-8')
        if MOBILE1.split('|')[0] == 'success':
            MOBILE = MOBILE1.split('|')[1]
            self.MOBILE = MOBILE
            print('获取号码是:\n' + MOBILE)
        else:
            print('获取TOKEN错误,错误代码' + MOBILE1)
        print("获取的话号码...end")

    def getCode(self):
        print("获取验证码...start")
        # 获取短信，注意线程挂起5秒钟，每次取短信最少间隔5秒
        TOKEN = self.TOKEN  # TOKEN
        ITEMID = self.ITEMID  # 项目id
        MOBILE = self.MOBILE  # 手机号码
        WAIT = 100  # 接受短信时长60s
        url = 'http://api.fxhyd.cn/UserInterface.aspx?action=getsms&token=' + \
              TOKEN + '&itemid=' + ITEMID + '&mobile=' + MOBILE + '&release=1'
        text1 = urllib2.urlopen(urllib2.Request(
            url=url, headers=self.header_dict)).read().decode(encoding='utf-8')
        TIME1 = time.time()
        TIME2 = time.time()
        ROUND = 1
        while (TIME2 - TIME1) < WAIT and not text1.split('|')[0] == "success":
            time.sleep(5)
            text1 = urllib2.urlopen(urllib2.Request(
                url=url, headers=self.header_dict)).read().decode(encoding='utf-8')
            TIME2 = time.time()
            ROUND = ROUND + 1
        ROUND = str(ROUND)
        if text1.split('|')[0] == "success":
            text = text1.split('|')[1]
            TIME = str(round(TIME2 - TIME1, 1))
            print('短信内容是' + text + '\n耗费时长' + TIME + 's,循环数是' + ROUND)
            # 提取短信内容中的数字验证码
            pat = "[0-9]+"
            IC = 0
            IC = re.search(pat, text)
            if IC:
                print("验证码是:\n" + IC.group())
                self.ic = str(IC.group())
            else:
                print("请重新设置表达式")
        else:
            print('获取短信超时，错误代码是' + text1 + ',循环数是' + ROUND)
        # 释放号码
        url = 'http://api.fxhyd.cn/UserInterface.aspx?action=release&token=' + \
              TOKEN + '&itemid=' + ITEMID + '&mobile=' + MOBILE
        RELEASE = urllib2.urlopen(urllib2.Request(
            url=url, headers=self.header_dict)).read().decode(encoding='utf-8')
        if RELEASE == 'success':
            print('号码成功释放')
        print("获取验证码...end")

    def getPage(self):
        db = redisUtil()
        # 通用设置
        beanSetStr = db.get("beanSet")
        norSetStr = db.get("norSet")
        beanSet = json.loads(str(beanSetStr))
        norSet = json.loads(str(norSetStr))
        os = sys.platform.system()
        # Windows

        for key in norSet:
            # driverPath
            # driverPath = norSet["driverPath"]
            driverPath = sys.path[0]
            # enginePath
            # enginePath = norSet["enginePath"]
            enginePath = sys.path[0]
            # isShow
            isShow = norSet["isShow"]
        if isShow == 'true':
            if os != 'Windows':
                dr = webdriver.Chrome(executable_path=str(driverPath) + "/driver/chrome2.43/mac/chromedriver")
            else:
                dr = webdriver.Chrome(executable_path=str(driverPath) + "/driver/chrome2.43/win/chromedriver.exe")
        else:
            if os != 'Windows':
                dr = webdriver.PhantomJS(
                    executable_path=str(driverPath) + "/phantomsjs/mac/bin/phantomjs")
            else:
                dr = webdriver.PhantomJS(
                    executable_path=str(driverPath) + "/phantomsjs/win/bin/phantomjs")
        # dr.maximize_window()
        dr.get('https://www.huya.com')
        # 获得当前窗口的句柄
        homehandle = dr.current_window_handle
        time.sleep(self.timeNor)
        # 注册
        locator = (By.CSS_SELECTOR, "#nav-regiest")
        WebDriverWait(dr, 20, 0.5).until(EC.presence_of_element_located(locator))
        dr.find_element_by_css_selector("#nav-regiest").click()
        # 获取手机号
        if self.hasTel !="":
            self.getTel()
            print ("获取新的手机号："+self.MOBILE)
            print ("未对已注册的手机号做处理")
        else:
            self.MOBILE = self.hasTel
            print ("已知手机号："+self.MOBILE+"，"+self.hasTel)
        dr.implicitly_wait(self.timeNor)
        # 输入手机号
        dr.find_element_by_css_selector("body > div.UDBSdkLgn > div.UDBSdkLgn-box > div.UDBSdkLgn-inner.account.login > div.UDBSdkLgn-body > div.UDBSdkLgn-main > div.UDBSdkLgn-register.J_UDBSdkLgnPane > div > div > div.UDBSdkLgn-regItem.UDBSdkLgn-clearFix.UDBSdkLgn-regAreas > input").send_keys(str(self.MOBILE))
        dr.implicitly_wait(self.timeNor)
        # 点击发送验证码
        dr.find_element_by_css_selector("body > div.UDBSdkLgn > div.UDBSdkLgn-box > div.UDBSdkLgn-inner.account.login > div.UDBSdkLgn-body > div.UDBSdkLgn-main > div.UDBSdkLgn-register.J_UDBSdkLgnPane > div > div > div:nth-child(3) > span").click()
        dr.implicitly_wait(self.timeNor)
        dr.find_element_by_css_selector("body > div.UDBSdkLgn > div.UDBSdkLgn-box > div.UDBSdkLgn-inner.account.login > div.UDBSdkLgn-body > div.UDBSdkLgn-main > div.UDBSdkLgn-register.J_UDBSdkLgnPane > div > div > div:nth-child(3) > span").click()
        # 获取验证码 5秒
        self.getCode()
        dr.find_element_by_css_selector("body > div.UDBSdkLgn > div.UDBSdkLgn-box > div.UDBSdkLgn-inner.account.login > div.UDBSdkLgn-body > div.UDBSdkLgn-main > div.UDBSdkLgn-register.J_UDBSdkLgnPane > div > div > div:nth-child(3) > input").send_keys(self.ic)
        dr.implicitly_wait(self.timeNor)
        dr.find_element_by_css_selector("body > div.UDBSdkLgn > div.UDBSdkLgn-box > div.UDBSdkLgn-inner.account.login > div.UDBSdkLgn-body > div.UDBSdkLgn-main > div.UDBSdkLgn-register.J_UDBSdkLgnPane > div > div > div:nth-child(4) > input").send_keys("qAz123!@#")
        dr.implicitly_wait(self.timeNor)
        dr.find_element_by_css_selector("body > div.UDBSdkLgn > div.UDBSdkLgn-box > div.UDBSdkLgn-inner.account.login > div.UDBSdkLgn-body > div.UDBSdkLgn-main > div.UDBSdkLgn-register.J_UDBSdkLgnPane > div > div > div.UDBSdkLgn-regButton > span").click()
        if self.ic !="":
            print("手机号："+self.MOBILE+"密码：qAz123!@#"+"验证码："+self.ic)
            self.counts = self.counts + 1
            # userinfos = redisUtil.get("userinfos")
            userinfo = {'MOBILE': self.MOBILE, 'PASSWD': 'qAz123!@#', 'ic': self.ic}
            db = redisUtil()
            db.rpushx("userinfos",userinfo)

if __name__ == "__main__":
    print('This is main of module "hyregister.py"')
    hyR = hyregister("huya",3)
    while hyR.counts < 10:
        hyR.getPage()
