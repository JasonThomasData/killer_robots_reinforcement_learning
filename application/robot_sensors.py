import math 

#Note - Using a cartesian coordinate system, so this works for a grid world where counting units starts at the bottom left hand corner

def get_target_compass_direction(robot_x, robot_y, target_x, target_y):
    
    dif_x = robot_x - target_x
    dif_y = robot_y - target_y

    target_direction_radians = math.atan2(dif_x,dif_y)
    target_direction_degrees = int(math.degrees(target_direction_radians)) + 180

    return target_direction_degrees

    #The math.degrees() function returns something between -180 and 180, but we want 0 - 360, so we add 180 
    #For an explainer on how - http://www.summitpost.org/compass-basics-an-introduction-to-orientation-and-navigation/358187


def get_direction_facing_offset(robot_facing, target_direction_degrees):
    #This takes into account the robot's facing direction
    
    if robot_facing == 'east':
        target_direction_degrees -= 90
    elif robot_facing == 'south':
        target_direction_degrees -= 180
    elif robot_facing == 'west':
        target_direction_degrees -= 270

    if target_direction_degrees <= 0:
        target_direction_degrees = 360 + target_direction_degrees

    return target_direction_degrees


def get_direction_in_buckets(target_direction_degrees):
    #We want a maximum of 16 directions
    
    if target_direction_degrees > 0 and target_direction_degrees < 45:
        return 23 #math.ceil((0+45)/2)
    elif target_direction_degrees > 45 and target_direction_degrees < 90:
        return 68 #math.ceil((0+45)/2)
    elif target_direction_degrees > 90 and target_direction_degrees < 135:
        return 113 #math.ceil((0+45)/2)
    elif target_direction_degrees > 135 and target_direction_degrees < 180:
        return 158 #math.ceil((0+45)/2)
    elif target_direction_degrees > 180 and target_direction_degrees < 225:
        return 203 #math.ceil((0+45)/2)
    elif target_direction_degrees > 225 and target_direction_degrees < 270:
        return 248 #math.ceil((0+45)/2)
    elif target_direction_degrees > 270 and target_direction_degrees < 315:
        return 293 #math.ceil((0+45)/2)
    elif target_direction_degrees > 315 and target_direction_degrees < 360:
        return 338 #math.ceil((0+45)/2)

    #The numbers in between the main 8 points - 360(N), 45(NE), 90(E), 135(SE), 180(S), 225(SW), 270(W), 315(NW) - take the median value in that range, rounded up to the nearest integer
    return target_direction_degrees


def get_target_direction_index(robot, target):
    target_direction_degrees = get_target_compass_direction(robot.x, robot.y, robot.target.x, robot.target.y)
    target_direction_offset = get_direction_facing_offset(robot.facing, target_direction_degrees)
    target_direction_buckets = get_direction_in_buckets(target_direction_offset)
    return '%03d' %(target_direction_buckets)

def get_border_touching_index(robot_x, robot_y, test_environment_wide, test_environment_high):
    borders_touching = 0
    if robot_x == 0 or robot_x == test_environment_wide - 1:
        borders_touching += 1
    if robot_y == 0 or robot_y == test_environment_high - 1:
        borders_touching += 1
    return borders_touching

def get_target_next_to_index(robot_x, robot_y, target_x, target_y):
    target_next_to = 0
    if abs(robot_x - target_x) <= 1 and abs(robot_y - target_y) <= 1:
        target_next_to = 1
    return target_next_to

def get_state_int(robot, test_environment):
    target_direction_index = get_target_direction_index(robot, robot.target)
    borders_touching_index = get_border_touching_index(robot.x, robot.y, test_environment.wide, test_environment.high)
    target_next_to_index = get_target_next_to_index(robot.x, robot.y, robot.target.x, robot.target.y)
    int_string = '%s%s%s%s%s' %(robot.id_number, target_direction_index, borders_touching_index, target_next_to_index, robot.hit_points)
    return int_string