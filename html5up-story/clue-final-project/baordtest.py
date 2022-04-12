import sys

import pygame
from pygame.locals import *

pygame.init()

FPS = 60

FramePerSec = pygame.time.Clock()
 
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
DISPLAYSURF = pygame.display.set_mode((1000,875))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Clue")

class Board(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("images/board.jpg")
        self.rect = self.image.get_rect()
        self.rect.center=(355,375)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class User_Cards(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/mrs. peacock.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def set_rect_center(self, x, y):
        self.rect.center = (x, y)

BOARD1 = Board()
USER_CARDS = User_Cards()

while True:     
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
     
    DISPLAYSURF.fill(WHITE)
    BOARD1.draw(DISPLAYSURF)
    # can put next two lines into a for loop to iterate through a deck of cards
    USER_CARDS.set_rect_center(70, 800)
    USER_CARDS.draw(DISPLAYSURF)
         
    pygame.display.update()
    FramePerSec.tick(FPS)
