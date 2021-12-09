class Player() :
    def __init__(self) -> None :
        #Nombre de gobelets restants :
        self.nbLittleGoblets = 2
        self.nbMediumBoblets = 3
        self.nbBigGoblets = 2

        #Gobelet sélectionné (1 : petit, 2 : moyen, 3 : grand) : 
        self.selectedGoblet = 2

    