# ==============================================================================
# ===  Assignment 2.2 Solutions - 2023 Programming in Psychological Science  ===
# ==============================================================================
#
# ===== Record of Revisions =====
# Date      |  Programmer   | Descriptions of Change
# ==========|===============|=======================
# 20-Jan-23 | Leonhard Volz | Adaption 2023
# 27-Jan-23 | Michael Nunez | Q3 solution addition
# 30-Feb-23 | Michael Nunez | Adding student solutions
#
# Imports =====================================================================
import numpy as np
import datetime
import time

# Q1 --------------------------------------------------------------------------
# There are a few methods.
# This is a nice method adapted from a student solution
# Note you could also use: from datetime import datetime 
# To make your imports shorter

current_hour = datetime.datetime.now().hour
current_minute = datetime.datetime.now().minute
current_time = int(str(current_hour)+str(current_minute))

print("The current time is:", current_time)
if current_time >= 100 and current_time < 400:
    print("Go to sleep!")
elif current_time >= 800 and current_time < 900:
    print("Eet je hagelslag!")
else:
    print("Gut gemacht!")


# Q2 --------------------------------------------------------------------------
# This is solution from a student.
# Note there was no reason for Michael to put weight_sum = 2*0 in 
# the Assignment2_2P_2023 document.

numeric_vec = np.random.uniform(low=0, high=100, size=4)

weight_sum = 0
for i in range(len(numeric_vec)):
	# This could also be i % 2 == 0 because of an ambiguity with Python indexing at 0
    if (i+1) % 2 == 0: # See modulo operation: https://en.wikipedia.org/wiki/Modulo
        weight_sum = weight_sum + 2*numeric_vec[i]
    else:
        weight_sum = weight_sum + numeric_vec[i]

weight_avg = weight_sum / (np.size(numeric_vec)*1.5)

# Cleverer solution

weight_sum = 0
for i in range(len(numeric_vec)):
    weight_sum = weight_sum + (2 - ((i+1) % 2))*numeric_vec[i]

weight_avg = weight_sum / (np.size(numeric_vec)*1.5)

# Q3 --------------------------------------------------------------------------
# a) This function does not run. Python CAN see global variables in a function.
# However because the line grass = "blue" is in the function, the global variable 
# is not recognized.
# In R this would be possible because the global variable is found even when the 
# variable grass is defined later.
# Read more: https://www.w3schools.com/python/gloss_python_global_variables.asp

# Try this:
grass = "green"
def color_it(color_me, grass_me):
    grass_me = grass
    color_me = "blue"
    # grass = "blue"
    colorful_items = np.array([(color_me, grass_me)])
    return colorful_items

sky = "grey"
ground = "brown"
these_items = color_it(sky, ground)
print(these_items)

# This is an import distinction to know for your exam!

# b)
# Fixed function
grass = "green"

def color_it(color_me, grass_me):
    grass_me = "green"
    color_me = "blue"
    colorful_items = np.array([(color_me, grass_me)])
    return colorful_items

sky = "grey"
ground = "brown"
these_items = color_it(sky, ground)
print(these_items)

# Or just this:
grass = "green"

def color_it(color_me, grass_me):
    return np.array([("green", "blue")])

sky = "grey"
ground = "brown"
these_items = color_it(sky, ground)
print(these_items)


# Q4 --------------------------------------------------------------------------
vec = np.array([1, 2, 3, 3, 4, 5])

def special(vector):
    special_vec = np.array(vector[0])
    for i in range(len(vector)):
        if vector[i] not in special_vec:
            special_vec = np.append(special_vec, vector[i])
    print(special_vec)


special(vec)


# Q5 --------------------------------------------------------------------------
# answer derived from a student:
# With a class, one can create a new type of object. One can create attributes for this object,
# like variables and functions which can be performed on it. It is also possible to
# create new variables that are assigned to this class.
# Read more: https://docs.python.org/3/tutorial/classes.html

# Complex number class
class ComplexNum:
    """Creates a complex number"""
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


