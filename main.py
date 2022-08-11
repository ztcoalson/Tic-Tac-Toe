from shutil import move
from board import *

def main():
    #game ready
    g = Game()
    win = False
    while not win:
        g.print_board()
        g.player_turn()
        g.ai_turn()
        g.print_board()
        win = True

if __name__ == "__main__":
    main()