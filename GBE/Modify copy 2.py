import Load
import os
import Basics

def pageFileName(pageData):
    page = 1
    pageID = pageData.get("ID")
    pageTitle = pageData.get("title")
    pageName = str(pageID) + "." + str(pageTitle) + ".json"
    return pageName

def deletePage(bookName, page):
    Book = Load.loadBook(bookName)
    print(Book)
    if type(page) == type(1):
        for i in Book:
            if i['ID'] == page:
                page = pageFileName(i)
                ID = i['ID']
                break
            
    os.remove(os.path.join(Load.get_project_root(), 'books', bookName, page ))
    Book = Load.loadBook(bookName)

    for i in Book:
        if i['ID'] > int(ID):
            i['ID'] = i['ID'] - 1
        print('\n')
        print(i)

    Save.saveBook()
deletePage('TheBook', 1)
