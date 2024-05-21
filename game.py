
class Game():
    
    def __init__(self, nbPlayers):
        
        if nbPlayers > 5 or nbPlayers < 1:
            raise RuntimeError

        self.players = dict()
        
        for p in nbPlayers:
            self.players[p] = {}
            self.players
