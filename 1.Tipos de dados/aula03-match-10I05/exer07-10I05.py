import os
os.system("clear")

resultado = 0
a = int(input("Informe o valor do 1º número: "))
opc = input("Qual operação deseja? (+-*/): ")
b = int(input("Informe o valor do 2º número: "))

match(opc): 
    case "+":
        resultado = a + b
    case "-": 
        resultado = a - b
    case "*": 
        resultado = a * b
    case "/":
        resultado = a / b
    case _:
        print("INVÁLIDO.")

print(f"Resultado: {resultado}.")

