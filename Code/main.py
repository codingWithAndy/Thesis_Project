import os
import sys
import pygame

current_path = os.getcwd()
print(current_path)


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

# Open a window
#size = (window_width, window_height)
#screen = pygame.display.set_mode(size)

# Set title to the window
pygame.display.set_caption("Hello World!")

dead = False

clock = pygame.time.Clock()
#background_image = pygame.image.load(current_path+'/Images/artificial-intelligence-codes-developing-screen.jpg').convert()
count = 0

def menu():
    pygame.display.set_caption("Main Menu")
    count = 0
    dead = False
    window_width = 1024
    window_height = 640
    screen = screen = set_screen_size(window_width, window_height)
    background_image = pygame.image.load(current_path+'/Images/AI Brain.jpg').convert()
    #background_image = pygame.transform.scale(background_image, (1024,640))

    while(dead == False):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dead = True

        screen.blit(background_image, [0, 0])

        pygame.display.flip()
        clock.tick(clock_tick_rate)
        count += 1


def set_screen_size(width,height):
    size = (width, height)
    return pygame.display.set_mode(size)

def splash_screen():
    count = 0
    dead = False
    window_width = 1024
    window_height = 660
    #size = (window_width, window_height)
    screen = set_screen_size(window_width,window_height)
    background_image = pygame.image.load(current_path + '/Images/artificial-intelligence-codes-developing-screen.jpg').convert()
    while(dead == False):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dead = True

        screen.blit(background_image, [0, 0])

        pygame.display.flip()
        clock.tick(clock_tick_rate)
        count += 1
        if count == 10:
            break

splash_screen()
menu()

print("I am out!")
