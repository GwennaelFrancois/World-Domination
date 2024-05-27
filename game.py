from .toolbox import rollDice

class Game():
    
    def __init__(self, nbPlayers):
        self.nbPlayers = nbPlayers
        self.turns = []
        self.turn = 0
        if nbPlayers > 5 or nbPlayers < 1:
            raise RuntimeError

        self.players = dict()
        
        for p in range(1, nbPlayers+1):
            self.players[p] = {"units": 0, "territories": 1, "capitals": 2, "cities": 3, "missions": 4}

    def __str__(self):
        return "Players : " + str(self.players)

    def drawTurns(self):
        """Draw turns of players

        :param nbPlayers: number of players in the game
        :type nbPlayers: int
        :return: ordered list of players ex : [3, 4, 1, 2, 5]
        :rtype: list
        """
        players = [p+1 for p in range(self.nbPlayers)]
        dices = [rollDice() for _ in players]

        # @todo do smthg for the draws
        for _ in range(self.nbPlayers):
            index = dices.index(max(dices))
            dices.pop(index)
            self.turns.append(players.pop(index))
    
    def endTurn(self) -> bool:
        """End current turn and start next one.
        Check if someone won the game
        :return: If someone won the game
        :rtype: bool
        """
        self.turn += 1
        if self.turn == len(self.turns): self.turn = 0

        return False #@todo
