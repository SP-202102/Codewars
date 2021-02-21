def rot13(message):
    result = ""
    cleartextLower = "abcdefghijklmnopqrstuvwxyz"
    cyphertextLower = "nopqrstuvwxyzabcdefghijklm"

    for c in message:
        if c.isalpha():
            cypherChar= cyphertextLower[cleartextLower.find(c.lower())]
            if (c.isupper()):
                cypherChar = cypherChar.upper()
        else:
            cypherChar = c
        result += cypherChar
        print(c + " - " + cypherChar)
            
    return result

print(rot13("abcG"))