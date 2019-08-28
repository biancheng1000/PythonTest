
import datetime
##4.1 输出“王者荣耀”的游戏角色

#数据定义 
typelist=['坦克','战士','刺客 ']
tranklist={"苏烈","刘邦","钟馗","张飞","牛魔","程咬金","白起","刘婵","庄周","项羽","廉颇","巨灵神","安禄山","猪八戒"}
soldierList=("狂铁","裴擒虎","铠","孙悟空","哪吒","杨戬","橘石京","亚瑟","雅典娜","夏侯惇","关羽","吕布","韩信","老夫子")
assassinList=["百里玄策","庞统","花木兰","荆轲","不知火舞","李白","娜可露露","兰陵王","露娜","韩信","宫本武藏","盖聂","红拂"]
deailList=[tranklist,soldierList,assassinList]
data=dict(zip(typelist,deailList))

#遍历输出
for key,value in data.items():
    print("=====",key,"=====")
    for id in value:
        print(id,end=' ')
    print("\n")
  



#4.2 模拟火车订票系统 
titles=('车次','出发站-到达站','出发时间','到达时间','历时')
trainNumber=['T40','T298','T158','Z62']
stations='长春-北京'
startTime=('00:12','00:06','12:48','21:58')
endTime=('12:20','10:50','21:06','06:08')

for i in range(0,4):
    print("%-15s"%(titles[i]),end='')
print('')

for i in range(0,4):
    print("%-15s"%(trainNumber[i]),
           stations,
           "%-15s"%(startTime[i]),
           "%-15s"%(endTime[i]),end='')

    end= datetime.datetime.strptime(endTime[i],'%H:%M')
    st=datetime.datetime.strptime(startTime[i],'%H:%M')
    if end<st:
        end=end+datetime.timedelta(days=1)
    deltaTime=end-st    
    print( "%-15s"%(':'.join(str(deltaTime).split(',')[-1].split(':')[:2])))
print('输入要购买的车次:')
train=input()
print('输入乘车人（用逗号分隔）:')
namelist=input()

if train in trainNumber:
    index=trainNumber.index(train)
    print("你已购%s次列车 %s %s开，请%s尽快换取纸质车票"%(train,stations,startTime[index],namelist))
else:
    print('您输入的车次不存在')


#4.3 电视剧的收视率排行榜
names=['Give up,hold on to me','The private dishes of the husbands','My father-in-law will do martiaiarts','North Canton still belive in love','Impossible talk','Sparrow','East of dream Avenue','The prodigal son of the new frontier town','Distant distance','Music legend']
rates=[1.4,1.343,0.92,0.862,0.553,0.411,0.164,0.259,0.394,0.562]
newrateis=sorted(rates,reverse=False)
for i in newrateis:
    id=rates.index(i)
    print('《%s》收视率:%f'%(names[id],i))


#4.4 订制自己的手机套餐
hf=('0分钟','50分钟','100分钟','300分钟','不限量')
ll=('0M','500M','1G','5G','不限量')
dx=('0条','50条','100条')

print('------------------')
print('定制自己的手机套餐')
print('A.请设置通话的时长:')
for i in range(1,len(hf)+1):
    print('%d. %s'%(i,hf[i-1]))
print('输入选择的通话时长编号：')
hfindex=int(input())

print('B.请设置流量包:')
for i in range(1,len(ll)+1):
    print('%d. %s'%(i,ll[i-1]))
print('输入选择的流量包编号：')
llindex=int(input());


print('C.请设置短信条数编码:')
for i in range(1,len(dx)+1):
    print('%d. %s'%(i,dx[i-1]))
print('输入选择的短信编号：')
dxindex=int(input());

print('您的手机套餐定制成功:免费通话时长为%s/月，流量为%s/月,短信条数%s/月'%(hf[hfindex-1],ll[llindex-1],dx[dxindex-1]))


