#! usr/bin/env python

import os, sys, random
parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)

from application import robot_actions, factory

#Create objects required for tests
robot_x = random.randint(1, 15 - 1)
robot_y = random.randint(1, 15 - 1)
robot_hit_points = 4
robot_facing_direction = 'east'
robot_colour = 'red'
robot_id = 1
robot = factory.Robot(robot_x, robot_y, robot_hit_points, robot_facing_direction, robot_colour, robot_id)

class ConfigApp:
    def __init__(self):
        self.available_directions = ['north', 'east', 'south', 'west']

config = ConfigApp()

#True if robot starts facing east, which has an index of 1
def test_actions_1():
    assert robot_actions.get_turn_index('east', 'right', config) == 2

def test_actions_2():
    assert robot_actions.get_turn_index('south', 'right', config) == 3

def test_actions_3():
    assert robot_actions.get_turn_index('west', 'right', config) == 0

def test_actions_4():
    assert robot_actions.get_turn_index('north', 'right', config) == 1

def test_actions_5():
    assert robot_actions.get_turn_index('east', 'left', config) == 0

def test_actions_6():
    assert robot_actions.get_turn_index('north', 'left', config) == 3

def test_actions_7():
    assert robot_actions.get_turn_index('west', 'left', config) == 2

def test_actions_8():
    assert robot_actions.get_turn_index('south', 'left', config) == 1

def test_actions_9():
    assert robot_actions.turn(robot, 'left', config) == 'turn_left'

def test_actions_10():
    assert robot_actions.turn(robot, 'right', config) == 'turn_right'

def test_actions_11():
    assert robot_actions.move_forward(robot) == 'move_forward'

def test_actions_12():
    assert robot_actions.move_backward(robot) == 'move_backward'

def test_actions_13():
    assert robot_actions.move_left(robot) == 'move_left'

def test_actions_14():
    assert robot_actions.move_right(robot) == 'move_right'