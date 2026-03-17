# APROVANDO EMPRÉSTIMO
import time as t

valor_casa = int(input('Digite o valor da casa:\n'))
entrada = int(input('Digite o valor da entrada:\n'))
minimo = valor_casa * 0.20 # vai calcular os 20% minimos da entrada
if entrada < minimo:
    print('O valor da entrada da casa está abaixo dos 20% mínimos recomendados pela CAIXA ECONOMICA FEDERAL. Deseja prosseguir mesmo assim?')
    resposta = input('S para SIM e N para NÃO:\n').lower()
    if input != 's' or input != 'sim':
        print('O Programa encerra aqui.')
        exit()

print('Perfeito! Vamos prosseguir.') # caso o comprador prossiga mesmo assim
salario = int(input('Digite o valor do seu salario:\n'))
anos = int(input('Em quantos anos deseja pagar a casa?\n'))
    # transformando anos em meses
meses = anos * 12

prestacao = valor_casa / meses
limite = salario * 0.30
if prestacao > limite: # se exceder 30% do salario, o emprestimo sera negado
    print('Calculando.')
    t.sleep(0.8)

    print('Calculando..')
    t.sleep(0.8)

    print('Calculando...')
    t.sleep(0.8)

    print('Empréstimo negado! o valor da prestação ultrapassa o limite de 30% do salário.')
    print(f'Valor da prestação: R$${prestacao:.2f}, O seu limite é de R${limite:.2f}')
else:
    print('Empréstimo concedido! Vá até uma agência para saber mais. =)')
    print(f'Valor da prestação: R$${prestacao:.2f}, O seu limite é de R${limite:.2f}')