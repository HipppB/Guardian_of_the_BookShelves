

class Choix():
    def __init__(self, Number, ChoiceText, OutputScene, Object):
        self.Number = Number
        self.ChoiceText = ChoiceText
        self.OutputScene = OutputScene
        self.Object = Object


class Scene():
    def __init__(self, ID, Name, Description, MainText, ListeChoix):
        self.ID = ID
        self.Name = Name
        self.Description = Description
        self.MainText = MainText
        self.ListeChoix = ListeChoix

