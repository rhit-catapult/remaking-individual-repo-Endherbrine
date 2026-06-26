import pygame
import sys
import time  # Note this!
import hero_module
import cloud_module

def main():
    """ Main game loop that creates the sprite objects, controls interactions, and draw the screen. """
    pygame.init()

    pygame.display.set_caption("Rainy Day")
    screen = pygame.display.set_mode((1000,600))

    #Variables
    clock = pygame.time.Clock()
    mike = hero_module.Hero(screen,200,400,"Mike_umbrella.png","Mike.png")
    alyssa = hero_module.Hero(screen,700,400,"Alyssa_umbrella.png","Alyssa.png")
    cloud = cloud_module.Cloud(screen,300,50,"cloud.png")

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        #Movement of the cloud
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w]:
            cloud.y -= 5
        if pressed_keys[pygame.K_s]:
            cloud.y += 5
        if pressed_keys[pygame.K_a]:
            cloud.x -= 5
        if pressed_keys[pygame.K_d]:
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