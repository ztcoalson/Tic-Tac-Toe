from net import *
import torch
import random

class Ai:
    def __init__(self, icon, number, name = "ai"):
        self.name = name
        self.icon = icon
        self.number = number
        self.net = Net() # TODO: load net from set of weights with mutations

    def random_choice(self, board):
        while True:
            row, col = random.randint(0, 2), random.randint(0, 2)
            if board[row][col] == 0:
                return row, col
    
    def choice(self, board):
        # convert game info to tensor
        ai_number, board_state = torch.tensor([self.number], dtype=torch.float), torch.flatten(torch.tensor(board, dtype=torch.float))
        inputs = torch.cat((ai_number, board_state))
        
        # get output from net
        with torch.no_grad():
            output = torch.argmax(self.net(inputs)).item()

        # return network output if it is valid else random choice
        return (output//3, output%3) if board[output//3][output%3] == 0 else self.random_choice(board)
