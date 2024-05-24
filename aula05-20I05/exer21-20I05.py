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

def subt (n1,n2):
    resultado = n1 - n2
    return resultado

def mult (n1,n2):
    resultado = n1 * n2
    return resultado

def div (n1,n2):
    resultado = n1 / n2
    return resultado

cabecalho()
primeiroNmr = int(input("Digite o 1° número: "))
segundoNmr = int(input("Digite o 2º número: "))

soma = somar(primeiroNmr, segundoNmr)
subtrair = subt(primeiroNmr, segundoNmr)
multiplicação = mult(primeiroNmr, segundoNmr)
divisão = div(primeiroNmr, segundoNmr)

cabecalho()
print(f"soma: {soma}")
print(f"subtração: {subtrair}")
print(f"multiplicação: {multiplicação}")
print(f"divisão: {divisão}")