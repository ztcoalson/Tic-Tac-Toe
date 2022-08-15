from array import *
from msilib.schema import Billboard
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
        self.board[row][col] = "O"
        
    def check_win(self):
        for i in range(len(self.board)):
            x1 = x2 = o1 = o2 = 0
            for j in range(len(self.board[0])):
                if self.board[i][j] == 'X':
                    x1 += 1
                elif self.board[i][j] == 'O':
                    o1 += 1
                if self.board[j][i] == 'X':
                    x2 += 1
                elif self.board[j][i] == 'O':
                    o2 += 1
            if x1 == 3 or x2 == 3 or o1 == 3 or o2 == 3:
                return True
        diagonal1 = [self.board[0][0], self.board[1][1], self.board[2][2]]
        diagonal2 = [self.board[0][2], self.board[1][1], self.board[2][0]]
        if diagonal1 == ['X']*3 or diagonal1 == ['O']*3 or diagonal2 == ['X']*3 or diagonal2 == ['O']*3:
            return True
        return False
                


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
                
