import random
from application import factory, win_lose_conditions

#This object will not contain any states. Those are in the config module

class DestroyTargetScenario(object):
    
    def add_objects_to_environment(self, test_environment, config):
        self.add_target_to_environment(test_environment)
        self.add_robot_to_environment(test_environment, config)

    def add_target_to_environment(self, test_environment):
        #For robot to reach/destroy
        target_x = random.randint(1, test_environment.wide - 2) #Ensures always inside test_environment upon initialisation
        target_y = random.randint(1, test_environment.high - 2)
        target = factory.Target(target_x, target_y, 'blue')
        test_environment.targets_in_test_environment.append(target)

    def add_robot_to_environment(self, test_environment, config):
        #A single agent
        robot_x = random.randint(1, test_environment.wide - 2) #Ensures always inside test_environment upon initialisation
        robot_y = random.randint(1, test_environment.high - 2)
        target = test_environment.targets_in_test_environment[0]
        #Now, check if the robot is on its target initially, if so, do this again
        if target.x == robot_x and target.y == robot_y:
            self.add_robot_to_environment(test_environment, config)
            return #The function will run again, but only once more
        starting_direction = random.choice(config.available_directions)
        colour = 'red'
        id_number = 1
        robot = factory.Robot(robot_x, robot_y, config.robot_starting_health, starting_direction, colour, id_number)
        robot.target = target
        test_environment.robots_in_test_environment.append(robot)

    def check_win_conditions(self, test_environment, robot, config):
        if win_lose_conditions.target_destroyed(robot.target.hit_points) == True:
            robot.result = config.success_string
            robot.result_value = 1
            test_environment.result_reached = True
        if win_lose_conditions.target_reached(robot.x, robot.y, robot.target.x, robot.target.y) == True:
            robot.result = 'reached_target'
            robot.result_value = -1
            test_environment.result_reached = True
        if win_lose_conditions.fall_off_test_area(robot.x, robot.y, test_environment.wide, test_environment.high) == True:
            robot.result = 'fell_off'
            robot.result_value = -1
            test_environment.result_reached = True
            #move this to the win_lose_condition module
        if test_environment.steps_this_generation >= config.test_area_width * config.test_area_width * config.max_moves_modifier:
            robot.result = 'too_many_steps'
            robot.result_value = -1
            test_environment.result_reached = True