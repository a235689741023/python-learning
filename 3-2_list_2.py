

shoplist = ['牛奶','蛋','咖啡豆','西瓜','鳳梨']
shoplist.remove('蛋') #.remove()將指定元素移除
print("執行shoplist.remove('蛋')後")
print('購物清單shoplist為',shoplist)

del shoplist[0]  #del 串列[索引值] >>將第幾個元素刪除
print("執行del shoplist[0]後")
print('購物清單shoplist為',shoplist)
print('\n') #換行




#shoplist = ['牛奶','蛋','咖啡豆','西瓜','鳳梨']
shoplist.pop(0)
print("執行shoplist.pop(0)後")      #.pop()將第幾歌個元素刪除
print('購物清單shoplist為',shoplist)
shoplist.pop()  #若不指定>>刪除最後一個
print("執行shoplist.pop()後")
print('購物清單shoplist為',shoplist)
shoplist.pop(-1)
print("執行shoplist.pop(-1)後")
print('購物清單shoplist為',shoplist)

