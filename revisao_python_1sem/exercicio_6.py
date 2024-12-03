tamanhoLista = int(input("Quantos números você deseja informar? "))
lista_numeros = []
contadorlista = 0

while contadorlista < tamanhoLista:
    inputNumeros = float(input("Digite um número: "))
    lista_numeros.append(inputNumeros)

    contadorlista += 1

for i in lista_numeros:
    print(f"O número {i} elevado ao quadrado é {i**2}")