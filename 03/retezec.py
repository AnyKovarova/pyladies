# retezec = 'Ahoj'
# print(retezec.upper())
# print(retezec.lower())
# print(retezec)

# jmeno = input('Zadej jméno: ')
# prijmeni = input('Zadej příjmení: ')

# prvni = jmeno[0].upper()
# druha = prijmeni[0].upper()
# #inicialy = jmeno[0] + prijmeni[0]
# print('Tvoje iniciály jsou: ', prvni + ' ' + druha + '.')

retezec = input('Napiš nějaké slovo:')
pozice = int(input('Kterou pozici mám změnit?'))
znak = input('Za co mám vyměnit?')

pred = retezec[:pozice] #znak na pozici se nepočítá
za = retezec[pozice + 1:] #první znak se počítá, takže potřebuju posunout o jedno, abych se vyhnula znaku, který chci nahradit.

zmena = pred + znak + za
print('Výsledek je: ' + zmena + '!')