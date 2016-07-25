def move_projectile(projectile):
    if projectile.facing == 'north':
        projectile.y += 1
    elif projectile.facing == 'east':
        projectile.x += 1
    elif projectile.facing == 'south':
        projectile.y -= 1
    elif projectile.facing == 'west':
        projectile.x -= 1

def detect_move_off_test_area(proj_i, projectile, test_environment):
    if projectile.x < 0 or projectile.y < 0 or projectile.x >= test_environment.wide or projectile.y >= test_environment.high:
        if test_environment.canvas != None:
            test_environment.canvas_shapes_to_remove.append(projectile.canvas_shape)
        if projectile in test_environment.projectiles_in_test_environment:
            test_environment.projectiles_in_test_environment.remove(projectile)

def check_this_pair_collision(projectile, test_environment, target_or_robot):
    if projectile.x == target_or_robot.x and projectile.y == target_or_robot.y:
        target_or_robot.hit_points -= 1
        test_environment.canvas_shapes_to_remove.append(projectile.canvas_shape)
        if projectile in test_environment.projectiles_in_test_environment:
            test_environment.projectiles_in_test_environment.remove(projectile)

def detect_collision(proj_i, projectile, test_environment):
    for robot in test_environment.robots_in_test_environment:
        check_this_pair_collision(projectile, test_environment, robot)
    for target in test_environment.targets_in_test_environment:
        check_this_pair_collision(projectile, test_environment, target)