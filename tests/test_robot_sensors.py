#! usr/bin/env python

import os, sys, random
parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)

from application import robot_sensors

def test_compass_direction_1():
    assert robot_sensors.get_target_compass_direction(4, 5, 4, 7) == 360

def test_compass_direction_2():
    assert robot_sensors.get_target_compass_direction(8, 12, 10, 12) == 90

def test_compass_direction_3():
    assert robot_sensors.get_target_compass_direction(8, 11, 11, 12) == 72

def test_compass_direction_4():
    assert robot_sensors.get_target_compass_direction(14, 11, 11, 12) == 288

def test_compass_direction_5():
    assert robot_sensors.get_target_compass_direction(14, 11, 12, 9) == 225

def test_compass_direction_6():
    assert robot_sensors.get_target_compass_direction(9, 13, 13, 8) == 142

def test_compass_direction_7():
    assert robot_sensors.get_target_compass_direction(9, 9, 10, 10) == 45

def test_facing_offset_1():
    assert robot_sensors.get_direction_facing_offset('north', 360) == 360

def test_facing_offset_2():
    assert robot_sensors.get_direction_facing_offset('east', 360) == 270

def test_facing_offset_3():
    assert robot_sensors.get_direction_facing_offset('south', 90) == 270

def test_facing_offset_4():
    assert robot_sensors.get_direction_facing_offset('west', 90) == 180

def test_facing_offset_5():
    assert robot_sensors.get_direction_facing_offset('north', 72) == 72

def test_facing_offset_6():
    assert robot_sensors.get_direction_facing_offset('east', 72) == 342

def test_facing_offset_7():
    assert robot_sensors.get_direction_facing_offset('south', 288) == 108

def test_facing_offset_8():
    assert robot_sensors.get_direction_facing_offset('west', 288) == 18

def test_facing_offset_9():
    assert robot_sensors.get_direction_facing_offset('north', 142) == 142

def test_facing_offset_10():
    assert robot_sensors.get_direction_facing_offset('east', 142) == 52

def test_facing_offset_11():
    assert robot_sensors.get_direction_facing_offset('south', 45) == 225

def test_facing_offset_12():
    assert robot_sensors.get_direction_facing_offset('west', 45) == 135

def test_direction_buckets_1():
    assert robot_sensors.get_direction_in_buckets(360) == 360

def test_direction_buckets_2():
    assert robot_sensors.get_direction_in_buckets(90) == 90

def test_direction_buckets_3():
    assert robot_sensors.get_direction_in_buckets(72) == 68

def test_direction_buckets_4():
    assert robot_sensors.get_direction_in_buckets(288) == 293

def test_direction_buckets_5():
    assert robot_sensors.get_direction_in_buckets(142) == 158

def test_direction_buckets_6():
    assert robot_sensors.get_direction_in_buckets(45) == 45

def test_direction_buckets_7():
    assert robot_sensors.get_direction_in_buckets(255) == 248

def test_direction_buckets_8():
    assert robot_sensors.get_direction_in_buckets(21) == 23

def test_direction_buckets_9():
    assert robot_sensors.get_direction_in_buckets(113) == 113

def test_direction_buckets_10():
    assert robot_sensors.get_direction_in_buckets(59) == 68

def test_direction_buckets_11():
    assert robot_sensors.get_direction_in_buckets(231) == 248

def test_direction_buckets_12():    
    assert robot_sensors.get_direction_in_buckets(150) == 158
    
def test_direction_buckets_13():
    assert robot_sensors.get_direction_in_buckets(345) == 338

def test_border_touching_1():
    assert robot_sensors.get_border_touching_index(1, 0, 'north', 15, 15) == '0010' #ew, ns

def test_border_touching_1_2():
    assert robot_sensors.get_border_touching_index(0, 1, 'north', 15, 15) == '0001' #ew, ns

def test_border_touching_2():
    assert robot_sensors.get_border_touching_index(0, 0, 'west', 15, 15) == '1001'

def test_border_touching_2_2():
    assert robot_sensors.get_border_touching_index(0, 10, 'west', 15, 15) == '1000'

def test_border_touching_3():
    assert robot_sensors.get_border_touching_index(0, 1, 'south', 15, 15) == '0100'

def test_border_touching_4():
    assert robot_sensors.get_border_touching_index(0, 13, 'east', 15, 15) == '0010'

def test_border_touching_4_2():
    assert robot_sensors.get_border_touching_index(0, 14, 'east', 15, 15) == '0011'

def test_border_touching_5():
    assert robot_sensors.get_border_touching_index(0, 14, 'north', 15, 15) == '1001'

def test_border_touching_6():
    assert robot_sensors.get_border_touching_index(1, 14, 'west', 15, 15) == '0100'

def test_border_touching_7():
    assert robot_sensors.get_border_touching_index(13, 14, 'south', 15, 15) == '0010'

def test_border_touching_8():
    assert robot_sensors.get_border_touching_index(14, 14, 'east', 15, 15) == '1001'

def test_border_touching_9():
    assert robot_sensors.get_border_touching_index(14, 13, 'north', 15, 15) == '0100'

def test_border_touching_10():
    assert robot_sensors.get_border_touching_index(13, 13, 'west', 15, 15) == '0000'

def test_border_touching_11():
    assert robot_sensors.get_border_touching_index(1, 13, 'south', 15, 15) == '0000'

def test_border_touching_12():
    assert robot_sensors.get_border_touching_index(1, 1, 'east', 15, 15) == '0000'

def test_border_touching_13():
    assert robot_sensors.get_border_touching_index(13, 1, 'north', 15, 15) == '0000'

def test_target_next_to_1():
    assert robot_sensors.get_target_next_to_index(3, 3, 3, 4) == 1

def test_target_next_to_2():
    assert robot_sensors.get_target_next_to_index(3, 3, 4, 4) == 1

def test_target_next_to_3():
    assert robot_sensors.get_target_next_to_index(3, 3, 4, 5) == 0

def test_target_next_to_4():
    assert robot_sensors.get_target_next_to_index(3, 3, 3, 5) == 0

def test_target_next_to_5():
    assert robot_sensors.get_target_next_to_index(2, 7, 2, 2) == 0

def test_target_next_to_6():
    assert robot_sensors.get_target_next_to_index(2, 7, 2, 9) == 0

def test_target_next_to_7():
    assert robot_sensors.get_target_next_to_index(2, 7, 2, 8) == 1

def test_target_next_to_8():
    assert robot_sensors.get_target_next_to_index(2, 7, 2, 6) == 1

def test_target_next_to_9():
    assert robot_sensors.get_target_next_to_index(2, 7, 6, 6) == 0