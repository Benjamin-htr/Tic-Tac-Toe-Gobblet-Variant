from src.logic.Player import Player
import random

class Ia (Player) :
    def __init__(self, gameCtrl, name : str, niveau : str) -> None :
        Player.__init__(self, gameCtrl, name)
        
        self.niveau = niveau


    def play(self) -> bool :
        print("Je suis une ia "+self.niveau)
        if self.niveau == "simple" :
            validCases = self.getValidCases()
            randomPlay = validCases[random.randint(0, len(validCases)-1)]
            self.selectedGoblet = randomPlay["goblet"]
            super().play(randomPlay["line"], randomPlay["column"])
    
            return True

    #Fonction IA simple (permet d'obtenir les cases vides et celles de l’adversaire qu’elle peut recouvrir d’un plus gros gobelet) :
    def getValidCases(self) -> list :
        gobletsList = [self.nbLittleGoblets, self.nbMediumGoblets, self.nbBigGoblets]
        validCases = []
        #On parcourt la grille :
        for line in range(len(self.gameCtrl.grid)) :
            for column in range(len(self.gameCtrl.grid[line])) :
                #Pour chaque gobelets :
                for g in range (len(gobletsList)) :
                    #S'il lui en reste
                    if gobletsList[g] > 0 :
                        #On regarde si elle peut recouvrir la case (ou le gobelet de l'adv)
                        if self.gameCtrl.isValid(line, column, g+1) :
                            #puis on l'ajoute + sort de la boucle pour rester sur le gobelet minimum nécessaire
                            validCases.append({"line":line, "column":column, "goblet":g+1})
                            break

        return validCases





    

        