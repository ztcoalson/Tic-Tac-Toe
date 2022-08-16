import random

class Ai:
    def __init__(self, icon, name = "ai"):
        self.name = name
        self.icon = icon

    def choice(self, board):
        while True:
            row, col = random.randint(0, 2), random.randint(0, 2)
            if board[row][col] == " ":
                return row, col