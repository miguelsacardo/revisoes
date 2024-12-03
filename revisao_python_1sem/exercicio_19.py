'''
19.	Exercício: Crie um programa que leia o nome e a nota de 5 alunos e armazene os dados em um dicionário. Depois, exiba o nome do aluno com a maior nota.

'''

lista_alunos = []
alunos = {}
contador = 0
maiorNota = 0

while contador < 5:
    alunos['Nome'] = str(input("Escreva o nome do aluno: "))
    alunos['Nota'] = float(input("Escreva a nota do aluno: "))

    lista_alunos.append(alunos.copy())

    contador += 1

for al in lista_alunos:
    if al['Nota'] > maiorNota:
        maiorNota = al['Nota']
        print(al['Nome'])


    



