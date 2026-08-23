# Given [10, 20, ..., 90, 100], print the first element, las element, second and fourth
# elements together and all elements excluding the first and the last.

import numpy as np
given = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
arr = np.array(given)
first = arr[0]
last = arr[9]
second = arr[1]
fourth = arr[3]
slice = arr[1:9]
reverse = arr[::-1]
print("ndarray is:", arr)
print("First Element is:", first)
print("Last Element is:", last)
print("Second and Fourth Elements are:", second,",", fourth, "respectively.")
print("Slice of the array is:", slice)
print("Reverse of the ndarray is:", reverse)