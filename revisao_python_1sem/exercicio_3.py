contadorNumeros = 0
maiorNumero = 0

while contadorNumeros < 3:
	inputNumeros = float(input("Informe um número: "))
	if inputNumeros > maiorNumero:
		maiorNumero = inputNumeros
	contadorNumeros += 1
print(f"O maior número dos três fornecidos é {maiorNumero}")
