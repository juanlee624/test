#!/usr/bin/python
#-*-coding:utf-8-*-
import  math
names=['lijuan','pangzi','limenglong','chengchunxiang']
for name in names:
    print (name)

sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum =sum +x
    print (sum)

r=list(range(5))
print (r)

h=list(range(101))
print(h)
total=0
for x in  h:
    total=total+x
print(total)

a=int
print(a(-12.3))

n1=255
n2=1000
print(hex(n1))
print(hex(n2))

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x




def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny

x,y=move(100,100,60,math.pi/6)
print(x,y)

r=move(100,100,60,math.pi/6)
print(r)



def quadratic(a,b,c):
    global x1
    global x2
    da= b** 2 - 4 * c
    if a!=0 and da>=0:
        x1=(-b+math.sqrt(da))/(2*a)
        x2=(-b-math.sqrt(da))/(2*a)
        print(x1, x2)
        return x1,x2
    elif da <0:
        print('参数输入不合法')
    else:
        print('a不能为0')

a=int(input('请输入a:'))
b=int(input('请输入b:'))
quadratic(a, b, c)









