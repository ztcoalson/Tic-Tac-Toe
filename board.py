from array import *
from player import *
from ai import *

class Game:
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = Player()
    ai = Ai()

    def player_turn(self):
        row, col = self.player.choice(self.board)
        self.board[row-1][col-1] = "X"

    def ai_turn(self):
        row, col = self.ai.choice(self.board)
        self.board[row-1][col-1] = "O"
        
    def check_win(self):
        pass

    def print_board(self):
        x = 0
        y = 0
        for i in self.board:
            for j in i:
                x += 1
                if x <= 2:
                    print(j, end="|")
                else:
                    print(j, end="\n")
            x = 0
            y += 1
            if y <= 2:
                print("-----")
                
