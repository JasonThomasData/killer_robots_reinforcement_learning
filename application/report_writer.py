from application import robot_memory
import math

def get_wins_percentage(wins_this_interval, record_number_per_interval):
    if record_number_per_interval != 0:
        return wins_this_interval / record_number_per_interval * 100
    return 0

def get_statistics_within_record_limit(database, success_string, lower_record_limit, record_number_per_interval):
    upper_record_limit = lower_record_limit + record_number_per_interval
    wins_this_interval = robot_memory.retreive_statistics_all(database, success_string, lower_record_limit, upper_record_limit)
    wins_percentage = get_wins_percentage(wins_this_interval, record_number_per_interval)
    print('%s,%.2f' %(lower_record_limit, wins_percentage))

def make_report(database, success_string):
    _, total_record_number = robot_memory.retreive_statistics_total(database, success_string)
    intervals_to_display = 25
    record_number_per_interval = int(math.floor(total_record_number / intervals_to_display))
    print('~~~')
    print('record_limit, win_record_percentage')
    for i in range(intervals_to_display):
        lower_record_limit = (i) * record_number_per_interval
        get_statistics_within_record_limit(database, success_string, lower_record_limit, record_number_per_interval)