# Q6 --------------------------------------------------------------------------
# This one is tricky!
def nthpower(number, n, start = 1., precision = 1e-12):
    if n == 0.:
        return 1.  # 0th power is always 1
    diff = precision * 1e6  # initiate diff to be larger than precision
    conv = 0
    while abs(diff) > precision:
        rate = diff 
        diff = n * (start**(1/n) - number) / (start**(1/n - 1))  # Newton's method
        if abs(rate) >= abs(diff):
            # if the rate of change is not decreasing, throw convergence error
            conv += 1
            if conv > 5:  # for more than 5 iterations
                raise ArithmeticError ("no convergence")
        else:
            conv = 0
        start -= diff
    return start

# Student solution, the last input to the function is optional
"""
Newtons method estimates the root or zero of a function by improving an initial guess iteratively using the derivative of the function.
The function that needs to be set to zero is f(x) = x^(1/n) - number. With n being the power and x being the initial guess.
The derivative for x of this function is f'(x) = x1(1/n-1)/n.
The method below improves the initial guess itereatively by using the formula x_new = x_old - f(x_old)/f'(x_old) until the difference 
between the old and new guess is smaller than a tolerance or until a maximum number of iterations is reached.

The method is not always exact and the initial guess can impact the result. In these cases, the method fails to find a global minimum.
"""

def nthpower(number, n, start = 1):
    if n == 0:
        print("The 0th power of a number is always 1")
        return 1
    guess = start
    i = 1
    tol = 1e-10 # the tolerance defines how close the new guess needs to be to the old guess to stop the iteration
    while i < 10000000: # the maximum number of iterations is set to 10 million
        guess_new = guess - (guess**(1/n)-number)/((guess**(1/n-1)/n)) # the new guess is calculated using the above described formula
        if abs(guess - guess_new) < tol: # if the difference between the old and new guess is smaller than the tolerance, the iteration stops
            return round(guess_new, 5)
        guess = guess_new 
        i += 1
    return round(guess, 5) # if the maximum number of iterations is reached, the last guess is returned

print(f"My function calculates: {nthpower(2, 0)}, the correct answer is: {2**0}")
print(f"My function calculates: {nthpower(2, 1, 2)}, the correct answer is: {2**1}")
print(f"My function calculates: {nthpower(2, 2)}, the correct answer is: {2**2}")
print(f"My function calculates: {nthpower(2.5, 3)}, the correct answer is: {2.5**3}")
print(f"My function calculates: {nthpower(2, 3)}, the correct answer is: {2**3}")



# Q7 --------------------------------------------------------------------------
# Solution derived from a student, note that time.perf_counter() has more precision than time.time()
start_time = time.perf_counter()
nthpower(4214, 5)
end_time = time.perf_counter()
duration_nthroot = end_time - start_time
print(duration_nthroot)

start_time = time.perf_counter()
4214 ** (1 / 5)
end_time = time.perf_counter()
duration_base = end_time - start_time
print(duration_base)

# But it is fine if you use time.time(), you would just need to run the code in a loop, like this:
interations = 100000
start_time = time.time()
for i in range(interations):
    nthpower(4214, 5)
duration_nthroot = time.time() - start_time
print(duration_nthroot)

start_time = time.time()
for i in range(interations):
    4214 ** (1 / 5)
duration_base = time.time() - start_time
print(duration_base)


# Q8 --------------------------------------------------------------------------
def prime(n):
    """
    Returns something...
    """
    result = np.zeros(n)
    count = 0
    number = 1
    while(count < n):
        check = True
        number += 1
        for i in range(count):
            if number % result[i] == 0.:
                check = False
                break
        if check:
            result[count] = number
            count += 1
    return result


# Q9 --------------------------------------------------------------------------
if False:
    ?prime
from sequences import prime
if False:
    ?prime


# Q10 --------------------------------------------------------------------------
import os
os.system("py sequences.py")  # or os.system("python sequences.py"), os.system("python3 sequences.py")


# Q11 --------------------------------------------------------------------------
# no poker solution provided, ask for help if you need hints