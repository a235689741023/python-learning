#指定
# = >> 等號右邊先運算，再指定給左邊

#算數
# +  # +=
# -  # -=
# *  # *=
# / 浮點除法  # /=
# // 整數除法(去掉小數點)  # //=
# % 求餘數  # %=
# ** 次方  # **=


#位元
# & 位元且
# | 位元或
# ^ 位元互斥或   一個T、一個F >>才設為True
# ~ 位元取相反
# << 位元左移   101<<2 = 10100
# >> 位元右移   0101>>2 = 0001


#比較
A = (5<2)
print(A)
# <
# >
# <=
# >=
# !=
# ==
A = (5!=2)
print(A)
A = (5==2)
print(A, end='\n\n')


#邏輯
# and
# or
# not非


# in 與 is 運算子 (回傳True和False)
# x in y  >> x是否為y的一個元素
# x is y  >> 兩物件的id是否相同
# in
x = 1
y = [1, 2, 3]
print(x in y)
# not in
print(x not in y)
# is
x = [1, 2, 3]
print(x is y)
# is not
print(x is not y)

# x==y >>只要數值相同就True
# x is y >>必須參考同一物件
x = [1, 2, 3]
y = [1, 2, 3]
print(id(x), id(y))
print(x is y)
print(x == y)



#運算子優先順序
# ()  []  {鍵:值}  {}
# **
# +x  -x  ~x
# *  /  //  %
# +  -
# <<  >>
# &
# ^
# |
# <  <=  >  >=  ==  !=  in    not in    is     is not    not
# and
# or
# if  elif  else
# lambda 匿名函式



