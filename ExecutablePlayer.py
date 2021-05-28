from GBE import Player, Load,Basics as Ba

Player.mainMenu()

Page = Load.loadPage("The gardians of the Bookshelves' Adventure", "0.Book_Description.json")
print(Page)

Player.PageMenu(Page)

Ba.printSentence("End of book")
Ba.line()