#! usr/bin/env python

import os, sys, random
parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)

from application import win_lose_conditions

def test_target_reached_1():
    assert win_lose_conditions.target_reached(1, 1, 1, 1) == True

def test_target_reached_2():
    assert win_lose_conditions.target_reached(1, 2, 2, 1) == False

def test_target_reached_3():
    assert win_lose_conditions.target_reached(3, 1, 1, 3) == False

def test_target_reached_4():
    assert win_lose_conditions.target_reached(4, 7, 4, 7) == True

def test_target_reached_5():
    assert win_lose_conditions.target_reached(3, 2, 3, 2) == True

def test_target_reached_6():
    assert win_lose_conditions.target_reached(-3, 2, 3, 2) == False

def test_target_reached_7():
    assert win_lose_conditions.target_reached(3, -2, 3, 2) == False

def test_target_destroyed_1():
    assert win_lose_conditions.target_destroyed(4) == False

def test_target_destroyed_2():
    assert win_lose_conditions.target_destroyed(2) == False

def test_target_destroyed_3():
    assert win_lose_conditions.target_destroyed(0) == True

def test_target_destroyed_4():
    assert win_lose_conditions.target_destroyed(-2) == True

def test_fell_off_1():
    assert win_lose_conditions.fall_off_test_area(4, 4, 11, 11) == False

def test_fell_off_2():
    assert win_lose_conditions.fall_off_test_area(0, 0, 15, 15) == False

def test_fell_off_3():
    assert win_lose_conditions.fall_off_test_area(14, 14, 15, 15) == False

def test_fell_off_4():
    assert win_lose_conditions.fall_off_test_area(5, 15, 15, 15) == True

def test_fell_off_5():
    assert win_lose_conditions.fall_off_test_area(5, -1, 15, 15) == True