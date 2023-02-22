compmax,nlajes=map(int,input().split())
lst=[]
newlst=[] #sub-array
cpedir=0
cpeesq=0
pedir=0
peesq=0
flag=0 #0 para o pe direito 1 para esquerdo
i=0 # marcar a posicao que o rui se encontra
posi=0
for k in range(0,nlajes,1):
    lst.append(int(input()))
while i<nlajes-1:
    for j in range (0,compmax,1):
        if flag==0: #o Rui opta pela laje de maior valor, ou seja, o salto acaba com o pe direito
            if i<nlajes-1-compmax: # quando o rui nao se encontra nas ultimas compmax lajes o rui só salta para a meta quando já não há lajes
                if i!=j and lst[i]>lst[i+j] and lst[i]>pedir:
                        pedir=lst[i]
                        posi=i
                        
                else:
                    if lst[i+j] > pedir:
                        pedir=lst[i+j]
                        posi=i+j       
            else:
                if i==nlajes-2: #o rui so pode ir para a meta quando não houver mais lajes
                    pedir=lst[i+1]
                    posi=i+1
                elif i<nlajes-2:
                    if lst[i]>lst[i+j] and lst[i]>pedir and i+j<nlajes-2:
                        pedir=lst[i]
                        posi=i
                    else:
                        if lst[i+j] > pedir and i+j<nlajes-2:
                            pedir=lst[i+j]
                            posi=i+j
                        elif i+j==nlajes-2:
                            pedir=lst[i+1]
                            posi=i+1
                            
        else:
            if i<=nlajes-1-compmax: # quando o rui nao se encontra nas ultimas compmax lajes o rui só salta para a meta quando já não há lajes
                newlst.append(lst[i+j+1])
                if j == compmax-1:
                    peesq=min(newlst) 
                    for p in range (0,compmax,1):
                        if newlst[p]==peesq:
                            posi= i + p +1                
            else: #quando o rui se encontra nas nlajes-1-compmax, ele pode ir diretamente para a meta
                posi=nlajes-1 #chegamos à meta
    if flag == 0:         
        flag=1 #vai saltar com o pe esquerdo
        cpedir+=pedir
    elif flag == 1:
        flag=0 #vai saltar com o pe direito
        cpeesq+=peesq
    i+=posi
    
pontuacao=cpedir-cpeesq
print(pontuacao)