def noSpace(message):
    notab = message.replace("\t", "")
    return notab.replace(" ", "")
# Remeber to link noSpace to input
def EncryptOrDecrypt():
    while True:
        AskforEncryptOrDecrypt = input("Type 0 to Encrypt or type 1 to Decrypt: ")
        if "0" in AskforEncryptOrDecrypt:
            print("\nYou Choose Encrypting.")
            return 0
        elif "1" in AskforEncryptOrDecrypt:
            print("\nYou Choose Decrypting.")
            return 1
        else:
            print("\nERROR! Answer may only contain 0 or 1.")
            print("Please try again.\n")
            continue

choice = EncryptOrDecrypt()
def GetTextInput(choice):
    while True:
        if choice == 0:
            encryptText = input("\nPlease write the text you want to Encrypt: ")
            if checkIfOnlyText(encryptText) == True:
                return encryptText
        elif choice == 1:
            decryptText = input("\nPlease write the text you want to Decrypt: ")
            if checkIfOnlyText(decryptText) == True:
                return decryptText
GetTextInput(choice)