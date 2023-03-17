def noSpace(message):
    notab = message.replace("\t", "")
    return notab.replace(" ", "")
# Remeber to link noSpace to input
def EnOrDe():
    X = True
    while X is True:
        Ask = input("Type 0 to Encrypt or type 1 to Decrypt: ")
        if "0" in Ask:
            print("You Choose Encrypting.")
            break
        if "1" in Ask:
            print("You Choose Decrypting.")
            break
        else:
            print("\nERROR! Answer may only contain 0 or 1.")
            print("Please try again.\n")
            continue

EnOrDe()