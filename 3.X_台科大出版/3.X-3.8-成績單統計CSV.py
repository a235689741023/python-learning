"""
CSV (Comma-Seperated Values) >> 常見的open data格式，欄位間以 逗號 分隔，純文字檔
Python內鍵csv模組 >>處理CSV

csv模組用法:

import  csv   #載入csv.py

with  open  ("scores.csv",  encoding="utf-8")  as  csvfile :    #開啟檔案指定為csvfile
    reader  =  csv.reader(csvfile)    #回傳reader物件  >> 變成 字串list物件    #第一個reader只是變數名稱
    for  row  in  reader:                #for迴圈  逐行讀取資料
        XXXXXXX

！！如果CSV檔案和.py檔案放在不同資料夾 >> 必須加入檔案路徑
"""

# 使用  with  指令開啟檔案
f = open("scores.csv")   #開啟
csvfile = f.read()   #讀取
f.close()            #關閉  #如果close前發生錯誤，close就不會執行  >>用 with 解決( 檔案開啟後程式異常會自動調用close() )


#成績單統計小幫手
import csv

print("{0:<3}{1:<5}{2:<3}{3:<5}{4:<5}".format("", "姓名", "總分", "平均", "等級"))
with  open  ("scores.csv",  encoding="utf-8")  as  csvfile :    #開啟檔案指定為csvfile
    x = 0
    for row in csv.reader(csvfile):
        if x>0:
            scoreTotal = int(row[1]) + int(row[2]) + int(row[3])
            average = round(scoreTotal / 3, 1)   #取到 小數點後第一位

            if average >= 80:
                grade = "甲"
            elif 60 <= average < 80:
                grade = "乙"
            elif 50 <= average < 60:
                grade = "丙"
            else:
                grade = "戊"
        x += 1
