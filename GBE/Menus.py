from . import Basics as Ba, Load, Modify, Save


# Menu Principal
def mainMenu():
    while True:
        Ba.clear()
        Ba.line()
        Ba.printTitle("Welcome in the book Editor !", centered = True)
        Ba.emptyLine()
        Ba.printSentence("From here you can modify, create and list all the books that have been created and that are in the file system !")
        Ba.emptyLine()
        Ba.printSentence("Liste des livres :")
        ListBooks = Load.listBook()
        ListTheBooks(ListBooks, Mode = "List")
        Ba.emptyLine()
        #Mettre la liste des livres ici
        Ba.line()
        listchoices = ["Create Book", "Edit Book", "Delete Book", "Quit Program"]
        NumChoice = Ba.Choice(listchoices)
        Ba.printSentence("You choose the choice number " + str(NumChoice))
        Ba.line()
        #Redirection
        if NumChoice == 0:
            LoadedBook = menuCreateNewBook()
            menuEditBook(LoadedBook)
            pass
        if NumChoice == 1:
            menuListBook(EditMode= True)
        if NumChoice == 2:
            menuDeleteBook(ListBooks)
        if NumChoice == 3:
            break
    Ba.clear()
    Ba.line()
    Ba.printTitle("Closing the program", centered = True)
    Ba.emptyLine()
    Ba.printSentence("See you soon !")
    Ba.emptyLine()
    Ba.line()


# Menu CreateNewBook

def menuListBook(EditMode = False):
    Ba.clear()
    Ba.line()
    Ba.printTitle("List of all books :", True)
    Ba.emptyLine()
    ListBooks = Load.listBook()
    if EditMode:
        ListTheBooks(ListBooks, Mode = "ID")
    else:
        ListTheBooks(ListBooks, Mode = "List")
    Ba.emptyLine()
    Ba.line()
    if EditMode:
        Ba.printTitle("Choose a Book to edit by typing its number", True)
        BookNumber = Ba.inputNumber(range(0, len(ListBooks)))
        Ba.line()
        menuEditBook(ListBooks[BookNumber])
    else:
        listchoices = ["Back To Home Screen", "Edit a Book"]
        NumChoice = Ba.Choice(listchoices)
        if NumChoice == 0:
            pass
        elif NumChoice == 1:
            menuListBook(EditMode= True)

def menuDeleteBook(ListBooks):
    Ba.clear()
    Ba.line()
    Ba.printTitle("List of all books : Choose One to delete", True)
    Ba.emptyLine()
    ListTheBooks(ListBooks, Mode = "List")
    Ba.emptyLine()
    Ba.line()
    Choice = Ba.inputText(textBefore="Enter the name of the book you want to delete : ", FromList= ListBooks, verification = True)
    if Choice == "exit program":
        pass
    else:
        Save.DeleteFolder(Choice)
        print(Choice)
    input()
            
def ListTheBooks(ListBooks, Mode = "List"):
    i = 0
    for Book in ListBooks:
        if Mode == "ID":
            Ba.printSentence(str(i) +". " + Book)
            i += 1
        if Mode == "List":
            Ba.printSentence("- " + Book)

def menuCreateNewBook():
    Ba.clear()
    Ba.line()
    Ba.printTitle("Let's create a new Book !", True)
    Ba.emptyLine()
    Ba.line()
    LoadedBook = Ba.inputText("What is the name of the book ? ",maxlenght=25, verification=True )
    Save.createFolder(LoadedBook)
    Description = Ba.inputText("Enter a brief description of your story, that will be your sinopsis: \n#", maxlenght=10000)
    LoadedPage = Modify.CreateBlankPage(LoadedBook, Description)
    Save.savePage(LoadedPage)
    return LoadedBook

