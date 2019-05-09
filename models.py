import random
import math
import arcade

TARGET_SPEED = 5

class Gun:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = 70
 
    def update(self, delta):
        pass

class Target:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

    def update(self, delta):
        pass

class Aim:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

class World:
    STATE_FROZEN = 1
    STATE_STARTED = 2

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.state = World.STATE_FROZEN
        self.gun = Gun(self, width // 2, height // 2)
        self.aim = Aim(self, width // 2, height // 2)

    def update(self, delta):
        if self.state == World.STATE_FROZEN:
            return
        self.gun.update(delta)
        

    def on_mouse_motion(self, x, y, dx, dy):
        self.aim.x = x
        self.aim.y = y
    
    def start(self):
        self.state = World.STATE_STARTED

    def freeze(self):
        self.state = World.STATE_FROZEN

    def is_started(self):
        return self.state == World.STATE_STARTED

    



    

    


