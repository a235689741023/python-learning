"""
格式參數：
%a      星期縮寫
%A      完整星期名
%b      月份縮寫
%B      完整月份名
%c      日期與時間  ex:  Mon Apr 01 16:43:52 2017
%d      月的第幾天
%U      年的第幾週
%w      週的第幾天(0~6，0為星期天)
%Y      西元年
%y      西元年末兩位數
%m      月份(01~12)
%H      小時，24小時制(00~23)
%I      小時，12小時制(01~12)
%M      分鐘(00~59)
%S      秒數(00~61，允許閏秒)
%p      AM. 或 PM.
"""

import time
print(time.strftime("%A, %b %d %H:%M:%S"))