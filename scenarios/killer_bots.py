import random
from application import factory, win_lose_conditions

#This object will not contain any states. Those are in the config module

class KillerBotsScenario(object):
    
    def add_objects_to_environment(self, test_environment, config):
        self.add_first_robot_to_environment(test_environment, config)
        self.add_second_robot_to_environment(test_environment, config)
        robot_1 = test_environment.robots_in_test_environment[0]
        robot_2 = test_environment.robots_in_test_environment[1]
        robot_1.target = robot_2
        robot_2.target = robot_1

    def add_first_robot_to_environment(self, test_environment, config):
        #A single agent
        robot_x = random.randint(1, test_environment.wide - 2) #Ensures always inside test_environment upon initialisation
        robot_y = random.randint(1, test_environment.high - 2)
        #Now, check if the robot is on its target initially, if so, do this again
        starting_direction = random.choice(config.available_directions)
        colour = 'red'
        id_number = 1
        robot = factory.Robot(robot_x, robot_y, config.robot_starting_health, starting_direction, colour, id_number)
        test_environment.robots_in_test_environment.append(robot)

    def add_second_robot_to_environment(self, test_environment, config):
        #A single agent
        robot_x = random.randint(1, test_environment.wide - 2) #Ensures always inside test_environment upon initialisation
        robot_y = random.randint(1, test_environment.high - 2)
        #Now, check if the robot is on its target initially, if so, do this again
        target = test_environment.robots_in_test_environment[0]
        if target.x == robot_x and target.y == robot_y:
            self.add_second_robot_to_environment(test_environment, config)
            return #The function will run again, but only once more
        starting_direction = random.choice(config.available_directions)
        colour = 'blue'
        id_number = 2
        robot = factory.Robot(robot_x, robot_y, config.robot_starting_health, starting_direction, colour, id_number)
        test_environment.robots_in_test_environment.append(robot)

    def check_win_conditions(self, test_environment, robot, config):
        if win_lose_conditions.object_destroyed(robot.target.hit_points) == True:
            robot.result = config.success_string
            robot.result_value = 2
            test_environment.result_reached = True
        if win_lose_conditions.object_destroyed(robot.hit_points) == True:
            robot.result = 'this_bot_destroyed_by_opponent'
            robot.result_value = -2
            test_environment.result_reached = True
        if win_lose_conditions.target_reached(robot.x, robot.y, robot.target.x, robot.target.y) == True:
            robot.result = 'bots_collided'
            robot.result_value = -1
            test_environment.result_reached = True
        if win_lose_conditions.fall_off_test_area(robot.x, robot.y, test_environment.wide, test_environment.high) == True:
            robot.result = 'this_bot_fell_off'
            robot.result_value = -1
            test_environment.result_reached = True
            #move this to the win_lose_condition module
        if test_environment.steps_this_generation >= config.test_area_width * config.test_area_width * config.max_moves_modifier:
            robot.result = 'too_many_steps'
            robot.result_value = -1
            test_environment.result_reached = True