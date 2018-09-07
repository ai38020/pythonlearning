from collections import namedtuple
person = namedtuple('person','name age sex')
xm = person ('xiaoming','20','male')
x = "{p.name} {p.age} old this year".format (p=xm)
print (x)
