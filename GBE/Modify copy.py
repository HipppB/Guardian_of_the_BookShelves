import Basics

LoadPage = {
  "ID": 1,
  "title": "Main",
  "Description": "string",
  "Book": "Book1",
  "choices": {
    "0": { "Name": "Choix1", "Page": 0, "GiveItem": [], "TakeItem": [] },
    "2": { "Name": "Choix2", "Page": 1, "GiveItem": ["Sword"], "TakeItem": [] },
    "8": { "Name": "Choix3", "Page": 1, "GiveItem": ["Sword"], "TakeItem": [] },
  }
}

def resetChoiceID(PageData):

    valueList = list(PageData["choices"].values())

    PageData["choices"] = {}

    for entry in valueList:
        PageData["choices"][str(valueList.index(entry))] = entry

    return PageData


def createChoice(PageData):
    newChoice = { "Name": "", "Page": 0, "GiveItem": [], "TakeItem": [] }
    numChoices = len(LoadPage["choices"])
    LoadPage["choices"][numChoices] = newChoice
    return LoadPage


def deleteChoice(PageData):


    choiceToRemove = str(Basics.inputText("ID of choice you want remove : "))

    del PageData["choices"][choiceToRemove]

    return PageData


def modifyChoice(PageData):
    choiceToChange = Basics.inputText("ChoiceNumberToEdit :")
    choiceData = PageData["choices"][choiceToChange]

    partToChange = Basics.inputText("Change Name, Page, GiveItem or TakeItem:")
    valueToChange = Basics.inputText("Into what : ")
    if partToChange == "Page":
        valueToChange = int(valueToChange)


    choiceData[partToChange] = valueToChange

    return PageData

deleteChoice(LoadPage)
resetChoiceID(LoadPage)

print(LoadPage)

#modifyChoice(LoadPage)
#createChoice(LoadPage)



