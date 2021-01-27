import math

angulo = float(input('Qual angulo voce quer?'))

cos = math.cos(math.radians(angulo))
sen = math.sin(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print(f'O angulo escolhido foi {angulo:.0f}, o resulado do coseno é {cos:.2f} do seno {sen:.2f} e da tangente é {tan:.2f}')

