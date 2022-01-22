# pygame basics 

import pygame 

colors = {
    "black" : (0, 0, 0), 
    "white" : (255, 255, 255), 
    "blue" : (0, 0, 255), 
    "green" : (0, 255, 0), 
    "red" : (255, 0, 0)
}


def minimal_code():

    pygame.init() 
    pygame.display.set_caption('minimal code')

    screen = pygame.display.set_mode((1280, 768))
    running = True 

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

def draw_shapes():
    pygame.init() 
    pygame.display.set_caption('draw shapes')

    screen = pygame.display.set_mode((1280, 768))
    running = True 

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(colors['white'])
        pygame.draw.circle(screen, colors['blue'], [60, 250], 40, 1)
        pygame.draw.circle(screen, colors['blue'], [60, 100], 10, 1)
        pygame.draw.polygon(screen, colors['red'], [[60, 100], [200, 200], [300, 100]], 1)
        pygame.display.flip()
        
def draw_alpha():
    pygame.init() 
    pygame.display.set_caption('draw alpha')

    screen = pygame.display.set_mode((1280, 768))
    running = True 

    size = w, h = (400, 400)
    surface = pygame.Surface(size, pygame.SRCALPHA)
    pygame.draw.circle(surface, colors['blue'], [60, 250], 40, 1)
    pygame.draw.circle(surface, colors['blue'], [60, 100], 10, 1)
    pygame.draw.polygon(surface, (255, 0, 0, 64), [[60, 100], [100, 200], [300, 100]])

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(colors['white'])
        screen.blit(surface, (200, 200))
        pygame.display.flip()


if __name__ == "__main__":
    draw_alpha()
