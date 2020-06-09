def caesar_encrypt (plaintext, key):
  ciphertext = ''
  for c in plaintext: 
    if c == ' ':
      ciphertext = ciphertext + c 
    elif  c.isupper():
      ciphertext = ciphertext + chr((ord(c) + key - 65) % 26 + 65) # zašifruje velká písmena - hodnota "A" v ASCII je 65, ord() získá hodnotu ASCII a po odečtení hodnoty A zjistí fce chr() písmeno
    else:
      ciphertext = ciphertext + chr((ord(c) + key - 97) % 26 + 97) # zašifruje malá písmena - hodnota "a" v ASCII je 97, postup stejný jako u velkých písmen

  
  return ciphertext
 

def caesar_decrypt (ciphertext, key):
  decrypted = ' '
  for c in ciphertext:
    if c == ' ':
      decrypted = decrypted + c 
    elif c.isupper():
      decrypted = decrypted + chr((ord(c) - key - 65) % 26 + 65) # rozšifruje zpět, protože odstraní posun, takže zjistíme původní hodnoty (písmena)
    else:
      decrypted = decrypted + chr((ord(c) - key - 97) % 26 + 97)
  
  return decrypted

print('Vítej ve skriptu pro Césarovu šifru!\n')
text = input('Zadej svůj text: ')

while True:
  key = input('Zadej svoje tajné šifrovací číslo:')
  try:
    int(key)
  except ValueError:
    print('Musí to být celé číslo, zkus to znovu!')
  else:
    key = int(key)
    break
  
print('Původní text:\n ', text)
print('Zašifrovaný text:\n ', caesar_encrypt(text, key))
print('Pro kontrolu zpět rozšifrováno:\n ', caesar_decrypt(caesar_encrypt(text,key),key))


    