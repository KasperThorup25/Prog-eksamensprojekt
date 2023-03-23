def encryptChar(textChar, keyChar):
    encryptCharAscii = ord(keyChar) - 97 + ord(textChar)
    if encryptCharAscii > 122:
        encryptCharAscii -= 26
    return chr(encryptCharAscii)


def decryptChar(textChar, keyChar):
    encryptCharAscii = ord(keyChar) - 97 - ord(textChar)
    if encryptCharAscii > 122:
        encryptCharAscii += 26
    return chr(encryptCharAscii)




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



text = input("text: ")
key = input("key: ")

print(scramble(text,key))