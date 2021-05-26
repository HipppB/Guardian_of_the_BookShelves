from . import Basics as Ba, Load, Modify, Save

# Menu Principal
def mainMenu():
    while True:
        Ba.clear()
        Ba.line()
        Ba.printTitle("Welcome in the book Editor !", centered = True)
        Ba.emptyLine()
        Ba.printSentence("From here you can modify, create and list all the books that have been created and that are in the file system !")
        Ba.emptyLine()
        Ba.printSentence("List of your books :")
        ListBooks = Load.listBook()
        ListTheBooks(ListBooks, Mode = "List")
        Ba.emptyLine()
        #Mettre la liste des livres ici
        Ba.line()
        listchoices = ["Create Book", "Edit Book", "Delete Book", "Duplicate Book", "Quit Program"]
        NumChoice = Ba.Choice(listchoices)
        Ba.printSentence("You choose the choice number " + str(NumChoice))
        Ba.line()
        #Redirection
        if NumChoice == 0:
            LoadedBook = menuCreateNewBook()
            menuEditBook(LoadedBook)
            pass
        if NumChoice == 1:
            menuListBook(EditMode= True)
        if NumChoice == 2:
            menuDeleteBook(ListBooks)
        if NumChoice == 3:
            Save.copyBook(menuListBook(EditMode= "Return"))

        if NumChoice == 4:
            break
    Ba.clear()
    Ba.line()
    Ba.printTitle("Closing the program", centered = True)
    Ba.emptyLine()
    Ba.printSentence("See you soon !")
    Ba.emptyLine()
    Ba.line()


# Menu CreateNewBook

def menuListBook(EditMode = False):
    Ba.clear()
    Ba.line()
    Ba.printTitle("List of all books :", True)
    Ba.emptyLine()
    ListBooks = Load.listBook()
    if EditMode == "Return":
        ListTheBooks(ListBooks, Mode = "ID")
        Ba.emptyLine()
        Ba.line()
        Ba.printTitle("Choose a Book by typing its number", True)
        BookNumber = Ba.inputNumber(range(0, len(ListBooks)))
        Ba.line()
        return ListBooks[BookNumber]
    if EditMode:
        ListTheBooks(ListBooks, Mode = "ID")
    else:
        ListTheBooks(ListBooks, Mode = "List")
    Ba.emptyLine()
    Ba.line()
    if EditMode:
        Ba.printTitle("Choose a Book to edit by typing its number", True)
        BookNumber = Ba.inputNumber(range(0, len(ListBooks)))
        Ba.line()
        menuEditBook(ListBooks[BookNumber])
    else:
        listchoices = ["Back To Home Screen", "Edit a Book"]
        NumChoice = Ba.Choice(listchoices)
        if NumChoice == 0:
            pass
        elif NumChoice == 1:
            menuListBook(EditMode= True)


def menuDeleteBook(ListBooks):
    Ba.clear()
    Ba.line()
    Ba.printTitle("List of all books : Choose One to delete", True)
    Ba.emptyLine()
    ListTheBooks(ListBooks, Mode = "List")
    Ba.emptyLine()
    Ba.line()
    Choice = Ba.inputText(textBefore="Enter the name of the book you want to delete : ", FromList= ListBooks, verification = True)
    if Choice == "exit program":
        pass
    else:
        Save.DeleteFolder(Choice)
        print(Choice)
    input()
            
def ListTheBooks(ListBooks, Mode = "List"):
    i = 0
    for Book in ListBooks:
        if Mode == "ID":
            Ba.printSentence(str(i) +". " + Book)
            i += 1
        if Mode == "List":
            Ba.printSentence("- " + Book)

