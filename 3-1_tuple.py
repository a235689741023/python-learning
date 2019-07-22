#tuple

t1 = ()
print(t1)


t2 = 1,2,3
print(t2)


t3 = (1, 2, 3)
print(t3)
print(t3[0])
#unpacking
a, b, c = t3
print('a=', a, 'b=', b, 'c=', c)


a = 10
b = 20
print('交換前：a=',a,',b=',b)
a, b=b, a                     #直接用tuple交換
print('交換後：a=',a,',b=',b)


list = [1, 2, 3, 4]
t4 = tuple(list)    #用函式tuple()，將串列換成tuple
print(t4)

t5 = (t4, 5, 6)  #tuple內部的tuple會被視為一個元素
print(t5)
print(len(t5))
print(t5[0][0])  #存取內部的tuple需要用2個[]存取

t6 = ('z',)  #如果tuple只有一個元素>>需在元素後面加上逗點
print(t6)
t7 = ('z')  #不是tuple
print(t7)
