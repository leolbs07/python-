import os
os.system("clear")
TAM = 3  # Constante para o número de notas

def calcular_media(notas):
    """Calcula a média das notas."""
    return sum(notas) / len(notas)

def verificar_situacao(media):
    """Verifica se o aluno está aprovado ou reprovado."""
    resultado = "Aprovado!" if media >= 7 else "Reprovado!"
    return resultado

def mostrar_resultado(notas):
    """Exibe a média e a situação do aluno."""
    media = calcular_media(notas)
    print(f"\nMédia: {media:.1f}")
    situacao = verificar_situacao(media)
    print(f"Resultado: {situacao}")

def main():
    """Função principal."""
    notas = []
    for i in range(1, TAM + 1):
        nota = float(input(f"Digite a {i}ª nota: "))
        notas.append(nota)

    mostrar_resultado(notas)

main()
