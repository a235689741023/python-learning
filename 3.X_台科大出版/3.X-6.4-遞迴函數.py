"""
引用自身函數
任何可用選擇結構or重複結構編寫的程式，皆可用遞迴

1. 一個可以反覆執行的遞迴過程
2. 一個跳出執行的出口
"""
def factorial(i):
    if i == 0:
        return 1
    else:
        ans *= factorial(i-1)
    return ans
#以for計算 階乘
sum = 1
n = int(input('請輸入n = '))
for i in range(0, n+1):
    for j in range(i, 0, -1):    #注意ww
        sum *= j
    print('%d! = %3d' % (i, sum))
    sum = 1


# Direct  Recursion
#  Indirect  Recursion  >>呼叫其他遞迴函數，再從其他遞迴函數呼叫原來的遞迴函數


#費伯那序列
def fib(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fib(n-2)+fib(n-1)
n = int(input('輸入要計算第幾個費氏數列:'))
for i in range(n+1):
    print('fib(%d) = %d' % (i, fib(i)))


#河內塔
def hanoi(n, p1, p2, p3):
    if n==1:
        print("套環從 %d 移到 %d" % (p1, p3))
    else:
        hanoi(n-1, p1, p3, p2)
        print("套環從 %d 移到 %d" % (p1, p3))
        hanoi(n-1, p2, p1, p3)
j = int(input("請輸入套環數量"))
hanoi(j, 1, 2, 3)
