# 找出及格的人

全班 = set(['John', 'Mary', 'Tina', 'Fiona', 'Claire', 'Eva', 'Ben', 'Bill', 'Bert'])
英文及格 = set(['John', 'Mary', 'Fiona', 'Claire', 'Ben', 'Bill'])
數學及格 = set([ 'Mary', 'Fiona', 'Claire', 'Eva', 'Ben',])

print('兩科都及格:', 英文及格&數學及格)
print('數學不及格:', 全班-數學及格)
print('英文及格且數學不及格', 英文及格-數學及格)
