import os
os.system("clear")

nome =  (input("Infome o seu nome: "))
idade = int (input("Informe sua idade: "))
notaA = float (input("Informe a primeira nota: "))
notaB = float (input("Informe o valor da segunda nota: "))

media = (notaA + notaB) / 2

print("\nExibir resultados.")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Primeira nota: {notaA}")
print(f"Segunda nota: {notaB}")
print(f"Média: {media}")