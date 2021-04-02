import os
import json
from pathlib import Path

def get_project_root() -> Path:
  return Path(__file__).parent

LoadPage = {
  "ID": 1,
  "title": "Main",
  "Description": "string",
  "Book": "Book1",
  "choices": {
    "0": {
      "Name": "MainStreet",
      "Page": 2,
      "GiveItem": [],
      "TakeItem": []
    },
    "1": {
      "Name": "string",
      "Page": 1,
      "GiveItem": ["Sword"],
      "TakeItem": []
    }
  }
}

def savePage(pageData):

  bookName = pageData.get("Book")
  pageID = pageData.get("ID")
  pageTitle = pageData.get("title")

  pageName = str(pageID) + "." + str(pageTitle) + ".json"

  filePath = os.path.join(get_project_root(), 'Books', bookName, pageName )

  file = open(filePath, "r+")
  file.truncate(0)
  json.dump(LoadPage, file)
  file.close()

savePage(LoadPage)