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
    listchoices = ["Create Book", "Edit Book", "List Books", "Quit Program"]
    NumChoice = Choice(listchoices) #Return the choice
    print("You choose the choice number", NumChoice)
    if NumChoice == 0:
        menuNewBook()
    if NumChoice == 4:
        quit
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
            
print("bonjour")
Clear()
mainMenu()