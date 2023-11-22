import pygame
import random

# the following are the 3 piece blocks
# rotation 1
piece3shape1 = [['xxx'],
                # rotation 2
                ['x',
                 'x',
                 'x']]

# rotation 1
piece3shape2 = [['xx',
                 'x.'],
                # rotation 2
                ['x.',
                 'xx'],
                # rotation 3
                ['xx',
                 '.x']]

# the following will be the 4 piece blocks
# rotation 1
piece4shape1 = [['xx',
                 'xx']]

# rotation 1
piece4shape2 = [['.xx',
                 'xx.'],
                # rotation 2
                ['x.',
                 'xx',
                 '.x']]

# rotation 1
piece4shape3 = [['xx.',
                 '.xx'],
                # rotation 2
                ['.x',
                 'xx',
                 'x.']]

# rotation 1
piece4shape4 = [['x',
                 'x',
                 'x',
                 'x'],

                # rotation 2
                ['xxxx']]

# rotation 1
piece4shape5 = [['...x.',
                 '.xxx.'],
                # rotation 2
                ['..x..',
                 '..x..',
                 '..xx.'],
                # rotation 3
                ['xxx',
                 'x..'],
                # rotation 4
                ['xx',
                 '.x',
                 '.x']]

# rotation 1
piece4shape6 = [['x..',
                 'xxx'],
                # rotation 2
                ['xx',
                 'x.',
                 'x.', ],
                # rotation 3
                ['xxx',
                 '..x'],
                # rotation 4
                ['x.',
                 'x.',
                 'xx']]

# rotation 1
piece4shape7 = [['.x.',
                 'xxx'],
                # rotation 2
                ['x.',
                 'xx',
                 'x.'],
                # rotation 3
                ['xxx',
                 '.x.'],
                # rotation 4
                ['.x',
                 'xx',
                 '.x']]

# the following will be the 5 piece blocks
# rotation 1
piece5shape1 = [['xxxxx'],

                ['x',
                 'x',
                 'x',
                 'x',
                 'x']]
# rotation 1
piece5shape2 = [['x...',
                 'xxxx'],
                # rotation 2
                ['xx',
                 'x.',
                 'x.',
                 'x.'],
                # rotation 3
                ['xxxx',
                 '...x'],
                # rotation 4
                ['.x',
                 '.x',
                 '.x',
                 '.x',
                 'xx']]

# rotation 1
piece5shape3 = [['xxxx',
                 'x...'],
                # rotation 2
                ['xx',
                 '.x',
                 '.x',
                 '.x'],
                # rotation 3
                ['...x',
                 'xxxx'],
                # rotation 4
                ['x.',
                 'x.',
                 'x.',
                 'x.',
                 'xx']]

# rotation 1
piece5shape4 = [['xx'
                 'xx'
                 '.x'],
                # rotation 2
                ['xxx'
                 'xx.'],
                # rotation 3
                ['x.',
                 'xx',
                 'xx'],
                # rotation 4
                ['.xx',
                 'xxx']]

# rotation 1
piece5shape5 = [['xx',
                 'xx',
                 'x.'],
                # rotation 2
                ['xxx',
                 '.xx'],
                # rotation 3
                ['.x',
                 'xx',
                 'xx'],
                # rotation 4
                ['xx.',
                 'xxx']]

# rotation 1
piece5shape6 = [['.xx',
                 'xx.',
                 '.x.'],
                # rotation 2
                ['x..',
                 'xxx',
                 '.x.'],
                # rotation 3
                ['.x.',
                 '.xx',
                 'xx.'],
                # rotation 4
                ['.x.',
                 'xxx',
                 '..x']]

# rotation 1
piece5shape7 = [['xx.',
                 '.xx',
                 '.x.'],
                # rotation 2
                ['..x',
                 'xxx',
                 '.x.'],
                # rotation 3
                ['.x.',
                 'xx.',
                 '.xx'],
                # rotation 4
                ['.x.',
                 'xxx',
                 'x..']]

# rotation 1
piece5shape8 = [['.x',
                 'xx',
                 '.x',
                 '.x'],
                # rotation 2
                ['xxxx',
                 '.x..'],
                # rotation 3
                ['x.',
                 'x.',
                 'xx',
                 'x.'],
                # rotation 4
                ['..x.',
                 'xxxx']]

# rotation 1
piece5shape9 = [['x.',
                 'xx',
                 'x.',
                 'x.'],
                # rotation 2
                ['xxxx',
                 '..x.'],
                # rotation 3
                ['.x',
                 'xx',
                 '.x',
                 '.x'],
                # rotation 4
                ['.x..',
                 'xxxx']]

# rotation 1
piece5shape10 = [['xx..',
                  '.xxx'],
                 # rotation 2
                 ['.x',
                  '.x',
                  'xx',
                  'x.'],
                 # rotation 3
                 ['xxx.',
                  '..xx'],
                 # rotation 4
                 ['.x',
                  'xx',
                  'x.',
                  'x.']]

