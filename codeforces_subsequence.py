"""B. Codeforces Subsequences
time limit per test2 seconds
memory limit per test512 megabytes
inputstandard input
outputstandard output
Karl likes Codeforces and subsequences. He wants to find a string of lowercase English letters that contains at least k subsequences codeforces. Out of all possible strings, Karl wants to find a shortest one.

Formally, a codeforces subsequence of a string s is a subset of ten characters of s that read codeforces from left to right. For example, codeforces contains codeforces a single time, while codeforcesisawesome contains codeforces four times: codeforcesisawesome, codeforcesisawesome, codeforcesisawesome, codeforcesisawesome.

Help Karl find any shortest string that contains at least k codeforces subsequences.

Input
The only line contains a single integer k (1≤k≤1016).

Output
Print a shortest string of lowercase English letters that contains at least k codeforces subsequences. If there are several such strings, print any of them.

Examples
inputCopy
1
outputCopy
codeforces
inputCopy
3
outputCopy
codeforcesss
"""



def f():
    return map(int ,input().split())
def lis():
    return list(map(int ,input().split()))
""".........................................."""
from functools import reduce
a=[0]*10
k=int(input())
c=0
s="codeforces"
while reduce(lambda x,y:x*y,a)<k:
	a[c%10]+=1
	c+=1
t=""
 
for i in range(10):
	t+=s[i]*a[i]
print(t)
