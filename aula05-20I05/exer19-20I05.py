import os
os.system("clear")

def cabecalho():
    os.system("clear")
    print("---------------------")
    print(" === SENAI | FIEB ===")
    print("---------------------")

QNTD_NMRS = 5
nmrs = []

for i in range(QNTD_NMRS):
    cabecalho()
    numero = int(input(f"Digite o {i+1}° número: "))
    if numero < 0:
        numero = 0
    nmrs.append(numero)

for i, numero in enumerate(nmrs):
    print(f"{i+1}° múmero: {numero}")