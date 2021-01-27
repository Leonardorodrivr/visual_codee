dia = int(input('Quantos dias ficou com o carro?'))

valor1 = dia * 60

km = float(input('Quantos km rodou desde que pegou o carro?'))

valor2 = (km * 0.15)

conta_final = valor1 + valor2

print(f'Por dias usados o valor fica em {valor1}R$, em km rodado {valor2:.0F}R$, voce precisa pagar {conta_final:.0F}R$')

