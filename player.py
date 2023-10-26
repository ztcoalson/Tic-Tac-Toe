class Player:
    def __init__(self, c) -> None:
        self.c = c

    def valid_move(self, x, y, board):
        try:
            board[x][y]
        except:
            return False
        
        return board[x][y] == " "

    def make_move(self, board):
        user_input = input("Move: ").split(" ")
        x, y = int(user_input[0])-1, int(user_input[1])-1
        
        while not self.valid_move(x, y, board):
            user_input = input("Invalid move, try again: ")
            x, y = int(user_input[0])-1, int(user_input[1])-1
        
        board[x][y] = self.c