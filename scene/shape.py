import pygame
import math

class Color:
    '''
    Color class to represent r, g, b, a
    '''
    BLACK = (0, 0, 0) 
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255) 
    GREEN = (0, 255, 0) 
    RED = (255, 0, 0)

    def __init__(self):
        self.r = 0
        self.g = 0
        self.b = 0
        self.a = 255

    def __init__(self, r, g, b, a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

class Transform: 
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rx = 0
        self.ry = 0
        self.scale = 1
        pass

    def rotate(self, inc_rx, inc_ry):
        self.rx += inc_rx
        self.ry += inc_ry

    def locate(self, x, y):
        self.x = x 
        self.y = y

    def move(self, dx, dy):
        self.x += dx 
        self.y += dy

    def scale(self, sc): 
        self.scale = sc

class Shape: 

    def __init__(self, width, height, color):
        self.width = width 
        self.height = height
        self.color = color
        self.cx = width / 2
        self.cy = height / 2
        self.transform = Transform()
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

    def draw(self, surface):
        pass

    def draw(self, surface, x, y, scale):
        pass

class Circle(Shape): 
    def __init__(self, width, height, color, radius, fill=1): 
        super().__init__(width, height, color)
        self.radius = radius 
        self.fill = fill
        self.thick = self.radius * self.fill

    def draw(self, surface):
        pygame.draw.circle(
            self.surface, 
            self.color, 
            [self.cx, self.cy], 
            self.radius, 
            math.ceil(self.thick)+1)
        surface.blit(self.surface, (self.transform.x, self.transform.y))

    def draw(self, surface, x, y, scale):
        pygame.draw.circle(
            self.surface, 
            self.color, 
            [self.cx, self.cy], 
            self.radius, 
            math.ceil(self.thick)+1)
        
        w = self.width * scale 
        h = self.height * scale
        ns = pygame.transform.scale(self.surface, (w, h))
        surface.blit(ns, (x, y))

class Rect(Shape): 
    def __init__(self, width, height, color, fill=1): 
        super().__init__(width, height, color)
        self.fill = fill
        self.thick = self.width * self.fill

    def draw(self, surface):
        pygame.draw.rect(
            self.surface, 
            self.color, 
            [0, 0, self.width, self.height],
            math.ceil(self.thick)+1)
        surface.blit(self.surface, (self.transform.x, self.transform.y))

    def draw(self, surface, x, y, scale):
        pygame.draw.rect(
            self.surface, 
            self.color, 
            [0, 0, self.width, self.height],
            math.ceil(self.thick)+1)
        
        w = self.width * scale 
        h = self.height * scale
        ns = pygame.transform.scale(self.surface, (w, h))
        surface.blit(ns, (x, y))