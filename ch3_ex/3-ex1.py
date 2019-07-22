#存取串列中元素

s = input('請輸入英文句子:')
s.strip('.')  # ！！
word = s.split(' ')
print(word[::-1])

