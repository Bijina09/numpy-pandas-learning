import numpy as np

numbers = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

print("Original Array : ", numbers)
reshaped = numbers.reshape(3,4)
print("Reshaped into (3 x 4) : ", reshaped)
print("Reshaped into (4 x 3) : ", numbers.reshape(4,3))

print("Flattened (3 x 4) : ", reshaped.flatten())

print("Each row in (3 x 4) : ")
for row in reshaped:
  print(row)

a = np.array([1,2,3])
b = np.array([4,5,6])

print("Concatenated : ",np.concatenate((a,b)))
print("Stack : ",np.stack((a,b)))
print("VStack : ",np.vstack((a,b)))
print("Hstack : ",np.hstack((a,b)))