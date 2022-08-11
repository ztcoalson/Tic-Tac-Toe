import re

class Player:
    def choice(self, board):
        while True:
            moves = re.split(" ", input("Move: "))
            if len(moves) != 2:
                print("please enter a valid move in the form of 'row column'")
                continue
            row, col = moves[0], moves[1]
            if not row.isdigit() or not col.isdigit():
                print("please enter numerical values only")
                continue
            row, col = int(row), int(col)
            if row > 3 or row < 1 or col > 3 or col < 1:
                print("please enter values between 1 and 3")
                continue
            if board[row-1][col-1] != " ":
                print("this space is occupied")
                continue
            break
        return row, col
            
                
            