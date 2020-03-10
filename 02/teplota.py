teplota = int(input('Kolik stupňů má voda? '))
if teplota <= 0:
    print('Brrr, to je led!')
elif teplota <= 10:
    print('Hmm, ideální na osvěžující drink!')
elif teplota <= 20:
    print('No, na koupání to nebude :D.')
elif teplota <= 35 :
    print('Na moře dobrý.')
elif teplota <= 45 :
    print('Ideální teplota vody ve vaně!')
elif teplota <= 59 :
    print('Prostě horká voda.')
elif teplota <= 70 :
    print('Zalij zelený čaj!')
elif teplota <= 80 :
    print('Zalij bílý čaj!')
elif teplota <= 90 :
    print('Zalij oolong!')
elif teplota <= 100 :
    print('Zalij černý caj!')
elif teplota <= 200 :
    print('Pára!')
else:
    print('Takové teploty nejsou potřeba :D ')