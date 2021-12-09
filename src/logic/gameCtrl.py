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
        #Représente la grille de jeu :
        self.grid = [[0,0,0],
                    [0,0,0],
                    [0,0,0]]

        self.player_1 = None
        self.player_2 = None


    def newGame(self) :
        print(self.game_type)
        if self.game_type == "1 joueur" :
            self.player_1 = Player()
            self.player_2 = Ia()

        elif self.game_type == "2 joueur" :
            self.player_1 = Player()
            self.player_2 = Player()

        self.actual_player = self.player_1

            
        return None
