def word_mesh(words):
    wordBefore=""
    for currentWord in words:
        print(currentWord)
        if wordBefore =="":
            wordBefore=currentWord
        else:
            for character in currentWord:
                wordBefore.find(character)
    return ""