from application import robot_memory, factory, game_environment, robot_decisions, win_lose_conditions, visual_display, projectile_behaviour, video_control
from tkinter import Tk, Canvas
import time, random, os
import config_application

def remove_destroyed_robots(test_environment):
    for robot in test_environment.robots_in_test_environment:
        if robot.hit_points <= 0:
            if test_environment.canvas != None:
                test_environment.canvas_shapes_to_remove.append(robot.canvas_shape)

def remove_destroyed_targets(test_environment):
    for target in test_environment.targets_in_test_environment:
        if target.hit_points <= 0:
            if test_environment.canvas != None:
                test_environment.canvas_shapes_to_remove.append(target.canvas_shape)

def end_this_generation(test_environment, database):
    #If there is a canvas, remove it now before next generation
    if test_environment.generation_animation != None:
        test_environment.generation_animation.destroy()

    #All robots update robot memory
    #If you're wondering, I made the robot's result null on purpose, since None will not be as easy to debug
    for robot in test_environment.robots_in_test_environment:
        print('%s, %s, %s' %(test_environment.generation_number, robot.colour, robot.result))
        if robot.result != 'null':
            robot_decisions.save_all_states_to_db(test_environment.generation_number, robot, database, test_environment.steps_this_generation)

def one_moment_in_this_generation(test_environment, config, database, scenario):
    test_environment.steps_this_generation += 1

    for robot in test_environment.robots_in_test_environment:
        state_int, action_this_turn = robot_decisions.take_action(robot, config, database, test_environment)
        scenario.check_win_conditions(test_environment, robot, config)
        robot_decisions.create_record(robot, state_int, action_this_turn)

    #The robots, above, can move once per turn, while projectiles move as many spaces per turn as the user sets in the config file
    for _ in range(config.projectiles_move_per_moment):
        test_environment.animation_frame_count += 1
        #All projectiles move, collisions detected, objects earmarked for removal from test environment
        remaining_projectiles = test_environment.projectiles_in_test_environment
        for proj_i, projectile in enumerate(remaining_projectiles):
            projectile.x, projectile.y = projectile_behaviour.move_projectile(projectile.x, projectile.y, projectile.facing)
        for proj_i, projectile in enumerate(remaining_projectiles):
            projectile_behaviour.detect_move_off_test_area(projectile, test_environment)
            projectile_behaviour.detect_collision(projectile, test_environment)

        remove_destroyed_robots(test_environment)
        remove_destroyed_targets(test_environment)

        if test_environment.generation_animation != None:
            visual_display.animate_move(test_environment, config)
            video_control.save_frame(test_environment, config)

def one_generation(generation_number, config, database, scenario):
    
    #Contains all onjects in environment - projectiles, robots and targets
    test_environment = game_environment.TestEnvironment(generation_number, config.test_area_width, config.test_area_width)
    scenario.add_objects_to_environment(test_environment, config)


    #Render test_environment every nth generation
#    if test_environment.generation_number % config.animate_on_multiple == 0 or test_environment.generation_number in config.animate_these_frames:
#        successes, total = robot_memory.retreive_statistics_total(database, config.success_string)
#        if successes != 0 and total != 0:
#            success_rate = "%.2f pc" %((successes/total)*100)
#        else:
#            success_rate = 'NA'
#        visual_display.create_animation(success_rate, test_environment, config)

#Removing these for console run

    #All robots take a turn, projectiles move
    while test_environment.result_reached == False:
        one_moment_in_this_generation(test_environment, config, database, scenario)

    end_this_generation(test_environment, database)

def process_scenario(config, database, scenario):

    print('~~~')
    print('generation_num, robot_colour, result')

    _, total_record_number = robot_memory.retreive_statistics_total(database, config.success_string)
    for generation_number in range(total_record_number, total_record_number + config.generations_to_process):
        one_generation(generation_number, config, database, scenario)
