#找出兩首詩共同的字

p1 = '紅豆生南國，春來發幾枝？願君多采擷，此物最相思。'
p2 = '春眠不覺曉，處處聞啼鳥。夜來風雨聲，花落知多少。'
set1 = set(p1)
set2 = set(p2)
set1.remove('，')
set1.remove('。')
set1.remove('？')
set2.remove('，')
set2.remove('。')

print(set1&set2)
