N = int(input())
totalacertos=0
pontuacao=0
lst1=list(map(int,input().split()))
lst2=list(map(int,input().split()))
for i in range(0,N,1):
    if i==0:
        if lst1[i]==lst2[i]:
            if lst1[i+1]==lst2[i+1]:
                totalacertos+=1
                pontuacao+=3
            else:
                totalacertos+=1
                pontuacao+=1
    elif i==N-1:
        if lst1[i]==lst2[i]:
            if lst1[i-1]==lst2[i-1]:
                totalacertos+=1
                pontuacao+=3
            else:
                totalacertos+=1
                pontuacao+=1
    else:    
        if lst1[i]==lst2[i]:
            if lst1[i+1]==lst2[i+1] or lst1[i-1]==lst2[i-1] :
                totalacertos+=1
                pontuacao+=3
            else:
                totalacertos+=1
                pontuacao+=1
print(totalacertos)
print(pontuacao)