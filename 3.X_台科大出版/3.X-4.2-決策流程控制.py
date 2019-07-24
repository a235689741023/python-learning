"""
if 判斷式:
    指令
else:
    指令

# if...else條件表達式
X  if  C  else  Y


#多重選擇
if  判斷式1:
    指令
elif 判斷式2:
    指令
else:
    指令


# 巢狀if

"""

# if...else條件表達式
print('{0}'.format("偶數" if (X % 2)==0 else "奇數"))


#偵測目前時間 決定問候語
import time

print("現在時間: {}".format( time.strftime("%H:%M:%S")))
h = int(time.strftime("%H"))

if h>5 and h<11:
    print("早安！")
elif h>=11 and h<18:
    print("午安！")
else:
    print("晚安！")
