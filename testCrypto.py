                                                                # Create a file called testCrypto.py.
                                                                # In testCrypto.py, test (and output the results) of both encrypt and decrypt 3 times.

def encryptMessage():
    msg = input('Enter a message to encrypt it... ')
    cipherText = scramble2Encrypt(msg)
    print('Encrypted message = ', cipherText)

def scramble2Encrypt(plainText):
    evenCharacters = ""
    oddCharacters = ""
    characterCount = 0
    for ch in plainText:
        if characterCount % 2 == 0:
            evenCharacters = evenCharacters + ch
        else:
            oddCharacters = oddCharacters + ch
        characterCount = characterCount + 1
    cipherText = oddCharacters + evenCharacters
    return cipherText

def scramble2Decrypt(cipherText):
    halfLength = len(cipherText) // 2
    oddCharacters = cipherText[:halfLength]
    evenCharacters = cipherText[halfLength:]
    plainText = ""

    for i in range(halfLength):
        plainText = plainText + evenCharacters[i]
        plainText = plainText + oddCharacters[i]

    if len(oddCharacters) < len(evenCharacters):
        plainText = plainText + evenCharacters[-i]

    return plainText

def encryptMessage():
    msg = input('Enter a message to encrypt... ')
    cipherText = scramble2Encrypt(msg)
    print('Encrypted message = ', cipherText)
def decryptMessage():
    msg = input('Encrypted message = ')
    plainText = scramble2Decrypt(msg)
    print('Decrypted message = ', plainText)

msg = input('Enter a message to encrypt... ')
cipherText = scramble2Encrypt(msg)
print('Encrypted message = ', cipherText)

msg = input('Enter a message to decrypt... ')
plainText = scramble2Decrypt(msg)
print('Decrypted message = ', plainText)

msg = input('Enter a message to encrypt... ')
cipherText = scramble2Encrypt(msg)
print('Encrypted message = ', cipherText)

msg = input('Enter a message to decrypt... ')
plainText = scramble2Decrypt(msg)
print('Decrypted message = ', plainText)

msg = input('Enter a message to encrypt... ')
cipherText = scramble2Encrypt(msg)
print('Encrypted message = ', cipherText)

msg = input('Enter a message to decrypt... ')
plainText = scramble2Decrypt(msg)
print('Decrypted message = ', plainText)