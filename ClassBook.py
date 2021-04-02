from gbeditor import line, printTitle, emptyline, printSentence, Choice, Clear

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
        print("Le livre", title, "à été crée")
    
    def get_title(self):
        return self.title
   
    def get_book(self):
        return self.get_title()
    
    def get_pagefile(self, pageid):
        filename = str(pageid) + "." + self.pages[pageid] + ".json"
        return filename

    def edit_title(self, newtitle):
        self.title = newtitle
    

class Page(Book):
    def __init__(self, id, title, description = "", choices = {0:{ "Name": "Quit", "Page": 0, "GiveItem": None, "TakeItem": None}}):
        self.pagetitle = title
        self.pageid = id
        self.pagedescription = description
        self.choices = choices
    def get_ID(self):
        return self.pageid
    def get_pageTitle(self):
        return self.pagetitle
    
    def get_pagedescription(self):
        return self.pagedescription
    
    def get_choices(self, method=0):
        # 0 -> Retourne la liste des ids des choix ex : [0,1,2]
        if method == 0:
            return list(self.choices.keys())
        # 1 -> Retourne la liste des noms des choix dans l'ordre, utile pour passer au generateur de boutton ex : ["Choice 1", "Choice 2"]
        if method == 1:
            listchoix = []
            for key in self.choices:
                listchoix.append(self.choices[key]["Name"])
            return listchoix
        # 2 -> Retourne le dictionnaire de choix
        if method == 2:
            return self.choices
        
    def get_direction(self, idchoix):
        # Retourne le nom de la page associée au choix
        return self.choices[idchoix]["Page"]

    def edit_pageTitle(self, newtitle):
        self.pagetitle = newtitle


    def add_choice(self, name, page, GiveItem = None, TakeItem = None):
        try:
            if len(name) > 21:
                name = input("The choosen name for this choice is too long, please enter another one (Max lenght: 21) : ")
            newChoiceID = len(list(self.choices.keys()))
            try:
                page = int(page)

            except:
                print("The page number must be a number !")
            self.choices[newChoiceID] = {"Name": name, "Page": page, "GiveItem": GiveItem, "TakeItem": TakeItem}
            return "Success"
        except:
            return "Failed"

