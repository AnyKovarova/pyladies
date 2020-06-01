
from random import randrange

body = 0;
odpoved = input ('Hraješ hru "Oko bere". Tvým úkolem je získat 21 bodů, ne více, jinak hra končí a ty jsi prohrál! Na začátku máš 0 bodů. Budeš hrát? ANO/NE: ')

while odpoved == 'ano':
    tah_pocitace = randrange(2,11)
    print(tah_pocitace)
    body = body + tah_pocitace
    if body > 21:
        print ('Ups, prohrál/a jsi! Tvoje body:', body)
        quit()
    elif body == 21:
        print ('Vyhrál/a jsi!')
        quit()
    else:
        print('Tvé skóre je:', body)
    odpoved = input('Chceš hrát dál? ANO/NE: ')

if odpoved == 'ne':
    print('Smůla, konec hry!')
    quit()
else :
    print('Nerozumím, končíš!')
    quit()