def menuCreateNewBook():
    Ba.clear()
    Ba.line()
    Ba.printTitle("Let's create a new Book !", True)
    Ba.emptyLine()
    Ba.line()
    LoadedBook = Ba.inputText("What is the name of the book ? ",maxlenght=25, verification=True )
    Save.createFolder(LoadedBook)
    Description = Ba.inputText("Enter a brief description of your story, that will be your sinopsis: \n#", maxlenght=10000)
    LoadedPage = Modify.CreateBlankPage(LoadedBook, Description)
    Save.savePage(LoadedPage)
    return LoadedBook

def menuCreatePage(LoadedBook):
    Ba.clear()
    Ba.line()
    Ba.printTitle("Add a page to the book " + LoadedBook, centered=True)
    Ba.emptyLine()
    Ba.printSentence("Choose the name of your new page and a description, you'll be able to modify these information later and so create choices for the user.")
    Ba.emptyLine()
    Ba.printSentence("The number of the page is automatically given and can be modified by the program, you can write " + str("{pageNumber}")  + " to add it in the title or description of your page")
    LoadedPage = Modify.CreatePage(LoadedBook)
    Ba.emptyLine
    Ba.line
    Save.savePage(LoadedPage)
    return LoadedPage

def menuEditPage(LoadedPage):
    Ba.clear()
    Ba.line
def menuEditBook(LoadedBook):
    while True:
        Ba.clear()
        Ba.line()
        Ba.printTitle("Edition of the book " + LoadedBook , True)
        Ba.emptyLine()
        Ba.printSentence("From here you can Add a page, look to all the pages of the book, and even more ! Just enter what you want to do !")
        Ba.printSentence("The Page number 0 is the main page of your book.")
        Ba.emptyLine()
        ListPage = Load.listPages(LoadedBook)
        Ba.printSentence("Pages in this book :")
        ListTheBooks(ListPage[1], Mode = "List")
        Ba.emptyLine()
        Ba.line()
        listchoices = ["Create page", "Delete a Page", "Modify a Page", "See Links between page", "Quit"]
        NumChoice = Ba.Choice(listchoices)
        if NumChoice == 0:
            menuCreatePage(LoadedBook)
        elif NumChoice == 1:
            menuListPages(LoadedBook, Mode= "Delete")
        elif NumChoice == 2:
            menuListPages(LoadedBook, Mode= "Modify")
        elif NumChoice == 3:
            MenuDisplayLinks(LoadedBook)
        elif NumChoice == 4:
            break
        else:
            print("Their was a problem !")
            
# Sous menu Edit Book

def menuListPages(LoadedBook, Mode= "List"):
    Ba.clear()
    Ba.line()
    ListPage = Load.listPages(LoadedBook)
    if Mode == "List":
        Ba.printTitle("List of all pages" + LoadedBook , True)
        Ba.emptyLine()
        Ba.line()
        for Page in ListPage[1]:
            Ba.printSentence("- " + Page)
        listchoices = ["Modify a Page", "Delete a Page", "Quit"]
        Ba.emptyLine()
        Ba.line()
        NumChoice = Ba.Choice(listchoices)
        if NumChoice == 0:
            menuListPages(LoadedBook, Mode= "Modify")
        elif NumChoice == 1:
            menuListPages(LoadedBook, Mode= "Delete")
        elif NumChoice == 2:
            pass
        

    elif Mode == "Modify":
        Ba.printTitle("Select a page to Modify" + LoadedBook , True)
        Ba.emptyLine()
        Ba.line()
        i = 0
        for Page in ListPage[1]:
            Ba.printSentence(str(i) +". " + Page)
            i += 1
        Ba.emptyLine()
        
        NumChoice = Ba.inputNumber(range(0, i + 1))
        menuViewPage(LoadedBook, [ListPage[0][NumChoice],ListPage[1][NumChoice]])
        Ba.line()


    elif Mode == "Delete":
        Ba.printTitle("Select a page to delete" + LoadedBook , True)
        Ba.printTitle("/!\\ Cannot be delete ! /!\\" + LoadedBook , True)
        Ba.emptyLine()
        Ba.line()
        for Page in ListPage[1]:
            Ba.printSentence("- " + Page)   
        NumChoice = Ba.inputText(textBefore="Enter the name of the page you want to delete : ", FromList= ListPage[1])
        #Call the delete function with parameter "page" to delete a page
        input("TO DO mais ca à bien recu l'ordre de supprimer la page suivante : " + NumChoice)
        Modify.deletePage(LoadedBook, ListPage[1].index(NumChoice))


    Ba.emptyLine()
    Ba.line()



