# Day 4 NumPy Reshaping & Joining Arrays

import numpy as np

arr = np.array([1,2,3,4,5,6])

print(arr)
print(arr.shape)

# Now reshaping

reshaped = arr.reshape(2,3)

print(reshaped)
print(reshaped.shape)

print(arr.reshape(3,2))
print(arr.reshape(6,1))

#Invalid
#print(arr.reshape(2,2))

# Flattening
# COnvert a multidimentional array back to one dimention

arr_2d = np.array([
    [1,2,3],
    [4,5,6]
])

print(arr_2d.flatten())

print(arr_2d.ravel())

# 3 Iterating through arrays

arr = np.array([10,20,30,40])

for value in arr:
  print(value)

arr = np.array([
    [1,2,3],
    [4,5,6]
])

for row in arr:
  print(row)

for row in arr:
  for value in row:
    print(value)

# 4 Joining Arrays

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

result = np.concatenate((arr1,arr2))

print(result)

# 5 Joining 2D Arrays

arr_2D_1 = np.array([
    [1,2,3],
    [4,5,6]
])

arr_2D_2 = np.array([
    [10,20,30],
    [40,50,60]
])

result_2D = np.concatenate((arr_2D_1, arr_2D_2))

print(result_2D)

# Stacking

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print(np.stack((arr1,arr2)))

print(np.vstack((arr1,arr2)))
print(np.hstack((arr1,arr2)))