# rotation 1
piece5shape11 = [['..xx',
                  'xxx.'],
                 # rotation 2
                 ['.x',
                  'xx',
                  '.x',
                  '.x'],
                 # rotation 3
                 ['.xxx',
                  'xx..'],
                 # rotation 4
                 ['x.',
                  'x.',
                  'xx',
                  '.x']]

# rotation 1
piece5shape12 = [['x.x',
                  'xxx'],
                 # rotation 2
                 ['xx',
                  'x.',
                  'xx'],
                 # rotation 3
                 ['xxx',
                  'x.x'],
                 # rotation 4
                 ['xx',
                  '.x',
                  'xx']]

# rotation 1
piece5shape13 = [['xxx',
                  '.x.',
                  '.x.'],
                 # rotation 2
                 ['..x',
                  'xxx',
                  '..x'],
                 # rotation 3
                 ['.x.',
                  '.x.',
                  'xxx'],
                 # rotation 4
                 ['x..',
                  'xxx',
                  'x..']]

# rotation 1
piece5shape14 = [['x..',
                  'x..',
                  'xxx'],
                 # rotation 2
                 ['xxx',
                  'x..',
                  'x..'],
                 # rotation 3
                 ['xxx',
                  '..x',
                  '..x'],
                 # rotation 4
                 ['..x',
                  '..x',
                  'xxx']]

# rotation 1
piece5shape15 = [['..x',
                  '.xx',
                  'xx.'],
                 # rotation 2
                 ['x..',
                  'xx.',
                  '.xx'],
                 # rotation 3
                 ['.xx',
                  'xx.',
                  'x..'],
                 # rotation 4
                 ['xx.',
                  '.xx',
                  '..x']]

# rotation 1
piece5shape16 = [['.x.',
                  'xxx',
                  '.x.']]

# rotation 1
piece5shape17 = [['.xx',
                  '.x.',
                  'xx.'],
                 # rotation 2
                 ['x..',
                  'xxx',
                  '..x'],
                 # rotation 3
                 ['.xx',
                  '.x.',
                  'xx.'],
                 # rotation 4
                 ['x..',
                  'xxx',
                  '..x']]

# rotation 1
piece5shape18 = [['xx.',
                  '.x.',
                  '.xx'],
                 # rotation 2
                 ['..x',
                  'xxx',
                  'x..'],
                 # rotation 3
                 ['xx.',
                  '.x.',
                  '.xx'],
                 # rotation 4
                 ['..x',
                  'xxx',
                  'x..']]

shapes_3piece = [piece3shape1, piece3shape2]

shapes_4piece = [piece4shape1, piece4shape2, piece4shape3, piece4shape4, piece4shape5, piece4shape6, piece4shape7]

shapes_5piece = [piece5shape1, piece5shape2, piece5shape3, piece5shape4, piece5shape5, piece5shape6, piece5shape7,
                 piece5shape8, piece5shape9,
                 piece5shape10, piece5shape11, piece5shape12, piece5shape13, piece5shape14, piece5shape15,
                 piece5shape16, piece5shape17, piece5shape18]

