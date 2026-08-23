# Given an array containing 1 to 10, print the first five elements, every second element
# and last three elements.

import numpy as np
given = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr = np.array(given)
five = arr[0:5]
second = arr[0:10:2]
three = arr[7:10]
print("ndarray is:", arr)
print("First five elements are:", five)
print("Every Second element in the array is listed as follows:", second)
print("The last three elements are:", three)
