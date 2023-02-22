line=input()
count=0
for i in range(len(line)):
    if line[i]=='p' or line[i]=='P':
        count+=1
print(count)