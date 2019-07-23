# 可使用多個 if-elif-else

score = int(input('請輸入成績:'))
if score >= 80:
    print('非常好')
elif score >= 60:
    print('還不錯')
else:
    print('要加油')


#郵資計算
w = float(input('請輸入物品重量:'))
if w <= 5:
    print('郵資為50元')
elif w <= 10:
    print('郵資為70元')
elif w <= 15:
    print('郵資為90元')
elif w <= 20:
    print('郵資為110元')
else:
    print('超過20公斤無法寄送')


# BMI計算
w = float(input('請輸入體重(kg)?'))
h = float(input('請輸入身高(m)?'))
bmi = w/(h*h)
print('BMI =', bmi)
if bmi < 18:
    print("體重過輕")
elif bmi < 24:
    print("體重正常")
elif bmi < 27:
    print("體重過重")
else:
    print("體重肥胖")
