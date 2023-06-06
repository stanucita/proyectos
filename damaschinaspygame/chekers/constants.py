import pygame

WIDTH, HEIGHT = 800, 800#ancho y altura
ROWS, COLS = 8, 8#filas y columnas
SQUARE_SIZE = WIDTH//COLS#tamaño del cuadrado 


RED = (255, 0, 0)#color de los cuadros
WHITE = (255, 255, 255)#color de la ficha blanca
BLACK = (0, 0, 0)#color de la ficha negra
BLUE = (0, 0, 255)# identificador de movimiento
GREY = (128,128,128)#margen de las fichas

CROWN = pygame.transform.scale(pygame.image.load('descarga.jpg'), (44, 25))#imagen que aparecera al ganar la partida