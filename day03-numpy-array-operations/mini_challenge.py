import numpy as np

print("Student Marks")

array = np.array([
    [85, 78, 92],
    [90, 88, 95],
    [76, 81, 84]
])

print("Highest Marks : ", np.max(array))
print("Lowest Marks : ", np.min(array))
print(f"Average Marks : {np.mean(array):.2f}")
print("Average of each student : ", np.round(np.mean(array, axis=1),2))
print("Average of each subject : ", np.round(np.mean(array, axis=0), 2))
print("Added 5 grace marks to each student : \n", array + 5)
print("Second student's marks : ", array[1,:])
print("Third subject marks : ", array[:,2])