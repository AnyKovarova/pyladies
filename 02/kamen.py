import random

ruka = ['kámen', 'nůžky', 'papír']
tah_cloveka = input('kámen, nůžky, nebo papír? ')

if tah_cloveka not in ruka:
    print('Nerozumím.')
    exit()

tah_pocitace = random.choice(ruka)

print('Počítač:', tah_pocitace)

if tah_cloveka == tah_pocitace:
    print('Plichta.')
elif (
        (tah_cloveka == 'kámen' and tah_pocitace != 'papír')
        or (tah_cloveka == 'nůžky' and tah_pocitace != 'kámen')
        or (tah_cloveka == 'papír' and tah_pocitace != 'nůžky')
    ):
    print('Vyhrál jsi!')
else:
    print('Prohrál jsi!')
