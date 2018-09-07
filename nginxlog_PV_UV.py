from __future__ import print_function

ips = []
with open('userapi_access.log') as f:
    for line in f:
       #line.split( )
        ips.append(line.split ( ) [4])

print("PV is {0}".format(len (ips)))
print("UV is {0}".format(len (set (ips))))
print (set (ips))
#print (line)
#print (ips)
