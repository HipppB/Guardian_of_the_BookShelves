LoadPage = {
  "ID": 1,
  "title": "Main",
  "Description": "string",
  "Book": "Book1",
  "choices": {
    "0": { "Name": "", "Page": 0, "GiveItem": [], "TakeItem": [] },
    "1": { "Name": "string", "Page": 1, "GiveItem": ["Sword"], "TakeItem": [] }
  }
}

def createChoice(PageData):
    blankChoice = { "Name": "", "Page": 0, "GiveItem": [], "TakeItem": [] }
    numChoices = len(LoadPage["choices"])
    LoadPage["choices"][int(numChoices)] = blankChoice
    return LoadPage

createChoice(LoadPage)
print(LoadPage)

