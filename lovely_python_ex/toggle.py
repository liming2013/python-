#coding:utf-8
'''cdays-5-exercise-1.py �жϽ����Ƿ�������
    @note: ʹ����import, timeģ��, �߼���֧, �ִ���ʽ����
'''

import time                             #����timeģ��
thisyear = time.localtime()[0]             #��ȡ��ǰ���
if thisyear % 400 == 0 or (thisyear % 4 ==0 and thisyear % 100 != 0): #�ж���������, ����ģ400Ϊ0, ����ģ4Ϊ0��ģ100��Ϊ0
    print 'this year %s is a leap year' % thisyear
else:
    print 'this year %s is not a leap year' % thisyear