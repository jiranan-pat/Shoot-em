import arcade
from models import World
 
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Shoot 'Em"


class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
        super().__init__(*args, **kwargs)
 
    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
 
    def draw(self):
        self.sync_with_model()
        super().draw()
 
class TargetSprite(arcade.Sprite):
    def __init__(self, model):
        self.model = model
        self.target_sprite = arcade.Sprite(
            'images/target_red2_outline.png')

    def draw(self):
        self.target_sprite.set_position(self.model.x, self.model.y)
        self.target_sprite.draw()

class BulletSprite(arcade.Sprite):
    def __init__(self, model):
        self.model = model
        self.bullet_sprite = arcade.Sprite(
            'images/bulletYellow_outline.png')

    def draw(self):
        self.bullet_sprite.set_position(self.model.x, self.model.y)
        self.bullet_sprite.draw()

class AimSprite(arcade.Sprite):
    def __init__(self, model):
        self.model = model
        self.aim_sprite = arcade.Sprite(
            'images/rsz_aiming.png')

    def draw(self):
        self.aim_sprite.set_position(self.model.x, self.model.y)
        self.aim_sprite.draw()
 
class ShootEmWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        
        self.set_mouse_visible(False)
        self.background = arcade.load_texture(
            "./images/background.png")
        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)

       
        self.gun_sprite = ModelSprite('images/shotgunv2.png', model=self.world.gun)

        self.aim_sprite = AimSprite(model=self.world.aim)
        self.bullet_sprite = BulletSprite(model=self.world.bullet)


    def draw_background(self):
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
    
    def update(self, delta):
        self.world.update(delta)
 
    def on_draw(self):
        arcade.start_render()

        self.draw_background()
        self.gun_sprite.draw()
        self.bullet_sprite.draw()
        self.aim_sprite.draw()
        output = f"Score: 0"
        arcade.draw_text(output, 15, 570, arcade.color.BLACK, 16)

    
    def on_mouse_press(self, x, y, button, modifiers):
        self.world.on_mouse_press(x, y, button, modifiers)
    
    def on_mouse_motion(self, x, y, dx, dy):
        self.world.on_mouse_motion(x, y, dx, dy)
 
 
def main():
    window = ShootEmWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()