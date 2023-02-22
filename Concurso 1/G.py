N=int(input())
a=int(input())
b=int(input())
soma=0
count=0
for i in range (0,N-2,1):
    c=int(input())
    if c!=a and c!=b and (c%b==0 or c>a):
        soma+=c
        count+=1
if count==0:
    print("Resposta G - nenhum valor satisfaz")
else:
    print("Resposta G - soma: %d" %soma)
