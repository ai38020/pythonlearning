from __future__ import print_function
n = int(input("input length:"))
#n = 4  # type: int
print ('*'*n)
for i in range(n-2):
	print ('*'+' '*(n-2)+'*')
   # print ('*',end='')
   # print (' '*(n-2),end='')
   # print ('*')
else:
    print ('*'*n)