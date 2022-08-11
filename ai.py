import random

class Ai:
    def choice(self, board):
        while True:
            row, col = random.randrange(1, 3), random.randrange(1, 3)
            if board[row][col] != " ":
                continue
            break
        return row, col