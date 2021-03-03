from packfunctions import line, printTitle, emptyline, printSentence, Choice, Clear

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