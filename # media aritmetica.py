# media aritmetica
print('bem vindo a calculadora de media aritmetica"')

nota1 = float(input('digite a primeira nota:\n'))
nota2 = float(input('digite a segunda nota:\n'))
nota3 = float(input('digite a terceira nota:\n'))

media = (nota1 + nota2 + nota3) / 3
if media > 7:
    print('Parabéns, você passou!')
elif media == 7:
    print('Você passou MUITO arrastado. Estude mais!')
elif media < 7:
    print('Você reprovou. Estude mais!')
else:
    print('Não foi possivel calcular a sua média. Tente calcular novamente!')