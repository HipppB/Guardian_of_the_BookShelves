import os
from pathlib import Path
import json

def get_project_root() -> Path:
    return Path(__file__).parent
    # renvoie au chemin du dossier racine on l'utilise dans tous les acces au fichiers

def loadBook():
    bookList = os.listdir(os.path.join(get_project_root(), 'books'))
    return bookList 
    # ["bookTitle1","bookTitle2"]

def listPages(book):
    pageList = []
    fileList = os.listdir(os.path.join(get_project_root(), 'books', book, 'Pages'))
    for p in fileList:
        page = json.load(open(os.path.join(get_project_root(), 'books', book, 'Pages', p)))
        pageString = (str(page["ID"]) + '. ' + page["Name"])
        pageList.append(pageString)
    return pageList 
    # ["0. PageName", "1. PageName"]

def loadPage(book, page):
    Page = json.load(open(os.path.join(get_project_root(), 'books', book, 'Pages', page)))
    return Page

def menuPageView(book, page):
    Clear()
    Page = json.load(open(os.path.join(get_project_root(), 'books', book, 'Pages', page)))
    line()
    printTitle((book + " -- " + Page["Name"] + " : "), centered = True)
    emptyline()
    printSentence(Page["Text"])
    emptyline()
    line()

print(loadPage())