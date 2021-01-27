import random
p = input('Primeiro aluno:')
a = input('Segundo aluno:')
m = input('Terceiro aluno:')
v = input('Quarto aluno:')

name = [p, a, m, v]
s = random.choice(name)

print(f'O aluno sorteado foi: {s}')

