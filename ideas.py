import pytest

from gradecalc import Course

Grades(
    weights = {'homework', }
)

# Case: class with no weights
english_40b = Course(
    grades = [0.9, 0.55, 0.65],
    drops = 2, # Look! A need for categories without wights
        # Goal: be able to say 3 drops for hw only
    future_grades = [0.95], # This should be a grade object in itself
        # Goal: make grade joins
        #OR future_grades = 3
)
# Analysis: averager with drops
# Behind the scenes:
grade ~ value, drop or Grades, drop
past = Grades([grade, grade, grade], drops)
future = Grades([grade], drops)
eng_40b = Grades.join([past, future])

# Case: class with categories without weights
psych_10a = Course(
    categories = ['homework', 'final'],
    grades = {
        'homework': [(9,10), (10,10), (8,10)],
        'final': [(19,20)],
    },
    drops = {
        'homework': 1,
    }
)
# Analysis: weighted averager with total points as weights,
#    on top of weighted averager with points as weights and drops
# Behind the scenes:
grade ~ value and weight
hw = Grades([grade, grade, grade], drops = 1)
final = Grade(19, 20)
psych_10a = Grades.join(hw, final)
    #Grades.join merely joins the grade lists, after drops
    #Grades.fork partitions into distinct categories with separate weights
    #Idea: both could be an implementation of the Grades constructor

# Idea: drops is an operation applied to grades
# Idea: future grades is a Grades with expected values filled in

# Goal
grades = grades1.merge(grades2) # Add future grades for calculations

# Idea: tree structure
# subnodes are also grade objects
# hw - list of items, averaged, w drops,
# course - dict of items, weighted
# Problem: this exposes the inner workings to user
# Goal: keep library as clean and efficient as possible
# But: maybe under the hood it can do this!

### Under the Hood ###
# Parent Class: Grades
# Subclasses: AveragedGrades, WeightedGrades

# Idea: All grades are just categories with weights
# Support: even hw is lots of cats with weights of their score