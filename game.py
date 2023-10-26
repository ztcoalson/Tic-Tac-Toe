from player import Player
from ai import AI

class Game:
    """Represents Game of Tic-Tac-Toe"""
    def __init__(self) -> None:
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.player = Player("X")
        self.ai = AI("O")

    def print_board(self):
        print("  1 2 3")
        for i, row in enumerate(self.board):
            line = f"{i+1} "
            for j, tile in enumerate(row):
                if j == 2:
                    line += tile
                else:
                    line += tile + "|"
            print(line)
            if i != 2:
                print("  -----")

    def turn(self):
        self.ai.make_move(self.board)
        # check for win
        self.player.make_move(self.board)
        # check for win