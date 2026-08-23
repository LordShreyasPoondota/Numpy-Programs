# Given [10, 20, 30, 40, 50], add 10 to every element, multiply every element
# by 3, divide every element by 10, square every element.

import numpy as np
given = [10, 20, 30, 40, 50]
arr = np.array(given)
add = arr + 10
multiply = arr * 3
divide1 = arr / 10
divide2 = arr // 10
square = arr ** 2
print("ndarray is:", arr)
print("Addition of elements by 10 is:", add)
print("Multiplication of elements by 3 is:", multiply)
print("Division of elements by 10 is:", divide1, "---\'True Division\'")
print("Division of elements by 10 is:", divide2, "---\'Floor Division\'")
print("Square of elements is:", square)
