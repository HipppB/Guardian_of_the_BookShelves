import Basics

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

def resetChoiceID(PageData):
    choiceList = list(PageData["numbers"])
    valueList = []
    for value in choiceList:
        valueList.append(value)
    PageData["numbers"] = dict(zip(valueList, range(len(valueList))))

    return PageData


def createChoice(PageData):
    newChoice = { "Name": "", "Page": 0, "GiveItem": [], "TakeItem": [] }
    numChoices = len(LoadPage["choices"])
    LoadPage["choices"][int(numChoices)] = newChoice
    return LoadPage


def deleteChoice(PageData):
    choiceToRemove = Basics.inputText("Choice to remove ? :")
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

print(LoadPage)

resetChoiceID(LoadPage)

print(LoadPage)

#modifyChoice(LoadPage)
#createChoice(LoadPage)



