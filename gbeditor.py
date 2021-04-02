import os
#from utils.uiFunctions import line, printTitle, emptyline, printSentence, Choice, Clear
from pathlib import Path
import json
#Inittialisation of the program, the width of the menu could potentially adapt per book
lengthmenu = 103
lengthspace = lengthmenu - 2


###########################################################################################################################""


def get_project_root() -> Path:
    return Path(__file__).parent

def getBooks():
    bookList = os.listdir(os.path.join(get_project_root(), 'books'))
    return bookList

def getFiles(book):
    fileList = os.listdir(os.path.join(get_project_root(), 'books', book ))
    return fileList

def getPages(book):
    pageView = []
    pageDict = {}
    fileList = os.listdir(os.path.join(get_project_root(), 'books', book))
    for p in fileList:
        page = json.load(open(os.path.join(get_project_root(), 'books', book, p)))
        pageString = (str(page["ID"]) + '. ' + page["Name"])
        pageView.append(pageString)
    return pageView 


###########################################################################################################################""

def menuList():
    Clear()
        #La fonction line creer une ligne de tableau
    line()
    #L'argument True centre le titre
    printTitle("Here are the books on your computer :", centered = True)
    #Saute une ligne
    emptyline()
    #La fonction printSentence ne permet pas de centrer le texte mais retourne à la ligne automatiquement
    for f in getBooks():
        printSentence(f)    
    emptyline()
    line()
    #La fonction Choice prend une liste des Choice et creer automatiquement l'interface dans la limite de 15 Choice. Les Choice doivent faire moins de 21 caractères
    listchoices = ["Back to Menu", "Choose Book", "Quit Program"]
    NumChoice = Choice(listchoices) #Return the choice
    print("You choose the choice number", NumChoice)
    if NumChoice == 0:
        mainMenu()
    if NumChoice == 1:
        while True:
            bookChoice = input("What book do you want to see ?")
            menuBookView(bookChoice)

    if NumChoice == 2:
        quit

###########################################################################################################################""

def menuBookView(book):
    pages = getPages(book)
    Clear()
    line()
    printTitle(("Here are the pages of " + book + " : "), centered = True)
    emptyline()
    for f in pages:
        printSentence(f)
    emptyline()
    line()
    listchoices = ["Back", "Choose Page", "Quit Program"]
    NumChoice = Choice(listchoices) #Return the choice
    print("You choose the choice number", NumChoice)
    if NumChoice == 0:
        menuList()
    if NumChoice == 1:
        pageChoice = input("what page do you want to see ? : ")
        if type(pageChoice) =='integer':

        menuPageView(book, pageChoice)
    if NumChoice == 2:
        quit

###########################################################################################################################""

def menuPageView(book, page):
    Clear()
    Page = json.load(open(os.path.join(get_project_root(), 'books', book, page)))
    line()
    printTitle((book + " -- " + Page["Name"] + " : "), centered = True)
    emptyline()
    printSentence(Page["Text"])
    emptyline()
    line()

###########################################################################################################################""

def mainMenu():
    Clear()
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
    listchoices = ["Create Book", "Edit Book", "List Books", "Quit Program"]
    NumChoice = Choice(listchoices) #Return the choice
    print("You choose the choice number", NumChoice)
    if NumChoice == 0:
        menuNewBook()
    if NumChoice == 2:
        menuList()
    if NumChoice == 4:
        quit

###########################################################################################################################""

def menuNewBook():
    Clear()
    confirmation = False
    while not confirmation:
        line()
        printTitle("Let's create a new Book !", True)
        emptyline()
        printTitle("What is the name of the book ? ")
        emptyline()
        line()
        BookTitle = input("")
        
        if input("Confirm the name of your book Please: \n") == BookTitle:
            confirmation = True
        else:
            print("The names does not match !")
    Clear()
    confirmation = False
    while not confirmation:
        line()
        printTitle("Creation of the book " + BookTitle , True)
        emptyline()
        printSentence("From here you can Add a page, look to all the pages of the book, and even more ! Just enter what you want to do !")
        printSentence("The first page you create will be the principal page of your book.")
        emptyline()
        line()
        listchoices = ["Create page", "Delete Page", "View Page", "Create Item", "See all Pages", "See all Links", "Quit Program"]
        NumChoice = Choice(listchoices)
        
        if NumChoice != 404:
            confirmation = True
        else:
            print("Their was a problem !")
          
###########################################################################################################################""
  
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