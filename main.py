from game import *
from ml import *

def main():
    game = Game()
    winner = game.play()
    print(f"{winner} wins!")

if __name__ == "__main__":
    main()