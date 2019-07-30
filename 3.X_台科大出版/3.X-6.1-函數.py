"""
def  函數名稱( 參數1, 參數2, ....)
    程式指令
    return   回傳值   #有回傳值才需要  #如果沒有回傳值>>回傳None

"""
def func(a,b):
    x = a + b
    return x
print(func(1,2))


#位置引數
def func(a,b,c=0):  #預設引數
    x = a + b + c
    return x
print(func(1,2,3))
print(func(1,2))


#關鍵字引數
def func(a,b,c):
    x = a + b + c
    return x
print(func(c=2,b=3,a=1))
print(func(1,c=3, b=2))  #混用 >> 位置引數must在關鍵字引數之前

#任意引數串列
#事先不知道要傳入的引數個數
#  *參數  >>傳入的引數視為  一組tuple
#  **參數  >>傳入的引數視為  一組dict(字典)
def func(*num):
    total = 0
    for n in num:
        total += n
    return total
print(func(1,2))
print(func(1,2,3))
print(func(1,2,3,4))

def func(**num):
    return num
print(func(a=1,b=2,c=3))

#函數的回傳值
def func(x):
    if x<10:
        return x
    else:
        return "Over"
a= func(15)
print(a)
print(type(a))

def func(a,b):
    n = a + b
    x = a * b
    return n,x   #可一次回傳多個值，需用逗號分隔
num1, num2 = func(10,20)
print(num1)
print(num2)


#分帳程式
def SplitBill():
    bill = float(input("帳單金額: "))
    split = float(input("分帳人數: "))
    tip = 0.1
    total = bill*(1+tip)
    each_total = total / split
    each_pay = round(each_total, 0)
    return each_total, each_pay
e1, e2 = SplitBill()
print("每人應付 {}, 應付: {}".format(e1, e2))


