N = int(input())
soma=0
lst=[]
for i in range (0,N,1):
    lst.append(int(input()))
for i in range (1,N-1,1):
    if lst[i]>2*lst[i-1] and lst[i]>2*lst[i+1]:
        soma+=1
print(soma)    
