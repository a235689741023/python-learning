# 被 單引號、雙引號 包夾的文字
s1 = '作者"孟浩然" 詩名"春曉"'
print(s1)
s2 = '作者"孟浩然" 詩名"春曉"'
print(s2)

# 三個單引號'''、 三個雙引號""" >>顯示多行文字 >>空白、換行 會正常顯示
s3 = '''        春眠不覺曉，處處聞啼鳥。
        夜來風雨聲，花落知多少。
        
        詩名"春曉"  作者"孟浩然"'''
print(s3)




#字串運算子

# 1.串接 >> 用 +
s1 = '01234'
s2 = '56789'
s3 = s1 + s2
print(s3)

# 2.存取 >> 用 [] >> s[0]存取第1個，s[-1]存取最後1個，s[-2]存取倒數第2個
s1 = '0123456789'
print(s1[0])
print(s1[1])
print(s1[-1])
print(s1[-2])

# 3.複製 >> 用 *
s2 = s1 * 2
s3 = s1 * 3
print(s2, s3)

# 4.切割 >> 用 [開始:結束:間隔]  >> 從開始到結束(不包含結束字元) 每隔[間隔]個字元 取出一個字元
# s[:] >>取s的每一個元素
# s[開始:] >>取從[開始]到s結尾的所有元素
# s[:結束] >>取從s[0]到 [結束]前一個元素 的所有元素
# s[開始:結束] >>取從[開始]到 [結束]前一個 為止的所有
# s[::-1]  >>反轉字串！    結果會和 s[-1::-1]一樣ww
# 若[間隔]>0  由左到右取出， 若[間隔]<0  由右到左取出

# 5.串接多行 >> 用 \  >> 上一行的最後用\ , 則下一行會被視為與上一行是同一行
s = '春眠不覺曉，處處聞啼鳥。\n\
夜來風雨聲，花落知多少。\n\
\n\
\t詩名"春曉"  作者"孟浩然"'
print(s)                        # \t >> 空出8個半形字元


