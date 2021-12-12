from src.logic.ConfigCtrl import ConfigCtrl
from src.logic.Ia import Ia
from src.logic.Player import Player


class GameCtrl :
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

    def setGobletGrid(self, line : int, column : int, goblet : int) -> bool :
        isValid = self.isValid(line, column, goblet)
        if isValid :
            self.grid[line][column] = {"player" : self.actual_player, "goblet" : goblet}
        
        return isValid
    
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




    def isValid(self, line : int, column : int, goblet : int) -> bool :
        result = (goblet > self.grid[line][column]["goblet"])
        return result

    def isWin(self, player : Player) -> bool :
        #On parcourt les lignes :
        for i in range(len(self.grid)) :
            win = True
            for j in range(len(self.grid[i])) :
                if self.grid[i][j]["player"] != player :
                    win = False
                    break
            if win :
                return win

        #On parcourt les colonnes :
        for i in range(len(self.grid)) :
            win = True
            for j in range(len(self.grid[i])) :
                if self.grid[j][i]["player"] != player :
                    win = False
                    break
            if win :
                return win

        #On parcourt les diagonales
        win = True
        for i in range(len(self.grid)):
            if self.grid[i][i]["player"] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(len(self.grid)):
            if self.grid[i][len(self.grid) - 1 - i]["player"] != player:
                win = False
                break
        if win:
            return win
        return False
            


    def printGrid(self) -> None :
        for line in self.grid :
            print(line,"\n")


        

    

    
    

    

    