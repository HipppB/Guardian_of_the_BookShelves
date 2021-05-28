import os
from GBE.Load import pageNumber
from GBE import Load, Save, editor
from GBE.Basics import inputNumber, printSentence, inputText, line

def CreatePage(book):
    line()
    printSentence("let's create a page")
    loadPage={}
    loadPage["ID"] = pageNumber(book)
    loadPage["title"] = inputText(textBefore= "Enter a title : ", maxlenght = 500, verification = False, typeInput = "title")
    loadPage["Description"] = inputText(textBefore= "Enter the description : ", maxlenght = 500, verification = False)
    loadPage["Book"] = book
    loadPage["choices"]={}
    loadPage["end"] = True
    line()
    return loadPage

def CreateBlankPage(book, desc, title=""):
    if title == "":
        title = book
    line()
    loadPage={}
    loadPage["ID"] = pageNumber(book)
    loadPage["title"] = title
    loadPage["Description"] = desc
    loadPage["Book"] = book
    loadPage["choices"]= {}
    loadPage["end"]= True
    line()
    return loadPage

def pageFileName(pageData):
    pageID = pageData.get("ID")
    pageTitle = pageData.get("title")
    pageName = str(pageID) + "." + Save.formatString(str(pageTitle)) + ".json"
    return pageName

def deletePage(bookName, pageNumber):
    Book = Load.loadBook(bookName)
    for i in Book:
        if i['ID'] == pageNumber:
            ID = i['ID']
            os.remove(os.path.join(Load.get_project_root(), 'Books', bookName, str(pageFileName(i)) ))

    for i in Book:
        if i['ID'] > int(ID):
            os.remove(os.path.join(Load.get_project_root(), 'Books', bookName, str(pageFileName(i)) ))
            i['ID'] = i['ID'] - 1
            Save.savePage(i)
    

def ChangePageName(LoadedPage, newName):
    oldPathName = os.path.join(Load.get_project_root(), 'Books', LoadedPage["Book"], pageFileName(LoadedPage))
    LoadedPage["title"] = newName
    newPathName = os.path.join(Load.get_project_root(), 'Books', LoadedPage["Book"], pageFileName(LoadedPage))
    os.rename(oldPathName, newPathName)
    return LoadedPage, pageFileName(LoadedPage)

def ChangePageDescription(LoadedPage):
    LoadedPage["Description"] = editor.MenuEditor(LoadedPage["Description"])
    return LoadedPage


# Choices :

def resetChoiceID(PageData):
    valueList = list(PageData["choices"].values())
    PageData["choices"] = {}
    for entry in valueList:
        PageData["choices"][str(valueList.index(entry))] = entry
    return PageData


def createChoice(PageData, newChoice = { "Name": "untitled", "Page": 0, "GiveItem": [], "TakeItem": [] }):
    numChoices = len(PageData["choices"])
    PageData["choices"][numChoices] = newChoice
    return PageData


def deleteChoice(PageData, choiceToRemove):
    del PageData["choices"][str(choiceToRemove)]
    return PageData


def modifyChoice(PageData):
    choiceToChange = inputText("ChoiceNumberToEdit :")
    #The key is not an Int !
    choiceData = PageData["choices"][choiceToChange]
    partToChange = inputText("Change Name, Page, GiveItem or TakeItem:", FromList=["Name", "Page", "GiveItem", "TakeItem"])
    if partToChange == "GiveItem" or partToChange == "TakeItem":
        option = inputText('Do you want to add or remove an item (add/remove)?', FromList=["add", "remove"])
        item = inputText('Which Item ?')
        
        if option == "add":
            choiceData[partToChange].append(item)
        if option == "remove":
            try:
                choiceData[partToChange].remove(item)
            except:
                printSentence("Their is no such Item. Passing. Press Enter to continue")
                input()
        return PageData
    elif partToChange == "Page":
        RangePage = range(0, len(Load.listPages(PageData["Book"])[0]))
        print(RangePage)
        valueToChange = inputNumber(RangePage, "Enter New Page Number")
    else:
        valueToChange = inputText("Into what : ")
    choiceData[partToChange] = valueToChange
    return PageData
