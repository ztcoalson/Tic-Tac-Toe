from shutil import move
from game import *

def main():
    ai1 = Ai('X')
    ai2 = Ai('O')
    g = Game()
    print(g.play(ai1, ai2))
    

if __name__ == "__main__":
    main()