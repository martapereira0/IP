def primo(x):
    if x==1:
        return False
    if x==2:
        return True
    if x%2==0:
        return False #par e maior do que 2
    d=3
    while d*d <= x:
        if x%d==0:
            return False
        d+=2
    return True

N=int(input())
for j in range (0,N):
    n=int(input())
    number = n
    fact=1
    lst=[]
    i=0
    while i < number+1:
        if primo(i):
            while n%i==0:
                fact*=i
                lst.append(i)
                n=n/i
        i+=1
    print("%d = " %number,end='')
    for m in range (0,len(lst)):
        if m==0 and len(lst)>1:
            print("%d*" %lst[m],end='')
        elif m==0 and len(lst)==1:
            print("%d" %lst[m],end='')
        elif m==len(lst)-1:
            print("%d"%lst[m],end='')
        else:
            print("%d*" %lst[m],end='')
    print()
