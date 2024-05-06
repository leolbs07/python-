import os
os.system("clear")

numberA = int(input("Digite o valor do primeiro número: "))
numberB = int(input("Digite o valor do segundo número: "))

soma = numberA + numberB
media = soma / 2
produto = numberA * numberB

if numberA > numberB:
    maior = numberA
    menor = numberB
elif numberA < numberB:
    menor = numberA
    maior = numberB

print("Resultados a seguir:\n")
print(f"Primeiro número: {numberA}")
print(f"segundo número: {numberB}")
print(f"\nsoma: {soma}")
print(f"Produto: {produto}")
print(f"Média: {media}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")