for _ in range(int(input())):
    d = 0
    N,K = map(int,input().split())
    for j in range(1,K+1):
        if(d<(N%j)): d=N%j
    print(d)
