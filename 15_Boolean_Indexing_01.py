# Given [5, 12, 8, 20, 3, 15, 4, 15, 7, 22, 9, 13], print values greater than 10 and
# values less than 10, DO NOT PRINT VALUES EQUAL TO 10.

import numpy as np
given = [5, 12, 8, 20, 3, 15, 4, 15, 7, 22, 9, 13]
arr = np.array(given)
mask_greater = arr > 10
mask_lesser = arr < 10
print("ndarray is:", arr)
print("Values which are Greater than 10 are listed as follows:", arr[mask_greater])
print("Values which are Less than 10 are listed as follows:", arr[mask_lesser])