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
        print("#" + sentence + " " * (lengthspace - length) +"#")
    else:
        if length % 2 != 0:
            print("#" + " " * int((lengthspace - length)/2), sentence, " " * int((lengthspace - length)/2) + "#")
        else:
            print("#" + " " * int((lengthspace - length)/2), sentence, " " * int((lengthspace + 1 - length)/2) + "#")


def Choice(listeChoice):
    paternes = {1:(1,), 2:(2,), 3:(3,), 4:(4,), 5:(3,2), 6:(3,3), 7:(4,3), 8:(4,4), 9:(3,3,3), 10:(4,3,3), 11:(4,4,3), 12:(4,4,4), 13:(4,4,3,2), 14:(4,4,3,3), 15:(4,4,4,3)}
    NbDeChoice = len(listeChoice)
    Choice = listeChoice
    if NbDeChoice > 15:
        print("Trop de Choice, maximum = 15")
    paterne = paternes[NbDeChoice]
    NbFait = 0
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
        print()
        return input("Please enter the number of your choice : ")

#Inittialisation of the program, the width of the menu could potentially adapt per book
lengthmenu = 103
lengthspace = lengthmenu - 2

# Menu Principal
def mainMenu():
    #La fonction line creer une ligne de tableau
    line()
    #L'argument True centre le titre
    printTitle("Welcome in the book Editor !", centered = True)
    #Saute une ligne
    emptyline()
    #La fonction printSentence ne permet pas de centrer le texte mais retourne à la ligne automatiquement
    printSentence("From here you can modify, create and list all the books that have been created and that are in the file system !")
    emptyline()
    emptyline()
    line()
    #La fonction Choice prend une liste des Choice et creer automatiquement l'interface dans la limite de 15 Choice. Les Choice doivent faire moins de 21 caractères
    listchoices = ["Choice 1", "Choice 2", "Choice 3", "Quit Program"]
    NumChoice = Choice(listchoices) #Return the choice
    print("You choose the choice number", NumChoice)

Clear()
mainMenu()