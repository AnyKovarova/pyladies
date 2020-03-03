a = int(input('Zadej stranu čtverce: '))
cislo_je_spravne = a > 0
O = 4 * a
S = a**2
r = a
pi = 3.1415926
obvod_kruhu = 2 * pi * r
obsah_kruhu = pi * r**2

# print('Obvod ctverce se stranou 356 cm je ', 4 * 356 ,'cm.')
# print('Obsah ctverce se stranou 356 cm je ', 356 * 356 ,'cm2.')
if cislo_je_spravne:
    print('Obvod ctverce se stranou 356 cm je ', O ,'cm.')
    print('Obsah ctverce se stranou 356 cm je ', S ,'cm2.')
    print('Obvod kruhu s poloměrem ', r ,'je ', obvod_kruhu ,'cm.')
    print('Obsah kruhu s poloměrem ', r ,'je ' , obsah_kruhu ,'cm2.')
else:
    print('Strana musí být kladná, jinak z toho nebude čtverec!')

print('Děkujeme za použití geometrické kalkulačky.')