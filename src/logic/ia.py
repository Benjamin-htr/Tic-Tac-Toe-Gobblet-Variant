from src.logic.Player import Player
import random

class Ia (Player) :
    def __init__(self, gameCtrl, name : str, niveau : str) -> None :
        Player.__init__(self, gameCtrl, name)
        
        self.niveau = niveau
        self.gobletsList = [self.nbLittleGoblets, self.nbMediumGoblets, self.nbBigGoblets]


    def play(self) -> bool :
        print("Je suis une ia "+self.niveau)
        if self.niveau == "simple" :
            validCases = self.getValidCases()
            print("\n\n\n--------------------------------\nTOUR DE LIA :\n")
            print("win possible :", self.getWinPossibles(),"\n")
            print("align possible :", self.getAlignPossibles(validCases),"\n")
            print("center possible :", self.getCenterPossibles(validCases),"\n")
            print("corner possible :", self.getCornerPossibles(validCases),"\n")
            print("cotés possible :", self.getSidePossibles(validCases),"\n")
            print("validCases : ", validCases,"\n")
            randomPlay = validCases[random.randint(0, len(validCases)-1)]
            self.selectedGoblet = randomPlay["gobletToPlay"]
            return super().play(randomPlay["line"], randomPlay["column"])

        elif self.niveau == "avancee" :
            pass

        

    #Fonction IA simple (permet d'obtenir les cases vides et celles de l’adversaire qu’elle peut recouvrir d’un plus gros gobelet) :
    def getValidCases(self) -> list :
        self.gobletsList = [self.nbLittleGoblets, self.nbMediumGoblets, self.nbBigGoblets]
        validCases = []
        #On parcourt la grille :
        for line in range(len(self.gameCtrl.grid)) :
            for column in range(len(self.gameCtrl.grid[line])) :
                #Pour chaque gobelets :
                for g in range (len(self.gobletsList)) :
                    #S'il lui en reste
                    if self.gobletsList[g] > 0 :
                        #On regarde si elle peut recouvrir la case (ou le gobelet de l'adv)
                        if self.gameCtrl.isValid(line, column, g+1) :
                            #puis on l'ajoute + sort de la boucle pour rester sur le gobelet minimum nécessaire
                            validCases.append({"line":line, "column":column, "gobletToPlay":g+1})
                            break

        return validCases

    #Fonction IA avancée (Joue le coup gagnant s'il y en a) :
    def playCoupGagnant(self) -> bool :
        """ winPossiblesPlays = self.winPossibles()
        self.gobletsList = [self.nbLittleGoblets, self.nbMediumGoblets, self.nbBigGoblets]
        if winPossiblesPlays != [] :
            for winPlay in winPossiblesPlays :
                for g in range(len(self.gobletsList)) :
                    if self.gobletsList[g] > 0 and g+1 >= winPlay["goblet"] :
                        self.selectedGoblet = winPlay["goblet"]
                        super().play(winPlay["line"], winPlay["column"])
                        return True

        return False """
        return self.playLittlePossibilitie(self.getWinPossibles())

    #Fonction permettant de jouer le plus petit pion parmis une liste de coup possibles
    def playLittlePossibilitie(self, possibilities : list) -> bool :
        self.gobletsList = [self.nbLittleGoblets, self.nbMediumGoblets, self.nbBigGoblets]
        if possibilities != [] :
            for g in range(len(self.gobletsList)) :
                for winPlay in possibilities :
                    if self.gobletsList[g] > 0 and g+1 >= possibilities["goblet"] :
                        self.selectedGoblet = possibilities["goblet"]
                        super().play(possibilities["line"], possibilities["column"])
                        return True
        return False




    #Fonction IA avancée (Retourne un tableau donnant toutes les combinaisons gagnantes possibles actuellement) :
    def getWinPossibles(self) -> list :
        winPossibles = []
        #On parcourt les lignes :
        for i in range(len(self.gameCtrl.grid)) :
            nbOwnedCase = 0
            placeToWin = []
            for j in range(len(self.gameCtrl.grid[i])) :
                if self.gameCtrl.grid[i][j]["player"] == self :
                    nbOwnedCase += 1
                else :
                    placeToWin = {"line" : i, "column" : j, "gobletToPlay" : self.gameCtrl.grid[i][j]["goblet"]+1}
            
            if nbOwnedCase >= 2 :
                winPossibles.append(placeToWin)

        #On parcourt les colonnes :
        for i in range(len(self.gameCtrl.grid)) :
            nbOwnedCase = 0
            placeToWin = []
            for j in range(len(self.gameCtrl.grid[i])) :
                if self.gameCtrl.grid[j][i]["player"] == self :
                    nbOwnedCase += 1
                else :
                    placeToWin = {"line" : j, "column" : i, "gobletToPlay" : self.gameCtrl.grid[j][i]["goblet"]+1}
                    
            if nbOwnedCase >= 2 :
                winPossibles.append(placeToWin)

        #On parcourt les diagonales
        nbOwnedCase = 0
        for i in range(len(self.gameCtrl.grid)):
            if self.gameCtrl.grid[i][i]["player"] == self:
                nbOwnedCase += 1
            else :
                placeToWin = {"line" : i, "column" : i, "gobletToPlay" : self.gameCtrl.grid[i][i]["goblet"]+1}
        if nbOwnedCase >= 2 :
                winPossibles.append(placeToWin)

        nbOwnedCase = 0
        for i in range(len(self.gameCtrl.grid)):
            if self.gameCtrl.grid[i][len(self.gameCtrl.grid) - 1 - i]["player"] == self:
                nbOwnedCase += 1
            else :
                placeToWin = {"line" : i, "column" : len(self.gameCtrl.grid) - 1 - i, "gobletToPlay" : self.gameCtrl.grid[i][len(self.gameCtrl.grid) - 1 - i]["goblet"]+1}
        if nbOwnedCase >= 2 :
                winPossibles.append(placeToWin)

        return winPossibles

    def playAlign(self) -> bool :
        pass

    #Fonction IA avancée (Donne les combinaison permettant d'aligner les pions) :
    def getAlignPossibles(self, possiblePlays : list) -> list :
        alignPossible = []
        #Pour chaque case de la grille :
        for line in range(len(self.gameCtrl.grid)) :
            for column in range(len(self.gameCtrl.grid[line])) :
                #Si elle appartient à l'ia :
                if self.gameCtrl.grid[line][column]["player"] == self :
                    #On parcours toutes les possibilités de jeux possibles données en paramètre :
                    for possibilitie in possiblePlays :
                        lineB = possibilitie["line"]
                        columnB = possibilitie["column"]
                        #Si cette possib. n'appartient pas déjà au joueur et si elle n'est pas déjà présente dans les possibilités d'alignement :
                        if self.gameCtrl.grid[lineB][columnB]["player"] != self and {"line" : lineB, "column" : columnB, "gobletToPlay" : possibilitie["gobletToPlay"]} not in alignPossible :
                            #Et si elle est bien alignée et qu'il possède le bon pion :
                            if self.isAlign(line, column, lineB, columnB) and possibilitie["gobletToPlay"] > 0 and not(line == lineB and column == columnB) :
                                alignPossible.append({"line" : lineB, "column" : columnB, "gobletToPlay" : possibilitie["gobletToPlay"]})

        return alignPossible
    
    #Permet de savoir si deux cellules sont voisines :
    def isAttenante(self, lineA : int, columnA : int, lineB : int, columnB : int) -> bool :
        return (abs(lineA-lineB) <= 1) and (abs(columnA-columnB) <= 1)

    #Permet de savoir si deux deux cellules sont alignés (d'après la logique du jeu) :
    def isAlign(self, lineA, columnA, lineB, columnB) -> bool :
        if self.isAttenante(lineA, columnA, lineB, columnB) :
            #Si les deux cases ne sont pas sur les cotés :
            if not(abs(lineA - columnA) == 1 and abs(lineB - columnB) == 1) :
                #Alors elles sont bien alignés :
                return True

        return False
    
    #Fonction IA avancée (Donne les combinaison permettant de jouer dans le centre parmis une liste de possibilités) :
    def getCenterPossibles(self, possiblePlays : list) -> list :
        centerPossible = []
        for possibilitie in possiblePlays :
            #Si la case est au centre
            if (possibilitie["line"] == 1 and possibilitie["column"] == 1) :
                centerPossible.append({"line" : possibilitie["line"], "column" : possibilitie["column"], "gobletToPlay" : possibilitie["gobletToPlay"]})
        
        return centerPossible

    #Fonction IA avancée (Donne les combinaison permettant de jouer dans les coins parmis une liste de possibilités) :
    def getCornerPossibles(self, possiblePlays : list) -> list :
        cornerPossibles = []
        for possibilitie in possiblePlays :
            #Si la case est dans les coins
            if (possibilitie["line"] + possibilitie["column"]) %2 == 0 and not(possibilitie["line"] == 1 and possibilitie["column"] == 1) :
                cornerPossibles.append({"line" : possibilitie["line"], "column" : possibilitie["column"], "gobletToPlay" : possibilitie["gobletToPlay"]})
        
        return cornerPossibles

    #Fonction IA avancée (Donne les combinaison permettant de jouer sur les cotés parmis une liste de possibilités) :
    def getSidePossibles(self, possiblePlays : list) -> list :
        sidePossibles = []
        for possibilitie in possiblePlays :
            #Si la case est sur les cotés :
            if abs(possibilitie["line"] - possibilitie["column"]) == 1 :
                sidePossibles.append({"line" : possibilitie["line"], "column" : possibilitie["column"], "gobletToPlay" : possibilitie["gobletToPlay"]})
        
        return sidePossibles

    


    