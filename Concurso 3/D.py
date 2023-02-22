# # está fechada o está aberta
ngavetas=int(input())
estados=[]
count=0
for i in range(ngavetas):
    estados.append(str(input()))
for i in range(ngavetas):
    if i==0 and estados[i]=="#":
        count+=1
    elif i!=0 and estados[i]=="#" and estados[i-1]=="#":
        count+=1
print(count)
