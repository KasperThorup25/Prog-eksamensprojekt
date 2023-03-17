import re

def checkIfNotText(getTextInput):
    return re.sub(r'[^a-zA-Z\s]', '', getTextInput) # fjern alle non-text characters