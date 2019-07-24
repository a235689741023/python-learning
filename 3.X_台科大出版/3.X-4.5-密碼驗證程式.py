count = 0
password = 1234
while count<3 :
    guess = int(input("請輸入密碼: "))
    if guess==password:
        print("密碼正確！！")
        break
    else:
        print("密碼錯誤！！")
    count+=1
    if count==3:
        print("密碼錯誤三次，取消登入")
