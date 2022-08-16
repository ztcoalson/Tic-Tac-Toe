from shutil import move
from game import *
from ml import *

def main():
    ml = ML(100)
    print(ml.runIteration())

if __name__ == "__main__":
    main()