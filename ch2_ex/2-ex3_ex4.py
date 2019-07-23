#分組報告
num = int(input('請輸入座號:'))
print('組別為', (num-1)//5 + 1)  #先減1 ！！


#買飲料
n = int(input('輸入買的罐數:'))
cost = (n//12)*200 + (n%12)*20
print('需花費', cost, '元')


