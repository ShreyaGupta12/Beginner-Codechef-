import math
for i in range(int(input())):
    r=int(input())
    x1,y1=map(int,input().split())
    x2,y2=map(int,input().split())
    x3,y3=map(int,input().split())
    a=math.sqrt((x1-x2)**2+(y1-y2)**2)
    b=math.sqrt((x2-x3)**2+(y2-y3)**2)
    c=math.sqrt((x1-x3)**2+(y1-y3)**2)
    if (a<=r and b<=r) or (b<=r and c<=r) or (a<=r and c<=r): print('yes')
    else: print('no')
