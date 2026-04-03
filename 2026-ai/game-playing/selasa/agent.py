class Agent:
    def __init__(self, player):
        self.player = player

    def choose_move(self, game):
        """
        Implementasikan strategi Anda di sini.

        Parameter:
        - game: object Connect4

        Return:
        - kolom (int)
        """
        valid_moves = game.get_valid_moves()

        # TODO: ganti dengan strategi Anda
        return valid_moves[0]
