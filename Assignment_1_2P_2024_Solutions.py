# Assignment 1.2P Solutions - 2024 Programming in Psychological Science
#
# Record of Revisions
#
# Date            Programmer              Descriptions of Change
# ====         ================           ======================
# 07-Jan-24 Leonhard Volz & Michael Nunez     Original code

# Q1.2P.1 ----------------------------------------------------------------------

def Q1_2P_1():

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

# Q1.2P.3 ----------------------------------------------------------------------
if False:  # we do not want to execute this in python when running the script 
    %paste  # does not work in a python script
            # it is only defined for iPython terminal execution
            #
            # in native Python, `%` is the modulo operator 

# Q1.2P.4 ----------------------------------------------------------------------
if False:  # we do not want to execute this in python when running the script 
    # to change the working directory: 
    %cd "your directory" 
    # print the current working directory: 
    %pwd
    # list the contents of the working directory: 
    %ls
    # list current workspace variables: 
    %who   # variable names
    %whos  # objects with additional information

# Q1.2P.5 ----------------------------------------------------------------------
if False:  # we do not want to execute this in python when running the script 
    pip install pip-install-test   # using your terminal
    %pip install pip-install-test  # using the iPython console

# Q1.2P.6 ----------------------------------------------------------------------
sample_scores = np.array([1, 6, 7, 8, 9, np.nan])
np.nanvar(sample_scores)  # calculates the variance while ignoring nan values

# often, numeric python packages have separate (convenience) functions for 
# operations that in R would be specified by additional arguments

# Q1.2P.7 ----------------------------------------------------------------------
# valid solution #1 - directly fill array with np.nan
nan_array = np.full((4,3,5), np.nan) 

# valid solution #2 - create empty array & fill with np.nan in second step
nan_array2 = np.empty((4,3,5)) 
nan_array2[:] = np.nan

# Q1.2P.8 ----------------------------------------------------------------------
file = 'EuroNumbers_data.csv'  # or complete location string
data_dict = pd.read_csv(file, sep=';').to_dict()
data_dict.keys()    # returns the keys
# data_dict.values()  # returns the values
# data_dict.items()   # returns a list of all key:value pairs

# Q1.2P.9 ----------------------------------------------------------------------
np.random.seed(1234)  # Set the random seed
speed_sec = np.zeros(10)
sim_speed = np.random.uniform(size=5)  # Speed simulation in seconds
speed_sec[0:5] = sim_speed * np.random.uniform(low=0.5, high=10, size=5)
speed_sec[5:10] = sim_speed

language = np.repeat(np.array(['R', 'Python']), 5)

code_type = np.char.add(np.array(['forloop'] * 5), np.arange(1,6).astype(str))
code_type = np.tile(code_type, 2)

all_data = {"language" : language, 
           "code_type" : code_type,
           "speed" : speed_sec} 
my_data = pd.DataFrame(all_data)
print(my_data)

# Q1.2P.10 ---------------------------------------------------------------------
# 4 stars!
# It was better than the R self assessment. 
# I liked that I needed to run multiple choice answers. 
# I learned how to use import os.
# 92.86% (13/14)