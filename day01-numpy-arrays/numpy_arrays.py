import numpy as np

# Checking version
print(np.__version__)

# 1. NumPy Creating Arrays
    # We can create a NumPy ndarray object by using the array() function.

#Int
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))

#Float
arr_float = np.array([2.75,2.56,1.99])
print(arr_float)
print(type(arr_float))

#String
arr_string = np.array(["Ram", "Hari", "Sita"])
print(arr_string)
print(type(arr_string))

#Boolean
arr_bool = np.array([True, False])
print(arr_bool)
print(type(arr_bool))

# 2. dimensions in Arrays

#0-D Arrays

arr_0D = np.array(32)
print(arr_0D)

#1-D Arrays (Uni-dimensional) (Vector)

arr_1D = np.array([1,2,3,4,5])
print(arr_1D)

#2-D Arrays (Matrix)

arr_2D = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])
print(arr_2D)

#3-D Arrays (Tensor)

arr_3D = np.array([
        [[1,3,5], [7,9,11]],
        [[2,4,6], [8,10,12]]
])

print(arr_3D)

#Checking number of dimensions

print(arr_0D.ndim)
print(arr_1D.ndim)
print(arr_2D.ndim)
print(arr_3D.ndim)

#Higher dimensional Arrays

arr_higher_Dimen = np.array([1,2,3,4], ndmin=5)
print(arr_higher_Dimen)
print("Number of dimensions :", arr_higher_Dimen.ndim)

# 3. Array Attributes

print("Dimension : ", arr_0D.ndim) #Tells the dimension 
print("Shape : ", arr_0D.shape) #Elements in each dimensions
print("Size : ", arr_0D.size) #Total number of elements
print("Data Type: ", arr_0D.dtype) #int64 for numpy

print("Dimension : ", arr_1D.ndim)
print("Shape : ", arr_1D.shape)
print("Size : ", arr_1D.size)
print("Data Type: ", arr_1D.dtype)

print("Dimension : ", arr_2D.ndim)
print("Shape : ", arr_2D.shape)
print("Size : ", arr_2D.size)
print("Data Type: ", arr_2D.dtype)

print("Dimension : ", arr_3D.ndim)
print("Shape : ", arr_3D.shape)
print("Size : ", arr_3D.size)
print("Data Type: ", arr_3D.dtype)

print("Dimension : ", arr_higher_Dimen.ndim)
print("Shape :", arr_higher_Dimen.shape)
print("Size : ", arr_higher_Dimen.size)
print("Data Type : ", arr_higher_Dimen.dtype)

# 4. Specify Data Type

arr_int_dataType = np.array([1,2,3,4], dtype=np.int32)
print(arr_int_dataType)

arr_float_dataType = np.array([1,2,3,4], dtype=np.float64)
print(arr_float_dataType)

arr_bool_dataType = np.array([1,2,3,False], dtype=np.bool_)
print(arr_bool_dataType)

# 5. Special Arrays

#Array of Zeros
arr_zeros = np.zeros(5)
print(arr_zeros)

#Array of Ones
arr_ones = np.ones(5)
print(arr_ones)

#start,stop
arr_arange = np.arange(1,21)
print(arr_arange)

#start,stop,num (no. of samples to generate)
#Does not exclude the stop value
arr_linspace = np.linspace(1,2,3)
print(arr_linspace)