import Basics as Ba

def MenuEditor():
    Text = []
    while True:
        Ba.line()
        Ba.printTitle("GBE text editor")
        Ba.emptyLine()
        Ba.printSentence("From here, each action is definitive, the text is saved after each line modification")
        Ba.printSentence("The numbers are only here to display line Numbers, they won't appear in final text")
        Ba.printSentence("Actual Text :")
        Ba.printSentence("Indiquer la description ici")
        for i in range(0, len(Text)):
            Ba.printSentence(str(i) + " #" + Text[i])
        Ba.emptyLine()
        Choices = ["New Line", "Delete Line", "Insert Line", "Modify Line", "Quit"]
        NumChoice = Ba.Choice(Choices)
        if NumChoice == 0:
            pass
        elif NumChoice == 1:
            pass
        elif NumChoice == 2:
            pass
        elif NumChoice == 3:
            return Text

MenuEditor()