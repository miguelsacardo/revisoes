'''
12.	Exercício: Escreva um programa que leia um arquivo texto e conte quantas palavras têm mais de 5 caracteres.
'''
count = 0
caracteresCount = 0
with open("exercicio12.txt", "r") as arquivo:
    
    linhas = [linha.rstrip() for linha in arquivo]
    resultado = " ".join(linhas)
    separador = resultado.split()

    for i in separador:
        print(i,":",len(i))
        if len(i) > 5:
            caracteresCount += 1  
print(f"No arquivo .txt, há {caracteresCount} palavra(s) com mais de 5 caracteres.")

