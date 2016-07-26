from application import robot_actions, robot_sensors, robot_memory, game_environment
import random

def do_action(robot, action_to_do, config, test_environment):
    if action_to_do == 'turn_left':
        return robot_actions.turn(robot, 'left', config)
    elif action_to_do == 'turn_right':
        return robot_actions.turn(robot, 'right', config)
    elif action_to_do == 'move_forward':
        return robot_actions.move_forward(robot)
    elif action_to_do == 'move_left':
        return robot_actions.move_left(robot)
    elif action_to_do == 'move_right':
        return robot_actions.move_right(robot)
    elif action_to_do == 'move_backward':
        return robot_actions.move_backward(robot)
    elif action_to_do == 'fire_projectile':
        return robot_actions.fire_projectile(robot, test_environment, config)

def pick_random_action(config):
    return random.choice(config.available_actions)

def take_action(robot, config, database, test_environment):
    state_int = robot_sensors.get_state_int(robot, test_environment)
    if random.random() > config.random_threshold:
        action_to_do = pick_random_action(robot, config)
    else:
        action_to_do = robot_memory.get_best_next_move(config, state_int, database)
    if action_to_do == None:
        action_to_do = pick_random_action(config)
    return state_int, do_action(robot, action_to_do, config, test_environment)

def create_record(robot, state_int, action_this_turn):
    new_record = {
        'state_int': state_int,
        'action_this_turn': action_this_turn
    }
    robot.states_and_actions.append(new_record)

def save_all_states_to_db(generation_number, robot, database, steps_this_generation):
    for record in robot.states_and_actions:
        robot_memory.enter_state_move_tuple(record['state_int'], record['action_this_turn'], robot.result_value, database)
    robot_memory.save_log(generation_number, steps_this_generation, robot.result, database)