import arcade
from models import World
 
SCREEN_WIDTH = 1024
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
 
 
class ShootEmWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
 
        arcade.set_background_color(arcade.color.AMAZON)
 
        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)
 
        self.dot_sprite = ModelSprite('images/shotgun.png', model=self.world.player)
 
    def update(self, delta):
        self.world.update(delta)
 
    def on_draw(self):
        arcade.start_render()
 
        self.dot_sprite.draw()
 
 
def main():
    window = ShootEmWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()