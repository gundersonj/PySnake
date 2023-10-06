import pygame
import random

from .constants import GAME_BACKGROUNDS, GAME_OVER_BACKGROUNDS, FOOD

class Images:
    game_over: pygame.Surface
    background: pygame.Surface
    food: pygame.Surface
    
    def __init__(self) -> None:
        self.game_over = pygame.image.load(
            GAME_OVER_BACKGROUNDS[0]
        ).convert_alpha()
        self.randomize_background()
        self.randomize_food()

    def randomize_background(self):
        self.background = pygame.image.load(
            random.choice(GAME_BACKGROUNDS)
        ).convert_alpha()
        
    def randomize_food(self):
        self.food = pygame.image.load(
            random.choice(FOOD)
        ).convert_alpha()

    def scale(self, image, width, height):
        image = pygame.transform.scale(image, (width, height))

        return image
