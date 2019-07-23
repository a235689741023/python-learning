#近視判斷
sight = float(input('請輸入視力:'))
if sight < 0.9:
    print('有近視')
else:
    print('視力正常')


#象限判斷
x = float(input('x座標='))
y = float(input('y座標='))
if (x>0)and(y>0):
    print('第一象限')
elif (x<0)and(y>0):
    print('第二象限')
elif (x<0)and(y<0):
    print('第三象限')
elif (x>0)and(y<0):
    print('第四象限')
else:
    print('在坐標軸上')
