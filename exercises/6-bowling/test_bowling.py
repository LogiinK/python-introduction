from src import *

def test_bowling2loses():
    assert bowling2strike("-- -- -- -- -- -- -- -- -- --") == 0

def test_bowling2win():
    assert bowling2strike("-- -- 36 12 -- 81 11 -- -- 22") == 27

def test_bowling2strike():
    assert bowling2strike("X -- 22 12 -- 81 11 -- -- 22") == 32

def test_strike_with_throws_after():
    assert bowling2strike("X 25 22 12 -- 81 11 -- -- 22") == 46

def test_strike_perfect_with_throws_after():
    assert bowling2strike("X X X X X X X X X X X X") == 300

def test_spare_with_throws_after():
    assert bowling2strike("X 25 2/ -- 9/ 11 -- -- 26") == 56

def test_spare_perfect_with_throws_after2():
    assert bowling2strike("X X X X X 3/ 2/ 4/ 3/ 2/ 3") == 197