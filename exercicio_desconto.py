D = float(input('Qual é o preço do produto? R$'))

desc = float(D*5/100)

descFinal = D - desc


print(f'O produto que custava R${D}, na promoçao com 5% de desconto caiu para {descFinal}')

