#製作電子郵件通訊錄

mail = dict()
name = input('請輸入姓名:')
email = input('請輸入email:')
mail[name] = email    #！！
name = input('請輸入姓名:')
email = input('請輸入email:')
mail[name] = email
name = input('請輸入姓名:')
email = input('請輸入email:')
mail[name] = email

want = input('請輸入要查詢電子郵件的姓名:')
print(mail[want])