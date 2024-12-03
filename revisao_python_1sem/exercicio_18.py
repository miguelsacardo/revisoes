'''
18.	Exercício: Escreva um programa que leia três números e exiba "verdadeiro" se a soma dos dois menores for maior que o maior número.
'''

lista_numeros = []
maiorNumero = 0
contador = 0

while contador < 3:
    numero = float(input("Informe um número: "))
    lista_numeros.append(numero)
    contador += 1

for numero in lista_numeros:
    if numero > maiorNumero:
        maiorNumero = numero

lista_numeros.remove(maiorNumero)
somaMenores = "Verdadeiro" if sum(lista_numeros) > maiorNumero else ""

print(somaMenores)


