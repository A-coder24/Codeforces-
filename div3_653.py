E1. Reading Books (easy version)
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
Easy and hard versions are actually different problems, so read statements of both problems completely and carefully.

Summer vacation has started so Alice and Bob want to play and joy, but... Their mom doesn't think so. She says that they have to read some amount of books before all entertainments. Alice and Bob will read each book together to end this exercise faster.

There are n books in the family library. The i-th book is described by three integers: ti — the amount of time Alice and Bob need to spend to read it, ai (equals 1 if Alice likes the i-th book and 0 if not), and bi (equals 1 if Bob likes the i-th book and 0 if not).

So they need to choose some books from the given n books in such a way that:

Alice likes at least k books from the chosen set and Bob likes at least k books from the chosen set;
the total reading time of these books is minimized (they are children and want to play and joy as soon a possible).
The set they choose is the same for both Alice an Bob (it's shared between them) and they read all books together, so the total reading time is the sum of ti over all books that are in the chosen set.

Your task is to help them and find any suitable set of books or determine that it is impossible to find such a set.

Input
The first line of the input contains two integers n and k (1≤k≤n≤2⋅105).

The next n lines contain descriptions of books, one description per line: the i-th line contains three integers ti, ai and bi (1≤ti≤104, 0≤ai,bi≤1), where:

ti — the amount of time required for reading the i-th book;
ai equals 1 if Alice likes the i-th book and 0 otherwise;
bi equals 1 if Bob likes the i-th book and 0 otherwise.
Output
If there is no solution, print only one integer -1. Otherwise print one integer T — the minimum total reading time of the suitable set of books.

Examples
inputCopy
8 4
7 1 1
2 1 1
4 0 1
8 1 1
1 0 1
1 1 1
1 0 1
3 0 0
outputCopy
18
inputCopy
5 2
6 0 0
9 0 0
1 0 1
2 1 1
5 1 0
outputCopy
8
inputCopy
5 3
3 0 0
2 1 0
3 1 0
5 0 1
3 0 1
outputCopy
-1
n,k = map(int, input().split())
alice = []
bob = []
common = []
for i in range(n):
	t, a, b = map(int, input().split())
	if a and b:
		common.append(t)
	elif a:
		alice.append(t)
	elif b:
		bob.append(t)
alice.sort()
bob.sort()
for i in range(min(len(alice), len(bob))):
	common.append(alice[i]+bob[i])
if len(common)<k:
	print(-1)
else:
	common.sort()
	print(sum(common[:k]))
