# comparando dois numeros
n1 = int(input('Digite um numero:\n'))
n2 = int(input('Digite outro numero:\n'))
if n1 > n2:
    print(f'o número {n1} é maior que o número {n2}.')
elif n2 > n1:
    print(f'O número {n2} é maior que o número {n1}.')
elif n1 == n2:
    print('Os números são iguais.')
else:
    print('O caractere digitado não corresponde a um número. Tente novamente!')