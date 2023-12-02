import pygame
import random
from game_parameters import *

MIN_SPEED = .5
MAX_SPEED = 3

class Player(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()

        self.forward_image = pygame.image.load("../assets/sprites/orange_fish.png").convert()
        self.forward_image.set_colorkey((0, 0, 0))



        self.image = self.forward_image
        self.rect = self.image.get_rect()
        # rect only stores integers, so we keep track of the position separately
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.x_velocity = 0
        self.y_velocity = 0

        self.speed = random.uniform(MIN_SPEED, MAX_SPEED)

        # #double size
        # size = self.image.get_size()
        # # and multiplying by scale to get desired size
        # newsize = (size[0] * 2, size[1] * 2)
        # # scaling up to desired size
        # self.forward_image = pygame.transform.scale(self.image, newsize)
        # self.image = pygame.transform.scale(self.image, newsize)


        self.reverse_image = pygame.transform.flip(self.forward_image, True, False)
        self.upimg = pygame.transform.rotate(self.forward_image, 90)
        self.downimg = pygame.transform.rotate(self.forward_image, 270)

    def move_up(self):
        self.y_velocity = - PLAYER_SPEED
        self.image = self.upimg
    def move_down(self):
        self.y_velocity = PLAYER_SPEED
        self.image = self.downimg
    def move_left(self):
        self.x_velocity = -1 * PLAYER_SPEED
        self.image = self.reverse_image
    def move_right(self):
        self.x_velocity = PLAYER_SPEED
        self.image = self.forward_image
    def stop(self):
        self.y_velocity = 0
        self.x_velocity = 0

    def update(self):
        self.x += self.x_velocity
        self.y += self.y_velocity
        self.rect.x = self.x
        self.rect.y = self.y
    def draw(self, screen):
        screen.blit(self.image, self.rect)
