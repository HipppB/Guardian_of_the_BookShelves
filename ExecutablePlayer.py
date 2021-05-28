from GBE import Player, Load

Player.mainMenu()

Page = Load.loadPage("The gardians of the Bookshelves' Adventure", "0.Book_Description.json")
print(Page)

Player.PageMenu(Page)
