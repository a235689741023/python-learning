"""
參數傳遞方式*2 (大多程式語言)
1.  傳值呼叫( Call by value)  >>將引數的值一一複製給函數的參數，在函數中對參數值做修改 不會影響原來的引數值
2.  傳址呼叫( Pass-by-reference)  >>傳給函數的參數值是變數的記憶體位址，引數與參數共享同一塊記憶體位置，兩者值的變動同步

Python的引數傳遞 >>不可變物件 and 可變物件
1. 不可變物件 (Immutable Object)  >>數值、字串  >>近似 傳值
2.  可變物件 (Mutable Object)  >>串列  >>以 傳址 處理

"""

def passFun(name, score):
    name = 'Micheal'
    print("函數內部修改過的名字和分數")
    print("===========")
    print("名字: ", name)
    score.append(85)     #新增一個成績分數，會同步更動函數的串列值
    print("分數: ", score)
name1 = "Andy"
score1 = [56, 84, 63]
print('函數呼叫前的名字和分數')
print("名字: ", name1)
print("分數: ", score1)
passFun(name1, score1)

print("函數內部被修改過的名字和分數")
print("可以注意到名字沒變，但分數被修改了")
print("名字: ", name1)
print("分數: ", score1)
