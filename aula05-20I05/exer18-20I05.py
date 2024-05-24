import os
os.system("clear")

def cabecalho():
    os.system("clear")
    print("---------------------")
    print(" === SENAI | FIEB ===")
    print("---------------------")

cabecalho()
nome = input("Digite seu nome: ")

cabecalho()
idade = int(input("Digite sua idade: "))
print("\n")
print(f"Nome informado: {nome}")
print(f"Idade informada: {idade}")