def menuViewPage(LoadedBook, Page):
    while True:
        # We load the page :
        LoadedPage = Load.loadPage(LoadedBook, Page[0])
        # We display the screen :
        Ba.clear()
        Ba.line()
        Ba.printTitle("Modifying the page " + LoadedPage["title"], centered=True)
        Ba.emptyLine()
        Ba.printSentence("Name of the book : " + LoadedPage["Book"])
        Ba.emptyLine()
        Ba.printSentence("Page Name : " + LoadedPage["title"])
        Ba.emptyLine()
        Ba.printSentence("Page Number : " + str(LoadedPage["ID"]))
        Ba.emptyLine()
        Ba.printSentence("Page Text :")
        Ba.printSentence(LoadedPage["Description"])
        Ba.emptyLine()
        Ba.printSentence("List of the choices :")
        for key in LoadedPage["choices"]:
            Ba.printSentence("- " + LoadedPage["choices"][key]["Name"] + " -> Go to page " + str(LoadedPage["choices"][key]["Page"]))
            Ba.printSentence("Gives :", Alinea=True)
            if len(LoadedPage["choices"][key]["GiveItem"]) != 0:
                for Item in LoadedPage["choices"][key]["GiveItem"]:
                    Ba.printSentence("- " + Item, Alinea=True)
            else:
                Ba.printSentence("Nothing", Alinea=True)
            Ba.printSentence("Takes  :", Alinea=True)
            if len(LoadedPage["choices"][key]["TakeItem"]) != 0:
                for Item in LoadedPage["choices"][key]["TakeItem"]:
                    Ba.printSentence("- " + Item, Alinea=True)
            else:
                Ba.printSentence("Nothing", Alinea=True)
        listchoices = ["Modify Name", "Modify Description", "Modify Choices", "Back"]
        Ba.emptyLine()
        Ba.line()
        NumChoice = Ba.Choice(listchoices)
        if NumChoice == 0:
            NewName = Ba.inputText("Enter a new name for the page : ", typeInput="title")
            NewData = Modify.ChangePageName(LoadedPage, NewName)
            LoadedPage = NewData[0]
            Page[0] = NewData[1]
        elif NumChoice == 1:
            LoadedPage = Modify.ChangePageDescription(LoadedPage)
        elif NumChoice == 2:
            LoadedPage = menuEditChoices(LoadedPage)
        elif NumChoice == 3:
            break
        # We save the page before leaving
        Save.savePage(LoadedPage)
    pass

def MenuDisplayLinks(LoadedBook):
    Ba.clear()
    Ba.line()
    Ba.printTitle("All links in the book " + LoadedBook, centered=True)
    Ba.emptyLine()
    Ba.printSentence("Format : Number of the page Page (Choice Name) -> Number of the page it goes to")
    Ba.emptyLine()
    Load.listLinks(LoadedBook)
    for choice in Load.listLinks(LoadedBook):
        Ba.printSentence("- " + str(choice[0]) + " (" + choice[1] + ") -> " + str(choice[2]))
    Ba.emptyLine()
    Ba.line()
    input("You can not modify page links from here, press enter to go back to previous menu")

