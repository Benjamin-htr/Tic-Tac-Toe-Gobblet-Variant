#Permet l'import de GamCtrl pour le type hinting sans créer de problème d'import cyclique :
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.logic.GameCtrl import GameCtrl

#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
#Classe représentant la logique d'un joueur :
#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
class Player() :
    #----------------------------------------------------------------------------------------------------------------------------------
    #Constructeur :
    #----------------------------------------------------------------------------------------------------------------------------------
    def __init__(self, gameCtrl : GameCtrl, id : int) -> None :
        #ATTRIBUTS :

        #Identifiant du joueur (1 ou 2 en principe)
        self.id = id
        #Nombre de petits gobelets restants :
        self.nbLittleGoblets = 2
        #Nombre de gobelets moyens restants :
        self.nbMediumGoblets = 3
        #Nombre de grands gobelets restants :
        self.nbBigGoblets = 2
        #Représente la partie :
        self.gameCtrl = gameCtrl
        #Représente le gobelet sélectionné (1 : petit, 2 : moyen, 3 : grand) :  
        self.selectedGoblet = 2

    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction permettant de sélectionner un gobelet :
    #----------------------------------------------------------------------------------------------------------------------------------
    def selectGoblet(self, goblet_type : int) -> None :
        self.selectedGoblet = goblet_type
        print("Joueur "+str(self.id)+" : gobelet select : ",self.selectedGoblet)

    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction permettant de jouer un coup :
    #----------------------------------------------------------------------------------------------------------------------------------
    def play(self, line : int, column : int) -> bool :
        #Si l'utilisateur essaie de jouer un gobelet qu'il n'a plus, on stoppe la fonction
        if self.getNbGoblets(self.selectedGoblet) <= 0 :
            return False

        #Si le gobelet a bien été placé sur a grille, on met à jour le nombre de gobelet :
        if self.gameCtrl.setGobletGrid(line, column, self.selectedGoblet) :
            if self.selectedGoblet == 1 :
                self.nbLittleGoblets -= 1
            elif self.selectedGoblet == 2 :
                self.nbMediumGoblets -= 1
            elif self.selectedGoblet == 3 :
                self.nbBigGoblets -= 1
            return True

    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction permettant de retourner le nombre restant du type de gobelet entré paramètre :
    #----------------------------------------------------------------------------------------------------------------------------------
    def getNbGoblets(self, gobletSize : int) -> int :
        if gobletSize == 1 :
            result = self.nbLittleGoblets
        elif gobletSize == 2 :
            result = self.nbMediumGoblets
        elif gobletSize == 3 :
            result = self.nbBigGoblets

        return result
    

    