for _ in range(int(input())):
    m,x,y=map(int,input().split())
    l=sorted(list(map(int,input().split())))
    s=0
    if l[0]-1>x*y: s+=l[0]-1-x*y
    if 100-l[m-1]>x*y: s+=100-l[m-1]-x*y 
    for i in range(0,m-1):
        if l[i+1]-l[i]>2*(x*y): s+=l[i+1]-l[i]-2*(x*y)-1 
    print(s)
