import mysql.connector  # import the correct module
from tkinter import *
import tkinter
import pygame
import random
from collections import Counter


# this module will compare the username and password to check if they match up or not
def login_button():
    # compares the inputs and the data from my database
    sql = "SELECT * FROM loginsystem WHERE username = '%s' AND password = '%s'" % (try_username.get(), try_password.get())
    mycursor.execute(sql)  # this will execute the sql statement
    if mycursor.fetchone():  # if the username and the password combination is found that this will be printed
        main_menu()
        return True

    else:  # if the username an dthe password is not found that this will be printed
        print('Invalid password or username')
        return False


def signup_button():
    count_password = len(try_password.get())
    count_username = len(try_username.get())
    if 6 < count_password < 13 and 6 < count_username < 13:
        sql = "insert into loginsystem (username, password) values ('%s', '%s')"  # imports values into database
        inp = (try_username, try_password)
        # this sql statement inputs in the database
        mycursor.execute(sql, inp)  # this will execute the sql statement
        logindb.commit()  # this will make shure it is executed
        print('sign up complete, please press the ''login'' to start playing')  # this shows the user they were succesfull
    else:
        print('the passwords and username needs to be longer that 6 characters and shorter than 14')

def load_up():
    global load
    load = True
    while load: 
        T = Tk()  # this sets up my program nicely
        T.title('login')  # this is the titel of the main game
        T.geometry('300x100')  # dimension of the window
        global try_username  # make the inputs global
        global try_password


        try_username = tkinter.StringVar()  # we indicate what type of variables we declared
        try_password = tkinter.StringVar()

        Label(T, text='Enter Username').place(x=20, y=10)  # creates a labes to tell where username to enter their username
        Label(T, text='Enter Password').place(x=20, y=35)  # creates a labes to tell where username to enter their passwrod

        Entry(textvariable=try_username).place(x=120, y=10)  # creates where the user can actually put their username and password
        Entry(textvariable=try_password).place(x=120, y=35)


        Button(T, text='Login', command=login_button, height=1, width=9).place(x=20, y=60)  # if this button is pressed than login_button module will be carried out
        Button(T, text='Sign Up', command=signup_button, height=1, width=9).place(x=160, y=60)  # if this button is pressed than login_button module will be carried out

        T.mainloop()






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
    return Piece(4, 0, random.choice(shapes_3piece), (225, 255, 255), 0)

#this will loop and create a random piece of a random colour using the class created
def retrieve_4piece():
    return Piece(5, 0, random.choice(shapes_4piece), (225, 255, 255), 0)

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



def clear_rows(x, y, playfield, taken):
    lines = 0
    for i in range(y):
        if (0, 0, 0) not in playfield[i]:
            lines += 1
            constand = i
            for j in range(x):
                try:
                    taken.remove((j, i))
                    taken.remove((j, i))
                    taken.remove((j, i))
                    taken.remove((j, i))
                    taken.remove((j, i))
                except:
                    continue



    if lines > 0:
        for key in sorted(list(taken), key = lambda x: x[1]) [::-1]:
            x, y = key
            if y < constand:
                new_values = (x, y + lines)
                taken.remove(key)
                taken.append(new_values)

    return lines


global score

def check_lost(taken, x):
    for i in range(x):
        if (i, 0) in taken:
            return True
    return False

