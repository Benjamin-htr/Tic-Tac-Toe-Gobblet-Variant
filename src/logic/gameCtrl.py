from src.logic.ConfigCtrl import ConfigCtrl
from src.logic.Ia import Ia
from src.logic.Player import Player

#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
#Classe représentant la logique d'une partie de jeu :
#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
class GameCtrl :
    #----------------------------------------------------------------------------------------------------------------------------------
    #Constructeur :
    #----------------------------------------------------------------------------------------------------------------------------------
    def __init__(self) -> None :
        self.configCtrl = ConfigCtrl()

        #ATTRIBUTS :

        #Type de jeu (1 ou 2 joueurs) :
        self.game_type = self.configCtrl.getGame_type()
        #Mode de l'IA (simple ou avancee) :
        self.ia_level = self.configCtrl.getIa_level()
        #Représente le joueur qui doit jouer ce tour :
        self.actual_player = None
        #Représente la grille générale du jeu (les gobelets des deux joueurs):
        self.grid = [[{"player" : None, "goblet" : 0},{"player" : None, "goblet" : 0},{"player" : None, "goblet" : 0}],
                    [{"player" : None, "goblet" : 0},{"player" : None, "goblet" : 0},{"player" : None, "goblet" : 0}],
                    [{"player" : None, "goblet" : 0},{"player" : None, "goblet" : 0},{"player" : None, "goblet" : 0}]]
        #Représente le joueur 1 :
        self.player_1 = None
        #Représente le joueur 2 (joueur humain ou ia) :
        self.player_2 = None

    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction lançant une nouvelle partie de jeu :
    #----------------------------------------------------------------------------------------------------------------------------------
    def newGame(self) :
        print("New Game !")
        #Si le mode de jeu est 1 joueur, on ajoute un joueur et une ia à la partie:
        if self.game_type == "1 joueur" :
            self.player_1 = Player(self, 1)
            self.player_2 = Ia(self, 2, self.ia_level)

        #Sinon, si le mode de jeu est 2 joueurs, on ajoute 2 joueurs à la partie:
        elif self.game_type == "2 joueurs" :
            self.player_1 = Player(self, 1)
            self.player_2 = Player(self, 2)

        #Le joueur 1 joue le premier :
        self.actual_player = self.player_1
            
        return None

    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction permettant de placer un gobelet sur la grille :
    #----------------------------------------------------------------------------------------------------------------------------------
    def setGobletGrid(self, line : int, column : int, goblet : int) -> bool :
        isValid = self.isValid(line, column, goblet)
        #Si le placement est valide
        if isValid :
            #On met à jour la grille
            self.grid[line][column] = {"player" : self.actual_player, "goblet" : goblet}
        
        return isValid
    
    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction permettant de passer au tour suivant :
    #----------------------------------------------------------------------------------------------------------------------------------
    def nextTurn(self) -> None :
        if self.actual_player == self.player_1 :
            self.actual_player = self.player_2
            #Si je joue face à une ia :
            if self.game_type == "1 joueur" :
                #Celle-ci joue automatiquement
                self.actual_player.play()
                #Puis passe son tour
                self.nextTurn()
        elif self.actual_player == self.player_2 :
            self.actual_player = self.player_1

    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction permettant de vérifier si le placement d'un certain gobelet dans la grille est valide:
    #----------------------------------------------------------------------------------------------------------------------------------
    def isValid(self, line : int, column : int, goblet : int) -> bool :
        result = (goblet > self.grid[line][column]["goblet"])
        return result

    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction permettant de vérifier si le joueur passé en paramètre est gagnant :
    #----------------------------------------------------------------------------------------------------------------------------------
    def isWin(self, player : Player) -> bool :
        #On parcourt la grille de ligne en ligne :
        for i in range(len(self.grid)) :
            win = True
            for j in range(len(self.grid[i])) :
                #Si la case n'appartient pas au joueur
                if self.grid[i][j]["player"] != player :
                    #Alors cette ligne n'est pas une combinaison gagnante
                    win = False
                    break
            #Si cette ligne est une combinaison gagnante, alors le joueur est gagnant
            if win :
                return win

        #On parcourt la grille de colonne en colonne :
        for i in range(len(self.grid)) :
            win = True
            for j in range(len(self.grid[i])) :
                #Si la case n'appartient pas au joueur
                if self.grid[j][i]["player"] != player :
                    #Alors cette colonne n'est pas une combinaison gagnante
                    win = False
                    break
            #Si cette colonne est une combinaison gagnante, alors le joueur est gagnant
            if win :
                return win

        win = True
        #On parcourt la grille sur la diagonale descendante :
        for i in range(len(self.grid)):
            #Si la case n'appartient pas au joueur
            if self.grid[i][i]["player"] != player :
                #Alors cette diagonale n'est pas une combinaison gagnante
                win = False
                break
        #Si cette diagonale est une combinaison gagnante, alors le joueur est gagnant
        if win:
            return win

        win = True
        #On parcourt la grille sur la diagonale montante :
        for i in range(len(self.grid)):
            if self.grid[i][len(self.grid) - 1 - i]["player"] != player:
                #Si la case n'appartient pas au joueur
                win = False
                break
        #Si cette diagonale est une combinaison gagnante, alors le joueur est gagnant
        if win:
            return win
        return False
            
    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction de DEBUG (affiche la grille) :
    #----------------------------------------------------------------------------------------------------------------------------------
    def printGrid(self) -> None :
        for line in self.grid :
            print(line,"\n")


        

    

    
    

    

    