shoplist = ['milk', 'egg', 'coffee', 'watermelon' ]
shoplist.sort()                  # .sort() 排序
print('執行shoplist.sort()後')
print('shoplist為', shoplist)


shoplist = ['milk', 'egg', 'coffee', 'watermelon' ]
for item in shoplist:    # for 變數 in 串列 :  >>讀取所有元素到變數
    print(item)


shoplist1 = ['牛奶', '咖啡', '蛋']
shoplist2 = ['西瓜', '鳳梨']
shoplist_all = shoplist1 + shoplist2    #用 + 串接兩個串列
print('串接後的字串為', shoplist_all)

#產生串列1
list1 = list('python')    # 函式 list()  >>可放入字串或tuple
print(list1)
tuple2 = ('a', 'b', 1, 2)
list2 = list(tuple2)
print(list2)

#產生串列2
list3 = "2016/1/1".split('/')   #函式 .split() 會回傳串列
print(list3)


#使用 [開始 : 結束 : 間隔]  存取串列！

#拷貝串列 1
list1 = [1, 2, 3, 4]
list2 = list1    #用 =  >>兩串列指向  同一  物件 >>其中一個修改，兩個都會改變
print('list1 =', list1, 'list2 =', list2)
list1[2] = 19
print('list1 =', list1, 'list2 =', list2)

#拷貝串列 2
list1 = [1, 2, 3, 4]
list3 = list1[:]
list3[2] = 19
print('list1 =', list1, 'list3 =', list3)     #用  [:]  或  .copy()  拷貝>>只會更改個別項目
list4 = list1.copy()
list4[2] = 19
print('list1 =', list1, 'list4 =', list4)
