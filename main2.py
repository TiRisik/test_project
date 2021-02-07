import pygame
import os
from Board import Board
from Ceil import Ceil

k = 0
active_chess = None
pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size)


def load_image(name):
    fullname = os.path.join('../data', name)
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
                        active_chess = figure
                        k = 0
                else:
                    if not figure:
                        board.move_figure(active_chess, selected_coordinate)
                        k = 1
        pygame.display.flip()
    pygame.quit()

    #
    # board.render(screen)
    # draw_letters_and_numbers(screen)
    # imch = ImageChess()
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             coordinate_chess = board.get_coordinate(event.pos)
    #             if coordinate_chess in white_coordinate or coordinate_chess in black_coordinate:
    #                 active_chess = coordinate_chess
    #             elif active_chess:
    #                 imch.update(active_chess, coordinate_chess)
    #                 imch.select_photo(screen)
    #                 board.render(screen)
    #     imch.select_photo(screen)
    #     draw_letters_and_numbers(screen)
    #     pygame.display.flip()
    # pygame.quit()
