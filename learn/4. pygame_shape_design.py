# shape. the drawing primitives of play simulator. 

import pygame

class Transform:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rx = 0
        self.ry = 0
        self.scale = 1
        pass

    def rotate(self, x, y):
        pass

    def locate(self, x, y):
        pass

    def move(self, dx, dy):
        pass

class Curve:
    def __init__(self):
        pass

class LinearCurve(Curve): 
    def __init__(self):
        pass 

class Color:

    def __init(self):
        self.r = 0
        self.g = 0
        self.b = 0
        self.a = 1

class Shape:

    def __init__(self):
        self.transform = Transform()

    def draw(self, surface : pygame.Surface):
        pass

class CircleShape(Shape):

    def __init__(self):
        pass

class RectShape(Shape):

    def __init__(self):
        pass

class PolyShape(Shape):

    def __init__(self):
        pass

class TriShape(PolyShape):

    def __init__(self):
        pass

class AnimShape(Shape):

    def __init__(self):
        pass

class Particle:

    def __init__(self):
        pass


class Camera:

    def __init__(self):
        pass


class Scene: 

    def __init__(self):
        pass

    def attach(self, shape : Shape):
        pass

    def detach(self, id):
        pass


class SectorScene:

    def __init__(self):
        pass


# the above classes are the most of the tools to build 