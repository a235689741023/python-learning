#Python >> 動態語言，不用事先宣告，可用 = 隨時改變變數所參考的物件

a = 1
print(a, id(a))
a = 'Python'
print(a, id(a))    # id() >>物件編號，相同的編號指向相同物件

x = 1
y = x
print(id(x), id(y))
print(x, y)

#變數的命名