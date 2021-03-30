items=[2048,1024,512,256,128,64,32,16,8,4,2,1]
for _ in range (int(input())):
    amt=int(input())
    c=i=0
    while i<12:
        if items[i]<=amt:
            c+=1
            amt-=items[i]
            
        else:
            i+=1
    print(c)
