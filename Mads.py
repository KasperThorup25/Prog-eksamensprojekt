def checkIfOnlyText(textInput):
    for i in range(len(textInput)):
        if 65 > ord(textInput[i]) < 90 or 97 < ord(textInput[i]) > 122:
            return False
    return True


#text = input("text: ")
#print(checkIfOnlyText(text))