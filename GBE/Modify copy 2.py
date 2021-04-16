import Load
import os
import Basics
import Save
def pageFileName(pageData):
    page = 1
    pageID = pageData.get("ID")
    pageTitle = pageData.get("title")
    pageName = Save.formatString(str(pageTitle)) + ".json"
    return pageName

def deletePage(bookName, page):
    Book = Load.loadBook(bookName)
    for i in Book:
        if i['ID'] == page:
            page = pageFileName(i)
            ID = i['ID']
            Book.pop(i)
            break
    try: 
        os.remove(os.path.join(Load.get_project_root(), 'Books', bookName, page ))
        Book = Load.loadBook(bookName)
        for i in Book:
            if i['ID'] > int(ID):
                i['ID'] = i['ID'] - 1
            Save.savePage(i)
    except:
        print('No page to delete')

deletePage('TheBook', 1)
