from typing import List

def digitos(x: int) -> List[int]:
    digits = []
    while x > 0:
        digit = x % 10
        digits.append(digit)
        x = x // 10
    return digits[::-1]


def codifica(num,secr):
    lst=digitos(num)
    str=[]
    for i in lst:
        for j in range(len(secr)):
            if i==j:
                str.append(secr[j])
    x="".join(str)
    return x
print(codifica(2020739,"FRAGMENTOU"))
