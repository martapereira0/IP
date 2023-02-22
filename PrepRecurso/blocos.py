def blocos():
    n,k,p=map(int,input().split())
    c=0 #contador intermediário
    cf=0 #contador final
    while n>0:
        x=int(input())
        if x==p:
            c+=1
        elif x!=p:
            if c>=k:
                cf+=1
            c=0
        n-=1
    if c>=k:
        cf+=1
    return cf

print(blocos())