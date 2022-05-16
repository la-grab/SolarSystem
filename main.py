import pygame

pygame.init()

SIZE = WIDTH, HEIGHT = 800, 800

pygame.display.set_caption("SolarSystem")
WIN = pygame.display.set_mode(SIZE)

YELLOW = (255, 255, 0)


class Planet:
    AU = 149.6e9 * 1000
    F = 6.77428e-11
    SCALE = 250 / AU #1 AU = 100 pixels
    TIMESTEP = 60*60*24

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2
        pygame.draw.circle(win, self.color, (x,y), self.radius)


def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0 , 0 , 30, YELLOW, 1.98892*10**30)
    sun.sun = True

    planets = [sun]

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.draw(WIN)

        pygame.display.update()
    pygame.quit()


main()
