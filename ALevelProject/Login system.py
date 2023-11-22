import mysql.connector  # import the correct module
from tkinter import *
import tkinter
import pygame as py
from collections import Counter

logindb = mysql.connector.connect(host='localhost', user='root', password='Dieren2013', port='3306',
                                  database='userlogin')
# this will connect my database
mycursor = logindb.cursor()  # allows me to curse through my database

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
    if 6 < count_password and count_username < 13:
        sql = "insert into loginsystem (username, password) values ('%s', '%s')"  # imports values into database
        inp = (try_username, try_password)
        # this sql statement inputs in the database
        mycursor.execute(sql, inp)  # this will execute the sql statement
        logindb.commit()  # this will make shure it is executed
        print('sign up complete, please press the ''login'' to start playing')  # this shows the user they were succesfull
    else:
        print('the passwords needs to be loner that 6 characters')

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

def easy():
    print('this will be the easy mode')
def regular():
    print('this will be the regular mode')
def hard():
    print('this will be the hard mode')


def main_menu():
    win_height = 700 #the window height will be 1000
    win_width = 600 #the window width will be 1200
    win = py.display.set_mode((win_width, win_height)) #sets the display mode
    py.display.set_caption('Choose difficulty') #the name of teh window

    class Button():  # all the images will follow this calss
        def __init__(self, x, y, image):
            self.image = py.transform.scale(image, (400, 133))# the image will scale down
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)

        def draw(self):  # this will draw the image on the screen
            win.blit(self.image, (self.rect.x, self.rect.y))
            pressed = False #flag is set
            mouse_position = py.mouse.get_pos() #this gets the mouse position

            if self.rect.collidepoint(mouse_position):#checks where the butter is pressed
                if py.mouse.get_pressed()[0] == 1 and self.clicked == False: #if it pressed than this will happen
                    self.clicked = True
                    pressed = True

            if py.mouse.get_pressed()[0] == 0:#if nothing is pressed nothing will happen
                self.clicked = False

            return pressed

    # the following allow me to load the images up
    EasyModeButton_img = py.image.load('IMG_EasyModeButton.png').convert_alpha()
    RegularModeButton_img = py.image.load('IMG_RegularModeButton.png').convert_alpha()
    HardModeButton_img = py.image.load('IMG_HardModeButton.png').convert_alpha()

    # i am creating the 3 buttons now
    EasyModeButton = Button(100, 100, EasyModeButton_img)
    RegularModeButton = Button(100, 300, RegularModeButton_img)
    HardModeButton = Button(100, 500, HardModeButton_img)

    run = True
    while run:
        win.fill((0, 0, 0))#black background colour
        #draws the buttons
        if EasyModeButton.draw():#if it works this module will be loaded
            easy()
            run = False
        if RegularModeButton.draw():#if it works this module will be loaded
            regular()
            run = False
        if HardModeButton.draw():#if it works this module will be loaded
            hard()
            run = False

        for event in py.event.get(): #if the close button is pressed it will be terminated
            if event.type == py.QUIT:
                run = False

        py.display.update()
    py.quit()

load_up()
