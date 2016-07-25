import random 
from application import factory, projectile_behaviour

#Take action, one per turn
def get_turn_index(robot_facing, turn_direction, config):
    current_facing_index = config.available_directions.index(robot_facing)
    if turn_direction == 'left':
        if current_facing_index == 0:
            return 3
        else:
            return current_facing_index - 1
    else:
        if current_facing_index == 3:
            return 0
        else:
            return current_facing_index + 1

def turn(robot, turn_direction, config):
    turn_index = get_turn_index(robot.facing, turn_direction, config)
    robot.facing = config.available_directions[turn_index]
    return 'turn_%s' %(turn_direction)

def move_forward(robot):
    if robot.facing == 'north':
        robot.y += 1
    elif robot.facing == 'east':
        robot.x += 1
    elif robot.facing == 'south':
        robot.y -= 1
    elif robot.facing == 'west':
        robot.x -= 1
    return 'move_forward'

def move_backward(robot):
    if robot.facing == 'north':
        robot.y -= 1
    elif robot.facing == 'east':
        robot.x -= 1
    elif robot.facing == 'south':
        robot.y += 1
    elif robot.facing == 'west':
        robot.x += 1
    return 'move_backward'

def move_left(robot):
    if robot.facing == 'north':
        robot.x -= 1
    elif robot.facing == 'east':
        robot.y += 1
    elif robot.facing == 'south':
        robot.x += 1
    elif robot.facing == 'west':
        robot.y -= 1
    return 'move_left'

def move_right(robot):
    if robot.facing == 'north':
        robot.x += 1
    elif robot.facing == 'east':
        robot.y -= 1
    elif robot.facing == 'south':
        robot.x -= 1
    elif robot.facing == 'west':
        robot.y += 1
    return 'move_right'

def fire_projectile(robot, test_environment, config):
    new_projectile = factory.Projectile(robot.x, robot.y, robot.facing)
    #projectile_behaviour.move_projectile(new_projectile) #It will never hit the shooter
    test_environment.projectiles_in_test_environment.append(new_projectile)
    return 'fire_projectile'