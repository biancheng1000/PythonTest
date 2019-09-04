#练习6.1 导演为剧本选主角
def out(actor):
    print("%s开始参演这个剧本"%actor)
actor=input("导演选定的主角是：")
out(actor)

#练习 6.2 模拟美团外卖商家的套餐 
package={"考神套餐":"13元","单人套餐":"9.9元","情侣套餐":"20元"}
def printTest(**para):
    for key,value in para.items():
        print('{:s}{:s}'.format(key,value))
printTest(**package)


#练习6.3 根据生日判断星座
Horoscope={"白羊座":(3.21,4.19),"金牛座":(4.20,5.20),"双子座":(5.21,6.21),"巨蟹座":(6.22,7.22),"狮子座":(7.23,8.22),
           "处女座":(8.23,9.22),"天秤座":(9.23,10.23),"天蝎座":(10.24,11.22),"射手座":(11.23,12.21),"摩羯座":(12.22,1.19),
           "水瓶座":(1.20,2.18),"双鱼座":(2.19,3.20)}
def DeterminStart(month,day):
    gatevalue=month+day/100
    for key,value in Horoscope.items():
        if(gatevalue>value[0] and gatevalue<value[-1]):
            print("%d月%d日星座为：%s"%(month,day,key))

month=int(input("请输入月份："))
while(month>12 or month==0):
    print("无效月份")
    month=int(input("请输入月份："))
day=int(input("请输入日："))
while(day>30 or day==0) or(month==2 and day>28):
    print("无效日")
    month=int(input("请输入日："))

DeterminStart(month,day)

#练习 6.4 将美元转为人民币
RATE=6.28
def Convert(dolar):
    return dolar*RATE

Dmoney=input("请输入美元：")
print("转换后人民币金额是:%.2f"%Dmoney)

#6.附加题
def SumValue(value):
    if(value==1):
        return 1
    else:
        return value+SumValue(value-1)
print("1-100的求和是：%d"%SumValue(100))