import pygame

class Window:
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

    def create_window(self):
        window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        return window