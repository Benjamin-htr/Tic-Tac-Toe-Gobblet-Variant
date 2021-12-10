from src.logic.Player import Player

class Ia (Player) :
    def __init__(self, gameCtrl, name : str) -> None :
        Player.__init__(self, gameCtrl, name)

        