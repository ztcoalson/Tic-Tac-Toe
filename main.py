from shutil import move
from board import *

def main():
    g = Game()
    g.print_board()
    g.player_turn()
    g.print_board()

if __name__ == "__main__":
    main()