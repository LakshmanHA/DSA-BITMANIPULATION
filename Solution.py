for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort(reverse=True)
    res=999999
    for i in range(n):
        if i!=n-1:
            k=l[i]^l[i+1]
            res=min(res,k)
    print(res)
