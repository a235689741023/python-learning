"""
for  變數  in   序列:   (序列可以是list、str、tuple、range)
    程式指令

range( [start],  stop  [, step] )

"""
def pyramid():
    h =int(input("請輸入層數: "))
    s =input("請輸入符號: ")

    for n in range(1, h+1):
        str ="{0}{1:^20}"
        print(str.format(n, s*(n*2-1))) #注意這裡

pyramid()
user = input("按x鍵離開，按任意鍵繼續 ")
while (user != "x"):
        pyramid()
        user = input("按x鍵離開，按任意鍵繼續 ")
print("Goodbye!")



