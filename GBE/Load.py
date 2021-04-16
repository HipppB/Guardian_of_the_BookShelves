import os
from pathlib import Path
import json

def get_project_root() -> Path:
    return Path(__file__).parent.parent
    # renvoie au chemin du dossier racine on l'utilise dans tous les acces au fichiers

def loadBook(book):
    Books = []
    fileList = os.listdir(os.path.join(get_project_root(), 'Books', book))
    for p in fileList:
        page = json.load(open(os.path.join(get_project_root(), 'Books', book, p)))
        Books.append(page)
    return Books

def listBook():
    bookList = []
    fileList = os.listdir(os.path.join(get_project_root(), 'Books'))
    for book in fileList:
        bookList.append(book)
    return bookList 
    # ["bookTitle1","bookTitle2"]

def listPages(book):
    pageList = [[],[]]
    fileList = sorted(os.listdir(os.path.join(get_project_root(), 'books', book)))
    for p in fileList:
        page = json.load(open(os.path.join(get_project_root(), 'Books', book, p)))
        pageList[0].append(p)
        pageList[1].append(page["title"])
    return pageList
    # [["0.PageName1.json", "1.PageName2.json"]["PageName1", "PageName2"]]

def loadPage(book, page):
    Page = json.load(open(os.path.join(get_project_root(), 'Books', book, page)))
    return Page
    # Dictionnary of the page in python format

def pageNumber(book):
    num = len(listPages(book))
    return num

