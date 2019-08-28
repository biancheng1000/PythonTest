#coding=utf-8

#练习2.1 模拟手机充值
print('欢迎使用XXX冲值业务，请输入充值金额')
inputValue = int(input())
print('充值成功，您本次充值%d元' % (inputValue))

#练习2.2 绘制《植物大战僵尸》中的石头怪
print("  * * * * ")
print(" *       *")
print("*  @   @  *")
print("*         *")
print("*    @    *")
print(" *       * ")
print("  * * * * ")
print("")
print("")

#练习2.3 根据父母身高预测儿子的身高
print("请输入父亲的身高:")
fatherHeight=float(input())
print("请输入母亲的身高:");
matherHeight=float(input())
print("预测儿子的身高为:%.2f"%((fatherHeight+matherHeight)*0.54))

#练习2.4 根据总步数计算消耗的热量值
print("请输入当天行走的步数：")
steps=float(input())
print("今天共消耗卡路里：%.2f千卡"%((steps*28)/1000))