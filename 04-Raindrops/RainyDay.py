import pygame
import sys
import time  # Note this!
import random  # Note this!


class Raindrop:
    def __init__(self, screen: pygame.Surface, x, y):
        """ Creates a Raindrop sprite that travels down at a random speed. """
        self.screen = screen
        self.x = x
        self.y = y
        self.speed =  random.randint(5,15)

    def move(self):
        """ Move the self.y value of the Raindrop down the screen (y increase) at the self.speed. """
        self.y += self.speed
        
    def off_screen(self):
        """ Returns true if the Raindrop y value is not shown on the screen, otherwise false. """
        return self.y >= self.screen.get_height()

    def draw(self):
        """ Draws this sprite onto the screen. """
        pygame.draw.line(self.screen,(0,0,200),(self.x,self.y),(self.x,self.y + 5), 2)
        


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
            self.raindrops.append(Raindrop(self.screen,random.randint(self.x,self.x + 300),random.randint(self.y,self.y+100)))
        


def main():
    """ Main game loop that creates the sprite objects, controls interactions, and draw the screen. """
    pygame.init()

    pygame.display.set_caption("Rainy Day")
    screen = pygame.display.set_mode((1000,600))

    #Variables
    clock = pygame.time.Clock()
    mike = Hero(screen,200,400,"Mike_umbrella.png","Mike.png")
    alyssa = Hero(screen,700,400,"Alyssa_umbrella.png","Alyssa.png")
    cloud = Cloud(screen,300,50,"cloud.png")

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        #Movement of the cloud
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            cloud.y -= 5
        if pressed_keys[pygame.K_DOWN]:
            cloud.y += 5
        if pressed_keys[pygame.K_LEFT]:
            cloud.x -= 5
        if pressed_keys[pygame.K_RIGHT]:
            cloud.x += 5

        screen.fill((255,255,255))

        #Make the cloud rain and see if the rain hits the heroes
        cloud.rain(10)
        for rain in cloud.raindrops:
            rain.draw()
            rain.move()
            if mike.hit_by(rain):
                mike.last_hit_time = time.time()
            if alyssa.hit_by(rain):
                alyssa.last_hit_time = time.time()
            if rain.off_screen():
                cloud.raindrops.remove(rain)
        
        cloud.draw()
        alyssa.draw()
        mike.draw()
        
        pygame.display.update()
main()