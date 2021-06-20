import sys
from math import pi
import pygame
from pendulum import double_pendulum, Pendulum

pygame.init()
width = 720
height = 1280
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Double Pendulum")
clock = pygame.time.Clock()

#Colors
sweet_pink = (255, 56, 129)

pends = []
num = 1000

for i in range(num):
    a_1 = 1.4 + i*0.0001
    a_2 = 1.4 + i*0.0001
    s = (i/num) * 100
    temp = pygame.Color((0,0,0))
    temp.hsva = (336, s, 100)
    pends.append(double_pendulum(160, 170, 1, 1, (width/2, height/2 - height/10), temp, a_1, a_2))

# single_pend = Pendulum((width/2, height/2 - height/10), 20, 300, theta= -pi/2)
    

def make_video(screen):
    _image_num = 0
    while True:
        _image_num += 1
        str_num = "000" + str(_image_num)
        file_name = "image" + str_num[-4:] + ".png"
        pygame.image.save(screen, 'video\ '.rstrip(' ') + file_name)
        yield

save_screen = make_video(screen)
video = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_v:
                video = not video

    screen.fill([0, 0, 0])
    
    for pen in pends:
        pen.update()
        pen.draw(screen)

    # single_pend.draw(screen)
    # single_pend.update()

    if video:
        next(save_screen)

    pygame.display.flip()
    clock.tick(60)
