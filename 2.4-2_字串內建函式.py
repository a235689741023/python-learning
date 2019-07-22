# 字串.split(切割字元)  >> 將字串以切割字元 切割
s1 ='春眠不覺曉，處處聞啼鳥，夜來風雨聲，花落知多少。'
list1 = s1.split('，')
print(list1)


# 連結字串.join(要串接的串列)  >> 用 連結字串 當中介物，把串列裡的東東串起來
#list1 = ['春眠不覺曉', '處處聞啼鳥', '夜來風雨聲', '花落知多少。']
s2 = '，'.join(list1)
print(s2)


# 字串.replace(原始字串, 取代字串)
s1 ='春眠不覺曉，處處聞啼鳥，夜來風雨聲，花落知多少。'
s3 = s1.replace('春', '冬')
print(s3)


# 字串.find(要找的字串)  >>從 左 邊開始找到第一個出現的 位置值 ，找不到會回傳-1
s1 ='春眠不覺曉，處處聞啼鳥，夜來風雨聲，花落知多少。'
print(s1.find('花落'))


# 字串.rfind(要找的字串)  >>從 右 邊開始找到第一個出現的 位置值 ，找不到會回傳-1
s1 ='春眠不覺曉，處處聞啼鳥，夜來風雨聲，花落知多少。'
print(s1.rfind('花落'))


# 字串.startswith(要找的字串)   >>開頭
s1 ='春眠不覺曉，處處聞啼鳥，夜來風雨聲，花落知多少。'
print(s1.startswith('春眠'))


# 字串.endswith(要找的字串)
s1 ='春眠不覺曉，處處聞啼鳥，夜來風雨聲，花落知多少。'
print(s1.endswith('多少。'))


# 字串.count(要找的字串)  >>要找的字串 出現的次數
print(s1.count('處'))


# 字串.center(數值)  >>保留長度為「數值」的字串空間，將字串 置中 擺放
s1 = '春眠不覺曉'
print(s1.center(10))

# 字串.rjust(數值)  >>保留長度為「數值」的字串空間，將字串 靠右 擺放
print(s1.rjust(10))

# 字串.ljust(數值)  >>保留長度為「數值」的字串空間，將字串 靠左 擺放
print(s1.ljust(10))


# 英文字串.capitalize()  >>將英文字串的 字首 轉換成大寫
s1 = 'an apple a day.'
print(s1.capitalize())

# 英文字串.title()  >>將英文字串 每個單字的字首 轉換成大寫
s1 = 'an apple a day.'
print(s1.title())

# 英文字串.swapcase()  >>將英文字串的每個字母 大小寫互換
s1 = 'An apple a day.'
print(s1.swapcase())

# 英文字串.upper()  >>將英文字串的每個字母 都變大寫
print(s1.upper())

# 英文字串.lower()  >>將英文字串的每個字母 都變小寫
print(s1.lower())


# 字串.zfill(width)  >>在字串左邊 補0,直到整個字串長度為width
s1 = '123'
print(s1.zfill(5))


# 字串.strip(chars)  >>移除字串兩邊 chars指定的字元，字元可以不只1個 >>如果沒指定，則移除空白字元
s1 = '  Hello, Mary.  '
print(s1.strip())

# 字串.lstrip(chars)  >>移除字串 左邊 chars指定的字元，字元可以不只1個 >>如果沒指定，則移除空白字元
s1 = '  Hello, Mary.  '
print(s1.lstrip(' H'))

# 字串.rstrip(chars)  >>移除字串 右邊 chars指定的字元，字元可以不只1個 >>如果沒指定，則移除空白字元
s1 = '  Hello, Mary.  '
print(s1.rstrip(' .'))


