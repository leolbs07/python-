import os
os.system("clear")

nome =  (input("Infome o seu nome: "))
idade = int (input("Informe sua idade: "))
soma = 0 
notas = []
for i in range(3):
    nota = int (input(f"Infome sua {i+1}ª nota: "))
    notas.append(nota)
    soma += nota

media = soma / (i+1)
    
os.system("clear")

print(f"Nome: {nome}")
print(f"Idade: {idade}")

for i in range(3):
    print(f"Nota {i+1}: {notas[i]}")

print(f"Média: {round(media,1)}\n\n")