def menuCreatePage(LoadedBook):
    Ba.clear()
    Ba.line()
    Ba.printTitle("Ajoutez une page au livre " + LoadedBook, centered=True)
    Ba.emptyLine()
    Ba.printSentence("Choisissez le nom de votre nouvelle page et une description, vous pourrez modifier ces informations par la suite ainsi que creer les choix pour l'utilisateur.")
    Ba.emptyLine()
    Ba.printSentence("Le numero de la page est attribué automatiquement et est succeptible d'être modifié par le programme, vous pouvez marquer " + str("{pageNumber}")  + " pour l'inclure dans le titre ou la description de votre page")
    LoadedPage = Modify.CreatePage(LoadedBook)
    Ba.emptyLine
    Ba.line
    Save.savePage(LoadedPage)
    return LoadedPage

def menuEditPage(LoadedPage):
    Ba.clear()
    Ba.line
def menuEditBook(LoadedBook):
    Ba.clear()
    Ba.line()
    Ba.printTitle("Edition of the book " + LoadedBook , True)
    Ba.emptyLine()
    Ba.printSentence("From here you can Add a page, look to all the pages of the book, and even more ! Just enter what you want to do !")
    Ba.printSentence("The Page number 0 is the main page of your book.")
    Ba.emptyLine()
    ListPage = Load.listPages(LoadedBook)
    Ba.printSentence("Pages in this book :")
    ListTheBooks(ListPage[1], Mode = "ID")
    Ba.emptyLine()
    Ba.line()
    listchoices = ["Create page", "Delete a Page", "Modify a Page", "See Links between page", "Quit"]
    NumChoice = Ba.Choice(listchoices)
    if NumChoice == 0:
        menuCreatePage(LoadedBook)
    elif NumChoice == 1:
        menuListPages(LoadedBook, Mode= "Delete")
    elif NumChoice == 2:
        menuListPages(LoadedBook, Mode= "Modify")
    elif NumChoice == 3:
        menuListPages(LoadedBook, Mode= "List")
    elif NumChoice == 4:
        pass
    elif NumChoice == 5:
        pass
    else:
        print("Their was a problem !")
            
# Sous menu Edit Book

def menuListPages(LoadedBook, Mode= "List"):
    Ba.clear()
    Ba.line()
    ListPage = Load.listPages(LoadedBook)
    if Mode == "List":
        Ba.printTitle("List of all pages" + LoadedBook , True)
        Ba.emptyLine()
        Ba.line()
        for Page in ListPage[1]:
            Ba.printSentence("- " + Page)
        listchoices = ["Modify a Page", "Delete a Page", "Quit"]
        Ba.emptyLine()
        Ba.line()
        NumChoice = Ba.Choice(listchoices)
        if NumChoice == 0:
            menuListPages(LoadedBook, Mode= "Modify")
        elif NumChoice == 1:
            menuListPages(LoadedBook, Mode= "Delete")
        elif NumChoice == 2:
            pass
        

    elif Mode == "Modify":
        Ba.printTitle("Select a page to Modify" + LoadedBook , True)
        Ba.emptyLine()
        Ba.line()
        i = 0
        for Page in ListPage[1]:
            Ba.printSentence(str(i) +". " + Page)
            i += 1
        NumChoice = Ba.inputNumber(range(0, i + 1))
        menuViewPage(ListPage[1][NumChoice])


    elif Mode == "Delete":
        Ba.printTitle("Select a page to delete" + LoadedBook , True)
        Ba.printTitle("/!\\ Cannot be delete ! /!\\" + LoadedBook , True)
        Ba.emptyLine()
        Ba.line()
        for Page in ListPage[1]:
            Ba.printSentence("- " + Page)   
        NumChoice = Ba.inputText(textBefore="Enter the name of the page you want to delete : ", FromList= ListPage[1])
        #Appeler la foncton de suppression de page avec comme parametre la page
        input("TO DO mais ca à bien recu l'ordre de supprimer la page suivante : " + NumChoice)


    Ba.emptyLine()
    Ba.line()



def menuViewPage(LoadedPage):
    Ba.clear()
    Ba.line()
    print("Edit de la page \n", LoadedPage)
    pass
