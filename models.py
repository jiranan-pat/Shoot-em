import random
import math
import arcade

TARGET_SPEED = 5
# BULLET_SPEED = 5

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
        self.start_x = x
        self.start_y = 70
        self.x = self.start_x
        self.y = self.start_y
    
        self.dest_x = self.x
        self.dest_y = self.y

        self.x_diff = self.dest_x - self.start_x
        self.y_diff = self.dest_y - self.start_y
        angle = math.atan2(self.y_diff, self.x_diff)
        self.angle = math.degrees(angle)

    def fire(self, angle):
        self.change_x = math.cos(self.angle) * BULLET_SPEED
        self.change_y = math.sin(self.angle) * BULLET_SPEED
        self.x += self.change_x
        self.y += self.change_y

    def update(self, delta):
        self.angle = self.next_angle
        self.fire(self.angle)

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
        self.bullet = Bullet(self, width // 2, height // 2)
        self.aim = Aim(self, width // 2, height // 2)

    def update(self, delta):
        if self.state == World.STATE_FROZEN:
            return
        self.gun.update(delta)
        self.bullet.update(delta)

    def on_mouse_motion(self, x, y, dx, dy):
        self.aim.x = x
        self.aim.y = y

    # def on_mouse_press(self, x, y, button, modifiers):
    #     if button == arcade.MOUSE_BUTTON_LEFT:
    #         self.bullet.next_angle
    
    def start(self):
        self.state = World.STATE_STARTED

    def freeze(self):
        self.state = World.STATE_FROZEN

    def is_started(self):
        return self.state == World.STATE_STARTED

    



    

    


