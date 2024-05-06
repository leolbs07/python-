import os
os.system("clear")
nome = (input("Informe o seu nome: "))
idade = int(input("Informe a sua idade: "))
noA = float(input("Primeira nota: "))
noB = float(input("Segunda nota: "))
noC = float(input("Terceira nota: "))

media = (noA + noB + noC) / 3
if media >= 7:
    print("Aprovado!")
else:
    print("Reprovado!")
