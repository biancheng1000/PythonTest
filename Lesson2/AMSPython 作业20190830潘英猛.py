
#练习1：打印象棋口诀
import re
rule="马走日，象走田，车走直路炮翻山，士走斜线护将边，小卒一去不回还。"
pattern=r"[，]"
result=re.sub(pattern,'，\n',rule)
print("象棋口诀：")
print(result)

#练习2：判断车牌归属地
import re
pro="京、沪、津、渝、鲁、冀、晋、蒙、辽、吉、黑、苏、浙、皖、闽、赣、豫、湘、鄂、粤、桂、琼、川、贵、云、藏、陕、甘、青、宁、新、港、澳、台"
provenc=["北京","上海","天津","重庆","山东","河北","山西","内蒙古","辽宁","吉林","黑龙江","苏州","浙江","安徽","福建","江西","河南","湖南","湖北","广东","贵州","海南","四川","贵州","云南","西藏","陕西","甘肃","青海","宁夏","新疆","香港","澳门","台湾"]
newPro= pro.replace("、","|")
print(newPro)
provencDic=dict(zip(pro,provenc))
pattern=str.format("[%s][A-Za-z]"%newPro)
print(pattern)

while True:
     print("请输入待验证的车牌号码,（输入Q退出）：")
     carnum=input()
    # carnum="京A17272"
     if(carnum.lower()=='q'):
         break;
     mt=re.match(pattern,carnum,re.I)
     if(mt!=None):
         #取第一个汉字
         pshot=mt.group()[0]
         print("这张车牌归属地：%s"%provencDic[pshot])
     else:
         print("无效车牌照")
print("退出")

#练习3 模拟微信红包
from decimal import Decimal
import random  #导入随机方法库
print("========模拟微信抢红包========")
total=float(input("请输入要装入红包的总金额(元）："))
num=int(input("请输入红包的个数（个）："))
min=0.01

money_list=[]  #创建红包列表
total=Decimal(total)   #转换红包金额为十进制
num=Decimal(num)       #转换红包个数为十进制
min=Decimal(str(min))  #min：定义最小红包个数
if total>num*min:      #判断红包金额是否大于 每个红包个数*单红包最小金额0.01
    for i in range(1,int(num)):
        safe_total=total-(num-i)*min
        temp_min=min*100   #随机红包的最小值
        temp_max=int(safe_total*100) #随机红包的最大值
        if temp_min>temp_max:
            money=temp_min/100
        else:
            money=Decimal(random.randint(temp_min,temp_max))/100
        total-=money
        money_list.append(money)  #添加随即输出红包到红包列表
    money_list.append(total)
    random.shuffle(money_list)   #随机输出，打乱列表顺序
for x in range(len(money_list)):
    print("第"+str(x+1)+"个红包:"+str(money_list[x])+"元")



#练习4：显示实时天气预报
report='{:s}年{:s}月{:s}日\t天气预报:{:s}\t{:s}℃~{:s}℃\t{:s}{:s}~{:s}级'
report_tem=report.format('2018','4','17','晴','20','7','微风转西风','3','4')
print(report_tem)

time=['08:00','12:00','16:00','20:00','00:00','04:00']
weather=['晴','晴','晴','晴','晴']
temperature=[13,19,18,15,12,9]
wind=['微风','微风','西风3~4级','西风3~4级','微风','微风']
for i in range(5):
    print('{:s}\t天气预报{:s}\t{:s}\t{:s}'.format(str(time[i]),str(weather[i]),str(temperature[i]),str(wind[i])))
