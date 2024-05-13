import os 
os.system("clear")

soma = 0

for i in range(4):
    nota = float(input(f"Digite a {i+1}º nota: "))
    soma+= nota

media = soma / 4
print(f"A média das notas é: {media}")