def main_EGame():
    score = 0
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
    board_range = [(0, 16), (1, 16), (2, 16), (3, 16), (4, 16), (5, 16), (6, 16), (7, 16)]

    taken_position = []

    clock = pygame.time.Clock() #keeps track of time
    falling_speed = 150
    time = 0
    high_score = 1000
    #this will be the initial falling speed



    run = True
    while run:
        playfield = playfield_easymode()
        time += clock.get_rawtime()
        clock.tick()

        coordinates = convert_shape(moving_piece)

        for z in range(len(taken_position)):
            row, col = taken_position[z]
            playfield[col][row] = (255,255,255)

        for z in range(3):
            row, col = coordinates[z]#This will get the pieces in the forms (2,0),(3,0),(3,1)
            playfield[col][row] = moving_piece.colour#Converts the coordinates to the colour
        if time > falling_speed:
            time = 0
            falling_speed == falling_speed + score/100
            moving_piece.y += 1

            row, col = coordinates[0]
            if (row, col + 1) in taken_position or (row, col+1) in board_range:
                for z in range(3):
                    row, col = coordinates[z]
                    taken_position.append((row, col))
                moving_piece = display_piece
                display_piece = retrieve_3piece()
                score += (clear_rows(8, 16, playfield, taken_position)) * 10

            row, col = coordinates[1]
            if (row, col + 1) in taken_position or (row, col+1) in board_range:
                for z in range(3):
                    row, col = coordinates[z]
                    taken_position.append((row, col))
                moving_piece = display_piece
                display_piece = retrieve_3piece()
                score += (clear_rows(8, 16, playfield, taken_position)) * 10

            row, col = coordinates[2]
            if (row, col + 1) in taken_position or (row, col+1) in board_range:
                for z in range(3):
                    row, col = coordinates[z]
                    taken_position.append((row, col))
                moving_piece = display_piece
                display_piece = retrieve_3piece()
                score += (clear_rows(8, 16, playfield, taken_position)) * 10

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


            if event.type == pygame.KEYDOWN: #this will how the imputs from the keyboards are interpreted
                if event.key == pygame.K_DOWN:
                    Piece.movement(moving_piece, pygame.K_DOWN)

                if event.key == pygame.K_LEFT:
                    row1, col1 = coordinates[0]
                    row2, col2 = coordinates[1]
                    row3, col3 = coordinates[2]
                    if (row1 - 1, col1) not in taken_position and (row2 -1 , col2) not in taken_position and (row3 - 1, col3):
                        Piece.movement(moving_piece, pygame.K_LEFT)
                        if coordinates[0] < (0, 100) or coordinates[1] < (0, 100) or coordinates[2] < (0, 100):  # Checks if the piece is out of range
                            Piece.movement(moving_piece, pygame.K_RIGHT)  # It is the opposite and undoes the previous line

                if event.key == pygame.K_RIGHT:
                    row1, col1 = coordinates[0]
                    row2, col2 = coordinates[1]
                    row3, col3 = coordinates[2]
                    if (row1 + 1, col1) not in taken_position and (row2 + 1, col2) not in taken_position and (row3 + 1, col3):
                        Piece.movement(moving_piece, pygame.K_RIGHT)
                        if coordinates[0] > (7,-100) or coordinates[1] > (7,-100) or coordinates[2] > (7,-100):#Checks if the piece is out of range
                            Piece.movement(moving_piece, pygame.K_LEFT)#It is the opposite and undoes the previous line

                if event.key == pygame.K_UP:
                    Piece.rotation(moving_piece, pygame.K_UP)
                    if coordinates[0] > (7,-100) or coordinates[1] > (7,-100) or coordinates[2] > (7,-100):
                        Piece.rotation(moving_piece, pygame.K_DOWN)#It is the opposite and undoes the previous line
                    if coordinates[0] < (0,100) or coordinates[1] < (0,100) or coordinates[2] < (0,100):#Checks if the piece is out of range
                        Piece.rotation(moving_piece, pygame.K_DOWN)#It is the opposite and undoes the previous line

        win.fill((225,255,255))

        for i in range(len(playfield)):
            for j in range(len(playfield[i])):
                pygame.draw.rect(win, playfield[i][j], [0 + j * 36, 24 + i * 36, 36, 36], 0)

        font = pygame.font.SysFont('comicsanns', 30)
        text = font.render("Score: " + str(score), 1, (0,0,0))
        win.blit(text, (300, 100))


        text = font.render("highscore: " + str(high_score), 1, (0, 0, 0))
        win.blit(text, (300, 70))

        if check_lost(taken_position, 8):
            game_over_screen()

        pygame.display.update()





