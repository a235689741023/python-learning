#字典(dict)   # {鍵 : 值}

dict1 = {}
print(dict1)
lang = {'早安':'Good Morning','你好':'Hello'}
print(lang)

print('「你好」的英文為', lang['你好'])  # 用 字典[鍵]  讀取對應的值
#print('「你好嗎」的英文為', lang['你好嗎'])      #不存在字典裡 >> KeyError

print('「你好」的英文為', lang.get('你好'))  # 用 .get(鍵)  函式讀取對應的值
print('「你好嗎」的英文為', lang.get('你好嗎'))  #不存在字典裡 >> 回傳 None
print('「你好嗎」的英文為', lang.get('你好嗎','不在字典裡'))   #第一個鍵不存在 >> 回傳輸入的第二個參數


lang['你好'] = 'Hi'   #  字典['鍵] = 值  >>修改值，if原先鍵不存在>>新增
print(lang)
lang['學生'] = 'Student'
print(lang)


del lang['早安']   # del 字典['鍵']  >>刪除鍵and對應的值
print(lang)

lang.clear()   #函式 .clear()  清空整個字典
print(lang)


# 函式 dict() 將tuple或串列 轉換成字典 >>前者轉換成鍵，後者轉換成值
a = [['早安','Good Morning'],['你好','Hello']]
dict1 = dict(a)
print(dict1)
b = [('早安','Good Morning'),('你好','Hello')]
dict2 = dict(b)
print(dict2)
c = (['早安','Good Morning'],['你好','Hello'])
dict3 = dict(c)
print(dict3)
d = (('早安','Good Morning'),('你好','Hello'))
dict4 = dict(d)
print(dict4)


# 函式 dict1.update(dict2)  合併兩個字典 >>若有重複的鍵，dict2的鍵and值會取代dict1的
lang1 = {'你好':'Hello'}
lang2 = {'學生':'Student'}
lang1.update(lang2)
print(lang1)
lang1 = {'早安':'Good Morning','你好':'Hello'}
lang2 = {'你好':'Hi'}
lang1.update(lang2)
print(lang1)

#函式 dict1 = dict2.copy()  複製dict2到dict1，指向不同物件
# 用 dict1 = dict2  >>指向同一個物件 >>同步修改
lang1 = {'早安':'Good Morning','你好':'Hello'}
lang2 = lang1
lang2['你好'] = 'Hi'
print('lang1為',lang1)
print('lang2為',lang2)
lang1 = {'早安':'Good Morning','你好':'Hello'}
lang3 = lang1.copy()
lang3['你好'] = 'Hi'
print('lang1為',lang1)
print('lang3為',lang3)


# 用 for 讀取字典每個元素
lang = {'早安':'Good Morning','你好':'Hello'}
for ch,en in lang.items():  #搭配函式 .items()  >>讀取 鍵and值
    print('中文為',ch,'英文為',en)
for ch in lang.keys():  #搭配函式 .keys() >>讀取 鍵
    print(ch, lang[ch])
for en in lang.values():  #搭配函式 .values() >>讀取 值
    print(en)
