import os
os.system("clear")

lst = []

qntdNeg = 0
smPos = 0

for i in range(5):
    nmr = float(input(f"Digite o {i+1}º número: "))
    lst.append(nmr)


for i in lst:
    if i < 0:
        qntdNeg += 1
    elif i > 0:
        smPos += i

print(f"Quantidade de números negativos: {qntdNeg}")
print(f"soma dos números positivos: {smPos:.2f}")