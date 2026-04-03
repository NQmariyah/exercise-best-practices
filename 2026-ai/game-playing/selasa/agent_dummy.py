import random

class Agent:
    def __init__(self, player):
        self.player = player

    def choose_move(self, game):
        valid_moves = game.get_valid_moves()
        return random.choice(valid_moves)
