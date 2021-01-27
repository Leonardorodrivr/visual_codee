altura = float(input('Quanto de altura tem sua parade, em metros?:'))
largura = float(input('Quanto tem de largura sua parede, em metros?:'))

area = altura * largura
latas_de_tinta = area / 2


print(f'Sua parede tem {altura:.0f} Metros de altura, e sua largura é de {largura:.0f} Metros, Sua area é de {area:.0f} Metros, Entao sao necessarias {latas_de_tinta:.0f} Litros de tinta para que pinte toda a parede')


