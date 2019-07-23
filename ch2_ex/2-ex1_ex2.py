#三數總和與平均
g1 = int(input('輸入第一次期中考成績:'))
g2 = int(input('輸入第二次期中考成績:'))
g3 = int(input('輸入期末考成績:'))
print('總分為', g1+g2+g3, '平均為', (g1+g2+g3)/3)

#英制轉公制
f = int(input('請輸入幾呎:'))
i = int(input('請輸入幾吋:'))
cm = (f*12 + i)*2.54
print('等於', cm, '公分')
