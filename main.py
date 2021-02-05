import pygame
from drawing import Board, draw_letters_and_numbers, ImageChess, white_coordinate, black_coordinate

active_chess = None
pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size)


if __name__ == '__main__':
    board = Board(8, 8)
    running = True
    screen.fill(pygame.Color('white'))
    board.render(screen)
    draw_letters_and_numbers(screen)
    imch = ImageChess()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                coordinate_chess = board.get_coordinate(event.pos, screen)
                if coordinate_chess in white_coordinate or coordinate_chess in black_coordinate:
                    active_chess = coordinate_chess
                elif active_chess:
                    imch.update(active_chess, coordinate_chess)
                    imch.select_photo(screen)
                    board.render(screen)
        imch.select_photo(screen)
        draw_letters_and_numbers(screen)
        pygame.display.flip()
    pygame.quit()
