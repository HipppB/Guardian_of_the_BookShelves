from GBE import Basics as Ba
from GBE import Load
from GBE import Menus as Me

def mainMenu():
    while True:
        Ba.clear()
        print(Ba.playerASCII)
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
            loadedBook = Load.loadBook(ListBooks[Ba.inputNumber(range(len(ListBooks)))])
        if NumChoice == 1:
            break
