from configparser import ConfigParser
import os

class configCtrl() :
    def __init__(self) -> None :

        #attributes :
        self.config = ConfigParser()
        self.game_type = "1 joueur"
        self.ia_level = "simple"

        #create config file if not exist :
        if not os.path.exists('config.ini') :
            self.updateConfig()
   
    def write_file(self):
        self.config.write(open('config.ini', 'w'))


    def updateConfig(self, game_type : str = "1 joueur", ia_level: str = "simple") :
        self.game_type = game_type
        self.ia_level = ia_level

        self.config['USER'] = {'game_type': self.game_type, 'ia_level': self.ia_level}
        self.write_file()


    def getGame_type(self) -> str :
        self.config.read('config.ini')
        result = self.config.get('USER', 'game_type')
        
        return result

    def getIa_level(self) -> str :
        self.config.read('config.ini')
        result = self.config.get('USER', 'ia_level')
        return result