#补充题
data=[
"2017/07/03",
"2017/07/04", 
"2017/07/05", 
"2017/07/06", 
"2017/07/07", 
"2017/07/10", 
"2017/07/11",
"2017/07/12",
"2017/07/13", 
"2017/07/14",
"2017/07/17", 
"2017/07/18", 
"2017/07/19", 
"2017/07/20", 
"2017/07/21", 
"2017/07/24", 
"2017/07/25", 
"2017/07/26", 
"2017/07/27", 
"2017/07/28", 
"2017/07/31", 
"2017/08/01", 
"2017/08/02", 
"2017/08/03", 
"2017/08/04",
"2017/08/07", 
"2017/08/08", 
"2017/08/09", 
"2017/08/10", 
"2017/08/11", 
"2017/08/14", 
"2017/08/15", 
"2017/08/16", 
"2017/08/17", 
"2017/08/18", 
"2017/08/21", 
"2017/08/22", 
"2017/08/23", 
"2017/08/24", 
"2017/08/25", 
"2017/08/28", 
"2017/08/29", 
"2017/08/30", 
"2017/08/31", 
"2017/09/01", 
"2017/09/04", 
"2017/09/05", 
"2017/09/06", 
"2017/09/07", 
"2017/09/08",
"2017/09/11",
"2017/09/12",
"2017/09/13",
"2017/09/14",
"2017/09/15",
"2017/09/18",
"2017/09/19",
"2017/09/20",
"2017/09/21",
"2017/09/22",
"2017/09/25",
"2017/09/26",
]
price=[
3650.85,
3619.98, 
3659.68, 
3660.1, 
3655.93, 
3653.69, 
3670.81,
3658.82,
3686.92, 
3703.09,
3663.56, 
3667.18, 
3729.75, 
3747.88, 
3728.6, 
3743.47, 
3719.56, 
3705.39, 
3712.19, 
3721.89, 
3737.87, 
3770.38, 
3760.85, 
3727.83, 
3707.58,
3726.79, 
3732.21, 
3731.04, 
3715.92, 
3647.35, 
3694.68, 
3706.06, 
3701.42, 
3721.28, 
3724.67, 
3740.99, 
3752.3, 
3756.09, 
3734.65, 
3795.75, 
3842.71, 
3834.54, 
3834.3, 
3822.09, 
3830.54, 
3845.62, 
3857.05, 
3849.45, 
3829.87, 
3825.99,
3825.65,
3837.93,
3842.61,
3829.96,
3831.3,
3843.14,
3832.12,
3842.44,
3837.82,
3837.73,
3817.79,
3820.78,
]
eque=[
1.09,
1.09, 
1.09, 
1.1, 
1.1, 
1.09, 
1.08,
1.17,
1.17, 
1.17,
1.1, 
1.11, 
1.12, 
1.12, 
1.11, 
1.11, 
1.19, 
1.11, 
1.12, 
1.12, 
1.13, 
1.14, 
1.13, 
1.08, 
1.13,
1.05, 
1.13, 
1.21, 
1.14, 
1.22, 
1.21, 
1.21, 
1.14, 
1.14, 
1.15, 
1.17, 
1.17, 
1.25, 
1.17, 
1.17, 
1.18, 
1.17, 
1.19, 
1.19, 
1.27, 
1.17, 
1.18, 
1.17, 
1.18, 
1.18,
1.18,
1.26,
1.18,
1.19,
1.18,
1.18,
1.19,
1.19,
1.27,
1.18,
1.17,
1.18,
]
maxprice=[0 for i in range(62)]
maxeque=[0 for i in range(62)]

#计算净值的回撤率
for i in range(62):
    eq=eque[i]
    hc=0
    for j in range(i+1,62):
        tp=(eq-eque[j])/eq
        if tp>hc:
            hc=tp
    maxeque[i]=hc
mxhc=max(maxeque)
ind=maxeque.index(mxhc)
print("日期：%s,净值最大回撤率%.2f"%(data[ind],mxhc))
   

#计算净值的回撤率
for i in range(62):
    eq=price[i]
    hc=0
    for j in range(i+1,62):
        tp=(eq-price[j])/eq
        if tp>hc:
            hc=tp
    maxprice[i]=hc
mxhc=max(maxprice)
ind=maxprice.index(mxhc)
print("日期：%s,价格最大回撤率%.2f"%(data[ind],mxhc))



    

























































































































     