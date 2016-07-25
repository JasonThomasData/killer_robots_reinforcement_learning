#Agents performing tasks
class Robot:
    def __init__(self, start_x, start_y, health, facing, colour, id_number):
        self.x = start_x
        self.y = start_y
        self.facing = facing
        self.hit_points = health
        self.states_and_actions = []
        self.target = None
        self.canvas_shape = None
        self.result = 'null'
        self.result_value = 0
        self.colour = colour
        self.id_number = id_number

#Robot to shoot or move towards
class Target:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour
        self.canvas_shape = None
        self.hit_points = 4

#Robot fires these
class Projectile:
    def __init__(self, x, y, facing, config):
        self.x = x
        self.y = y
        self.facing = facing
        self.attack_power = 1
        self.colour = 'black'
        self.canvas_shape = None
        self.hit_points = 1