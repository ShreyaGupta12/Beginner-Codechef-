for _ in range(int(input())):
    q,p=map(int,input().split())
    s=float(q*p)
    print((s-(0.1*s)) if q>=1000 else s)
