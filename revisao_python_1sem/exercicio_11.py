'''
11.	Exercício: Configure um projeto em uma IDE para executar um programa que leia uma lista de números de um arquivo .txt e calcule sua média.
'''

lista_numeros = []
with open('exercicio11.txt', "r") as arquivo:
    for linhas in arquivo:
        lista_numeros.append(int(linhas))   

    media = sum(lista_numeros)/len(lista_numeros)

print(f"A média dos números do arquivo .txt é {media}")

