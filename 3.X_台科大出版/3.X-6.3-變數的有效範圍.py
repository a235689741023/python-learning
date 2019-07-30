"""
全域(Global)變數  >>宣告在 程式區塊和函式之外，都可以用。使用需相當謹慎
區域(Local)變數  >>適用於所宣告的函數或流程控制的程式區塊，離開此範圍就會結束生命週期

"""
def global_local():
    num=100
    print('num =', num)
num = 500
global_local()    #程式中有相同名稱的全域變數與區域變數 >> 以 區域變數  優先
print('num =', num)

print()
def global_local():
    global num         #如果要在函數內使用全域變數  >>需在函數中 以global宣告
    print('num =', num)
    num=100
num = 500
global_local()
print('num =', num)


