import random

TARGET_SPEED = 5
BULLET_SPEED = 5

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

class Bullet:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = 70

class Fire:
    pass

class Aim:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y


 
class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.gun = Gun(self, width // 2, height // 2)
        self.bullet = Bullet(self, width // 2, height // 2)
        self.aim = Aim(self, width // 2, height // 2)


    def on_mouse_motion(self, x, y, dx, dy):
        self.aim.x = x
        self.aim.y = y

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def update(self, delta):
        self.gun.update(delta)

    


