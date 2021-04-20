from GBE.Load import pageNumber
from GBE import Load, Save, editor
import os
from GBE.Basics import printSentence, inputText, line

def CreatePage(book):
    line()
    printSentence("let's create a page")
    loadPage={}
    loadPage["ID"] = pageNumber(book)
    loadPage["title"] = inputText(textBefore= "Enter a title : ", maxlenght = 500, verification = False, typeInput = "title")
    loadPage["Description"] = inputText(textBefore= "Enter the description : ", maxlenght = 500, verification = False)
    loadPage["Book"] = book
    loadPage["choices"]={}
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