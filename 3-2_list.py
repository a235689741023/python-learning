#串列(list) []

shoplist = ['牛奶','蛋','咖啡豆','西瓜','鳳梨']
print('購物清單shoplist為',shoplist)
#print(shoplist)


print('購物清單shoplist[0]為',shoplist[0])  #讀取元素

print('購物清單shoplist的長度為',len(shoplist)) #len()讀取串列長度


shoplist[1] = '皮蛋' #修改個別元素
print("執行shoplist[1] = '皮蛋'後")
print('購物清單shoplist為',shoplist)


index = shoplist.index('咖啡豆')  #函式.index() >>讀取元素索引值
print("執行index = shoplist.index('咖啡豆')後")
print('index =',index)


shoplist.append('麵包')  #函式.append在串列 最後 增加新元素
print("執行shoplist.append('麵包')後")
print('購物清單shoplist為',shoplist)

shoplist.insert(4, '蘋果')
print("執行shoplist.insert(4, '蘋果')後") #在 指定位置 增加新元素
print('購物清單shoplist為',shoplist)



