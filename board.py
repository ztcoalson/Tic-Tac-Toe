from array import *
from player import *

class Game:
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = Player()

    def player_turn(self):
        self.player.choice()
        if(self.player.move == "12"):
            print("works")
            self.board = [["X", " ", " "], [" ", " ", " "], [" ", " ", " "]] #make a change to only one element globally
            

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
                
