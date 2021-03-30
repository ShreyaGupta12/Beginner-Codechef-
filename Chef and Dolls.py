for _ in range(int(input())):
    n=int(input())
    l=[]
    res=0
    for i in range(n):
      l.append(int(input()))
      res^=l[i]
    print(res)
