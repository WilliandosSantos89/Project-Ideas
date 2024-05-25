# Implemtação das operações

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Impossível dividir por zero"


def potencia(a, b):
    return a ** b

def resto(a, b):
    return a % b

def raiz(a):
    return a ** (1/2)

def quadrado(a):
    return a ** 2

def cubo(a):
    return a ** 3

def main()
    print('Bem vindos à Calculadora!')
    numero_1 = float('Digite o primeiro valor: ')
    numero_2 = float('Digite o segundo valor: ')

    print('\nEscolha a operação: ')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Potência')
    print('6 - Resto')
    print('7 - Raiz Quadrada')
    print('8 - Quadrado')
    print('9 - Cubo')
    print('0 - Sair')

    opcao = (int(input('Digite o número da opção desejada: ')))

    if opcao == 1:
        resultado = (soma(numero_1, numero_2))
        print(f'O resultado da soma é {resultado}')

    elif opcao == 2:
        resultado = (subtracao(numero_1, numero_2))
        print(f'O resultado da subtração é {resultado}')

    elif opcao == 3:
        resultado = (multiplicacao(numero_1, numero_2))
        print(f'O resultado da multiplicação é {resultado}')
    
    elif opcao == 4:
        resultado = (divisao(numero_1, numero_2))
        print(f'O resultado da divisão é {resultado}')

    elif opcao == 5:
        resultado = (potencia(numero_1, numero_2))
        print(f'O resultado da potência é {resultado}')

    elif opcao == 6:
        resultado = (resto(numero_1, numero_2))
        print(f'O resultado do resto é {resultado}')

    elif opcao == 7:
        resultado = (raiz(numero_1))
        print(f'O resultado da raiz é {resultado}')

    elif opcao == 8:
        resultado = (quadrado(numero_1))
        print(f'O resultado do quadrado é {resultado}')

    elif opcao == 9:
        resultado = (cubo(numero_1))
        print(f'O resultado do cubo é {resultado}')

    elif opcao == 0:
        print('Saindo...')
