#! usr/bin/env python

import os, sys, random
parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)

from application import projectile_behaviour, factory, game_environment

class TargetOrRobot(object):
    def __init__(self):
        self.x = 10
        self.y = 10
        self.hit_points = 4

test_environment = game_environment.TestEnvironment(0, 15, 15)
projectile_1 = factory.Projectile(2, 2, 'east')
target_or_robot = TargetOrRobot()

def test_detect_move_off_test_area_1():
    test_environment.projectiles_in_test_environment.append(projectile_1)
    projectile_behaviour.detect_move_off_test_area(projectile_1, test_environment)
    assert len(test_environment.projectiles_in_test_environment) == 1

def test_detect_move_off_test_area_2():
    projectile_1.x, projectile_1.y = 4, 4
    projectile_behaviour.detect_move_off_test_area(projectile_1, test_environment)
    assert len(test_environment.projectiles_in_test_environment) == 1

def test_detect_move_off_test_area_3():
    projectile_1.x, projectile_1.y = 10, 50
    projectile_behaviour.detect_move_off_test_area(projectile_1, test_environment)
    assert len(test_environment.projectiles_in_test_environment) == 0

def test_detect_move_off_test_area_4():
    projectile_1.x, projectile_1.y = -5, 5
    test_environment.projectiles_in_test_environment.append(projectile_1)
    projectile_behaviour.detect_move_off_test_area(projectile_1, test_environment)
    assert len(test_environment.projectiles_in_test_environment) == 0

def test_check_this_pair_collision_1():
    projectile_1.x, projectile_1.y = 5, 5
    test_environment.projectiles_in_test_environment.append(projectile_1)
    projectile_behaviour.check_this_pair_collision(projectile_1, test_environment, target_or_robot)
    assert len(test_environment.projectiles_in_test_environment) == 1

def test_check_this_pair_collision_2():
    projectile_1.x, projectile_1.y = 7, 4
    target_or_robot.x, target_or_robot.y = 7, 4
    projectile_behaviour.check_this_pair_collision(projectile_1, test_environment, target_or_robot)
    assert len(test_environment.projectiles_in_test_environment) == 0

def test_check_this_pair_collision_3():
    projectile_1.x, projectile_1.y = 2, 2
    test_environment.projectiles_in_test_environment.append(projectile_1)
    target_or_robot.x, target_or_robot.y = 3, 2
    projectile_behaviour.check_this_pair_collision(projectile_1, test_environment, target_or_robot)
    assert len(test_environment.projectiles_in_test_environment) == 1