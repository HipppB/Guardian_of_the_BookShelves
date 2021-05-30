lengthmenu = 103
lengthspace = lengthmenu - 2

#CLear terminal View
def clear():
    print("\n" * 100)

#Full Line
def line():
    print("#" * lengthmenu)

#Empty line
def emptyLine():
    print("#" + " " * lengthspace + "#")

#Print a sentence and go to line automatically
def printSentence(sentence, centered = False, Alinea = False):
    if isinstance(sentence, str):
        printAString(sentence, centered, Alinea)
    elif isinstance(sentence, list):
        for line in sentence:
            printAString(line, centered, Alinea)
    else:
        print("There is a Type issue, the Sentence can not be print")

def printAString(sentence, centered = False, Alinea = False):
    sentence = sentence.replace("\n", " ||| ")
    words = sentence.split()

    if Alinea:
        print("#\t ", end="")
    else:
        print("# ", end="")
    if Alinea: 
        totallength = 8
    else:
        totallength = 1
    for word in words:
        totallength += len(word) + 1
        if word == "|||":
            print(" " * (lengthspace - (totallength - len(word) - 1)) + "#", end="")
            print("\n# ", end="")
            totallength = 1
        elif totallength <= lengthspace:
            print(word, end=" ")
        else:
            print(" " * (lengthspace - (totallength - len(word) - 1)) + "#", end="")
            if Alinea:
                print("#\t ", end="")
            else:
                print("\n# ", end="")
            print(word, end=" ")
            totallength = len(word) + 2
    print(" " * (lengthspace - (totallength)) + "#")

# Print text from a list, each element of the list is printed on a new line
def printTextFromList(List, Alinea = False):
    for line in List:
        printSentence(line, centered = False, Alinea = Alinea)
# Print a title 
def printTitle(sentence, centered = False):
    length = len(sentence) + 2
    if centered == False:
        print("# " + sentence + " " * (lengthspace - length) +" #")
    else:
        if length % 2 != 0:
            print("#" + " " * int((lengthspace - length)/2), sentence, " " * int((lengthspace - length)/2) + "#")
        else:
            print("#" + " " * int((lengthspace - length)/2), sentence, " " * int((lengthspace + 1 - length)/2) + "#")


# Input Text with or without verification and lenght limit

def inputText(textBefore= "", maxlenght = 500, verification = False, typeInput="text", Forbiden = [], FromList=[]):
    if typeInput == "title":
        Forbiden = ["@", "'", ".", ":", "\\", "%", "/", "!", "," ]
    Good = False
    while (not Good) or verification:
        ForbidenCharacters = True
        while ForbidenCharacters:
            print("# ", end="")
            response = input(textBefore + " ")
            for caracter in Forbiden:
                if caracter in response:
                    printSentence("Type " + caracter + " forbidden in this entry")
                    ForbidenCharacters = True
                    break
                ForbidenCharacters = False
            if len(Forbiden) == 0:
                ForbidenCharacters = False
            
        if len(response) < maxlenght:
            Good = True
        else:
            print("# Incorrect Response, the maximum lenght is", maxlenght)
        if verification and Good:
            responseVerification = input("# Please confirm : ")
            if responseVerification == response:
                verification = False
                printSentence("Success")
            else:
                printSentence("The inputs don't match, please retry.")
        if (response not in FromList) and (len(FromList) > 0):
            if response != "exit program":
                print("# Invalid, please retry. Enter \"exit program\" to go back.")
                Good = False
    return response


# Input a Number in or not in a given range:

def inputNumber(rangeNumber, textBefore = None):
    if textBefore == None:
        textBefore= "Enter an integer :"
    while True:
        try:
            number = int(inputText(textBefore= textBefore, verification = False))
            if rangeNumber != None:
                if number in rangeNumber:
                    return number
                else:
                    printSentence("This number is not valid.")
            else:
                return number
        except:
            printSentence("Please enter a valid integer.")



# Input a choice from a given list of choice :

