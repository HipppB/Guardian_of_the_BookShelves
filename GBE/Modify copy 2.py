import GBE.Load as Load
import os
page = 1

def pageFileName(pageData):
    pageID = pageData.get("ID")
    pageTitle = pageData.get("title")
    pageName = str(pageID) + "." + str(pageTitle) + ".json"
    return pageName


def deletePage(book, page):
    book = Load.loadBook(book)
    print(book)
    if type(page) == type(1):    
        for i in book:
            if i['ID'] == page:
                page = pageFileName(i)
                ID = i['ID']
                break
    os.remove(os.path.join(Load.get_project_root(), 'books', book, page ))
    for i in book:
        if i['ID'] > ID:
            i['ID'] = i['ID'] - 1
    print(book)

deletePage('TheBook', 'Page0.json')
