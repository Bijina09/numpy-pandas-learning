# 1. Splitting arrays

import numpy as np


array = np.array([1,2,3,4,5,6])

result = np.array_split(array,3)

print(result[0])
print(result[1])
print(result[2])

result = np.array_split(array,2)

print(result[0])
print(result[1])

result = np.array_split(array,4)

print(result)

# 2. Splitting 2D Arrays

arr = np.array([
    [1,2],
    [3,4],
    [5,6],
    [7,8]
])

print(np.array_split(arr,2))

print(np.array_split(arr,2,axis=1))

# 3. Searching in arrays

arr = np.array([10, 20, 30, 20, 40, 20])

result = np.where(arr == 20)

print(result)

print(arr[result])

# 4. Searching using conditions

print(np.where(arr > 20))

print(np.where(arr % 2 == 0))

# 5. Sorting Arrays

arr = np.array([5, 2, 8, 1, 9, 3])

print(np.sort(arr))

# Strings

names = np.array(["Sita", "Ram", "Hari", "Gita"])

print(np.sort(names))

print(arr)

# 6. Sorting a 2D Array

arr = np.array([
    [3, 1, 2],
    [9, 5, 7]
])

print(np.sort(arr))

print(np.sort(arr, axis=0))

print(np.sort(arr, axis=1))