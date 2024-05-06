import os 
os.system("clear")
nmrA = int(input("Informe o valor do primeiro número: ")) 
nmrB = int(input("Informe o valor do segundo número: ")) 

# Resolvendo cálculos 
soma = nmrA + nmrB

media = soma / 2

produto = nmrA * nmrB

maior = max(nmrA, nmrB)

menor = min(nmrA, nmrB)
'''
if nmrA < nmrB:
    maior = nmrA
else:
    maior = nmrB

if nmrA > nmrB
    menor = nmrA

else:
    menor = nmrB
'''
print("Resultados a seguir:\n")
print(f"Primeiro número: {nmrA}")
print(f"segundo número: {nmrB}")
print(f"\nsoma: {soma}")
print(f"Produto: {produto}")
print(f"Média: {media}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