def main_RGame():
    score = 0
    pygame.init()
    # dimensions for the easy mode
    E_win_width = 500
    E_win_height = 550
    # this will be the actual window detail for the easy mode
    win = pygame.display.set_mode((E_win_width, E_win_height))# creates the window
    pygame.display.set_caption('regular mode')# name of the window
    pygame.display.update()# updates the display
    moving_piece = retrieve_4piece()#current object
    display_piece = retrieve_4piece()
    board_range = [(0, 20), (1, 20), (2, 20), (3, 20), (4, 20), (5, 20), (6, 20), (7, 20), (8, 20), (9, 20), (10, 20)]

    taken_position = []

    clock = pygame.time.Clock() #keeps track of time
    falling_speed = 100
    time = 0
    #this will be the initial falling speed
    high_score = 1000

    run = True
    while run:
        playfield = playfield_regularmode()
        time += clock.get_rawtime()
        clock.tick()

        coordinates = convert_shape(moving_piece)

        for z in range(len(taken_position)):
            row, col = taken_position[z]
            playfield[col][row] = (255,255,255)

        for z in range(4):
            row, col = coordinates[z]#This will get the pieces in the forms (2,0),(3,0),(3,1)
            playfield[col][row] = moving_piece.colour#Converts the coordinates to the colour

        if time > falling_speed:
            time = 0
            falling_speed == falling_speed + score/100
            moving_piece.y += 1

            row, col = coordinates[0]
            if (row, col + 1) in taken_position or (row, col+1) in board_range:
                for z in range(4):
                    row, col = coordinates[z]
                    taken_position.append((row, col))
                moving_piece = display_piece
                display_piece = retrieve_4piece()
                score += (clear_rows(10, 20, playfield, taken_position)) * 10


            row, col = coordinates[1]
            if (row, col + 1) in taken_position or (row, col+1) in board_range:
                for z in range(4):
                    row, col = coordinates[z]
                    taken_position.append((row, col))
                moving_piece = display_piece
                display_piece = retrieve_4piece()
                score += (clear_rows(10, 20, playfield, taken_position)) * 10


            row, col = coordinates[2]
            if (row, col + 1) in taken_position or (row, col+1) in board_range:
                for z in range(4):
                    row, col = coordinates[z]
                    taken_position.append((row, col))
                moving_piece = display_piece
                display_piece = retrieve_4piece()
                score += (clear_rows(10, 20, playfield, taken_position)) * 10

            row, col = coordinates[3]
            if (row, col + 1) in taken_position or (row, col+1) in board_range:
                for z in range(4):
                    row, col = coordinates[z]
                    taken_position.append((row, col))
                moving_piece = display_piece
                display_piece = retrieve_4piece()
                score += (clear_rows(10, 20, playfield, taken_position)) * 10



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


            if event.type == pygame.KEYDOWN: #this will how the imputs from the keyboards are interpreted
                if event.key == pygame.K_DOWN:
                    Piece.movement(moving_piece, pygame.K_DOWN)

                if event.key == pygame.K_LEFT:
                    row1, col1 = coordinates[0]
                    row2, col2 = coordinates[1]
                    row3, col3 = coordinates[2]
                    row4, col4 = coordinates[3]
                    if (row1 - 1, col1) not in taken_position and (row2 -1 , col2) not in taken_position and (row3 - 1, col3) not in taken_position and (row4 - 1, col3) not in taken_position:
                        Piece.movement(moving_piece, pygame.K_LEFT)
                        if coordinates[0] < (0, 100) or coordinates[1] < (0, 100) or coordinates[2] < (0, 100) or coordinates[3] < (0,100):  # Checks if the piece is out of range
                            Piece.movement(moving_piece, pygame.K_RIGHT)  # It is the opposite and undoes the previous line

                if event.key == pygame.K_RIGHT:
                    row1, col1 = coordinates[0]
                    row2, col2 = coordinates[1]
                    row3, col3 = coordinates[2]
                    row4, col4 = coordinates[3]
                    if (row1 + 1, col1) not in taken_position and (row2 + 1, col2) not in taken_position and (row3 + 1, col3) not in taken_position and (row4 + 1, col4) not in taken_position:
                        Piece.movement(moving_piece, pygame.K_RIGHT)
                        if coordinates[0] > (9,-100) or coordinates[1] > (9,-100) or coordinates[2] > (9,-100) or coordinates[3] > (9, -11):#Checks if the piece is out of range
                            Piece.movement(moving_piece, pygame.K_LEFT)#It is the opposite and undoes the previous line

                if event.key == pygame.K_UP:
                    Piece.rotation(moving_piece, pygame.K_UP)
                    if coordinates[0] > (9,-100) or coordinates[1] > (9,-100) or coordinates[2] > (9,-100) or coordinates[3] > (9, -100):
                        Piece.rotation(moving_piece, pygame.K_DOWN)#It is the opposite and undoes the previous line
                    if coordinates[0] < (0,100) or coordinates[1] < (0,100) or coordinates[2] < (0,100) or coordinates[3] < (0,100):#Checks if the piece is out of range
                        Piece.rotation(moving_piece, pygame.K_DOWN)#It is the opposite and undoes the previous line


        win.fill((225,255,255))

        for i in range(len(playfield)):
            for j in range(len(playfield[i])):
                pygame.draw.rect(win, playfield[i][j], [0 + j * 25, 24 + i * 25, 25, 25], 0)


        font = pygame.font.SysFont('comicsanns', 30)
        text = font.render("Score: " + str(score), 1, (0,0,0))
        win.blit(text, (300, 100))

        text = font.render("highscore: " + str(high_score), 1, (0, 0, 0))
        win.blit(text, (300, 70))

        pygame.display.update()

        if check_lost(taken_position, 10):
            game_over_screen()

