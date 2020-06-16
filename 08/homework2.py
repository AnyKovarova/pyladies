import re
rc = input('Zadejte rodné číslo (XXXXXX/YYYY): ')

m = re.match(r'^(([0-9]{2})([0-9]{2})([0-9]{2}))\/([0-9]{4})$',rc)

if m is None:
    print('False')

if int(m.group(1) + m.group(5)) % 11:
    print('False')
else:
    print('True')

year = m.group(2)

month = int(m.group(3))
if month > 12:
    sex = 'žena'
    month = month - 50
else:
    sex = 'muž' 

day = m.group(4)

print('Datum narození je: ',day,'/',month,'/',year)
print('Pohlaví je:', sex)