import arcade
import random
import math
import os

SPRITE_SCALING = 0.5
SPRITE_TARGET_SCALING = 0.3
TARGET_COUNT = 100
TARGET_SPEED = 5
BULLET_SPEED = 1

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Shoot 'Em"

INSTRUCTION = 1
GAME_RUNNING = 2
GAME_OVER = 3

class Target(arcade.Sprite):
    def reset_pos(self): 
        self.center_x = random.randrange(SCREEN_WIDTH + 20,
                                         SCREEN_WIDTH + 100)
        self.center_y = random.randrange(250,525)

    def update(self):
        self.center_x -= TARGET_SPEED
        if self.right < 0:
            self.reset_pos()


class ShootEm(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.background = arcade.load_texture(
            "./images/background.png")

        self.current_state = INSTRUCTION
        self.total_time = 31.0

        self.gun_list = None
        self.target_list = None
        self.bullet_list = None
        self.aim_list = None

        self.score = 0
        self.gun_sprite = None
        self.aim_sprite = None

        self.instruction = arcade.load_texture("images/instruction.png")
        self.gun_sound = arcade.sound.load_sound("sounds/Gun+Shot2.wav")

    def setup(self):
        self.total_time = 31.0
        self.gun_list = arcade.SpriteList()
        self.target_list = arcade.SpriteList()
        self.aim_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        self.score = 0
        self.gun_sprite = arcade.Sprite("images/shotgunv2.png")
        self.gun_sprite.center_x = SCREEN_WIDTH // 2
        self.gun_sprite.center_y = 70
        self.gun_list.append(self.gun_sprite)

        self.aim_sprite = arcade.Sprite("images/rsz_aiming.png")
        self.aim_sprite.center_x = SCREEN_WIDTH // 2
        self.aim_sprite.center_y = SCREEN_HEIGHT // 2
        self.aim_list.append(self.aim_sprite)

        for i in range(TARGET_COUNT):
            
            target = Target("images/target_red2_outline.png", SPRITE_TARGET_SCALING)
            
            target.center_x = random.randrange(SCREEN_WIDTH)
            target.center_y = random.randrange(250,525)
            
            self.target_list.append(target)

        self.set_mouse_visible(False)

    def draw_instructions_page(self):
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.instruction)

    def draw_game_over(self):
        output = "Game Over"
        arcade.draw_text(output, 300, 400, arcade.color.BLACK, 54)

        output = f"Your Score: {self.score}"
        arcade.draw_text(output, 385, 300, arcade.color.BLACK, 24)
        output = "Click to restart"
        arcade.draw_text(output, 385, 250, arcade.color.BLACK, 24)

    def draw_game(self):
        self.draw_background()
        self.gun_list.draw()
        self.target_list.draw()
        self.aim_list.draw()
        self.bullet_list.draw()
        
        seconds = int(self.total_time) % 60

        output = f"TIME: {seconds:02d}"

        arcade.draw_text(output, 400, 560, arcade.color.BLACK, 30)

        output = f"Score: {self.score}"
        arcade.draw_text(output, 15, 565, arcade.color.BLACK, 20)

    def on_draw(self):
        arcade.start_render()

        if self.current_state == INSTRUCTION:
            self.draw_instructions_page()

        elif self.current_state == GAME_RUNNING:
            self.draw_game()

        else:
            self.draw_game()
            self.draw_game_over()

    def on_mouse_press(self, x, y, button, modifiers):
        if self.current_state == INSTRUCTION:
            self.setup()
            self.current_state = GAME_RUNNING
        elif self.current_state == GAME_OVER:
            self.setup()
            self.current_state = GAME_RUNNING

        bullet = arcade.Sprite("images/bulletYellow_outline.png")

        start_x = self.gun_sprite.center_x - 10
        start_y = self.gun_sprite.center_y + 80
        bullet.center_x = start_x
        bullet.center_y = start_y

        dest_x = x
        dest_y = y

        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        bullet.angle = math.degrees(angle)

        bullet.change_x = math.cos(angle) * BULLET_SPEED
        bullet.change_y = math.sin(angle) * BULLET_SPEED

        self.bullet_list.append(bullet)
        arcade.play_sound(self.gun_sound)


    def on_mouse_motion(self, x, y, dx, dy):
        if self.current_state == GAME_RUNNING:
            self.aim_sprite.center_x = x
            self.aim_sprite.center_y = y

    def update(self, delta_time):
        if self.current_state == GAME_RUNNING:
            self.target_list.update()
            self.bullet_list.update()
            self.total_time -= delta_time

            for bullet in self.bullet_list:
                hit_list = arcade.check_for_collision_with_list(bullet, self.target_list)

                if len(hit_list) > 0:
                    bullet.kill()

                for target in hit_list:
                    target.kill()
                    self.score += 1

                if bullet.bottom > self.width or bullet.top < 0 or bullet.right < 0 or bullet.left > self.width:
                    bullet.kill()

            if int(self.total_time) == 0.0:
                self.current_state = GAME_OVER
                self.set_mouse_visible(True)
    
    def draw_background(self):
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
