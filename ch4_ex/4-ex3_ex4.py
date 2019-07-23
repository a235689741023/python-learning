#體溫與發燒
t = float(input('請輸入體溫?'))
if (t<36) :
    print('體溫過低')
elif (t<38) :
    print('體溫正常')
elif (t<39) :
    print('體溫有點燒')
else:
    print('體溫很燒')


#閏年判斷
y = int(input('請輸入年分(西元):'))
if (y%400 == 0):
    print('閏年')
elif (y%4==0)and(y%100!=0):
    print('閏年')
else:
    print('平年')
