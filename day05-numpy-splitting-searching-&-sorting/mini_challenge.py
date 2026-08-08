import numpy as np

marks = np.array([
    [85, 72, 90],
    [60, 88, 75],
    [95, 91, 89],
    [70, 65, 80]
])

arr_parts = np.array_split(marks,2)

print("Array Part-1 : \n",arr_parts[0])
print("Array Part-2 : \n",arr_parts[1])

print("\nMarks greater than 90 index: \n",np.where(marks > 90))
print("\nMarks greater than 90 : \n",marks[np.where(marks > 90)])

print("Marks less than 70 : \n",marks[np.where(marks < 70)])

print("\nSorted Marks : \n",np.sort(marks))

print("Sorted marks along axis=0 : \n",np.sort(marks,axis=0))

print("Sorted marks along axis=1 : \n",np.sort(marks, axis=1))