def Choice(listeChoice):
    NbDeChoice = len(listeChoice)
    Choice = listeChoice
    if NbDeChoice > 15:
        print("Error -- Too much Choices")
        return 400
    def printChoices(FirstLine = False):
        paternes = {1:(1,), 2:(2,), 3:(3,), 4:(4,), 5:(3,2), 6:(3,3), 7:(4,3), 8:(4,4), 9:(3,3,3), 10:(4,3,3), 11:(4,4,3), 12:(4,4,4), 13:(4,4,3,2), 14:(4,4,3,3), 15:(4,4,4,3)}
        paterne = paternes[NbDeChoice]
        NbFait = 0
        if FirstLine:
            line()
        for row in paterne:
            numCase = 0
            print("#", end="")
            lengthCase = (lengthspace + 1 - row)/row
            for i in range(NbFait, row + NbFait):
                longueurMot = len(Choice[i]) + len(str(i)) + 2
                if longueurMot % 2 != 0:
                    Choice[i] = Choice[i] + " "
                    longueurMot += 1 
                NbEspace = lengthCase - longueurMot
                if row % 2 == 0:
                    numCase += 1
                    if ((row == 4) and (numCase == 2 or numCase == 3)) or row == 2:
                        if longueurMot % 2 == 0:
                            print(" " * int(NbEspace/2 + 1) + str(i) + ". " + Choice[i] + " " * int(NbEspace/2 - 1), end="#")
                        else:
                            print(" " * int(NbEspace/2) + str(i) + ". " + Choice[i] + " " * int(NbEspace/2 - 1), end="#")
                    else:
                        if longueurMot % 2 == 0:
                            print(" " * int(NbEspace/2 + 1) + str(i) + ". " + Choice[i] + " " * int(NbEspace/2), end="#")
                        else:
                            print(" " * int(NbEspace/2) + str(i) + ". " + Choice[i] + " " * int(NbEspace/2), end="#")
                else:
                    if longueurMot % 2 == 0:
                        print(" " * int(NbEspace/2 + 1) + str(i) + ". " + Choice[i] + " " * int(NbEspace/2), end="#")
                    else:
                        print(" " * int(NbEspace/2) + str(i) + ". " + Choice[i] + " " * int(NbEspace/2), end="#")
            NbFait += row
            print()
            line()
    printChoices()
    choice = inputNumber(rangeNumber = range(0,NbDeChoice))
    return choice
    
playerASCII= """
    &&&&&&&&&&&&%&&&&&&&&&&&&&&&                                                                                                                        
    &&/(((((((((((############&&                                                                                                                        
    &&/(((((((((/(############&&                                                                                                                        
    &&/((((((&&(((############&&         @@@@@@@@@ @@@@@@@@@@                                       @                                                   
    &&/((((((&***&&###########&&     @@@@@@@@@@@@  @@@@@@@@@@@@@        @@@@@@@@@@  @@@@           @@@    @@@@    @@@@@  @@@@@@@  @@@@@@@@@@@           
    &&/((((((&*******%&%######&&    @@@            @@@       @@@        @@@    @@@# @@@@          @@@@@@    @@@@ @@@@    @@@      @@@@    @@@           
    &&/((((((&**********/&&###&&   @@@        @@@  @@@@@@@@@@@@         @@@@@@@@@@  @@@@        @@@@ @@@@     @@@@@      @@@@@@@  @@@@@@@@@@@           
    &&/((((((&******%&%#######&&   @@@@       @@@  @@@      @@@@        @@@         @@@@       @@@@    @@@     @@@       @@@      @@@@ @@@@             
    &&/((((((&**%&############&&    @@@@      @@@  @@@       @@@        @@@         @@@@      @@@       @@@@   @@@       @@@      @@@@  @@@@            
    &&&((((((&((((###########&&&      @@@@@@@@@@@  @@@@@@@@@@@@         @@@         @@@@@@@@@@@@         @@@@  @@@       @@@@@@@  @@@     @@@@          
     &&&((((((((/(##########&&&                                                                                                                         
      %&&&((((((((########&&&&                                                                                                                          
         &&&&&((/(####&&%&&                                                                                                                             
             &&&&&&&&&&   
"""
editorASCII= """                                                                                                                                                                                       
         &&&                      &&&&                                                                                                                      
      &&.   *&&                #&%    (&%                                                                                                                   
    &&    &&*  &&            && &&(      &#                                                                                                                 
&&      & &%%%%%%%%%%%%%%%%%%%%%/ &&  #&&                                                                                                                  
   &&     &%&                 &      &&                                                                                                                     
     &&   &%&                 &   #&&      @@@@@@@@@@@  @@@@@@@@@@@@         @@@@@@@  @@@@@@@@      @@@  @@@@@@@@@@    @@@@@@@     @@@@@@@@@@               
        && &%%%%%%%%%%%%%%%%%%%%%&       @@@@.          @@@       @@@        @@@      @@@@  @@@@@   @@@     @@@     @@@@@  @@@@@   @@@@   @@@@              
          &//////////////////////%      @@@@            @@@      @@@@        @@@      @@@@    @@@@  @@@     @@@    @@@        @@@  @@@@   @@@@              
             &                 &/&      @@@.      @@@@ @@@@@@@@@@@@@/        @@@@@@   @@@@     @@@  @@@     @@@    @@@        @@@@ @@@@@@@@@@               
          #&&&&&&&&&&&&&&&&&&&&%/&       @@@#      @@@  @@@       @@@        @@@      @@@@   @@@@   @@@     @@@    @@@@      @@@@  @@@@  @@@#               
         &&&&&&&&&&&&&&&&&&&&&&&&/ &&     @@@@@@@@@@@@  @@@@@@@@@@@@@        @@@@@@@@ @@@@@@@@@     @@@     @@@      @@@@@@@@@@    @@@@   @@@@              
      #&% &%&%#################&%&&  &&       @@@@@     @@@@@@@@@@                                                                                          
    &&&   &%&                 &    *&%  &&                                                                                                                  
    &  ,&&%%%%%%%%%%%%%%%%%%%%%%%/&    &&                                                                                                                   
   &&     &&&&              &&       &&                                                                                                                     
  &&&&&&&&.                   *&& &&                                                                                                                        
                                 &                                                                                                                          
"""                                                                                                                                                                                          