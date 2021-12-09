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
        self.grid = [[0,0,0],
                    [0,0,0],
                    [0,0,0]]

        self.player_1 = None
        self.player_2 = None


    def newGame(self) :
        if self.game_type == "1 joueur" :
            self.player_1 = Player(self)
            self.player_2 = Ia(self)

        elif self.game_type == "2 joueur" :
            self.player_1 = Player(self)
            self.player_2 = Player(self)

        self.actual_player = self.player_1
            
        return None

    def setGobletGrid(self, line, column, goblet) -> None:
        isValid = self.isValid(line, column, goblet)
        if isValid :
            self.grid[line][column] = goblet
            print(self.grid)
        else :
            result="test"
            print("Non valide !")


    def isValid(self, line, column, goblet) -> bool :
        result = goblet > self.grid[line][column]
        return result


    
    

    

    