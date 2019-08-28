
##练习1：打印象棋口诀
#import re
#rule="马走日，象走田，车走直路炮翻山，士走斜线护将边，小卒一去不回还。"
#pattern=r"[，]"
#result=re.sub(pattern,'，\n',rule)
#print("象棋口诀：")
#print(result)

#练习2：判断车牌归属地
import re
pro="京、沪、津、渝、鲁、冀、晋、蒙、辽、吉、黑、苏、浙、皖、闽、赣、豫、湘、鄂、粤、桂、琼、川、贵、云、藏、陕、甘、青、宁、新、港、澳、台"
newPro= pro.replace("、","|")
print(newPro)
pattern=str.format("r[%s][A-Za-z][.]"%newPro)
print(pattern)

#while True:
#    print("请输入待验证的车牌号码：")


