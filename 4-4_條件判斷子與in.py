# 用 條件判斷和in 測試資料容器 tuple、串列、字典、集合，是否包含某個元素

# tuple
a = (1, 2, 3, 4)
if 1 in a:
    print('數字1在tuple a中')
else:
    print('數字1不在tuple a中')

#串列
a = list('abcdefghijklmnopqrstuvwxyz')
if 'q' in a:
    print('q在串列a中')
else:
    print('q不在串列a中')

#字典
lang1 = {'早安':'Good Morning', '謝謝':'Thank you'}
if '謝謝' in lang1:
    print('謝謝的英文是', lang1['謝謝'])
else:
    print('查不到謝謝的英文')

#集合
a = set('tiger')
if 't' in a:
    print('t在集合a中')
else:
    print('t不在集合a中')
