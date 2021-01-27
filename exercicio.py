print ('WELCOME TO THE EXERCISE')


n1 = float(input('Primeira nota do teste:'))
n2 = float(input('Segunda nota da prova:'))
media = (n1 +n2)/2
print(f'Sua media foi de:{(n1 + n2)/2}')

if media >= 5.0:
    print('passou')

if media < 5.0:
    print('nao passou')

