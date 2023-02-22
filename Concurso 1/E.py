T,per=map(int,input().split())
diasconsec=0
maxdiasconsec=0
for i in range (0,per,1):
    temperatura = int(input())
    if (temperatura<=T+2 and temperatura>=T-2):
        diasconsec+=1
        if diasconsec>maxdiasconsec:
            maxdiasconsec=diasconsec
    else:
        diasconsec=0
if maxdiasconsec==0:
    print("Sem registo de temperaturas moderadas")
elif maxdiasconsec==1:
    print("Temperaturas moderadas apenas em dias isolados")
else:
    print("Durante %d dias consecutivos, temperaturas moderadas" %maxdiasconsec)

