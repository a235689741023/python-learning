# 集合(set)     #{}
#store沒有順序性的資料

#建立新集合 >> 用 set() 或 {}
s = {1, 2, 3, 4}
print(s)
s = set(('a', 1, 'b', 2))   # set()裡 >>可放 字串,tuple,串列,字典
print(s)
s = set(['apple','banana','apple'])  # 集合會自動刪除重複的元素
print(s)
s = set({'早安':'Good Morning','你好':'Hello'})  #只存取 鍵 到集合裡
print(s)
s = set('racecar')
print(s)


s = set('tiger')
print(s)
s.add('z')  #函式 .add() 新增集合元素
print(s)
s.remove('t')  #函式 .remove() 刪除集合元素
print(s)


# 集合的運算 >> 聯集|  交集&  差集-  互斥或^
a = set('tiger')
b = set('bear')
print('a是', a)
print('b是', b)
print('聯集', a|b)
print('交集', a&b)
print('差集', a-b)
print('互斥或', a^b)


#集合的比較
a = set('tiger')
b = set('tigers')
print('a是', a)
print('b是', b)
print(a<=b)  # 子集合 <=      # A.issubset(B)
print(a.issubset(b))
print(a<b)  #真子集合 <
print(a>=b)  #t超集合 >=     # A.issuperset(B)
print(a.issuperset(b))
print(a>b)  #真超集合 >
