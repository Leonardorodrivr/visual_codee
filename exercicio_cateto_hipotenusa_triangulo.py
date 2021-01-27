from math import hypot

cO = float(input('qual o tamanho do cateto oposto?'))

cA = float(input('qual o tamanho do cateto adjacente?'))

h = hypot(cO, cA)

print(f'a hipotenuas mede {h}')

