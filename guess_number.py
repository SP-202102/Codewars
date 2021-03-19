# RATEZAHL!!
# ein kleines Spiel, bei dem der Computer sich eine Zahl ausdenkt, die der Spieler raten muss
#
from random import *

maximumNumber = 10

# Computer denkt sich Zahl aus
computerNumber = round( random()* maximumNumber )
# print("gewählte Zahl: " + str( computerNumber ) )

# hier soll die Rate-Schleife loslaufen
playAgain = True

while playAgain:
    
    # Spieler rät Zahl
    guessedNumber = 0
    userInput = input("Bitte Zahl eingeben: ")

    # erst prüfen, ob es überhaupt eine Zahl ist
    try:
        guessedNumber = int(userInput)
    except ValueError:
        print('Eingabe war GAR KEINE ZAHL!')   
        #TODO: Schleife neu starten
    except TypeError:
        print("Dussel: du kannst die Typen nicht mischen! Die MÖGEN SICH NICHT!")
        #TODO: Schleife neu starten

    # ab hier ist guessedNumber auf jeden Fall ein Integer
    if (guessedNumber > maximumNumber):
            print("Deine Zahl muss zwischen 0 und " + str(maximumNumber) + " liegen!")
    else:
        # Computer sagt, ob Zahl größer oder kleiner oder richtig ist
        if (guessedNumber == computerNumber):
            print("YES, richtig geraten!!!!")
            # Wenn richtig: Schleife beenden
            playAgain = False
            if input("Willst du nochmal spielen? ").upper() == "JA":
                playAgain = True
                computerNumber = round( random()* maximumNumber )
        else:
            if (guessedNumber > computerNumber):
                print("Deine geratene Zahl ist zu GROSS!")
            else:
                print("Deine geratene Zahl ist zu KLEIN!")
                
                
                

