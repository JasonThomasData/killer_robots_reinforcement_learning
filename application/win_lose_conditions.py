def target_reached(robot_x, robot_y, target_x, target_y):
    if robot_x == target_x and robot_y == target_y:
        return True
    return False

def object_destroyed(target_hit_points):
    if target_hit_points <= 0:
        return True
    return False

def fall_off_test_area(robot_x, robot_y, test_environment_wide, test_environment_high):
    if robot_x < 0 or robot_y < 0 or robot_x >= test_environment_wide or robot_y >= test_environment_high:
        return True
    return False