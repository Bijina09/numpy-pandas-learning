import numpy as np

arr = np.array([5, 10, 15, 20, 25, 30])

print(arr[2]) # 15
print(arr[-1]) # Last element-30
print(arr[:3]) # Print first three elements
print(arr[1::2]) # Print every second element
print(arr[::-1]) # Reverse the array

arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

# Print 8
print(arr[2, 1])
# Print second row
print(arr[1,:])
# Print first column
print(arr[:,0])
# Print last two elements 
print(arr[2,1:])