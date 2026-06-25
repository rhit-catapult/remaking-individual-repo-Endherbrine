import pygame
import sys
import random
import math


# You will implement this module ENTIRELY ON YOUR OWN!
class Ball:
    def __init__(self,screen: pygame.Surface, color, x, y, radius, speed_x, speed_y):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y
    
    def draw(self):
        pygame.draw.circle(self.screen,self.color,(self.x,self.y),self.radius)

    def move(self):
        self.y += self.speed_y
        self.x += self.speed_x

        if self.colliding_with_floor():
            self.speed_y = self.speed_y * -1
        elif self.colliding_with_ceiling():
            self.speed_y = self.speed_y * -1
        
        if self.colliding_left():
            self.speed_x = self.speed_x * -1
        elif self.colliding_right():
            self.speed_x = self.speed_x * -1
        

    def colliding_with_floor(self):
        floor_to_center = self.screen.get_height() - self.radius
        return self.y >= floor_to_center
    
    def colliding_with_ceiling(self):
        return self.y < self.radius
    
    def colliding_left(self):
        return self.x < self.radius
    
    def colliding_right(self):
        return self.x >= self.screen.get_width() - self.radius


# TODO: Create a Ball class.
# TODO: Possible member variables: screen, color, x, y, radius, speed_x, speed_y
# TODO: Methods: __init__, draw, move


def main():
    pygame.init()
    screen = pygame.display.set_mode((900, 500))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    # TODO: Create an instance of the Ball class called ball1
    balls = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                random_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                mouse_pos = pygame.mouse.get_pos()
                balls.append(Ball(screen,random_color,mouse_pos[0],mouse_pos[1],random.randint(1,10),random.randint(-6,6),random.randint(-10,10)))
            if event.type == pygame.K_r:
                balls.clear()
                
        print(balls)
        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        for ball in balls:
            ball.draw()
            ball.move()

        pygame.display.update()


main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
