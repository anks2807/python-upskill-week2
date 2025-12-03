import numpy as np

# Check if all elements in the array are positive
numbers = np.array([1,2,3,4,5])
output = all(numbers > 0)
print(output)


numbers = np.array([1, 3, 5, 7, 8])
print(any(numbers % 2 == 0))

numbers = np.array([34, 67, 100, 23, 90])
print(any(numbers % 5 == 0))