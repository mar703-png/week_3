#################### PROBLEM 1: Basic Arithmetic & Order of Operations ####################
# Task 1: Using the order of operations (PEMDAS/BODMAS), evaluate the following expression:
# 3 + 6 * (5 + 4) / 3 - 7. Print the result.

# Task 2: Calculate the remainder when 145 is divided by 12 using modulo and print the result.

# Task 3: Raise 7 to the power of 3 and print the result.

#################### PROBLEM 2: Working with Functions ####################
# Task 4: Given a list of numbers:
# ### numbers = [23, 89, 12, 54, 92, 65, 71, 13, 45]
# Use the max() and min() functions to find the highest and lowest number respectively.

# Task 5: Round the number 12.5678 to 2 decimal places.

# Task 6: Find the absolute value of -45.

#################### PROBLEM 3: Advanced Math Functions ####################
from math import *

# Task 7: Using the math library, find the floor value of 15.7.

# Task 8: Find the ceiling value of 15.2.

# Task 9: Calculate the square root of 625.

#################### PROBLEM 4: Problem Solving ####################
# Task 10: You are given two lists:
# ##### prices = [34.56, 45.78, 23.89, 12.34, 78.90]
# quantities = [3, 5, 2, 4, 6]
# Calculate the total cost for each item (price multiplied by quantity).
# Then, find the average cost of all items after rounding it to 2 decimal places.

#################### END OF ADVANCED PROBLEM SET  -- end Bell Ringer  ####################

# print(3 + 6 * (5 + 4) / 3 - 7) # Task 1

# print (145 % 12) # Task 2

# print( 7 ** 3) # Task 3

# print (max(23, 89, 12, 54, 92, 65, 71, 13, 45))
# print (min(23, 89, 12, 54, 92, 65, 71, 13, 45)) # Task 4

# num = 12.5678
# rounded_num = round(num, 2) 
# print(rounded_num)   # Task 5

# print(abs(-45)) # Task 6

# print (floor(15.7)) # Task 7

# print(ceil(15.2)) # Task 8

# print(sqrt(625)) # Task 9

numbers = (34.56 * 3, 45.78 * 5, 23.89 * 2, 12.34 * 4, 78.90 * 6)

average = sum(numbers)/len(numbers)

print("Average of list: ", round(average,2)) # Task 10