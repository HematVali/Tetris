import pygame
import random


"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

pygame.font.init()

# GLOBALS VARS
s_width = 600
s_height = 900
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

# SHAPE FORMATS

S = [['.xx',
      'xx.'],

     ['x.',
      'xx',
      '.x']]

Z = [['.....',
      '.....',
      '.xx..',
      '..xx.',
      '.....'],

     ['.....',
      '..x..',
      '.xx..',
      '.x...',
      '.....']]

I = [['..x..',
      '..x..',
      '..x..',
      '..x..',
      '.....'],

     ['.....',
      'xxxx.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.xx..',
      '.xx..',
      '.....']]

J = [['.x...',
      '.xxx.',
      '.....',
      '.....'],

     ['..xx.',
      '..x..',
      '..x..',],

     ['.xxx.',
      '...x.',
      '.....'],

     ['..x..',
      '..x..',
      '.xx..',
      '.....']]

LPiece = [['.....',
      '...x.',
      '.xxx.',
      '.....',
      '.....'],

     ['.....',
      '..x..',
      '..x..',
      '..xx.',
      '.....'],

     ['.....',
      '.....',
      '.xxx.',
      '.x...',
      '.....'],

     ['.....',
      '.xx..',
      '..x..',
      '..x..',
      '.....']]

T = [['.....',
      '..x..',
      '.xxx.',
      '.....',
      '.....'],

     ['.....',
      '..x..',
      '..xx.',
      '..x..',
      '.....'],
     ['.....',
      '.....',
      '.xxx.',
      '..x..',
      '.....'],
     ['.....',
      '..x..',
      '.xx..',
      '..x..',
      '.....']]


shapes = [S, Z, I, O, J, LPiece, T]
shape_colours = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]

# index 0 - 6 represent shape


class Piece(object): #This is the parent class for all the objects
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.colour = shape_colours[shapes.index(shape)]
        self.rotation = 0

def create_grid(locked_pos={}):
    grid = [[(0, 0, 0) for x in range(10)] for y in range(20)]  # this is the creation of the grid its been looped and it means 10 rows of black

    for i in range(20):                #checks if there is already an object make it 10 and 20
        for j in range(10):
            if (j, i) in locked_pos:
                x = locked_pos[(j, i)]
                grid[i][j] = x

    return grid

def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == 'x':
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1])

    return positions

def valid_space(shape, grid):
    accepted_pos = [[(j, i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]
    accepted_pos = [j for sub in accepted_pos for j in sub]

    formatted = convert_shape_format(shape)

    for pos in formatted:
        if pos not in accepted_pos:
            if pos[1] > -1:
                return False
    return True


def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y  < 1:
            return True

    return False


def get_shape():
    return Piece(5, 0, random.choice(shapes))


def draw_text_middle(text, size, color, surface):
    pass





def clear_rows(grid, locked):
    inc = 0
    for i in range(len(grid)-1, -1, -1):
        row = grid[i]
        if (0,0,0) not in row:
            inc += 1
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j,i)]
                except:
                    continue

    if inc > 0:
        for key in sorted(list(locked), key = lambda x: x[1]) [::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y +inc)
                locked[newKey] = locked.pop(key)

def draw_next_shape(shape, surface):
    font = pygame.font.SysFont('comicsanns', 30)
    label = font.render('next shape', 1, (255,255,255))

    x = top_left_x + play_width
    y = top_left_y + play_height/2
    format = shape.shape[shape.rotation % len(shape.shape)]


    surface.blit(label, (x + 10, y - 30))

def draw_window(surface, grid):
    surface.fill((0, 0, 0))

    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('tetris', 1, (255, 255, 255))  # creates the text at the top

    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))  # locates the text in the top middle of the screen


    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y + i*block_size, block_size, block_size), 0)
            pygame.draw.rect(surface, (25,0,0), (top_left_x, top_left_y, play_width, play_height), 5) #this is the big rectangle


    #pygame.display.update()

def main(win):

    locked_positions = {}
    lines = 0

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time/1000 > fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not(valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN: #this will how the imputs from the keyboards are interpreted
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.x += 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.x -= 1
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.y -= 1
                if event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.rotation -= 1


        shape_pos = convert_shape_format(current_piece)

        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.colour

        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.colour
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            clear_rows(grid, locked_positions)
            lines = 0

        draw_window(win, grid)
        draw_next_shape(next_piece, win)
        pygame.display.update()

        if check_lost(locked_positions):
            run = False

    pygame.display.quit()


def main_menu(win):
    main(win)



def isCompleteLine(board, y):
    # Return True if the line filled with boxes with no gaps.
    for x in range(10):
        if board[y][x] == (0,0,0):
            return False

    return True

def removeCompleteLines(board):
    # Remove any completed lines on the board, move everything above them down, and return the number of complete lines.
    numLinesRemoved = 0
    y = 20 - 1 # start y at the bottom of the board
    while y >= 0:
        if isCompleteLine(board, y):
            # Remove the line and pull boxes down by one line.
            for pullDownY in range(y, 0, -1):
                for x in range(10):
                    board[x][pullDownY] = board[x][pullDownY-1]
            # Set very top line to blank.
            for x in range(10):
                board[x][0] = (0,0,0)
            numLinesRemoved += 1
            # Note on the next iteration of the loop, y is the same.
            # This is so that if the line that was pulled down is also
            # complete, it will be removed.
        else:
            y -= 1 # move on to check next row up

    return numLinesRemoved


def intersects(grid):
    score = 0
    for i in range(1, 16):
        zeros = 0
        for j in range(8):
            if grid[i][j] == (0, 0, 0):
                zeros += 1
        if zeros == 0:
            for i1 in range(i, 1, -1):
                for j in range(9):
                    grid[i1][j] = grid[i1 - 1][j]


    return score

def break_lines():
    lines = 0

win = pygame.display.set_mode((s_width, s_height))   #the final display
pygame.display.set_caption('tetris')
main_menu(win)  # start game