def menuEditChoices(LoadedPage):
    while True:
        Ba.clear()
        Ba.line()
        Ba.printTitle("Choices of " + LoadedPage['title'], centered=True)
        Ba.emptyLine()
        for key in LoadedPage["choices"]:
            Ba.printSentence(str(key)+ "- " + LoadedPage["choices"][key]["Name"] + " -> Go to page " + str(LoadedPage["choices"][key]["Page"]))
            Ba.printSentence("Gives :", Alinea=True)
            if len(LoadedPage["choices"][key]["GiveItem"]) != 0:
                for Item in LoadedPage["choices"][key]["GiveItem"]:
                    Ba.printSentence("- " + Item, Alinea=True)
            else:
                Ba.printSentence("Nothing", Alinea=True)
            Ba.printSentence("Takes  :", Alinea=True)
            if len(LoadedPage["choices"][key]["TakeItem"]) != 0:
                for Item in LoadedPage["choices"][key]["TakeItem"]:
                    Ba.printSentence("- " + Item, Alinea=True)
            else:
                Ba.printSentence("Nothing", Alinea=True)
        Ba.line()
        listchoices = ["Create Choice", "Delete Choice" , "Modify Choice", "Back"]
        Ba.emptyLine()
        NumChoice = Ba.Choice(listchoices)
        if NumChoice == 0:
            #Just add a choice !
            LoadedPage = menuCreateChoice(LoadedPage)
        elif NumChoice == 1:
            LoadedPage = menuDeleteChoice(LoadedPage)
        elif NumChoice == 2:
            LoadedPage = Modify.modifyChoice(LoadedPage)
        elif NumChoice == 3:
            break
        #We rearrange all Choices ID not to skip any numbers due to modifications like deleting a choice
        LoadedPage = Modify.resetChoiceID(LoadedPage)
    return LoadedPage

def menuCreateChoice(LoadedPage):
    Ba.clear()
    Ba.line()
    Ba.printTitle("Creation of a new Choice in " + LoadedPage['title'], centered=True)
    Ba.emptyLine()
    NewChoice = {"Name": "Untitled", "Page": 0, "GiveItem": [], "TakeItem": []}
    NewChoice["Name"] = Ba.inputText("Name of the Choixe", maxlenght=20)
    RangePage = range(0, Load.listPages(LoadedPage["Book"]))
    NewChoice["Page"] = Ba.inputNumber(textBefore="Where does the choice leads to ? Enter the page number", rangeNumber=RangePage)
    LoadedPage = Modify.createChoice(LoadedPage, NewChoice)
    return LoadedPage

def menuDeleteChoice(LoadedPage):
    Ba.clear()
    Ba.line()
    Ba.printTitle("Delete a choice of " + LoadedPage['title'], centered=True)
    Ba.emptyLine()
    listchoices = []
    for key in LoadedPage["choices"]:
        listchoices.append(LoadedPage["choices"][key]["Name"])
        Ba.printSentence("- " + LoadedPage["choices"][key]["Name"] + " -> Go to page " + str(LoadedPage["choices"][key]["Page"]))
        Ba.printSentence("Gives :", Alinea=True)
        if len(LoadedPage["choices"][key]["GiveItem"]) != 0:
            for Item in LoadedPage["choices"][key]["GiveItem"]:
                Ba.printSentence("- " + Item, Alinea=True)
        else:
            Ba.printSentence("Nothing", Alinea=True)
        Ba.printSentence("Takes  :", Alinea=True)
        if len(LoadedPage["choices"][key]["TakeItem"]) != 0:
            for Item in LoadedPage["choices"][key]["TakeItem"]:
                Ba.printSentence("- " + Item, Alinea=True)
        else:
            Ba.printSentence("Nothing", Alinea=True)
    Ba.emptyLine()
    if len(listchoices) == 0:
        print("There is no choice to delete.")
    else:
        ChoiceToDelete = Ba.inputText("Input the choice NAME you want to delete : ", verification= True, FromList=listchoices)
        Modify.deleteChoice(LoadedPage, listchoices.index(ChoiceToDelete))
    return LoadedPage

