#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time

# ��ʽ����2016-03-20 11:45:39��ʽ
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

# ��ʽ����Sat Mar 28 22:24:24 2016��ʽ
print time.strftime("%A %B %d %H:%M:%S %Y", time.localtime()) 

print time.strftime("%W", time.localtime()) 

print time.strftime("%j", time.localtime()) 
  
# ����ʽ�ַ���ת��Ϊʱ���
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))


