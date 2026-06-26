import pygame
import random  # Note this!
import raindrop_module

class Cloud:
    def __init__(self, screen: pygame.Surface, x, y, image_filename: str):
        """ Creates a Cloud sprite that will produce Raindrop objects.  The cloud will be moving around. """
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_filename)
        self.raindrops = []

    def draw(self):
        """ Draws this sprite onto the screen. """
        self.screen.blit(self.image,(self.x,self.y))

    def rain(self, amount):
        """ Adds a Raindrop to the array of raindrops so that it looks like the Cloud is raining. """
        for i in range(amount):
            self.raindrops.append(raindrop_module.Raindrop(self.screen,random.randint(self.x,self.x + 300),random.randint(self.y,self.y+100)))