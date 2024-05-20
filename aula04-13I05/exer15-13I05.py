import os

os.system("clear")

nota : float = -1
soma : float = 0

for i in range(3):
    while True :
        nota = float(input("Digite uma nota: "))
        if nota < 0 or nota > 10:
            print("Nota inválida ... \n")
        else:

            soma += nota
            break

media = soma / 3


print(f"Média: {media}")
if media >= 7:
    print("Aprovado!")
elif media < 5:
    print("Reprovado!")
elif media < 7 & media > 5:
    print("Recuperação!")