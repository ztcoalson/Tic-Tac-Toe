from shutil import move
from board import *

def main():
    #game ready
    g = Game()
    while not g.check_win():
        g.print_board()
        g.player_turn()
        if g.check_win():
            g.print_board()
            break
        g.ai_turn()
        g.print_board()

if __name__ == "__main__":
    main()