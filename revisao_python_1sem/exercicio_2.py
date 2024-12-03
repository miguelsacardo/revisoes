tamanhoLista = int(input("Digite a quantidade de números que você quer informar: "))
contadorNumeros = 0
lista_numeros = []
maiorNumero = 0

while contadorNumeros < tamanhoLista:
	inputNumeros = float(input("Escreva um número: "))
	lista_numeros.append(inputNumeros)
	contadorNumeros += 1

for i in lista_numeros:

	if i > maiorNumero:
		maiorNumero = i
		if maiorNumero < 100:
		    mostrar = maiorNumero
			
print(f"O maior número menor que 100 da sua lista é {mostrar}")
        
