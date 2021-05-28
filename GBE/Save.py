import os
import shutil
import json
from pathlib import Path
from . import Load

def get_project_root() -> Path:
  return Path(__file__).parent.parent


def savePage(pageData):

  bookName = pageData.get("Book")
  pageID = pageData.get("ID")
  pageTitle = pageData.get("title")

  pageName = str(pageID) + "." + formatString(str(pageTitle)) + ".json"

  filePath = os.path.join(get_project_root(), 'Books', bookName, pageName)

  try:
      file = open(filePath, "w+")
      file.truncate(0)
      json.dump(pageData, file, indent=2)
      file.close()
  except IOError:
      print("This page does not exist")
      return None

def formatString(StringToFormat):
  StringToFormat = StringToFormat.replace(" ", "_").replace(":", "")
  return StringToFormat

def createFolder(bookName):
  filePath = os.path.join(get_project_root(), 'Books', bookName)
  if not os.path.exists(filePath):
        os.makedirs(filePath)

def DeleteFolder(bookName):
    filePath = os.path.join(get_project_root(), 'Books', bookName)
    try:
        shutil.rmtree(filePath)
    except:
        raise

def copyBook(bookName):
  filePath = os.path.join(get_project_root(), 'Books', bookName)
  bookName = bookName + " copy"
  filePath2 = os.path.join(get_project_root(), 'Books', bookName)
  while os.path.exists(filePath2):
    bookName = bookName + " copy"
    filePath2 = os.path.join(get_project_root(), 'Books', bookName)
  shutil.copytree(filePath, filePath2)
  for Page in Load.listPages(bookName)[0]:
    loadedPage = Load.loadPage(bookName, Page)
    loadedPage["Book"] = bookName
    savePage(loadedPage)

def changeBookName(BookName, NewBookName):
  filePath = os.path.join(get_project_root(), 'Books', BookName)
  filePath2 = os.path.join(get_project_root(), 'Books', NewBookName)
  while os.path.exists(filePath2):
    NewBookName = input("This Book Name already exists, please choose another name : ")
    filePath2 = os.path.join(get_project_root(), 'Books', BookName)
  #Copy the book
  shutil.copytree(filePath, filePath2)
  #Change Book pages
  for Page in Load.listPages(NewBookName)[0]:
    loadedPage = Load.loadPage(NewBookName, Page)
    loadedPage["Book"] = NewBookName
    savePage(loadedPage)
  #Delete Old Book
  DeleteFolder(BookName)

  #Returns the New Book Name
  return NewBookName
