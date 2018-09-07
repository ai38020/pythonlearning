import re
data = "what is python 2.7.13 and Python 3.6.0 ?"
a = re.findall('python [0-9]\.[0-9]\.[0-9]', data, flags=re.IGNORECASE)
print(a)

re_obj = re.compile('python [0-9]\.[0-9]\.[0-9]', flags=re.IGNORECASE)
b = re_obj.findall(data)
print(b)

c = re.match('what', data)
print (c)

d = re.match('\d+',"123 is one")
print (d)
d.start()

e = re.sub('[0-9]\.[0-9]\.[0-9]','x.x.x',data)
print (e)