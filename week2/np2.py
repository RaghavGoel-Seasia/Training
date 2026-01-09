import numpy as np

list1 = list(range(9))

print(list1)

array1 = np.asarray(list1, dtype = np.int32)
array2 = np.fromiter(list1, dtype = np.int32)

print(array1)
print(array2)