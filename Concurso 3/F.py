rows,cols=map(int,input().split())
res=''
lst=[]
for i in range(rows):
    lst.append(input())
    
for i in range(0,cols,1):
    uns=0
    zeros=0
    for j in range(0,rows,1):
        if lst[j][i]=='0':
            zeros+=1
        else:
            uns+=1

    if zeros>uns or uns==zeros:
        res = res + '0'
    else:
        res = res + '1'
print(res)
