"""
+  串接字串
*   重複字串

比較運算子( Unicode值 )
'0'~'9'  <  'A'~'Z'   < ' a'~'z'
x < y <= z

in 與  not in

用 . 取得物件(object)
len() 函數

about 大小寫 的方法
captalize()     只有第一個單字的字首大寫
lower()         將字母轉成小寫
upper()         將字母轉成大寫
title()         每個單字的字首大寫
islower()       判斷字串是否所有字元皆是小寫
isupper()       判斷字串是否所有字元皆是大寫
istitle()           判斷字串首字元是否為大寫，其餘皆小寫
"""
print('快樂' > 'Happy')

s = "The first wealth is health\u266C"
print(" {} 長度是 {}".format(s, len(s)))

str1 = "Do one thing at a time!"
str2 = str1[13:]
str_w = len(str2)
print("取出字串= 「{}」, 長度：{}".format(str2, str_w))


#搜尋特定字串出現次數  count()
#  目標字串.count( 特定字串 [, 開始索引 [, 結束索引 ] ] )

#移除字串左右特定字元  strip()  rstrip()  lstrip()
# 字串.strip( [特定字元] )
#特定字元 >> 預設為空白字元，可輸入多個


#字串替換  replace()
# 字串.replace( 原字串, 新字串 [, 替換次數] )
str = "蘋果可以做成蘋果汁、蘋果乾和蘋果沙拉"
s = str.replace("蘋果", "葡萄")
print(s)

#搜尋字串  find()  index()
#  str.fine( 字元或字串 [, 開始索引 [, 結束索引] ] )    尋找特定字元/串
#  str.index( 字元或字串 [, 開始索引 [, 結束索引] ] )     回傳指定字元/串的索引值
#找不到 >> find()回傳-1，index()則是ValueError訊息

# startswith( 開頭的字元 [, 開始索引 [, 結束索引] ] )
# endswith( 結尾的字元 [, 開始索引 [, 結束索引] ] )


# Python內建文字檔案的函數，不需import其他模組
# open() 開啟檔案，第一個參數是檔名，第二個參數是 使用文字檔的方法
#  r讀取  w寫入模式開啟檔案    a寫入(寫入的資料附加在現有內容之後)    r+讀取與寫入
with open("redcap.txt", "r") as f:
    story = f.read()   #讀出檔案內容

words = ["grandma", "wolf", "Little Red Riding Hood"]

for w in words:
    sc = story.count(w)
    print("{} 出現了 {} 次".format(w, sc))

