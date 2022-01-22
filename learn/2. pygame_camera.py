# pygame의  camera는 컴퓨터에 설치된 카메라에 대한 캡처 도구이다. 

import pygame 
import pygame.camera
import sys

pygame.init() 
pygame.camera.init() 

screen = pygame.display.set_mode((640, 480))
dev_list = pygame.camera.list_cameras()
if len(dev_list) == 0:
    sys.exit(-1)

cam = pygame.camera.Camera("/dev/video0", (640, 480))
cam.start() 

while True:
    image = cam.get_image() 
    flip_image = pygame.transform.flip(image, True, False)
    screen.blit(flip_image)
    pygame.display.flip()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()