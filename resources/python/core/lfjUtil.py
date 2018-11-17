#coding=utf-8
from selenium import webdriver
import time
import xlwt
import xlrd

# 创建一个Workbook对象，这就相当于创建了一个Excel文件
book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('lfj-urls', cell_overwrite_ok=True)
# 向表test中添加数据
sheet.write(0, 0, '房间号'.decode('utf-8'))  # 其中的'0-行, 0-列'指定表中的单元
sheet.write(0, 1, '链接URL'.decode('utf-8'))
print "开始爬取信息..."
dr = webdriver.Firefox(executable_path="/Users/geds/Documents/shzhyun/mashi/danmu/pyspl/driver/geckodriver")
dr.maximize_window()
dr.get('https://www.6.cn')
time.sleep(5)
# 登录
dr.find_element_by_css_selector("#userPanel_index > ul > li.login > a").click()
time.sleep(5)
dr.find_element_by_css_selector("#member-login-un").send_keys("geds")
time.sleep(5)
dr.find_element_by_css_selector("#member-login-pd").send_keys("yang729")
time.sleep(5)
dr.find_element_by_css_selector("#loginFrame_quick > dl > dt > input").click()
# 爬取房间链接
pic_s = dr.find_elements_by_class_name("pic")
i = 1
for pic in pic_s:
    target = str(pic.get_attribute("target"))
    href = str(pic.get_attribute("href"))
    sheet.write(i, 0, target.decode('utf-8'))
    sheet.write(i, 1, href.decode('utf-8'))
    i = i+1
    print "房间号："+str(target)
    print "链接："+str(href)
dr.find_element_by_class_name("#chatForm > div.chat-txt > span.to-text > input[type='text']").send_keys("hello")



# print 'Browser will close'
# dr.quit()
# print 'Browser closed'
