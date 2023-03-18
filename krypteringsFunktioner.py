def encryptChar(textChar, keyChar):
    encryptCharAscii = ord(keyChar) - 97 + ord(textChar)
    if encryptCharAscii > 122:
        encryptCharAscii -= 26
    return chr(encryptCharAscii)




def encrypt(text, key):
    encryptedText = ""
    keyLength = len(key)
    keyIndex = 0
    for i in range(len(text)):
        encryptedText += encryptChar(text[i],key[keyIndex])
        keyIndex += 1
        if keyIndex >= keyLength:
            keyIndex = 0
    return encryptedText



text = input("text: ")
key = input("key: ")

print(encrypt(text,key))