import pygame
import random

from .constants import BACKGROUNDS, FOOD

class Images:
    game_over: pygame.Surface
    background: pygame.Surface
    food: pygame.Surface
    
    def __init__(self) -> None:
        self.game_over = pygame.image.load(
            BACKGROUNDS[1]
        ).convert_alpha()
        self.background = pygame.image.load(
            BACKGROUNDS[0]
        ).convert_alpha()
        self.randomize_food()
        
    def randomize_food(self):
        self.food = pygame.image.load(
            random.choice(FOOD)
        ).convert_alpha()

    def scale(self, image, width, height):
        image = pygame.transform.scale(image, (width, height))

        return image
