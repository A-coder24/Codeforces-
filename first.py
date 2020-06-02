tests=int(input())
for _ in range(tests):
    n=input()
    i=0
    d=[]
    while(i<len(n)):
        t=0
        
        while(n[i]=="0"):
            t+=1
            i+=1
            if i==len(n):
                break
        if t!=0:
            d.append(t)
        if i==len(n):
            break
        t=0
        while(n[i]=="1"):
            t+=1
            i+=1
            if i==len(n):
                break
        if t!=0:
            d.append(t)
    ans=0
    print(d)
    if len(d)<=2:
        print("0")
    else:
        i=0
        x=min(d[0],d[-1])
        if x==d[-1]:
            d.pop(0)
        else:
            d.pop()
        ans=0
        ans1=0
        for i in range(len(d)):
            if i%2==0:
                ans+=d[i]
            else:
                ans1+=d[i]
        print(min(ans1,ans))
        




 