import pytest

from easygrades import *

def test_1():
    grade = GradeAverage([Grade(5,25), Grade(33,30)])
    assert grade.earned() == 38
    assert grade.max() == 55
    assert grade.calculate_grade() == 38/55