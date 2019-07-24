"""
迴圈三要素:
1. 變數起始值
2. 迴圈條件式
3. 調整變數增減

# while迴圈
while  條件判斷式:
    指令

#for 迴圈
for  變數  in  序列:
    指令
else: (可省略)
    指令
"""
# for迴圈
x = "abcdefg"
x = ['Friday', 'Saturday', 'Sunday']
x = [1, 2, 3, 4, 5]
for i in x:
    print(i)

# range()  函數 >> 讓數字串列更有效率
#  range( (起始值),  終止值  (,  增減值))
#數字串列 由起始值到 終止值前一個
sum = 0
for count in range(0, 21, 5):
    sum += count
print("5的倍數累加結果為:", sum)

# 找元素索引值 >> enumerate函數
# for  索引值,  變數  in  enumerate( 序列 )
names = ['Eileen', 'Jennifer', 'Brian']
for index,x in enumerate(names):
    print("{0}---{1}".format(index, x))

#巢狀迴圈
for x in range(1,10):
    for y in range(1,10):
        print("{0}*{1} = {2:^2}".format(x, y, x*y), end="  ")
    print()





