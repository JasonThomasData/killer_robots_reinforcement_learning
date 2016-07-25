import sqlite3, random, time

def make_record_map(record_from_db):
    record_dict = {
        'turn_left': record_from_db[0],
        'turn_right': record_from_db[1],
        'move_forward': record_from_db[2],
        'move_backward': record_from_db[3],
        'move_left': record_from_db[4],
        'move_right': record_from_db[5],
        'fire_projectile': record_from_db[6]
    }
    return record_dict

def get_best_move_choice(config, record_from_db):
    record_map = make_record_map(record_from_db)
    approved_record_map = {}
    for key, value in record_map.items():
        if key in config.available_actions:
            approved_record_map[key] = value
    best_choice_value = max(list(approved_record_map.values()))
    move_choices = []
    for key, value in approved_record_map.items():
        if value == best_choice_value:
            move_choices.append(key)
    return random.choice(move_choices)

def get_best_next_move(config, state_int, database):
    record_from_db = retreive_record(state_int, database)
    if record_from_db == None:
        return record_from_db
    else:
        return get_best_move_choice(config, record_from_db)

#Prepare a record for the records table
def enter_state_move_tuple(state_int, action_this_turn, result_value, database):
    record_from_db = retreive_record(state_int, database)
    if record_from_db == None:
        new_record = (0, 0, 0, 0, 0, 0, 0)
        record_map = make_record_map(new_record)
        insert_record(state_int, database)
    else:
        record_map = make_record_map(record_from_db)
    record_map[action_this_turn] += result_value
    update_record(record_map, state_int, database)

def retreive_record(state_int, database):
    try:
        database.cursor.execute("SELECT turn_left, turn_right, move_forward, move_backward, move_left, move_right, fire_projectile FROM records WHERE state_int=?", [state_int])
        for record in database.cursor:
            return record
        return None

    except sqlite3.OperationalError: #occurs when tables don't exist
        create_record_table(database)
        return None

def retreive_statistics_total(database, success_string):
    try:
        win_record_number = database.cursor.execute("SELECT Count(*) FROM log WHERE result_of_generation=?", [success_string]).fetchone()[0]
        total_record_number = database.cursor.execute("SELECT Count(*) FROM log").fetchone()[0]
        return win_record_number, total_record_number

    except sqlite3.OperationalError: #occurs when tables don't exist
        create_log_table(database)
        return 0, 0

def retreive_statistics_all(database, success_string, lower_record_limit, upper_record_limit):
    win_record_number = database.cursor.execute("SELECT Count(*) FROM log WHERE result_of_generation=? AND generation_number>=? AND generation_number<?", (success_string, lower_record_limit, upper_record_limit)).fetchone()[0]
    return win_record_number

def create_record_table(database):
    database.cursor.execute("CREATE TABLE records (state_int int PRIMARY KEY, turn_left int, turn_right int, move_forward int, move_backward int, move_left int, move_right int, fire_projectile int)")
    database.robot_memory.commit()

def create_log_table(database):
    try:
        database.cursor.execute("CREATE TABLE log (date_string_finished text, generation_number int, moves_this_generation int, result_of_generation text)")
        database.robot_memory.commit()
    except sqlite3.OperationalError:
        return

def insert_record(state_int, database):
    database.cursor.execute("INSERT INTO records (state_int, turn_left, turn_right, move_forward, move_backward, move_left, move_right, fire_projectile) VALUES (?,?,?,?,?,?,?,?)", (state_int, 0,0,0,0,0,0,0))
    database.robot_memory.commit()

def save_log(generation_number, moves_this_generation, result_string, database):
    database.cursor.execute("INSERT INTO log (date_string_finished, generation_number, moves_this_generation, result_of_generation) VALUES (?,?,?,?)", (time.strftime('%c'), generation_number, moves_this_generation, result_string))
    database.robot_memory.commit()

def update_record(record_map, state_int, database):
    database.cursor.execute("UPDATE records SET turn_left=?, turn_right=?, move_forward=?, move_backward=?, move_left=?, move_right=?, fire_projectile=? WHERE state_int=?", (record_map['turn_left'], record_map['turn_right'], record_map['move_forward'], record_map['move_backward'], record_map['move_left'], record_map['move_right'], record_map['fire_projectile'], state_int))
    database.robot_memory.commit()