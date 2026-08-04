import numpy as np

# Indexing 1D Arrays
arr = np.array([10, 20, 30, 40, 50])

print(arr[0])
print(arr[2])
print(arr[-1])

# Indexing 2D Arrays
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr[0, 1])
print(arr[1, 2])

# Indexing 3D Arrays
arr = np.array([
    [
        [1,2],
        [3,4]
    ],
    [
        [5,6],
        [7,8]
    ]
])

print(arr[0,1,0])
print(arr[1,0,1])

# Array Slicing
arr = np.array([10,20,30,40,50,60])

print(arr[1:4])
print(arr[:3])
print(arr[2:])
print(arr[-4:-1])

# Step slicing
print(arr[::2])
print(arr[1::2])
print(arr[::-1])

# Slicing 2D Arrays
arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(arr[:,1])
print(arr[1,:])
print(arr[0:2,1:])