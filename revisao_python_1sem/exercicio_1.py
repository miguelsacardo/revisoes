lista_numeros = [] 
contadorPar = 0
contadorNumeros = 0
while contadorNumeros < 10:
		numero = float(input("Escreva um número: "))
		lista_numeros.append(numero)
		contadorNumeros += 1
	
for i in lista_numeros:
	if i%2 == 0:
		contadorPar += 1
print(f"Há {contadorPar} número(s) par(es) na lista de números fornecida") 	
