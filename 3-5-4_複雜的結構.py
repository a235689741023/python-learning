# tuple, 串列, set, 字典 >>都可互相包含組成更大的結構

星期 = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
月份 = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

dic = {'week':星期, 'month':月份}   # 直接形成字典ww
print(dic['month'])     #注意取出方式！
print(dic['month'][7])