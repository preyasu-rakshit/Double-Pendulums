import pygame
from math import pi, sin, cos

pygame.init()


class double_pendulum:
    def __init__(self, length_1, length_2, mass_1, mass_2,
                 anchor,color, theta_1=pi/4, theta_2=pi/4) -> None:
        self.lenght_1 = length_1
        self.lenght_2 = length_2
        self.mass_1 = mass_1
        self.mass_2 = mass_2
        self.anchor = anchor
        self.theta_1 = theta_1
        self.theta_2 = theta_2
        self.anchorx, self.anchory = anchor
        self.gravity = 1

        self.alpha_1 = 0
        self.alpha_2 = 0

        self.omega_1 = 0
        self.omega_2 = 0

        self.PATH = []
        self.path_len = 10

        self.color = color

    def draw(self, surface):
        x_1 = self.anchorx + self.lenght_1*sin(self.theta_1)
        y_1 = self.anchory + self.lenght_1*cos(self.theta_1)

        x_2 = x_1 + self.lenght_2*sin(self.theta_2)
        y_2 = y_1 + self.lenght_2*cos(self.theta_2)

        self.pos1 = (x_1, y_1)
        self.pos2 = (x_2, y_2)

        # if len(self.PATH) < self.path_len:
        #     self.PATH.append(self.pos2)

        # else:
        #     del self.PATH[0]
        #     self.PATH.append(self.pos2)

        pygame.draw.aaline(surface, self.color, self.anchor, self.pos1)
        pygame.draw.circle(surface, self.color, self.pos1, self.mass_1)

        pygame.draw.aaline(surface, self.color, self.pos1, self.pos2)
        pygame.draw.circle(surface, self.color, self.pos2, self.mass_2)

        # if len(self.PATH) > 2:
        #     pygame.draw.aalines(surface, self.color, False, self.PATH)

    def update(self):
        g = self.gravity

        m1 = self.mass_1
        m2 = self.mass_2

        t1 = self.theta_1
        t2 = self.theta_2

        L1 = self.lenght_1
        L2 = self.lenght_2

        v1 = self.omega_1
        v2 = self.omega_2

        num1 = -g*(2*m1 + m2)*sin(t1) - m2*g*sin(t1 - 2*t2) - 2*sin(t1 - t2)*m2*(v2*v2*L2 + v1*v1*L1*cos(t1 - t2))
        deno1 = L1*(2*m1 + m2 - m2*cos(2*t1 - 2*t2))

        num2 = 2*sin(t1 - t2)*(v1*v1*L1*(m1 + m2) + g*(m1 + m2)
                               * cos(t1) + v2*v2*L2*m2*cos(t1 - t2))
        deno2 = L2*(2*m1 + m2 - m2*cos(2*t1 - 2*t2))

        self.alpha_1 = num1/deno1
        self.alpha_2 = num2/deno2

        self.omega_1 += self.alpha_1
        self.omega_2 += self.alpha_2

        self.theta_1 += self.omega_1
        self.theta_2 += self.omega_2

        # self.omega_1 *= 0.999
        # self.omega_2 *= 0.999


class Pendulum:
    def __init__(self, anchor, mass, length, theta=pi/4) -> None:
        self.anchor = anchor
        self.anchorx, self.anchory = anchor
        self.mass = mass
        self.length = length
        self.theta = theta
        self.x = self.anchorx + (self.length*sin(self.theta))
        self.y = self.anchory + (self.length*cos(self.theta))
        self.ALPHA = 0
        self.OMEGA = 0
        self.damp_const = 0.999
        self.g = 1
        self.pos = (self.x, self.y)
        self.PATH = []
        self.path_len = 100

        self.color = (56, 255, 109)

    def draw(self, surface):
        pygame.draw.aaline(surface, self.color,
                           self.anchor, self.pos)
        pygame.draw.circle(surface, self.color,
                           self.pos, self.mass)

        if len(self.PATH) > 1:
            pygame.draw.aalines(surface, self.color, False, self.PATH)

    
    def update(self):
        # self.theta += 0.01
        self.ALPHA = -(self.g*sin(self.theta)/self.length)
        self.OMEGA += self.ALPHA
        self.theta += self.OMEGA
        self.x = self.anchorx + (self.length*sin(self.theta))
        self.y = self.anchory + (self.length*cos(self.theta))
        self.pos = (self.x, self.y)

        if len(self.PATH) < self.path_len:
            self.PATH.append(self.pos)
        else:
            del self.PATH[0]
            self.PATH.append(self.pos)

        # self.PATH.append(self.pos)
        self.OMEGA *= self.damp_const
