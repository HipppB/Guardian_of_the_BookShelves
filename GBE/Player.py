from GBE import Basics as Ba
from GBE import Load
from GBE import Menus as Me
import time


def mainMenu():
    inventory = {}
    Ba.clear()
    print(Ba.playerASCII)
    print("Loading...")
    time.sleep(1)
    LoadedBook = Me.menuListBook(EditMode="Return")
    ListPages = Load.listPages(LoadedBook)
    LoadedPage = Load.loadPage(LoadedBook, ListPages[0][0])
    print(LoadedPage)
    PageMenu(LoadedPage)
    while Ba.inputText("Do you want to restart the book ?", FromList=["Yes", "yes", "no", "No"]).lower() == "yes":
        PageMenu(LoadedPage)

def PageMenu(Page):
    Ba.clear()
    Ba.line()
    Ba.printTitle(Page['Book'], centered=True)
    Ba.printTitle(Page['title'], centered=True)
    Ba.emptyLine()
    Ba.printSentence((Page['Description']))
    Ba.emptyLine()
    Ba.line()
    if len(Page['choices']) == 0:
        return False
    else:
        listChoicePage = [Page['choices'][str(i)]['Name'] for i in Page['choices']]
        choice = Ba.Choice(listChoicePage)
        Ba.line()
        listPages = Load.listPages(Page['Book'])
        newPageID = Page['choices'][str(choice)]['Page']
        newPageName = str(listPages[0][newPageID])
        newPage = Load.loadPage(Page['Book'], newPageName)

        PageMenu(newPage)