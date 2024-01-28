# Assignment 3.2P Cheat Solution - 2024 Programming in Psychological Science
#
# Record of Revisions
#
# Date            Programmer              Descriptions of Change
# ====         ================           ======================
# 28-Jan-24      Marcell Völler                Original code


# Q3.2P.9 ----------------------------------------------------------------------


def cheat(assignment_number, question_number):
    while assignment_number not in [1, 2]:
        assignment_number = input("This assignment is not available (yet). Try using 1 or 2!")
    if assignment_number == 1:
        available_questions = [1, 2]
        while question_number not in available_questions:
            question_number = input("This question is not available (yet). Try using {}".format(available_questions))
        if question_number == 1:
            print("""
# Q1.2P.1 ----------------------------------------------------------------------

import numpy as np  # imports the `numpy` module with the alias `np`

import pandas as pd # generally you would put all import statements at the top
                    # of the script - enables, e.g., easy installation of all
                    # relevant packages

another_array = np.zeros((2, 4, 6))

# valid solution #1 - indexes the single element
print(another_array[-1, 0, 2])

# valid solution #2 - subsets the full dimension
print(another_array[:, 0, :])
print(another_array[:, :, 2])
print(another_array[-1, :, :])

# Generally, remember that Python (in contrast to R)
#     - is zero-indexed (indices go from 0 to (n-1))
#     - negative indices "invert" the access instead of deselection
#     - you need to indicate fully indexed dimensions with a colon

            """)
        elif question_number == 2:
            print("""
# Q1.2P.2 ----------------------------------------------------------------------
another_array = np.zeros((2, 4, 6))
new_array = another_array.copy() 
# alternatively: new_array = np.copy(another_array)
new_array[1, 2, 2] = 1
print(f"another: '{another_array[1, 2, 2]}' vs. new: '{new_array[1, 2, 2]}'")

# In Python, when using =, we only assign a reference to an object in memory,
# so both new_array and another_array are pointing to the same memory
# allocation, namely, the one created by np.zeros(). To make a true copy, you
# can use the .copy() method or np.copy().

            """)
    if assignment_number == 2:
        available_questions = [5]
        while question_number not in available_questions:
            question_number = input("This question is not available (yet). Try using {}".format(available_questions))

        if question_number == 5:
            print("""
# Q5 --------------------------------------------------------------------------
# answer derived from a student:
# With a class, one can create a new type of object. One can create attributes for this object,
# like variables and functions which can be performed on it. It is also possible to
# create new variables that are assigned to this class.
# Read more: https://docs.python.org/3/tutorial/classes.html

# Complex number class
class ComplexNum:
    "Creates a complex number"
    numtype = 'complex'

    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def vec_length(self):
        return np.sqrt(self.r ** 2 + self.i ** 2)

    def phase_angle(self):
        return np.arctan2(self.i, self.r) * 180 / np.pi # np.arctan() may not choose the correct quadrant


my_num = ComplexNum(3.0, 4.0)
print(my_num)
print((my_num.r, my_num.i))
print(my_num.numtype)
print(my_num.vec_length())
print(my_num.phase_angle())

                """)

