def binario_para_decimal_manual(binario):
    decimal = 0
    position = 0
    while binario != 0:
        digito = binario % 10
        decimal += digito * 2 ** position
        binario //= 10
        position += 1
    
    return decimal

# Exemplo de uso - Insira o valor para ser convertido entre o parênteses
print(binario_para_decimal_manual())