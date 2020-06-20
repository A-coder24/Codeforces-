"""D. AND, OR and square sum
time limit per test2 seconds
memory limit per test512 megabytes
inputstandard input
outputstandard output
Gottfried learned about binary number representation. He then came up with this task and presented it to you.

You are given a collection of n non-negative integers a1,…,an. You are allowed to perform the following operation: choose two distinct indices 1≤i,j≤n. If before the operation ai=x, aj=y, then after the operation ai=x AND y, aj=x OR y, where AND and OR are bitwise AND and OR respectively (refer to the Notes section for formal description). The operation may be performed any number of times (possibly zero).

After all operations are done, compute ∑ni=1a2i — the sum of squares of all ai. What is the largest sum of squares you can achieve?

Input
The first line contains a single integer n (1≤n≤2⋅105).

The second line contains n integers a1,…,an (0≤ai<220).

Output
Print a single integer — the largest possible sum of squares that can be achieved after several (possibly zero) operations.

Examples
inputCopy
1
123
outputCopy
15129
inputCopy
3
1 3 5
outputCopy
51
inputCopy
2
349525 699050
outputCopy
1099509530625
Note
In the first sample no operation can be made, thus the answer is 1232.

In the second sample we can obtain the collection 1,1,7, and 12+12+72=51.

If x and y are represented in binary with equal number of bits (possibly with leading zeros), then each bit of x AND y is set to 1 if and only if both corresponding bits of x and y are set to 1. Similarly, each bit of x OR y is set to 1 if and only if at least one of the corresponding bits of x and y are set to 1. For example, x=3 and y=5 are represented as 0112 and 1012 (highest bit first). Then, x AND y=0012=1, and x OR y=1112=7.

"""
n=int(input())
arr=list(map(int,input().split()))
s=[0]*20
for i in arr:
    num=i
    t=0

    while(num > 1):
        s[t]+=num%2
        num=num//2
        t+=1
    
    s[t]+=num%2
total=0
while(s!=[0]*20):
    ans=""
    for i in range(20):
        if s[i] >0:
            ans+="1"
            s[i]-=1
        else:
            ans+="0"
    total+=pow(int(ans[::-1],2),2)
print(total)

     