# scene 
# - bounds 
# - camera
#   - zoom in / out 
#   - move

import math
import pygame
import scene.shape

class Scene: 
    def __init__(self, sw, sh, lx, ly, rx, ry): 
        self.sw = sw  # surface width 
        self.sh = sh  # surface height 
        self.lx = lx  # left bound x
        self.ly = ly  # left bound y 
        self.rx = rx  # right bound x 
        self.ry = ry  # right bound y
        self.surface = pygame.Surface((sw, sh), pygame.SRCALPHA)
        self.scale = 1.0
        self.pan_x = 0
        self.pan_y = 0
        self.shapes = {}

    def attach(self, name, shape):
        self.shapes[name] = shape

    def detach(self, name):
        del self.shapes[name]

    def find(self, name):
        return self.shapes[name]

    def zoom(self, value): 
        self.scale *= value
        self.scale = max(0.05, self.scale)

    def locate(self, x, y):
        self.pan_x = x 
        self.pan_y = y

    def pan(self, dx, dy):
        self.pan_x += dx 
        self.pan_y += dy

    def draw(self, screen): 
        self.surface.fill(scene.shape.Color.WHITE)
        self._draw_shapes()
        screen.blit(self.surface, (0, 0))

    def _draw_shapes(self):
        for key in self.shapes: 
            shape = self.shapes[key]
            x = (shape.transform.x - (self.lx+self.pan_x)) * self.scale
            y = (shape.transform.y - (self.ly+self.pan_y)) * self.scale
            shape.draw(self.surface, x, y, self.scale)

if __name__ == "__main__" : 
    print('scene module')