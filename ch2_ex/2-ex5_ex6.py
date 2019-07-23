#電腦資料儲存單位
print('1 KB=', 2**10, 'byte')
print('1 MB=', 2**20, 'byte')
print('1 GB=', 2**30, 'byte')
print('1 TB=', 2**40, 'byte')
print('1 PB=', 2**50, 'byte')
print('1 EB=', 2**60, 'byte')
print('1 ZB=', 2**70, 'byte')
print('1 YB=', 2**80, 'byte')


#字串處理                                                           #重要！
s = input('請輸入字串:')  #直接輸入ww
word = s.split(' ')
print('以空白字元切割後，得到的單字:', word)
s2 = ' '.join(word)
print('還原字串:', s2)
print('全部轉換成大寫:', s2.upper())