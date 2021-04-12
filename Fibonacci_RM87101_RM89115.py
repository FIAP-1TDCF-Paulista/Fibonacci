'''
FIAP
Defesa Cibernética - 1TDCF - 2021
Development e Coding for Security
Prof. Ms. Fábio H. Cabrini
Atividade: Check Point 1
Alunos
Nome Gustavo Martins Khairalla - RM: 87101
Nome Kauan Musse - RM: 89115
'''

print('=' * 40)
print('''       SEQUENCIA DE FIBONACCI     ''')
print('=' * 40)

while True:
    num = int(input('\033[31mDigite um numero para ver sua sequencia de FIBONACCI:\033[m '))
    f1 = 0
    f2 = 1
    cont = 3
    print(f'{f1} + {f2}', end='')

    while cont <= num:
        f3 = f1 + f2
        print(f' \033[31m+\033[m {f3}', end='')
        f1 = f2
        f2 = f3
        cont += 1
    print('\033[31m <- FIM\033[m')

    try:
        if num == 0:
            print('Não foi possivel fazer a sequencia de FIBONACCI com o numero zero!')
    finally:
        if num == 1:
            print('Não foi possivel fazer a sequencia de FIBONACCI com o numero um! ')
            continue

    op = str(input('\033[31mVocê deseja ver mais algum termo [S/N]?\033[m ')).strip().upper()[0]
    while op not in 'SN':
        op = str(input('\033[31mVocê deseja ver mais algum termo [S/N]?\033[m ')).strip().upper()[0]
        if op == 'S':
            continue

    if op == 'N':
        break
print('FIM')
