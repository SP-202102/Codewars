# Bart, Lisa & Maggie
#from typing import List, Any

def tolleFunction(some_text):
    print(some_text)


#Beispielliste = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]
Beispielliste = [{'name': 'Bart'}]  
#Beispielliste = []
#Beispielliste = [{'name': 'Bart'}, {'name': 'Lisa'}]
def namelist(names = "test"):
    Ergebnis = ""
    VerarbeiteteNamen: list[Any] = []
    if len(names) == 1:
         Dicteintrag = Beispielliste[0]
         Ergebnis = Dicteintrag["name"] + ",  \"Wrong output for a single name\""
    else:
            for AktuellerName in names:

                if len(names) -1 is len(VerarbeiteteNamen):
                    Ergebnis += " & " + AktuellerName["name"]

                else:
                    VerarbeiteteNamen.append(AktuellerName["name"])
            Ergebnis = ", ".join(VerarbeiteteNamen) + Ergebnis
    return (Ergebnis)
print(namelist(Beispielliste))