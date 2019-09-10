##练习1
#class Telephone:
#    def __init__(self,newlangavage=""):
#        Telephone.langvage=newlangavage
#        if newlangavage=="":
#            print("智能手机的默认语言为英文")
#        else:
#            print("将智能手机的默认语言设置为",Telephone.langvage)

#te=Telephone()
#te=Telephone("中文")

##练习2
#class CreditCard:
#    password="123456"
#    def __init__(self,account,password=""):
#        if(password==""):
#            print("信用卡："+account+"的默认密码为："+CreditCard.password)
#        else:
#            print("重置信用卡："+account+"的密码为："+password)
#vd=CreditCard("4013735633800642")
#vd=CreditCard("4013735633800642","1123254")

##练习3 
#class SaleDetail:
#    num=""
#    name=""
#    def __init__(self,num,name):
#        self.num=num
#        self.name=name
#    @property
#    def detail(self):
#        print("商品的编号：{:10s}商品的名称：{:10s}".format(self.num,self.name))

#list={"1":[SaleDetail("T0001","小米1"),SaleDetail("T0002","小米2"),SaleDetail("T0003","小米3")],
#"2":[SaleDetail("T0004","小米4"),SaleDetail("T0005","小米5"),SaleDetail("T0006","小米6")],
#"3":[SaleDetail("T0007","小米7"),SaleDetail("T0008","小米8"),SaleDetail("T0009","小米9")]}

#print("-------------销售明细---------------")
#while True:
#    month= input("请输入要查询的月份:")
#    detail=list.get(month)
#    if detail==None:
#        print("查询的月份不存在!")
#    else:
#        for d in list.get(month):
#            d.detail
#    if month=="0":
#        break
#print("查询结束")

#练习4：
