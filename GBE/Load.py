import os
from pathlib import Path
import json

def get_project_root() -> Path:
    return Path(__file__).parent.parent
    # renvoie au chemin du dossier racine on l'utilise dans tous les acces au fichiers

def loadBook(book):
    Books = []
    fileList = os.listdir(os.path.join(get_project_root(), 'books', book))
    for p in fileList:
        page = json.load(open(os.path.join(get_project_root(), 'books', book, p)))
        Books.append(page)
    return Books

def listBook():
    fileList = os.listdir(os.path.join(get_project_root(), 'books'))
    return fileList 
    # ["bookTitle1","bookTitle2"]

def listPages(book):
    pageList = []
    fileList = sorted(os.listdir(os.path.join(get_project_root(), 'books', book)))
    for p in fileList:
        page = json.load(open(os.path.join(get_project_root(), 'books', book, p)))
        pageList.append(page["title"])
    return [fileList, pageList]
    # [["0.PageName.json", "1.PageName.json"]["PageName", "PageName"]]

def loadPage(book, page):
    Page = json.load(open(os.path.join(get_project_root(), 'books', book, page)))
    return Page
    # Dictionnary of the page in python format

def pageNumber(book):
    num = len(listPages(book)[1])
    return num

