"""
FIAP
DEFESA CIBERNÉTICA
DEVELOPMENT E CODING FOR SECURITY
PROF. MS. FÁBIO H. CABRINI
Atividade: Check Point 1
ALUNOS
FILIPE GRAHL RM 86663
VICTOR DIAS GONÇALVEZ RM 88582
"""
print("Algoritmo que recebe uma entrada do usuario e fornece a sequencia de Fibonacci até aquele número:")

i = 0
simValido = ['s', 'sim', 'si', 'S', 'SIM', 'Si', 'SI']
naoValido = ['n', 'nao', 'não', 'ñ', 'Ñ', 'Não', 'NÃO']
while True:
    n = int(input("Digite um Número Inteiro maior que 2: "))
    print("-="*20)
    i = n
    if n >= 2:
        f0 = 0
        f1 = 1
        print("0 \n1")
        n -= 2
        while n > 0:
            fn = f0 + f1
            f0 = f1
            f1 = fn
            print(fn)
            n -= 1
        print("-="*20)
        x = input("Gostaria de digitar mais um número?")
        if x in simValido:
            print("-="*20)
            i = 1
        elif x in naoValido:
            break
        else:
            print("Por favor, leia as instruções e comece novamente")
    else:
        print("Leia as instruções de entrada e comece de novo.")
        i = 1
print("Obrigado. Tenha um ótimo dia!")
