import Load
import os
import Basics
import Save

def pageFileName(pageData):
    pageID = pageData.get("ID")
    pageTitle = pageData.get("title")
    pageName = str(pageID) + "." + Save.formatString(str(pageTitle)) + ".json"
    return pageName

def deletePage(bookName, page):
    Book = Load.loadBook(bookName)
    for i in Book:
        if i['ID'] == page:
            ID = i['ID']
            os.remove(os.path.join(Load.get_project_root(), 'Books', bookName, str(pageFileName(i)) ))

    for i in Book:
        if i['ID'] > int(ID):
            os.remove(os.path.join(Load.get_project_root(), 'Books', bookName, str(pageFileName(i)) ))
            i['ID'] = i['ID'] - 1
            Save.savePage(i)
