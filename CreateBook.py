from packfunctions import line, printTitle, emptyline, printSentence, Choice, Clear

# Menu Principal
def mainMenu():
    #La fonction line creer une ligne de tableau
    line()
    #L'argument True centre le titre
    printTitle("Welcome in the book Editor !", centered = True)
    #Saute une ligne
    emptyline()
    #La fonction printSentence ne permet pas de centrer le texte mais retourne à la ligne automatiquement
    printSentence("From here you can modify, create and list all the books that have been created and that are in the file system !")
    emptyline()
    emptyline()
    line()
    print("Here are your existing books: ")
    print(books)
    emptyline()
    line()
    #La fonction Choice prend une liste des Choice et creer automatiquement l'interface dans la limite de 15 Choice. Les Choice doivent faire moins de 21 caractères
    listchoices = ["Create Book", "Edit Book", "List Books", "Quit Program"]
    NumChoice = Choice(listchoices) #Return the choice
    print("You choose the choice number", NumChoice)
    if NumChoice == 0:
        menuNewBook()
    if NumChoice == 1:
        menuEditBook()
    if NumChoice == 4:
        quit
def menuNewBook():
    Clear()
    confirmation = False
    while not confirmation:
        print("Existing books: ")
        print(books)
        line()
        printTitle("Let's create a new Book !", True)
        emptyline()
        printTitle("What is the name of the book ? ")
        emptyline()
        line()
        BookTitle = input("")
        
        if input("Confirm the name of your book Please: \n") == BookTitle:
            confirmation = True
            books.append(BookTitle)
        else:
            print("The names does not match !")
    Clear()
    confirmation = False
    while not confirmation:
        line()
        printTitle("Creation of the book " + BookTitle , True)
        emptyline()
        printSentence("From here you can Add a page, look to all the pages of the book, and even more ! Just enter what you want to do !")
        printSentence("The first page you create will be the principal page of your book.")
        emptyline()
        line()
        listchoices = ["Create page", "Delete Page", "View Page", "Create Item", "See all Pages", "See all Links", "Quit Program"]
        NumChoice = Choice(listchoices)
        
        if NumChoice != 404:
            confirmation = True
        if NumChoice == 0:
            createPage()
        else:
            print("Their was a problem !")
            
    Description= input("Enter a brief description of your story, that will be your sinopsis: ")

    printSentence("Synopsis: \n" + Description)
    emptyline()
    line()

Clear()

books=['test']

pages={0: "test page", 2: "page 2"}

def menuEditBook():
    line()
    #charger book existant
    #liste de livre
    print(books)
    book_to_edit= input("Which book would you like to edit ? (Write its name) ")
    if book_to_edit in books:
        print("Edition menu of your book: " + book_to_edit)
        listchoices = ["Create page", "Delete Page", "View Page", "Create Item", "See all Pages", "Quit Program"]
        NumChoice = Choice(listchoices)

        if NumChoice== 0:
            createPage()

        if NumChoice==1:
            menuDeletePage()
        
        if NumChoice==2:
            #print list of pages
            print(pages)
            line()
            #ask which page you want to view
            pageview= int(input("Which page would you like to view ? "))
            
            # if pageview in ages print content of the page else display page non existant
            if pageview in pages:
                print(pageview)
            else:
                print("Page non existant")


        if NumChoice==6:
            quit
    else:
        print("book non existant")

#pages is a dictionary
def menuNewpage():
    titlePage= input("Give a title to your page: ")
    sceneNumber= int(input("Enter the scene Number: "))
    pages.append(titlePage)
    loadPage=createPage()
    return loadPage

     
def createPage(book):
    printSentence("let's create a page")
    loadPage={}
    loadPage["ID"]=pageNumber(book)
    loadPage["title"]= input("enter title")
    loadPage["description"]= input("enter a description")
    loadPage["book"]= book
    loadPage["choice"]={}
    return loadPage

def menuDeletePage():
    print(pages)
    while True:
        try:
            Pageid = int(input("Which page would you like to delete ? "))
            answer= ""

            while answer != "yes" and answer != "no":

                answer= input("Are you sure you want to delete this page? (yes/no) \n")
                if  answer == "yes":
                    confirmation = True
                    pages.pop(Pageid)
                    print("Here's the updated list of pages")
                    print(pages)
                elif answer == "no":
                    confirmation= False
                return confirmation

        except:
            print("invalid number")


menuEditBook()