'''def procurar_letra(m,words):
    for p in range(len(words)): #0<=p<1
        flag=0
        for index in range(len(words[p])): # 0<=index<2
            if flag==1:
                break
            for i in range(rows): #0<=rows<6
                if flag==1:
                    break
                for j in range(cols): #0<=cols<6
                    if m[i][j]==words[p][index]:
                        if procurar_palavrah(m,i,j,words,p,index,rows,cols) == 1:
                            flag=1
                            break
                        if procurar_palavrav(m,i,j,words,p,index,rows,cols) == 1:
                            flag=1
                            break
                        if procurar_palavrad(m,i,j,words,p,index,rows,cols) == 1:
                            flag=1
                            break
    return 0

def procurar_palavrah(m,line,column,words,p,index,rows,cols):
    #horizontalmente da esq p/ a dir
    indice=index
    count=1
    for j in range(column+1,column+len(words[p]),1):
        index+=1
        if words[p][index]==m[line][j] and j<cols:
            count+=1
            cf=j #coluna final
        else:
            break
    if count==len(words[p]):
        print("%d %d %d %d" %(line+1,column+1,line+1,cf+1))
        return 1
    #horizontalmente da dir p/ esq
    index=indice
    count=1
    for j in range(column-1,column-len(words[p]),-1):
        index+=1
        if words[p][index]==m[line][j] and j>=0:
            count+=1
            cf=j #coluna final
        else:
            break
    if count==len(words[p]):
        print("%d %d %d %d" %(line+1,column+1,line+1,cf+1))
        return 1
    return 0

def procurar_palavrav(m,line,column,words,p,index,rows,cols):
    #verticalmente de cima p/ baixo
    indice=index
    count=1
    for i in range (line+1,line+len(words[p]),1):
        index+=1
        if m[i][column]==words[p][index] and i<rows:
            count+=1
            lf=i #linha final
        else:
            break
    if count==len(words[p]):
        print("%d %d %d %d" %(line+1,column+1,lf+1,column+1))
        return 1
    index=indice
    count=1
    for i in range (line-1,line-len(words[p]),-1):
        index+=1
        if m[i][column]==words[p][index] and i>=0:
            count+=1
            lf=i #linha final
        else:
            break
    if count==len(words[p]):
        print("%d %d %d %d" %(line+1,column+1,lf+1,column+1))
        return 1
    return 0

def procurar_palavrad(m,line,column,words,p,index,rows,cols):
    #diagonal principal
    indice=index
    count=1
    flag=3
    for i in range (line+1,line+len(words[p]),1):
        if flag==4:
            column-=1
        else:
            break
        for j in range(column-1,column-len(words[p]),-1):
            index+=1
            if m[i][j]==words[p][index] and i<rows and j>=0:
                count+=1
                lf=i
                cf=j
                flag=4
                break
            else:
                flag=3
                break
            
    if count==len(words[p]):
        print("%d %d %d %d" %(line+1,column+1,lf+1,cf+1))
        return 1

    for i in range (line-1,line-len(words[p]),-1): 
        if flag==4:
            column-=1
        else:
            break
        for j in range(column+1,column+len(words[p]),1):
            index+=1
            if m[i][j]==words[p][index] and i>=0 and j<cols:
                count+=1
                lf=i
                cf=j
                flag=4
                break
            else:
                flag=3
                break
    if count==len(words[p]):
        print("%d %d %d %d" %(line+1,column+1,lf+1,cf+1))
        return 1
    
    for i in range (line+1,line+len(words[p]),1):   
        for j in range(column+1,column+len(words[p]),1):
            index+=1
            if m[i][j]==words[p][index] and i<rows and j<cols:
                count+=1
                lf=i
                cf=j
            else:
                break
    if count==len(words[p]):
        print("%d %d %d %d" %(line+1,column+1,lf+1,cf+1))
        return 1
    index=indice
    count=1
    for i in range (line+1,line-len(words[p]),-1):   
        for j in range(column+1,column-len(words[p]),-1):
            index+=1
            if m[i][j]==words[p][index] and i>=0 and j>=0:
                count+=1
                lf=i
                cf=j
            else:
                break
    if count==len(words[p]):
        print("%d %d %d %d" %(line+1,column+1,lf+1,cf+1))
        return 1
    return 0


rows,cols=map(int,input().split())
m=[] #matriz
words=[]
for i in range(rows):
    m.append(input())
k=int(input())
for j in range(k):
    words.append(input())
procurar_letra(m,words)'''


def lersopa(m):
    L=[]
    for i in range(m):
        L.append(input())
        return L
def pesquisa(palavra,sopa,m,n):
    dirs=[[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]]
    for i in range(m):
        for j in range(n):
            for k in range(8): #percorrer as direcoes possiveis
                if encaixa([i,j],sopa,m,n,dirs[k],palavra):
                    fimi = i+(len(palavra)-1) * dirs[k][0]
                    fimj = j+(len(palavra)-1) * dirs[k][1]
                    print(i+1,j+1,fimi+1,fimj+1)
                    return 

def encaixa(inicio,sopa,m,n,direcao,p):
    i=inicio[0]
    j=inicio[1]
    k=0
    while i<m and i<=0 and j<n and j>=0 and k<len(p) and sopa[i][j]==p[k]:
        k+=1
        i+=direcao[0]
        j+=direcao[1]
    if k==len(p):
        return True
    return False


def sopaletras():
    m,n=map(int,input().split()) #dimensão da matriz
    sopa=lersopa(m)
    k=int(input()) #quantidade de palavras a ler
    for i in range(k):
        palavra=input()
        pesquisa(palavra,sopa,m,n)

sopaletras()


