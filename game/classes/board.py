from .figure import *
from .symbols import *

import base64


class Board:
    def __init__(self):
        self.white_figures = (
            [Pawn(2, i) for i in range(1, 9)]
            + [Rook(1, 1), Rook(1, 8)]
            + [Knight(1, 2), Knight(1, 7)]
            + [Bishop(1, 3), Bishop(1, 6)]
            + [Queen(1, 4), King(1, 5)]
        )

        self.black_figures = (
            [Pawn(7, i, color="black") for i in range(1, 9)]
            + [Rook(8, 1, color="black"), Rook(8, 8, color="black")]
            + [Knight(8, 2, color="black"), Knight(8, 7, color="black")]
            + [Bishop(8, 3, color="black"), Bishop(8, 6, color="black")]
            + [Queen(8, 5, color="black"), King(8, 4, color="black")]
        )

        self.figures = self.white_figures + self.black_figures

        for figure in self.figures:
            figure.set_other_figures(self.figures)

    
    def __str__(self):
        board = [[' ' for _ in range(8)] for __ in range(8)] 
        
        for figure in self.get_figures():
            if figure.is_alive():
                board[8 - (figure.x)][figure.y - 1] = SYMBOLS[figure.color + '_' + figure.name.lower()]

        return '\n'.join([''.join(s) for s in board])

    def get_figures(self):
        return self.figures 
    
    def move(self, x1, y1, x2, y2, user_friendly=True):
        print(self)
        print(x1, y1)
        for figure in self.get_figures():
            if figure.get_coordinates() == (x1, y1):
                return figure.move(x2, y2, user_friendly=user_friendly)
        else:
            raise FigureNotFoundException(x1, y1)
        
    def get_attack_positions(self, x, y):
        for figure in self.get_figures():
            if figure.get_coordinates() == (x, y):
                return figure.get_attack_positions()
        
    def game_is_going(self):
        for figure in self.get_figures():
            if isinstance(figure, King):
                if not figure.is_alive():
                    return False 
        return True
    
    def who_is_winner(self):
        alive_kings = []
        for figure in self.get_figures():
            if isinstance(figure, King):
                if figure.is_alive():
                    alive_kings.append(figure.color)
        
        if len(alive_kings) in [0, 2]:
            return None 
        else:
            return alive_kings[0]
        
    def encode(self):
        s = ''
        for figure in self.get_figures():
            if figure.is_alive():
                s += FIGURES_TO_NUMBERS[figure.name.lower()] 
                s += figure.color.lower()[0]
                s += str(figure.get_coordinates()[0]) + str(figure.get_coordinates()[1])
        return s 
    

    



