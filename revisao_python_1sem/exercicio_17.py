'''
17.	Exercício: Crie um programa que leia uma senha de 4 dígitos do usuário e permita até 3 tentativas para acertar.
'''

tentativas = 0
while tentativas < 3: 
    senhaUsuario = int(input("Digite sua senha de 4 dígitos: "))

    if senhaUsuario == 1234:
        print("Senha correta!")
        break
    else:
        if tentativas == 2:
            print("Você excedeu seu número de tentativas.")
            break
        else:
            print("Sua senha está incorreta! Tente de novo.")
            tentativas += 1
       