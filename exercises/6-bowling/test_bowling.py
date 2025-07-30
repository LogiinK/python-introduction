from src import *

def test_bowling2loses():
    assert bowling2loses("-- -- -- -- -- -- -- -- -- --") == 0

def test_bowling2win():
    assert bowling2win("-- -- 57 12 -- 82 11 -- -- 22") == 31

#def test_bowling2strike():
#    assert bowling2strike("X -- 57 12 X 82 11 -- -- 22") == 59