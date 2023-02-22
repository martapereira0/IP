frase1=str(input())
frase2=str(input())


str1=""
str2=""
count=0
for i in range(len(frase1)):
    if frase1[i]!=" " and frase1[i].isalpha():
        str1 += frase1[i]

for i in range(len(frase2)):
    if frase2[i]!=" " and frase2[i].isalpha():
        str2 += frase2[i]

string1=str1.lower()
string2=str2.lower()

line1=sorted(string1)
line2=sorted(string2)
if len(line1) !=  len(line2):
    print("no")
else:
    for i in range(len(line1)):
        if line1[i]!=line2[i]:
            count=0
        else:
            count+=1
    if count==len(line1):
        print("yes")
    else:
        print("no")
