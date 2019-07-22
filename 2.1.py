#bool()

#視為False >> False, 0(整數), 0.0(浮點數), None, ()空tuple, []空串列, {}空字典, ''空字串
print(bool(1))
print(bool(0))
print(bool())


#int() 整數 (可輸入 整數、浮點數、整數字串)

#可以任意大！    #只有整數字串can指定基底
print(int(100))
print(int(3.14))
print(int('100', 2)) #表示放入的100是以2進位表示 >> 轉成10進位


#float() 浮點數(可輸入 整數、浮點數、浮點數字串)

print(float(1))
print(float(3.14))
print(float('3.1415'))


#str() 字串(不可變的物件，需用字串物件提供的函式才能修改)

ss = str('Python')
#ss[0] = 'Q'   #不可直接這樣修改

b = True
print(b, type(b))
num = 20
print(num, type(num))
pi = 3.14
print(pi, type(pi))
s = "Hello"
print(s, type(s))    # type() 印出變數的物件所屬類別   