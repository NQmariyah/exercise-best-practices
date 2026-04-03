from agent import Agent as Agent1
from agent_dummy import Agent as Agent2

ROWS = 4
COLS = 4


class Connect4:
    def __init__(self):
        self.board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
        print('-' * (COLS * 2 - 1))

    def get_valid_moves(self):
        return [c for c in range(COLS) if self.board[0][c] == ' ']

    def make_move(self, col, player):
        for row in reversed(range(ROWS)):
            if self.board[row][col] == ' ':
                self.board[row][col] = player
                return True
        return False

    def check_winner(self, player):
        # Horizontal
        for r in range(ROWS):
            for c in range(COLS - 3):
                if all(self.board[r][c + i] == player for i in range(4)):
                    return True

        # Vertical
        for c in range(COLS):
            for r in range(ROWS - 3):
                if all(self.board[r + i][c] == player for i in range(4)):
                    return True

        # Diagonal /
        for r in range(ROWS - 3):
            for c in range(COLS - 3):
                if all(self.board[r + i][c + i] == player for i in range(4)):
                    return True

        # Diagonal \
        for r in range(3, ROWS):
            for c in range(COLS - 3):
                if all(self.board[r - i][c + i] == player for i in range(4)):
                    return True

        return False

    def is_full(self):
        return all(self.board[0][c] != ' ' for c in range(COLS))


def play_game(agent1, agent2, show_board=True):
    game = Connect4()
    current = agent1

    while True:
        if show_board:
            game.print_board()

        move = current.choose_move(game)

        if move not in game.get_valid_moves():
            print(f"Invalid move by {current.player}. Lose!")
            break

        game.make_move(move, current.player)

        if game.check_winner(current.player):
            game.print_board()
            print(f"Player {current.player} wins!")
            break

        if game.is_full():
            game.print_board()
            print("Draw!")
            break

        current = agent2 if current == agent1 else agent1


if __name__ == "__main__":
    agent1 = Agent1('X')
    agent2 = Agent2('O')

    play_game(agent1, agent2)
