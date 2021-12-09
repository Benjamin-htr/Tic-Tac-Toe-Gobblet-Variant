from src.logic.configCtrl import configCtrl

class gameCtrl :
    def __init__(self) -> None :
        self.configCtrl = configCtrl()

        self.game_type = self.configCtrl.getGame_type()
        self.ia_level = self.configCtrl.getIa_level()

        self.grid = [[0,0,0],
                    [0,0,0],
                    [0,0,0]]



    