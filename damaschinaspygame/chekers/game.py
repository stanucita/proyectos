import pygame#para la compilacion de esta libreria se esta usando la version de python 3.10.2
from .constants import RED, WHITE, BLUE, SQUARE_SIZE# importamos de la hoja que llamamos constantes las siguientes tuplas lo que nos permite almacenar valores de manera ordenada
from chekers.board import Board#abrimos la carpeta de damas chinas y abrimos la hoja de la configuracion central

class Game:# definimos la clase del que en este caso es la central del juego que luego llamaremos en la interfaz principal
    def __init__(self, win):# construimos de base con el self de inicializador base
        self._init()
        self.win = win#ganar
    
    def update(self):# en esta funcion encontramos los posibles movimientos que son posibles realizar por cada ficha
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None #por el puntero que pase sobre la ficha enseñara a donde se podra mover la ficha seleccionada
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}#validamos los movimiento si son posibles

    def winner(self):
        return self.board.winner()#{ñlkjhgfdssdfghjklñ}

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
            
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED