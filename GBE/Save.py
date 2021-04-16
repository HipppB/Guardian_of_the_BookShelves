import os
import shutil
import json
from pathlib import Path

def get_project_root() -> Path:
  return Path(__file__).parent.parent


def savePage(pageData):

  bookName = pageData.get("Book")
  pageID = pageData.get("ID")
  pageTitle = pageData.get("title")

  pageName = str(pageID) + "." + formatString(str(pageTitle)) + ".json"

  filePath = os.path.join(get_project_root(), 'Books', bookName, pageName )

  file = open(filePath, "w+")
  file.truncate(0)
  json.dump(pageData, file)
  file.close()

def formatString(StringToFormat):
  StringToFormat = StringToFormat.replace(" ", "_").replace(":", "")
  return StringToFormat

def createFolder(bookName):
  filePath = os.path.join(get_project_root(), 'Books', bookName)
  if not os.path.exists(filePath):
        os.makedirs(filePath)

def DeleteFolder(bookName):
  filePath = os.path.join(get_project_root(), 'Books', bookName)
  if os.path.exists(filePath):
    shutil.rmtree(filePath)

def copyBook(bookName):
  filePath = os.path.join(get_project_root(), 'Books', bookName)
  bookName = bookName + " Copy"
  filePath2 = os.path.join(get_project_root(), 'Books', bookName)
  while os.path.exists(filePath2):
    bookName = bookName + " Copy"
    filePath2 = os.path.join(get_project_root(), 'Books', bookName)
  shutil.copytree(filePath, filePath2)