def main_DGame():
    score = 0
    pygame.init()
    # dimensions for the easy mode
    E_win_width = 600
    E_win_height = 650
    # this will be the actual window detail for the easy mode
    win = pygame.display.set_mode((E_win_width, E_win_height))# creates the window
    pygame.display.set_caption('hard mode')# name of the window
    pygame.display.update()# updates the display
    moving_piece = retrieve_5piece()#current object
    display_piece = retrieve_5piece()
    board_range = [(0, 24), (1, 24), (2, 24), (3, 24), (4, 24), (5, 24), (6, 24), (7, 24), (8, 24), (9, 24), (10, 24), (11, 24), (12, 24)]

    taken_position = []

    clock = pygame.time.Clock() #keeps track of time
    falling_speed = 300
    time = 0
    #this will be the initial falling speed
    high_score = 1000


    run = True
    while run:
        playfield = playfield_hardmode()
        time += clock.get_rawtime()
        clock.tick()

        coordinates = convert_shape(moving_piece)

        for z in range(len(taken_position)):
            row, col = taken_position[z]
            playfield[col][row] = (255,255,255)

        for z in range(5):
            row, col = coordinates[z]#This will get the pieces in the forms (2,0),(3,0),(3,1)
            playfield[col][row] = moving_piece.colour#Converts the coordinates to the colour

        if time > falling_speed:
            time = 0
            falling_speed == falling_speed + score/100
            moving_piece.y += 1

            row, col = coordinates[0]
            if (row, col + 1) in taken_position or (row, col+1) in board_range:
                for z in range(5):
                    row, col = coordinates[z]
                    taken_position.append((row, col))
                moving_piece = display_piece
                display_piece = retrieve_5piece()
                score += clear_rows(12, 24, playfield, taken_position)


            row, col = coordinates[1]
            if (row, col + 1) in taken_position or (row, col+1) in board_range:
                for z in range(5):
                    row, col = coordinates[z]
                    taken_position.append((row, col))
                moving_piece = display_piece
                display_piece = retrieve_5piece()
                score += clear_rows(12, 24, playfield, taken_position)


            row, col = coordinates[2]
            if (row, col + 1) in taken_position or (row, col+1) in board_range:
                for z in range(5):
                    row, col = coordinates[z]
                    taken_position.append((row, col))
                moving_piece = display_piece
                display_piece = retrieve_5piece()
                score += clear_rows(12, 24, playfield, taken_position)

            row, col = coordinates[3]
            if (row, col + 1) in taken_position or (row, col+1) in board_range:
                for z in range(5):
                    row, col = coordinates[z]
                    taken_position.append((row, col))
                moving_piece = display_piece
                display_piece = retrieve_5piece()
                score += clear_rows(12, 24, playfield, taken_position)

            row, col = coordinates[4]
            if (row, col + 1) in taken_position or (row, col+1) in board_range:
                for z in range(5):
                    row, col = coordinates[z]
                    taken_position.append((row, col))
                moving_piece = display_piece
                display_piece = retrieve_5piece()
                score += clear_rows(12, 24, playfield, taken_position)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


            if event.type == pygame.KEYDOWN: #this will how the imputs from the keyboards are interpreted
                if event.key == pygame.K_DOWN:
                    Piece.movement(moving_piece, pygame.K_DOWN)

                if event.key == pygame.K_LEFT:
                    row1, col1 = coordinates[0]
                    row2, col2 = coordinates[1]
                    row3, col3 = coordinates[2]
                    row4, col4 = coordinates[3]
                    row5, col5 = coordinates[4]
                    if (row1 - 1, col1) not in taken_position and (row2 -1 , col2) not in taken_position and (row3 - 1, col3) not in taken_position and (row4 - 1, col4) not in taken_position and (row5 -1, col5) not in taken_position:
                        Piece.movement(moving_piece, pygame.K_LEFT)
                        if coordinates[0] < (0, 100) or coordinates[1] < (0, 100) or coordinates[2] < (0, 100) or coordinates[3] < (0,100) or coordinates[4] < (0,100):  # Checks if the piece is out of range
                            Piece.movement(moving_piece, pygame.K_RIGHT)  # It is the opposite and undoes the previous line

                if event.key == pygame.K_RIGHT:
                    row1, col1 = coordinates[0]
                    row2, col2 = coordinates[1]
                    row3, col3 = coordinates[2]
                    row4, col4 = coordinates[3]
                    row5, col5 = coordinates[4]
                    if (row1 + 1, col1) not in taken_position and (row2 + 1, col2) not in taken_position and (row3 + 1, col3) not in taken_position and (row4 + 1, col4) not in taken_position or (row5 + 1, col5):
                        Piece.movement(moving_piece, pygame.K_RIGHT)
                        if coordinates[0] > (11,-100) or coordinates[1] > (11,-100) or coordinates[2] > (11,-100) or coordinates[3] > (11, -11) or coordinates[4] > (11, -11):#Checks if the piece is out of range
                            Piece.movement(moving_piece, pygame.K_LEFT)#It is the opposite and undoes the previous line

                if event.key == pygame.K_UP:
                    Piece.rotation(moving_piece, pygame.K_UP)
                    if coordinates[0] > (11,-100) or coordinates[1] > (11,-100) or coordinates[2] > (11,-100) or coordinates[3] > (11, -100) or coordinates[4] > (11, -100):
                        Piece.rotation(moving_piece, pygame.K_DOWN)#It is the opposite and undoes the previous line
                    if coordinates[0] < (0,100) or coordinates[1] < (0,100) or coordinates[2] < (0,100) or coordinates[3] < (0,100) or coordinates[4] < (0, 100):#Checks if the piece is out of range
                        Piece.rotation(moving_piece, pygame.K_DOWN)#It is the opposite and undoes the previous line


        win.fill((225,255,255))

        for i in range(len(playfield)):
            for j in range(len(playfield[i])):
                pygame.draw.rect(win, playfield[i][j], [0 + j * 16, 24 + i * 16, 16, 16], 0)

        font = pygame.font.SysFont('comicsanns', 30)
        text = font.render("Score: " + str(score), 1, (0,0,0))
        win.blit(text, (300, 100))

        text = font.render("highscore: " + str(high_score), 1, (0, 0, 0))
        win.blit(text, (300, 70))

        pygame.display.update()

        if check_lost(taken_position, 12):
            game_over_screen()

