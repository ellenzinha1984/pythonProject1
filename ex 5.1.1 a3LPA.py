# Exercício operações matemáticas
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
operacao = input('Digite a operação desejada:\n 1 - Soma\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão\n Qual a opção escolhida? ')
if (operacao=='1'):
    print('A soma entre {} e {} é {}.'.format (n1, n2, n1 + n2))
elif (operacao=='2'):
    print('A subtração de {} e {} é {}.'.format(n1, n2, n1 - n2))
elif (operacao=='3'):
    print('A multiplicação de {} por {} é {}.'.format(n1, n2, n1 * n2))
elif (operacao=='4'):
    print('A divisão de {} por {} é {}.'.format(n1, n2, n1 / n2))
else:
    print('Escolha uma opção válida.')
