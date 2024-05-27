
class Game():
    
    def __init__(self, nbPlayers):
        self.nbPlayers = nbPlayers
        if nbPlayers > 5 or nbPlayers < 1:
            raise RuntimeError

        self.players = dict()
        
        for p in range(1, nbPlayers+1):
            self.players[p] = {"units": 0, "territories": 1, "capitals": 2, "cities": 3, "missions": 4}


    def __str__(self):
        return "Players : " + str(self.players)
