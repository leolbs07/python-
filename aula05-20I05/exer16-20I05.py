import os
os.system("clear")

par = 0 
impar = 0 

for i in range(6):
    nmr = int(input(f"Digite o valor do {i+1}° número: "))

    if nmr % 2 == 0:
        par += 1
    else:
        impar += 1 

print("Quantidade de pares:", par)
print("Quantidade de ímpares:", impar)

