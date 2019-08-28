#coding=utf-8
import random
#练习3.1 模拟支付宝蚂蚁森林的能量产生过程 


source=""
while source!="0":
    print('查询能量输入能量来源！退出程序请输入0')
    print('能量来源如下：')
    print("生活缴费、行走捐、共享单车、线下支付、网络购票")
    source= input();
    source= source.strip();
    if source=="生活缴费":
        print("262")
    elif source=="行走捐":
        print("200g")
    elif source=="共享单车":
        print("54")
    elif source=="线下支付":
        print("5g")
    elif source=="网络购票":
        print("180g")
    else:
        print("输入错误")
print("已退出")



#练习3.2 猜数字游戏
print("----------猜数字游戏----------")
target=random.randint(1,10)
number=0;
while number!=-1:
   print('请输入1~10中间的任意一个数：')
   number= int(input())
   if target<number:
       print('太大，请重新输入:')
   elif target>number:
       print('太小,请重新输入:')
   else:
       print('恭喜你，你赢了，猜中的数字是%d'%(number))
       number=-1
print("----------游戏结束----------")


#练习3.3 模拟跳一跳小游戏的加分块
print('-----------跳一跳------------')
pass
print('欢迎回来，请开始游戏......')
print('请输入（中心、音乐块、微信支付块）：')
score=0
inputdata=""
while True:
    print('请输入：',end='')
    inputdata=input()
    if inputdata=="中心":
        print('您的分数为：32')
        score+=32
    elif inputdata=="音乐块":
        print('您的分数为:30')
        score+=30
    elif inputdata=='微信支付块':
        print('您的分数为：42')
        score+=42
    else:
        break;
print('哎呀呀，游戏结束,您的总分数为%d'%(score))

        
#练习3.4 模拟10086查询功能
print('------------10086查询功能-----------')

order=1
while order!='0':
    print('输入1，查询当前余额')
    print('输入2，查询当前的剩余流量')
    print('输入3，查询当前剩余通话')
    print('输入0，退出自助查询系统！')
    order=input()
    if order=="1":
        value=random.randint(1,999)
        print("当前余额为:%d元"%(value))
    elif order=="2":
        value=float(random.randint(1,999)/10.0)
        print("当前剩余流量:%.2fG"%(value))
    elif order=="3":
        value=random.randint(1,999)
        print("当前剩余通话为：%d分钟"%(value))
    else:
        if order!="0":
           print("无效指令,请重新输入")
print('退出自助查询系统')

#练习 3.5 打印1000以内的质数
#方法1 for循环
for i in range(2,10000):
    istarget=True;
    for j in range(2,i):
        if (i!=j) and (i%j==0):
           istarget=False
    if istarget:
        print(i,end=' ')

print("打印完成")

# 方法2 while循环
i=2
while i<10000:
    istarget=True
    j=2
    while j<i:
        if j!=i and i%j==0:
            istarget=False
            break
        j+=1
    if istarget:
        print(i,end=' ')
    i+=1
print("打印完成")