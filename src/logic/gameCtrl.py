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
            self.player_2 = Ia(self, 2)

        elif self.game_type == "2 joueurs" :
            self.player_1 = Player(self, 1)
            self.player_2 = Player(self, 2)

        print(self.player_1)
        self.actual_player = self.player_2
        print(self.actual_player)
            
        return None

    def setGobletGrid(self, line : int, column : int, goblet : int) -> bool :
        isValid = self.isValid(line, column, goblet)
        if isValid :
            self.grid[line][column] = {"player" : self.actual_player, "goblet" : goblet}
            print(self.grid)
        
        return isValid
        

    def isValid(self, line : int, column : int, goblet : int) -> bool :
        result = (goblet > self.grid[line][column]["goblet"])
        return result
        

    

    
    

    

    