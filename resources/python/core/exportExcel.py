# _*_coding:utf-8_*_
import sys

import xlwt
from datetime import datetime

from kombu.utils import json

from redisUtil import redisUtil




def write_data_to_excel():
    db = redisUtil();
    # 将sql作为参数传递调用get_data并将结果赋值给result,(result为一个嵌套元组)
    result = db.lrange("userinfos",0,-1)
    # 实例化一个Workbook()对象(即excel文件)
    wbk = xlwt.Workbook()
    # 新建一个名为Sheet1的excel sheet。此处的cell_overwrite_ok =True是为了能对同一个单元格重复操作。
    sheet = wbk.add_sheet('userinfos', cell_overwrite_ok=True)
    # 获取当前日期，得到一个datetime对象如：(2016, 8, 9, 23, 12, 23, 424000)
    today = datetime.today()
    # 将获取到的datetime对象仅取日期如：2016-8-9
    today_date = datetime.date(today)
    # 遍历result中的每个元素。
    sheet.write(0, 0, u'手机号')
    sheet.write(0, 1, u'密码')
    sheet.write(0, 2, u'验证码')
    for i in xrange(len(result)):
        res = result[i]
        # 对result的每个子元素作遍历，
        beanSetStr = db.get("beanSet")
        tmp = str(res).replace('\'', '"',20)
        tmp = str(tmp).replace('u"', '"',20)
        dictinfo = json.loads(tmp)
        for key in dictinfo:
            # 将每一行的每个元素按行号i,列号j,写入到excel中。
            sheet.write(i+1, 0, dictinfo['MOBILE'])
            sheet.write(i+1, 1, dictinfo['PASSWD'])
            sheet.write(i+1, 2, dictinfo['ic'])
    # 以传递的name+当前日期作为excel名称保存。
    wbk.save(sys.path[0]+"/tmp/userinfos" + str(today_date) + '.xls')
    print (sys.path[0]+"/tmp/userinfos" + str(today_date) + '.xls')


# 如果该文件不是被import,则执行下面代码。
if __name__ == '__main__':
    write_data_to_excel()