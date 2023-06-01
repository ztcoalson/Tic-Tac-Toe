from human import *
from ai import *

class Game:
    def __init__(self, p1 = Human("X", 1), p2 = Ai("O", 2)):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.p1 = p1
        self.p2 = p2

    def play(self, display_board=True):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        while not self.check_win():
            if display_board:
                self.print_board()
            self.player_turn(self.p1)
            if display_board:
                self.print_board()
            if not self.check_win():
                self.player_turn(self.p2)
        return self.check_win()

    def player_turn(self, p):
        row, col = p.choice(self.board)
        self.board[row][col] = p.number
        
    def check_win(self):
        # check rows and columns
        filled = 0
        for i in range(len(self.board)):
            x1 = x2 = o1 = o2 = 0
            for j in range(len(self.board[0])):
                if self.board[i][j] != 0:
                    filled += 1
                if self.board[i][j] == self.p1.number:
                    x1 += 1
                elif self.board[i][j] == self.p2.number:
                    o1 += 1
                if self.board[j][i] == self.p1.number:
                    x2 += 1
                elif self.board[j][i] == self.p2.number:
                    o2 += 1
            if x1 == 3 or x2 == 3:
                return self.p1.name
            elif o1 == 3 or o2 == 3:
                return self.p2.name
        
        # check diagonals
        diagonal1 = [self.board[0][0], self.board[1][1], self.board[2][2]]
        diagonal2 = [self.board[0][2], self.board[1][1], self.board[2][0]]
        if diagonal1 == [self.p1.number]*3 or diagonal2 == [self.p1.number]*3:
            return self.p1.name
        elif diagonal1 == [self.p2.number]*3 or diagonal2 == [self.p2.number]*3:
            return self.p2.name
        
        # check draw
        if filled == 9:
            return "draw"
        
        return None
                
    def print_board(self):
        x = y = 0
        map = {0: " ", self.p1.number: self.p1.icon, self.p2.number: self.p2.icon}
        for i in self.board:
            for j in i:
                if (x := x+1) <= 2:
                    print(map[j], end="|")
                else:
                    print(map[j], end="\n")
            x = 0
            if (y := y+1) <= 2:
                print("-----")
        print("======")
                
