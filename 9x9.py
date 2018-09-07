from __future__ import print_function
j = 2
for i in range(1,10):
    for k in range(1,j):
        print(k,'x',i,'=',i*k,end="\t")
    j+=1
    print("\n")
