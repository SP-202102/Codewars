
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

print(word_mesh(["beacon", "condominium", "umbilical", "california"]), "conumcal")
print(word_mesh(["allow", "lowering", "ringmaster", "terror"]), "lowringter")
print(word_mesh(["abandon", "donation", "onion", "ongoing"]), "dononon")
print(word_mesh(["jamestown", "ownership", "hippocampus", "pushcart", "cartographer", "pheromone"]), "ownhippuscartpher")
