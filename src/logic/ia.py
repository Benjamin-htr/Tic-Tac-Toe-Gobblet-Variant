from src.logic.Player import Player

class Ia (Player) :
    def __init__(self, gameCtrl, name : str, niveau : str) -> None :
        Player.__init__(self, gameCtrl, name)
        
        self.niveau = niveau



    def play(self) -> bool :
        print("Je suis une ia")
        return True

        