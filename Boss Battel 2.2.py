"""
Boss Battel
"""

import arcade
import math
import random

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Boss Battel"
tid = 1
t = tid

CHARACTER_SCALING = 0.7
projektil_scaling = 0.5
PLAYER_MOVEMENT_SPEED = 7
TILE_SCALING = 0.5
player_position = (300, 400)
start_hastighed = 3
angle = 3
tryk = False
class projektil():
    def __init__(self, x,y):

        self.start_hastighed = 3
        self.angle = math.pi * 1
        self.start_x = 400
        self.start_y = 300
        x = 2
        y=2
        self.pos =x,y
        self.pos = (self.start_x ,self.start_y)
        self.tryk = False

    def on_mouse_press(self, x, y, button, modifiers):
        projektil = arcade.Sprite(":resources:gui_basic_assets/items/sword_gold.png", projektil_scaling)

    def update(self, delta_tid):
        if self.tryk:
            self.tid += delta_tid
            projektil_x = start_hastighed * math.cos(self.angle) * self.tid + 1
            projektil_y = start_hastighed * math.sin(self.angle) * self.tid - 0.5 * 150.82 * self.tid ** 2 + 1
            self.projektil = projektil_x - projektil_y
    def draw (self):
        x, y = self.pos
        arcade.draw_circle_filled((self.pos) ,5)
        #projektil.angle = math.degrees(self.angle)
        #print(f"projektil angle: {projektil.angle:.2f}")

        #retning_x = x
        #retning_y = y

        #self.projektil_list.append(projektil)

class GameWindow(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.scene = None
        self.player_sprite = None
        self.physics_engine = None
        self.projektil_list = None
        self.tryk = False
        arcade.set_background_color(arcade.csscolor.GREY)



    def setup(self):
        image_source = ":resources:images/animated_characters/robot/robot_fall.png"
        self.scene = arcade.Scene()
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 100
        self.scene.add_sprite("Player", self.player_sprite)
        self.projektil_list = list()
        self.projektil_list.append(projektil(player_position))

        #for i in range(100, 300, 300):
            #wall=arcade.sprite(":resources:images/tiles/stoneHalf.png", TILE_SCALING)
            #self.scene.add_sprite("Walls", wall)

        for x in range(0, 900, 64):
            wall = arcade.Sprite(":resources:images/tiles/stoneMid.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 35
            self.scene.add_sprite("Walls", wall)



        self.physics_engine = arcade.PhysicsEngineSimple(
        self.player_sprite, self.scene.get_sprite_list("Walls")
        )
        pass
    def on_key_press(self, key, modifiers):
            if key == arcade.key.UP:
                self.projektil.tryk = True
                self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
            elif key == arcade.key.DOWN:
                self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
            elif key == arcade.key.LEFT:
                self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
            elif key == arcade.key.RIGHT:
                self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
            if key == arcade.key.UP:
                self.player_sprite.change_y = -8
            elif key == arcade.key.DOWN:
                self.player_sprite.change_y = 0
            elif key == arcade.key.LEFT:
                self.player_sprite.change_x = 0
            elif key == arcade.key.RIGHT:
                self.player_sprite.change_x = 0
            pass
    def on_update(self, delta_time):
        self.physics_engine.update()
        projektil.update(self, delta_time)
        pass


    def on_draw(self):
        self.clear()
        self.scene.draw()
        projektil()


def main():
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()