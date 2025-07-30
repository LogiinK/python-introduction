from src import *

def test_bowling2loses():
    assert bowling2strike("-- -- -- -- -- -- -- -- -- --") == 0

def test_bowling2win():
    assert bowling2strike("-- -- 36 12 -- 81 11 -- -- 22") == 27

def test_bowling2strike():
    assert bowling2strike("X -- 22 12 -- 81 11 -- -- 22") == 32

def test_strike_with_throws_after():
    assert bowling2strike("X 25 22 12 -- 81 11 -- -- 22") == 46