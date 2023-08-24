# Codewars Problems - Revisit to improve time complexity
# ------------------------------------------------
# Question 1: Remove Duplicates from list
# Define a function that removes duplicates from an array of non negative numbers and returns it as a result.

# The order of the sequence has to stay the same.

# Examples:

# Input -> Output
# [1, 1, 2] -> [1, 2]
# [1, 2, 1, 1, 3, 2] -> [1, 2, 3]

# My original answer:

def distinct(seq):
# remove duplicates from list
# create an empty list
    a_list = []

    for number in seq:
        if a_list.count(number):
            continue
        else:
            a_list.append(number)
    return a_list
print(distinct([1, 1, 2]))
# time complexity - O(n^2)

# Refactored solution

# remove duplicates from list
# create an empty list
def distinct(seq):
    new_list= []
    
    #run a for loop
    for numbers in seq:
        if numbers not in new_list:
            new_list.append(numbers) # if numbers aren't appended to new list then add them
    return new_list
print(distinct([1, 1, 2]))
# time complexity - O(n) - the if statement doesn't use the .count() method so it reduces the time


# -----------------------------------------
# Question 2: Quarter of the year
# Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.
# For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.
# Constraint:

# 1 <= month <= 12

# My original answer:
def quarter_of(month):
    # your code here
    if month<=3:
        return 1
    elif month<=6:
        return 2
    elif month<=9:
        return 3
    else:
        return 4
print("The quarter of chosen month is:")
print(quarter_of(12))
#time complexity - O(1)

# Refactored answer:
def quarter_of(month):
    return (month + 2) // 3 # month + 2 determines the quarter based on the month's position within the quarter 
print("The quarter of chosen month is:")
print(quarter_of(12))
# time complexity - O(1) - it's the same as the other one. I picked this because I wanted to see if using fewer lines of code would actually make it more efficient.


# -----------------------------------------
# Question 3 : Beginner Series #3 Sum of Numbers

# Given two integers a and b, which can be positive or negative, 
# find the sum of all the integers between and including them and return it. 
# If the two numbers are equal return a or b.

# Note: a and b are not ordered!

# Examples (a, b) --> output (explanation)
# (1, 0) --> 1 (1 + 0 = 1)



# My original answer:
def get_sum(a, b):
    if a == b: 
        return a

    total = 0
    small, big = sorted([a,b])

    for i in range(small,big + 1):
        for j in range(small, big + 1):
            total= total + i + j

print(get_sum(0,1))
# time complexity O(n ^2) there is a nested for loop and it causes this to run slower

# Refactored answer:

def get_sum(a, b):
    if a == b:  # edge case
        return a
    
    small, big = sorted([a, b])
    total = 0
    for i in range(small, big + 1):
        total = total + i  # Adding each number to the total
    
    return total
print(get_sum(0,1))

# time complexity O(n) - since there is only 1 for loop this code will run faster


