import pygame
import time  # Note this!
import sys

class Hero:
    def __init__(self, screen: pygame.Surface, x, y, with_umbrella_filename: str, without_umbrella_filename: str):
        """ Creates a Hero sprite (Mike) that does not move. If hit by rain he'll put up his umbrella. """
        self.screen = screen
        self.x = x
        self.y = y
        self.image_umbrella = pygame.image.load(with_umbrella_filename)
        self.image_no_umbrella = pygame.image.load(without_umbrella_filename)
        self.last_hit_time = 0

    def draw(self):
        """ Draws this sprite onto the screen. """
        if time.time() > self.last_hit_time + 1:
            self.screen.blit(self.image_no_umbrella,(self.x,self.y))
        else:
            self.screen.blit(self.image_umbrella,(self.x,self.y))
        

    def hit_by(self, raindrop):
        """ Returns true if the given raindrop is hitting this Hero, otherwise false. """
        hit_box = pygame.Rect(self.x,self.y,
                              self.image_umbrella.get_width(),self.image_umbrella.get_height())
        return hit_box.collidepoint(raindrop.x,raindrop.y)        

def main():
    """ Main game loop that creates the sprite objects, controls interactions, and draw the screen. """
    pygame.init()

    pygame.display.set_caption("Hero Module")
    screen = pygame.display.set_mode((1000,600))

    #Variables
    clock = pygame.time.Clock()
    mike = Hero(screen,200,400,"Mike_umbrella.png","Mike.png")
    alyssa = Hero(screen,700,400,"Alyssa_umbrella.png","Alyssa.png")

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        #Movement of the cloud

        screen.fill((255,255,255))

        #Make the cloud rain and see if the rain hits the heroes
        alyssa.draw()
        mike.draw()
        
        pygame.display.update()

if __name__ == "__main__":
    main()