for _ in range(int(input())):
    ans=0
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    for i in a:
        if (i+k)%7==0: ans=ans+1
    print(ans)
