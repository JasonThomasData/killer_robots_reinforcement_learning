#This is the object that contains all the objects in the world - robots, projectiles, targets
class TestEnvironment:
    def __init__(self, generation_number, wide, high):
        self.wide = wide
        self.high = high
        self.generation_number = generation_number
        self.steps_this_generation = 0
        self.animation_frame_count = 0
        self.canvas = None
        self.generation_animation = None
        self.canvas_shapes_to_remove = []
        self.projectiles_in_test_environment = []
        self.targets_in_test_environment = []
        self.robots_in_test_environment = []
        self.test_area = None
        self.result_reached = False