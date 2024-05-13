import os 
os.system("clear")
notas = 0
for i in range(3):
    nota = float(input(f"Digite a {i+1}ª nota: "))


media = notas / 3

if media <= 7:
    print("Aprovado")
elif media > 4:
    print("Reprovado")
else: 
    print("Recuperação")

