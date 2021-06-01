from GBE import Basics as Ba
from GBE import Load
from GBE import Menus as Me
import time

def mainMenu():
    Ba.clear()
    print(Ba.playerASCII)
    print("Loading...")
    time.sleep(1)
    LoadedBook = Me.menuListBook(EditMode="Return")
    ListPages = Load.listPages(LoadedBook)
    LoadedPage = Load.loadPage(LoadedBook, ListPages[0][0])
    inventory = {}
    try:
        PageMenu(LoadedPage, inventory=inventory)
        while Ba.inputText("Do you want to restart the book ? [y/n]", FromList=["Y", "y", "N", "n"]).lower() == "y":
            inventory.clear()
            PageMenu(LoadedPage, inventory)
    except:
        print("Seems you tried to access a non existing page. This may appen if you play on a Non finished Book.")

def displayInv(inventory):
    Ba.printSentence("Your Inventory : ")
    for item in inventory:
        Ba.printSentence(str(item) + " (*" +  str(inventory[item]) + ")", Alinea=True)
    if len(inventory) == 0:
        Ba.printSentence("Your inventory is empty.", Alinea=True)
    return

def ChangeInventory(Choice, inventory):
    for item in Choice["GiveItem"]:
        if item.lower() in inventory:
            inventory[item.lower()] = inventory[item.lower()] + 1
        else:
            inventory[item.lower()] = 1
    for item in Choice["TakeItem"]:
        if item.lower() in inventory:
            inventory[item.lower()] = inventory[item.lower()] - 1
        if inventory[item.lower()] == 0:
            del inventory[item.lower()]
    return inventory

def CheckIfItem(TakeItem, inventory):
    for item in TakeItem:
        if not item.lower() in inventory:
            return item
    return True
def PageMenu(Page, inventory, Fail = None):
    
    Ba.clear()
    if Fail != None:
        print(Fail)
    Ba.line()
    Ba.printTitle("Book : " + Page['Book'], centered=True)
    Ba.line()
    Ba.printTitle("Page : " + Page['title'], centered=True)
    Ba.emptyLine()
    Ba.emptyLine()
    displayInv(inventory=inventory)
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
        CheckItemChoice = CheckIfItem(Page['choices'][str(choice)]['TakeItem'], inventory=inventory)
        if CheckItemChoice == True:
            newPageID = Page['choices'][str(choice)]['Page']
            newPageName = str(listPages[0][newPageID])
            newPage = Load.loadPage(Page['Book'], newPageName)
            inventory = ChangeInventory(Page['choices'][str(choice)], inventory=inventory)
            PageMenu(newPage, inventory=inventory)
        else:
            errorMsg = "Unfortunatly you need the item " + str(CheckItemChoice) + " to select this choice ! Please Select another option."
            PageMenu(Page, inventory=inventory, Fail = errorMsg)
