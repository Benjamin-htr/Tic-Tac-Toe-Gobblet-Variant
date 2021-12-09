from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.logic.GameCtrl import GameCtrl

class Player() :
    def __init__(self, gameCtrl : GameCtrl) -> None :
        #Nombre de gobelets restants :
        self.nbLittleGoblets = 2
        self.nbMediumBoblets = 3
        self.nbBigGoblets = 2

        #Représente la partie :
        self.gameCtrl = gameCtrl

        #Représente la grille spécifique du joueur (avec seulement ses gobelets) :
        self.grid = [[0,0,0],
                    [0,0,0],
                    [0,0,0]]

        #Représente le gobelet sélectionné (1 : petit, 2 : moyen, 3 : grand) : 
        #vaut 2 par défaut 
        self.selectedGoblet = 2


    def selectGoblet(self, goblet_type : int) -> None :
        self.selectedGoblet = goblet_type
        print(self.selectedGoblet)

    def play(self, line : int, column : int) -> None :
        print("case select : ", line, column)
        isValid = self.gameCtrl.isValid(line, column, self.selectedGoblet)
        if isValid :
            self.gameCtrl.setGobletGrid(line, column, self.selectedGoblet)

        return isValid

    

    