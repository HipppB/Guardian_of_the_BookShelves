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

def resetChoiceID(PadeData):
    choiceList = list(PadeData["numbers"])
    for i in choiceList
    list(x.keys()).index("c")



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



#deleteChoice(LoadPage)
#modifyChoice(LoadPage)
#createChoice(LoadPage)
print(LoadPage)

