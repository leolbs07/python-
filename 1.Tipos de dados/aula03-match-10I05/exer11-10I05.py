import os
os.system("clear")

par = 0
impar = 0
for i in range(5):
    numero = int(input(f"Digite o valor do {i+1}º número: "))

    if numero % 2 == 0:
        par += 1
    else:
        impar += 1 

    print("Quantidade de pares:", par)
    print("Quantidade de ímpares:", impar)
    

