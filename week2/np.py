import numpy as np

b = np.arange(120).reshape(5,4,1,1,2,3)


#print(b.shape)
#print(b)
rng = np.random.default_rng()
print(rng.random((3,4,2,5), dtype = np.int64))
