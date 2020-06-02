def explore(adj,m):
    d=len(adj[m-1])
    print(adj[m-1])
    if d==0:
        return "Ayush"
    if d==1:
        return "Ayush"
    if d%2==0:
        return "Ashish"
    else:
        return "Ayush"


import sys
tests=int(input())


for _ in range(tests):
    n,m= map(int,input().split())
    edges=[]
    for _ in range(n-1):
        edges.append(list(map(int, input().split())))

    


    adj = [[] for _ in range(n)]
    for [a, b] in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(adj)
    for i in range(n):
        for [a, b] in edges:
            if a-1 in adj[m-1] :
                adj[m-1]+=adj[a-1]
            if b-1 in adj[m-1]:
                adj[m-1]+=adj[b-1]          
    adj[m-1]=set(adj[m-1])            
            
    
    
    print(explore(adj,m))
    
    