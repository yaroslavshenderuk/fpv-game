import pygame
import math
import sys

FPS = 60

run = True

score = 0

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 100
    
    def input(self, event, keys, delta) -> None:
        if keys[pygame.K_UP]:
            self.x -= self.speed * delta

def main() -> int:
    global run

    pygame.init()

    pygame.display.set_caption("FPV Game")
    pygame.display.set_icon(pygame.image.load("data/icon.png"))
    screen = pygame.display.set_mode((600, 600))

    clock = pygame.time.Clock()

    while run:
        delta = clock.get_time() / 1000
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                print(delta)
        
        screen.fill("#25ae33")

        pygame.display.flip()

        clock.tick(FPS)
    
    pygame.quit()

    return 0

if __name__ == "__main__":
    sys.exit(main())