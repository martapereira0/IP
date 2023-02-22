C,N=map(int,input().split())
produtos=[]
total=0 #valor total a pagar
for i in range(N):
    preco=int(input())
    desc=input()
    if preco <= C:
        C=C-preco
        produtos.append(desc)
        total+=preco
for i in range(len(produtos)):
    print(produtos[i])
print("%d %d" %(total,C))