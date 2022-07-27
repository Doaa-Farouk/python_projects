def translate(word):
    '''Funstion to change vowel letters to z letter'''
    translation = ""
    for letter in word.upper():
        if letter in "AEUOI":
            translation += "Z"
              
        else:
            translation += letter
           
    return translation


print(translate("Omar"))
