from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
import pygame
import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys, time


class MyWindow(QMainWindow):
    
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Coding with Andy!")
        self.initUI()

    
    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("My first label!")
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click Me!")
        self.b1.clicked.connect(self.clicked)

        
    def clicked(self):
        print("Clicked button")
        #self.label.setText("you pressed the button! \n Boom!")
        #self.update()
        #self.label.repaint() # Need this to work on Mac OS
        self.hide()
        splash_screen()

        

    def update(self):
        self.label.adjustSize()


    def reshow_page(self):
        end_game_loop()
        self.show()
        



#def clicked():
#    print("clicked")


def window():
    app = QApplication(sys.argv)
    
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

    # Taking code to the class

    '''
    win = QMainWindow()

    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("Coding with Andy!")

    label = QtWidgets.QLabel(win)
    label.setText("My first label!")
    label.move(50,50)

    b1 = QtWidgets.QPushButton(win)
    b1.setText("Click Me!")
    b1.clicked.connect(clicked) # Name of function with the ()
    '''



current_path = os.getcwd()
print(current_path)


app = QApplication(sys.argv)
win = MyWindow()
web = QWebEngineView()
web.load(QUrl("https://www.nintendo.co.uk/"))

#class Background(pygame.sprite.Sprite):
#    def __init__(self, image_file, location):
#        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
#        self.image = pygame.image.load(image_file)
#        self.rect = self.image.get_rect()
#        self.rect.left, self.rect.top = location

'''
pygame.init()
screen = pygame.display.set_mode((910, 607))

splash_screen_img = pygame.image.load(current_path+'/Images/artificial-intelligence-codes-developing-screen.jpg')

splash_screen_img.convert()
screen.fill([255, 255, 255])
rect = splash_screen_img.get_rect()
screen.blit(splash_screen_img, rect)

clock = pygame.time.Clock()
fps = 30

screen.fill([255, 255, 255])
rect = splash_screen_img.get_rect()
screen.blit(splash_screen_img, rect)
while True:

    
    pygame.display.update()
    clock.tick(fps)

clock.tick(fps)
'''

# initialize game engine
pygame.init()

#window_width = 910
#window_height = 607

animation_increment = 10
clock_tick_rate = 20


black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

# Open a window
#size = (window_width, window_height)
#screen = pygame.display.set_mode(size)

# Set title to the window
pygame.display.set_caption("Hello World!")

dead = False

clock = pygame.time.Clock()
#background_image = pygame.image.load(current_path+'/Images/artificial-intelligence-codes-developing-screen.jpg').convert()
count = 0

# Creating text


def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


def button(screen, msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)


def web_init():
    app = QApplication(sys.argv)
    web = QWebEngineView()
    web.load(QUrl("https://www.nintendo.co.uk/"))

    #########


def show_web_page():
    ###### Trying QT Web #######
    pygame.display.quit()
    reading = True
    #app, web = web_init()
    print("In show web page")
    web.show()

    while reading:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                # -> Figure out a better way to close the application
                #web.hide()
                #web_init()
                reading = False
                menu()
        #pygame.display.update()


def end_game_loop():
    dead = True
    window_width = 1024
    window_height = 640
    screen = set_screen_size(window_width, window_height)
    menu(screen)

dead = False


def menu(screen):
    print("In menu")
    pygame.display.set_caption("Main Menu")
    window_width = 1024
    window_height = 640
    #screen = screen_display
    screen = set_screen_size(window_width, window_height)

    count = 0
    dead = False

    background_image = pygame.image.load(
        current_path+'/Images/AI Brain.jpg').convert()
    #background_image = pygame.transform.scale(background_image, (1024,640))

    while(dead == False):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dead = True

        screen.blit(background_image, [0, 0])

        mouse = pygame.mouse.get_pos()

        #print(mouse)

        if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(screen, bright_green, (150, 450, 100, 50))
        else:
            pygame.draw.rect(screen, green, (150, 450, 100, 50))

        button(screen, "GO!", 150, 450, 100, 50, green, bright_green, splash_screen)
        button(screen, "Quit", 550, 450, 100, 50, red, bright_red, win.reshow_page)

        '''
        # Creating buttons
        #pygame.draw.rect(screen, (0, 255, 0), (150, 450, 100, 50))
        pygame.draw.rect(screen, (255, 0, 0), (550, 450, 100, 50)) # ('screen to place',('Colour'),(location))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects("Button 1!", smallText)
        textRect.center = ((150+(100/2)), (450+(50/2)))
        screen.blit(textSurf, textRect)
        '''
        pygame.display.update()
        clock.tick(clock_tick_rate)
        count += 1
    
    pygame.display.quit()
    pygame.display.update()



def set_screen_size(width, height):
    size = (width, height)
    return pygame.display.set_mode(size)


def splash_screen():
    pygame.init()

    # Set title to the window
    pygame.display.set_caption("Hello World!")
    count = 0
    dead = False
    window_width = 910
    window_height = 607
    #size = (window_width, window_height)
    screen = set_screen_size(window_width, window_height)

    background_image = pygame.image.load(
        current_path + '/Images/artificial-intelligence-codes-developing-screen.jpg').convert()
    while(dead == False):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dead = True

        screen.blit(background_image, [0, 0])

        pygame.display.update()
        clock.tick(clock_tick_rate)
        count += 1
        if count == 10:
            menu(screen)

#screen = set_screen_size(200, 200)

window()
