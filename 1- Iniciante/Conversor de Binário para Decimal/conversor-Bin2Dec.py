

def binario_para_decimal(binario):
    decimal = int(binario, 2)
    return decimal

def main():
    try:
        converter = input('Digite um valor para ser convertido: ')
        resultado_decimal = binario_para_decimal(converter)
        print(f'O valor {converter} convertido para decimal é {resultado_decimal}')
    except ValueError:
        print('Entrada inválida. Digite uma valor binário válido')

if __name__ == '__main__':
    main()