"""
取得字串中的字元
1. 透過索引值(index)
2. 使用切片(slice)  >>取某段字串
3. 使用 split()  >>分割字串

字串不能賦予值(會發生錯誤)，if重新賦予 >>是建立新字串 而非修改原字串
"""

# index
str1 = "Hello"
print(str1[0])
print(str1[-1])

# slice
# 字串[ 起始: 結束: 間隔]

# split
# 字串.split( 分割符號, 分割次數)
str2 = "Do \none \nthing \nat a time!"
print(str2.split())    # 沒有指定 >>以 空格 和 換行符號(\n)  分割
print(str2.split(' ', 1))


# 將26個小寫英文字母反轉輸出
letters = ""
for x in range(97, 123):    #小寫字母97~122，大寫字母65~90
    letters += str(chr(x))   #  chr() 回傳ASCll對應的字元，ord() 回傳字元對應的ASCll碼
print(letters)

revletters = letters[::-1]
print(revletters)

# 將數字反轉輸出
letters = ""
for y in range(48, 58):    #數字 48~57
    letters += str(chr(y))
print(letters)

revletters = letters[::-1]
print(revletters)

# .join()  連結字串
