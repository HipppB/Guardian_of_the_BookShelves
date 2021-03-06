from init import lengthmenu, lengthspace
def Clear():
    print("\n" * 40)

def line():
    print("#" * lengthmenu)

def emptyline():
    print("#" + " " * lengthspace + "#")

def printSentence(sentence, centered = False):
    words = sentence.split()
    print("# ", end="")
    totallength = 1
    for word in words:
        totallength += len(word) + 1
        if totallength <= lengthspace:
            print(word, end=" ")
        else:
            print(" " * (lengthspace - (totallength - len(word) - 1)) + "#", end="")
            print("\n# ", end="")
            print(word, end=" ")
            totallength = len(word) + 2
    print(" " * (lengthspace - (totallength)) + "#")
def printTitle(sentence, centered = False):
    length = len(sentence) + 2
    if centered == False:
        print("# " + sentence + " " * (lengthspace - length) +" #")
    else:
        if length % 2 != 0:
            print("#" + " " * int((lengthspace - length)/2), sentence, " " * int((lengthspace - length)/2) + "#")
        else:
            print("#" + " " * int((lengthspace - length)/2), sentence, " " * int((lengthspace + 1 - length)/2) + "#")

def inputtexte(TextBefore = ""):
    print("# ", end="")
    if TextBefore != "":
        print(TextBefore, end=" ")
    question = input()
    line()
    return question

def Choice(listeChoice):
    NbDeChoice = len(listeChoice)
    Choice = listeChoice
    if NbDeChoice > 15:
        print("Trop de Choice, maximum = 15")
        return 400
    def printChoices(FirstLine = False):
        paternes = {1:(1,), 2:(2,), 3:(3,), 4:(4,), 5:(3,2), 6:(3,3), 7:(4,3), 8:(4,4), 9:(3,3,3), 10:(4,3,3), 11:(4,4,3), 12:(4,4,4), 13:(4,4,3,2), 14:(4,4,3,3), 15:(4,4,4,3)}
        paterne = paternes[NbDeChoice]
        NbFait = 0
        if FirstLine:
            line()
        for row in paterne:
            numCase = 0
            print("#", end="")
            lengthCase = (lengthspace + 1 - row)/row
            for i in range(NbFait, row + NbFait):
                longueurMot = len(Choice[i]) + len(str(i)) + 2
                if longueurMot % 2 != 0:
                    Choice[i] = Choice[i] + " "
                    longueurMot += 1 
                NbEspace = lengthCase - longueurMot
                if row % 2 == 0:
                    numCase += 1
                    if ((row == 4) and (numCase == 2 or numCase == 3)) or row == 2:
                        if longueurMot % 2 == 0:
                            print(" " * int(NbEspace/2 + 1) + str(i) + ". " + Choice[i] + " " * int(NbEspace/2 - 1), end="#")
                        else:
                            print(" " * int(NbEspace/2) + str(i) + ". " + Choice[i] + " " * int(NbEspace/2 - 1), end="#")
                    else:
                        if longueurMot % 2 == 0:
                            print(" " * int(NbEspace/2 + 1) + str(i) + ". " + Choice[i] + " " * int(NbEspace/2), end="#")
                        else:
                            print(" " * int(NbEspace/2) + str(i) + ". " + Choice[i] + " " * int(NbEspace/2), end="#")
                else:
                    if longueurMot % 2 == 0:
                        print(" " * int(NbEspace/2 + 1) + str(i) + ". " + Choice[i] + " " * int(NbEspace/2), end="#")
                    else:
                        print(" " * int(NbEspace/2) + str(i) + ". " + Choice[i] + " " * int(NbEspace/2), end="#")
            NbFait += row
            print()
            line()
    printChoices()
    while True:
        try:
            choice = int(inputtexte("Please enter the number of your choice : "))
            if choice > (NbDeChoice - 1):
                Clear()
                printSentence("Invalid choice ! the valid choices are:")
                printChoices(True)
            else:
                break
        except:
           printSentence("You must input an integer !")
    return choice