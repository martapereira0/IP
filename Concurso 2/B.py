lst=list(map(int,input().split()))
N = int(input())
for i in range(0,N,1):
    cdivisores=0
    divisoresneg=0
    n = int(input())
    for j in range (0,len(lst)-1,1):
        if n % lst[j]==0:
            cdivisores+=1
            if lst[j] < 0:
                divisoresneg+=1
    print("Resp: Numero de divisores de %d na sequencia = %d" %(n,cdivisores))
    print("      Numero dos negativos = %d" %divisoresneg)
