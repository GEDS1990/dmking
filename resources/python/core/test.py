#!/usr/bin/env python
# -*- coding: utf-8 -*-
# alix @ 2018-10-21 21:33:05
import re

from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import urllib2
from org.shzhyun.splider.core.redisUtil import redisUtil
import sys
reload(sys)
sys.setdefaultencoding('utf8')

MOBILE = '12312'
ic = '12311111'

print('This is main of module "hyFpwd.py"')
userinfo = {"MOBILE": MOBILE, "PASSWD": "qAz123!@#", "ic": ic}
db = redisUtil()
db.rpush("TEST", userinfo)