from GBE import Basics as Ba, Menus as Me, Load

def mainMenu():
    Ba.clear()
    Ba.line()
    Ba.printTitle("Please select a book to read", centered=True)
    Ba.emptyLine()
    Ba.printSentence("List of the books you can play :")
    ListBooks = Load.listBook()
    Me.ListTheBooks(ListBooks, Mode = "ID")
    
mainMenu()