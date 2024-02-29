import random as r
from re import L
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
import ground


class World():
    def __init__(self, xdim, ydim, ground_height):
        self.xdim = xdim
        self.ydim = ydim
        self.ground_height = ground_height


class Player():
    def __init__(self, name, xpos, ypos, health=100):
        self.name = name
        self.xpos = xpos
        self.ypos = ypos
        self.health = health
        self.cannonAng = 0
        self.cannonPow = 0

    def __repr__(self):
        return self.name

    def getPos(self):
        return (self.xpos, self.ypos)

    def moveX(self, step):
        self.xpos += step

    def moveY(self, step):
        self.ypos += step

    def moveCannon(self, ang):
        self.cannonAng = ang

    def setPower(self, pow):
        self.cannonPow = pow


class Particle():
    def __init__(self, xpos, ypos, xvel, yvel) -> None:
        self.xpos = xpos
        self.ypos = ypos
        self.xvel = xvel
        self.yvel = yvel

    def update(self, timestep):
        g = -9.81

        self.xpos += timestep * self.xvel

        self.ypos += timestep * self.yvelv
        self.yvel += timestep * g


class PhysicsSim():
    def __init__(self, timestep) -> None:
        self.timestep = timestep
        self.particles = []
        self.Ground = []

    def createGround(self, world):
        x = np.array([i for i in range(world.xdim)])
        y = np.array(ground.create_ground(
            [world.ground_height, world.ground_height], world.xdim))
        y = 0.8 * world.ydim * y
        self.Ground = [(x[i], int(y[i])) for i in x]

    def createParticle(self, xpos, ypos, xvel, yvel):
        self.particles.append(Particle(xpos, ypos, xvel, yvel))

    def update(self):
        for particle in self.particles:
            particle.update(self.timestep)

    def checkGroundCollision(self, particle):
        if particle.ypos == self.Ground[particle.xpos][1]:
            return True
        else:
            return False

    def collideParticle(self):
        for i, particle in enumerate(self.particles):
            if self.checkGroundCollision(particle) == True:
                self.particles.pop(i)


# Object creation

world = World(700, 700, 100)
a = PhysicsSim(5)
a.createGround(world)

border = 20
seed1 = r.randint(0+border, world.xdim-border)
seed2 = r.randint(0+border, world.xdim-border)
seed3 = r.randint(0+border, world.xdim-border)
p1 = Player('SilenceInTheBox', a.Ground[seed1][0], a.Ground[seed1][1])
p2 = Player('Snotspoon', a.Ground[seed2][0], a.Ground[seed2][1])
p3 = Player('ToastToasty', a.Ground[seed3][0], a.Ground[seed3][1])


def pressed_button():
    name = e1.get()
    p1.name = name


m0 = Tk()
l1 = Label(m0, text='Name:')
e1 = Entry(m0, width=20)
b1 = Button(m0, text='Enter', command=pressed_button)

l1.grid(row=0, column=0)
e1.grid(row=1, column=0, sticky='w')
b1.grid(row=1, column=1, sticky='e')

m0.mainloop()
# Visualisation

m1 = Tk()

label = Label(m1, text='Tank Game --- v. 0.1')
label.pack()

canvas = Canvas(m1, width=world.xdim, height=world.ydim)
canvas.pack()

frame = Frame(m1,)

button1 = Button(frame, text='1', width=world.xdim//16)
button2 = Button(frame, text='2', width=world.xdim//16)

button1.pack(side=LEFT)
button2.pack(side=RIGHT)
frame.pack()


for i, pos in enumerate(a.Ground[:-1]):
    # print(pos)
    x1 = a.Ground[i][0]
    y1 = world.ydim-abs(a.Ground[i][1])
    x2 = a.Ground[i+1][0]
    y2 = world.ydim-abs(a.Ground[i+1][1])
    # print(x1,y1,x2,y2)
    canvas.create_line(x1, y1, x2, y2)

# print(p1.getPos())
# print(p2.getPos())
canvas.create_rectangle(p1.getPos()[0]-5, world.ydim-p1.getPos()[1], p1.getPos()[
                        0]+5, world.ydim-p1.getPos()[1]-10, fill='green')
canvas.create_rectangle(p2.getPos()[0]-5, world.ydim-p2.getPos()
                        [1], p2.getPos()[0]+5, world.ydim-p2.getPos()[1]-10, fill='red')
print(p1.name)

Event()
m1.mainloop()
