import pygame
import os
from Board import Board
from Ceil import Ceil

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
k = 0
current_directory = os.path.abspath(os.getcwd())
active_chess = None
pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
active_color = 'WHITE'
passive_color = 'BLACK'


def draw_letters_and_numbers(screen):
    font = pygame.font.Font(None, 30)
    k, k1 = 0, 1
    for i in range(2):
        if i:
            texts = letters.copy()
            x, y = 80, 780
        else:
            texts = numbers.copy()
            x, y = 5, 5
        for j in range(8):
            text = font.render(str(texts[j]), True, (128, 128, 128))
            text_x = x + j * 100 * k
            text_y = y + j * 100 * k1
            screen.blit(text, (text_x, text_y))

        k, k1 = 1, 0


def load_image(name):
    fullname = os.path.join(current_directory, 'data', name)
    image = pygame.image.load(fullname)
    return pygame.transform.scale(image, (80, 80))


def get_coordinate(mouse_pos):
    x, y = mouse_pos
    return Ceil(x // board.cell_size, y // board.cell_size)


if __name__ == '__main__':
    board = Board()
    running = True
    screen.fill(pygame.Color('white'))
    ceils = board.get_board()
    while running:
        for i in range(board.height):
            for j in range(board.width):
                coordinate = i * board.cell_size, j * board.cell_size
                size = board.cell_size, board.cell_size
                if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                    ceil_color = (255, 255, 255)
                else:
                    ceil_color = (31, 20, 10)
                pygame.draw.rect(screen,
                                 ceil_color,
                                 (coordinate, size), 0)
                if figure := board.get_figure(Ceil(i, j)):
                    screen.blit(load_image(figure.get_image()), (coordinate[0] + 10, coordinate[1] + 10))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                selected_coordinate = get_coordinate(event.pos)
                figure = board.get_figure(selected_coordinate)
                if not active_chess or k == 1:
                    if figure:
                        if figure.color == active_color:
                            active_chess = figure
                            k = 0
                            active_color, passive_color = passive_color, active_color
                else:
                    if not figure:
                        board.move_figure(active_chess, selected_coordinate, board)
                        k = 1
                    else:
                        board.move_figure(active_chess, selected_coordinate, board)
                        k = 1
        draw_letters_and_numbers(screen)
        pygame.display.flip()
    pygame.quit()
