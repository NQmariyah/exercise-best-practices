from agent import Agent as Agent1
from agent_dummy import Agent as Agent2


class NimGame:
    def __init__(self, piles=None):
        if piles is None:
            self.piles = [3, 4, 5]
        else:
            self.piles = piles

    def print_state(self):
        print("Piles:", self.piles)

    def get_valid_moves(self):
        moves = []
        for i, pile in enumerate(self.piles):
            for amount in range(1, pile + 1):
                moves.append((i, amount))
        return moves

    def make_move(self, move):
        pile_index, amount = move
        self.piles[pile_index] -= amount

    def is_game_over(self):
        return all(p == 0 for p in self.piles)


def play_game(agent1, agent2, show_state=True):
    game = NimGame()
    current = agent1

    while True:
        if show_state:
            game.print_state()

        move = current.choose_move(game)

        if move not in game.get_valid_moves():
            print(f"Invalid move by {current.player}. Lose!")
            break

        game.make_move(move)

        if game.is_game_over():
            print(f"Player {current.player} wins!")
            break

        current = agent2 if current == agent1 else agent1


if __name__ == "__main__":
    agent1 = Agent1('A')
    agent2 = Agent2('B')

    play_game(agent1, agent2)
