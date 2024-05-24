import os
os.system("clear")

def cabecalho():
    os.system("clear")
    print("---------------------")
    print(" === SENAI | FIEB ===")
    print("---------------------")

def somar (n1,n2):
    resultado = n1 + n2
    return resultado

cabecalho()
primeiroNmr = int(input("Digite o 1° número: "))
segundoNmr = int(input("Digite o 2º número: "))

soma = somar(primeiroNmr, segundoNmr)

cabecalho()
print(f"soma: {soma}")