import os
import json
from pathlib import Path

def get_project_root() -> Path:
  return Path(__file__).parent.parent

def savePage(pageData):

  bookName = pageData.get("Book")
  pageID = pageData.get("ID")
  pageTitle = pageData.get("title")

  pageName = str(pageID) + "." + str(pageTitle) + ".json"

  filePath = os.path.join(get_project_root(), 'Books', bookName, pageName )

  file = open(filePath, "r+")
  file.truncate(0)
  json.dump(pageData, file)
  file.close()

