import numpy as np

# b = np.arange(120).reshape(5,4,1,1,2,3)


# #print(b.shape)
# #print(b)
# rng = np.random.default_rng()
# print(rng.random((3,4,2,5), dtype = np.int64))

a = np.arange(30).reshape(5,6)

# print(a[[1,3]])
# print(a[np.ix_([1,3],[2,4])])
a = a[1:4, [2,4]]

print(a)



