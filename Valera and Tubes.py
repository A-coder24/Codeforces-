import sys
import math
import bisect
input = sys.stdin.readline
############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))
def printlist(var) : sys.stdout.write(' '.join(map(str, var))+'\n')

n,m,k=invr()
d=[]
for i in range(1,n+1):
    if i%2!=0:
        for j in range(1,m+1):
            d.append(i)
            d.append(j)
    else:
        for j in range(m,0,-1):
            d.append(i)
            d.append(j)
r=0
for i in range(k-1):
    print(2,d[r],d[r+1],d[r+2],d[r+3])
    r+=4
print((len(d)-r)//2,*d[r:])