def main_menu():
    win_height = 700 #the window height will be 1000
    win_width = 600 #the window width will be 1200
    win = pygame.display.set_mode((win_width, win_height)) #sets the display mode
    pygame.display.set_caption('Choose difficulty') #the name of teh window

    class Button():  # all the images will follow this calss
        def __init__(self, x, y, image):
            self.image = pygame.transform.scale(image, (400, 133))# the image will scale down
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)

        def draw(self):  # this will draw the image on the screen
            win.blit(self.image, (self.rect.x, self.rect.y))
            pressed = False #flag is set
            mouse_position = pygame.mouse.get_pos() #this gets the mouse position

            if self.rect.collidepoint(mouse_position):#checks where the butter is pressed
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: #if it pressed than this will happen
                    self.clicked = True
                    pressed = True

            if pygame.mouse.get_pressed()[0] == 0:#if nothing is pressed nothing will happen
                self.clicked = False

            return pressed

    # the following allow me to load the images up
    EasyModeButton_img = pygame.image.load('IMG_EasyModeButton.png').convert_alpha()
    RegularModeButton_img = pygame.image.load('IMG_RegularModeButton.png').convert_alpha()
    HardModeButton_img = pygame.image.load('IMG_HardModeButton.png').convert_alpha()

    # i am creating the 3 buttons now
    EasyModeButton = Button(100, 100, EasyModeButton_img)
    RegularModeButton = Button(100, 300, RegularModeButton_img)
    HardModeButton = Button(100, 500, HardModeButton_img)



    run = True
    while run:
        win.fill((0, 0, 0))#black background colour
        #draws the buttons
        if EasyModeButton.draw():#if it works this module will be loaded
            main_EGame()
            run = False
        if RegularModeButton.draw():#if it works this module will be loaded
            main_RGame()
            run = False
        if HardModeButton.draw():#if it works this module will be loaded
            main_DGame()
            run = False

        for event in pygame.event.get(): #if the close button is pressed it will be terminated
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()



