


def getTextInput(choise):
    while True:
        if choice == "encrypt":
            encryptText = input("\nPlease write the text you want to Encrypt: ")
            if checkIfOnlyText(removeSpace(encryptText)) == True:
                return removeSpace(encryptText)
        elif choice == "decrypt":
            decryptText = input("\nPlease write the text you want to Decrypt: ")
            if checkIfOnlyText(removeSpace(decryptText)) == True:
                return removeSpace(decryptText)


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


def decryptChar(textChar, keyChar):
    decryptCharAscii = ord(textChar) - (ord(keyChar) - 97)
    if decryptCharAscii < 97:
        decryptCharAscii += 26
    return chr(decryptCharAscii)

def encryptChar(textChar, keyChar):
    encryptCharAscii = ord(keyChar) - 97 + ord(textChar)
    if encryptCharAscii > 122:
        encryptCharAscii -= 26
    return chr(encryptCharAscii)


def scramble(text, key, decryptOrEncrypt):
    encryptedText = ""
    keyLength = len(key)
    keyIndex = 0
    for i in range(len(text)):
        if decryptOrEncrypt == "decrypt":
            encryptedText += decryptChar(text[i].lower(), key[keyIndex])
        elif decryptOrEncrypt == "encrypt":
            encryptedText += encryptChar(text[i].lower(), key[keyIndex])
        keyIndex += 1
        if keyIndex >= keyLength:
            keyIndex = 0
    return encryptedText




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
    encryptedText = scramble(text, key, choice)
    print(encryptedText)

elif choice == "decrypt": # Decrypt
    text = getTextInput(choice)
    key = getKey()
    decryptedText = scramble(text, key, choice)
    print(decryptedText)