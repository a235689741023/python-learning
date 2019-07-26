# 建立字串
str1 = "I'm all right, but it's raining."
str2 = 'I\'m all right, but it\'s raining.'
print(str1)
print(str2)

str3 = "Hello!\nHow are you?"
print(str3)

str4 = str(123)  # str()  轉換成字串

str5 = "What's wrong with you? \
Nothing!"                           #印出來還是在同一行
print(str5)

title = """                     
末祝
        2019
                新年快樂"""
print(title)                       #用 3個引號 固定多行輸出的格式


#跳脫字元
print(" \ ")  #倒斜線
print(" \' ")  #單引號
print(" \" ")   #雙引號
print(" \b ")   #退後 (backspace鍵)
print(" \n ")   #換行
print(" \t ")    #定位 (tab鍵)
print(" \u1024 ")    #  \u加上4個16進位數，表是一個Unicode字符


#顯示特殊字元
str1 = "Never say \tNever!\nNever say \"Impossible!\" \u2665 "  #印出愛心
print(str1)
str2 = "Never say Never\b\b\b\b\b"  # \b 將Never刪除了
print(str2)
str3 = "c:\\temp"  #因為 \t 是跳脫字元，前面必須再加一個 \ 才能印出
print(str3)
str4 = r"c:\temp"  #在字串前加 前置字元r  >> 也可以正確印出 \t
print(str4)
