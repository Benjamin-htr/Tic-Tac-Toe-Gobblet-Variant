from src.logic.ConfigCtrl import ConfigCtrl
from src.logic.Ia import Ia
from src.logic.Player import Player


class GameCtrl :
    def __init__(self) -> None :
        self.configCtrl = ConfigCtrl()

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

        self.player_1 = None
        self.player_2 = None


    def newGame(self) :
        print("New Game !")
        if self.game_type == "1 joueur" :
            self.player_1 = Player(self, 1)
            self.player_2 = Ia(self, 2, self.ia_level)

        elif self.game_type == "2 joueurs" :
            self.player_1 = Player(self, 1)
            self.player_2 = Player(self, 2)

        print(self.player_1)
        self.actual_player = self.player_1
        print(self.actual_player)
            
        return None

    def setGobletGrid(self, line : int, column : int, goblet : int) -> bool :
        isValid = self.isValid(line, column, goblet)
        if isValid :
            self.grid[line][column] = {"player" : self.actual_player, "goblet" : goblet}
            print(self.grid)
        
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
            





        

    

    
    

    

    