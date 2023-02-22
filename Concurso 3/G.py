rows,cols=map(int,input().split())
lst=[]
k=0
for i in range (rows):
    lst.append(input())
        
gambozinos=0
print()



for i in range(2,rows-2): #i linhas
    for j in range(4,len(lst[i])-4,2): #j colunas
        if lst[i][j]=='1':
            if lst[i][j+1]=='1' and lst[i-1][j]=='1' and lst[i+1][j]=='1' and lst[i+1][j-1]=='1':
                if lst[i-1][j+1]=='0' and lst[i-2][j]=='0' and lst[i-1][j-1]=='0' and lst[i][j-1]=='0' and lst[i+1][j-2]=='0' and lst[i+2][j-1]=='0' and lst[i+2][j]=='0' and lst[i+1][j+1]=='0' and lst[i][j+2]=='0':
                    gambozinos+=1
            elif lst[i][j-1]=='1' and lst[i-1][j]=='1' and lst[i+1][j]=='1' and lst[i+1][j+1]=='1':
                if lst[i][j+1]=='0' and lst[i-1][j+1]=='0' and lst[i-2][j]=='0' and lst[i-1][j-1]=='0' and lst[i][j-2]=='0' and lst[i+1][j-1]=='0' and lst[i+2][j]=='0' and lst[i+2][j+1]=='0' and lst[i+1][j+2]=='0':
                    gambozinos+=1
            elif lst[i][j+1]=='1' and lst[i-1][j]=='1' and lst[i+1][j]=='1' and lst[i-1][j-1]=='1':
                if lst[i][j+2]=='0' and lst[i-1][j+1]=='0' and lst[i-2][j]=='0' and lst[i-2][j-1]=='0' and lst[i-1][j-2]=='0' and lst[i][j-1]=='0' and lst[i+1][j-1]=='0' and lst[i+2][j]=='0' and lst[i+1][j+1]=='0': 
                    gambozinos+=1
            elif lst[i][j-1]=='1' and lst[i][j+1]=='1' and lst[i-1][j+1]=='1' and lst[i+1][j]=='1':
                if lst[i][j+2]=='0' and lst[i-1][j+2]=='0' and lst[i-2][j+1]=='0' and lst[i-1][j]=='0' and lst[i-1][j-1]=='0' and lst[i][j-2]=='0' and lst[i+1][j-1]=='0' and lst[i+2][j]=='0' and lst[i+1][j+1]=='0':
                    gambozinos+=1
            elif lst[i-1][j]=='1' and lst[i][j+1]=='1' and lst[i][j-1]=='1' and lst[i+1][j-1]=='1':
                if lst[i][j+2]=='0' and lst[i-1][j+1]=='0' and lst[i-2][j]=='0' and lst[i-1][j-1]=='0' and lst[i][j-2]=='0' and lst[i+1][j-2]=='0' and lst[i+2][j-1]=='0' and lst[i+1][j]=='0' and lst[i+1][j+1]=='0':
                    gambozinos+=1      
print(gambozinos)