def game_over_screen():
    win_height = 700 #the window height will be 1000
    win_width = 600 #the window width will be 1200
    win = pygame.display.set_mode((win_width, win_height)) #sets the display mode
    pygame.display.set_caption('Game Over') #the name of teh window
    class Button():  # all the images will follow this calss
        def __init__(self, x, y, image):
            self.image = pygame.transform.scale(image, (400, 133))# the image will scale down
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)

        def draw(self):  # this will draw the image on the screen
            win.blit(self.image, (self.rect.x, self.rect.y))
            pressed = False #flag is set
            mouse_position = pygame.mouse.get_pos() #this gets the mouse position

            if self.rect.collidepoint(mouse_position):#checks where the butter is pressed
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: #if it pressed than this will happen
                    self.clicked = True
                    pressed = True

            if pygame.mouse.get_pressed()[0] == 0:#if nothing is pressed nothing will happen
                self.clicked = False

            return pressed

    playagain_img = pygame.image.load('play_again.jpg').convert_alpha()
    quit_img = pygame.image.load('QUIT.jpg').convert_alpha()
    play_again = Button(100, 100, playagain_img)
    quit = Button(100, 300, quit_img)


    run = True
    while run:
        win.fill((0,0,0))
        if play_again.draw():#if it works this module will be loaded
            main_menu()
            run = False
        if quit.draw():
            run = False

        for event in pygame.event.get(): #if the close button is pressed it will be terminated
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()



main_EGame()