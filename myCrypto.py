                                                                                # Create a file called myCrypto.py.
                                                                                # Implement one of the encryption algorithms using these files.
                                                                                # Make sure you add comments indicating the type of encryption algorithm used.
                                                                                # You should have a method called encrypt and a method called decrypt at the minimum in this file.

                                                                                # Transposition Cipher
def encryptMessage():
    msg = input('Enter a message to encrypt it... ')
    cipherText = doEncrypt(msg)
    print('Encrypted message = ', cipherText)

def doEncrypt(plainText):
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

def doDecrypt(cipherText):
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

msg = input('Enter a message to encrypt...')
cipherText = doEncrypt(msg)
print('Encrypted message = ', cipherText)

msg = input('Enter the given message to decrypt...')
plainText = doDecrypt(msg)
print('Decrypted message = ', plainText)


