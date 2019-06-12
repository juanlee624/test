#!/usr/bin/python
#-*-coding:utf-8-*-

height=input('请输入身高：')
weight=input('请输入体重：')
h=float(height)
w=float(weight)
bmi=w/w**2
if bmi < 18.5:
    print ('过轻')
elif  18.5<=bmi<25:
    print ('正常')
elif  25<=bmi<28 :
     print('过重')
elif 28<=bmi <32:
     print('肥胖')
else :
     print('严重肥胖')