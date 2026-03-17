# alistamento
ano_atual = int(input('Digite o ano atual:\n'))
ano_nascimento = int(input('digite seu ano de nascimento:\n'))
alistamento = ano_atual - ano_nascimento
if alistamento == 18:
    print('Você já tem 18 anos, então, é hora de se alistar!')
elif alistamento > 18:
    print('Você já passou da hora de se alistar. Procure fazer o alistamento IMEDIATAMENTE!')
elif alistamento < 18:
    print('Você ainda não está na hora de se alistar.')
else:
    print('ai é foda patrao')