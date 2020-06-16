domaci_zvirata = ["pes", "kočka", "králík", "had"]
jina_zvirata = ["had", "pes", "andulka", "kočka", "lenochod"]
import operator

for zvire in domaci_zvirata:
    if len(zvire) < 5:
        print(zvire)
    
for zvire in domaci_zvirata:    
    if zvire[0] == 'k':
        print(zvire)

text = input('Napiš zvíře: ')
if text in domaci_zvirata:
    print('True')
else:
    print('False')

seznam1 = list(set(domaci_zvirata) & set(jina_zvirata))
print(seznam1)

seznam2 = list(set(domaci_zvirata) - set(jina_zvirata))
print(seznam2)

seznam3 = list(set(jina_zvirata) - set(domaci_zvirata))
print(seznam3)

sort = sorted(domaci_zvirata)
print(sort)

# ukol 6
abc = {}

for zvire in jina_zvirata:      
    abc[ord(zvire[1])] = zvire      # serazeni podle druheho pismena (na zaklade hodnoty ASCII)
print(abc)

keys = abc.keys()
values = abc.values()
print(keys, values)
