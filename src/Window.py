import pygame
class Window:
    def __init__(self, caption):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600)) #Screen size
        pygame.display.set_caption(str(caption))