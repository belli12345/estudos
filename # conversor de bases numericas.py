# conversor de bases numericas
n = int(input('Digite um numero:\n'))
tipo_conversao = int(input('''Escolha uma base de conversão através dos números:
[ 1 ] para Binário
[ 2 ] para Octal
[ 3 ] para Hexadecimal
INSIRA SUA RESPOSTA:\n'''))

if tipo_conversao == 1:
    print(f'{n} convertido para Binário é: {bin(n) [2:]}!') 
elif tipo_conversao == 2:
    print(f'{n} convertido para Octal é: {oct(n) [2:]}!')
elif tipo_conversao == 3:
    print(f'{n} convertido para Hexadecimal é {hex(n) [2:]}!')
else:
    print('O número que você digitou não corresponde a nenhuma Base de Conversão. Rode o programa novamente e digite o numero certo!')
    exit()