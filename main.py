












def getTextInput(choise):
    while True:
        if choice == "encrypt":
            encryptText = input("\nPlease write the text you want to Encrypt: ")
            if checkIfOnlyText(encryptText) == True:
                return encryptText
        elif choice == "decrypt":
            decryptText = input("\nPlease write the text you want to Decrypt: ")
            if checkIfOnlyText(decryptText) == True:
                return decryptText


def EncryptOrDecrypt():
    while True:
        AskforEncryptOrDecrypt = input("Type 0 to Encrypt or type 1 to Decrypt: ")
        if "0" in AskforEncryptOrDecrypt:
            print("\nYou Choose Encrypting.")
            return "encrypt"
        elif "1" in AskforEncryptOrDecrypt:
            print("\nYou Choose Decrypting.")
            return "decrypt"
        else:
            print("\nERROR! Answer may only contain 0 or 1.")
            print("Please try again.\n")
            continue


def checkIfOnlyText(textInput): #returner true hvis stringen kun er bogstaver
    for i in range(len(textInput)):
        if 65 > ord(textInput[i]) < 90 or 97 < ord(textInput[i]) > 122:
            return False
    return True


def scramble(text, key, decryptOrEncrypt):
    encryptedText = ""
    keyLength = len(key)
    keyIndex = 0
    for i in range(len(text)):
        if decryptOrEncrypt == "decrypt":
            encryptedText += encryptChar(text[i],key[keyIndex])
        elif decryptOrEncrypt == "encrypt":
            encryptedText += decryptChar(text[i], key[keyIndex])
        keyIndex += 1
        if keyIndex >= keyLength:
            keyIndex = 0
    return encryptedText


def decryptChar(textChar, keyChar):
    encryptCharAscii = ord(keyChar) - 97 - ord(textChar)
    if encryptCharAscii > 122:
        encryptCharAscii += 26
    return chr(encryptCharAscii)

def encryptChar(textChar, keyChar):
    encryptCharAscii = ord(keyChar) - 97 + ord(textChar)
    if encryptCharAscii > 122:
        encryptCharAscii -= 26
    return chr(encryptCharAscii)


def getKey():
    while True:
        key = input("\nPlease write the key you want to use: ")
        if checkIfOnlyText(key) == True:
            return key

def removeSpace(message):
    notab = message.replace("\t", "")
    return notab.replace(" ", "")







# Dette er til skellettet af koden


choice = EncryptOrDecrypt() # returner "encrypt" eller "decrypt"

if choice == "encrypt": # Encrypt
    text = getTextInput(choice)
    key = getKey()
    textWithoutSpace = removeSpace(text)
    decryptedText = decrypt(text, key)
    # print(decryptedText)

elif choice == "decrypt": # Decrypt
    text = getTextInput(choice)
    key = getKey()
    encryptedText = encrypt(text, key)
    # print(encryptedText)