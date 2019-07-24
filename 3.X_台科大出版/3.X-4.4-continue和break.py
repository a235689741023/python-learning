"""
break  >>  跳脫 最近的一層 迴圈，將控制權交給 迴圈區塊外的下一行

continue  >>  放棄  同一層迴圈  在continue以下的指令，跳回同一層迴圈  最上面  for或while那一行繼續執行

"""

# break
for x in range(1, 10):
    if x == 5:
        break
    print( x, end="  ")

print()

# continue
for x in range(1, 10):
    if x == 5:
        continue
    print( x, end="  ")

