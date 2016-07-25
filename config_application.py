import sqlite3

class ConfigCommon(object):
    def __init__(self):
        self.test_area_width = 15
        self.robot_starting_health = 4
        self.available_directions = ['north', 'east', 'south', 'west']
        self.render_spaces_width = 48      #Robot, target, test_area spaces width
        self.robot_arc_extent = 270      #Out of 360. Robots have a gap missing on their front sides
        self.robot_arc_start = 45

class ConfigChasingTarget(ConfigCommon):
    def __init__(self):
        ConfigCommon.__init__(self)
        self.generations_to_process = 1200    #The number of tests to run over to generate the robot memory
        self.random_threshold = 1      #If a random number is higher than this, do a random action - not used so far, consider removing
        self.max_moves_modifier = 1.5      #This many times larger than the test_area's area, which is test_area_width ^ 2
        self.database_location = 'database/chasing_target.db'
        self.animate_on_multiple = 500      #Animate on the nth generation
        self.animate_these_frames = [10, 20, 30, 40, 50, 75, 100, 125, 150, 200, 250, 300, 400]      #Animate on the these generations
        self.animation_folder = 'animation/chasing_target/'
        self.available_actions = ['turn_left', 'turn_right', 'move_forward']
        self.success_string = 'reached_target'
        self.projectiles_move_per_moment = 1

class ConfigDestroyTarget(ConfigCommon):
    def __init__(self):
        ConfigCommon.__init__(self)
        self.generations_to_process = 1200      #The number of tests to run over to generate the robot memory
        self.random_threshold = 1      #If a random number is higher than this, do a random action - not used so far, consider removing
        self.max_moves_modifier = 1.5      #This many times larger than the test_area's area, which is test_area_width ^ 2
        self.database_location = 'database/destroy_target.db'
        self.animate_on_multiple = 500      #Animate on the nth generation
        self.animate_these_frames = [10, 20, 30, 40, 50, 75, 100, 125, 150, 200, 250, 300, 400]      #Animate on the these generations
        self.animation_folder = 'animation/destroy_target/'
        self.available_actions = ['turn_left', 'turn_right', 'fire_projectile',
                                'move_forward', 'move_left', 'move_right']
        self.success_string = 'target_destroyed'
        self.projectiles_move_per_moment = 3

class ConfigKillerBots(ConfigCommon):
    def __init__(self):
        ConfigCommon.__init__(self)
        self.generations_to_process = 2000     #The number of tests to run over to generate the robot memory
        self.random_threshold = 1      #If a random number is higher than this, do a random action - not used so far, consider removing
        self.max_moves_modifier = 1.5      #This many times larger than the test_area's area, which is test_area_width ^ 2
        self.database_location = 'database/killer_bots.db'
        self.animate_on_multiple = 50      #Animate on the nth generation
        self.animate_these_frames = [5, 10, 25, 75]      #Animate on the these generations
        self.animation_folder = 'animation/killer_bots/'
        self.available_actions = ['turn_left', 'turn_right', 'fire_projectile',
                                'move_forward', 'move_left', 'move_right']
        self.success_string = 'this_bot_destroyed_target'
        self.projectiles_move_per_moment = 3

class DatabaseConfig(object):
    def __init__(self, config):
        self.robot_memory = sqlite3.connect(config.database_location, timeout=20)
        self.cursor = self.robot_memory.cursor()