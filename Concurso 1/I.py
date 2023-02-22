N = int(input())
tam = N
calex=0
cbela=0
lst=list(map(int,input().split()))
index=0 #posicoes da lista
njogadas=0 #numero de jogadas 
iter=0 #identificar quando é que a bela escolhe o maior ou o menor
fim=0 # o monte foi retirado do fim
inicio=0 # o monte foi retirado do início
while tam>0:
    if lst[index] >= lst[N-1-fim] and njogadas%2==0 :
        calex += lst[index]
        inicio+=1
        index+=1
    elif lst[index] <= lst[N-1-fim] and njogadas%2==0 :
        calex += lst[N-1-fim]
        fim+=1
    elif njogadas%2!=0:
        if (lst[index] >= lst[N-1-fim] and iter%2==0) or (lst[index] <= lst[N-1-fim] and iter%2!=0): 
            cbela += lst[N-1-fim]
            iter+=1
            fim+=1
        elif (lst[index] <= lst[N-1-fim] and iter%2==0) or (lst[index] >= lst[N-1-fim] and iter%2!=0):
            cbela += lst[index]
            iter+=1
            inicio+=1
            index+=1
    njogadas+=1
    tam-=1
    
if calex > cbela:
    print("Alex ganha com %d contra %d" %(calex,cbela))
elif calex < cbela:
    print("Bela ganha com %d contra %d" %(cbela,calex))
else:
    print("Alex e Bela empatam a %d" %calex)