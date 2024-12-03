'''
16.	Exercício: Reescreva o seguinte código para torná-lo mais legível usando boas práticas de código limpo:
a=5
b=10
c=a*b
if c>50:
 print("Grande")
else:print("Pequeno")

'''
num1 = 5
num2 = 10

multiplicacao = num1 * num2

if multiplicacao > 50:
    print(f"O resultado da multiplicação {multiplicacao} é grande!")
else:
    print(f"O resultado da multiplicação {multiplicacao} é pequeno!")