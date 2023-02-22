lst=[]
local=int(input())
while local != 0:
    lst.append(local)
    local=int(input())
i=0
j=i
flag=0
while i <= len(lst)-1:
    while j <= len(lst)-1:
        if lst[i]==lst[j] and i!=j:
            for k in range(j-1,i-1,-1):
                lst.remove(lst[k])
                flag=1
        if flag==0:
            j+=1
        else:
            j=i
            flag=0
    if flag==0:
        i+=1
        j=i
    else:
        i=0
        flag=0
    
            
for m in range(0,len(lst),1):
    print(lst[m])