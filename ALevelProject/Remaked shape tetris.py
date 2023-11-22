import pygame
import random

figures = [
    [[1, 5, 9, 13], [4, 5, 6, 7]],
    [[4, 5, 9, 10], [2, 6, 5, 9]],
    [[6, 7, 9, 10], [1, 5, 6, 10]],
    [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
    [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
    [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
    [[1, 2, 5, 6]],
]

colour_bank = [(225, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]


# the colours are listed as follows [red, green, blue, yellow, cyan and magenta]

class Piece(object):  # This is the parent class for all the objects
    def __init__(self, x, y, shape, colour, rotation):
        self.x = x
        self.y = y
        self.shape = random.randint(figures)
        self.colour = colour
        self.rotation = rotation

    def draw(self):
        Piece.draw(playfield_easymode())

    def movement(self, userInput):
        if userInput == pygame.K_RIGHT:
            self.x += 1
        if userInput == pygame.K_LEFT:
            self.x -= 1
        if userInput == pygame.K_DOWN:
            self.y += 1

    def rotation(self):
        self.rotation = self.rotation + 1







#this will loop and create a random piece of a random colour using the class created
def retrieve_3piece():
    return Piece(4, 0, random.choice(figures), (random.choice(colour_bank)), 0)

#this will loop and create a random piece of a random colour using the class created
def retrieve_4piece():
    return Piece(5, 0, random.choice(figures), (random.choice(colour_bank)), 0)

#this will loop and create a random piece of a random colour using the class created
def retrieve_5piece():
    return Piece(6, 0, random.choice(figures), random.choice(colour_bank), 0)

#the piece format needs to be converted from 'x' and '.'
def convert_shape(shape):
    coordinates = []
    layout = shape.shape[shape.rotation % len(shape.shape)] #checks which rotation the shape is on as it uses the mod function

    for i, line in enumerate(layout):
        row = list(line)
        for j, column in enumerate(row):
            if column == 'x':#if the column has and x
                coordinates.append((shape.x + j, shape.y + i))#the coordinates are taken int

    for i, pos in enumerate(coordinates):
        coordinates[i] = (pos[0] - 2, pos[1])

    return coordinates


block_size  = 36 #each squeare will be 6 by 6

#dimensions for the easy mode
E_playF_width = 288
E_playF_height = 576
E_win_width = 576
E_win_height = 600
#this will be the actual window detail for the easy mode
E_win = pygame.display.set_mode((E_win_width, E_win_height))
pygame.display.set_caption('easy mode')

#dimensions for the regular mode
R_playF_width = 360
R_playF_height = 720
R_win_width = 720
R_win_height = 800
#this will be the actual window detail for the regular mode
R_win = pygame.display.set_mode((R_playF_width, R_playF_height))
pygame.display.set_caption('regular mode')

#dimensions for the difficult mode
H_playF_width = 432
H_playF_height = 864
H_win_width = 864
H_win_height = 900
#this will be the actual window detail for the hard mode
H_win = pygame.display.set_mode((H_playF_width, H_playF_height))
pygame.display.set_caption('hard mode')

#this module will create the easy mode playfield and checks if positions is taken
def playfield_easymode():
    playfield = [[(240,248,255) for i in range(8)] for j in range(16)] #creates 3 black boxes 8 times for 16 rows


    return playfield

#this module will create the regular mode playfield and checks if positions is taken
def playfield_regularmode():
    playfield = [[(0, 0, 0) for x in range(10)] for y in range(20)] #creates 3 black boxes 10 times for 20 rows

    return playfield

#this module will create the hard mode playfield and checks if positions is taken
def playfield_hardmode():
    playfield = [[(0, 0, 0) for x in range(12)] for y in range(24)]#creates 3 black boxes 12 times for 24 rows

    return playfield

clock = pygame.time.Clock()
clock.tick()
time = 0

def falling(y_cooridinate, game_score):
    game_score = 0
    clock = pygame.time.Clock() #keeps track of time
    clock.tick()
    falling_speed = 1
    time = clock.get_rawtime()

    if time > falling_speed:
        time = 0
        y_cooridinate.y += 1

        falling(y_cooridinate, game_score)

locked = []

def main_EGame():
    pygame.init()
    # dimensions for the easy mode
    E_win_width = 576
    E_win_height = 600
    # this will be the actual window detail for the easy mode
    win = pygame.display.set_mode((E_win_width, E_win_height))# creates the window
    pygame.display.set_caption('easy mode')# name of the window
    pygame.display.update()# updates the display
    moving_piece = retrieve_3piece()#current object
    display_piece = retrieve_3piece()

    playfield = playfield_easymode()
    score = 0
    clock = pygame.time.Clock() #keeps track of time
    falling_speed = 500
    time = 0
    #this will be the initial falling speed
    valid_position = [[(x, y) for x in range (8) if playfield[y][x] == (240,248,255)] for y in range(16)]

    run = True
    while run:
        playfield = playfield_easymode()
        time += clock.get_rawtime()
        clock.tick()


        if time > falling_speed:
            time = 0
            moving_piece.y += 1
            falling_speed += score*10


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN: #this will how the imputs from the keyboards are interpreted
                if event.key == pygame.K_DOWN:
                    Piece.movement(moving_piece, pygame.K_DOWN)
                if event.key == pygame.K_LEFT:
                    Piece.movement(moving_piece, pygame.K_LEFT)
                    if moving_piece.x < 2:
                        Piece.movement(moving_piece, pygame.K_RIGHT)
                if event.key == pygame.K_RIGHT:
                    Piece.movement(moving_piece, pygame.K_RIGHT)
                    if moving_piece.x > 8:
                        Piece.movement(moving_piece, pygame.K_LEFT)
                if event.key == pygame.K_UP:
                    Piece.rotation(moving_piece)



        win.fill((240,248,254))
        shape_pos = moving_piece

        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                playfield[y][x] = moving_piece.colour

        for i in range(len(playfield)):
            for j in range(len(playfield[i])):
                pygame.draw.rect(win, moving_piece.colour, [144 + j * 36, 24 + i * 36, 36, 36], 0)
                pygame.draw.rect(win, ((0, 0, 0)), [144, 24, 288, 576], 1)

        pygame.display.update()




main_EGame()
