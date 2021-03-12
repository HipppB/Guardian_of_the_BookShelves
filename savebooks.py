import json
from ClassBook import Book, Page
#Ceci simule la création d'un livre test avec 2 pages:




def FormatPage(thePage):
    page = {}
    page["ID"] = thePage.get_ID()
    page["title"] = thePage.get_pageTitle()
    page["description"] = thePage.get_pagedescription()
    page["Book"] = thePage.get_book()
    page["choices"] = thePage.get_choices(method = 2)
    #Cette fonction retourne le dictionnaire page, on utilisera
    # json.dumps(page, indent=4) pour formater le dictionnaire en Json lors de l'ecriture
    #Cela permet de ne pas passer par une String intermédiaire
    return page




TestPage = {"ID": 1, "title": "Ceci est une page", "Description": "Ceci est une très très longue descripion", "Book":"Le livre test", "choices":{0:{ "Name": "Quit", "Page": 0, "GiveItem": None, "TakeItem": None}, 1:{ "Name": "Take the Sword", "Page": 1, "GiveItem": "Sword", "TakeItem": None}} }
def WritePage(thePage):
    with open('./Test.json', 'w', encoding='utf-8') as f:
        json.dump(thePage, f, indent=4)



