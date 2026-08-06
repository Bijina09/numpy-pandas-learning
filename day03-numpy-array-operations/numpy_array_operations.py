# Indexing

import numpy as np

arr = np.array([10,20,30,40,50])

print(arr[0])
print(arr[2])
print(arr[-1])


# With 2D arrays
arr2 = np.array([
    [1,2,3],
    [4,5,6]
])

print(arr2[0,0])
print(arr2[1,2])
print(arr2[1,1])

# Slicing
print(arr[1:4]) #10 20 30 40
print(arr[:3]) # 10 20 30
print(arr[2:]) #30 40 50 
print(arr[::-1]) # 50 40 30 20 10

# 2D Slicing
print(arr2[:,1]) # 2 5
print(arr2[0,:]) # 1 2 3
print(arr2[:,0:2]) # 1 2 4 5

# Modifying Values

arr[0] = 15
print(arr)

arr2[1,2] = 999
print(arr2)

# Mathematical Operations

a = np.array([1,2,3])

print(a + 5)
print(a - 1)
print(a * 3)
print(a / 2)
print(a ** 2)

# Array-to-array Operations

x = np.array([1,2,3])
y = np.array([4,5,6])

print(x + y)
print(x - y)
print(x * y)
print(x / y)

# Universal Functions

arr = np.array([1,4,9,16])

print(np.sqrt(arr))
print(np.square(arr))
print(np.abs(arr))

# Aggregation Functions

arr = np.array([2,4,6,8,10])

print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))
print(np.std(arr))

# Operations on 2D array

arr = np.array([
    [1,2,3],
    [4,5,6]
])

print(np.sum(arr))
print(np.sum(arr, axis=0))
print(np.sum(arr, axis=1))

print(np.mean(arr, axis=0))
print(np.mean(arr, axis=1))

# axis = 0 => rows, top-to-bottom
# axis = 1 => columns, left-to-right