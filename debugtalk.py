# -*- coding: utf-8 -*-
import time
import random
import os
import mysql.connector
from _random import Random


# 执行select语句返回第一列第一行的值 建议select语句书写正确
def select(value):
    conn = mysql.connector.connect(user='minsc', password='yj@98PRgnzn',
    host='106.14.10.19', port='3306',
    database='minsc', use_unicode=True)
    c = conn.cursor()
    c.execute(value)
    for row in c:
       row
    answer = row[0]
    c.close()
    conn.close()
    return answer


# 等待时间
def sleep(n_secs):
    time.sleep(n_secs)


# 随机中文名
def getChineseName(num=3):
    surname = u"赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤";
    surname = random.choice(surname);
    middlename = u"精忠报国维持正义文昌德茂广远泽长吉善余庆继世传家恩思绍前人志长昭青永世谋居心中繁茂庆千秋世连德茂广元泽长";
    middlename = random.choice(middlename);
    name = u"君不见走马川行雪海边平沙莽莽黄入天轮台九月风夜吼一川碎石大如斗随风满地石乱走匈奴草黄马正肥金山西见烟尘飞汉家大将西出师将军金甲夜不脱半夜军行戈相拨风头如刀面如割马毛带雪汗气蒸五花连钱旋作冰幕中草檄砚水凝虏骑闻之应胆慑料知短兵不敢接车师西门伫献捷";
    name = random.choice(name);
    if num == 2 :  # 2位姓名
        return surname + name
    elif num == 3:  # 3位姓名
        return surname + middlename + name
    else:  # 不传或传错均默认3位姓名
        return surname + middlename + name

# print(getChineseName())


# 随机邮箱
def getEmail():
    mail = ["qq", "163", "gmail", "hotmail", "yahoo", "sohu"]
    return str(random.randint(100000000, 999999999)) + "@" + random.choice(mail) + ".com"

# print(getEmail())


# 随机手机号
def getPhone():
    telFirst = ["134", "135", "136", "137", "138", "139", "147", "148", "150", "151", "152", "157", "158",
                "159", "165", "172", "178", "182", "183", "184", "187", "188", "198", "130", "131", "132", "145", "146",
                "155", "156", "166", "171", "175", "176", "185", "186", "133", "149", "153", "173", "174", "177", "180",
                "181", "189", "191", "199", "170" ]
    phone = random.choice(telFirst) + str(random.randint(10000000, 99999999))
    return phone

# print(getPhone())


# 指定长度随机字母
def getStr(num):
    str = "abcdefghijklmnopqrstuvwxyz"
    i = 1
    name = ""
    while i <= num :
        name = name + random.choice(str)
        i += 1
    return name

# print(getStr(1))


# 指定长度随机数字
def getNum(start, end):
    return random.randint(start, end)

# print(getNum(0, 100))


# 字符串拼接
def joinStr(*value):
    string = ""
    for i in value:
        if isinstance(i, str):  # 判断如果传的数字转成字符
            string = string + i
        else:
            string = string + str(i)
    return string

# print(joinStr("tao", "bao", ".com", 77, "  ", 99))


# 读取文件内容
def get_file(filePath="test.apk"):
    return open(filePath, "rb")
