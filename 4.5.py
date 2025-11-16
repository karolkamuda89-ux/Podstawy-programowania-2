###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # read the character's code (use ord())
    litera = ord(char)
    # add one to the character's code
    przesunieta = litera + 1
    # replace new character code with its
    # corresponding character (use chr())
    litera_odszyfrowana = chr(przesunieta)
    # add encrypted character to encrypted text
    encrypted_text = encrypted_text  + litera_odszyfrowana 

print(plain_text)
print(encrypted_text)
encrypted_text1 = ''
for char in encrypted_text:
    literka = ord(char)
    przesunieta1 = literka - 1
    literka_odszyfrowana = chr(przesunieta1)
    encrypted_text1 = encrypted_text1 + literka_odszyfrowana
print(encrypted_text)
print(encrypted_text1)