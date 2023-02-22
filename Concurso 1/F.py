a,b=map(int,input().split())
abertura=0
maxabertura=0
while a!=-1 and b!=-1:
    if a==1 and b==1:
        abertura+=1
        if abertura>maxabertura:
            maxabertura=abertura
    elif a==1 and b==0:
        abertura=0
        c=int(input())
        while c!=1 and c!=2:
            c=int(input())
    a,b=map(int,input().split())
print(maxabertura)