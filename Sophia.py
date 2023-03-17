def getKey():
    print('Hello')
    while True:

        key = input("Which key would you like to use?  ")

        if checkIfNotText(key) == True:
            return key
        else:
            print("You can only use letters, try again")


getKey()