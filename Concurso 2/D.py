N,M=map(int,input().split())
players=[0]*N
indexs=[] # numeros indentificadores dos jogadores vencedores
for i in range (0,M,1):
    plays=list(map(int,input().split()))
    S=sum(plays) #somar as jogadas
    R=S%N
    players[R]+=1
max_number=max(players) #saber qual é a pontuação mais alta
nplayersmax=players.count(max_number) #contar quantas vezes ocorre a pontuação mais alta
for m in range (0,N,1):
    if players[m]==max_number:
        indexs.append(m)
for k in range(0,N,1):
    print(players[k])
print()
for w in range(0,nplayersmax,1):
    print(indexs[w])
    