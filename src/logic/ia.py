from src.logic.Player import Player
import random

class Ia (Player) :
    def __init__(self, gameCtrl, name : str, niveau : str) -> None :
        Player.__init__(self, gameCtrl, name)
        
        #ATTRIBUTS :

        #Représente le niveau de l'IA (simple ou avancée) :
        self.niveau = niveau
        #Représente les gobelets de l'IA :
        self.gobletsList = [self.nbLittleGoblets, self.nbMediumGoblets, self.nbBigGoblets]

    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction de jeu de l'IA :
    #----------------------------------------------------------------------------------------------------------------------------------
    def play(self) -> bool :
        if self.niveau == "simple" :
            #L'IA récupère toutes les possibilités de jeux pour elle :
            validCases = self.getValidCases()
            #Elle en choisit une au hasard
            randomPlay = validCases[random.randint(0, len(validCases)-1)]
            #Sélectionne le plus petit gobelet nécessaire :
            self.selectGoblet(randomPlay["gobletToPlay"])
            #Puis le joue :
            return super().play(randomPlay["line"], randomPlay["column"])

        elif self.niveau == "avancee" :
            self.playAdvanced()
        
    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction IA simple (permet d'obtenir les cases vides et celles de l’adversaire qu’elle peut recouvrir d’un plus gros gobelet) :
    #----------------------------------------------------------------------------------------------------------------------------------
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

    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction IA Avancée de jeu (Définit l'ordre de priorité des critère de choix de jeu de l'IA avancée) :
    #----------------------------------------------------------------------------------------------------------------------------------
    def playAdvanced(self, debug = False) -> bool :
        validCases = self.getValidCases()
        winPossibles = self.getWinPossibles()
        alignPossibles = self.getAlignPossibles(validCases)
        centerPossibles =self.getCenterPossibles(validCases)
        cornerPossibles =self.getCornerPossibles(validCases)
        sidePossibles =self.getSidePossibles(validCases)

        if debug :
            print("\n\n\n--------------------------------\nTOUR DE LIA :\n")
            print("win possible :", winPossibles,"\n")
            print("align possible :", alignPossibles,"\n")
            print("center possible :", centerPossibles,"\n")
            print("corner possible :", cornerPossibles,"\n")
            print("cotés possible :", sidePossibles,"\n")
            print("validCases : ", validCases,"\n")

        typePlay = ""
        #L'IA joue le coup gagnant si c'est possible (en plaçant le plus petit pion nécessaire)
        if self.playLittlePossibilitie(winPossibles) :
            typePlay="playWin"
            return True
        #Sinon, si elle peut aligner des pions : :
        elif alignPossibles :
            #L'ia aligne ses pions en priorisant le centre si possible (en plaçant le plus petit pion nécessaire):
            if self.playLittlePossibilitie(self.getCenterPossibles(alignPossibles)) :
                typePlay="playAlignCenter"
                return True
            #Sinon, L'ia aligne ses pions en priorisant les coins si possible (en plaçant le plus petit pion nécessaire):
            elif self.playLittlePossibilitie(self.getCornerPossibles(alignPossibles)) : 
                typePlay="playAlignCorner"
                return True
            #Sinon, L'ia aligne ses pions en priorisant les cotés si possible (en plaçant le plus petit pion nécessaire):
            elif self.playLittlePossibilitie(self.getSidePossibles(alignPossibles)) : 
                typePlay="playAlignSide"
                return True
        #Sinon, L'ia joue au centre si possible (en plaçant le plus petit pion nécessaire):
        elif self.playLittlePossibilitie(centerPossibles) :
            typePlay="playCenter"
            return True
        #Sinon, L'ia joue dans les coins si possible (en plaçant le plus petit pion nécessaire):
        elif self.playLittlePossibilitie(cornerPossibles) :
            typePlay="playCorner"
            return True
        #Sinon, L'ia joue sur les cotés si possible (en plaçant le plus petit pion nécessaire):
        elif self.playLittlePossibilitie(sidePossibles) :
            typePlay="playSide"
            return True
        if debug : 
            print(typePlay)
            
        return False
            

    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction IA avancée (permet de jouer le plus petit pion parmi une liste de coup possibles)
    #----------------------------------------------------------------------------------------------------------------------------------
    def playLittlePossibilitie(self, possibilities : list) -> bool :
        self.gobletsList = [self.nbLittleGoblets, self.nbMediumGoblets, self.nbBigGoblets]
        #S'il la liste de possibs. n'est pas vide :
        if possibilities != [] :
            #Pour chaque gobelets :
            for g in range(len(self.gobletsList)) :
                #On parcourt les possibilités :
                for possibilitie in possibilities :
                    #Si ce gobelet est disponible et est plaçable, on le sélectionne, puis on le joue
                    if (self.gobletsList[g] > 0) and (g+1 >= possibilitie["gobletToPlay"]) :
                        self.selectGoblet(g+1)
                        if super().play(possibilitie["line"], possibilitie["column"]) :
                            return True
        return False

    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction IA avancée (Retourne un tableau donnant toutes les combinaisons gagnantes possibles actuellement) :
    #----------------------------------------------------------------------------------------------------------------------------------
    def getWinPossibles(self) -> list :
        winPossibles = []
        #On parcourt la grille de jeu de lignes en lignes :
        for i in range(len(self.gameCtrl.grid)) :
            nbOwnedCase = 0
            placeToWin = []
            for j in range(len(self.gameCtrl.grid[i])) :
                #Si la case appartient à l'ia, on incrémente le compteur de case lui appartenant sur la ligne
                if self.gameCtrl.grid[i][j]["player"] == self :
                    nbOwnedCase += 1
                #Si elle ne lui appartient pas, on enregistre cette case
                else :
                    placeToWin = {"line" : i, "column" : j, "gobletToPlay" : self.gameCtrl.grid[i][j]["goblet"]+1}
            #Si le nombre de case appartenant à l'ia est >= 2 sur la ligne, on ajoute le coup manquant pour gagner aux possibilités.
            if nbOwnedCase >= 2 :
                winPossibles.append(placeToWin)

        #On parcourt la grille de jeu de colonnes en colonnes :
        for i in range(len(self.gameCtrl.grid)) :
            nbOwnedCase = 0
            placeToWin = []
            for j in range(len(self.gameCtrl.grid[i])) :
                #Si la case appartient à l'ia, on incrémente le compteur de case lui appartenant sur la colonne
                if self.gameCtrl.grid[j][i]["player"] == self :
                    nbOwnedCase += 1
                #Si elle ne lui appartient pas, on enregistre cette case
                else :
                    placeToWin = {"line" : j, "column" : i, "gobletToPlay" : self.gameCtrl.grid[j][i]["goblet"]+1}
            #Si le nombre de case appartenant à l'ia est >= 2 sur la colonne, on ajoute le coup manquant pour gagner aux possibilités.
            if nbOwnedCase >= 2 :
                winPossibles.append(placeToWin)

        nbOwnedCase = 0
        #On parcourt la grille de jeu sur la diagonale descendante : 
        for i in range(len(self.gameCtrl.grid)):
            #Si la case appartient à l'ia, on incrémente le compteur de case lui appartenant sur la diagonale
            if self.gameCtrl.grid[i][i]["player"] == self:
                nbOwnedCase += 1
            #Si elle ne lui appartient pas, on enregistre cette case
            else :
                placeToWin = {"line" : i, "column" : i, "gobletToPlay" : self.gameCtrl.grid[i][i]["goblet"]+1}
        #Si le nombre de case appartenant à l'ia est >= 2 sur la diagonale,  on ajoute le coup manquant pour gagner aux possibilités.
        if nbOwnedCase >= 2 :
                winPossibles.append(placeToWin)

        nbOwnedCase = 0
        #On parcourt la grille de jeu sur la diagonale montante :
        for i in range(len(self.gameCtrl.grid)):
            #Si la case appartient à l'ia, on incrémente le compteur de case lui appartenant sur la diagonale 
            if self.gameCtrl.grid[i][len(self.gameCtrl.grid) - 1 - i]["player"] == self:
                nbOwnedCase += 1
            #Si elle ne lui appartient pas, on enregistre cette case
            else :
                placeToWin = {"line" : i, "column" : len(self.gameCtrl.grid) - 1 - i, "gobletToPlay" : self.gameCtrl.grid[i][len(self.gameCtrl.grid) - 1 - i]["goblet"]+1}
        #Si le nombre de case appartenant à l'ia est >= 2 sur la diagonale,  on ajoute le coup manquant pour gagner aux possibilités.
        if nbOwnedCase >= 2 :
                winPossibles.append(placeToWin)

        return winPossibles

    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction IA avancée (Donne les combinaisons permettant d'aligner les pions) :
    #----------------------------------------------------------------------------------------------------------------------------------
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
    
    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction IA avancée (Permet de savoir si deux cellules sont voisines) :
    #----------------------------------------------------------------------------------------------------------------------------------
    def isAttenante(self, lineA : int, columnA : int, lineB : int, columnB : int) -> bool :
        return (abs(lineA-lineB) <= 1) and (abs(columnA-columnB) <= 1)


    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction IA avancée (Permet de savoir si deux deux cellules sont alignés (d'après la logique du jeu)) :
    #----------------------------------------------------------------------------------------------------------------------------------
    def isAlign(self, lineA, columnA, lineB, columnB) -> bool :
        if self.isAttenante(lineA, columnA, lineB, columnB) :
            #Si les deux cases ne sont pas sur les cotés :
            if not(abs(lineA - columnA) == 1 and abs(lineB - columnB) == 1) :
                #Alors elles sont bien alignés :
                return True

        return False
    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction IA avancée (Donne les combinaison permettant de jouer dans le centre parmis une liste de possibilités) :
    #----------------------------------------------------------------------------------------------------------------------------------
    def getCenterPossibles(self, possiblePlays : list) -> list :
        centerPossible = []
        for possibilitie in possiblePlays :
            #Si la case est au centre
            if (possibilitie["line"] == 1 and possibilitie["column"] == 1) :
                centerPossible.append({"line" : possibilitie["line"], "column" : possibilitie["column"], "gobletToPlay" : possibilitie["gobletToPlay"]})
        
        return centerPossible

    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction IA avancée (Donne les combinaison permettant de jouer dans les coins parmis une liste de possibilités) :
    #----------------------------------------------------------------------------------------------------------------------------------
    def getCornerPossibles(self, possiblePlays : list) -> list :
        cornerPossibles = []
        for possibilitie in possiblePlays :
            #Si la case est dans les coins
            if (possibilitie["line"] + possibilitie["column"]) %2 == 0 and not(possibilitie["line"] == 1 and possibilitie["column"] == 1) :
                cornerPossibles.append({"line" : possibilitie["line"], "column" : possibilitie["column"], "gobletToPlay" : possibilitie["gobletToPlay"]})
        
        return cornerPossibles

    #---------------------------------------------------------------------------------------------------------------
    #Fonction IA avancée (Donne les combinaison permettant de jouer sur les cotés parmis une liste de possibilités) :
    #---------------------------------------------------------------------------------------------------------------
    def getSidePossibles(self, possiblePlays : list) -> list :
        sidePossibles = []
        for possibilitie in possiblePlays :
            #Si la case est sur les cotés :
            if abs(possibilitie["line"] - possibilitie["column"]) == 1 :
                sidePossibles.append({"line" : possibilitie["line"], "column" : possibilitie["column"], "gobletToPlay" : possibilitie["gobletToPlay"]})
        
        return sidePossibles

    


    