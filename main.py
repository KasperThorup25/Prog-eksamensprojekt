#Dette er til skellettet af koden


choise = EncryptOrDecrypt() #returner 0 eller 1

if choise == 0: #Encrypt
    text = getTextInput(choise)
    key = getKey()
    decryptedText = decrypt(text, key)
    #print(decryptedText())

elif choise == 1: #Decrypt
    text = getTextInput(choise)
    key = getKey()
    encryptedText = encrypt(text, key)
    # print(encryptedText())















def getTextInput(choise):
    checkIfNotText()


def EncryptOrDecrypt():
    pass


def checkIfNotText(): #returner true eller false
    pass


def decrypt():
    pass


def encrypt():
    pass


def getKey():
    pass