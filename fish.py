import pygame
import random

MIN_SPEED = .5
MAX_SPEED = 3

class Fish(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()

        self.image = pygame.image.load("../chomp/assets/sprites/green_fish.png").convert()
        self.image = pygame.transform.flip(self.image, True, False)

        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

        self.rect.center = (x,y)

        self.speed = random.uniform(MIN_SPEED, MAX_SPEED)

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x

    def draw(self, screen):
        screen.blit(self.image, self.rect)

fishes = pygame.sprite.Group()


class FishOpposite(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()

        self.image = pygame.image.load("../chomp/assets/sprites/green_fish.png").convert()
        # scale image if need by getting current size
        size = self.image.get_size()
        # and multiplying by scale to get desired size
        newsize = (size[0] * .5, size[1] * .5)
        # scaling up to desired size
        self.image = pygame.transform.scale(self.image, newsize)

        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()

        self.x = 0
        self.y = y

        self.rect.center = (x,y)

        self.speed = random.uniform(MIN_SPEED, MAX_SPEED)

    def update(self):
        self.x += self.speed
        self.rect.x = self.x

    def draw(self, screen):
        screen.blit(self.image, self.rect)

fishes = pygame.sprite.Group()