# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# import the connect_database function
# and the database_version variable
# from the database.py into the current file
# from database import connect_database, database_version
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    #  middle of screen
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.update(dt)
        player.draw(screen)
        
        # refreshes the screen; CALL THIS LAST AFTER DOING OTHER DRAW EVENTS!
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

        
if __name__ == "__main__":
    main()
