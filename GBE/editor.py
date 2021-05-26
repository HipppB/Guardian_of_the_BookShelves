import GBE.Basics as Ba

#Can receive, list, string, integers returns list
def MenuEditor(Text):
    if Text == None:
        Text = []
    if not isinstance(Text, list):
        Text = [Text]

    while True:
        Ba.clear()
        Ba.line()
        Ba.printTitle("GBE text editor", centered=True)
        Ba.emptyLine()
        Ba.printSentence("From here, each action is definitive, the text is saved after each line modification")
        Ba.printSentence("The numbers are only here to display line Numbers, they won't appear in final text")
        Ba.printSentence("Actual Text :")
        for i in range(0, len(Text)):
            Ba.printSentence(str(i) + " # " + Text[i])
        Ba.emptyLine()
        Ba.line()
        Choices = ["New Line", "Delete Line", "Modify Line", "Quit"]
        NumChoice = Ba.Choice(Choices)
        if NumChoice == 0:
            print("# Before which line do you want to make a new line ? (To insert at the end: -1)")
            Position = Ba.inputNumber(range(-1, len(Text)))
            if Position == -1:
                Position = len(Text)
            newLine = Ba.inputText("Enter line content :")
            Text.insert(Position, newLine)

        elif NumChoice == 1:
            print("# Enter the line number you want to delete (Irreversible, -1 to cancel)")
            Position = Ba.inputNumber(range(-1, len(Text)))
            if Position == -1:
                print("# Canceled.")
            else:
                Text.pop(Position)
        elif NumChoice == 2:
            print("# Enter the line number you want to modify")
            Position = Ba.inputNumber(range(0, len(Text)))
            newLine = Ba.inputText("Enter new line content :")
            Text.pop(Position)
            Text.insert(Position, newLine)
        elif NumChoice == 3:
            #Return a list of string ()
            return Text
