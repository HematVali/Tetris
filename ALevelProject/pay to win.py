import pygame, sys, time
from pygame.locals import QUIT
BLUE = (  0,   0, 155)
BOX_SIZE = 20
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BOARD_WIDTH = 10

def run_tetris_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('My Tetris')

    ########## NEW #########################
    piece = create_piece()
    ########################################
    while True:
        screen.fill((  0,   0,   0))


        ############## DISPLAY PIECE IN THE BOARD #####################
        draw_piece(screen, piece)
        ###############################################################
        pygame.draw.rect(
            screen,
            BLUE,
            [100, 50, 10*20, 20*20-10], 5)

        pygame.display.update()

        for event in pygame.event.get(QUIT):
            pygame.quit()
            sys.exit()

def create_piece():
    piece = {}
    piece['row'] = 0
    piece['column'] = 4
    return piece

def draw_piece(screen, piece):
    shadow_color = (217, 222, 226)
    # board margin + line thickness + (column * box_size)
    origin_x = 100 + 1 +(piece['column']*20+1)
    origin_y = 50 + 5 + (piece['row']*20+1)
    pygame.draw.rect(screen, shadow_color, [origin_x, origin_y, 20, 20])


def create_game_matrix():
    game_matrix_columns = 10
    game_matrix_rows = 20
    board = []
    for row in range(game_matrix_rows):
        new_row = []
        for column in range(game_matrix_columns):
            new_row.append('.')
        board.append(new_row)
    return board

run_tetris_game()