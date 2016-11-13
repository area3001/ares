import pyglet
from pyglet.window import key
import cocos
from cocos import actions, layer, sprite, scene
from cocos.director import director
import cocos.euclid as eu
import cocos.collision_model as cm
import math

MAP_SIZE = (600, 600)

VELOCITY_MAX = 400
VELOCITY_INERTIA = 3  # smaller means more inertia
VELOCITY_BRAKE_VS_SPEED = 3
VELOCITY_IMPACT_ON_TURNING = 0.0025
TURNING_SPEED = 5
VELOCITY_DECLINE = 0.995  # not touching controls means the velocity will go to zero

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

    # check if out of map
    self.position = (max(0, min(self.position[0], MAP_SIZE[0])), \
                     max(0, min(self.position[1], MAP_SIZE[1])))

# How to handle collisions
#mapcollider = mapcolliders.RectMapCollider("bounce")

# Car Actions class
class Car(actions.Move):

  def step(self, dt):
    super(Car, self).step(dt)

    rl = keyboard[key.RIGHT] - keyboard[key.LEFT]
    speed_or_brake = keyboard[key.UP] - keyboard[key.DOWN]

    radians = self.target.rotation * math.pi / 180

    # Update the speed from the perspective of the car
    try:
      speed_or_brake =   keyboard[key.UP] - VELOCITY_BRAKE_VS_SPEED * keyboard[key.DOWN] \
                       if self.target.speed > 0 else \
                         VELOCITY_BRAKE_VS_SPEED * keyboard[key.UP] -  keyboard[key.DOWN]
      self.target.speed = VELOCITY_DECLINE * (min(VELOCITY_INERTIA * speed_or_brake + self.target.speed, VELOCITY_MAX))
    except AttributeError:
      self.target.speed = math.sqrt(self.target.velocity[0]**2 + self.target.velocity[1]**2)

    velocity_x = self.target.speed * math.sin(radians)
    velocity_y = self.target.speed * math.cos(radians)
    self.target.velocity = (velocity_x, velocity_y)

    # turn the car
    print VELOCITY_IMPACT_ON_TURNING
    rl = TURNING_SPEED * rl * VELOCITY_IMPACT_ON_TURNING * abs(self.target.speed)
    rl = rl if self.target.speed > 0 else - rl
    action = actions.interval_actions.RotateBy(rl, 0)
    self.target.do(action)

    self.target.update_in_collision_manager()
    self.target.maybe_impact()

# Main class
def main():
    global keyboard
    global collision_manager

    collision_manager = cm.CollisionManagerBruteForce()

    director.init(width=MAP_SIZE[0], height=MAP_SIZE[1], autoscale=True, resizable=True)

    # Create a layer
    player_layer = layer.Layer()

    # create an obstacle and add to layer
    obstacle = CollidableSprite('sprites/obstacle.png', 200, 200, 0)
    player_layer.add(obstacle)
    obstacle.velocity = (0, 0)

    # create the car and add to layer
    car = CollidableSprite('sprites/taxi.png', 100, 100, 10)
    action = actions.interval_actions.ScaleBy(0.25, 0)
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