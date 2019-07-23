# 4-1 單向選擇
# if條件判斷:
#     條件成立敘述

# 以「4個空白鍵」or tab鍵 縮行開頭，但整個程式只能擇一使用

score = int(input('請輸入成績:'))
if score >= 60 :
    print("很好，繼續保持下去")


#4-2 雙向選擇
# if條件判斷:
#     條件成立敘述
# else:
#    條件不成立敘述

cost = int(input('請輸入購買金額?'))
if cost >= 2000:
    print(cost * 0.9)
else:
    print(cost)

# 判斷奇偶
num = int(input('請輸入數字:'))
if num%2 :    #
    print(num, '是奇數')
else:
    print(num, '是偶數')

#三角形判斷
a = int(input('輸入三角形邊長a = '))
b = int(input('輸入三角形邊長b = '))
c = int(input('輸入三角形邊長c = '))
if (a+b>c)and(a+c>b)and(b+c>a):
    print('三角形成立')
else:
    print('三角形不成立')
