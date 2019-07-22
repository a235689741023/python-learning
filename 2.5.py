#2-5-1
clothes = int(input('輸入上衣數量'))
pants = int(input('輸入褲子數量'))
vest = int(input('輸入背心數量'))
total = 300*clothes + 350*pants + 400*vest
print('總共', total, '元', sep='')


#2-5-2
r = float(input('請輸入半徑'))
PI = 3.14159  #設定好PI的值
圓周長 = 2*r*PI
圓面積 = r*r*PI
print('周長=', 圓周長)
print('面積=', 圓面積)


#2-5-3
c = float(input('請輸入攝氏溫度:'))
f = c*9/5 + 32
print('華氏溫度=', f)


#2-5-4 複利計算
money = int(input('請輸入本金:'))
interest = float(input('請輸入年利率(%):'))
y1 = money * (1 + interest/100)
y2 = money * ((1 + interest/100)**2)
y3 = money * ((1 + interest/100)**3)
print('第一年本利和=', y1)
print('第二年本利和=', y2)
print('第三年本利和=', y3)


#2-5-5 迴文！！
s = input('請輸入字串:')
print('判斷結果為', s == s[::-1])



