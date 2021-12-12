from configparser import ConfigParser
import os

#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
#Classe représentant la logique des options :
#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
class ConfigCtrl() :
    #----------------------------------------------------------------------------------------------------------------------------------
    #Constructeur :
    #----------------------------------------------------------------------------------------------------------------------------------
    def __init__(self) -> None :
        #Objet permettant de manipuler plus facilement le fichier de config :
        self.config = ConfigParser()

        #ATTRIBUTS :

        #Représente le type de jeu (1 joueur ou 2 joueurs) :
        self.game_type = "1 joueur"
        #Représente le niveau de l'IA (simple ou avancee) :
        self.ia_level = "simple"

        #Créer le fichier de configuration s'il n'existe pas déjà :
        if not os.path.exists('config.ini') :
            self.updateConfig()
   
    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction permettant d'écrire le fichier de config :
    #----------------------------------------------------------------------------------------------------------------------------------
    def write_file(self) :
        self.config.write(open('config.ini', 'w'))

    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction permettant de mettre à jour le fichier de config :
    #----------------------------------------------------------------------------------------------------------------------------------
    def updateConfig(self, game_type : str = "1 joueur", ia_level: str = "simple") :
        self.game_type = game_type
        self.ia_level = ia_level

        self.config['USER'] = {'game_type': self.game_type, 'ia_level': self.ia_level}
        self.write_file()

    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction permettant de retourner le type de jeu (1 joueur ou 2 joueurs) :
    #----------------------------------------------------------------------------------------------------------------------------------
    def getGame_type(self) -> str :
        self.config.read('config.ini')
        result = self.config.get('USER', 'game_type')
        
        return result

    #----------------------------------------------------------------------------------------------------------------------------------
    #Fonction permettant de retourner le niveau de l'IA (simple ou avancee) :
    #----------------------------------------------------------------------------------------------------------------------------------
    def getIa_level(self) -> str :
        self.config.read('config.ini')
        result = self.config.get('USER', 'ia_level')
        return result