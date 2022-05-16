import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SolarSystem")

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.quit():
                run = False
    pygame.quit()

main()
