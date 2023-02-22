def maxdescidas():
    ant=int(input())
    c=0
    cmax=0
    x=int(input())
    while x!=-1: 
        if ant>x:
            c+=1
        else:
            if c>cmax:
                cmax=c
            c=0
        ant=x
        x=int(input())
    if c>cmax:
        return c
    return cmax

print(maxdescidas())
