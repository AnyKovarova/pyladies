print('Odpovídej "ano" nebo "ne".')
stastna_retezec = input('Jsi šťastná? ')
if stastna_retezec == 'ano':
    stastna = True
else:
    if stastna_retezec == 'ne':
        stastna = False
    else:
        print ('Nerozumím.')

bohata_retezec = input('Jsi bohatá? ')
if bohata_retezec == 'ano':
    bohata = True
else:
    if bohata_retezec == 'ne':
        bohata = False
    else:
        print('Nerozumím!')

if bohata:
    if stastna:
        # Je bohatá a zároveň štǎstná, ta se má.
        print('Gratuluji!')
    else:
        print('Zkus se víc usmívat.')
else:
    if stastna:
        # Tady musí být jen šťastná.
        print('Zkus míň utrácet.')
    else:
        # A tady víme, že není ani šťastná, ani bohatá.
        print('To je mi líto.') 