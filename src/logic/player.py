from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.logic.GameCtrl import GameCtrl

class Player() :
    def __init__(self, gameCtrl : GameCtrl, id : int) -> None :
        #Nombre de gobelets restants :
        self.id = id
        self.nbLittleGoblets = 2
        self.nbMediumGoblets = 3
        self.nbBigGoblets = 2

        #Représente la partie :
        self.gameCtrl = gameCtrl

        #Représente le gobelet sélectionné (1 : petit, 2 : moyen, 3 : grand) : 
        #vaut 2 par défaut 
        self.selectedGoblet = 2


    def selectGoblet(self, goblet_type : int) -> None :
        self.selectedGoblet = goblet_type
        print(self.selectedGoblet)

    def play(self, line : int, column : int) -> bool :
        #Si l'utilisateur essaie de jouer un gobelet qu'il n'a plus, on stoppe la fonction
        if self.getNbGoblets(self.selectedGoblet) <= 0 :
            return False

        if self.gameCtrl.setGobletGrid(line, column, self.selectedGoblet) :
            if self.selectedGoblet == 1 :
                self.nbLittleGoblets -= 1
            elif self.selectedGoblet == 2 :
                self.nbMediumGoblets -= 1
            elif self.selectedGoblet == 3 :
                self.nbBigGoblets -= 1
            return True

    def getNbGoblets(self, gobletSize : int) -> int :
        if gobletSize == 1 :
            result = self.nbLittleGoblets
        elif gobletSize == 2 :
            result = self.nbMediumGoblets
        elif gobletSize == 3 :
            result = self.nbBigGoblets

        return result
    

    