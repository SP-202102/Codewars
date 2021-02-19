def word_mesh(words):
    resultString = ""
    previousWord=""
    for currentWord in words:
        foundMesh = False
        if previousWord == "":
            #first run
            previousWord = currentWord
            #treat first round as true
            foundMesh = True
        else:
            #compare longest chain in current word with last chars from previous
            for i in range(min(len(currentWord), len(previousWord)), 1,-1):
                if currentWord[:i] == previousWord[-i:]:
                    resultString += currentWord[:i]
                    foundMesh = True
                    break
        
        if foundMesh == False:
            return "failed to mesh"

        previousWord = currentWord

    return resultString

print(word_mesh(["allow", "lowering", "ringmaster", "terror"]), "lowringter")
print(word_mesh(["abandon", "donation", "onion", "ongoing"]), "dononon")
print(word_mesh(["jamestown", "ownership", "hippocampus", "pushcart", "cartographer", "pheromone"]), "ownhippuscartpher")
print(word_mesh(["beacon", "condominium", "umbilical", "california"]), "conumcal")

    def word_mesh_with_prints(words):
    resultString = ""
    previousWord=""
    for currentWord in words:
        print("Current Word: '" + currentWord + "'")
        print("=======================================")
        foundMesh = False
        if previousWord == "":
            #first run
            previousWord = currentWord
            #treat first round as true
            foundMesh = True
        else:
            #compare longest chain in current word with last chars from previous
            for i in range(min(len(currentWord), len(previousWord)), 1,-1):
                print("Checking: '" + currentWord[:i] + "' against: '" + previousWord[-i:] + "'")
                if currentWord[:i] == previousWord[-i:]:
                    resultString += currentWord[:i]
                    foundMesh = True
                    break
        
        if foundMesh == False:
            return "failed to mesh"

        previousWord = currentWord

    print("Result: "+resultString)

    return resultString


#this idea was too complicated overall:
# def word_mesh2(words):
    resultString = ""
    previousWord=""
    for currentWord in words:
        print(currentWord)
        if previousWord =="":
            previousWord = currentWord
        else:
            subStringFind = 0
            #check if first chars of second word is in first word
            for i in range(1, len(currentWord)):
                subStringFind = previousWord.rfind(currentWord[:i])
                print("Checking: '" + currentWord[:i] + "'")
                print("Found at: " + str(subStringFind))
                #check, whether we actually found at the END of the word before
                if subStringFind == -1:
                    print("Substring '" + currentWord[:i] + "' Not found at all")
                    break
                elif i + subStringFind == len(previousWord):
                    print("OK, this is the end")
                    #concat the result
                    resultString += currentWord[:i]
                    break
                else:
                    print("damn, somewhere else")
        previousWord = currentWord
        print("Result: "+resultString)

    return resultString
