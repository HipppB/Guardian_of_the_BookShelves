from GBE import Basics as Ba
from GBE import Load
from GBE import Menus as Me

def mainMenu():
    print(Ba.playerASCII)
    Me.menuListBook(EditMode="Return")

def BookMenu(LoadedBook):
    Ba.clear()
    Ba.line()
<<<<<<< Updated upstream
    Ba.printTitle(LoadedBook["title"])
    pass
    while True:
        Ba.clear()
        Ba.line()
        Ba.printTitle("Please select a book to read", centered=True)
        Ba.emptyLine()
        Ba.printSentence("List of the books you can play :")
        ListBooks = Load.listBook()
        Me.ListTheBooks(ListBooks, Mode = "ID")
        Ba.emptyLine()
        Ba.line()
        listchoices = ["Play a Book", "quit"]
        NumChoice = Ba.Choice(listchoices)
        Ba.printSentence("You choose the choice number " + str(NumChoice))
        Ba.line()
        if NumChoice == 0:
            LoadedBook = {}
        if NumChoice == 1:
            break
=======
    Ba.printTitle("Please select a book to read", centered=True)
    Ba.emptyLine()
    Ba.printSentence("List of the books you can play :")
    ListBooks = Load.listBook()
    Me.ListTheBooks(ListBooks, Mode = "ID")

def PageMenu(Page):
    Ba.clear()
    Ba.line()
    Ba.printTitle(Page['title'], centered=True)
    Ba.emptyLine()
    Ba.printSentence((Page['Description']))
    Ba.emptyLine()
    Ba.line()

    listChoicePage = [Page['choices'][str(i)]['Name'] for i in Page['choices']]
    choice = Ba.Choice(listChoicePage)
    Ba.line()

    newPage = Load.loadPage(Page['Book'], pageList(choice))
>>>>>>> Stashed changes
