"""
政府資料開放平台  https://data.gov.tw/
提供 XML、JSON、CSV檔案格式

XML
可延伸標記語言 (Extensible Markup Language)
允許使用者自定義標籤(tags)，可定義每種商業文件的格式
在不同應用程式中都能使用(可跨平台)，容易設計
XML >>以結構and資訊內容為導向，由標籤定義出文件的架構 (樹狀結構)
HTML >>只能定義文件格式

JSON
JavaScript的物件表示法  (JavaScript  Object  Notation)
輕量的資料交換格式，適用於網路資料傳輸
形式1：串列(陣列)  >> [] 裡包含物件集合(collection)，每組集合用逗號分隔
形式2：物件  >> {}裡包含 名稱and值  >> {name:value}

XML  >>需解析標記
JSON >>檔案格式小，容易解析

擷取步驟
XML：  取出url(網頁)內容 >> 用 BeautifulSoup 模組解析XML標記 >> 儲存為CSV檔
JSON：  取出 url 內容  >> 用 json 模組 解析JSON資料 >> print輸出

Python 抓取網頁資料have多種模組
這裡使用  urllib.request 模組  >>只要將網址傳入 urlopen函數 就會傳回 HttpResponse物件，接著可使用 read() 讀取網頁內容

Python 提供多種爬蟲(Crawl)模組
HTML、XML屬於 標記結構 >>適用 BeautifulSoup 模組
JSON格式 >>直接用 json 模組


BeautifulSoup 常用的方法與屬性
title屬性     回傳網頁標題      data.title
text屬性      除去所有標記，只傳回內容    data.text
find方法      傳回第一個符合條件的字串物件      data.find('SiteName')
find_all方法      傳回所有符合條件的字串物件      data.find_all('SiteName')
select方法        傳回CSS選擇器篩選的所有內容     data.select('#id')
get_text方法      傳回字串物件的標記內容     data.find('SiteName').get_text()
#利用for迴圈取出所有標記內容
取出資料如果還有其他用途，可以將它儲存為 CSV檔

"""
#XML 擷取資料
od_url = "https://opendata.epa.gov.tw/ws/Data/AQI/?$format=xml"

import urllib.request as ur

with ur.urlopen(od_url) as response:
    get_xml = response.read()

from bs4 import BeautifulSoup

data = BeautifulSoup(get_xml, 'xml') #
SiteName = data.find_all('SiteName')
County = data.find_all('County')
Status = data.find_all('Status')
pm25 = data.find_all('PM2.5')
PublishTime = data.find_all('PublishTime')

csv_str = ""
for i in range(0, len(SiteName)):
    csv_str += "{}, {}, {}, {}\n".\
        format(SiteName[i].get_text(),\
               County[i].get_text(),\
               Status[i].get_text(),\
               pm25[i].get_text(),\
               PublishTime.get_text())

with open("pm_xml.csv", "w") as f:    #寫入檔按
    story = f.write(csv_str)
print("完成")

