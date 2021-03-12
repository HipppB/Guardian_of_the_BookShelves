import json
from ClassBook import Book, Page
import os
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



TheBook = "TestBook"
TestPage = {"ID": 1, "title": "Ceci_est_une_page", "Description": "Ceci est une très très longue descripion", "Book":"Le livre test", "choices":{0:{ "Name": "Quit", "Page": 0, "GiveItem": None, "TakeItem": None}, 1:{ "Name": "Take the Sword", "Page": 1, "GiveItem": "Sword", "TakeItem": None}} }

def WritePage(theBook, thePage):
    path = "./books/" + theBook + "/" + str(thePage["ID"]) + "." + thePage["title"] + ".json"
    if not os.path.exists("./books/" + theBook):
        os.makedirs("./books/" + theBook)
    with open(path, 'w', encoding='utf-8') as f:    
        json.dump(thePage, f, indent=4)
    print("done")


WritePage(TheBook, TestPage)

def LoadBook(bookname):
    if not os.path.exists("./books/" + bookname):
        return 404
    else:
        
