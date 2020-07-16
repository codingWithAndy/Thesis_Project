from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
import os
import sys
import pygame
from PyQt5.QtGui import *

current_path = os.getcwd()
print(current_path)


app = QApplication(sys.argv)
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

def hide_display():
    pygame.display.quit()


# Creating text
def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


def button(msg, x, y, w, h, ic, ac, action=None):
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
    


def menu():
    print("In menu")
    pygame.display.set_caption("Main Menu")
    window_width = 1024
    window_height = 640
    screen = set_screen_size(window_width, window_height)

    count = 0
    dead = False
    
    background_image = pygame.image.load(current_path+'/Images/AI Brain.jpg').convert()
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

        button("GO!", 150, 450, 100, 50, green, bright_green, splash_screen)
        button("Quit", 550, 450, 100, 50, red, bright_red, hide_display)

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


def set_screen_size(width,height):
    size = (width, height)
    return pygame.display.set_mode(size)

def splash_screen():
    count = 0
    dead = False
    window_width = 910
    window_height = 607
    #size = (window_width, window_height)
    screen = set_screen_size(window_width,window_height)
    background_image = pygame.image.load(current_path + '/Images/artificial-intelligence-codes-developing-screen.jpg').convert()
    while(dead == False):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dead = True

        screen.blit(background_image, [0, 0])

        pygame.display.update()
        clock.tick(clock_tick_rate)
        count += 1
        if count == 10:
            menu()

screen = set_screen_size(200,200)
splash_screen()

print("I am out!")
#quit()
