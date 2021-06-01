import os
from pathlib import Path
import json

 # Manage exeption


def get_project_root() -> Path:
    return Path(__file__).parent.parent
    # renvoie au chemin du dossier racine on l'utilise dans tous les acces au fichiers

def loadBook(book):
    Books = []
    try:
        fileList = os.listdir(os.path.join(get_project_root(), 'Books', book))
        for p in fileList:
            page = json.load(open(os.path.join(get_project_root(), 'Books', book, p)))
            Books.append(page)
        return Books
    except IOError:
        print("Book not accessible")
        return None


def listBook():
    bookList = []
    fileList = os.listdir(os.path.join(get_project_root(), 'Books'))
    for book in fileList:
        bookList.append(book)
    return bookList 
    # ["1. bookTitle1","2. bookTitle2"]

def listPages(book):
    pageList = [[],[]]
    fileList = sorted(os.listdir(os.path.join(get_project_root(), 'Books', book)))
    for p in fileList:
        page = json.load(open(os.path.join(get_project_root(), 'Books', book, p)))
        pageList[0].append(p)
        pageList[1].append(page["title"])
    return pageList
    # [["0.PageName1.json", "1.PageName2.json"]["PageName1", "PageName2"]]

def loadPage(book, page):
    try:
        Page = json.load(open(os.path.join(get_project_root(), 'Books', book, page)))
        return Page
    except IOError:
        print("This page does not exist")
        return None
    # Dictionnary of the page in python format

def pageNumber(book):
    num = len(listPages(book)[1])
    return num

def listLinks(Book, advanced = None):
    if advanced == None:
        links = []
    else:
        links = {}

    ListofPages = listPages(Book)
    for page in ListofPages[0]:
        
        PageData = loadPage(Book, page)
        if advanced != None:
            links[PageData["ID"]] = []
        for choice in PageData["choices"]:
            if advanced == None:
                links.append([PageData["ID"], PageData["choices"][choice]["Name"], PageData["choices"][choice]["Page"]])
            else:
                links[PageData["ID"]].append(PageData["choices"][choice]["Page"])
    return links
    # [ [PageID, ChoiceName, Page Direction], [PageID, ChoiceName, Page Direction]]


# A book is considered as finish if all path can lead to an end page and if all pages are accessible
# Their must be no loops (A page can be visited only once)
# A non finish book can be launch but is indicated
def isBookFinished(Book):
    #Let's get all the links between page
    links = listLinks(Book, " ")
    #print(links)
    travelDone = {}
    #print(len(listPages(Book)[1]))
    #print(travelDone)
    def analyseTravel(pageNum):
        if pageNum not in travelDone:
            travelDone[pageNum] = []
        try:
            if len(links[pageNum]) != 0:
                for pageNumDest in links[pageNum]:
                    # If we haven't made the test we do it
                    if not pageNumDest in travelDone[pageNum]:
                        if travelDone[pageNum]:
                            travelDone[pageNum].append(pageNumDest)
                        else:
                            travelDone[pageNum] = [pageNumDest]
                        analyseTravel(pageNumDest)
        except:
            return False
        #if len(links[pageNum]) == 0:
            #print("There is an end in page", pageNum)
    
    analyseTravel(0)
    #print(travelDone)

    if links != travelDone:
        return False
    else:
        return True

def getArgument(book, page, argument):
    page = loadPage(book, page)
    try:
        research = page[argument]
        return research
    except IOError:
        return None


