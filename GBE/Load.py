import os
from pathlib import Path
import json

def get_project_root() -> Path:
    return Path(__file__).parent.parent
    # renvoie au chemin du dossier racine on l'utilise dans tous les acces au fichiers

def loadBook(book):
    Books = []
    try:
        fileList = os.listdir(os.path.join(get_project_root(), 'Books', book))
        for p in fileList:
            page = json.load(open(os.path.join(get_project_root(), 'Books', book, p)))
            Books.append(page)
        return Books
    except IOError:
        print("Book not accessible")
        return None



def listBook():
    bookList = []
    fileList = os.listdir(os.path.join(get_project_root(), 'Books'))
    for book in fileList:
        bookList.append(book)
    return bookList 
    # ["1. bookTitle1","2. bookTitle2"]

def listPages(book):
    pageList = [[],[]]
    fileList = sorted(os.listdir(os.path.join(get_project_root(), 'Books', book)))
    for p in fileList:
        page = json.load(open(os.path.join(get_project_root(), 'Books', book, p)))
        pageList[0].append(p)
        pageList[1].append(page["title"])
    return pageList
    # [["0.PageName1.json", "1.PageName2.json"]["PageName1", "PageName2"]]

def loadPage(book, page):
    try:
        Page = json.load(open(os.path.join(get_project_root(), 'Books', book, page)))
        return Page
    except IOError:
        print("This page does not exist")
        return None
    # Dictionnary of the page in python format

def pageNumber(book):
    num = len(listPages(book)[1])
    return num

def listLinks(Book):
    links = []
    ListofPages = listPages(Book)
    for page in ListofPages[0]:
        PageData = loadPage(Book, page)
        for choice in PageData["choices"]:
            links.append([PageData["ID"], PageData["choices"][choice]["Name"], PageData["choices"][choice]["Page"]])
    return links
