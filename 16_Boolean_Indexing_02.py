# Given [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], use Boolean indexing to print even numbers,
# odd numbers, and values divisible by 5.

import numpy as np
given = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr = np.array(given)
even = arr % 2 == 0
odd = arr % 2 != 0
print("ndarray is:", arr)
print("Even numbers of the array are as follows:", arr[even])
print("Odd numbers of the array are as follows:", arr[odd])