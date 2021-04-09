from Load import pageNumber
from Basics import printSentence, inputText, line


def CreatePage(book):
    line()
    printSentence("let's create a page")
    loadPage={}
    loadPage["ID"] = pageNumber(book)
    loadPage["title"] = inputText(textBefore= "Enter a title : ", maxlenght = 500, verification = False, typeInput = "title")
    loadPage["description"] = inputText(textBefore= "Enter the description of the Book : ", maxlenght = 500, verification = False)
    loadPage["book"] = book
    loadPage["choice"]={}
    line()

    return loadPage
