"""A. Ice Skating
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
Bajtek is learning to skate on ice. He's a beginner, so his only mode of transportation is pushing off from a snow drift to the north, east, south or west and sliding until he lands in another snow drift. He has noticed that in this way it's impossible to get from some snow drifts to some other by any sequence of moves. He now wants to heap up some additional snow drifts, so that he can get from any snow drift to any other one. He asked you to find the minimal number of snow drifts that need to be created.

We assume that Bajtek can only heap up snow drifts at integer coordinates.

Input
The first line of input contains a single integer n (1 ≤ n ≤ 100) — the number of snow drifts. Each of the following n lines contains two integers xi and yi (1 ≤ xi, yi ≤ 1000) — the coordinates of the i-th snow drift.

Note that the north direction coinсides with the direction of Oy axis, so the east direction coinсides with the direction of the Ox axis. All snow drift's locations are distinct.

Output
Output the minimal number of snow drifts that need to be created in order for Bajtek to be able to reach any snow drift from any other one.

Examples
inputCopy
2
2 1
1 2
outputCopy
1
inputCopy
2
2 1
4 1
outputCopy
0
"""


n = int(input())

p = []
for i in range(n):
    x, y = map(int, input().split())
    p.append((x, y))

visit = [False] * 101
def dfs(no):
    if visit[no]: return
    visit[no] = True
    for i in range(n):
        if p[no][0] == p[i][0] or p[no][1] == p[i][1]:
            dfs(i)

answer = 0
for no in range(n):
    if visit[no] == False:
        answer += 1
        dfs(no)

print(answer - 1)
