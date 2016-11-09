import pyglet
from pyglet.window import key

import cocos
from cocos import actions, layer, sprite, scene
from cocos.director import director
import cocos.euclid as eu
import cocos.collision_model as cm

MAX_VELOCITY = 150

class CollidableSprite(cocos.sprite.Sprite):
  def __init__(self, image, cx, cy, radius):
    super(CollidableSprite, self).__init__(image)
    self.position = (cx, cy)
    self.cshape = cm.CircleShape(eu.Vector2(cx, cy), 40)

  def update_in_collision_manager(self):
    collision_manager.remove_tricky(self)
    self.cshape = cm.CircleShape(eu.Vector2(self.position[0], self.position[1]), 40)
    collision_manager.add(self)

  def maybe_impact(self):
    if collision_manager.any_near(self, 1):
      self.velocity = (- self.velocity[0], - self.velocity[1])

# How to handle collisions
#mapcollider = mapcolliders.RectMapCollider("bounce")

# Car Actions class
class Car(actions.Move):

  def step(self, dt):
    super(Car, self).step(dt)

    rl = keyboard[key.RIGHT] - keyboard[key.LEFT]
    ud = keyboard[key.UP] - keyboard[key.DOWN]

    # need to make this from the perspective of the target
    velocity_x = min(self.target.velocity[0] + 5 * rl, MAX_VELOCITY)
    velocity_y = min(self.target.velocity[1] + 5 * ud, MAX_VELOCITY)
    self.target.velocity = (velocity_x, velocity_y)

    action = actions.interval_actions.RotateBy(rl, 0)
    self.target.do(action)

    self.target.update_in_collision_manager()
    self.target.maybe_impact()

# Main class
def main():
    global keyboard
    global collision_manager

    collision_manager = cm.CollisionManagerBruteForce()

    director.init(width=1300, height=1300, autoscale=False, resizable=True)

    # Create a layer
    player_layer = layer.Layer()

    # create an obstacle and add to layer
    obstacle = CollidableSprite('sprites/obstacle.png', 200, 200, 0)
    player_layer.add(obstacle)
    obstacle.velocity = (0, 0)

    # create the car and add to layer
    car = CollidableSprite('sprites/taxi.png', 100, 100, 10)
    action = actions.interval_actions.ScaleBy(0.5, 0)
    car.do(action)

    player_layer.add(car)
    car.velocity = (0, 0)

    # Set the sprite's movement class.
    car.do(Car())

    # Create a scene and set its initial layer.
    main_scene = scene.Scene(player_layer)

    # collisions
    collision_manager.add(car)
    collision_manager.add(obstacle)

    # Attach a KeyStateHandler to the keyboard object.
    keyboard = key.KeyStateHandler()
    director.window.push_handlers(keyboard)

    # Play the scene in the window.
    director.run(main_scene)

if __name__ == '__main__':
    main()