colour_bank = [(225, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]


# the colours are listed as follows [red, green, blue, yellow, cyan and magenta]

class Piece(object):  # This is the parent class for all the objects
    def __init__(self, x, y, shape, colour, rotation):
        self.x = x
        self.y = y
        self.shape = shape
        self.colour = colour
        self.rotation = rotation

    def movement(self, userInput):
        if userInput == pygame.K_RIGHT:
            self.x += 1
        if userInput == pygame.K_LEFT:
            self.x -= 1
        if userInput == pygame.K_DOWN:
            self.y += 1
        if userInput == pygame.K_UP:
            self.y -= 1


    def rotation(self, userInput):
        if userInput == pygame.K_UP:
            self.rotation += 1
        if userInput == pygame.K_DOWN:
            self.rotation -= 1



#this will loop and create a random piece of a random colour using the class created
def retrieve_3piece():
    return Piece(4, 0, random.choice(shapes_3piece), (random.choice(colour_bank)), 0)

#this will loop and create a random piece of a random colour using the class created
def retrieve_4piece():
    return Piece(5, 0, random.choice(shapes_4piece), (random.choice(colour_bank)), 0)

#this will loop and create a random piece of a random colour using the class created
def retrieve_5piece():
    return Piece(6, 0, random.choice(shapes_5piece), random.choice(colour_bank), 0)

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

#this module will create the easy mode playfield and checks if positions is taken
def playfield_easymode():
    playfield = [[(0, 0, 0) for x in range(8)] for y in range(16)]

    return playfield

#this module will create the regular mode playfield and checks if positions is taken
def playfield_regularmode():
    playfield = [[(0, 0, 0) for x in range(10)] for y in range(20)] #creates 3 black boxes 10 times for 20 rows

    return playfield

#this module will create the hard mode playfield and checks if positions is taken
def playfield_hardmode():
    playfield = [[(0, 0, 0) for x in range(12)] for y in range(24)]#creates 3 black boxes 12 times for 24 rows

    return playfield


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
    board_range = [(1, 15), (2, 15), (3, 15), (4, 15), (5, 15), (6,15), (7,15), (8, 15)]
    taken_position = []

    score = 0
    clock = pygame.time.Clock() #keeps track of time
    falling_speed = 500
    time = 0
    #this will be the initial falling speed


    run = True
    while run:
        playfield = playfield_easymode()
        time += clock.get_rawtime()
        clock.tick()

        coordinates = convert_shape(moving_piece)

        for z in range(len(taken_position)):
            row, col = taken_position[z]
            playfield[col][row] = moving_piece.colour

        for z in range(3):
            row, col = coordinates[z]#This will get the pieces in the forms (2,0),(3,0),(3,1)
            playfield[col][row] = moving_piece.colour#Converts the coordinates to the colour

        if time > falling_speed:
            time = 0
            falling_speed += score*10
            moving_piece.y += 1
            if coordinates[0] in board_range:
                taken_position.append(coordinates[0])
                taken_position.append(coordinates[1])
                taken_position.append(coordinates[2])
                moving_piece = display_piece
                display_piece = retrieve_3piece()


            if coordinates[0] in taken_position:
                for z in range(3):
                    row, col = coordinates[z]
                    taken_position.append((row, col - 1))
                moving_piece = display_piece
                display_piece = retrieve_3piece()

            if coordinates[1] in board_range:
                taken_position.append(coordinates[0])
                taken_position.append(coordinates[1])
                taken_position.append(coordinates[2])
                moving_piece = display_piece
                display_piece = retrieve_3piece()

            if coordinates[1] in taken_position:
                for z in range(3):
                    row, col = coordinates[z]
                    taken_position.append((row, col - 1))
                moving_piece = display_piece
                display_piece = retrieve_3piece()

            if coordinates[2] in board_range:
                taken_position.append(coordinates[0])
                taken_position.append(coordinates[1])
                taken_position.append(coordinates[2])
                moving_piece = display_piece
                display_piece = retrieve_3piece()

                for i in range(len(playfield)):
                    for j in range(len(playfield[i])):
                        row = playfield[i]
                        if (0, 0, 0) not in row:
                            taken_position.remove((i, j))

            if coordinates[2] in taken_position:
                Piece.movement(moving_piece, pygame.K_UP)
                for z in range(3):
                    row, col = coordinates[z]
                    taken_position.append((row, col - 1))
                moving_piece = display_piece
                display_piece = retrieve_3piece()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


            if event.type == pygame.KEYDOWN: #this will how the imputs from the keyboards are interpreted
                if event.key == pygame.K_DOWN:
                    Piece.movement(moving_piece, pygame.K_DOWN)
                if event.key == pygame.K_LEFT:
                    Piece.movement(moving_piece, pygame.K_LEFT)
                    if coordinates[0] < (0,100) or coordinates[1] < (0,100) or coordinates[2] < (0,100):#Checks if the piece is out of range
                        Piece.movement(moving_piece, pygame.K_RIGHT)#It is the opposite and undoes the previous line
                    if coordinates[0] or coordinates[1] or coordinates[2] in taken_position:
                        Piece.movement(moving_piece, pygame.K_RIGHT)  # It is the opposite and undoes the previous line

                if event.key == pygame.K_RIGHT:
                    Piece.movement(moving_piece, pygame.K_RIGHT)
                    if coordinates[0] > (7,-100) or coordinates[1] > (7,-100) or coordinates[2] > (7,-100):#Checks if the piece is out of range
                        Piece.movement(moving_piece, pygame.K_LEFT)#It is the opposite and undoes the previous line
                if event.key == pygame.K_UP:
                    Piece.rotation(moving_piece, pygame.K_UP)
                    if coordinates[0] > (7,-100) or coordinates[1] > (7,-100) or coordinates[2] > (7,-100) or coordinates[0] < (0,100) or coordinates[1] < (0,100) or coordinates[2] < (0,100):#Checks if the piece is out of range
                        Piece.rotation(moving_piece, pygame.K_DOWN)#It is the opposite and undoes the previous line

        win.fill((240,248,255))

        for i in range(len(playfield)):
            for j in range(len(playfield[i])):
                pygame.draw.rect(win, playfield[i][j], [144 + j * 36, 24 + i * 36, 36, 36], 0)
                pygame.draw.rect(win, ((0, 0, 0)), [144, 24, 288, 576], 1)

        for i in range(len(playfield)):
            for j in range(len(playfield[i])):
                if playfield[i][j] == (255,255,255):
                    print('false')


        pygame.display.update()




main_EGame()
