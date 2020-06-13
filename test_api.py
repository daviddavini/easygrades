'''Goal tests to pass when project is complete.
Focuses on user experience instead of inner workings.'''

import pytest
from easygrades import *

def test_list():
   phil_45 = Course(grades = [0.90, 0.87, 0.95, 0.98])
   assert phil_45.grade() == (0.9 + 0.87 + 0.95 + 0.98) / 4

def test_weights():
    math_131bh = Course(
        weights = {'hw': 0.30, 'quiz': 0.30, 'final': 0.4}, 
        grades = {
            'hw': [0.95, 0.8],
            'quiz': [1, 0.9],
            'final': [0.3],
        }
    )
    assert math_131bh.grade() == 0.3 * (0.95+0.8)/2 + 0.3 * (1+0.9)/2 + 0.4*0.3

def test_drops():
    cs_31 = Course(grades = [0.9, 0.8, 0.2], drops = 2)
    assert cs_31.grade() == (0.9 + 0.8) / 2

def test_weights_and_drops():
    econ_12 = Course(
        weights = {'reading': 0.5, 'exams': 0.5},
        grades = {
            'reading': [1, 1, 0],
            'exams': [0.9, 0.8],
        },
        drops = {
            'reading': 1,
        }
    )
    assert econ_12.grade() == 0.5*(1) + 0.5*(0.85)

