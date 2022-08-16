import random

class Ai:
    def __init__(self, icon):
        self.name = "ai"
        self.icon = icon

    def choice(self, board):
        while True:
            row, col = random.randint(0, 2), random.randint(0, 2)
            if board[row][col] == " ":
                return row, col