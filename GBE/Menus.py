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
        Ba.emptyLine()
        Ba.line()
        listchoices = ["Create Book", "Edit Book", "List Books", "Quit Program"]
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
            menuListBook(EditMode= False)
        if NumChoice == 3:
            break


# Menu CreateNewBook

def menuListBook(EditMode = False):
    Ba.clear()
    Ba.line()
    Ba.printTitle("List of all books :", True)
    Ba.emptyLine()
    ListBooks = Load.listBook()
    i = 0
    for Book in ListBooks:
        if EditMode:
            Ba.printSentence(str(i) +". " + Book)
            i += 1
        else:
            Ba.printSentence("- " + Book)
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

def menuEditBook(LoadedBook):
    Ba.clear()
    Ba.line()
    Ba.printTitle("Edition of the book " + LoadedBook , True)
    Ba.emptyLine()
    Ba.printSentence("From here you can Add a page, look to all the pages of the book, and even more ! Just enter what you want to do !")
    Ba.printSentence("The Page 0 is the main page of your book.")
    Ba.emptyLine()
    Ba.line()
    listchoices = ["Create page", "Delete Page", "Modify Page", "See all Pages", "See all Links", "Quit"]
    NumChoice = Ba.Choice(listchoices)
    if NumChoice == 0:
        Modify.CreatePage(LoadedBook)
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
    if Mode == "list":
        Ba.printTitle("List of all pages" + LoadedBook , True)
        Ba.emptyLine()
        Ba.line()
        for Page in ListPage[1]:
            Ba.printSentence("- " + Page)

    elif Mode == "Modify":
        Ba.printTitle("Select a page to Modify" + LoadedBook , True)
        Ba.emptyLine()
        Ba.line()
        i = 0
        for Page in ListPage[1]:
            Ba.printSentence(str(i) +". " + Page)
            i += 1
    elif Mode == "Delete":
        Ba.printTitle("Select a page to delete" + LoadedBook , True)
        Ba.printTitle("/!\\ Cannot be delete ! /!\\" + LoadedBook , True)
        Ba.emptyLine()
        Ba.line()
        for Page in ListPage[1]:
            Ba.printSentence("- " + Page)    
    Ba.emptyLine()
    Ba.line()



def menuViewPage(LoadedBook):
    pass