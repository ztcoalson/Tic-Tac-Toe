from array import *
from msilib.schema import Billboard
from human import *
from ai import *

class Game:
    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def play(self, p1, p2):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        while not self.check_win(p1, p2):
            self.player_turn(p1)
            if self.check_win(p1, p2):
                return self.check_win(p1, p2)
            self.player_turn(p2)
        return self.check_win(p1, p2)

    def player_turn(self, p):
        row, col = p.choice(self.board)
        self.board[row][col] = p.icon
        
    def check_win(self, p1, p2):
        filled = 0
        for i in range(len(self.board)):
            x1 = x2 = o1 = o2 = 0
            for j in range(len(self.board[0])):
                if self.board[i][j] != " ":
                    filled += 1
                if self.board[i][j] == p1.icon:
                    x1 += 1
                elif self.board[i][j] == p2.icon:
                    o1 += 1
                if self.board[j][i] == p1.icon:
                    x2 += 1
                elif self.board[j][i] == p2.icon:
                    o2 += 1
            if x1 == 3 or x2 == 3:
                return p1.name
            elif o1 == 3 or o2 == 3:
                return p2.name
        if filled == 9:
            return "draw"
        diagonal1 = [self.board[0][0], self.board[1][1], self.board[2][2]]
        diagonal2 = [self.board[0][2], self.board[1][1], self.board[2][0]]
        if diagonal1 == [p1.icon]*3 or diagonal2 == [p1.icon]*3:
            return p1.name
        elif diagonal1 == [p2.icon]*3 or diagonal2 == [p2.icon]*3:
            return p2.name
        return None
                
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
        print("======")
                
