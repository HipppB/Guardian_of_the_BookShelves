import Basics import printSentence, inputText
from Load import pageNumber

def CreatePage(book):
    printSentence("let's create a page")
    loadPage={}
    loadPage["ID"] = pageNumber(book)
    loadPage["title"] = inputText(textBefore= "Enter a title", maxlenght = 500, verification = False)
    loadPage["description"] = inputText(textBefore= "Enter the description of the Book", maxlenght = 500, verification = False)
    loadPage["book"] = book
    loadPage["choice"]={}
    return loadPage

CreatePage('Book1')