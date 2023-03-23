# Dette er til skellettet af koden


choise = EncryptOrDecrypt() # returner 0 eller 1

if choise == 0: # Encrypt
    text = getTextInput(choise)
    key = getKe y()
    textWithoutSpace = removeSpace(text)
    decryptedText = decrypt(text, key)
    # print(decryptedText)

elif choise == 1: # Decrypt
    text = getTextInput(choise)
    key = getKey()
    encryptedText = encrypt(text, key)
    # print(encryptedText)















def getTextInput(choise):
    checkIfOnlyText()


def EncryptOrDecrypt():
    pass


def checkIfOnlyText(): #returner true hvis stringen kun er bogstaver
    pass


def decrypt():
    pass


def encrypt():
    pass


def getKey(): #skal returnere
    pass
    checkIfOnlyText()



def removeSpace():
    pass